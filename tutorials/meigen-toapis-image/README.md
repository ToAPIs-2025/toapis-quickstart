# Product images with MeiGen local MCP and ToAPIs

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2 | Image | 1K / n=1 | $0.015/image | unverified | 1 |

Historical image charges remain unverified; quotes are not billed amounts.

Patched local MCP text-to-image validated; remote cloud video is a separate route and is not integrated by this patch.
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## Same prompt: 8 image models and example costs

Tested **2026-10-17**: the same text-to-image prompt, one output per example, sorted by example amount from low to high. **gpt-image-2(VIP) starts at $0.0019/image; low/1K here is $0.0019/image.**

Each row identifies a task settlement receipt or an account billing log. Unknown-phase logs are not final net settlements; model/time-window candidates are not confirmed task matches. Catalog rates are historical quotes, not locked prices. gpt-image-2.5-flare-vip is token-metered: **$0.005272 is this image's settled charge**, not a fixed image rate. It is a different API ID from gpt-image-2.5-flare. Qwen has no returned key quote; only its example log amount is shown.

The prompt is shared, but quality defaults and output dimensions differ. Request presets and actual pixels are listed separately. Seedream Pro requested 1K with quality omitted (medium quoted), and returned 2048×2048. These are independent ToAPIs API asset tests; they do not extend any project's native-provider, UI, import or video validation, and are not added to the historical project subtotal below.

| Model / API ID | Request preset → actual pixels | Catalog rate (2026-10-17) | Example amount USD ↑ | Cost evidence | Real output |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | Token-based; key quote unavailable | **$0.005272** | Task receipt: settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key quote unavailable | **$0.021** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | Log: model/time candidate; phase unknown | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-en.jpg)

[Shared prompt, originals and cost sources](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

[简体中文](README_zh-CN.md) · [Model and pricing](https://go.toapis.com/1012_meigen_gh_en) · [Upstream MeiGen](https://github.com/jau123/MeiGen-AI-Design-MCP)

Generate and save a product image with your own ToAPIs key through local MCP. This guide provides a small community patch at a fixed upstream commit. The official npm package does not include this patch; this is an independent integration example.

![Real output tested on Oct 12](assets/result.png)

## What was tested

On Oct 12, 2026, a real `generate_image` MCP call used the patched OpenAIProvider, submitted and polled a ToAPIs task, and saved a local PNG. Model: standard `gpt-image-2`; requested 3:4, 1K, one image. Actual output: 896×1184, without resizing. The single tool call took 50.91 seconds. This is not an average-time or reliability benchmark. See [evidence.json](evidence.json).

Read-only pricing checked on Oct 12: $0.015 per request at 1K, $0.020 at 2K and $0.025 at 4K, for n=1. Only 1K was tested live. Historical billed charges were not independently verified; use your account Usage Logs for the actual charge. [Dated quote](pricing.json)

## 1 Install the fixed source and patch

Use Git and Node.js 24. Clone both repositories in one workspace. Stop if the patch check fails and confirm the upstream commit first.

```powershell
git clone https://github.com/ToAPIs-2025/toapis-quickstart.git
git clone https://github.com/jau123/MeiGen-AI-Design-MCP.git meigen-toapis
git -C meigen-toapis checkout 33ecb583c541652574c5875963d1225fa4ecf751
git -C meigen-toapis apply --check ../toapis-quickstart/tutorials/meigen-toapis-image/adapter.patch
git -C meigen-toapis apply ../toapis-quickstart/tutorials/meigen-toapis-image/adapter.patch
Copy-Item toapis-quickstart/tutorials/meigen-toapis-image/*mjs meigen-toapis/
cd meigen-toapis
npx pnpm@11.25.0 install --frozen-lockfile --ignore-scripts
npx pnpm@11.25.0 exec tsc
```

This installs dependencies and builds local source without submitting an image. The original MIT copyright is preserved in [UPSTREAM-LICENSE](UPSTREAM-LICENSE).

## 2 Configure your own key

Create a private env file outside the repository; replace the example key and paths. Use `https://toapis.com` internationally or `https://toapis.cn` for mainland China. The adapter accepts an origin or `/v1` and normalizes the path once. Marketing links are not API base URLs.

```dotenv
TOAPIS_API_KEY=YOUR_OWN_KEY
TOAPIS_BASE_URL=https://toapis.cn
```

Add this to an MCP client that supports local stdio, change the absolute paths and reconnect. This is example configuration, not a screenshot of a client UI.

```json
{
  "mcpServers": {
    "meigen-toapis": {
      "command": "node",
      "args": ["C:/work/meigen-toapis/start-toapis.mjs"],
      "env": {
        "TOAPIS_ENV_FILE": "C:/private/toapis.env",
        "MEIGEN_OUTPUT_DIR": "C:/work/generated"
      }
    }
  }
}
```

Free connection check, from `meigen-toapis`: `node toapis-smoke.mjs C:/private/toapis.env C:/work/verification list`. This initializes MCP and lists tools without generating an image.

## 3 Generate and save one image

Call `generate_image` explicitly with the real test input below. Any text-agent model and fees belong to your client and are separate from this image validation.

```json
{
  "provider": "openai",
  "model": "gpt-image-2",
  "prompt": "Create an elegant ecommerce product poster for an unbranded matte orange insulated tumbler. Centered hero product on a black stone podium, warm orange rim light, deep charcoal studio background, controlled condensation, premium commercial photography, generous negative space in the upper third for a headline added later. No text, no logos, no watermarks.",
  "aspectRatio": "3:4",
  "resolution": "1K",
  "wait": true,
  "download": true
}
```

`provider=openai` is the existing BYOK entry; the patch adds explicit ToAPIs async handling. Changing the base URL alone is insufficient. Alternatively, `node toapis-smoke.mjs C:/private/toapis.env C:/work/generated live` submits one billable image; list is the default and live must be explicit.

Expect `success=true`, `status=completed` and a readable `savedPath`. Open the file, inspect its dimensions and retain the task ID. Save temporary outputs promptly.

## 4 Reuse the workflow

Change only the product, setting and lighting in the prompt first, keeping the model, 1K tier and single image. Template: `Commercial product photography of [your product], on [surface], with [lighting], [background], space for a headline added later. No text or logos.` This text-to-image preview has no reference-image input and cannot guarantee exact product identity. Add factual copy separately after generation.

## API contract and recovery

Bearer authentication; POST `/v1/images/generations` with model, prompt, ratio size, resolution and n=1. Use the task ID to GET `/v1/images/generations/{id}`; on completed, download `result.data[0].url` without the API key. Poll at about 8 seconds for up to 10 minutes. Never automatically retry submission POSTs. On timeout or cancellation, query the recorded task before submitting another. MeiGen Cloud `check_generation` cannot query ToAPIs tasks.

Only gpt-image-2 text-to-image is supported. 2K/4K are accepted parameter tiers but untested live; other model IDs are rejected. No reference images, remote OAuth, cloud video or Cloud Skills were integrated. This case does not upload reference material to MeiGen. Local MCP does not mean the entire product works offline.

## Verification and screenshots

Upstream SHA `33ecb583c541652574c5875963d1225fa4ecf751`. TypeScript, 4 adapter tests and 28 related regression tests passed again on Oct 12 using fixtures, with no billable generation. The real image is one success, not a throughput benchmark. [Step screenshots](screenshots/) are authored instruction pages rendered in a browser with the real result and example configuration; they do not depict upstream UI.
