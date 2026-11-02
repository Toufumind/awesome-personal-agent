# 来源与核验记录

简体中文 | [English](SOURCES.en.md)

源码项目首批核验日期：**2026-10-31（UTC）**。产品与论文按各自条目记录日期，不因这份索引更新而视为全体重新核验。

本文件保留源码项目的文档核验记录，并规定产品与论文的证据口径。**这份目录本身不是产品评测报告或论文复现结果。**

## 来源索引

| 类型 | 条目与来源记录 | 本轮可以说明什么 |
| --- | --- | --- |
| 源码项目 | [README](../README.md) 与下方项目依据 | 官方文档描述了什么；不代表安装成功、代码安全或任务可靠 |
| 公开可用产品（含商业） | [PRODUCTS](PRODUCTS.md) 中每项官方来源与核验日期 | 官方公布的用途、入口、开放条件与收费；不代表每个账号/地区都可用 |
| Eval / Benchmark 论文 | [PAPERS](PAPERS.md) 的评测/基准组 | 在明确阅读范围内可确认的任务、环境、指标与局限 |
| Agent 方法 / 系统论文 | [PAPERS](PAPERS.md) 的方法/系统组 | 在明确阅读范围内可确认的机制与实验；原文成绩仍是作者报告 |

[任务协议](TASKS.md) 是尚未执行的试验设计，不是新增实测证据或统一 benchmark。

产品与论文条目的详细依据集中保存在各自目录，避免复制出两份不同步的可用性或阅读记录。

## 分类型核验口径

- **源码项目**：官方仓库与版本文档是功能/部署依据；公开代码、可安装、自托管与开源许可分别判断。
- **产品**：产品页用于用途，帮助/开放说明用于可用性，定价页用于费用；入口可访问不代表已注册、已开通或已验证任务。候补、邀请、受限预览与公开使用不得混写。
- **论文**：记录原文、版本/年份、发表或预印本状态、阅读范围与日期。只读摘要不得推断全文细节；全文阅读也不等于代码复现。
- **性能结果**：明确区分作者报告、厂商演示和有记录的独立实测。不跨不同模型、预算、任务集或版本直接比较数字。
- **证据缺口**：写明未确认、未读取或未测试，不把空白补成肯定结论；不同来源发生冲突时保留读取时间和边界。

## 源码项目依据

首批 14 项通过网页读取官方仓库 README，核对项目身份、主要用途、部署层次和明显限制。**没有安装、运行、代码审计、漏洞审计或基准测试**；也未穷尽所有操作系统、版本、价格与服务条款。下列“边界”包括由文档事实推导的选型提醒，不是对产品缺陷的测试结论。

| 项目 | 官方依据 | 本轮确认与采用的边界 |
| --- | --- | --- |
| Hermes Agent | [官方 README](https://github.com/NousResearch/hermes-agent#readme) | 读到记忆、会话检索、技能、调度与消息渠道介绍；不采纳“唯一”“成本几乎为零”等宣传比较。 |
| Khoj | [官方 README](https://github.com/khoj-ai/khoj#readme) | 读到文档/网页问答、自定义 Agent、重复研究任务与自托管/云部署；不将知识助理描述为通用 GUI 执行器。 |
| Letta Code | [当前源码 README](https://github.com/letta-ai/letta-code#readme)、[旧主仓库迁移说明](https://github.com/letta-ai/letta#readme) | 旧主仓库指向 `letta-code`；当前文档说明 CLI、记忆、渠道、调度及 local/Cloud 后端，因此使用新源码地址并提醒数据位置。 |
| nanobot | [官方 README](https://github.com/HKUDS/nanobot#readme) | 读到 WebUI/终端/聊天入口、文件工具、记忆、调度和自备模型；官方明确主分支 README 与稳定版可能不同。 |
| NanoClaw | [官方 README](https://github.com/nanocoai/nanoclaw#readme) | 旧地址 `qwibitai/nanoclaw` 跳转至 `nanocoai/nanoclaw`；文档描述容器执行、定制代码、按需渠道、记忆和定时任务。不重复其绝对化安全措辞。 |
| OpenClaw | [官方 README](https://github.com/openclaw/openclaw#readme) | 读到 Gateway、渠道、状态、模型与扩展机制；Security 节明确未配置沙箱时主会话工具在宿主机执行。 |
| Mika | [官方中文 README](https://github.com/wangzan101/Mika#readme)、[原始 README](https://raw.githubusercontent.com/wangzan101/Mika/main/README.md) | 读到后台屏、浏览器、沙箱、调度和 beta 提示；安装 Android 11+、推荐 14+、沙箱 arm64，模型请求发送给用户配置的服务商。App 操控最低系统版本的读取记录有差异，见下方复核说明。未采纳“任何 App 都能操作”的泛化承诺。 |
| Mobile-Agent | [官方 README](https://github.com/X-PLUG/MobileAgent#readme) | 这是多个版本、模型、论文及跨平台 GUI 项目的集合；归为研究/框架，不将单个演示的成功率推及整个系列。 |
| Mobilerun | [当前官方 README](https://github.com/droidrun/mobilerun#readme) | `droidrun/droidrun` 跳转至 `droidrun/mobilerun`；读到 CLI/Python、界面树/截图以及 Android/iOS 不同接入路径，区分框架和 Cloud。 |
| Agent Zero | [官方 README](https://github.com/agent0ai/agent-zero#readme) | 读到 Docker Linux 桌面、浏览器、项目、记忆与主机桥接；Safety Model 提醒隔离运行、限制挂载与审核敏感动作。 |
| Browser Use | [官方 README](https://github.com/browser-use/browser-use#readme) | 文档分别提供 Hosted Cloud、CLI 与 Python Library 路径；保留三者区别，不固定会变化的价格。 |
| UI-TARS Desktop / Agent TARS | [官方 README](https://github.com/bytedance/UI-TARS-desktop#readme) | Introduction 明确两个产品及其不同入口；不把远程演示或历史发布说明当作当前可用性保证。 |
| LangGraph | [官方 README](https://github.com/langchain-ai/langgraph#readme) | 读到有状态编排、持久执行、人工介入和记忆；定位为开发基础设施，而非消费级助理。 |
| Mem0 | [官方 README](https://github.com/mem0ai/mem0#readme) | 读到用户/会话/Agent 记忆与库、自托管、云平台路径；不引用其性能数字，也不将记忆层写成任务执行器。 |

<a id="original-projects-audit"></a>
### 首批 14 项：固定版本、根许可与发布复核

独立复核完成于 **2026-10-31 21:42 UTC**：通过官方 GitHub 仓库元数据确认规范地址及默认分支，读取该分支观察到的 commit、以完整 commit 固定的 README 和根 LICENSE，并检查 `releases/latest` 与最多 3 条近期发布记录。14 个规范地址均与上表一致，均观察到 `archived=false`；28 个固定文件均成功读取。下表为这次复核的可追溯证据；上表保留首次阅读的功能与限制记录，不把未固定的早期页面当成新 commit 的逐字快照。

commit 日期是源码提交日期，发布日期是 GitHub `published_at`（均为 UTC）；两者不表示同一代码版本。`latest` 是当时接口指定的非预发布条目，不保证是所有组件/分支按时间最新的版本，也不是成熟度或任务可靠性认证。除明确标出的预发布外，下表 latest 项均观察到 `prerelease=false`。根许可仅记录已读代码文件，不替代依赖、模型权重、品牌资产、数据及云服务条款核查；本仓库自身的文档许可另见[范围声明](LICENSE.md#zh)。**没有下载发行包、安装运行、验签、安全审计或任务实测。**

| 项目与根许可 | 固定官方证据（观察到的默认分支） | 发布记录与边界 |
| --- | --- | --- |
| Hermes Agent · MIT | `main` · [`c419cf7c864a`](https://github.com/NousResearch/hermes-agent/commit/c419cf7c864ac0ee511dbd9f7091a8bba0b567ee) (2026-10-31 UTC) · [README.md](https://github.com/NousResearch/hermes-agent/blob/c419cf7c864ac0ee511dbd9f7091a8bba0b567ee/README.md) · [LICENSE](https://github.com/NousResearch/hermes-agent/blob/c419cf7c864ac0ee511dbd9f7091a8bba0b567ee/LICENSE) | latest [v0.22.5](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5) (2026-10-23 UTC). 未安装或验证技能、渠道及模型配置。 |
| Khoj · GNU AGPL v3 | `master` · [`ae229ca894c0`](https://github.com/khoj-ai/khoj/commit/ae229ca894c0b80ad84664afcfdde523b5e87057) (2026-08-02 UTC) · [README.md](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/README.md) · [LICENSE](https://github.com/khoj-ai/khoj/blob/ae229ca894c0b80ad84664afcfdde523b5e87057/LICENSE) | latest [2.0.0-beta.28](https://github.com/khoj-ai/khoj/releases/tag/2.0.0-beta.28) (2026-03-26 UTC). 标签含 **beta**，即使 API 标为 `prerelease=false` 也不改写为成熟版。根文件为 GNU AGPL v3 正文；未据此进一步断言 `-only` 或 `-or-later`。 |
| Letta Code · Apache-2.0（代码；品牌资产除外） | `main` · [`91897d5c4b0b`](https://github.com/letta-ai/letta-code/commit/91897d5c4b0b6b61d3b2c8df09ff7d86345e2b2e) (2026-10-31 UTC) · [README.md](https://github.com/letta-ai/letta-code/blob/91897d5c4b0b6b61d3b2c8df09ff7d86345e2b2e/README.md) · [LICENSE](https://github.com/letta-ai/letta-code/blob/91897d5c4b0b6b61d3b2c8df09ff7d86345e2b2e/LICENSE) | latest [v0.34.36](https://github.com/letta-ai/letta-code/releases/tag/v0.34.36) (2026-10-31 UTC). 根文件另有 **Brand Assets Exclusion**：Letta / Letta Code 名称、标志、文字标识、图片和 ASCII 图形不在该 Apache 许可授权内。代码许可不等于品牌资产许可。 |
| nanobot · MIT | `main` · [`8b37976d36c2`](https://github.com/HKUDS/nanobot/commit/8b37976d36c2812c62b464321e729a88872b60f9) (2026-10-31 UTC) · [README.md](https://github.com/HKUDS/nanobot/blob/8b37976d36c2812c62b464321e729a88872b60f9/README.md) · [LICENSE](https://github.com/HKUDS/nanobot/blob/8b37976d36c2812c62b464321e729a88872b60f9/LICENSE) | latest [v0.4.0](https://github.com/HKUDS/nanobot/releases/tag/v0.4.0) (2026-10-28 UTC). 默认分支文档可能领先发布包；功能须按安装版本复核。 |
| NanoClaw · MIT | `main` · [`acc2b1c8f52a`](https://github.com/nanocoai/nanoclaw/commit/acc2b1c8f52a954368cfaf04b61c32f9a1efc280) (2026-10-26 UTC) · [README.md](https://github.com/nanocoai/nanoclaw/blob/acc2b1c8f52a954368cfaf04b61c32f9a1efc280/README.md) · [LICENSE](https://github.com/nanocoai/nanoclaw/blob/acc2b1c8f52a954368cfaf04b61c32f9a1efc280/LICENSE) | latest [v2026.10.0](https://github.com/nanocoai/nanoclaw/releases/tag/v2026.10.0) (2026-10-09 UTC). 另见预发布 [v2026.10.1-rc.2](https://github.com/nanocoai/nanoclaw/releases/tag/v2026.10.1-rc.2)（2026-10-22 UTC，`prerelease=true`）；不要与 latest 混为一版。 |
| OpenClaw · MIT | `main` · [`d431ea3ef802`](https://github.com/openclaw/openclaw/commit/d431ea3ef802ccb7d9eba984e5b4e0e72e3fc004) (2026-10-31 UTC) · [README.md](https://github.com/openclaw/openclaw/blob/d431ea3ef802ccb7d9eba984e5b4e0e72e3fc004/README.md) · [LICENSE](https://github.com/openclaw/openclaw/blob/d431ea3ef802ccb7d9eba984e5b4e0e72e3fc004/LICENSE) | latest [v2026.10.9](https://github.com/openclaw/openclaw/releases/tag/v2026.10.9) (2026-10-29 UTC). 另见 [v2026.10.10-beta.5](https://github.com/openclaw/openclaw/releases/tag/v2026.10.10-beta.5)（2026-10-30 UTC，`prerelease=true`）及 [v2026.9.36](https://github.com/openclaw/openclaw/releases/tag/v2026.9.36)（2026-10-29 UTC）。latest 指定项不等于按发布时间排序的全部分支版本。 |
| Mika · Apache-2.0 | `main` · [`279a5cae405a`](https://github.com/wangzan101/Mika/commit/279a5cae405ac83106b47af9c2794ebfa3333a57) (2026-10-31 UTC) · [README.md](https://github.com/wangzan101/Mika/blob/279a5cae405ac83106b47af9c2794ebfa3333a57/README.md) · [LICENSE](https://github.com/wangzan101/Mika/blob/279a5cae405ac83106b47af9c2794ebfa3333a57/LICENSE) | latest [v0.1.27](https://github.com/wangzan101/Mika/releases/tag/v0.1.27) (2026-10-31 UTC). 发布含 1 个 APK 资产，未下载、安装或验签；`prerelease=false` 不抹去早期测试提示及系统要求快照差异，见下节。 |
| Mobile-Agent · MIT | `main` · [`81fa28b564ef`](https://github.com/X-PLUG/MobileAgent/commit/81fa28b564ef7a695521500bc15a0e1324b2b394) (2026-10-28 UTC) · [README.md](https://github.com/X-PLUG/MobileAgent/blob/81fa28b564ef7a695521500bc15a0e1324b2b394/README.md) · [LICENSE](https://github.com/X-PLUG/MobileAgent/blob/81fa28b564ef7a695521500bc15a0e1324b2b394/LICENSE) | [latest 接口](https://api.github.com/repos/X-PLUG/MobileAgent/releases/latest) 返回 404；[发布集合](https://api.github.com/repos/X-PLUG/MobileAgent/releases?per_page=3) 为空。 未观察到 GitHub release，不代表没有可运行代码、模型或其他分发渠道；模型权重许可须另查。 |
| Mobilerun · MIT | `main` · [`11dcdebdec9e`](https://github.com/droidrun/mobilerun/commit/11dcdebdec9ea99f172dd7e80af7ba1eadbeb6c8) (2026-10-28 UTC) · [README.md](https://github.com/droidrun/mobilerun/blob/11dcdebdec9ea99f172dd7e80af7ba1eadbeb6c8/README.md) · [LICENSE](https://github.com/droidrun/mobilerun/blob/11dcdebdec9ea99f172dd7e80af7ba1eadbeb6c8/LICENSE) | latest [v0.7.4](https://github.com/droidrun/mobilerun/releases/tag/v0.7.4) (2026-10-27 UTC). 框架发布号不等于 Portal、设备平台或 Cloud 服务的统一版本。 |
| Agent Zero · MIT | `main` · [`ff2a5b9c9c4e`](https://github.com/agent0ai/agent-zero/commit/ff2a5b9c9c4e490ba38dd7c313e779510bb2071a) (2026-10-13 UTC) · [README.md](https://github.com/agent0ai/agent-zero/blob/ff2a5b9c9c4e490ba38dd7c313e779510bb2071a/README.md) · [LICENSE](https://github.com/agent0ai/agent-zero/blob/ff2a5b9c9c4e490ba38dd7c313e779510bb2071a/LICENSE) | latest [v2.14](https://github.com/agent0ai/agent-zero/releases/tag/v2.14) (2026-10-13 UTC). MIT 来自实际根 LICENSE 正文，不依赖 GitHub 徽章识别；未安装或检查容器运行时。 |
| Browser Use · MIT | `main` · [`b49a68e4060a`](https://github.com/browser-use/browser-use/commit/b49a68e4060acb226da8f784194fef301c53a6d7) (2026-10-30 UTC) · [README.md](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/README.md) · [LICENSE](https://github.com/browser-use/browser-use/blob/b49a68e4060acb226da8f784194fef301c53a6d7/LICENSE) | latest [0.13.14](https://github.com/browser-use/browser-use/releases/tag/0.13.14) (2026-10-26 UTC). 发布号对应仓库版本，不是托管浏览器或 Cloud 服务的统一版本。 |
| UI-TARS Desktop / Agent TARS · Apache-2.0 | `main` · [`3ac2cb8d946d`](https://github.com/bytedance/UI-TARS-desktop/commit/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c) (2026-10-09 UTC) · [README.md](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/README.md) · [LICENSE](https://github.com/bytedance/UI-TARS-desktop/blob/3ac2cb8d946d78d5ff92ad17b318eaafa18c178c/LICENSE) | latest [v0.3.1](https://github.com/bytedance/UI-TARS-desktop/releases/tag/v0.3.1) (2026-10-08 UTC). 同仓库含多个入口；历史 [v0.3.0-beta.12](https://github.com/bytedance/UI-TARS-desktop/releases/tag/v0.3.0-beta.12) 也标为 `prerelease=false`，不能用该布尔值消除 beta 限制。 |
| LangGraph · MIT | `main` · [`e5c961d7fbe7`](https://github.com/langchain-ai/langgraph/commit/e5c961d7fbe7ca6fdd4c94c84d90511372514d55) (2026-10-31 UTC) · [README.md](https://github.com/langchain-ai/langgraph/blob/e5c961d7fbe7ca6fdd4c94c84d90511372514d55/README.md) · [LICENSE](https://github.com/langchain-ai/langgraph/blob/e5c961d7fbe7ca6fdd4c94c84d90511372514d55/LICENSE) | latest [1.2.19](https://github.com/langchain-ai/langgraph/releases/tag/1.2.19) (2026-10-30 UTC). 发布集合另有 [sdk==0.4.11](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.11) 与 [checkpointsqlite==3.1.3](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite%3D%3D3.1.3)；不是全部组件共用一个版本。 |
| Mem0 · Apache-2.0 | `main` · [`753496cf1435`](https://github.com/mem0ai/mem0/commit/753496cf1435d76c3a711f3af51303f7fdcb6420) (2026-10-30 UTC) · [README.md](https://github.com/mem0ai/mem0/blob/753496cf1435d76c3a711f3af51303f7fdcb6420/README.md) · [LICENSE](https://github.com/mem0ai/mem0/blob/753496cf1435d76c3a711f3af51303f7fdcb6420/LICENSE) | latest [ts-v3.3.1](https://github.com/mem0ai/mem0/releases/tag/ts-v3.3.1) (2026-09-25 UTC). latest 标题为 Node SDK；另有 Python SDK [v2.2.1](https://github.com/mem0ai/mem0/releases/tag/v2.2.1)（2026-09-25 UTC）。不能把 TS / Node 标签当作 Python、托管服务和整个项目的统一版本。 |

### Mika 系统要求复核

- **2026-10-31 20:35 UTC**：重新读取官方仓库首页和原始 README，系统要求表为安装/聊天/网页/沙箱 Android 11+、App 操控 Android 12+，推荐 Android 14+；FAQ 与该表一致。
- 同日 **01:59 UTC** 的较早阅读记录曾显示任务需 Android 13+。两个时点的页面证据存在差异，未固定到同一 commit，不能据此断言具体哪次发布调整了要求。
- **2026-10-31 21:42 UTC**：本次[固定 README](https://github.com/wangzan101/Mika/blob/279a5cae405ac83106b47af9c2794ebfa3333a57/README.md)（commit `279a5cae405a`）写明聊天/网页/文件 Android 11+、手机 App 操控 Android 12+、推荐 Android 14+，Linux 沙箱仅 arm64；这是当前源码快照，不追溯替换前两次未固定的记录。[v0.1.27](https://github.com/wangzan101/Mika/releases/tag/v0.1.27) 于 21:22:13 UTC 发布、`prerelease=false`，不能单凭该标记推翻早期测试提示或证明兼容性。
- 因此 README 保留共同明确的安装要求与推荐版本，将 App 操控最低版本写为**按所装版本文档核对**，不把任一主分支快照当作所有发布版本的兼容承诺。

<a id="expansion"></a>
## 项目扩充：固定来源与发布边界

核验日期：**2026-10-31 UTC**。新增 **15 项（12 项主分类 + 3 项单列预览）**，全部观察到 `archived=false`；这不代表活跃度或可靠性。README/许可按观察到的默认分支 commit 固定；15 个固定 README 与首次读取的 blob SHA 一致。除 README 外仅做必要的构建设置、工具或官方验证文档定点读取，**未安装、未执行、未跑基准、未验签或审计安全**。

发布状态来自官方发布集合及 latest 接口。`latest` 返回 404 仅表示没有该接口的非预发布条目，不表示没有任何预发布；`prerelease=false` 也不覆盖上游 beta/早期警告。固定 README 可能领先发布包，未进行逐项安装验收。以下根许可只说明已读代码文件，不重新授权模型、依赖、商标、数据或服务，与本仓库的[文档许可](LICENSE.md#zh)分开处理。

| 项目及根许可 | 固定官方依据 | 发布记录与核验边界 |
| --- | --- | --- |
| Operit · LGPL-3.0-only（主代码） | [README.md](https://github.com/AAswordman/Operit/blob/dbf71916fae9750cfdc9f9a774f5a0fee56633fb/README.md) · [LICENSE](https://github.com/AAswordman/Operit/blob/dbf71916fae9750cfdc9f9a774f5a0fee56633fb/LICENSE) · [app/build.gradle.kts](https://github.com/AAswordman/Operit/blob/dbf71916fae9750cfdc9f9a774f5a0fee56633fb/app/build.gradle.kts) | 非预发布 [v1.12.2](https://github.com/AAswordman/Operit/releases/tag/v1.12.2) (2026-09-18 UTC). 构建文件核对 Android 8.0+ / ARM64；根许可只覆盖相应主代码，设备权限与模型数据流另看。 |
| Open-AutoGLM · Apache-2.0（仓库代码） | [README.md](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/README.md) · [LICENSE](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/LICENSE) · [resources/privacy_policy.txt](https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/resources/privacy_policy.txt) | latest 无非预发布条目; [发布集合为空](https://api.github.com/repos/zai-org/Open-AutoGLM/releases?per_page=3). 研究框架；读取各平台设置、模型、操作回调和隐私说明。发布集合为空，不是 APK；模型权重许可另查。 |
| QwenPaw（原 CoPaw） · Apache-2.0 | [README.md](https://github.com/agentscope-ai/QwenPaw/blob/c26d31c0688aa9cce9bc1aef688177d2e14e25df/README.md) · [LICENSE](https://github.com/agentscope-ai/QwenPaw/blob/c26d31c0688aa9cce9bc1aef688177d2e14e25df/LICENSE) | 非预发布 [v2.2.2.post1](https://github.com/agentscope-ai/QwenPaw/releases/tag/v2.2.2.post1) (2026-10-22 UTC); 所见预发布 [v2.3.0-beta.1](https://github.com/agentscope-ai/QwenPaw/releases/tag/v2.3.0-beta.1) (2026-10-27 UTC). 读取渠道、桌面 Beta、权限层与遥测说明；`--defaults` 接受文档声明的遥测。CoPaw 是同一仓库，不重复计数。 |
| LobsterAI（有道龙虾） · MIT | [README.md](https://github.com/netease-youdao/LobsterAI/blob/da88493b5a8d3a977c82a13901bbe99ad162393a/README.md) · [LICENSE](https://github.com/netease-youdao/LobsterAI/blob/da88493b5a8d3a977c82a13901bbe99ad162393a/LICENSE) | 非预发布 [2026.10.30](https://github.com/netease-youdao/LobsterAI/releases/tag/2026.10.30) (2026-10-31 UTC). 当前采用 OpenClaw 运行时；发布标签日期与 UTC 实际发布日期不同。会话本地存储不代表模型/插件完全离线。 |
| OpenWorker · MIT | [README.md](https://github.com/andrewyng/openworker/blob/bea25db6f2034ec3093933a267f5933cbea04cd5/README.md) · [LICENSE](https://github.com/andrewyng/openworker/blob/bea25db6f2034ec3093933a267f5933cbea04cd5/LICENSE) | 非预发布 [v0.3.1](https://github.com/andrewyng/openworker/releases/tag/v0.3.1) (2026-10-05 UTC). README 明确 open beta，Windows 构建未代码签名；安装资产与设计说明不是审批/沙箱已通过安全验证。 |
| Rowboat · Apache-2.0 | [README.md](https://github.com/rowboatlabs/rowboat/blob/5f2af08bbf0ff9176d9224fa9b79c4a77798b669/README.md) · [LICENSE](https://github.com/rowboatlabs/rowboat/blob/5f2af08bbf0ff9176d9224fa9b79c4a77798b669/LICENSE) | 非预发布 [v1.0.3](https://github.com/rowboatlabs/rowboat/releases/tag/v1.0.3) (2026-09-17 UTC); 所见预发布 [v1.0.5](https://github.com/rowboatlabs/rowboat/releases/tag/v1.0.5) (2026-09-30 UTC). 非预发布 v1.0.3 与所见预发布 v1.0.5 分开；当前 Spaces/Harbor 文档不自动适用于稳定安装包。 |
| AnythingLLM · MIT | [README.md](https://github.com/Mintplex-Labs/anything-llm/blob/9caf2b4c29d9782f1cba4142be2525ebfa0ecd43/README.md) · [LICENSE](https://github.com/Mintplex-Labs/anything-llm/blob/9caf2b4c29d9782f1cba4142be2525ebfa0ecd43/LICENSE) · [server/utils/agents/aibitat/plugins/create-files/index.js](https://github.com/Mintplex-Labs/anything-llm/blob/9caf2b4c29d9782f1cba4142be2525ebfa0ecd43/server/utils/agents/aibitat/plugins/create-files/index.js) | 非预发布 [v1.19.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) (2026-10-26 UTC). 除 README 外定点读取 create-files 工具，确认 PDF/DOCX/XLSX/PPTX/文本注册；未实际生成或检查产物。桌面/Docker 权限与遥测另辨。 |
| goose · Apache-2.0 | [README.md](https://github.com/aaif-goose/goose/blob/b23d21cabd9b4de0c045dcdd731821a3a15c2bfc/README.md) · [LICENSE](https://github.com/aaif-goose/goose/blob/b23d21cabd9b4de0c045dcdd731821a3a15c2bfc/LICENSE) · [documentation/docs/guides/file-management.md](https://github.com/aaif-goose/goose/blob/b23d21cabd9b4de0c045dcdd731821a3a15c2bfc/documentation/docs/guides/file-management.md) · [documentation/docs/guides/running-tasks.md](https://github.com/aaif-goose/goose/blob/b23d21cabd9b4de0c045dcdd731821a3a15c2bfc/documentation/docs/guides/running-tasks.md) · [documentation/docs/guides/managing-tools/tool-permissions.md](https://github.com/aaif-goose/goose/blob/b23d21cabd9b4de0c045dcdd731821a3a15c2bfc/documentation/docs/guides/managing-tools/tool-permissions.md) | 非预发布 [v1.57.0](https://github.com/aaif-goose/goose/releases/tag/v1.57.0) (2026-10-28 UTC). 当前 general-purpose 定位及文件/任务/工具权限文档已读；block/goose 是重定向，不重复计数。未测任何扩展执行。 |
| IronClaw · MIT OR Apache-2.0 | [README.md](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/README.md) · [LICENSE-MIT](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/LICENSE-APACHE) · [FEATURE_PARITY.md](https://github.com/nearai/ironclaw/blob/b0b999d96781516ee05e6ba961d6f3ead900da96/FEATURE_PARITY.md) | 非预发布 [ironclaw-v1.4.1](https://github.com/nearai/ironclaw/releases/tag/ironclaw-v1.4.1) (2026-09-29 UTC); 所见预发布 [ironclaw-v1.4.1-rc.2](https://github.com/nearai/ironclaw/releases/tag/ironclaw-v1.4.1-rc.2) (2026-09-24 UTC). 双许可证均读取；FEATURE_PARITY 有部分/未实现项且时间早于当前文档，不能称完全对等；WASM 不等于所有工具隔离或提示注入免疫。 |
| Moltis · MIT | [README.md](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/README.md) · [LICENSE.md](https://github.com/moltis-org/moltis/blob/8a12400dc10551dfb9a6b568414b91a343ef2d5d/LICENSE.md) | 非预发布 [20261023.01](https://github.com/moltis-org/moltis/releases/tag/20261023.01) (2026-10-23 UTC). 根许可实际文件为 LICENSE.md；读取安装、认证、容器 socket 与远程执行配置。未下载或验签发行包。 |
| PicoClaw · MIT | [README.md](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/README.md) · [LICENSE](https://github.com/sipeed/picoclaw/blob/bbf6893ca7afad27f1d00a0f5a45982a549c6ed6/LICENSE) | 非预发布 [v0.3.1](https://github.com/sipeed/picoclaw/releases/tag/v0.3.1) (2026-07-03 UTC); 所见预发布 [nightly](https://github.com/sipeed/picoclaw/releases/tag/nightly) (2026-07-02 UTC). 官方警告 v1.0 前勿部署生产；低内存数字有不同构建限定，未作为本仓库实测引用。Android 入口不证明任意 App 操控。 |
| ZeroClaw · MIT OR Apache-2.0 | [README.md](https://github.com/zeroclaw-labs/zeroclaw/blob/1c1cd118ac536a1dd1bc79b9cce69cbdc04e4f29/README.md) · [LICENSE-MIT](https://github.com/zeroclaw-labs/zeroclaw/blob/1c1cd118ac536a1dd1bc79b9cce69cbdc04e4f29/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/zeroclaw-labs/zeroclaw/blob/1c1cd118ac536a1dd1bc79b9cce69cbdc04e4f29/LICENSE-APACHE) | 非预发布 [v0.8.7](https://github.com/zeroclaw-labs/zeroclaw/releases/tag/v0.8.7) (2026-10-27 UTC). 双许可证均读取；核对 supervised 默认及 YOLO 放宽路径、SOP/硬件与模型配置。不将列出的渠道/硬件当成已验收。 |
| Leon · MIT | [README.md](https://github.com/leon-ai/leon/blob/54180f99e17c7dcb062a0c98b06562b7b66597e5/README.md) · [LICENSE.md](https://github.com/leon-ai/leon/blob/54180f99e17c7dcb062a0c98b06562b7b66597e5/LICENSE.md) | latest 无非预发布条目; 所见预发布 [tcp-server_v2.0.0](https://github.com/leon-ai/leon/releases/tag/tcp-server_v2.0.0) (2026-02-19 UTC). develop 为 2.0 Developer Preview，旧 master 为不同架构；新文档未完成，已见发布为桥接/服务预发布组件，非完整成品。 |
| OpenMuse · MIT | [README.md](https://github.com/CopilotKit/openmuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/README.md) · [LICENSE](https://github.com/CopilotKit/openmuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/LICENSE) · [docs/VERIFICATION.md](https://github.com/CopilotKit/openmuse/blob/a4944f4c471d3dc93b8bfc060b5da309b5216ab2/docs/VERIFICATION.md) | latest 无非预发布条目; [发布集合为空](https://api.github.com/repos/CopilotKit/openmuse/releases?per_page=3). Alpha；需 Intelligence project key。读取官方 VERIFICATION 边界，但这是上游自报，未独立复现；示例、JS 导出不代表真实账号或签名移动 App 验收。 |
| Operit2 · AGPL-3.0（根许可） | [README.md](https://github.com/AAswordman/Operit2/blob/f476f4357b3323ae27f89038ad51a30b31cce383/README.md) · [LICENSE](https://github.com/AAswordman/Operit2/blob/f476f4357b3323ae27f89038ad51a30b31cce383/LICENSE) | latest 无非预发布条目; 所见预发布 [v2.0.0-preview.3](https://github.com/AAswordman/Operit2/releases/tag/v2.0.0-preview.3) (2026-06-28 UTC). Preview；preview.3 为四个 Linux/Windows CLI 包，其余平台有源码/构建路径。跨设备续接边界、权限与未完成 Server 产品均保留。 |

### 未纳入本次主清单的边界候选

15 个已选候选均已整合；以下是研究过程中另行发现、没有为凑数量纳入的项目。

- **Mycroft Core**：官方记录已归档，README 明示不再维护且可能无法运行；保留历史学习价值，不推荐新装。[README](https://github.com/MycroftAI/mycroft-core/blob/dev/README.md)
- **Suna / Kortix CompanyOS**：当前定位偏公司操作系统，不作为本次个人助理补充；根许可为 **Elastic License 2.0（ELv2，source-available，不称开源许可）**，不能沿用旧 MIT 叙述。[README](https://github.com/kortix-ai/suna/blob/dev/README.md) · [LICENSE](https://github.com/kortix-ai/suna/blob/dev/LICENSE)
- **Open Interpreter**：当前主线定位编码 Agent，不沿用旧 Python 时代的通用助理描述，暂不加入本次个人助理扩充。[README](https://github.com/openinterpreter/openinterpreter/blob/main/README.md)
- **simular-ai/simular**：候选仓库查询返回 404，仅保留为未解决的身份/访问问题，不推断不存在、许可、停更或产品可用性。

<a id="personal-work-additions"></a>
## 个人聊天与桌面工作补充：AstrBot、Eigent

核验日期：**2026-10-31 UTC**。本轮新增 **2 项主分类条目**：AstrBot 归入常驻个人助理，Eigent 归入桌面知识与办公助理；不改写上方首轮 15 项的历史记录。通过官方仓库读取下列固定 commit 的 README、根许可及 Eigent 本地部署指南，并选读 AstrBot 官方沙箱文档与两者发布页面。沙箱网页和发布页是当日可变页面观察，不声称与固定代码逐字同版。**仅文档核验；未安装、未执行项目代码、未连接账号、未跑任务或基准、未下载验签发行包、未审计安全。** 许可只指读取的仓库根文件，不自动覆盖模型、插件、依赖、商标或服务；AGPL v3 正文不进一步推定为 `-only` 或 `-or-later`。

| 项目及根许可 | 固定官方依据 | 发布记录与核验边界 |
| --- | --- | --- |
| AstrBot · AGPL-3.0（根许可） | `master` · `831abae85da8b6e58dc44d4544d163f8f9459ba1` · [README.md](https://github.com/AstrBotDevs/AstrBot/blob/831abae85da8b6e58dc44d4544d163f8f9459ba1/README.md) · [LICENSE](https://github.com/AstrBotDevs/AstrBot/blob/831abae85da8b6e58dc44d4544d163f8f9459ba1/LICENSE) · [沙箱 / Sandbox](https://docs.astrbot.app/use/astrbot-agent-sandbox.html) | 官方[发布页面](https://github.com/AstrBotDevs/AstrBot/releases)观察到 [v4.29.4](https://github.com/AstrBotDevs/AstrBot/releases/tag/v4.29.4)，不将主分支全部功能视为该包已验证能力。Python 3.12/uv 或 Docker；模型与渠道需配置。沙箱文档说明 macOS Seatbelt、Linux bubblewrap 与 Docker 内隔离的不同前提；Windows 暂无本机隔离，第三方沙箱为技术预览。按实际权限、挂载和网络配置核对，不从“沙箱”推断安全。消息平台、云模型与插件的数据流分别检查；WhatsApp 仍标为 Coming Soon，不作为已交付渠道。 |
| Eigent · Apache-2.0 | `main` · `17131f5d3e83d8680a3af5eb9b666afb6ea37c2b` · [README.md](https://github.com/eigent-ai/eigent/blob/17131f5d3e83d8680a3af5eb9b666afb6ea37c2b/README.md) · [LICENSE](https://github.com/eigent-ai/eigent/blob/17131f5d3e83d8680a3af5eb9b666afb6ea37c2b/LICENSE) · [server/README_EN.md](https://github.com/eigent-ai/eigent/blob/17131f5d3e83d8680a3af5eb9b666afb6ea37c2b/server/README_EN.md) | 官方[发布页面](https://github.com/eigent-ai/eigent/releases)观察到 [v1.0.7](https://github.com/eigent-ai/eigent/releases/tag/v1.0.7)。README 的云连接快速启动需注册；独立本地后端是另一条路径。本地指南列 Docker Desktop、Python 3.12、Node >=18 且 <23，并使用 FastAPI/PostgreSQL；配置云模型或远程 MCP 时请求仍会外发。入站 webhook 需公网 HTTPS。没有把 README 的零依赖/完全隔离宣传作为已验证事实，也未验证安装包平台覆盖或文件操作可靠性。 |

## 候选发现与相关清单

实际查看了以下清单，仅用于了解覆盖范围与发现候选项目；本仓库的项目描述依据上表官方来源独立撰写。

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents)：常驻助理、记忆层、运行时、消息桥接。
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents)：自托管和商业方案、选型维度。
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices)：产品、用例、源码及研究，含中英文。

## 核验范围和维护约定

- README 源码板块目前为 **34 项：31 个主分类条目 + 3 个单列预览条目**，覆盖六类主要用途和一个预览区。初始 14 项保留，首轮新增 15 项，个人工作新增 2 项，家居 / 可穿戴再增 2 项、[Octop](#octop) 再增 1 项（合计新增 20 项）；不含产品与论文目录，不是完整市场盘点。
- 不以 Star、commit 时间或量化可靠性作排名；固定 commit 只用于追溯证据，不是活跃度指标。本轮未核实的指标不作推断。
- 参考主分支 README 不代表所有版本均支持该能力，安装前应再次核对具体版本。
- 网页可读取只说明来源当时可访问，不说明软件安全、服务可用或未来链接稳定。
- 产品目录和论文目录的新增，不表示原有源码项目经过再次实测，也不把研究系统自动认定为公开可用产品。
- 更新某条目时同步更改其来源与核验日期。若只复查了一部分，不应把整份清单的核验日期整体刷新。
- 维护者已选择 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) 用于原创文档文字与原创编选内容，并选择 [MIT](../scripts/LICENSE) 用于本仓库原创脚本与测试代码；适用文件和排除项见 [docs/LICENSE.md](LICENSE.md#zh)。MIT 正文于 2026-10-31 核对 [OSI 官方文本](https://opensource.org/license/mit)，不代表重新核验上表项目。第三方材料与商标保留自身条款；独立机器可读夹具和结果模板没有因此获许。未添加覆盖整个仓库的根 `LICENSE`，也不是全仓库双重许可。

<a id="deepseek-superagent"></a>
## 实验性相关项目：dsh-superagent

**文档核验：2026-11-01（UTC）**。DeepSeek 团队的 [官方仓库 README](https://github.com/deepseek-ai/dsh-superagent-prototype#readme) 与 [MIT 许可](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/LICENSE) 表明：这是基于 DeepSeek Harness、面向单个 GitHub 仓库的主动编程研究原型，可选接入飞书；并非正式 DeepSeek 产品或生产就绪软件，文章中的部分设计尚未实现。[仓库元数据](https://api.github.com/repos/deepseek-ai/dsh-superagent-prototype) 的创建时间为 **2026-10-31 09:32:46 UTC**，不作为文章或产品发布日期。

因本仓库主清单不收纯编程工具，此处仅作实验性架构参考，**不计入 34 个源码项目**。仅核验文档，未安装、运行、审计或复现实验；不将内部实例与公开原型的能力等同。

<a id="home-voice-additions"></a>
## 家居 / 可穿戴新增：Home Assistant Assist 与 Omi

**2026-11-01（UTC），仅官方文档核验。** 新增 2 个源码项目，不新增商业产品计数。读取下列可变文档与根许可，未固定完整源码 commit 或核实发布包；未安装、购买、连接账户、录音或执行任务。原有条目保留原核验日期。根许可不自动覆盖模型、硬件、依赖和托管服务。

- **Home Assistant Assist:** [Assist](https://www.home-assistant.io/voice_control/) · [Architecture](https://contributors.home-assistant.io/architecture/platform/voice/) · [Ollama](https://www.home-assistant.io/integrations/ollama/) · [Cloud API](https://www.home-assistant.io/integrations/openai_conversation/) · [Apache-2.0](https://github.com/home-assistant/core/blob/dev/LICENSE.md). 收录配置后的家居控制路径，不是通用助理。Ollama 控制属实验性；Voice Preview Edition 是硬件名称，不代表 Assist 全部处于预览。
- **Omi:** [README](https://github.com/BasedHardware/omi#readme) · [MIT](https://github.com/BasedHardware/omi/blob/main/LICENSE) · [Overview](https://help.omi.me/en/articles/13135007-overview) · [Apps](https://help.omi.me/en/articles/13153599-omi-apps) · [Recording consent](https://help.omi.me/en/articles/13153576-using-omi-with-phone-only) · [Privacy](https://www.omi.me/pages/privacy). 须区分采集、记忆、任务生成与外部执行。源码快速启动连接云，不保证离线或零留存。未核实所有第三方 Apps 权限、后台清除时限、完整地区和收费。

Omi 正式隐私政策生效日期为 **2026-10-31**：可能加密保存会话音频以支持回放等功能，不能沿用旧帮助文档的“不保留音频”说法；训练需明确许可属于厂商声明，不是零留存保证。账户删除存在 14 天锁定 / 恢复期及法定保留例外，本仓库未验证后台清除。

<a id="octop"></a>
## 常驻助理补充：Octop

**文档核验：2026-11-02。** [官方仓库](https://github.com/TencentCloud/Octop)；固定 [v1.0.3b2 提交](https://github.com/TencentCloud/Octop/commit/a40f54a8099b1faebc89c680ec1e1ece8b97a4e6) 的 [README](https://github.com/TencentCloud/Octop/blob/a40f54a8099b1faebc89c680ec1e1ece8b97a4e6/README.md) 与 [MIT LICENSE](https://github.com/TencentCloud/Octop/blob/a40f54a8099b1faebc89c680ec1e1ece8b97a4e6/LICENSE)；[发布页](https://github.com/TencentCloud/Octop/releases/tag/v1.0.3b2)于 2026-11-02 提供桌面及 Python 包。

读取多用户/Agent、记忆、cron、渠道、浏览器功能、安装与路线图；AgentTeams 标 Beta、手机端内测，托管 Agent 与自演化等仍是计划。模型、OAuth/MCP、消息服务另受权限和地域条件约束；未安装、验签或审计多用户隔离，不采纳“自托管即隐私无妥协”的宣传结论。