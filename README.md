# ToAPIs Quickstart: text, image, and video in Python

<img src="assets/toapis-logo.png" alt="ToAPIs logo" width="72">

One Python script, three API workflows. Call a chat model, create an image, or submit a video generation task through [ToAPIs](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_intro). No third-party Python packages are required.

New to ToAPIs? [Sign up for 10 credits](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_signup_credits) (about $0.05), then try the default 1K low-quality image example. [Check pricing and actual charges](#free-credits-billing-and-top-ups) before further calls.

[English](README.md) · [简体中文](README_zh-CN.md)

> Start with `--dry-run`: it shows the endpoint and request body without an API key or billable call. Live calls require a key and may incur charges. Model availability and prices can change; check the [current pricing page](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_pricing).

## What this example covers

| Workflow | Model used in this example | API behavior |
| --- | --- | --- |
| Text | `gpt-6.1-sol` | Synchronous chat completion |
| Image | `gpt-image-2-vip` (1K, low) | Submit task, then poll for result URL |
| Video | `seedance-2` (4 s, 720p, no audio) | Submit task, then poll for result URL |

The script follows the [official quickstart](https://docs.toapis.com/docs/en/quickstart). ToAPIs also lists [Suno music generation](https://toapis.com/en/model-guide/suno); this quickstart has no Suno example because its request and task response still need a verified API contract. It does not cover TTS.

## 1. Check the request without spending credits

Install Python 3.10 or newer, clone this repository, then run:

```bash
python examples/quickstart.py chat --dry-run
python examples/quickstart.py image --prompt "A paper crane on an orange background" --dry-run
python examples/quickstart.py video --prompt "A paper crane unfolds on a desk, cinematic light" --dry-run
```

On Windows, `py` may be used in place of `python`.

## 2. Get a key and make one live call

[Create a ToAPIs API key](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_get_key) in your account. Store it as an environment variable. Do not paste it into a source file or commit it to GitHub.

**macOS / Linux:**

```bash
export TOAPIS_API_KEY="YOUR_API_KEY"
python examples/quickstart.py chat --prompt "Explain an API gateway in one sentence."
```

**PowerShell:**

```powershell
$env:TOAPIS_API_KEY = "YOUR_API_KEY"
python .\examples\quickstart.py chat --prompt "Explain an API gateway in one sentence."
```

For users served by the China endpoint, set `TOAPIS_BASE_URL=https://toapis.cn` (or pass `--base-url https://toapis.cn`). The script appends `/v1` automatically.

## 3. Try image or video

```bash
python examples/quickstart.py image --prompt "A clean orange-and-black geometric poster"
python examples/quickstart.py video --prompt "A paper crane unfolds on a desk, cinematic light"
```

The image command defaults to `gpt-image-2-vip` at 1K and `low` quality. To try its other quality levels, add `--image-quality medium` or `--image-quality high`. To use the standard model, add `--image-model gpt-image-2`; that model uses its fixed medium quality, so the script omits the `quality` field. See the credits and billing steps below before making live calls.
The video command uses `seedance-2` with a 4-second duration, 720p resolution, 16:9 aspect ratio, and `generate_audio=false`. [Review Seedance 2 parameters and pricing](https://toapis.com/en/model-guide/seedance-2) before making a live video call.

Image and video requests return a task ID first. The script checks its status every 8 seconds, for up to 15 minutes, and prints the result URL when complete. Generated links may expire; save output you need promptly. Use `--interval` and `--max-wait` to change polling. If your terminal times out after submission, keep the printed task ID and query the [image task](https://docs.toapis.com/docs/en/api-reference/tasks/image-status) or [video task](https://docs.toapis.com/docs/en/api-reference/tasks/video-status) endpoint directly.

## Free credits, billing, and top-ups

New accounts receive 10 credits (about $0.05) for initial testing. The default 1K, low-quality `gpt-image-2-vip` image is about $0.0019 per image; a 1K `gpt-image-2` image is about $0.015. These are estimates for the stated settings, not a promise of how many calls the remaining balance will cover. Public price displays can lag updates. Check the [current price list](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_billing_pricing) before changing models or settings, especially for video.

After a live call, copy the task ID printed by the script. Sign in to the [Dashboard](https://toapis.com/en/dashboard/models) with the same account. Open [Task Logs](https://toapis.com/en/dashboard/tasks) to find the image or video task and its result, and use **Usage Logs** to inspect the charge or credit usage for the request. If the entry is delayed, refresh the logs and compare the account balance after it appears. The amount recorded in the account is the final charge.

When the free credits are used, open [Billing / Top up](https://toapis.com/en/dashboard/billing) in the Dashboard to review available recharge options. Review the amount and payment details there before paying.
## API routes used

```text
POST /v1/chat/completions
POST /v1/images/generations
GET  /v1/images/generations/{task_id}
POST /v1/videos/generations
GET  /v1/videos/generations/{task_id}
```

The default base is `https://toapis.com`. See the [API documentation](https://docs.toapis.com/docs/en/quickstart) for parameters, response formats, and other models. Browse the [model catalog](https://toapis.com/en/market?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_models) before changing the model IDs in the script.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| `TOAPIS_API_KEY` error | Set the variable in the same terminal session. |
| HTTP 401 | Check that the key is active and copied correctly. |
| HTTP 400 | Check model availability and request parameters in the current docs. |
| HTTP 429 | Check your account limits and retry later. |
| Task times out | Use the printed task ID to inspect status; video can take longer than the default wait. |

## Verify and contribute

```bash
python -m unittest discover -s tests
```

The automated tests check request shapes and do not make paid calls. Manual live smoke checks completed on 2026-10-09 for the default chat, image, and video workflows. Issues and pull requests that keep the examples aligned with the [official docs](https://docs.toapis.com/docs/en/quickstart) are welcome.

Documentation checked: 2026-10-09. License: [MIT](LICENSE).
