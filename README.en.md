# Awesome Personal Agent

[简体中文](README.md) | English

> A curated guide to personal AI agents: open-source projects, publicly available products, evaluation benchmarks, and agent research.

**Fewer names, more useful selection criteria.** This repository covers source-code projects, publicly available products—including commercial services—and relevant papers. It records capabilities, availability, research contributions, and evidence limits separately rather than combining them into a single ranking.

Initial documentation review for source-code projects: **2026-10-31**. Product and paper entries carry their own dates and review scopes. Review does not mean hands-on testing, paper reproduction, or a security audit. Project links lead to official repositories, product links to official access points, and paper links to the originals. See the [source notes](docs/SOURCES.en.md) for evidence and review conventions.

| What are you looking for? | Start here | How to read it |
| --- | --- | --- |
| Install, self-host, or customize an agent | [Source-code projects](#source-projects) | Distinguish applications, runtimes, frameworks, and components; check deployment requirements |
| Use a personal-agent service directly | [Publicly available products](docs/PRODUCTS.en.md) | Includes commercial services; check access, region/account requirements, and payment conditions separately |
| Understand how agent capabilities are measured | [Papers: Eval / Benchmark](docs/PAPERS.en.md) | Examine tasks, environments, metrics, and limitations—not leaderboard scores as a proxy for real-world reliability |
| Understand how agents are built | [Papers: Methods / Systems](docs/PAPERS.en.md) | Examine planning, memory, tool use, long-running behavior, and what the paper actually validates |

## Contents

- [Start here](#start-here)
- [Scope](#scope)
- [Publicly available products, including commercial services](#products)
- [Source-code projects](#source-projects)
  - [Persistent personal assistants](#personal-assistants)
  - [Mobile agents](#mobile-agents)
  - [Computer & browser use](#computer-and-browser)
  - [Building blocks](#building-blocks)
- [Papers: benchmarks, methods, and systems](#papers)
- [Evaluation guide](#comparison)
- [Safety checklist](#safety)
- [Related lists](#related-lists)
- [Contributing & licensing](#contributing)

<a id="start-here"></a>
## Start here

These are reading routes, not a “best agent” ranking. Your choice depends on devices, models, permissions, and the maintenance effort you can support.

| Your goal | Start with | Check first |
| --- | --- | --- |
| Tell an Android phone to operate apps for you | [Mika](https://github.com/wangzan101/Mika) | Android version, debugging permissions, model provider, and beta limitations |
| Reach a persistent assistant through messaging apps | [OpenClaw](https://github.com/openclaw/openclaw), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [nanobot](https://github.com/HKUDS/nanobot) | Where it keeps running, how accounts connect, and which actions execute automatically |
| Focus on persistent memory and personal context | [Letta Code](https://github.com/letta-ai/letta-code), [Khoj](https://github.com/khoj-ai/khoj) | Where memories/documents are stored, whether they can be deleted, and what reaches the model |
| Customize a messaging assistant with a smaller codebase | [NanoClaw](https://github.com/nanocoai/nanoclaw) | Container mounts, channel installation, and the cost of maintaining custom code |
| Give an agent an isolated computer environment | [Agent Zero](https://github.com/agent0ai/agent-zero) | Docker, mounted directories, and host-bridge permissions |
| Write code to automate websites or phones | [Browser Use](https://github.com/browser-use/browser-use), [Mobilerun](https://github.com/droidrun/mobilerun) | Local versus hosted options, device connectivity, and runtime requirements |
| Build your own assistant rather than install one | [LangGraph](https://github.com/langchain-ai/langgraph), [Mem0](https://github.com/mem0ai/mem0) | You still need interfaces, authorization, scheduling, storage, and evaluation |
| Find a service without deploying it yourself | [Product directory](docs/PRODUCTS.en.md) | Whether access is open and requires a subscription, supported region, or eligible account |
| Study agent evaluation or implementation methods | [Paper directory](docs/PAPERS.en.md) | Benchmark versus method; what was read; whether results are only author-reported |

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

<a id="personal-assistants"></a>
### Persistent personal assistants

“Persistent” describes a supported way of running the assistant, not a guarantee that a default installation stays online all day. Device sleep, service interruptions, channel restrictions, and model quotas can affect tasks.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Application / runtime. Nous Research's assistant with persistent memory, past-conversation search, reusable skills, scheduled tasks, and messaging interfaces. | Requires model and runtime configuration. Skill learning is an implemented mechanism, not a guarantee of automatic, continuous improvements in task performance. |
| [Khoj](https://github.com/khoj-ai/khoj) | Application. Document- and web-oriented answers, research, custom agents, and recurring information tasks; self-hosting and a cloud service are available. | Best approached as a knowledge and research tool. Check indexing, model, and cloud data flows before connecting documents; it is not a general phone-control tool. |
| [Letta Code](https://github.com/letta-ai/letta-code) | Application / runtime. Persistent identity and editable memory, with a CLI, messaging channels, tools, skills, and scheduling. | Current source is in `letta-code`, not the old V1 server. It supports local and Cloud backends: check the selected backend rather than assuming memories stay on-device by default. |
| [nanobot](https://github.com/HKUDS/nanobot) | Application / framework. A Python personal agent with WebUI, terminal and messaging interfaces, file tools, memory, MCP, and scheduling. | Bring a model service or local model. Features documented for current source can differ from the published stable release; verify your version. |
| [NanoClaw](https://github.com/nanocoai/nanoclaw) | Application / runtime. A personal messaging assistant emphasizing customizable code and container execution, with memory, scheduled tasks, and channels added as needed. | The current repository is `nanocoai/nanoclaw`. Containers do not guarantee safety: inspect mounts, credentials, shared channels, and network access. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Application / runtime. A local Gateway manages sessions, tools, and messaging channels, with persistent state, skills, and replaceable model providers. | Official documentation warns that main-session tools can run on the host unless sandboxing is configured. Read the security guidance before connecting external message sources or exposing remote access. |

<a id="mobile-agents"></a>
### Mobile agents

The distinguishing capability here is **reading and operating phone app interfaces**, not simply giving a desktop agent a mobile chat interface.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Mika](https://github.com/wangzan101/Mika) | Android application. Operates apps through a background display and includes a browser, script sandbox, scheduled tasks, and a Chinese-language interface. | **Early public beta.** Installation requires Android 11+; check the documentation for your installed release for the minimum version for app control. Android 14+ is recommended; the sandbox is arm64-only. On-phone execution does not mean offline inference: content goes to your configured model provider. |
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) | Research / framework. A collection of generations of mobile and cross-platform GUI agents, models, and experimental code for studying interface understanding and multi-step operation. | Choose a specific subproject and version before checking environment and model requirements. Paper demonstrations do not promise compatibility with every phone, app, or task. |
| [Mobilerun (formerly DroidRun)](https://github.com/droidrun/mobilerun) | Framework. CLI / Python mobile automation combining interface trees and screenshots, with separate official Android and iOS integration paths. | Not equivalent to a standalone personal-assistant APK. Configure devices, Portal, debugging, or USB connections for each platform; distinguish the local framework from the Cloud product. |

<a id="computer-and-browser"></a>
### Computer & browser use

These tools address execution. They do not necessarily include persistent personal identity, background task management, or everyday-service integrations.

| Project | Form and main use | Selection caveat |
| --- | --- | --- |
| [Agent Zero](https://github.com/agent0ai/agent-zero) | Application / framework. A Dockerized Linux desktop, browser, projects, memory, skills, and subagents for research, files, and multi-step work. | A host bridge expands the permission boundary. Mount only necessary directories, and distinguish container operations from host access. |
| [Browser Use](https://github.com/browser-use/browser-use) | Framework / tool. Model-driven browser tasks through a local library and CLI, alongside separate hosted browsers and an Agent API. | The open-source library and paid hosted services are different deployment options. Evaluate login sessions, page contents, model calls, and browser hosting separately. |
| [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) | Application / tool stack. One repository includes the UI-TARS Desktop GUI application and Agent TARS CLI / Web UI with vision and tool integrations. | The two products have different installation and model requirements. Local computers, remote computers, and browsers shown in demos are not one interchangeable configuration. |

<a id="building-blocks"></a>
### Building blocks

**Not ready-made personal assistants.** These are for people who have decided to build their own.

| Project | Problem addressed | Still your responsibility |
| --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful-agent orchestration, durable execution, human intervention, and memory infrastructure. | Tool permissions, interfaces, business logic, deployment, and evaluation on real tasks. |
| [Mem0](https://github.com/mem0ai/mem0) | User, session, and agent memory layers, with library, self-hosted server, and hosted-platform options. | What to retain, access control, deletion and correction, and model/embedding configuration. A memory layer does not execute tasks by itself. |

<a id="papers"></a>
## Papers

→ [Browse the paper directory](docs/PAPERS.en.md)

Papers are divided into two groups so that measurement tools are not confused with the systems they measure:

- **Eval / Benchmark**: measuring task completion, tool use, memory, long-term interaction, and mobile/web/computer operation. Record environments, tasks, metrics, and what is not covered.
- **Agent Methods / Systems**: planning, execution, reflection, memory, proactive behavior, and persistent operation. Record the contribution, experimental scope, and implementation/code availability.

State whether the review covered an abstract, selected sections, or the full paper. Scores in a paper are **author-reported** unless separately accompanied by reproducible independent records; do not present them as this repository's own evaluation. Scores across different task sets, models, budgets, and versions cannot simply be combined into a product ranking.

<a id="comparison"></a>
## Evaluation guide

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

**No license has yet been selected for this repository's content; the maintainer will decide.** Linked third-party projects retain their own licenses and terms. Inclusion does not relicense their code, trademarks, or documentation.
