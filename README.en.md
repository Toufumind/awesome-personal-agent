# Awesome Personal Agent

[简体中文](README.md) | English

> A curated guide to personal AI agents: open-source projects, publicly available products, evaluation benchmarks, and agent research.

**Fewer names, more useful selection criteria.** This repository covers source-code projects, publicly available products—including commercial services—and relevant papers. It records capabilities, availability, research contributions, and evidence limits separately rather than combining them into a single ranking.

Initial documentation review for source-code projects: **2026-10-31**. Product and paper entries carry their own dates and review scopes. Review does not mean hands-on testing, paper reproduction, or a security audit. Project links lead to official repositories, product links to official access points, and paper links to the originals. See the [source notes](docs/SOURCES.en.md) for evidence and review conventions.

<a id="start-here"></a>
## Contents

Choose by task, not by ranking. The [source-project catalog](#source-projects) separates applications, runtimes, frameworks, components, and previews; check the caveats for your device and version.

| I want to… | Start here | Check first |
| --- | --- | --- |
| Reach a persistent assistant or use personal memory | [Persistent personal assistants](#personal-assistants) | Runtime, messaging channels, memory storage, and automatic actions |
| Operate phone apps | [Mobile agents](#mobile-agents) | Ready-made app vs. framework; OS, CPU, device permissions, and model endpoint |
| Work with documents, meetings, and deliverable files | [Desktop knowledge & work assistants](#desktop-assistants) | Packages, connectors, supported outputs, and data flows |
| Research, handle files, or automate a computer/browser | [Computer & browser use](#computer-and-browser) | GUI control vs. tool execution; host access, mounts, and local vs. hosted setup |
| Build my own assistant | [Building blocks](#building-blocks) | Interfaces, authorization, scheduling, storage, and evaluation still need integration |
| Explore early projects and help develop them | [Developer previews & alpha projects](#previews) | Source/build paths vs. finished apps; expect setup and debugging |
| Use a service without deploying it | [Publicly available products](#products) | Access, region/account restrictions, and payment conditions |
| Study evaluation or agent design | [Papers](#papers) | Eval / Benchmark vs. Methods / Systems; review scope and author-reported results |
| Plan a low-risk trial | [Task protocols](docs/TASKS.en.md) | Unexecuted protocols, not results or product scores |
| Connect personal needs with research and implementations | [Task–research–implementation guide](docs/LANDSCAPE.en.md) | Thematic links do not prove paper adoption or benchmark passes |

[Scope](#scope) · [Evaluation guide](#comparison) · [Safety checklist](#safety) · [Related lists](#related-lists) · [Contributing & licensing](#contributing)

<a id="scope"></a>
## Scope

This repository focuses on **AI systems that use tools to carry out tasks toward an individual's goals**. Long-term memory, persistent operation, and proactive work matter, but not every project offers them, and they are not three mandatory properties of every personal agent.

- **Application**: provides a usable interface for delegating tasks after installation and configuration.
- **Runtime**: provides execution, sessions, or long-running operation, usually with configuration and operational work still required.
- **Framework**: requires developers to implement or integrate workflows.
- **Component**: solves only part of the problem, such as memory; it is not a complete assistant.
- **Research**: primarily papers, models, or experimental code; it should not be treated as a mature consumer product.

These describe technical forms, not business models. Commercial products may build on open source, and research systems may publish code. Distinguish a brand's source repository from its hosted service. **Chatting from a phone does not mean controlling the phone; controlling a browser does not mean autonomously handling every everyday task.**

The repository has three tracks:

1. **Source-code projects**: official code or self-hostable implementations, organized by use. Publicly visible source does not automatically carry an open-source license; check upstream licensing.
2. **Publicly available products**: free, paid, and commercially hosted services; public source code is not required. The main directory focuses on public signup, download, or subscription paths. Waitlisted, invite-only, or announced-only products, if retained, must be labeled separately rather than presented as publicly available.
3. **Research papers**: separate **Eval / Benchmark** from **Agent Methods / Systems**. Open-source code is not mandatory. A paper does not imply a usable product, and published code does not imply reproduced results.

This is not a directory of every AI product. Chat-only interfaces, coding-only tools, and generic enterprise workflow platforms are outside the main list; related foundational research must explain its connection to personal agents. There is no minimum star count. Paid placement, affiliate links, and roadmap features presented as delivered capabilities are not accepted.

<a id="products"></a>
## Publicly available products

→ [Browse the product directory, including commercial services](docs/PRODUCTS.en.md)

The directory focuses on entry points people can actually try, not just company names. Each entry should distinguish **purpose, access method, current availability, region/platform/account restrictions, charging model, official evidence, and review date**. “Available” does not mean immediately accessible to every person or region, free of charge, or hands-on tested by this repository.

<a id="source-projects"></a>
## Open-source & source-available projects

Projects below are grouped by their main use. A separate listing for a hosted offering does not count as another independently verified capability set. Payment conditions and availability not detailed here still need checking for the specific version and service.

There are **29 source projects: 26 main-category entries and 3 separate previews**, across five main use categories and one preview section. All original 14 entries are retained. The 15 additions use pinned commits, license files, and release records checked on 2026-10-31. A release number does not guarantee every main-branch capability is present, and `prerelease=false` does not establish maturity or hands-on testing. Root licenses for additions apply to the inspected repository code, not automatically to models, dependencies, plugins, trademarks, or hosted services. See the [expansion evidence](docs/SOURCES.en.md#expansion).

<a id="personal-assistants"></a>
### Persistent personal assistants

“Persistent” describes a supported way of running the assistant, not a guarantee that a default installation stays online all day. Device sleep, service interruptions, channel restrictions, and model quotas can affect tasks.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Application / runtime. Nous Research's assistant with persistent memory, past-conversation search, reusable skills, scheduled tasks, and messaging interfaces. | Requires model and runtime configuration. Skill learning is an implemented mechanism, not a guarantee of automatic, continuous improvements in task performance. |
| [IronClaw](https://github.com/nearai/ironclaw) | Persistent assistant / Rust runtime. WebUI, REPL, channels, cron, and webhook tasks with persistent memory and WASM/MCP extensions. MIT OR Apache-2.0. | Observed ironclaw-v1.4.1; models and channels require configuration. Do not claim complete OpenClaw parity. WASM does not cover every host, Docker, MCP, or network path, nor establish immunity to prompt injection. |
| [Khoj](https://github.com/khoj-ai/khoj) | Application. Document- and web-oriented answers, research, custom agents, and recurring information tasks; self-hosting and a cloud service are available. | Best approached as a knowledge and research tool. Check indexing, model, and cloud data flows before connecting documents; it is not a general phone-control tool. |
| [Letta Code](https://github.com/letta-ai/letta-code) | Application / runtime. Persistent identity and editable memory, with a CLI, messaging channels, tools, skills, and scheduling. | Current source is in `letta-code`, not the old V1 server. It supports local and Cloud backends: check the selected backend rather than assuming memories stay on-device by default. |
| [Moltis](https://github.com/moltis-org/moltis) | Persistent personal-agent server. Web, voice, chat, and cron drive browsing, commands, file/memory updates, and notifications. MIT. | Observed 20261023.01, with release-binary/Homebrew/Docker paths. A single binary does not remove dependencies. The example mounts `docker.sock`; remote execution and host mounts expand authority. Signatures were not verified in this review. |
| [nanobot](https://github.com/HKUDS/nanobot) | Application / framework. A Python personal agent with WebUI, terminal and messaging interfaces, file tools, memory, MCP, and scheduling. | Bring a model service or local model. Features documented for current source can differ from the published stable release; verify your version. |
| [NanoClaw](https://github.com/nanocoai/nanoclaw) | Application / runtime. A personal messaging assistant emphasizing customizable code and container execution, with memory, scheduled tasks, and channels added as needed. | The current repository is `nanocoai/nanoclaw`. Containers do not guarantee safety: inspect mounts, credentials, shared channels, and network access. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Application / runtime. A local Gateway manages sessions, tools, and messaging channels, with persistent state, skills, and replaceable model providers. | Official documentation warns that main-session tools can run on the host unless sandboxing is configured. Read the security guidance before connecting external message sources or exposing remote access. |
| [PicoClaw](https://github.com/sipeed/picoclaw) | Lightweight persistent assistant. WebUI, CLI, and messaging tasks use tools, memory, and reminders, with binary, Docker, and Android runtime paths. MIT. | **Pre-1.0**: distinguish v0.3.1 from nightly; upstream warns against production deployment before v1.0. Running on Android does not establish arbitrary app control. Low runtime resource use excludes full local-model inference costs. |
| [QwenPaw (formerly CoPaw)](https://github.com/agentscope-ai/QwenPaw) | Application / persistent runtime. Console, TUI, and messaging requests produce digests, office files, browser work, and notifications. Apache-2.0. | Non-prerelease v2.2.2.post1; distinguish v2.3.0-beta.1 and the Beta desktop app. Python/Docker deployment needs model and channel setup. Documented initialization with `--defaults` accepts anonymous telemetry. CoPaw is not a separate entry. |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Persistent Rust runtime. Messaging, CLI, webhooks, and device events trigger shell, browser, HTTP, hardware tools, and resumable SOPs. MIT OR Apache-2.0. | Observed v0.8.7. Configure background service, models, channels, and hardware separately. Alongside supervised defaults, YOLO can relax restrictions. Check actual policies, workspace boundaries, and OS sandbox rather than inferring safety from Rust. |

<a id="mobile-agents"></a>
### Mobile agents

The distinguishing capability here is **reading and operating phone app interfaces**, not simply giving a desktop agent a mobile chat interface.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Mika](https://github.com/wangzan101/Mika) | Android application. Operates apps through a background display and includes a browser, script sandbox, scheduled tasks, and a Chinese-language interface. | **Early public beta.** Installation requires Android 11+; check the documentation for your installed release for the minimum version for app control. Android 14+ is recommended; the sandbox is arm64-only. On-phone execution does not mean offline inference: content goes to your configured model provider. |
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) | Research / framework. A collection of generations of mobile and cross-platform GUI agents, models, and experimental code for studying interface understanding and multi-step operation. | Choose a specific subproject and version before checking environment and model requirements. Paper demonstrations do not promise compatibility with every phone, app, or task. |
| [Mobilerun (formerly DroidRun)](https://github.com/droidrun/mobilerun) | Framework. CLI / Python mobile automation combining interface trees and screenshots, with separate official Android and iOS integration paths. | Not equivalent to a standalone personal-assistant APK. Configure devices, Portal, debugging, or USB connections for each platform; distinguish the local framework from the Cloud product. |
| [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | Research / phone-execution framework. Turns tasks and screenshots into taps, typing, and swipes, with takeover and confirmation callbacks. Repository code: Apache-2.0. | Python 3.10+ and a separate model endpoint; Android, HarmonyOS, and iOS have different setup paths. The observed GitHub releases list was empty—not a packaged APK. Screenshots reach the model; check weight licenses separately. |
| [Operit](https://github.com/AAswordman/Operit) | Android application. UI, browser, file, and terminal tasks, with schedules and Tasker/Intent workflows. Main code: LGPL-3.0-only. | Official APK v1.12.2; Android 8.0+, ARM64 only. Device permissions depend on the feature; Root is not universally required. Cloud models can still receive data. Distinguish it from the Operit2 preview. |

<a id="desktop-assistants"></a>
### Desktop knowledge & work assistants

These start from documents, meetings, personal knowledge, and file deliverables rather than chat alone. Check desktop packages, backend runtimes, and cloud services separately for capabilities and data flows.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | Desktop / self-hosted knowledge-and-agent application. Beyond document chat, it supports web research, memory, scheduling, and text/Office/PDF artifacts with the relevant tools enabled. MIT. | Observed v1.19.0. Desktop and Docker differ; multi-user permissions are not universal desktop features. Choose model, embedding, and vector-store providers. Disabling telemetry does not stop those services or tools from receiving data. |
| [LobsterAI](https://github.com/netease-youdao/LobsterAI) | Desktop application. Produces documents, spreadsheets, slides, pages, and charts from local files, with browser, scheduling, and messaging access. MIT. | Release 2026.10.30 was published on 2026-10-31 UTC with Mac/Windows assets. It currently uses an OpenClaw runtime, not an independently tested alternative engine. Models, sharing, and plugins can create external data flows. |
| [OpenWorker](https://github.com/andrewyng/openworker) | Desktop application. Uses authorized files and connectors for meeting preparation, reports, spreadsheets, and reviewable actions, with scheduling. MIT. | **Open beta**, observed v0.3.1. Main downloads support macOS Apple Silicon and Windows x64; Windows packages are not yet code-signed. Check actual approval, logging, and sandbox configuration—not a security certification. |
| [Rowboat](https://github.com/rowboatlabs/rowboat) | Knowledge-oriented desktop assistant. Connects email, meetings, and conversations to a Markdown knowledge graph, drafts, summaries, and background work. Apache-2.0. | Non-prerelease v1.0.3; v1.0.5 is a **prerelease**, and current docs may exceed installed packages. Mac/Windows/Linux paths need models/connectors. Obtain appropriate consent for meeting capture; local Markdown does not keep transmitted context local. |

<a id="computer-and-browser"></a>
### Computer & browser use

These tools address execution. They do not necessarily include persistent personal identity, background task management, or everyday-service integrations.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Agent Zero](https://github.com/agent0ai/agent-zero) | Application / framework. A Dockerized Linux desktop, browser, projects, memory, skills, and subagents for research, files, and multi-step work. | A host bridge expands the permission boundary. Mount only necessary directories, and distinguish container operations from host access. |
| [Browser Use](https://github.com/browser-use/browser-use) | Framework / tool. Model-driven browser tasks through a local library and CLI, alongside separate hosted browsers and an Agent API. | The open-source library and paid hosted services are different deployment options. Evaluate login sessions, page contents, model calls, and browser hosting separately. |
| [goose](https://github.com/aaif-goose/goose) | Desktop / CLI tool runtime. Its current official scope includes research, writing, file editing, and data work through extensions and MCP. Apache-2.0. | Observed v1.57.0; the canonical repository is now `aaif-goose/goose`. Configure models, extensions, and allow/ask/deny policies. It is not a preconfigured life manager; shell and third-party tools expand permissions. |
| [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) | Application / tool stack. One repository includes the UI-TARS Desktop GUI application and Agent TARS CLI / Web UI with vision and tool integrations. | The two products have different installation and model requirements. Local computers, remote computers, and browsers shown in demos are not one interchangeable configuration. |

<a id="building-blocks"></a>
### Building blocks

**Not ready-made personal assistants.** These are for people who have decided to build their own.

| Project | Problem addressed | Still your responsibility |
| --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful-agent orchestration, durable execution, human intervention, and memory infrastructure. | Tool permissions, interfaces, business logic, deployment, and evaluation on real tasks. |
| [Mem0](https://github.com/mem0ai/mem0) | User, session, and agent memory layers, with library, self-hosted server, and hosted-platform options. | What to retain, access control, deletion and correction, and model/embedding configuration. A memory layer does not execute tasks by itself. |

<a id="previews"></a>
### Developer previews & alpha projects

These three entries have research and customization value but **are not equivalent to mature packaged products**. Source, screenshots, or partial release assets do not establish delivery of a complete cross-platform product. Beta/pre-1.0 warnings in the main categories remain applicable too.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Leon](https://github.com/leon-ai/leon) | **2.0 Developer Preview**. A personal-assistant development project with layered memory, native skills, computer/browser tools, and proactive polling. MIT. | The default `develop` branch requires Node 24+, pnpm, and source setup; legacy `master` uses a different architecture. New documentation is unfinished. Recent releases are prerelease bridge/server components, not a complete 2.0 product. |
| [OpenMuse](https://github.com/CopilotKit/openmuse) | **Alpha application template**. Demonstrates task visibility, human takeover, document workflows, drafts, and reminders across mobile/web surfaces. MIT. | The observed GitHub releases list was empty. Requires Node/pnpm, a CopilotKit Intelligence project key, tool setup, and native builds for mobile. Not fully local; scripted/demo verification is not live-account acceptance. Autonomous payments/reservations remain roadmap items. |
| [Operit2](https://github.com/AAswordman/Operit2) | **Cross-device preview**. Host-specific file, terminal, and browser tools, with paired nodes continuing tasks at persisted-tool-result boundaries. Root license: AGPL-3.0. | v2.0.0-preview.3 has only Linux/Windows x86_64/aarch64 CLI assets; other platforms have source/build paths. Formats and protocols may break compatibility. Live model calls, processes, and browser sessions do not migrate; a complete Server product is not ready. |

<a id="papers"></a>
## Papers

→ [Browse the paper directory](docs/PAPERS.en.md)

Papers are divided into two groups so that measurement tools are not confused with the systems they measure:

- **Eval / Benchmark**: measuring task completion, tool use, memory, long-term interaction, and mobile/web/computer operation. Record environments, tasks, metrics, and what is not covered.
- **Agent Methods / Systems**: planning, execution, reflection, memory, proactive behavior, and persistent operation. Record the contribution, experimental scope, and implementation/code availability.

State whether the review covered an abstract, selected sections, or the full paper. Scores in a paper are **author-reported** unless separately accompanied by reproducible independent records; do not present them as this repository's own evaluation. Scores across different task sets, models, budgets, and versions cannot simply be combined into a product ranking.

<a id="comparison"></a>
## Evaluation guide

→ [Low-risk task protocols](docs/TASKS.en.md): templates for planning and recording future trials. **They have not been executed and contain no measured results.** They are not a standardized benchmark or a basis for assigning product scores by themselves.

Do not rely only on “autonomous,” “local-first,” or stars. Start with the same low-risk tasks before gradually granting more permissions.

| Dimension | Questions to record |
| --- | --- |
| Task completion | Does it only advise, or execute and verify the outcome? Can it stop clearly when it fails? |
| Execution location | Phone, desktop, your server, or a vendor's cloud? What happens during sleep or network loss? |
| Proactive behavior | Manual conversation, scheduled trigger, event trigger, or an ongoing goal? Can you pause and cancel easily? |
| Memory | Are conversation history and long-term memory separate? Can you inspect, correct, export, and delete them? |
| Permissions | What access do files, shell, browser, email, and contacts receive? Can sensitive actions require individual approval? |
| Data flows | What reaches model, search, telemetry, messaging, or hosted-browser providers? How long are logs retained? |
| Maintainability | Are installation instructions, releases, migration guides, issue reporting, and security-reporting routes available? |
| Cost | Are models, search, storage, browsers, cloud machines, and messaging charged separately? Can you set a budget? |

Suggested starter tasks: **read a redacted document and cite evidence → organize a test directory and show the changes → create a cancellable, low-risk reminder**. For mobile or browser tools, substitute tasks such as inspecting settings or reading public pages without external side effects. Record the version, model, human interventions, time, cost, outcome, and failure reasons; a single success is not a reliability measure.

<a id="safety"></a>
## Safety checklist

- [ ] Start with test accounts, redacted data, and a separate working directory. Back up important data.
- [ ] Grant only necessary permissions, rather than an entire home directory, every browser login session, or production credentials at once.
- [ ] Initially require human approval for payments, transfers, messages, deletions, publishing, and account-setting changes.
- [ ] Treat websites, emails, documents, and messages as possible sources of malicious instructions—not as user authorization.
- [ ] Review third-party skills, plugins, MCP servers, and installation scripts separately. A standard protocol is not proof of trustworthiness.
- [ ] Know how to stop execution, revoke tokens, disconnect channels, delete memories, and restore data.
- [ ] Handle login and verification steps manually when needed; do not use automation to bypass site rules or security checks.
- [ ] Do not equate open source, self-hosting, containers, or on-device interfaces with privacy, security, or fully offline operation.

This list is for selection and learning. Inclusion does not endorse a project's safety, availability, or claimed performance. Refer to the specific version, official documentation, service terms, and applicable rules before use.

<a id="related-lists"></a>
## Related lists

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents) — Persistent personal agents and their memory, runtime, and messaging ecosystems.
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents) — Self-hosted and commercial personal agents, with selection criteria.
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices) — Products, source projects, use cases, and research, with English and Chinese content.

These lists help discover candidates. Entries here are checked separately against official project sources rather than inheriting another list's capability, licensing, or quality conclusions.

<a id="contributing"></a>
## Contributing & licensing

Suggestions for projects, products, and papers, corrections, and reproducible usage or research-reproduction records are welcome. Read the [English contribution guide](CONTRIBUTING.en.md) / [中文贡献指南](CONTRIBUTING.md), update the relevant directory's sources and dates, and follow the conventions in the [source notes](docs/SOURCES.en.md).

**Original documentation prose and original curated content are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en); original repository scripts and test code use [MIT](scripts/LICENSE).** See the [license scope notice](docs/LICENSE.md#en) for complete boundaries and currently covered files. These are separate licenses by material type, not repository-wide dual licensing. Third-party material, linked projects, and trademarks retain their terms; separate machine-readable fixtures and result templates receive no grant through these notices. Inclusion is not relicensing or endorsement.
