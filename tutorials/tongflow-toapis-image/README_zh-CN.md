# TongFlow ToAPIs 插件生成商品图与保存 PNG

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## 模型类型、测试档位与花费

更新：2026-10-16。下表为已验证案例的历史档位与价格；本段补充不改变下方原批次记录。

| 模型（API ID） | 类型 | 测试档位 | 单次报价 | 已确认单次消费 | 数量 |
|---|---|---|---:|---:|---:|
| gpt-image-2 | 图片 | 1K / n=1 | $0.015/image | 未确认 | 1 |

历史图片实际消费尚未确认；报价不当作实扣。

原插件文生图CLI已验证；新增视频以真实SDK处理器加明确参数/任务传输包装层验证，画布未验收。

[视频补测、参数、费用与复用](video_extra/README_zh-CN.md)
<!-- TOAPIS-VIDEO-PREVIEWS-20261016 -->
### Seedance 视频演示与本条消费

[![TongFlow · Seedance 2 Mini](video_extra/previews/seedance-2-mini.jpg)](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/tongflow-toapis-image/video_extra/clips/seedance-2-mini.mp4)

**Seedance 2 Mini** · 480p · 4.04s · **$0.127484/clip** · 约 $0.031555/s

API结算与后台表单一致。美元/秒为本条配置折算。

<!-- /TOAPIS-VIDEO-PREVIEWS-20261016 -->
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

<!-- TOAPIS-IMAGE-SAMPLES-20261017 -->
## 同一提示词：8 个图片模型与消费对比

测试日期：**2026-10-17**。8 个模型使用同一条文生图提示词，每例 1 张，按本例消费金额从低到高排列。**gpt-image-2(VIP) $0.0019/image 起；本例 low/1K 为 $0.0019/image。**

金额来自任务结算回执或账号计费日志，逐行注明来源。阶段未知的日志不代表最终净结算；按模型/时间窗口匹配的记录尚未确认到单个任务。目录价是历史报价，不是锁价。gpt-image-2.5-flare-vip 按 Token 计费，**$0.005272 仅为这一张的已结算费用**，不是固定单张价；它与 gpt-image-2.5-flare 是不同 API ID。Qwen 的目录价未返回，只展示本例日志金额。

提示词相同，模型默认质量和实际分辨率不同；表内将请求与输出分别列出。Seedream Pro 请求 1K、未传 quality（报价档位 medium），实际返回 2048×2048。这组图片是独立 ToAPIs API 素材测试，不新增任何项目原生 Provider、UI、图片导入或视频的验收结论，也不计入下方历史项目消费小计。

| 模型 / API ID | 请求档位 → 实际尺寸 | 目录价（2026-10-17） | 本例消费金额 USD ↑ | 费用依据 | 真实输出 |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | 按 Token；Key 报价未返回 | **$0.005272** | 任务回执 settled | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key 报价未返回 | **$0.021** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | 日志：模型/时间窗口候选；阶段未知 | <a href="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg"><img src="https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](https://raw.githubusercontent.com/ToAPIs-2025/toapis-quickstart/main/tutorials/image-model-samples-2026-10-17/overview-cn.jpg)

[共同提示词、原图与费用来源](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/image-model-samples-2026-10-17/README_zh-CN.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

<!-- /TOAPIS-IMAGE-SAMPLES-20261017 -->

[English](README.md) · [同款模型](https://go.toapis.com/1012_tongflow_gh_cn) · [原插件](https://github.com/tong-io/tongflow-router-toapis)

使用 TongFlow 已有 ToAPIs 插件，以自己的 Key 生成商品图。本教程复现插件的文生图 CLI，未修改上游插件，不代表官方合作或整个画布产品已验收。

![插件返回的真实 PNG](assets/result.png)

## 实测与价格

2026-10-12，原插件固定版本 `46724d2aa05cf26ba98fcecc76a95145c83d35d3`、SDK `tongflow==0.3.4`、`image-gen`、标准模型 `gpt-image-2`。输入 1024×1024，输出 PNG 同尺寸，CLI 返回 success=true 和包含 bytesBase64 的 Image Asset；耗时 46.70 秒，是单次结果。

今天只读查询 1K/n=1 报价 $0.015／次；2K $0.020、4K $0.025。此插件用例只验证了 1K，不将其他报价档位当插件能力承诺。历史任务的 billing 为 null，真实扣费未核验。[实测记录](evidence.json) · [报价快照](pricing.json)

## 1 安装固定插件与 SDK

准备 Git、Python 3.10+ 和 PowerShell 7（下方 MaskInput 隐藏输入依赖 PS7）。从同一工作目录执行：

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

macOS/Linux 使用 `source .venv/bin/activate`，其他步骤同原插件文档。插件和 SDK 使用上游许可，本教程不重新分发源码；查看上游 LICENSE/CLA，再决定自己的扩展和分发方式。

## 2 配置并生成一张图片

`request.json` 已提供原创实测提示词、明确模型和尺寸；Key 只在进程环境中配置。国际网络可以用 `https://toapis.com/v1`，国内使用 `/v1` 结尾的 `https://toapis.cn/v1`，避免重复路径。以下真正提交一张可能收费的图片：

```powershell
$env:TOAPIS_API_KEY = Read-Host "Paste your own API key" -MaskInput
$env:TOAPIS_BASE_URL = "https://toapis.cn/v1"
Get-Content request.json -Raw | python entry.py > response.json
python decode_asset.py response.json --output result.png
Remove-Item Env:TOAPIS_API_KEY
```

不会把整个 Asset base64 打印到聊天；输出先保存 response.json，再用 decoder 得到 result.png。无 Key 时不要运行 entry.py。401 先查 Key；400 查模型与参数；中断后保留 task ID 并查询原任务，不盲目重复提交。

## 3 保存、核对与复用

`decode_asset.py` 要求 success=true、`image.bytesBase64` 和 PNG 文件头；输出 result.png 后人工打开。参考 [request.json](request.json)，先改 `prompt.text` 中的商品、材质、台面与灯光，保持 model 和 1024 尺寸，每次明确运行一张。提示词与输出不会保证真实商品标签或形状完全准确。

本例可复用为独立插件调用、配置排查和测试记录模板；不能从 CLI 成功推导画布节点已接好。若要做画布教程，另测插件加载、节点输入、Asset 显示与文件保存。

## 请求与结果

Bearer 鉴权。插件通过 POST `/v1/images/generations` 提交；取得 id 后 GET `/v1/images/generations/{id}`；completed 时下载结果并转换为 TongFlow Asset。明确指定模型，不把插件默认或目录中的其他型号视为通过验收。

通过范围：固定版本 image-gen CLI、异步任务、PNG 下载、Asset 序列化。未测范围：桌面画布、image-edit/fusion、文本、视频、音频、其他模型和大规模并发。插件存在不证明 ToAPIs 已签约或赞助。

[步骤截图](screenshots/) 为本教程说明页的浏览器截图，配真实输出，不冒充画布 UI。[上游插件说明](https://github.com/tong-io/tongflow-router-toapis)
