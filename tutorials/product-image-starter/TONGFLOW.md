# TongFlow ToAPIs plugin: a reproducible image-gen smoke test

Tested on 2026-10-12. Independent validation; no partnership announcement.

- Plugin: [tong-io/tongflow-router-toapis](https://github.com/tong-io/tongflow-router-toapis)
- Exact commit: [46724d2aa05cf26ba98fcecc76a95145c83d35d3](https://github.com/tong-io/tongflow-router-toapis/commit/46724d2aa05cf26ba98fcecc76a95145c83d35d3)
- Python SDK: `tongflow==0.3.4`
- Base: `https://toapis.cn/v1`
- Slot: `image-gen`; explicit model: `gpt-image-2`
- Prompt input: text, width=1024, height=1024

![PNG returned by the plugin](assets/tongflow-plugin.png)

The unmodified plugin submitted an async image task, polled it, downloaded its PNG, and returned `success=true` with an Asset containing `bytesBase64`, `filename`, and `mime`. End-to-end time: 46.70 seconds. Decode `bytesBase64` to save the actual image; do not print the entire base64 response into a public log.

## Repeat the CLI test

```bash
git clone https://github.com/tong-io/tongflow-router-toapis.git
cd tongflow-router-toapis
git checkout 46724d2aa05cf26ba98fcecc76a95145c83d35d3
python -m venv .venv
# Activate this environment with your shell's normal venv activation command.
python -m pip install tongflow==0.3.4
# Set TOAPIS_API_KEY privately.
# Set TOAPIS_BASE_URL=https://toapis.cn/v1
```

The plugin expects one JSON request on stdin:
```json
{
  "nodeSlot": "image-gen",
  "model": "gpt-image-2",
  "prompt": {
    "text": "Commercial product photography of one unbranded matte orange insulated cup with a black lid, on a pale stone plinth, soft morning light, natural contact shadow, no text, no logo.",
    "width": 1024,
    "height": 1024
  }
}
```

Save the JSON as `request.json`, then run:
```powershell
Get-Content request.json -Raw | python entry.py > result.json
```

This command generates one potentially billable image. An explicit model is required to reproduce the tested route. The checked-in run uses the longer original prompt in [data/runs.json](data/runs.json); use that exact prompt when comparing.

## Scope and limits

Passed: image-gen CLI/ABI submission, polling, PNG download and Asset serialization at this exact version.

Not tested: desktop canvas wiring, app installation, image-edit, fusion, text, video or all available models. No claims about user counts, conversion, partnership or current Trending placement.

TongFlow and its SDK retain their upstream license. This tutorial does not redistribute their source; install the official SDK and clone the original repository. Keep the plugin source/version attribution when deriving your own work.

[Try GPT Image 2](https://go.toapis.com/1012_gh_tongflow_image)

