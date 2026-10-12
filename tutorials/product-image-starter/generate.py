"""Generate ONE GPT Image 2 task, or inspect its request without a key.

Python standard library only. No automatic retry of task submission.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import struct
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen, build_opener, HTTPRedirectHandler

DEFAULT_PROMPT = (
    "Commercial product photography of one unbranded matte orange insulated cup, "
    "with a black lid and a clean cylindrical silhouette, standing on a warm pale "
    "stone plinth. Soft morning light from the left, natural contact shadow, "
    "minimal cream background, accurate product geometry, no text, no logo, "
    "no additional products. Center the full cup in a square composition."
)
EDIT_PROMPT = (
    "Keep the exact orange cup, black lid, silhouette and proportions of the "
    "reference image. Change only the scene to a dark charcoal studio with "
    "a subtle orange rim light and a natural contact shadow. One product, "
    "no extra objects, no text, no logo. Square commercial product photography."
)


def now():
    return datetime.now(timezone.utc).isoformat()


def normalize_base(value):
    u = urlparse(value.rstrip('/'))
    if u.scheme != 'https' or u.netloc not in ('toapis.com', 'toapis.cn'):
        raise ValueError('Use https://toapis.com or https://toapis.cn')
    if u.path not in ('', '/v1') or u.query or u.fragment:
        raise ValueError('Base must contain only the host and optional /v1')
    return f'https://{u.netloc}/v1'


def build_payload(prompt, reference_url=None):
    p = {'model': 'gpt-image-2', 'prompt': prompt, 'size': '1:1',
         'resolution': '1k', 'n': 1, 'response_format': 'url'}
    if reference_url:
        if urlparse(reference_url).scheme != 'https':
            raise ValueError('Reference must be a public HTTPS URL')
        p['reference_images'] = [reference_url]
    return p


def load_key(key_file=None):
    if key_file:
        for line in Path(key_file).read_text(encoding='utf-8-sig').splitlines():
            if line.strip().startswith('TOAPIS_API_KEY='):
                return line.strip().split('=', 1)[1].strip().strip('"\'')
        raise ValueError('Private env file has no TOAPIS_API_KEY')
    key = os.environ.get('TOAPIS_API_KEY', '')
    if not key:
        raise ValueError('Set TOAPIS_API_KEY privately; never put it in this repository')
    return key


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class APIError(RuntimeError):
    def __init__(self, status, retry_after=8):
        super().__init__(f'API HTTP {status}; check model permissions and task logs')
        self.status = status
        self.retry_after = retry_after


def api_json(method, url, key, payload=None, body=None, content_type=None):
    if payload is not None:
        body = json.dumps(payload).encode('utf-8')
        content_type = 'application/json'
    headers = {'Authorization': 'Bearer ' + key}
    if content_type:
        headers['Content-Type'] = content_type
    try:
        with build_opener(NoRedirect()).open(Request(url, data=body, headers=headers, method=method), timeout=90) as r:
            obj = json.loads(r.read(4 * 1024 * 1024))
    except HTTPError as exc:
        try:
            delay = float(exc.headers.get('Retry-After', '8'))
        except ValueError:
            delay = 8
        # Never emit response bodies that might echo a token.
        raise APIError(exc.code, max(8, min(120, delay))) from None
    except URLError:
        raise RuntimeError('Network request failed; inspect the original task before resubmitting') from None
    if not isinstance(obj, dict):
        raise RuntimeError('Expected a JSON object')
    return obj


def upload_image(base, key, path):
    content = Path(path).read_bytes()
    if not content.startswith(b'\x89PNG\r\n\x1a\n') or len(content) > 10_000_000:
        raise ValueError('This minimal example accepts PNG files up to 10 MB')
    boundary = 'toapis-' + hashlib.sha256(content).hexdigest()[:24]
    body = (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="reference.png"\r\n'
            'Content-Type: image/png\r\n\r\n').encode() + content + f'\r\n--{boundary}--\r\n'.encode()
    obj = api_json('POST', base + '/uploads/images', key, body=body,
                   content_type='multipart/form-data; boundary=' + boundary)
    url = (obj.get('data') or {}).get('url')
    if not url:
        raise RuntimeError('Upload returned no public URL')
    return url


def result_url(task):
    for item in (task.get('result') or {}).get('data', []):
        if isinstance(item, dict) and item.get('url'):
            return item['url']
    return task.get('url')


def poll(base, key, task_id, max_wait=900):
    started = time.monotonic()
    history = []
    delay = 8
    lost = 0
    while time.monotonic() - started < max_wait:
        time.sleep(delay)
        try:
            task = api_json('GET', base + '/images/generations/' + quote(task_id, safe=''), key)
            lost = 0
            delay = 8
        except APIError as exc:
            if exc.status in (429, 503, 500, 502, 504):
                lost += 1
                if lost > 5:
                    raise RuntimeError('Repeated status errors; resume by task ID') from None
                delay = max(exc.retry_after, min(64, 8 * (2 ** lost)))
                continue
            raise
        status = task.get('status', 'unknown')
        history.append({'at': now(), 'status': status, 'progress': task.get('progress')})
        if status == 'completed':
            if not result_url(task):
                raise RuntimeError('Completed task has no result URL')
            return task, history
        if status in ('failed', 'error', 'cancelled', 'expired'):
            raise RuntimeError('Task failed; no automatic paid resubmission')
        if status not in ('queued', 'pending', 'submitted', 'in_progress', 'processing', 'running'):
            raise RuntimeError('Unknown task status; inspect the original task')
    raise TimeoutError('Keep the task ID and resume; do not automatically generate again')


def download_png(url):
    if urlparse(url).scheme != 'https':
        raise ValueError('Result must be an HTTPS URL')
    # CDN requests deliberately have no Authorization header.
    with urlopen(Request(url), timeout=60) as r:
        data = r.read(32 * 1024 * 1024 + 1)
    if len(data) > 32 * 1024 * 1024 or not data.startswith(b'\x89PNG\r\n\x1a\n'):
        raise RuntimeError('Expected a PNG result within 32 MB; retain task ID for inspection')
    width, height = struct.unpack('>II', data[16:24])
    return data, [width, height]


def save_json(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--live', action='store_true', help='submit exactly one potentially billable task')
    p.add_argument('--base-url', default=os.getenv('TOAPIS_BASE_URL', 'https://toapis.cn'))
    p.add_argument('--key-file', help='path to a PRIVATE env file; its contents are never printed or copied')
    p.add_argument('--reference', help='local PNG; uploaded only in live mode')
    p.add_argument('--prompt', help='defaults to the original product prompt or reference-edit prompt')
    p.add_argument('--resume', help='query an existing task instead of submitting or uploading')
    p.add_argument('--out', default='output')
    args = p.parse_args()
    base = normalize_base(args.base_url)
    prompt = args.prompt or (EDIT_PROMPT if args.reference else DEFAULT_PROMPT)
    payload = build_payload(prompt)
    if not args.live:
        print(json.dumps({'mode': 'dry-run', 'url': base + '/images/generations', 'body': payload,
                          'reference': 'will upload a local PNG first' if args.reference else None}, indent=2))
        return
    key = load_key(args.key_file)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if (out / 'task.json').exists() and not args.resume:
        raise ValueError('Output already has a task. Use --resume with its ID or choose a new directory')
    started = time.monotonic()
    if args.resume:
        record = {'task_id': args.resume, 'mode': 'resumed', 'checked_at': now()}
        task_id = args.resume
    else:
        if args.reference:
            payload = build_payload(prompt, upload_image(base, key, args.reference))
        record = {'submitted_at': now(), 'request': payload, 'base_url': base, 'mode': 'live'}
        submitted = api_json('POST', base + '/images/generations', key, payload=payload)
        task_id = submitted.get('id') or submitted.get('task_id')
        if not task_id:
            raise RuntimeError('No task ID; check account task logs before submitting another request')
        record['task_id'] = task_id
    save_json(out / 'task.json', record)
    print('Task ID:', task_id, flush=True)
    task, history = poll(base, key, task_id)
    data, pixels = download_png(result_url(task))
    (out / 'result.png').write_bytes(data)
    # Publish only request/task/output facts, never account balance or credentials.
    record.update({'status': 'completed', 'completed_at': now(), 'elapsed_seconds': round(time.monotonic() - started, 2),
                   'history': history, 'actual_pixels': pixels, 'output_sha256': hashlib.sha256(data).hexdigest(),
                   'provider_model': task.get('model'), 'billing': task.get('billing'),
                   'actual_cost_usd': (task.get('billing') or {}).get('cost_usd'), 'output': 'result.png'})
    save_json(out / 'task.json', record)
    print(json.dumps({'status': 'completed', 'pixels': pixels, 'cost_usd': record['actual_cost_usd'],
                      'elapsed_seconds': record['elapsed_seconds']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
