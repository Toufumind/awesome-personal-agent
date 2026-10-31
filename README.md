# Awesome Personal Agent

简体中文 | [English](README.en.md)

> 精选个人 AI Agent 的项目、产品与论文：从长期助理、手机操作，到评测基准与系统方法。
>
> A curated guide to personal AI agents: open-source projects, publicly available products, evaluation benchmarks, and agent research.

**少一点名单堆砌，多一点选型依据。** 本仓库同时收录源码项目、公开可用产品（含商业产品），以及相关论文。按不同类型记录功能、可用性、研究贡献和证据边界，不把它们混成一张排行榜。

源码项目首批文档核验：**2026-10-31**；产品与论文的日期和核验范围见各自条目。核验不等于安装实测、论文复现或安全审计。源码项目链接官方仓库，产品链接官方入口，论文链接原文；依据与口径见 [来源记录](docs/SOURCES.md)。

| 你想找什么 | 入口 | 如何读 |
| --- | --- | --- |
| 安装、自托管或二次开发 | [源码项目](#source-projects) | 分清应用、运行时、框架与组件；查看部署前提 |
| 直接使用一个个人 Agent 服务 | [公开可用产品](docs/PRODUCTS.md) | 包含商业产品；分别确认开放范围、地区/账号要求与付费条件 |
| 了解怎样衡量 Agent 能力 | [论文：Eval / Benchmark](docs/PAPERS.md) | 看任务、环境、指标与局限，不把榜单分数当作现实可靠性 |
| 了解 Agent 如何构建 | [论文：方法 / 系统](docs/PAPERS.md) | 看规划、记忆、工具使用与长期运行等机制，以及论文实际验证范围 |

## 目录 · Contents

- [从需求开始](#start-here)
- [收录范围](#scope)
- [公开可用产品（含商业产品）](#products)
- [源码项目](#source-projects)
  - [常驻个人助理](#personal-assistants)
  - [手机 Agent](#mobile-agents)
  - [电脑与浏览器执行](#computer-and-browser)
  - [开发框架与记忆层](#building-blocks)
- [论文：评测基准与方法系统](#papers)
- [如何比较](#comparison)
- [安全使用清单](#safety)
- [相关清单](#related-lists)
- [贡献与许可](#contributing)

<a id="start-here"></a>
## 从需求开始 · Start here

这里是阅读入口，不是“最好用”排名；最终选择取决于设备、模型、权限和维护投入。

| 你的需求 | 先看 | 先确认什么 |
| --- | --- | --- |
| 给 Android 手机一句话，让它替我操作 App | [Mika](https://github.com/wangzan101/Mika) | Android 版本、调试权限、模型服务商与测试版限制 |
| 从聊天软件联系一个长期助理 | [OpenClaw](https://github.com/openclaw/openclaw)、[Hermes Agent](https://github.com/NousResearch/hermes-agent)、[nanobot](https://github.com/HKUDS/nanobot) | 常驻运行位置、账号接入方式、哪些操作会自动执行 |
| 重点是持续记忆与个人上下文 | [Letta Code](https://github.com/letta-ai/letta-code)、[Khoj](https://github.com/khoj-ai/khoj) | 记忆/文档存在哪里、能否删除、哪些内容会发送给模型 |
| 想用较小代码库定制聊天助理 | [NanoClaw](https://github.com/nanocoai/nanoclaw) | 容器挂载、渠道安装、定制代码的维护成本 |
| 让 Agent 在隔离的电脑环境中工作 | [Agent Zero](https://github.com/agent0ai/agent-zero) | Docker、文件挂载范围与宿主机桥接权限 |
| 写代码自动操作网页或手机 | [Browser Use](https://github.com/browser-use/browser-use)、[Mobilerun](https://github.com/droidrun/mobilerun) | 本地与托管方案差异、设备连接和运行环境 |
| 自己开发助理，而不是安装成品 | [LangGraph](https://github.com/langchain-ai/langgraph)、[Mem0](https://github.com/mem0ai/mem0) | 还需要自己实现界面、授权、调度、存储与评估 |
| 不想自行部署，寻找可直接使用的服务 | [产品目录](docs/PRODUCTS.md) | 是否已开放使用，是否需要订阅、特定地区或受支持账号 |
| 研究 Agent 的能力评估或实现方法 | [论文目录](docs/PAPERS.md) | 是 benchmark 还是方法论文；读到哪些部分，结果是否仅为作者报告 |

<a id="scope"></a>
## 收录范围 · Scope

本仓库关注的是：**围绕一个人的目标，通过工具执行任务的 AI 系统**。长期记忆、持续运行和主动工作是重要维度，但不是所有项目都具备，也不是“个人 Agent”的强制三件套。

- **应用 / Application**：有可用入口，安装配置后可交付任务。
- **运行时 / Runtime**：提供工具执行、会话或长期运行能力，通常仍需配置和运维。
- **框架 / Framework**：需要开发者编写或集成工作流。
- **组件 / Component**：只解决记忆等一部分问题，不是完整助理。
- **研究 / Research**：以论文、模型、实验代码为主，不能当作成熟消费产品。

这些是技术形态，不是商业模式。商业产品也可能基于开源项目，研究系统也可能提供代码；同名品牌的源码库与托管服务应分别标清。**能在手机聊天，不等于能操作手机；能操控浏览器，不等于能自主处理所有生活事务。**

本仓库的三条主线：

1. **源码项目**：提供官方代码或可自托管实现，按使用方式分类。公开源码不自动等于开源许可，具体许可仍须查阅上游文件。
2. **公开可用产品**：包括免费、付费和商业托管服务，不要求公开源码。以可公开注册、下载或订阅的使用入口为主；候补、邀请制或仅宣布的产品如保留，应单独标注，不冒充公开可用。
3. **研究论文**：分别收录 **Eval / Benchmark** 与 **Agent 方法 / 系统**。不强制论文有开源代码；有论文不代表有可用产品，有代码不代表已复现结果。

不追求覆盖所有 AI 产品，不把纯聊天界面、纯编码工具、通用企业工作流平台塞进主清单；相关基础研究需解释与个人 Agent 的联系。没有最低 Star 门槛；不收付费排名、推广返佣链接，也不把路线图写成已交付功能。

<a id="products"></a>
## 公开可用产品 · Publicly available products

→ [查看产品目录（含商业产品）](docs/PRODUCTS.md)

产品目录关注用户可以实际尝试的入口，而不是只列公司名称。每项应分开说明：**主要用途、访问方式、当前开放状态、地区/平台/账号限制、收费方式，以及官方依据与核验日期**。这里的“可用”不等于所有人、所有地区都可立即使用，也不等于免费或已由本仓库实测。

<a id="source-projects"></a>
## 源码项目 · Open-source & source-available projects

以下按主要用途保留项目入口；同一项目的托管产品若另有收录，不视为另一套已验证能力。没有单独列出的付费条件与可用性，仍需按具体版本和服务核对。

<a id="personal-assistants"></a>
### 常驻个人助理 · Persistent personal assistants

“常驻”指支持持续运行的使用方式，不保证默认安装即可全天在线。电脑休眠、服务中断、渠道限制和模型额度都可能影响任务。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 应用 / 运行时。Nous Research 的助理，包含持久记忆、历史会话检索、可复用技能、定时任务及聊天渠道入口。 | 需要配置模型和运行环境；技能学习是项目提供的机制，不代表任务效果会自动、持续提高。 |
| [Khoj](https://github.com/khoj-ai/khoj) | 应用。围绕个人文档与网页开展问答、研究、自定义 Agent 和定期信息任务；可自托管，也有云服务。 | 更适合知识与研究工作。接入文档前确认索引、模型与云端的数据流，不应理解为通用手机操控工具。 |
| [Letta Code](https://github.com/letta-ai/letta-code) | 应用 / 运行时。以持续身份和可编辑记忆为核心，提供 CLI、聊天渠道、工具、技能与调度。 | 当前源码在 `letta-code`，不是旧 V1 服务端；支持本地与 Cloud 后端，先确认实际选择，不能假定记忆默认只在本机。 |
| [nanobot](https://github.com/HKUDS/nanobot) | 应用 / 框架。Python 个人 Agent，提供 WebUI、终端和聊天入口，以及文件工具、记忆、MCP 与定时任务。 | 自备模型服务或本地模型；README 的源码功能与已发布稳定版可能不同，按所用版本核验。 |
| [NanoClaw](https://github.com/nanocoai/nanoclaw) | 应用 / 运行时。强调可定制代码与容器执行的个人聊天助理，支持记忆和定时任务，渠道按需添加。 | 新地址是 `nanocoai/nanoclaw`；容器不是安全保证，需检查挂载、凭据、渠道共享与网络访问范围。 |
| [OpenClaw](https://github.com/openclaw/openclaw) | 应用 / 运行时。通过本地 Gateway 管理会话、工具与消息渠道，支持持久状态、技能和可替换的模型服务。 | 官方提醒：未配置沙箱时，主会话工具可在宿主机执行。连接外部消息源或开放远程入口前先读安全文档。 |

<a id="mobile-agents"></a>
### 手机 Agent · Mobile agents

这一类的关键是**读取和操作手机 App 界面**，而不只是给桌面 Agent 加一个手机聊天入口。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Mika](https://github.com/wangzan101/Mika) | Android 应用。通过后台屏操作 App，集成浏览器、脚本沙箱与定时任务；提供中文界面。 | **早期公开测试版**。安装需 Android 11+，App 操控的最低系统版本请按所装版本文档核对，官方推荐 Android 14+；沙箱仅支持 arm64。手机端执行不等于离线推理，内容会发送到你配置的模型服务商。 |
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) | 研究 / 框架。包含多代手机及跨平台 GUI Agent、模型和实验代码，适合研究界面理解与多步操作。 | 先选具体子项目与版本，再读其环境和模型要求；论文演示不是对任意手机、App 或任务的兼容承诺。 |
| [Mobilerun（原 DroidRun）](https://github.com/droidrun/mobilerun) | 框架。通过 CLI / Python 组织手机自动化，结合界面树与截图；官方提供 Android 与 iOS 的不同接入路径。 | 不等同于一个独立手机助理 APK。设备、Portal、调试或 USB 设置按平台分别配置；本地框架与 Cloud 产品分开看。 |

<a id="computer-and-browser"></a>
### 电脑与浏览器执行 · Computer & browser use

这类工具解决“如何动手”，未必自带长期个人身份、后台待办或生活服务整合。

| 项目 | 形态与主要用途 | 选型提醒 |
| --- | --- | --- |
| [Agent Zero](https://github.com/agent0ai/agent-zero) | 应用 / 框架。提供 Docker 化 Linux 桌面、浏览器、项目、记忆、技能与子 Agent，用于研究、文件和多步工作。 | 宿主机桥接会扩大权限边界。只挂载必要目录；不要把容器内的操作与主机访问混为一谈。 |
| [Browser Use](https://github.com/browser-use/browser-use) | 框架 / 工具。让模型通过浏览器执行网页任务，提供本地库和 CLI 路径，另有托管浏览器与 Agent API。 | 开源库与付费托管服务不是同一个部署方式；登录态、网页内容、模型调用与浏览器托管需分别评估。 |
| [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) | 应用 / 工具栈。同仓库包含 GUI 桌面应用 UI-TARS Desktop，以及集成视觉和工具的 Agent TARS CLI / Web UI。 | 两个产品的安装与模型要求不同；不要把演示中的本地、远程电脑及浏览器能力当成同一种配置。 |

<a id="building-blocks"></a>
### 开发框架与记忆层 · Building blocks

**不是开箱即用的私人助理。** 适合已经决定自己开发的人。

| 项目 | 解决的问题 | 仍需自己负责 |
| --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 有状态 Agent 的流程编排、持久执行、人工介入与记忆基础设施。 | 工具权限、用户界面、业务逻辑、部署与真实任务评估。 |
| [Mem0](https://github.com/mem0ai/mem0) | 给应用提供用户、会话与 Agent 记忆层；有库、自托管服务与托管平台等路径。 | 收集哪些记忆、访问控制、删除与纠错、模型/嵌入配置；记忆层本身不会执行任务。 |

<a id="papers"></a>
## 论文 · Papers

→ [查看论文目录](docs/PAPERS.md)

论文分为两组，避免把测量工具与被测系统混在一起：

- **Eval / Benchmark（评测与基准）**：研究如何衡量任务完成、工具使用、记忆、长期交互、移动端/网页/电脑操作等能力。记录环境、任务与指标，说明覆盖不到什么。
- **Agent 方法 / 系统（Methods & Systems）**：研究规划、执行、反思、记忆、主动性与持续运行等机制。记录核心贡献、实验范围和实现/代码状态。

阅读范围应明确标注为摘要、选读章节或全文；论文中的成绩是**作者报告**，除非另有可复现的独立记录，不写成“我们评测发现”。不同任务集、模型、预算和版本的分数不能直接拼接成产品排名。

<a id="comparison"></a>
## 如何比较 · Evaluation guide

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

欢迎补充项目、产品与论文，纠正过时信息，也欢迎可复现的使用或研究复现记录。请先读 [中文贡献指南](CONTRIBUTING.md) / [English contribution guide](CONTRIBUTING.en.md)，同步更新对应目录的来源与日期，并遵循 [来源记录](docs/SOURCES.md) 的核验口径。

**本仓库内容的许可证尚未指定，待维护者决定。** 所链接的第三方项目各自适用其许可证和服务条款；收录不代表重新授权它们的源码、商标或文档。
