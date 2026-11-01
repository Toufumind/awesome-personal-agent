# Awesome Personal Agent

精选个人 AI Agent：源码项目、可用产品与研究论文。

**简体中文** · [English](README.en.md)

**[31 个项目](#source-projects) · [产品目录](docs/PRODUCTS.md) · [论文目录](docs/PAPERS.md)**

<a id="目录--contents"></a>
<a id="start-here"></a>
## 目录

- [常驻个人助理](#personal-assistants)
- [手机 Agent](#mobile-agents)
- [桌面知识与办公](#desktop-assistants)
- [电脑与浏览器执行](#computer-and-browser)
- [开发框架与记忆层](#building-blocks)
- [开发者预览](#previews)

<a id="源码项目--open-source--source-available-projects"></a>
<a id="source-projects"></a>
## 源码项目

按用途分类，含开源与源码可见项目，不作排名。

<a id="常驻个人助理--persistent-personal-assistants"></a>
<a id="personal-assistants"></a>
### 常驻个人助理

- [AstrBot](https://github.com/AstrBotDevs/AstrBot) — 聊天入口、知识库与工具集成。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — 持久记忆、技能与定时任务。
- [IronClaw](https://github.com/nearai/ironclaw) — Rust 助理运行时，支持 WASM / MCP 扩展。
- [Khoj](https://github.com/khoj-ai/khoj) — 围绕个人文档与网页的研究助理。
- [Letta Code](https://github.com/letta-ai/letta-code) — 持续身份、可编辑记忆与工具执行。
- [Moltis](https://github.com/moltis-org/moltis) — 支持语音、聊天与定时任务的助理服务器。
- [nanobot](https://github.com/HKUDS/nanobot) — 轻量 Python Agent，提供记忆、工具与多渠道入口。
- [NanoClaw](https://github.com/nanocoai/nanoclaw) — 以可定制代码和容器执行为核心的聊天助理。
- [OpenClaw](https://github.com/openclaw/openclaw) — 连接消息渠道、会话与工具的本地 Gateway。
- [PicoClaw](https://github.com/sipeed/picoclaw) — 轻量常驻助理，支持工具与提醒。**Pre-1.0，勿用于生产。**
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) — 原 CoPaw；聊天、办公文件与浏览器任务。**桌面版 Beta。**
- [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) — 支持消息、webhook 与硬件事件的 Rust 运行时。

[ 部署与选型提醒 → ](docs/GUIDE.md#personal-assistants)

<a id="手机-agent--mobile-agents"></a>
<a id="mobile-agents"></a>
### 手机 Agent

- [Mika](https://github.com/wangzan101/Mika) — Android App 操控、浏览器与定时任务。**早期公测。**
- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) — 手机与跨平台 GUI Agent 的研究框架。
- [Mobilerun](https://github.com/droidrun/mobilerun) — 原 DroidRun；CLI / Python 手机自动化框架，非独立 APK。
- [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) — 基于截图的手机执行研究框架，需独立模型端点。
- [Operit](https://github.com/AAswordman/Operit) — Android 助理：界面、文件、终端与工作流。**仅 ARM64。**

[ 部署与选型提醒 → ](docs/GUIDE.md#mobile-agents)

<a id="桌面知识与办公助理--desktop-knowledge--work-assistants"></a>
<a id="desktop-assistants"></a>
### 桌面知识与办公

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) — 文档知识库、网页研究与工具驱动的文件交付。
- [Eigent](https://github.com/eigent-ai/eigent) — 单 / 多 Agent 协作研究、写作与文件整理。
- [LobsterAI](https://github.com/netease-youdao/LobsterAI) — 有道龙虾；基于 OpenClaw 运行时的桌面办公助理。
- [OpenWorker](https://github.com/andrewyng/openworker) — 会议准备、报告与待审操作。**Open beta；Windows 未签名。**
- [Rowboat](https://github.com/rowboatlabs/rowboat) — 将邮件、会议与对话连接到个人知识图谱和后台工作。

[ 部署与选型提醒 → ](docs/GUIDE.md#desktop-assistants)

<a id="电脑与浏览器执行--computer--browser-use"></a>
<a id="computer-and-browser"></a>
### 电脑与浏览器执行

- [Agent Zero](https://github.com/agent0ai/agent-zero) — Docker 化桌面、浏览器、记忆与多步任务。
- [Browser Use](https://github.com/browser-use/browser-use) — 模型驱动的浏览器自动化库与 CLI。
- [goose](https://github.com/aaif-goose/goose) — 通过扩展与 MCP 完成研究、写作和文件任务的运行时。
- [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) — GUI 桌面应用与视觉 / 工具 Agent 栈。

[ 部署与选型提醒 → ](docs/GUIDE.md#computer-and-browser)

<a id="开发框架与记忆层--building-blocks"></a>
<a id="building-blocks"></a>
### 开发框架与记忆层

- [LangGraph](https://github.com/langchain-ai/langgraph) — 有状态 Agent 编排、持久执行与人工介入。
- [Mem0](https://github.com/mem0ai/mem0) — 用户、会话与 Agent 记忆层；不是完整助理。

[ 部署与选型提醒 → ](docs/GUIDE.md#building-blocks)

<a id="开发者预览与-alpha--developer-previews--alpha-projects"></a>
<a id="previews"></a>
### 开发者预览

- [Leon](https://github.com/leon-ai/leon) — **2.0 Developer Preview**：记忆、技能与主动轮询；需源码部署。
- [OpenMuse](https://github.com/CopilotKit/openmuse) — **Alpha 模板**：移动 / 网页任务与人工接管；支付、预约仍属路线图。
- [Operit2](https://github.com/AAswordman/Operit2) — **跨设备预览**：在持久化工具结果处续接任务，不迁移活动会话。

[ 部署与选型提醒 → ](docs/GUIDE.md#previews)

<a id="公开可用产品--publicly-available-products"></a>
<a id="products"></a>
## 产品

- [ 公开可用产品（含商业服务） → ](docs/PRODUCTS.md) — 使用入口、收费与地区 / 账号限制。

<a id="论文--papers"></a>
<a id="papers"></a>
## 论文

- [ 论文目录 → ](docs/PAPERS.md) — Eval / Benchmark · Agent 方法 / 系统。

<a id="收录范围--scope"></a>
<a id="scope"></a>
<a id="如何比较--evaluation-guide"></a>
<a id="comparison"></a>
<a id="安全使用清单--safety-checklist"></a>
<a id="safety"></a>
## 开始之前

关注围绕个人目标调用工具、执行任务的 AI 系统；框架与预览项目不等于成品助理。

先用测试数据和最小权限，敏感操作保留人工确认。本地部署、容器化不等于安全或离线推理。

[收录范围](docs/GUIDE.md#scope) · [如何比较](docs/GUIDE.md#comparison) · [安全清单](docs/GUIDE.md#safety) · [任务导读](docs/LANDSCAPE.md) · [试验协议](docs/TASKS.md)

源码项目文档核验：**2026-10-31**。未安装实测、复现或审计；试验协议尚未执行。[来源与日期](docs/SOURCES.md)（产品与论文分别记录）。

<a id="相关清单--related-lists"></a>
<a id="related-lists"></a>
## 相关清单

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents)
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents)
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices)

<a id="贡献与许可--contributing--licensing"></a>
<a id="contributing"></a>
## 贡献与许可

[贡献指南](CONTRIBUTING.md) · [来源记录](docs/SOURCES.md)

原创文字与编选：**CC BY 4.0**；已指定的原创脚本及测试代码：**MIT**。第三方材料条款独立，详见[许可范围](docs/LICENSE.md#zh)。
