# Generate and save a product image with the TongFlow ToAPIs plugin

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2 | Image | 1K / n=1 | $0.015/image | unverified | 1 |

Historical image charges remain unverified; quotes are not billed amounts.

Original image CLI validated; the video addition tests the real SDK handler with an explicit-parameter/durable-transport wrapper, not canvas acceptance.

[Video additions, parameters, costs and reuse](video_extra/README.md)
<!-- TOAPIS-VIDEO-PREVIEWS-20261016 -->
### Seedance video demos and clip costs

[![TongFlow · Seedance 2 Mini](video_extra/previews/seedance-2-mini.jpg)](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/tongflow-toapis-image/video_extra/clips/seedance-2-mini.mp4)

**Seedance 2 Mini** · 480p · 4.04s · **$0.127484/clip** · about $0.031555/s

API-settled amounts; the new tasks await billing-sheet cross-check. USD/s is specific to these clips.

<!-- /TOAPIS-VIDEO-PREVIEWS-20261016 -->
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

[简体中文](README_zh-CN.md) · [Model and pricing](https://go.toapis.com/1012_tongflow_gh_en) · [Original plugin](https://github.com/tong-io/tongflow-router-toapis)

Use your own ToAPIs key with the existing TongFlow plugin. This reproduces an unmodified image-gen CLI route, not a validated canvas workflow or a partnership announcement.

![Real PNG returned by the plugin](assets/result.png)

## Tested scope and price

Oct 12, 2026: plugin `46724d2aa05cf26ba98fcecc76a95145c83d35d3`, SDK `tongflow==0.3.4`, image-gen, standard `gpt-image-2`. Input width/height 1024; actual PNG 1024×1024. The CLI returned success=true and an Image Asset with bytesBase64. A single run took 46.70 seconds; this is not an average-time guarantee. [Evidence](evidence.json)

Read-only quote checked today: 1K/n=1 $0.015 per request, 2K $0.020, 4K $0.025. This plugin case validates only 1K, and does not promise control of other tiers. Historical billing was null; actual charges are unverified. [Dated quote](pricing.json)

## 1 Install the fixed plugin and SDK

Use Git, Python 3.10+ and PowerShell 7 for the Windows example. Clone both repositories in one workspace:

```powershell
git clone https://github.com/ToAPIs-2025/toapis-quickstart.git
git clone https://github.com/tong-io/tongflow-router-toapis.git
git -C tongflow-router-toapis checkout 46724d2aa05cf26ba98fcecc76a95145c83d35d3
Copy-Item toapis-quickstart/tutorials/tongflow-toapis-image/request.json tongflow-router-toapis/
Copy-Item toapis-quickstart/tutorials/tongflow-toapis-image/decode_asset.py tongflow-router-toapis/
cd tongflow-router-toapis
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install tongflow==0.3.4
```

On macOS/Linux activate with `source .venv/bin/activate`. The plugin and SDK retain their upstream licenses; review LICENSE and CLA before deriving or redistributing your own work. This tutorial does not redistribute them.

## 2 Configure and generate one image

`request.json` includes the real original prompt, explicit model and dimensions. Configure your own key privately. The example below requires PowerShell 7 for MaskInput and submits one potentially billable image:

```powershell
$env:TOAPIS_API_KEY = Read-Host "Paste your own API key" -MaskInput
$env:TOAPIS_BASE_URL = "https://toapis.cn/v1"
Get-Content request.json -Raw | python entry.py > response.json
python decode_asset.py response.json --output result.png
Remove-Item Env:TOAPIS_API_KEY
```

Use `https://toapis.com/v1` internationally or `https://toapis.cn/v1` for mainland China. Keep /v1 once. On POSIX, set the same environment variables privately and use `python entry.py < request.json > response.json`, then run the decoder. Do not print the entire base64 Asset into a public log.

## 3 Inspect and reuse

The decoder requires success=true, image.bytesBase64 and a PNG header. Open result.png and check its dimensions. Change the product, material, surface and lighting in [request.json](request.json), keeping gpt-image-2 and 1024 dimensions for the first reproduction. Each invocation is a separate image job. Generated product details still require review.

Reuse this as a plugin invocation, setup check and evidence template. A canvas tutorial needs separate tests for plugin loading, node wiring, Asset preview and file saving; CLI success does not establish those paths.

## API and recovery

Bearer authentication; POST `/v1/images/generations`, then GET `/v1/images/generations/{id}`. On completion the plugin downloads the image and serializes a TongFlow Asset. Keep the original task ID after interruption and query it before submitting another job. For 401 check the private key, and for 400 check the model and parameters.

Passed at this version: image-gen CLI, async task handling, PNG download and Asset serialization. The original October 12 image test did not cover canvas, editing/fusion, text, video, audio or throughput. The October 16 video SDK-handler test is documented separately above; canvas and other slots remain unvalidated. An existing plugin is not evidence of a commercial partnership.

[Step screenshots](screenshots/) are browser captures of authored tutorial pages with the real output; they do not show canvas UI.
