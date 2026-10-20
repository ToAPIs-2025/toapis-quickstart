# Image/video models, current prices and real cases

[English](README.md) · [中文](README_zh-CN.md)

Pricing checked 2026-10-20. Image examples are dated 2026-10-17; video examples 2026-10-20. Tables sort by example amount or case USD/s. Presets and input modes differ; this is not a matched-settings quality ranking. Unknown-phase image logs are not confirmed final net settlements. Current quotes and historical amounts are separate. Video charges are billing=settled; case USD/s divides charge by actual file duration, never processing time. Token tariffs appear in small text and do not imply a fixed per-second price.

gpt-image-2(VIP) starts at $0.0019/image; this low/1K preset is $0.0019/image. The standalone sampler has 31 historically successful image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid submission until an exact price is available.

## Images: per-image quotes and historical example amounts

| Image model / tested preset | Current preset quote / image | Historical example amount / image | Fee evidence |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | Billing log, phase unknown |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| gpt-image-2.5-sunburst-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| gemini-2.5-flash-image-preview<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| flux-kontext-pro<br><sub>default</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| qwen-image-3.0<br><sub>1K</sub> | Current-key quote unavailable | **$0.021/image** | Billing log, phase unknown |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| gemini-3.1-flash-image-preview<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| qwen-image-3.0-pro<br><sub>1K</sub> | Current-key quote unavailable | **$0.028/image** | Billing log, phase unknown |
| doubao-seedream-4-0<br><sub>1K</sub> | $0.0285/image | **$0.0285/image** | Billing log, phase unknown |
| gemini-3.1-flash-image-preview-vip<br><sub>1K</sub> | $0.03/image | **$0.03/image** | Billing log, phase unknown |
| nano_banana_2<br><sub>1K</sub> | $0.03/image | **$0.03/image** | Billing log, phase unknown |
| viduq2-fast<br><sub>1K</sub> | $0.030134/image | **$0.030134/image** | Billing log, phase unknown |
| doubao-seedream-5-0<br><sub>2K</sub> | $0.0315/image | **$0.0315/image** | Billing log, phase unknown |
| doubao-seedream-4-5<br><sub>2K</sub> | $0.0357/image | **$0.0357/image** | Billing log, phase unknown |
| flux-kontext-max<br><sub>default</sub> | $0.04/image | **$0.04/image** | Billing log, phase unknown |
| gemini-3-pro-image-preview<br><sub>1K</sub> | $0.04/image | **$0.04/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro-global<br><sub>1K</sub> | Current-key quote unavailable | **$0.045/image** | Billing log, phase unknown |
| gemini-3-pro-image-preview-vip<br><sub>1K</sub> | $0.05/image | **$0.05/image** | Billing log, phase unknown |
| nano_banana_pro<br><sub>1K</sub> | $0.05/image | **$0.05/image** | Billing log, phase unknown |
| viduq3-fast<br><sub>1K</sub> | $0.050223/image | **$0.050222/image** | Billing log, phase unknown |
| vidu-image<br><sub>1K</sub> | $0.066964/image | **$0.066964/image** | Billing log, phase unknown |
| flux-2-flex<br><sub>1K</sub> | $0.07/image | **$0.07/image** | Billing log, phase unknown |
| viduq2-pro<br><sub>1K</sub> | $0.100446/image | **$0.100446/image** | Billing log, phase unknown |

## Videos: settled clip charges and measured USD/s

| Video model | Preset / input | Settled clip charge | File duration | Case USD/s, ascending |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / text-to-video | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>Pricing tariff: $0.025/s</sub> |
| seedance-2-mini | 4s / 480p / first-frame | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>Pricing tariff: $3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / text-to-video | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>Pricing tariff: $5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / text-to-video | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>Pricing tariff: $0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / text-to-video | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>Pricing tariff: $0.064/s</sub> |
| seedance-2 | 4s / 480p / first-frame | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>Pricing tariff: $6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / text-to-video | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>Pricing tariff: $0.08/s</sub> |
| seedance-2-5 | 4s / 480p / text-to-video | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>Pricing tariff: $10/M total tokens</sub> |

## Reusable client

[31 image + 8 video preset client](client/README.md)

Native integration boundaries remain in each project README/ACCEPTANCE. API success here does not replace in-app acceptance.

## Original outputs

### gpt-image-2(VIP)

[![Original image](images/gpt-image-2-vip.png)](images/gpt-image-2-vip.png)

### gpt-image-2.5-flare-vip

[![Original image](images/gpt-image-2.5-flare-vip.png)](images/gpt-image-2.5-flare-vip.png)

### gpt-image-2.5-sunburst-vip

[![Original image](images/gpt-image-2.5-sunburst-vip.png)](images/gpt-image-2.5-sunburst-vip.png)

### gemini-2.5-flash-image-preview

[![Original image](images/gemini-2.5-flash-image-preview.png)](images/gemini-2.5-flash-image-preview.png)

### nano_banana

[![Original image](images/nano_banana.png)](images/nano_banana.png)

### gemini-nano-banana-2.1

[![Original image](images/gemini-nano-banana-2.1.jpg)](images/gemini-nano-banana-2.1.jpg)

### gpt-image-2

[![Original image](images/gpt-image-2.png)](images/gpt-image-2.png)

### flux-kontext-pro

[![Original image](images/flux-kontext-pro.png)](images/flux-kontext-pro.png)

### gemini-nano-banana-2.1-vip

[![Original image](images/gemini-nano-banana-2.1-vip.png)](images/gemini-nano-banana-2.1-vip.png)

### qwen-image-3.0

[![Original image](images/qwen-image-3.0.png)](images/qwen-image-3.0.png)

### gpt-image-2.5-flare

[![Original image](images/gpt-image-2.5-flare.png)](images/gpt-image-2.5-flare.png)

### gpt-image-2.5-sunburst

[![Original image](images/gpt-image-2.5-sunburst.png)](images/gpt-image-2.5-sunburst.png)

### flux-2-pro

[![Original image](images/flux-2-pro.jpg)](images/flux-2-pro.jpg)

### gemini-3.1-flash-image-preview

[![Original image](images/gemini-3.1-flash-image-preview.png)](images/gemini-3.1-flash-image-preview.png)

### qwen-image-3.0-pro

[![Original image](images/qwen-image-3.0-pro.png)](images/qwen-image-3.0-pro.png)

### doubao-seedream-4-0

[![Original image](images/doubao-seedream-4-0.jpg)](images/doubao-seedream-4-0.jpg)

### gemini-3.1-flash-image-preview-vip

[![Original image](images/gemini-3.1-flash-image-preview-vip.png)](images/gemini-3.1-flash-image-preview-vip.png)

### nano_banana_2

[![Original image](images/nano_banana_2.png)](images/nano_banana_2.png)

### viduq2-fast

[![Original image](images/viduq2-fast.png)](images/viduq2-fast.png)

### doubao-seedream-5-0

[![Original image](images/doubao-seedream-5-0.jpg)](images/doubao-seedream-5-0.jpg)

### doubao-seedream-4-5

[![Original image](images/doubao-seedream-4-5.jpg)](images/doubao-seedream-4-5.jpg)

### flux-kontext-max

[![Original image](images/flux-kontext-max.png)](images/flux-kontext-max.png)

### gemini-3-pro-image-preview

[![Original image](images/gemini-3-pro-image-preview.jpg)](images/gemini-3-pro-image-preview.jpg)

### doubao-seedream-5-0-pro

[![Original image](images/doubao-seedream-5-0-pro.jpg)](images/doubao-seedream-5-0-pro.jpg)

### doubao-seedream-5-0-pro-global

[![Original image](images/doubao-seedream-5-0-pro-global.jpg)](images/doubao-seedream-5-0-pro-global.jpg)

### gemini-3-pro-image-preview-vip

[![Original image](images/gemini-3-pro-image-preview-vip.png)](images/gemini-3-pro-image-preview-vip.png)

### nano_banana_pro

[![Original image](images/nano_banana_pro.jpg)](images/nano_banana_pro.jpg)

### viduq3-fast

[![Original image](images/viduq3-fast.png)](images/viduq3-fast.png)

### vidu-image

[![Original image](images/vidu-image.png)](images/vidu-image.png)

### flux-2-flex

[![Original image](images/flux-2-flex.jpg)](images/flux-2-flex.jpg)

### viduq2-pro

[![Original image](images/viduq2-pro.png)](images/viduq2-pro.png)

### MiniMax-H3-Max-Turbo

[![Video preview](videos/MiniMax-H3-Max-Turbo.jpg)](videos/MiniMax-H3-Max-Turbo.mp4)

[MP4](videos/MiniMax-H3-Max-Turbo.mp4) · $0.125/clip · $0.024131/s

### seedance-2-mini

[![Video preview](videos/seedance-2-mini.jpg)](videos/seedance-2-mini.mp4)

[MP4](videos/seedance-2-mini.mp4) · $0.13338/clip · $0.033015/s

### seedance-2-fast

[![Video preview](videos/seedance-2-fast.jpg)](videos/seedance-2-fast.mp4)

[MP4](videos/seedance-2-fast.mp4) · $0.214568/clip · $0.053111/s

### kling-v3

[![Video preview](videos/kling-v3.jpg)](videos/kling-v3.mp4)

[MP4](videos/kling-v3.mp4) · $0.3/clip · $0.059524/s

### MiniMax-H3

[![Video preview](videos/MiniMax-H3.jpg)](videos/MiniMax-H3.mp4)

[MP4](videos/MiniMax-H3.mp4) · $0.32/clip · $0.061896/s

### seedance-2

[![Video preview](videos/seedance-2.jpg)](videos/seedance-2.mp4)

[MP4](videos/seedance-2.mp4) · $0.26676/clip · $0.06603/s

### kling-3.0-turbo

[![Video preview](videos/kling-3.0-turbo.jpg)](videos/kling-3.0-turbo.mp4)

[MP4](videos/kling-3.0-turbo.mp4) · $0.32/clip · $0.079208/s

### seedance-2-5

[![Video preview](videos/seedance-2-5.jpg)](videos/seedance-2-5.mp4)

[MP4](videos/seedance-2-5.mp4) · $0.3883/clip · $0.096114/s

[Sanitized parameters and cost sources](cases.json) · [Image prompt](image-prompt.txt) · [T2V prompt](video-prompt.txt)

First-frame cases use their original generated PNGs. Audio-track observations are file-specific; upstream TTS features are not ToAPIs capability claims.
