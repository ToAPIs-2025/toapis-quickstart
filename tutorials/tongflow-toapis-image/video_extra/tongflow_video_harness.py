"""Existing typed SDK handler, explicit Seedance controls and durable transport wrapper."""
from pathlib import Path
import importlib.util,json,os,sys,base64
from seedance_client import Client
job=json.load(sys.stdin)
if '--live' not in sys.argv:
 print(json.dumps({'dry_run':True,'model':job['model'],'handler':'image_gen_video','requires':'--live and your private TOAPIS_API_KEY'}));raise SystemExit(0)
if os.environ.get('TONGFLOW_SDK_PATH'):sys.path.insert(0,os.environ['TONGFLOW_SDK_PATH'])
spec=importlib.util.spec_from_file_location('tongflow_toapis_plugin',os.environ['TONGFLOW_PLUGIN_ENTRY']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
from tongflow.models.image_gen_video import ImageGenVideoInput
from tongflow.protocol import Asset
c=Client(job['run_id']);m._REQUEST_MODEL=job['model']
if c.path.exists():
 previous=json.loads(c.path.read_text(encoding='utf-8'))
 if previous.get('task_id') and previous.get('request',{}).get('image_urls'):
  # Resume the exact task and uploaded first frame after a local serialization error.
  m._upload_image=lambda a:previous['request']['image_urls'][0]
# Keep the original SDK handler, upload and Asset output. The wrapper adds explicit
# Seedance knobs missing from the plugin and replaces retrying task transport.
def submit(route,body,kind):
 if route!='/videos/generations' or kind!='video':raise ValueError('Only the video slot is enabled')
 return c.submit({**body,'resolution':'480p','generate_audio':False})
def poll(route,task,kind):return c.poll(task)
m._submit_task=submit;m._poll_task=poll;m._download=lambda url:(c.download(url),'video/mp4')
image=Path(job['local_image']).read_bytes()
inp=ImageGenVideoInput(duration=4,text=job['prompt'],image=Asset(bytesBase64=base64.b64encode(image).decode(),mime='image/png',filename='original-product.png'),width=640,height=640)
result=m.image_gen_video(inp)
result=result if isinstance(result,dict) else result.model_dump()
if not result.get('success') or not result.get('video'):raise RuntimeError('SDK video handler did not succeed')
video=result['video'];video=video if isinstance(video,dict) else video.model_dump()
raw=base64.b64decode(video['bytesBase64'])
if b'ftyp' not in raw[:40]:raise RuntimeError('SDK Asset is not an MP4')
Path(job['output']).write_bytes(raw)
print(json.dumps({'success':True,'handler':'image_gen_video','sdk':'0.3.4','model':job['model'],'asset_serialization':True}))
