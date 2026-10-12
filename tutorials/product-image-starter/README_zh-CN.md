# 先做出结果，再谈 BD：商品图生成与参考图改场景

这份教程已在 **2026-10-12** 真实运行：先生成一只虚构的橙色保温杯，再把它作为参考图改成暗色摄影场景。另附 TongFlow 已有 ToAPIs 插件的真实文生图 CLI 测试。

[English](README.md) · [用同款模型生成](https://go.toapis.com/1012_gh_product_tutorial) · [TongFlow 测试步骤](TONGFLOW.md)

| 文生图：明亮商品主图 | 参考图编辑：暗色摄影场景 |
|---|---|
| ![明亮商品图](assets/product-hero.png) | ![参考图改场景](assets/reference-edit.png) |

橙色杯身、黑色杯盖和主体轮廓可辨认地延续到第二张图。它适合展示创意场景变体；对真实商品的结构/标签准确性仍需人工审查，不能保证像素级一致。

## 三条命令开始

需要 Python 3.10+，脚本无需安装第三方库。

```powershell
python generate.py
# 在本机私有环境配置 TOAPIS_API_KEY，不要把 Key 提交到仓库。
python generate.py --live --out output/hero
python generate.py --live --reference output/hero/result.png --out output/edit
```

第一条只显示请求，不调用。每条 `--live` 只生成一张图片；默认模型固定 gpt-image-2、比例1:1、分辨率1k、n=1，地址为国内主机。第二次调用先上传第一张 PNG，再把返回 URL 放入 reference_images。国际网络可用 `--base-url https://toapis.com`。

真实私有配置文件也可通过 `--key-file` 指定，内容不复制到教程或记录。示例没有自动追加生成、没有批量默认任务，也不盲目重试付费 POST。任务已经提交后请保留 ID，使用 `--resume YOUR_TASK_ID` 查询原任务。

## 本次实测记录

| 用例 | 模型/输出 | 实测端到端耗时 |
|---|---|---:|
| 原创文生图 | gpt-image-2 / 1024×1024 PNG | 36.47秒 |
| 上传参考图→改场景 | 同模型 / 1024×1024 PNG | 46.31秒 |
| TongFlow image-gen CLI | 同模型 / success=true，PNG Asset | 46.70秒 |

时间包含轮询与下载，第二例还包含参考图上传。可复核的请求、时间、任务 ID、图片哈希在 [data/runs.json](data/runs.json)；公开记录去掉临时参考图 URL。

执行前通过该 Key 查询 GET /v1/pricing?model=gpt-image-2，1K、n=1报价为每次0.015美元；本轮三张图合计**按报价预估0.045美元**。返回没有给出确认结算金额，所以不能写“实扣0.045美元”或“免费”。实际扣费待账户用量核对，报价随时可能变化。[价格/结算合同](https://docs.toapis.com/docs/en/api-reference/account/pricing)

## 为什么这份可以先发布

输入、原创提示词、真实输出、可运行代码和任务证据都齐备，可以先用教程吸引有实际需求的开发者。BD 可随后围绕使用反馈和接入维护展开。本例不需要事先宣布与作者合作，也不需要 Fork 一个完整产品。

TongFlow 额外测试验证了固定插件版本的文生图 CLI 路线；未验收画布、编辑和视频，不把它写成“整个 TongFlow 已完全兼容”。Scumble、Banana Slides、MeiGen 也没有在本例中被宣称通过验收。

## 核心接口

- POST /v1/images/generations：提交后拿任务 id。
- POST /v1/uploads/images：本地参考 PNG 上传换 URL。
- GET /v1/images/generations/{id}：查询直至 completed / failed。
- completed 后读 result.data[].url，并及时下载。

[图片模型文档](https://docs.toapis.com/docs/en/api-reference/images/gpt-image-2/generation) · [上传](https://docs.toapis.com/docs/en/api-reference/uploads/images) · [查询](https://docs.toapis.com/docs/en/api-reference/tasks/image-status)

```bash
python -m unittest discover -s . -p test_generate.py
```

5项结构/故障检查已通过。它们与真实调用证据分开记录。本例提示词原创，商品为虚构无品牌生成图，不包括音视频，也不声称模型或项目正在 Trending。

[同款图片模型入口](https://go.toapis.com/1012_gh_product_tutorial) · [通用模型与价格页](https://x.toapis.com/1012_gh_product_tutorial_home)

