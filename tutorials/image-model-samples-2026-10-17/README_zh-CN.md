# 同一提示词：图片模型价格与真实输出


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

[English](README.md) · [简体中文](README_zh-CN.md)

测试日期：**2026-10-17**。8 个模型使用同一条文生图提示词，每例 1 张，按本例消费金额从低到高排列。**gpt-image-2(VIP) $0.0019/image 起；本例 low/1K 为 $0.0019/image。**

金额来自任务结算回执或账号计费日志，逐行注明来源。阶段未知的日志不代表最终净结算；按模型/时间窗口匹配的记录尚未确认到单个任务。目录价是历史报价，不是锁价。gpt-image-2.5-flare-vip 按 Token 计费，**$0.005272 仅为这一张的已结算费用**，不是固定单张价；它与 gpt-image-2.5-flare 是不同 API ID。Qwen 的目录价未返回，只展示本例日志金额。

提示词相同，模型默认质量和实际分辨率不同；表内将请求与输出分别列出。Seedream Pro 请求 1K、未传 quality（报价档位 medium），实际返回 2048×2048。这组图片是独立 ToAPIs API 素材测试，不新增任何项目原生 Provider、UI、图片导入或视频的验收结论，也不计入下方历史项目消费小计。

| 模型 / API ID | 请求档位 → 实际尺寸 | 目录价（2026-10-17） | 本例消费金额 USD ↑ | 费用依据 | 真实输出 |
|---|---|---:|---:|---|---|
| gpt-image-2(VIP)<br><code>gpt-image-2-vip</code> | 1K / low → 1024×1024 | $0.0019/image | **$0.0019** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/gpt-image-2-vip.png"><img src="images/gpt-image-2-vip.png" width="112" alt="gpt-image-2(VIP) product image"></a> |
| gpt-image-2.5-flare-vip | 1024x1024 / low → 1024×1024 | 按 Token；Key 报价未返回 | **$0.005272** | 任务回执 settled | <a href="images/gpt-image-2.5-flare-vip.png"><img src="images/gpt-image-2.5-flare-vip.png" width="112" alt="gpt-image-2.5-flare-vip product image"></a> |
| nano_banana | 1K / default → 1024×1024 | $0.012/image | **$0.012** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/nano_banana.png"><img src="images/nano_banana.png" width="112" alt="nano_banana product image"></a> |
| gemini-nano-banana-2.1 | 1K / default → 1024×1024 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/gemini-nano-banana-2.1.jpg"><img src="images/gemini-nano-banana-2.1.jpg" width="112" alt="gemini-nano-banana-2.1 product image"></a> |
| gpt-image-2 | 1K / default → 1280×1280 | $0.015/image | **$0.015** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/gpt-image-2.png"><img src="images/gpt-image-2.png" width="112" alt="gpt-image-2 product image"></a> |
| qwen-image-3.0 | 1K / default → 1024×1024 | Key 报价未返回 | **$0.021** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/qwen-image-3.0.png"><img src="images/qwen-image-3.0.png" width="112" alt="qwen-image-3.0 product image"></a> |
| gpt-image-2.5-flare | 1K / high → 1024×1024 | $0.0225/image | **$0.0225** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/gpt-image-2.5-flare.png"><img src="images/gpt-image-2.5-flare.png" width="112" alt="gpt-image-2.5-flare product image"></a> |
| doubao-seedream-5-0-pro | 1K / default → 2048×2048 | $0.042857/image | **$0.042856** | 日志：模型/时间窗口候选；阶段未知 | <a href="images/doubao-seedream-5-0-pro.jpg"><img src="images/doubao-seedream-5-0-pro.jpg" width="112" alt="doubao-seedream-5-0-pro product image"></a> |

![8 models ordered by example amount](overview-cn.jpg)

[共同提示词、原图与费用来源](README_zh-CN.md) · [Pricing API](https://docs.toapis.com/docs/en/api-reference/account/pricing)

## 共同提示词

```text
Create a premium product advertising photograph, square composition. A matte ivory reusable water bottle with a brushed copper cap stands on a pale travertine pedestal. Exactly three small green leaves lie beside the bottle. One fresh orange cut in half sits on the right. Warm morning sunlight enters from the upper left, casting crisp botanical shadows on a terracotta backdrop. Subtle realistic condensation droplets, tactile materials, professional studio photography. On the front of the bottle print the word "DAYLIGHT" in clean dark green uppercase type. At the top of the composition add the short headline "MAKE ROOM FOR LIGHT" in elegant readable typography. Keep generous negative space, no other text, no watermark.
```

[请求参数与脱敏费用数据](samples.json)。这里列出真实独立 API 请求；使用各项目适配器前，仍需核对它的模型白名单及参数映射。
