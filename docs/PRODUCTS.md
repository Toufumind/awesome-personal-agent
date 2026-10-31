# 公开商业产品 · Public commercial products

[English](PRODUCTS.en.md) · [返回主清单](../README.md)

**核验日期：2026-10-31（UTC）。** 这页补充可直接使用的商业 / 专有 personal-agent 产品，不替代主清单中的开源应用、运行时与框架。排序按使用方式，不是推荐排名。

## 怎么读

- **证据级别：官方文档核验。** 下列任务能力和安全机制均为厂商文档所述，**不是本仓库实测结果**。本轮未安装、登录、购买套餐或执行任何对外操作。
- **已提供 ≠ 人人可用。** 套餐、灰度、所在地区、年龄、组织管理员、设备及第三方服务仍可限制访问；预览 / 实验性单列标注，不写成正式全面开放。
- **商业产品不一定开源；免费使用也不意味着开源。** 此处按完整成品服务收录，不因其使用开放模型、公开 SDK 或 Chromium 就把整套产品称为开源；未主张它们有完整可自托管源码。
- **“地区待确认”**表示本次查阅的官方来源未提供可确认的完整清单，不代表全球可用。中文界面也不代表中国大陆可注册或使用。
- 不固化易变价格或额度；核对官方套餐页与结账页面。模型名、agent 产品版本、主控模型、子 agent 模型和图像 / 语音模型不是一回事。

## 快速定位

| 产品 | 主要交付方式 | 当前阶段 / 最重要门槛 |
| --- | --- | --- |
| [ChatGPT Work](#chatgpt-work) | 多步任务、文件交付、云浏览器 | 已提供；合资格付费计划与工作区权限 |
| [Claude Cowork](#claude-cowork) | 文档、文件、浏览器与桌面工具 | 已提供；部分平台 / 团队体验为 beta |
| [Manus](#manus) | 云电脑任务与成果制作 | 已提供；credits 与任务权限 |
| [Genspark Super Agent](#genspark) | 成果制作、连接应用、代拨电话 | 已提供；电话需付费、号码验证及地区支持 |
| [Perplexity Computer](#perplexity-computer) | 后台工作、研究、文件及本机扩展 | 已提供；Brain 记忆仍为研究预览 |
| [Comet Assistant](#comet) | 已登录浏览器中的网页任务 | 已提供；浏览器下载与 agent 额度不同 |
| [Lindy](#lindy) | 邮箱、日程与消息入口的工作助理 | 已提供；偏个人工作 / 团队场景 |
| [Alexa+](#alexa) | 家庭语音、日程、设备与生活服务 | 美国已开放；其他地区阶段和能力不同 |
| [Gemini Tasks](#gemini) | Google 上下文、浏览器与定时任务 | 已开放但仍属实验性；地区限制明显 |
| [Copilot Cowork（个人版）](#copilot) | Microsoft 365 文件、邮件与日程 | **Preview**；美国 / 加拿大，Premium / Pro |

表中摘要的依据、平台及权限边界见对应条目。

## 已提供的产品

<a id="chatgpt-work"></a>
### ChatGPT Work — 通用任务与交付物

- **入口 / 门槛：** Web、移动端及合资格桌面端；付费计划和组织权限适用。地区先查 [ChatGPT 支持清单](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)。
- **任务 / 模型：** 研究、文档、表格、演示等交付；可用模型由套餐、工作区和模型选择器决定，不把 Work 等同于一个模型。[Work 与 Codex 说明](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- **数据 / 权限：** 云浏览器有独立 cookies 和登录态，不继承本机浏览器；网站访问授权与重要操作确认分开。桌面本地执行也不意味着消息和任务上下文只留本机。[云浏览器说明](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
- **边界：** 网站可能阻止自动访问，最终步骤可能需接管。旧 [ChatGPT agent 页面](https://help.openai.com/en/articles/11752874-chatgpt-agent) 的 Overview 已宣布不再提供并指向 Work；同页仍残留旧说明，本页不沿用旧额度。

**建议首测（未执行）：** 根据三份公开资料生成带来源的一页比较报告，不登录任何账户。

<a id="claude-cowork"></a>
### Claude Cowork — 文件与知识工作

- **入口 / 门槛：** 付费计划；桌面 macOS、Windows、Linux（beta），以及 Web / 移动端；Team 部分体验为 beta，Enterprise 需管理员开启。地区查 [Claude 支持清单](https://support.claude.com/en/articles/8461763-where-can-i-access-claude)。[当前上手文档](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- **任务 / 模型：** 整理文件、产出办公文档、研究、定时工作及浏览器操作；使用 Claude，具体模型以当前账户为准。不要与需要自己集成的 computer-use API 混为一谈。
- **数据 / 权限：** 当前文档描述云端会话；访问本地文件 / 应用经桌面端连接，打开的本地文件会在 Anthropic 服务器处理。隔离执行不等于数据不出设备。[安全说明](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- **边界：** 直接 computer use 的点击 / 输入不能视为每一步都经过普通工具的权限检查；敏感目录不应一并授权。云任务继续运行也不意味着离线电脑上的资源仍可访问。

**建议首测（未执行）：** 对一个仅含测试文件的目录提出整理方案，确认后复制整理，禁止删除原件。

<a id="manus"></a>
### Manus — 云电脑与成果制作

- **入口 / 门槛：** Web，macOS、Windows、iOS、Android；公开提供免费 / 付费 credits 方案，完整地区清单待确认。[下载](https://manus.im/download) · [套餐机制](https://manus.im/docs/introduction/plans)
- **任务 / 模型：** 云沙箱内研究、制作文件 / 演示 / 网站；Manus 2.0 还说明了事件自动化。产品版本不等于底层模型版本；本轮未核实完整模型路由。[架构与任务环境](https://manus.im/docs/introduction/welcome) · [2.0 发布说明](https://manus.im/blog/introducing-manus-2-0)
- **数据 / 权限：** Browser Operator 是独立的本机浏览器路径，使用已有登录态，每次会话授权，需桌面浏览器在线；官方推荐 Chrome / Edge。它与独立云浏览器的账户边界不同。[Browser Operator](https://manus.im/docs/features/browser-operator)
- **边界：** 不把网站生成、付费 Cloud Computer、浏览器操作和云端研究视为同一成本或同一权限。厂商“自主完成”措辞不是可靠性测评。

**建议首测（未执行）：** 研究一个公开主题并交付可下载文档；核对来源、文件和实际 credits 消耗。

<a id="genspark"></a>
### Genspark Super Agent — 成果与跨应用执行

- **入口 / 门槛：** Web；Super App 支持 Apple Silicon macOS、Windows、Linux。下载免费不等于任务免费，使用受计划与 credits 约束；完整地区清单待确认。[桌面说明](https://www.genspark.ai/helpcenter/super-app)
- **任务 / 模型：** 新 Super Agent 使用云沙箱、浏览器及文件系统，生成研究、表格、演示并复用 skills；模型 / 工具由产品编排，本轮未确认每一步的固定底座。[Super Agent](https://www.genspark.ai/helpcenter/super-agent)
- **数据 / 权限：** 接入邮箱、云盘等后可读写；不同连接的 OAuth 范围不一样，部分请求为固定权限集，不能假定“只选了文件”就只获得该文件的读取权限。[连接器权限说明](https://www.genspark.ai/helpcenter/connectors-and-integrations)
- **差异 / 边界：** Call For Me 可代拨真实电话并返回摘要，需付费计划、号码验证，部分国家未开放；不能用于营销、骚扰或隐藏 AI 身份。此处仅核文档，没有拨号。[电话工具说明](https://www.genspark.ai/helpcenter/call-for-me)

**建议首测（未执行）：** 用脱敏数据生成表格与说明，不接邮箱、不发邮件、不拨电话。

<a id="perplexity-computer"></a>
### Perplexity Computer — 后台工作与桌面扩展

- **入口 / 门槛：** Computer 面向 Pro / Max；Personal Computer 已有 Mac 和 Windows 入口。完整地区清单待确认；不能沿用早期 Windows 等候名单描述。[产品页](https://www.perplexity.ai/en-GB/products/computer) · [Windows 发布](https://www.perplexity.ai/changelog/shared-workspaces-personal-computer-for-windows-and-model-council)
- **任务 / 模型：** 研究、文件、应用、连接工具及持续任务；多模型编排，可按支持情况选择模型 / effort。Brain 记忆属于研究预览，不把它写成所有用户默认具备。[模型与运行方式更新](https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace) · [Max 与 Brain](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)
- **数据 / 权限：** 本机扩展可访问连接的文件夹、应用和已登录浏览器；Mac 设置涉及辅助功能、屏幕录制及磁盘访问等权限。普通 Computer 云端任务不能宣传成全本地推理。[本机设置](https://www.perplexity.ai/personal-computer-setup)
- **边界：** Personal Computer、Hybrid compute、Portable Computer 有不同硬件与数据流；选择本地模式前核对专门文档，不由“Personal”一词推断隐私。

**建议首测（未执行）：** 从专用测试目录生成摘要，要求列出每个读取的文件且不得修改。

<a id="comet"></a>
### Comet Assistant — 浏览器中的执行入口

- **入口 / 门槛：** Comet 已支持 macOS、Windows、iOS、Android。完整地区清单待确认；不同平台功能不应假定一致。[下载与平台](https://www.perplexity.ai/comet)
- **任务 / 模型：** 围绕标签页、网页与登录态进行研究和操作。Agent 查询额度与浏览器下载分开，当前订阅表不向 Free 提供 Browser Agent 查询；模型能力随模式 / 套餐变化。[订阅对照](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you) · [Max Assistant](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)
- **数据 / 权限：** 厂商说明密码等保存在设备，但请求所需标签页内容和相关历史可送到 Perplexity；可按网站阻止任务或关闭 Assistant。**凭据本地保存不等于页面内容不上传。**[Privacy Snapshot](https://www.perplexity.ai/en-GB/hub/blog/introducing-privacy-snapshot)
- **边界：** 这是浏览器 agent，不代表能任意操作手机 App；也不是上面的完整 Computer 工作环境。

**建议首测（未执行）：** 比较三个公开网页的同一指标，逐条核对引用，不登录或提交表单。

<a id="lindy"></a>
### Lindy — 邮箱与日程工作助理

- **入口 / 门槛：** Web、Slack、手机消息 / 语音入口；有试用 credits 与付费方案。更偏个人工作和团队，短信 / 电话等渠道的完整地区支持待确认。[助理场景](https://www.lindy.ai/hire/executive-assistant) · [套餐](https://www.lindy.ai/pricing)
- **任务 / 模型：** 邮箱处理、日程安排、会前准备、定时简报；套餐页说明可按任务选模型，但本页不锁定某个底座版本。[产品与记忆 / routines](https://www.lindy.ai/)
- **数据 / 权限：** 授权连接邮箱、日程及其他服务；官方声明权限可撤销、操作有日志，Lindy 及其模型提供商不以用户数据训练模型。这是厂商声明，不是本仓库安全审计。[安全说明](https://www.lindy.ai/security)
- **边界：** 获得邮箱权限不等于获得任意外发授权；先确认草稿、自动发送、邀请和团队共享的边界。共享工作区也不能当私人记忆保险箱。

**建议首测（未执行）：** 用测试邮箱制作每日简报与回复草稿，禁止发送、归档和删除。

<a id="alexa"></a>
### Alexa+ — 家庭语音与生活服务

- **入口 / 门槛：** 美国已向客户开放，通过兼容设备、Alexa app、Web 使用；Prime 完整权益与免费有限聊天体验不同，其他地区规则不能直接套用。[美国可用性与套餐](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)
- **任务 / 模型：** 家庭日程、智能家居、购物与支持的生活服务；官方说明使用 Amazon Nova 和 Anthropic 模型，不提供统一固定版本承诺。
- **地区 / 阶段：** 日本于 2026-10-29 开始 Early Access，仍需申请；日本餐厅预订、外卖等在当前公告中是未来计划。各国功能与开放阶段必须分别看。[国际与日本更新](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)
- **数据 / 权限：** 家庭偏好、语音、共享资料和连接服务进入助理上下文；Privacy dashboard 可管理交互、附件及录音保留设置。多成员家庭还需确认谁能调用购买、日历和设备能力。[同一官方说明的隐私部分](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)

**建议首测（未执行）：** 在支持的地区添加一条无私人信息的测试提醒并删除，先不启用购物或门锁控制。

## 实验性与预览：不要当作全面正式开放

<a id="gemini"></a>
### Gemini Tasks — Google 上下文与多步任务

- **阶段 / 门槛：** 实验性；18+、个人 Google 账户、AI Pro / Ultra，须开启 Keep Activity 与 Personal Intelligence。Web、移动端、Mac；不支持工作 / 学校账户。支持地区中排除 EEA、尼日利亚、瑞士和英国。[任务与可用性](https://support.google.com/gemini/answer/17094507?hl=en)
- **任务 / 模型：** 邮箱、文件、浏览器任务及日程；Gemini 模型 / 思考设置以账户菜单为准。[模型说明](https://support.google.com/gemini/answer/18648722) · [任务日程](https://support.google.com/gemini/answer/17094710)
- **数据 / 权限：** 可使用连接应用与登录网站上下文；本地 Chrome 的已有会话与云浏览器保存的数据需分别管理。敏感操作必须监督，不以定时任务代替授权。
- **命名 / 边界：** 官方 FAQ 明确 Spark 已改名 Task；不是独立的 Google Tasks 待办 App，也不能据此推断所有 Android App 都可操控。[同一任务文档](https://support.google.com/gemini/answer/17094507?hl=en)

**建议首测（未执行）：** 定时检查一个公开网页是否变化，验证通知与取消，而非操作个人邮箱。

<a id="copilot"></a>
### Microsoft Copilot Cowork（个人版）— Microsoft 365 工作流

- **阶段 / 门槛：** **Preview**。2026 年 10 月订阅表列出美国 / 加拿大的 Microsoft 365 Premium、Pro；Personal / Family 不包含此项，权益仅归订阅所有者。[订阅与地区表](https://support.microsoft.com/en-gb/microsoft-365-copilot/ai-credits-and-limits-for-microsoft-365-subscriptions)
- **任务 / 平台：** 浏览器及 Copilot 桌面入口，文档、Excel、PowerPoint、Outlook 邮件 / 日程、OneDrive 和定时任务；平台 / 设备可用性仍不同。[个人版上手文档](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork)
- **模型 / 数据：** 本轮未确认个人版 Cowork 的固定模型组合；不能把企业版底座或数据保护承诺直接外推。接入文件和账户后可产生真实写入，敏感操作需审阅 / 接管。
- **命名 / 边界：** Copilot Tasks 正迁往 Cowork；工作 / 学校版的正式可用状态不等于个人版已正式发布。[迁移说明](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app)

**建议首测（未执行）：** 用测试 OneDrive 文件生成摘要和新的副本，不覆盖源文件、不发邮件。

## 比“能不能做”更值得核对的六件事

1. **账户真实可用性：** 官网可打开、App 可下载、已付费、特定 agent 功能已开通是四件事。
2. **任务闭环：** 收到计划或“已完成”不算证据；打开成果，核对来源或目标系统中的结果。
3. **权限与记忆：** 分开记录读取、写入、外发、购买、后台运行、记忆保留和团队共享范围。
4. **本地与云端：** 分清执行机器、推理位置、文件上传、浏览器 cookies、第三方模型和日志；“本地客户端”不等于全本地。
5. **失败与退出：** 试验停止、拒绝、接管、取消定时任务及撤销连接；确认停止后是否仍有排队任务。
6. **真实成本：** 记录套餐、credits、模型、耗时、人工接管次数和最终成果；不能把单次演示当成功率。

后续贡献应附核验日期与官方依据。要写“实测”，请额外提供任务输入、环境 / 版本、账号地区与套餐、权限、过程记录和可核验结果；不要提交任何凭据或私人账户数据。
