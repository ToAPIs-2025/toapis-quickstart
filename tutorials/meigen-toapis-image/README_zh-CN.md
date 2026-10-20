# MeiGen 本地 MCP 生成商品图与保存结果


<!-- TOAPIS-MODELS-20261020 -->
## 模型与价格更新 · 2026-10-20

新增可独立运行的31套图片请求模板、8套视频模板。当前26套图片与8套视频可匹配同Key精确价格；另5套图片缺价，默认阻止新付费调用。它们属于额外API脚本；项目原生Provider、UI、导入及完整出片的验收范围仍以下方原教程为准。

| 图片模型／实测档位 | 当前档位报价／张 | 历史案例金额／张 | 费用证据 |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | 当前Key暂未返回报价 | **$0.005272/image**<br><sub>Token计费；当前$/M未返回，本例金额不是固定单张价。</sub> | 任务回执已结算 |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | 计费日志，阶段未知 |
| qwen-image-3.0<br><sub>1K</sub> | 当前Key暂未返回报价 | **$0.021/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | 计费日志，阶段未知 |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | 计费日志，阶段未知 |

| 视频模型 | 档位／输入 | 本例消费 | 文件时长 | 本例每秒金额（升序） |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / 文生视频 | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>pricing底层费率：$0.025/s</sub> |
| seedance-2-mini | 4s / 480p / 首帧 | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>pricing底层费率：$3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / 文生视频 | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>pricing底层费率：$5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / 文生视频 | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>pricing底层费率：$0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / 文生视频 | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>pricing底层费率：$0.064/s</sub> |
| seedance-2 | 4s / 480p / 首帧 | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>pricing底层费率：$6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / 文生视频 | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>pricing底层费率：$0.08/s</sub> |
| seedance-2-5 | 4s / 480p / 文生视频 | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>pricing底层费率：$10/M total tokens</sub> |

报价核对：2026-10-20。图片案例日期2026-10-17；视频案例日期2026-10-20。表格按本例金额／秒金额排序，质量、分辨率和输入不同，不是同配置质量排名。图片日志的阶段未知，不能当作单任务最终净结算；当前报价与历史金额分别显示。视频金额均由billing=settled确认，$/s按实际文件时长折算，任务处理耗时不参与计算。Token模型不是固定每秒价，底层$/M只作小字补充。

gpt-image-2(VIP)通用价格为$0.0019/image起；本例low/1K为$0.0019/image。新脚本有31套历史成功图片请求模板、8套视频模板；当前26套图片与8套视频可匹配价格，另5套图片因当前Key缺价而默认阻止新付费调用。

[本仓库多模型脚本](../../toapis-models/README_zh-CN.md) · [完整价表](../../PRICING_zh-CN.md) · [原图／视频及费用证据](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

下方保留原项目历史案例、消费及集成说明；历史金额不改成今天的新报价。

<!-- /TOAPIS-MODELS-20261020 -->

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## 模型类型、测试档位与花费

更新：2026-10-16。下表为已验证案例的历史档位与价格；本段补充不改变下方原批次记录。

| 模型（API ID） | 类型 | 测试档位 | 单次报价 | 已确认单次消费 | 数量 |
|---|---|---|---:|---:|---:|
| gpt-image-2 | 图片 | 1K / n=1 | $0.015/image | 未确认 | 1 |

历史图片实际消费尚未确认；报价不当作实扣。

补丁后的本地MCP文生图已验证；远程云端视频属于另一路线，未接入本补丁。
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

[English](README.md) · [同款模型与价格](https://go.toapis.com/1012_meigen_gh_cn) · [MeiGen 上游](https://github.com/jau123/MeiGen-AI-Design-MCP)

用自己的 ToAPIs Key，经 MeiGen 本地 MCP 生成商品图并保存 PNG。本教程提供固定源码版本上的社区适配补丁；上游官方 npm 包尚不包含这份补丁，不是双方合作公告。

![2026-10-12 实测原图](assets/result.png)

## 实测结果

2026-10-12，真实调用 MCP `generate_image`，经过适配后的 OpenAIProvider、ToAPIs 异步任务与图片下载，返回 completed 并在本地保存。模型 `gpt-image-2` 标准渠道，请求 3:4、1K、n=1；实际 PNG 为 896×1184，未裁切或放大。一次工具调用约 50.91 秒，不能据此承诺平均耗时或长期稳定性。

任务与图像哈希见 [evidence.json](evidence.json)。今天重新 GET 查询的 1K 报价为 $0.015／次；2K $0.020，4K $0.025，均为 n=1。仅 1K 做过真实生成；历史任务的实际扣费未知，账单以账户 Usage Logs 为准。[带日期报价](pricing.json)

## 1 安装固定版本和适配补丁

准备 Git、Node.js 24 与可用网络。下面在同一工作目录克隆两个仓库；`apply --check` 失败时先核对版本，停止应用补丁。

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

命令安装公开依赖并构建本地源码，不生成图片。MeiGen 原有 MIT 版权保留在 [UPSTREAM-LICENSE](UPSTREAM-LICENSE)。本例不复制整个上游项目到 ToAPIs 仓库。

## 2 配置自己的 Key

在仓库外创建 `C:/private/toapis.env`，自行填入 Key；这是示例路径，可替换。不要把私有文件提交 GitHub。

```dotenv
TOAPIS_API_KEY=YOUR_OWN_KEY
TOAPIS_BASE_URL=https://toapis.cn
```

国际网络可改 `https://toapis.com`。适配器允许 origin 或 `/v1`，统一拼接一次 `/v1`。营销短链不能填进 API Base。

在支持本地 stdio 的 MCP 客户端中添加下面配置，替换为实际绝对路径，再重新连接。这是配置示例，不是客户端 UI 截图。

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

免费连接检查：在 `meigen-toapis` 目录运行 `node toapis-smoke.mjs C:/private/toapis.env C:/work/verification list`。只初始化 MCP 与列出工具，不提交图片。

## 3 生成并保存一张图

明确调用 `generate_image`，使用如下实测输入。Agent 文字模型和费用由你的客户端决定，不属于本次图片 API 验收。

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

`provider=openai` 是原工具已有的 BYOK 入口；补丁会仅对 ToAPIs 地址增加异步处理，不能只换 Base 而省略补丁。可选命令 `node toapis-smoke.mjs C:/private/toapis.env C:/work/generated live` 会真正生成一张收费图片；脚本默认 list，必须明确写 live。

成功时应看到 `success=true`、`status=completed` 和可打开的 `savedPath`。检查保存文件尺寸与 task ID，及时保存临时结果 URL。不要把输出图片重新说成运行于远程 MeiGen Cloud。

## 4 复用成自己的商品图

先只替换 prompt 中的商品、场景与留白要求，保持模型、1K 与单张输出。提示词模板：`Commercial product photography of [your product], on [surface], with [lighting], [background], space for a headline added later. No text or logos.` 每次独立生成可能改变商品细节；这个预览不接受参考图，不能用于声称锁定真实商品结构。真实文案在图外或后期手工添加。

## 接口与失败处理

鉴权为 Bearer Key；POST `/v1/images/generations` 发 model、prompt、比例 size、resolution、n=1；取得任务 id 后 GET `/v1/images/generations/{id}`，completed 时读取 `result.data[0].url`、不带 API Key 下载。约 8 秒轮询，观察最多 10 分钟；提交 POST 不自动重试。超时或取消后先查询记录的 task ID，不马上重新生成。MeiGen Cloud 的 `check_generation` 不能查询 ToAPIs 任务。

首版只有 gpt-image-2 文生图；参考图、视频、云端 OAuth/积分、Cloud Skills 均未适配。2K/4K 参数可构造但未实测；其他模型会被适配器拒绝。素材没有用 MeiGen 参考上传服务，因为本例不提交参考图。不能以这条路径宣称整个产品全程离线。

## 验证与截图

固定上游 SHA `33ecb583c541652574c5875963d1225fa4ecf751`。2026-10-12 重检 TypeScript 编译、4 项适配测试与 28 项相关回归通过；测试使用 fixture，不产生收费生成。补丁可在固定版本应用，私有文件启动器已有工具连接记录。仅这一个真实成功案例，未进行吞吐或可靠性基准测试。

本教程的 [中文步骤截图](screenshots/) 为浏览器渲染的说明页，配真实 PNG 与输入示例，不冒充客户端或上游产品 UI。[English](README.md)
