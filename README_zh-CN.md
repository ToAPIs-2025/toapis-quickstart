# ToAPIs 快速开始：用 Python 调用文本、图像和视频模型

<img src="assets/toapis-logo.png" alt="ToAPIs 标识" width="72">

一个 Python 脚本演示三种调用方式：文本对话、图像生成和视频生成。无需安装第三方 Python 包。访问 [ToAPIs](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_intro) 获取服务。

首次使用？[注册领取 10 积分](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_signup_credits)，按当前计价可生成 26 张默认的 `gpt-image-2-vip` 图片（1K 分辨率、low 质量）。继续调用前，请[查看价格和实际积分消耗](#赠送积分扣费与充值)。
[English](README.md) · [简体中文](README_zh-CN.md)

> 建议先运行 `--dry-run`：只显示请求地址和参数，不需要 API Key，也不会产生调用费用。正式调用可能产生费用；模型和价格以[当前定价页](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_pricing)为准。

## 示例范围

| 场景 | 本示例使用的模型 | 返回方式 |
| --- | --- | --- |
| 文本 | `gpt-6.1-sol` | 同步返回对话结果 |
| 图像 | `gpt-image-2-vip`（1K、low） | 提交任务，再查询结果链接 |
| 视频 | `seedance-2`（4 秒、720p、无音频） | 提交任务，再查询结果链接 |

代码依据[官方快速开始文档](https://docs.toapis.com/docs/en/quickstart)编写。ToAPIs 目前还有 [Suno 音乐生成](https://toapis.com/en/model-guide/suno)；此快速开始暂不放 Suno 代码，待接口请求与任务返回结构核验后再补。不涵盖 TTS。

## 第一步：先检查请求格式

安装 Python 3.10 或更新版本，克隆仓库，在仓库根目录运行：

```bash
python examples/quickstart.py chat --dry-run
python examples/quickstart.py image --prompt "橙色背景上的纸鹤" --dry-run
python examples/quickstart.py video --prompt "纸鹤在桌面上展开，电影感光影" --dry-run
```

Windows 也可用 `py` 代替 `python`。

## 第二步：配置密钥并调用文本模型

在 [ToAPIs 账户](https://toapis.com/?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_get_key)创建 API Key。请把密钥放在环境变量中，不要写入代码或提交到 GitHub。

**PowerShell：**

```powershell
$env:TOAPIS_API_KEY = "YOUR_API_KEY"
python .\examples\quickstart.py chat --prompt "用一句话解释 API 网关。"
```

**macOS / Linux：**

```bash
export TOAPIS_API_KEY="YOUR_API_KEY"
python examples/quickstart.py chat --prompt "用一句话解释 API 网关。"
```

如需使用中国站接口，可设置 `TOAPIS_BASE_URL=https://toapis.cn`，或加参数 `--base-url https://toapis.cn`。脚本会自动补上 `/v1`。

## 第三步：试用图像和视频

```bash
python examples/quickstart.py image --prompt "简洁的橙黑色几何海报"
python examples/quickstart.py video --prompt "纸鹤在桌面上展开，电影感光影"
```

图像命令默认使用 `gpt-image-2-vip`、1K、`low` 质量。可加 `--image-quality medium` 或 `--image-quality high` 切换 VIP 质量；加 `--image-model gpt-image-2` 可改用普通版。普通版固定为 medium 质量，脚本不会传入 `quality` 参数。正式调用前，请先阅读下方的积分与扣费说明。

视频命令使用 `seedance-2`，时长 4 秒、分辨率 720p、画幅 16:9，并设置 `generate_audio=false`。正式调用前请查看 [Seedance 2 参数与计费说明](https://toapis.com/en/model-guide/seedance-2)。

图像和视频先返回任务 ID，脚本随后每 8 秒查询一次，最多等待 15 分钟。完成后会输出结果链接。生成链接可能过期，需要使用时请及时保存。可用 `--interval` 和 `--max-wait` 修改查询间隔与等待时长。如果终端在任务提交后中断，可用已打印的任务 ID 查询[图像任务](https://docs.toapis.com/docs/en/api-reference/tasks/image-status)或[视频任务](https://docs.toapis.com/docs/en/api-reference/tasks/video-status)状态。

## 赠送积分、扣费与充值

新账号首次注册赠送 10 积分，按当前计价可生成 26 张 `gpt-image-2-vip` 图片（1K 分辨率、low 质量）。更高画质或其他模型的积分消耗不同。10 积分不足以完成本仓库的 Seedance 视频示例；正式调用视频前，请先核对价格并充值。公开价表可能延迟更新；切换模型或参数前，请查看[当前价表](https://toapis.com/en/pricing?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_billing_pricing)。

正式调用后，记下脚本打印的任务 ID，使用同一账号进入 [Dashboard](https://toapis.com/en/dashboard/models)。在 [Task Logs（任务日志）](https://toapis.com/en/dashboard/tasks)查找图像或视频任务及结果，再到 **Usage Logs（用量日志）**查看该次请求的扣费或积分消耗。如果记录尚未出现，稍后刷新日志，并在记录更新后核对余额。以账户记录的实际扣费为准。

赠送积分用完后，可在 Dashboard 的 [Billing / Top up（账单与充值）](https://toapis.com/en/dashboard/billing)查看充值选项；支付前请核对金额和支付信息。
## 接口与排错

示例调用 `POST /v1/chat/completions`、`POST /v1/images/generations` 和 `POST /v1/videos/generations`；图像与视频分别通过对应的 `GET /v1/.../generations/{task_id}` 查询任务。参数和响应结构请以[官方文档](https://docs.toapis.com/docs/en/quickstart)为准；其他模型可从[模型目录](https://toapis.com/en/market?utm_source=github&utm_medium=organic_repo&utm_campaign=gh_quickstart&utm_content=readme_zh_models)查看。

| 现象 | 优先检查 |
| --- | --- |
| 提示缺少 `TOAPIS_API_KEY` | 是否在当前终端设置环境变量 |
| HTTP 401 | 密钥是否有效，复制时是否多了空格 |
| HTTP 400 | 当前文档中的模型和参数是否与示例一致 |
| HTTP 429 | 账户调用限制，稍后重试 |
| 任务等待超时 | 用输出的任务 ID 继续查询；视频可能需要更长时间 |

运行 `python -m unittest discover -s tests` 可验证示例的请求路径和参数。自动化测试只检查请求格式，不会产生付费调用。默认的文本、图像和视频流程已于 2026-10-09 分别完成一次真实调用验收。文档核对日期：2026-10-09。许可证：[MIT](LICENSE)。
