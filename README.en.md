# Awesome Personal Agent

![Awesome Personal Agent banner](assets/banner.png)

Personal AI agents: projects, products, and research.

[简体中文](README.md) · **English**

**[31 projects](#source-projects) · [Products](docs/PRODUCTS.en.md) · [Papers](docs/PAPERS.en.md)**

<a id="start-here"></a>
## Contents

- [Persistent assistants](#personal-assistants)
- [Mobile agents](#mobile-agents)
- [Desktop knowledge & work](#desktop-assistants)
- [Computer & browser use](#computer-and-browser)
- [Building blocks](#building-blocks)
- [Developer previews](#previews)

<a id="open-source--source-available-projects"></a>
<a id="source-projects"></a>
## Projects

Open-source and source-available projects, grouped by use—not ranked.

<a id="persistent-personal-assistants"></a>
<a id="personal-assistants"></a>
### Persistent assistants

- [AstrBot](https://github.com/AstrBotDevs/AstrBot) — Chat interfaces, knowledge bases, and tool integrations.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — Persistent memory, reusable skills, and scheduled tasks.
- [IronClaw](https://github.com/nearai/ironclaw) — Rust assistant runtime with WASM / MCP extensions.
- [Khoj](https://github.com/khoj-ai/khoj) — Research assistant for personal documents and the web.
- [Letta Code](https://github.com/letta-ai/letta-code) — Persistent identity, editable memory, and tool execution.
- [Moltis](https://github.com/moltis-org/moltis) — Assistant server with voice, chat, and scheduled tasks.
- [nanobot](https://github.com/HKUDS/nanobot) — Lightweight Python agent with memory, tools, and messaging channels.
- [NanoClaw](https://github.com/nanocoai/nanoclaw) — Customizable messaging assistant with container-based execution.
- [OpenClaw](https://github.com/openclaw/openclaw) — Local Gateway connecting messaging channels, sessions, and tools.
- [PicoClaw](https://github.com/sipeed/picoclaw) — Lightweight assistant with tools and reminders. **Pre-1.0; not for production.**
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) — Formerly CoPaw; chat, office files, and browser tasks. **Desktop: Beta.**
- [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) — Rust runtime for messaging, webhooks, and hardware events.

[ Setup & caveats → ](docs/GUIDE.en.md#personal-assistants)

<a id="mobile-agents"></a>
### Mobile agents

- [Mika](https://github.com/wangzan101/Mika) — Android app control, browser, and scheduled tasks. **Early beta.**
- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) — Research framework for mobile and cross-platform GUI agents.
- [Mobilerun](https://github.com/droidrun/mobilerun) — Formerly DroidRun; CLI / Python mobile automation, not a standalone APK.
- [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) — Screenshot-driven phone research framework; requires a model endpoint.
- [Operit](https://github.com/AAswordman/Operit) — Android assistant for UI, files, terminal, and workflows. **ARM64 only.**

[ Setup & caveats → ](docs/GUIDE.en.md#mobile-agents)

<a id="desktop-knowledge--work-assistants"></a>
<a id="desktop-assistants"></a>
### Desktop knowledge & work

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) — Document knowledge bases, web research, and tool-driven file outputs.
- [Eigent](https://github.com/eigent-ai/eigent) — Single- and multi-agent research, writing, and file organization.
- [LobsterAI](https://github.com/netease-youdao/LobsterAI) — Desktop work assistant using the OpenClaw runtime.
- [OpenWorker](https://github.com/andrewyng/openworker) — Meeting preparation, reports, and reviewable actions. **Open beta; Windows unsigned.**
- [Rowboat](https://github.com/rowboatlabs/rowboat) — Connects email, meetings, and conversations to a knowledge graph and background work.

[ Setup & caveats → ](docs/GUIDE.en.md#desktop-assistants)

<a id="computer-and-browser"></a>
### Computer & browser use

- [Agent Zero](https://github.com/agent0ai/agent-zero) — Dockerized desktop, browser, memory, and multi-step tasks.
- [Browser Use](https://github.com/browser-use/browser-use) — Model-driven browser automation library and CLI.
- [goose](https://github.com/aaif-goose/goose) — Runtime for research, writing, and file tasks through extensions and MCP.
- [UI-TARS Desktop / Agent TARS](https://github.com/bytedance/UI-TARS-desktop) — GUI desktop application and vision / tool agent stack.

[ Setup & caveats → ](docs/GUIDE.en.md#computer-and-browser)

<a id="building-blocks"></a>
### Building blocks

- [LangGraph](https://github.com/langchain-ai/langgraph) — Stateful agent orchestration, durable execution, and human intervention.
- [Mem0](https://github.com/mem0ai/mem0) — User, session, and agent memory layer—not a complete assistant.

[ Setup & caveats → ](docs/GUIDE.en.md#building-blocks)

<a id="developer-previews--alpha-projects"></a>
<a id="previews"></a>
### Developer previews

- [Leon](https://github.com/leon-ai/leon) — **2.0 Developer Preview**: memory, skills, and proactive polling; source setup required.
- [OpenMuse](https://github.com/CopilotKit/openmuse) — **Alpha template**: mobile / web tasks and human takeover; payments and bookings remain roadmap items.
- [Operit2](https://github.com/AAswordman/Operit2) — **Cross-device preview**: resumes at persisted tool results, not live sessions.

[ Setup & caveats → ](docs/GUIDE.en.md#previews)

<a id="publicly-available-products"></a>
<a id="products"></a>
## Products

- [ Publicly available products, including commercial services → ](docs/PRODUCTS.en.md) — Access, pricing, and region / account restrictions.

<a id="papers"></a>
## Papers

- [ Paper directory → ](docs/PAPERS.en.md) — Eval / Benchmark · Agent Methods / Systems.

<a id="scope"></a>
<a id="evaluation-guide"></a>
<a id="comparison"></a>
<a id="safety-checklist"></a>
<a id="safety"></a>
## Before you start

For tool-using AI systems working toward personal goals; frameworks and previews are not ready-made assistants.

Use test data and minimal permissions; require approval for sensitive actions. Local deployment or containers do not guarantee safety or offline inference.

[Scope](docs/GUIDE.en.md#scope) · [Evaluation guide](docs/GUIDE.en.md#comparison) · [Safety checklist](docs/GUIDE.en.md#safety) · [Task guide](docs/LANDSCAPE.en.md) · [Trial protocols](docs/TASKS.en.md)

Documentation review: **2026-10-31**. Not hands-on tests, reproductions, or security audits; trial protocols remain unexecuted. [Evidence & dates](docs/SOURCES.en.md) (products and papers have separate review dates).

<a id="related-lists"></a>
## Related lists

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents)
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents)
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices)

<a id="contributing--licensing"></a>
<a id="contributing"></a>
## Contributing & license

[Contributing](CONTRIBUTING.en.md) · [Source notes](docs/SOURCES.en.md)

Original prose and curation: **CC BY 4.0**. Designated original scripts/tests: **MIT**. Third-party terms remain separate; see [license scope](docs/LICENSE.md#en).
