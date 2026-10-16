# TongFlow video additions and model costs

[English](README.md) · [中文](README_zh-CN.md)

Project-specific tested outputs and failed attempts are recorded separately; earlier examples remain intact.

| Model/API ID | Result | Output | Clip cost | USD/second | Cost evidence |
|---|---|---|---:|---:|---|
| Seedance 2 Mini (`seedance-2-mini`) | completed | 4.04s / 640×640 | $0.127484 | $0.031555/s | API settled; owner sheet pending |

Requested: 4 seconds, 480p, 1:1, generate_audio=false, one first frame, no video/audio input. Successful outputs are 640×640, 24 fps and 4.04 seconds. Seedance bills total tokens; USD/second divides this clip’s settled cost by actual output duration, not a fixed per-second rate.

## Seedance 2 Mini

[![TongFlow — seedance-2-mini](previews/seedance-2-mini.jpg)](clips/seedance-2-mini.mp4)

[MP4](clips/seedance-2-mini.mp4) · [JSON](seedance-2-mini-summary.json)

Original SDK image_gen_video handler → original first-frame upload → wrapper adding resolution/audio and durable transport → SDK video Asset validated. The wrapper is a community example, not a merged upstream plugin change; canvas remains unvalidated.

Total-token rate at test: $3.285714/million tokens.

[Model landing page and pricing](https://go2.toapis.com/tg16sm)

## Reuse

Run from this tutorial’s root directory:

```sh
python video_extra/run_seedance_example.py --job video_extra/job.json
# One paid task with your private TOAPIS_API_KEY:
python video_extra/run_seedance_example.py --job video_extra/job.json --live
```

Default is dry-run. --live makes one paid task. Preserve .toapis-state; missing IDs and terminal failures never trigger automatic resubmission. Result downloads carry no API key.

```sh
pip install tongflow==0.3.4
git clone https://github.com/tong-io/tongflow-router-toapis.git
git -C tongflow-router-toapis checkout 46724d2aa05cf26ba98fcecc76a95145c83d35d3
# Set TONGFLOW_PLUGIN_ENTRY to the absolute path of entry.py.
# Set TOAPIS_BASE_URL=https://toapis.com/v1 for the plugin.
python video_extra/tongflow_video_harness.py < video_extra/sdk-job.json
python video_extra/tongflow_video_harness.py --live < video_extra/sdk-job.json
```

[Seedance 2 / 2 Mini API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2/generation) · [Seedance 2.5 API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2-5/generation)

The historical MiniMax sample is 5s/768p; these Seedance samples are 480p. They do not establish equal-quality pricing or a universal price ranking.
