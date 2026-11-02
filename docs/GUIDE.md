# 选型与使用指南

[← 返回项目清单](../README.md)

简体中文 | [English](GUIDE.en.md)

> 精选个人 AI Agent 的项目、产品与论文：从长期助理、手机操作，到评测基准与系统方法。
>
> A curated guide to personal AI agents: open-source projects, publicly available products, evaluation benchmarks, and agent research.

**少一点名单堆砌，多一点选型依据。** 本仓库同时收录源码项目、公开可用产品（含商业产品），以及相关论文。按不同类型记录功能、可用性、研究贡献和证据边界，不把它们混成一张排行榜。

源码项目首批文档核验：**2026-10-31**；产品与论文的日期和核验范围见各自条目。核验不等于安装实测、论文复现或安全审计。源码项目链接官方仓库，产品链接官方入口，论文链接原文；依据与口径见 [来源记录](SOURCES.md)。

<a id="start-here"></a>
## 目录 · Contents

按任务选择入口，不按排名选产品。[源码项目目录](#source-projects)区分应用、运行时、框架、组件与预览项目；请按设备和具体版本阅读选型提醒。

**第一次来？** 在[任务—研究—实现导读](LANDSCAPE.md)中选一个任务 → 查看对应实现与证据 → 用[低风险任务协议](TASKS.md)拟定试验。主题关联不证明产品采用某篇论文或通过基准；任务协议仍未执行。

**近期核验 · 2026-10-31：** [原始项目复核](SOURCES.md#original-projects-audit) · [新增项目与证据](SOURCES.md#expansion)。日期指文档核验，不是产品发布日期或实测结果。

| 我想…… | 从这里开始 | 先确认什么 |
| --- | --- | --- |
| 联系长期助理，或使用个人记忆 | [常驻个人助理](#personal-assistants) | 运行环境、聊天渠道、记忆存储与自动执行的操作 |
| 操作手机 App | [手机 Agent](#mobile-agents) | 成品应用还是框架；系统、CPU、设备权限与模型端点 |
| 处理文档、会议与文件交付 | [桌面知识与办公助理](#desktop-assistants) | 安装包、连接器、支持的产物与数据流 |
| 研究、处理文件或自动操作电脑/浏览器 | [电脑与浏览器执行](#computer-and-browser) | GUI 操控还是工具执行；宿主访问、挂载与本地/托管部署 |
| 自己开发助理 | [开发框架与记忆层](#building-blocks) | 界面、授权、调度、存储与评估仍需集成 |
| 探索早期项目并参与开发 | [开发者预览与 Alpha](#previews) | 源码/构建路径不等于成品应用；需承担配置和调试 |
| 不自行部署，直接使用服务 | [公开可用产品](#products) | 开放状态、地区/账号限制与付费条件 |
| 研究评测或 Agent 设计 | [论文](#papers) | Eval / Benchmark 与方法 / 系统分开；核验范围与作者报告结果 |
| 设计低风险试验 | [任务协议](TASKS.md) | 协议尚未执行，不是测试结果或产品评分 |

[收录范围](#scope) · [如何比较](#comparison) · [安全使用清单](#safety) · [相关清单](#related-lists) · [贡献与许可](#contributing)

<a id="scope"></a>
## 收录范围 · Scope

本仓库关注的是：**围绕一个人的目标，通过工具执行任务的 AI 系统**。长期记忆、持续运行和主动工作是重要维度，但不是所有项目都具备，也不是“个人 Agent”的强制三件套。

- **应用 / Application**：有可用入口，安装配置后可交付任务。
- **运行时 / Runtime**：提供工具执行、会话或长期运行能力，通常仍需配置和运维。
- **框架 / Framework**：需要开发者编写或集成工作流。
- **组件 / Component**：只解决记忆等一部分问题，不是完整助理。

**研究定位 / Research**：以论文、模型、实验代码为主，不能当作成熟消费产品；这是研发定位，不是与上述形态互斥的一层。

上述接入形态可重叠，不是商业模式。商业产品也可能基于开源项目，研究系统也可能提供代码；同名品牌的源码库与托管服务应分别标清。**能在手机聊天，不等于能操作手机；能操控浏览器，不等于能自主处理所有生活事务。**

本仓库的三条主线：

1. **源码项目**：提供官方代码或可自托管实现，按使用方式分类。公开源码不自动等于开源许可，具体许可仍须查阅上游文件。
2. **公开可用产品**：包括免费、付费和商业托管服务，不要求公开源码。以可公开注册、下载或订阅的使用入口为主；候补、邀请制或仅宣布的产品如保留，应单独标注，不冒充公开可用。
3. **研究论文**：分别收录 **Eval / Benchmark** 与 **Agent 方法 / 系统**。不强制论文有开源代码；有论文不代表有可用产品，有代码不代表已复现结果。

不追求覆盖所有 AI 产品，不把纯聊天界面、纯编码工具、通用企业工作流平台塞进主清单；相关基础研究需解释与个人 Agent 的联系。没有最低 Star 门槛；不收付费排名、推广返佣链接，也不把路线图写成已交付功能。

<a id="products"></a>
## 公开可用产品 · Publicly available products

→ [查看产品目录（含商业产品）](PRODUCTS.md)

产品目录关注用户可以实际尝试的入口，而不是只列公司名称。每项应分开说明：**主要用途、访问方式、当前开放状态、地区/平台/账号限制、收费方式，以及官方依据与核验日期**。这里的“可用”不等于所有人、所有地区都可立即使用，也不等于免费或已由本仓库实测。

<a id="source-projects"></a>
## 源码项目 · Open-source & source-available projects

以下按主要用途保留项目入口；同一项目的托管产品若另有收录，不视为另一套已验证能力。没有单独列出的付费条件与可用性，仍需按具体版本和服务核对。

当前收录 **34 个源码项目：31 个主分类条目 + 3 个单列预览条目**，共六类主要用途及一个预览区。初始 14 项及首轮新增 15 项全部保留；前轮补充 [AstrBot 与 Eigent](SOURCES.md#personal-work-additions)；本轮补充 [Home Assistant Assist 与 Omi](SOURCES.md#home-voice-additions)，另补充 [Octop](SOURCES.md#octop)，累计新增 20 项。各轮固定 commit、许可和发布记录及仅文档核验的范围见来源记录。条目中的发布号不保证该版本具备主分支全部功能，`prerelease=false` 也不代表成熟或已经实测。新增条目的根许可仅指已读仓库代码，不自动覆盖模型、依赖、插件、商标或托管服务；详见 [扩充来源](SOURCES.md#expansion)。

**形态怎么读：** 加粗部分标明应用、运行时、框架或组件等接入形态；同一项目可有多条路径，CLI 不自动等于完整助理。用途、设备与 Alpha / Beta 等阶段另看，不据此推断成熟度。

形态依据[已有官方文档记录](SOURCES.md)及条目内补充来源整理（2026-11-02），不是安装实测；未列出的形态不等于不存在，各来源仍保留原核验日期。

<a id="personal-assistants"></a>
### 常驻个人助理 · Persistent personal assistants

“常驻”指支持持续运行的使用方式，不保证默认安装即可全天在线。电脑休眠、服务中断、渠道限制和模型额度都可能影响任务。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | **应用 / 常驻运行时**。通过个人或群聊及 ChatUI 使用知识库、技能、MCP、网页与代码工具。根许可 AGPL-3.0。 | 观察到 v4.29.4；需配置模型和渠道，提供 Python 3.12/uv 与 Docker 路径。隔离能力因系统与部署而异；第三方沙箱仍为技术预览，云模型、消息平台与插件仍可能接收数据。 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | **应用 / 运行时**。Nous Research 的助理，包含持久记忆、历史会话检索、可复用技能、定时任务及聊天渠道入口。 | 需要配置模型和运行环境；技能学习是项目提供的机制，不代表任务效果会自动、持续提高。 |
| [IronClaw](https://github.com/nearai/ironclaw) | **常驻助理 / Rust 运行时**。WebUI、REPL、渠道、cron 与 webhook 任务，配合持久记忆、WASM/MCP 扩展。MIT OR Apache-2.0。 | 观察到 ironclaw-v1.4.1；安装后需配置模型与渠道。不能宣称与 OpenClaw 完全对等，WASM 也不覆盖所有宿主、Docker、MCP 和网络路径，更不证明免疫提示注入。 |
| [Khoj](https://github.com/khoj-ai/khoj) | **应用**。围绕个人文档与网页开展问答、研究、自定义 Agent 和定期信息任务；可自托管，也有云服务。 | 更适合知识与研究工作。接入文档前确认索引、模型与云端的数据流，不应理解为通用手机操控工具。 |
| [Letta Code](https://github.com/letta-ai/letta-code) | **应用 / 运行时**。以持续身份和可编辑记忆为核心，提供 CLI、聊天渠道、工具、技能与调度。 | 当前源码在 `letta-code`，不是旧 V1 服务端；支持本地与 Cloud 后端，先确认实际选择，不能假定记忆默认只在本机。 |
| [Moltis](https://github.com/moltis-org/moltis) | **常驻个人助理服务器**。Web、语音、聊天和 cron 驱动浏览器、命令、文件/记忆更新与通知。MIT。 | 观察到 20261023.01，可用发行二进制/Homebrew/Docker 路径。单二进制不代表无外部依赖；示例挂载 `docker.sock`，远程执行和主机挂载扩大权限。本轮未验签。 |
| [nanobot](https://github.com/HKUDS/nanobot) | **应用 / 框架**。Python 个人 Agent，提供 WebUI、终端和聊天入口，以及文件工具、记忆、MCP 与定时任务。 | 自备模型服务或本地模型；README 的源码功能与已发布稳定版可能不同，按所用版本核验。 |
| [NanoClaw](https://github.com/nanocoai/nanoclaw) | **应用 / 运行时**。强调可定制代码与容器执行的个人聊天助理，支持记忆和定时任务，渠道按需添加。 | 新地址是 `nanocoai/nanoclaw`；容器不是安全保证，需检查挂载、凭据、渠道共享与网络访问范围。 |
| [Octop](https://github.com/TencentCloud/Octop) | **自托管应用 / 运行时**。多用户、多 Agent、持久记忆、定时任务、消息渠道与浏览器操作；MIT。 | 核验 v1.0.3b2，提供 Windows / macOS / Linux 安装包；AgentTeams 为 Beta、手机端内测。需配置模型与渠道，自托管不等于纯离线或隔离已审计。[来源](SOURCES.md#octop) |
| [OpenClaw](https://github.com/openclaw/openclaw) | **应用 / 运行时**。通过本地 Gateway 管理会话、工具与消息渠道，支持持久状态、技能和可替换的模型服务。 | 官方提醒：未配置沙箱时，主会话工具可在宿主机执行。连接外部消息源或开放远程入口前先读安全文档。 |
| [PicoClaw](https://github.com/sipeed/picoclaw) | **轻量常驻助理**。WebUI、CLI 与聊天任务可调用工具、记忆和提醒，提供二进制、Docker 与 Android 运行路径。MIT。 | **Pre-1.0**：v0.3.1 与 nightly 分开，官方提示 v1.0 前勿部署生产。Android 可运行不等于能控制任意 App；低运行时资源占用不含完整本地大模型成本。 |
| [QwenPaw（原 CoPaw）](https://github.com/agentscope-ai/QwenPaw) | **应用 / 常驻运行时**。Console、TUI 与聊天渠道中的任务可生成摘要、办公文件、浏览器工作和通知。Apache-2.0。 | 非预发布 v2.2.2.post1；v2.3.0-beta.1 与桌面版均须保留 Beta 区分。Python/Docker 部署需配置模型和渠道；初始化 `--defaults` 会接受其声明的匿名遥测。CoPaw 不另计。 |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | **Rust 常驻运行时**。消息、CLI、webhook 与外设事件触发 Shell、浏览器、HTTP、硬件工具和可恢复 SOP。MIT OR Apache-2.0。 | 观察到 v0.8.7；后台服务、模型、渠道和硬件需分别设置。默认 supervised 之外还有放松限制的 YOLO 路径；检查实际策略、工作区与 OS 沙箱，不能因 Rust 断言安全。 |

<a id="home-voice-wearables"></a>
### 家居、语音与可穿戴

**文档核验：2026-11-01（UTC）；未安装、购买、连接账户、录音或实测。** 两项补充不同任务与交互形态，不代表完整市场覆盖。[依据](SOURCES.md#home-voice-additions)

| 项目 | 形态与个人任务 | 依赖、数据与选型提醒 |
| --- | --- | --- |
| [Home Assistant Assist](https://github.com/home-assistant/core) | **平台组件 / 集成应用功能**。家居语音 / 文字入口。内置意图匹配与可选 LLM Agent 分开；后者通过工具访问暴露的家居实体。Core 根许可 Apache-2.0。 | 需运行 Home Assistant、接入设备并配置语音链路 / 会话集成。Ollama 控制需独立服务器和支持工具的模型，仍属实验性；云模型另需 API / 计费。逐段检查唤醒、转写、推理和语音合成的数据流；本地 Hub 不等于全离线。先仅暴露测试灯，不授权门锁等高风险设备，确认家庭成员的使用和录音边界。 |
| [Omi](https://github.com/BasedHardware/omi) | **语音 / 环境记忆应用与平台**：手机、桌面或可穿戴采集形成记忆、任务；Apps 可处理记忆并连接外部工具。根许可 MIT。录音摘要不等于自主执行。 | 可不购买硬件使用 App；源码构建与托管产品分开。macOS 快速启动连接云后端，不是离线部署；完整后端、转写 / 模型及集成各有配置依赖。检查录音、转写、人物声纹、屏幕上下文和第三方 Apps 的访问范围。录音前告知参与者并取得适用同意，勿采集旁人私密对话；暂停采集、删除和导出须另核对。 |

**源码与服务不重复计数：** 每个官方仓库只计一项。Omi 的[托管 App / 硬件](https://www.omi.me/pages/product)有独立条款、额度和费用；未核实完整地区、套餐或配送，不新增为产品目录中的已核验商业条目。Home Assistant Cloud 也不是 Assist 的必需订阅。

**建议首测（未执行）：** Assist 仅控制测试灯并核对实际状态；Omi 只录制自己的一段虚构待办，检查任务、停止采集和删除，不连接私人账户或自动外发。

<a id="mobile-agents"></a>
### 手机 Agent · Mobile agents

这一类的关键是**读取和操作手机 App 界面**，而不只是给桌面 Agent 加一个手机聊天入口。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Mika](https://github.com/wangzan101/Mika) | **Android 应用**。通过后台屏操作 App，集成浏览器、脚本沙箱与定时任务；提供中文界面。 | **早期公开测试版**。安装需 Android 11+，App 操控的最低系统版本请按所装版本文档核对，官方推荐 Android 14+；沙箱仅支持 arm64。手机端执行不等于离线推理，内容会发送到你配置的模型服务商。 |
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) | **研究代码集合 / 执行框架**。包含多代手机及跨平台 GUI Agent、模型和实验代码，适合研究界面理解与多步操作。 | 先选具体子项目与版本，再读其环境和模型要求；论文演示不是对任意手机、App 或任务的兼容承诺。 |
| [Mobilerun（原 DroidRun）](https://github.com/droidrun/mobilerun) | **框架**。通过 CLI / Python 组织手机自动化，结合界面树与截图；官方提供 Android 与 iOS 的不同接入路径。 | 不等同于一个独立手机助理 APK。设备、Portal、调试或 USB 设置按平台分别配置；本地框架与 Cloud 产品分开看。 |
| [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | **研究 / 手机执行框架**。由任务与截图生成点击、输入和滑动等操作，提供人工接管与确认回调。仓库代码 Apache-2.0。 | Python 3.10+ 与独立模型端点；Android/HarmonyOS/iOS 的接入路径不同。观察到 GitHub releases 为空，不是现成 APK；截图传给模型，权重许可另核对。 |
| [Operit](https://github.com/AAswordman/Operit) | **Android 应用**。界面、浏览器、文件与终端任务，以及定时和 Tasker/Intent 工作流。主代码 LGPL-3.0-only。 | 官方 APK v1.12.2；Android 8.0+、仅 ARM64。设备控制权限按功能配置，并非都需 Root；云模型仍可接收数据。不要与预览中的 Operit2 混同。 |

<a id="desktop-assistants"></a>
### 桌面知识与办公助理 · Desktop knowledge & work assistants

以文档、会议、个人知识与可交付文件为入口；与纯聊天界面区分。桌面包、后端运行时和云服务的能力与数据流需分别确认。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | **桌面 / 自托管知识与 Agent 应用**。除文档问答外，还提供网页研究、记忆、调度，以及启用工具后的文本与 Office/PDF 产物。MIT。 | 观察到 v1.19.0。桌面与 Docker 功能不同，多用户权限不通用于桌面；自选模型、嵌入和向量库。关闭遥测不阻断这些外部服务和工具的数据传输。 |
| [Eigent](https://github.com/eigent-ai/eigent) | **桌面应用**。用单 Agent 或多 Agent 协作完成研究、写作、文件整理、浏览器及终端任务，并提供定时工作流。Apache-2.0。 | 观察到 v1.0.7；独立本地部署与需账号的云连接快速启动不同。本地指南要求 Docker Desktop、Python 3.12、Node 18–22；外部模型/MCP 仍会外发请求，入站 webhook 需公网 HTTPS。未安装或验证隔离。 |
| [LobsterAI（有道龙虾）](https://github.com/netease-youdao/LobsterAI) | **桌面应用**。围绕本地文件交付文档、表格、演示文稿、网页和图表，提供浏览器、调度与聊天入口。MIT。 | 2026.10.30 版本于 2026-10-31 UTC 发布，提供 Mac/Windows 安装资产。当前使用 OpenClaw 运行时，不是独立引擎的对照实测；模型、分享与插件仍有外部数据流。 |
| [OpenWorker](https://github.com/andrewyng/openworker) | **桌面应用**。通过授权文件与连接器准备会议、报告、表格和待审操作，并提供定时任务。MIT。 | **Open beta**，观察到 v0.3.1。主要下载支持 macOS Apple Silicon 与 Windows x64；Windows 包尚未代码签名。审批、日志和沙箱均需按配置检查，不视为安全认证。 |
| [Rowboat](https://github.com/rowboatlabs/rowboat) | **个人知识与执行型桌面助理**。将邮件、会议和对话连接到 Markdown 知识图谱、草稿、摘要与后台工作。Apache-2.0。 | 非预发布 v1.0.3，v1.0.5 为**预发布**；当前文档可能领先安装包。Mac/Windows/Linux 路径需配置模型和连接器；会议记录需适当同意，本地 Markdown 不保证外发上下文仍留本地。 |

<a id="computer-and-browser"></a>
### 电脑与浏览器执行 · Computer & browser use

这类工具解决“如何动手”，未必自带长期个人身份、后台待办或生活服务整合。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Agent Zero](https://github.com/agent0ai/agent-zero) | **应用 / 框架**。提供 Docker 化 Linux 桌面、浏览器、项目、记忆、技能与子 Agent，用于研究、文件和多步工作。 | 宿主机桥接会扩大权限边界。只挂载必要目录；不要把容器内的操作与主机访问混为一谈。 |
| [Browser Use](https://github.com/browser-use/browser-use) | **框架库 / CLI 工具**。让模型通过浏览器执行网页任务，提供本地库和 CLI 路径，另有托管浏览器与 Agent API。 | 开源库与付费托管服务不是同一个部署方式；登录态、网页内容、模型调用与浏览器托管需分别评估。 |
| [goose](https://github.com/aaif-goose/goose) | **桌面 / CLI 工具运行时**。官方当前定位含研究、写作、文件编辑与数据任务，通过扩展和 MCP 执行。Apache-2.0。 | 观察到 v1.57.0；规范仓库已迁至 `aaif-goose/goose`。需配置模型、扩展与允许/询问/拒绝策略，不是预配全部生活服务的管家；Shell 和第三方工具扩大权限。 |
| [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) | **桌面应用 / CLI 与 SDK**。同仓库包含 GUI 桌面应用 UI-TARS Desktop、集成视觉和工具的 Agent TARS CLI / Web UI，以及[实验性的 `@ui-tars/sdk`](https://github.com/bytedance/UI-TARS-desktop/blob/main/docs/sdk.md)。 | 两个产品的安装与模型要求不同；不要把演示中的本地、远程电脑及浏览器能力当成同一种配置。 |

<a id="building-blocks"></a>
### 开发框架与记忆层 · Building blocks

**不是开箱即用的私人助理。** 适合已经决定自己开发的人。

| 项目 | 解决的问题 | 仍需自己负责 |
| --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | **编排框架**。有状态 Agent 的流程编排、持久执行、人工介入与记忆基础设施。 | 工具权限、用户界面、业务逻辑、部署与真实任务评估。 |
| [Mem0](https://github.com/mem0ai/mem0) | **记忆组件**。给应用提供用户、会话与 Agent 记忆层；有库、自托管服务与托管平台等路径。 | 收集哪些记忆、访问控制、删除与纠错、模型/嵌入配置；记忆层本身不会执行任务。 |

<a id="previews"></a>
### 开发者预览与 Alpha · Developer previews & alpha projects

以下三项保留研究与定制价值，但**不与成熟成品等同**。有源码、截图或部分发布资产，不代表完整跨平台产品已交付。主分类中另有 beta/pre-1.0 项目，其警告同样有效。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Leon](https://github.com/leon-ai/leon) | **助理应用 / 运行时**。**2.0 Developer Preview**。分层记忆、原生技能、电脑/浏览器工具与主动轮询的个人助理开发项目。MIT。 | 默认 `develop` 分支需 Node 24+、pnpm 与源码启动；旧 `master` 是不同架构。新文档未完成，近期发布是桥接/服务组件预发布，不是完整 2.0 成品。 |
| [OpenMuse](https://github.com/CopilotKit/openmuse) | **应用模板**（**Alpha**）。展示任务状态、人工接管、文档流程、草稿与提醒等移动/网页体验。MIT。 | 观察到 GitHub releases 为空；需 Node/pnpm、CopilotKit Intelligence project key 和各工具配置，移动端需原生构建。非完全本地；样例/脚本化验证不等于真实账号验收，自动支付/预约等仍是路线图。 |
| [Operit2](https://github.com/AAswordman/Operit2) | **跨设备运行时 / CLI**。**跨设备预览**。不同 Host 的文件、终端和浏览器工具，以及配对节点在已持久化工具结果边界续接任务。根许可 AGPL-3.0。 | v2.0.0-preview.3 只有 Linux/Windows x86_64/aarch64 CLI 资产；其他端为源码/构建路径。协议和格式可能破坏性变化；不迁移运行中的模型请求、进程或浏览器会话，完整 Server 产品尚未就绪。 |

<a id="papers"></a>
## 论文 · Papers

→ [查看论文目录](PAPERS.md)

论文分为两组，避免把测量工具与被测系统混在一起：

- **Eval / Benchmark（评测与基准）**：研究如何衡量任务完成、工具使用、记忆、长期交互、移动端/网页/电脑操作等能力。记录环境、任务与指标，说明覆盖不到什么。
- **Agent 方法 / 系统（Methods & Systems）**：研究规划、执行、反思、记忆、主动性与持续运行等机制。记录核心贡献、实验范围和实现/代码状态。

阅读范围应明确标注为摘要、选读章节或全文；论文中的成绩是**作者报告**，除非另有可复现的独立记录，不写成“我们评测发现”。不同任务集、模型、预算和版本的分数不能直接拼接成产品排名。

<a id="comparison"></a>
## 如何比较 · Evaluation guide

→ [低风险任务协议](TASKS.md)：可用于规划和记录后续试验，**尚未执行，不包含实测成绩**。协议不是统一基准，也不能单凭模板给产品打分。

不要只看宣传中的 “autonomous”“local-first” 或 Star。先用同一组低风险任务测试，再逐步开放权限。

| 维度 | 建议记录的问题 |
| --- | --- |
| 任务闭环 | 只返回建议，还是实际执行并核验结果？失败时能否明确停下？ |
| 运行方式 | 在手机、桌面、自己的服务器还是厂商云端？休眠或断网后怎么办？ |
| 主动性 | 是手动对话、定时触发、事件触发，还是持续目标？是否容易暂停和取消？ |
| 记忆 | 会话记录与长期记忆是否分开？能否查看、改正、导出与删除？ |
| 权限 | 文件、Shell、浏览器、邮箱、联系人各获什么权限？敏感操作能否逐次确认？ |
| 数据去向 | 哪些内容交给模型、搜索、遥测、消息平台和托管浏览器？日志存多久？ |
| 可维护性 | 有无安装说明、版本发布、迁移指南、问题反馈与安全报告路径？ |
| 成本 | 模型、搜索、存储、浏览器、云机与短信等是否另计？是否有预算上限？ |

建议从三个任务开始：**读取一份脱敏文档并引用依据 → 整理测试目录并展示差异 → 创建一项可取消的低风险提醒**。手机或浏览器工具则换成查看设置、读取公开网页等不产生外部影响的任务。记录版本、模型、人工干预次数、耗时、费用、最终结果与失败原因，不把单次成功概括为可靠性。

<a id="safety"></a>
## 安全使用清单 · Safety checklist

- [ ] 先用测试账号、脱敏数据和独立工作目录；重要数据先备份。
- [ ] 只授予任务必需的权限，不把整个主目录、全部浏览器登录态或生产密钥一次性交出去。
- [ ] 付款、转账、发消息、删文件、发布内容与修改账号设置，先保留人工确认。
- [ ] 网页、邮件、文档和聊天消息都可能包含恶意指令；其中的文字不是用户授权。
- [ ] 第三方 Skills、插件、MCP 服务与安装脚本要单独检查；“接入标准协议”不等于可信。
- [ ] 确认如何停机、撤销令牌、断开渠道、删除记忆和恢复数据。
- [ ] 需要时手动处理登录与验证码，不让自动化绕过网站规则或安全验证。
- [ ] 不把开源、自托管、容器化或端侧界面当作隐私、安全、完全离线的同义词。

本清单是选型与学习资料，不为收录项目的安全性、可用性或宣传效果背书；实际使用以对应版本、官方文档、服务条款与适用规则为准。

<a id="related-lists"></a>
## 相关清单 · Related lists

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents) — 常驻个人 Agent 及其记忆、运行时与消息连接生态。
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents) — 自托管和商业个人 Agent，并附选型维度。
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices) — 产品、源码、用例与研究资料，含中英文内容。

这些清单用于发现候选项目；本仓库条目回到项目官方来源单独核验，不直接继承其他清单的功能、许可或质量结论。

<a id="contributing"></a>
## 贡献与许可 · Contributing & licensing

欢迎补充项目、产品与论文，纠正过时信息，也欢迎可复现的使用或研究复现记录。请先读 [中文贡献指南](../CONTRIBUTING.md) / [English contribution guide](../CONTRIBUTING.en.md)，同步更新对应目录的来源与日期，并遵循 [来源记录](SOURCES.md) 的核验口径。

**原创文档文字与原创编选内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en)；本仓库已指定的原创脚本及测试代码采用 [MIT](../scripts/LICENSE)。** 完整范围与当前适用文件见 [许可范围声明](LICENSE.md#zh)。这是按材料类型分开的许可，不是全仓库双重许可。第三方材料、所链接的项目及其商标保留各自条款；独立机器可读夹具与结果模板不因上述声明获得授权。收录不构成重新授权或背书。
