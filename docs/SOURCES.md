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

产品与论文条目的详细依据集中保存在各自目录，避免复制出两份不同步的可用性或阅读记录。

## 分类型核验口径

- **源码项目**：官方仓库与版本文档是功能/部署依据；公开代码、可安装、自托管与开源许可分别判断。
- **产品**：产品页用于用途，帮助/开放说明用于可用性，定价页用于费用；入口可访问不代表已注册、已开通或已验证任务。候补、邀请、受限预览与公开使用不得混写。
- **论文**：记录原文、版本/年份、发表或预印本状态、阅读范围与日期。只读摘要不得推断全文细节；全文阅读也不等于代码复现。
- **性能结果**：明确区分作者报告、厂商演示和有记录的独立实测。不跨不同模型、预算、任务集或版本直接比较数字。
- **证据缺口**：写明未确认、未读取或未测试，不把空白补成肯定结论；不同来源发生冲突时保留读取时间和边界。

## 源码项目依据

这部分通过网页读取官方仓库 README，核对项目身份、主要用途、部署层次和明显限制。**没有安装、运行、代码审计、漏洞审计或基准测试**；也未穷尽所有操作系统、版本、价格与服务条款。下列“边界”包括由文档事实推导的选型提醒，不是对产品缺陷的测试结论。

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

### Mika 系统要求复核

- **2026-10-31 20:35 UTC**：重新读取官方仓库首页和原始 README，系统要求表为安装/聊天/网页/沙箱 Android 11+、App 操控 Android 12+，推荐 Android 14+；FAQ 与该表一致。
- 同日 **01:59 UTC** 的较早阅读记录曾显示任务需 Android 13+。两个时点的页面证据存在差异，未固定到同一 commit，不能据此断言具体哪次发布调整了要求。
- 因此 README 保留共同明确的安装要求与推荐版本，将 App 操控最低版本写为**按所装版本文档核对**，不把任一主分支快照当作所有发布版本的兼容承诺。

## 候选发现与相关清单

实际查看了以下清单，仅用于了解覆盖范围与发现候选项目；本仓库的项目描述依据上表官方来源独立撰写。

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents)：常驻助理、记忆层、运行时、消息桥接。
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents)：自托管和商业方案、选型维度。
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices)：产品、用例、源码及研究，含中英文。

## 核验范围和维护约定

- README 源码板块的首批快照包含 **14 个项目，4 类主要用途**；这个数字不包含产品与论文目录，也不是完整市场盘点。
- 没有记录 Star、最新 commit 时间或量化可靠性；本轮未核实的指标不作推断。
- 参考主分支 README 不代表所有版本均支持该能力，安装前应再次核对具体版本。
- 网页可读取只说明来源当时可访问，不说明软件安全、服务可用或未来链接稳定。
- 产品目录和论文目录的新增，不表示原有源码项目经过再次实测，也不把研究系统自动认定为公开可用产品。
- 更新某条目时同步更改其来源与核验日期。若只复查了一部分，不应把整份清单的核验日期整体刷新。
- 仓库内容许可证待维护者决定，本轮没有添加 `LICENSE` 文件。
