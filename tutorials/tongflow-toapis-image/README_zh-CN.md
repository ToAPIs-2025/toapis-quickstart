# TongFlow ToAPIs 插件生成商品图与保存 PNG

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
