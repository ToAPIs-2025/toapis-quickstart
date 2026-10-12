# Product images before BD: a real GPT Image 2 tutorial

Generate a clean product shot, then edit its scene with the first image as a reference. This tutorial includes **two new ToAPIs outputs tested on 2026-10-12**, a Python script, and a separate smoke test of the existing TongFlow ToAPIs plugin.

[简体中文](README_zh-CN.md) · [Try GPT Image 2](https://go.toapis.com/1012_gh_product_tutorial) · [TongFlow test](TONGFLOW.md)

| Original generated product | Reference-based scene edit |
|---|---|
| ![Orange cup, light scene](assets/product-hero.png) | ![Same product, dark scene](assets/reference-edit.png) |

Both images use `gpt-image-2`, `size=1:1`, `resolution=1k`, `n=1`. Downloaded PNGs are 1024×1024. The orange body, black lid and recognizable silhouette carry into the second scene; this is a visual demonstration, not a guarantee of exact product geometry.

## Run it

Python 3.10+; no third-party packages.

```bash
python generate.py
# Set TOAPIS_API_KEY privately in your terminal.
python generate.py --live --out output/hero
python generate.py --live --reference output/hero/result.png --out output/edit
```

The first command only previews JSON. Each `--live` command submits exactly one potentially billable image. The second live command uploads the local PNG and passes its public URL in `reference_images`. The script then polls every eight seconds, downloads the PNG without forwarding your key to the CDN, and writes a task record.

Use `--base-url https://toapis.com` for the international host. The script normalizes an optional `/v1`. Never commit an API key. A private env file can be supplied with `--key-file`; it is read locally and is never copied into the output.

If a submitted task times out, keep its ID:
```bash
python generate.py --live --resume YOUR_TASK_ID --out output/recovered
```
Resume queries and downloads the original task; it does not submit another task. Do not blindly repeat a POST after a lost response.

## What was tested

| Case | Result | Measured end-to-end time |
|---|---|---:|
| Text → product image | completed, PNG downloaded | 36.47 s |
| Upload → reference-image scene edit | completed, PNG downloaded | 46.31 s |
| TongFlow plugin `image-gen` CLI/ABI | success=true, PNG Asset decoded | 46.70 s |

Timing includes polling/download; the edit case includes the upload. Outputs, requests, timestamps, task IDs and SHA-256 hashes are in [data/runs.json](data/runs.json). Public records omit the temporary uploaded reference URL.

A pre-test `GET /v1/pricing?model=gpt-image-2` returned USD 0.015 per request for n=1 / 1K. Three generation tasks therefore had a **catalog estimate of USD 0.045**. The task responses did not provide confirmed billing amounts: actual charges remain unconfirmed and must be checked in account usage. Prices can change; [pricing contract](https://docs.toapis.com/docs/en/api-reference/account/pricing).

## TongFlow: the exact scope

The existing [TongFlow ToAPIs plugin](https://github.com/tong-io/tongflow-router-toapis) was run unmodified at commit `46724d2aa05cf26ba98fcecc76a95145c83d35d3`, with `tongflow==0.3.4`, `TOAPIS_BASE_URL=https://toapis.cn/v1`, and an explicit `gpt-image-2` model.

[Reproduction steps and output](TONGFLOW.md). This verifies the **image-gen CLI/ABI path**. The desktop canvas, image editing and video nodes were not tested here. This is an independent integration example, not an announcement of a partnership.

## API contracts and checks

[GPT Image 2](https://docs.toapis.com/docs/en/api-reference/images/gpt-image-2/generation) · [Upload](https://docs.toapis.com/docs/en/api-reference/uploads/images) · [Task status](https://docs.toapis.com/docs/en/api-reference/tasks/image-status)

```bash
python -m unittest discover -s . -p test_generate.py
```

The checks cover reference fields, state transitions, HTTP-200 task failure, query rate limits and destination normalization. They are separate from the three real calls recorded above.

Prompts in this tutorial are original. The orange cup is a fictional, unbranded generated product. This case does not demonstrate video or audio capabilities, and it does not claim that any project or model is currently trending.

[Try the same image model](https://go.toapis.com/1012_gh_product_tutorial) · [Browse other models](https://x.toapis.com/1012_gh_product_tutorial_home)

