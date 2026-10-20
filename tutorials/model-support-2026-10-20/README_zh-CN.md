# 图片／视频模型支持、价格与真实案例

[English](README.md) · [中文](README_zh-CN.md)

报价核对：2026-10-20。图片案例日期2026-10-17；视频案例日期2026-10-20。表格按本例金额／秒金额排序，质量、分辨率和输入不同，不是同配置质量排名。图片日志的阶段未知，不能当作单任务最终净结算；当前报价与历史金额分别显示。视频金额均由billing=settled确认，$/s按实际文件时长折算，任务处理耗时不参与计算。Token模型不是固定每秒价，底层$/M只作小字补充。

gpt-image-2(VIP)通用价格为$0.0019/image起；本例low/1K为$0.0019/image。新脚本有31套历史成功图片请求模板、8套视频模板；当前26套图片与8套视频可匹配价格，另5套图片因当前Key缺价而默认阻止新付费调用。

## 图片：每张报价与历史案例金额

| 图片模型／实测档位 | 当前档位报价／张 | 历史案例金额／张 | 费用证据 |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | 当前Key暂未返回报价 | **$0.005272/image**<br><sub>Token计费；当前$/M未返回，本例金额不是固定单张价。</sub> | 任务回执已结算 |
| gpt-image-2.5-sunburst-vip<br><sub>low</sub> | 当前Key暂未返回报价 | **$0.005272/image**<br><sub>Token计费；当前$/M未返回，本例金额不是固定单张价。</sub> | 任务回执已结算 |
| gemini-2.5-flash-image-preview<br><sub>1K</sub> | $0.012/image | **$0.012/image** | 计费日志，阶段未知 |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | 计费日志，阶段未知 |
| flux-kontext-pro<br><sub>default</sub> | $0.02/image | **$0.02/image** | 计费日志，阶段未知 |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | 计费日志，阶段未知 |
| qwen-image-3.0<br><sub>1K</sub> | 当前Key暂未返回报价 | **$0.021/image** | 计费日志，阶段未知 |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | 计费日志，阶段未知 |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | 计费日志，阶段未知 |
| gemini-3.1-flash-image-preview<br><sub>1K</sub> | $0.025/image | **$0.025/image** | 计费日志，阶段未知 |
| qwen-image-3.0-pro<br><sub>1K</sub> | 当前Key暂未返回报价 | **$0.028/image** | 计费日志，阶段未知 |
| doubao-seedream-4-0<br><sub>1K</sub> | $0.0285/image | **$0.0285/image** | 计费日志，阶段未知 |
| gemini-3.1-flash-image-preview-vip<br><sub>1K</sub> | $0.03/image | **$0.03/image** | 计费日志，阶段未知 |
| nano_banana_2<br><sub>1K</sub> | $0.03/image | **$0.03/image** | 计费日志，阶段未知 |
| viduq2-fast<br><sub>1K</sub> | $0.030134/image | **$0.030134/image** | 计费日志，阶段未知 |
| doubao-seedream-5-0<br><sub>2K</sub> | $0.0315/image | **$0.0315/image** | 计费日志，阶段未知 |
| doubao-seedream-4-5<br><sub>2K</sub> | $0.0357/image | **$0.0357/image** | 计费日志，阶段未知 |
| flux-kontext-max<br><sub>default</sub> | $0.04/image | **$0.04/image** | 计费日志，阶段未知 |
| gemini-3-pro-image-preview<br><sub>1K</sub> | $0.04/image | **$0.04/image** | 计费日志，阶段未知 |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | 计费日志，阶段未知 |
| doubao-seedream-5-0-pro-global<br><sub>1K</sub> | 当前Key暂未返回报价 | **$0.045/image** | 计费日志，阶段未知 |
| gemini-3-pro-image-preview-vip<br><sub>1K</sub> | $0.05/image | **$0.05/image** | 计费日志，阶段未知 |
| nano_banana_pro<br><sub>1K</sub> | $0.05/image | **$0.05/image** | 计费日志，阶段未知 |
| viduq3-fast<br><sub>1K</sub> | $0.050223/image | **$0.050222/image** | 计费日志，阶段未知 |
| vidu-image<br><sub>1K</sub> | $0.066964/image | **$0.066964/image** | 计费日志，阶段未知 |
| flux-2-flex<br><sub>1K</sub> | $0.07/image | **$0.07/image** | 计费日志，阶段未知 |
| viduq2-pro<br><sub>1K</sub> | $0.100446/image | **$0.100446/image** | 计费日志，阶段未知 |

## 视频：本例实际消费与每秒金额

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

## 复用脚本

[31 image + 8 video preset client](client/README_zh-CN.md)

原生集成边界由各项目自己的ACCEPTANCE／README说明；本页API成功不能替代产品内验收。

## 真实输出

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

首帧视频使用各自原创PNG，具体来源见案例索引；MiniMax与Kling默认生成的音轨以文件实测为准，不把上游工具的TTS功能当作ToAPIs能力。
