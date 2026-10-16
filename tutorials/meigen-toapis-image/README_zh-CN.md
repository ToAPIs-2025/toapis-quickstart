# MeiGen 本地 MCP 生成商品图与保存结果

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## 模型类型、测试档位与花费

更新：2026-10-16。下表为已验证案例的历史档位与价格；本段补充不改变下方原批次记录。

| 模型（API ID） | 类型 | 测试档位 | 单次报价 | 已确认单次消费 | 数量 |
|---|---|---|---:|---:|---:|
| gpt-image-2 | 图片 | 1K / n=1 | $0.015/image | 未确认 | 1 |

历史图片实际消费尚未确认；报价不当作实扣。

补丁后的本地MCP文生图已验证；远程云端视频属于另一路线，未接入本补丁。
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

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
