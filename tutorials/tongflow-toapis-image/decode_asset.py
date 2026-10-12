import argparse,base64,json
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('response'); p.add_argument('--output',default='result.png'); a=p.parse_args()
obj=json.loads(Path(a.response).read_text(encoding='utf-8-sig'))
if obj.get('success') is not True: raise SystemExit('Plugin did not report success; inspect the task before resubmitting.')
asset=obj.get('image') or {}; raw=asset.get('bytesBase64')
if not isinstance(raw,str): raise SystemExit('No image.bytesBase64 Asset found')
if raw.startswith('data:'): raw=raw.split(',',1)[1]
data=base64.b64decode(raw,validate=True)
if not data.startswith(b'\x89PNG\r\n\x1a\n'): raise SystemExit('Expected a PNG; inspect output type')
Path(a.output).write_bytes(data); print('Saved PNG:',a.output)
