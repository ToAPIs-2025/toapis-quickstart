"""Minimal ToAPIs chat, image, and video examples using only Python stdlib."""

import argparse
import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

DEFAULT_BASE = "https://toapis.com/v1"


def api_base(value: str) -> str:
    base = value.rstrip("/")
    if not base.startswith("https://"):
        raise ValueError("TOAPIS_BASE_URL must start with https://")
    return base if base.endswith("/v1") else base + "/v1"


def build_request(kind: str, prompt: str, image_model: str = "gpt-image-2-vip", image_quality: str = "low") -> tuple[str, dict]:
    if kind == "chat":
        return "/chat/completions", {
            "model": "gpt-6.1-sol",
            "stream": False,
            "messages": [{"role": "user", "content": prompt}],
        }
    if kind == "image":
        body = {
            "model": image_model,
            "prompt": prompt,
            "size": "1:1",
            "resolution": "1k",
            "n": 1,
            "response_format": "url",
        }
        if image_model == "gpt-image-2-vip":
            body["quality"] = image_quality
        return "/images/generations", body
    if kind == "video":
        return "/videos/generations", {
            "model": "seedance-2",
            "prompt": prompt,
            "duration": 4,
            "size": "16:9",
            "aspect_ratio": "16:9",
            "resolution": "720p",
            "generate_audio": False,
        }
    raise ValueError(f"Unsupported kind: {kind}")


def request_json(method: str, url: str, key: str, payload: dict | None = None) -> dict:
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"Authorization": f"Bearer {key}"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    request = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=60) as response:
            result = json.load(response)
    except HTTPError as exc:
        detail = exc.read(1000).decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc
    if not isinstance(result, dict):
        raise RuntimeError("Expected a JSON object from ToAPIs")
    return result


def result_url(task: dict) -> str | None:
    result = task.get("result")
    if isinstance(result, dict):
        data = result.get("data")
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and isinstance(item.get("url"), str):
                    return item["url"]
    return None


def wait_for_task(base: str, key: str, kind: str, task_id: str,
                  interval: int, max_wait: int) -> dict:
    path = "images" if kind == "image" else "videos"
    url = f"{base}/{path}/generations/{quote(task_id, safe='')}"
    deadline = time.monotonic() + max_wait
    while True:
        task = request_json("GET", url, key)
        status = task.get("status", "unknown")
        print(f"Task {task_id}: {status} ({task.get('progress', 0)}%)", file=sys.stderr)
        if status == "completed":
            return task
        if status == "failed":
            raise RuntimeError(f"Generation failed: {task.get('error', task)}")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(f"Task did not finish within {max_wait} seconds: {task_id}")
        time.sleep(min(interval, remaining))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("chat", "image", "video"))
    parser.add_argument("--prompt", default="Hello from ToAPIs!")
    parser.add_argument("--base-url", default=os.getenv("TOAPIS_BASE_URL", DEFAULT_BASE))
    parser.add_argument("--image-model", choices=("gpt-image-2-vip", "gpt-image-2"),
                        default="gpt-image-2-vip", help="image model; default is the low-cost VIP variant")
    parser.add_argument("--image-quality", choices=("low", "medium", "high"), default="low",
                        help="quality for gpt-image-2-vip only")
    parser.add_argument("--dry-run", action="store_true", help="show the request without using a key or spending credits")
    parser.add_argument("--interval", type=int, default=8, help="seconds between image/video status checks")
    parser.add_argument("--max-wait", type=int, default=900, help="maximum wait for image/video tasks in seconds")
    args = parser.parse_args()
    if args.interval < 1 or args.max_wait < 1:
        parser.error("--interval and --max-wait must be positive")

    base = api_base(args.base_url)
    path, payload = build_request(args.kind, args.prompt, args.image_model, args.image_quality)
    if args.dry_run:
        print(json.dumps({"url": base + path, "body": payload}, indent=2, ensure_ascii=False))
        return 0

    key = os.getenv("TOAPIS_API_KEY")
    if not key:
        parser.error("Set TOAPIS_API_KEY in your environment; never put it in this repository")
    result = request_json("POST", base + path, key, payload)
    if args.kind == "chat":
        choices = result.get("choices") or []
        content = (choices[0].get("message") or {}).get("content") if choices else None
        print(content if content is not None else json.dumps(result, indent=2))
        return 0

    task_id = result.get("id") or result.get("task_id")
    if not task_id:
        raise RuntimeError(f"No task ID in generation response: {result}")
    print(f"Submitted {args.kind} task: {task_id}", file=sys.stderr)
    task = wait_for_task(base, key, args.kind, str(task_id), args.interval, args.max_wait)
    print(json.dumps({"task_id": task_id, "status": task.get("status"),
                      "url": result_url(task), "expires_at": task.get("expires_at")},
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, TimeoutError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
