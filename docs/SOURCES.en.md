# Sources and review records

[简体中文](SOURCES.md) | English

Initial review date for source-code projects: **2026-10-31 (UTC)**. Products and papers carry dates in their own entries. Updating this index does not mean every entry has been reviewed again.

This document preserves the documentation-review records for source projects and defines evidence conventions for products and papers. **The directory itself is not a product evaluation report or a set of reproduced paper results.**

## Source index

| Type | Entries and evidence records | What this review can establish |
| --- | --- | --- |
| Source-code projects | [README](../README.en.md) and the project evidence below | What official documentation describes—not successful installation, secure code, or reliable task execution |
| Publicly available products, including commercial services | Official sources and review dates in each [PRODUCTS](PRODUCTS.en.md) entry | Officially stated purpose, access points, availability conditions, and charging—not access for every account or region |
| Eval / Benchmark papers | Evaluation/benchmark group in [PAPERS](PAPERS.en.md) | Tasks, environments, metrics, and limitations supported by the stated reading scope |
| Agent Methods / Systems papers | Methods/systems group in [PAPERS](PAPERS.en.md) | Mechanisms and experiments supported by the stated reading scope; original results remain author-reported |

Detailed product and paper evidence stays in the corresponding directories to avoid duplicating availability or reading records that could drift out of sync.

## Evidence conventions by type

- **Source projects**: official repositories and versioned documentation support capability and deployment descriptions. Public code, installability, self-hosting, and open-source licensing are separate questions.
- **Products**: product pages support purpose, help/availability documents support access conditions, and pricing pages support charges. An accessible entry point does not mean an account was registered, access was activated, or a task was tested. Distinguish waitlists, invitations, restricted previews, and public access.
- **Papers**: record the original, version/year, publication or preprint status, reading scope, and date. Abstract-only reading cannot establish full-text details; reading the full paper is not code reproduction.
- **Performance results**: distinguish author reports, vendor demonstrations, and documented independent tests. Do not directly compare numbers across different models, budgets, task sets, or versions.
- **Evidence gaps**: state unconfirmed, unread, or untested information explicitly rather than filling gaps with positive conclusions. Preserve reading times and limits when sources conflict.

## Source-project evidence

This part was reviewed by reading official repository READMEs on the web, checking project identity, main purpose, deployment level, and important limitations. **No installation, execution, code audit, vulnerability audit, or benchmark run was performed.** Not every operating system, version, price, or service term was examined. The caveats below include selection advice inferred from documentation, not tested findings of product defects.

| Project | Official evidence | What was checked and how it was bounded |
| --- | --- | --- |
| Hermes Agent | [Official README](https://github.com/NousResearch/hermes-agent#readme) | Read descriptions of memory, conversation search, skills, scheduling, and messaging channels. Did not adopt promotional comparisons such as uniqueness or near-zero costs. |
| Khoj | [Official README](https://github.com/khoj-ai/khoj#readme) | Read about document/web answers, custom agents, recurring research, and self-hosted/cloud deployment. Did not describe a knowledge assistant as a general GUI executor. |
| Letta Code | [Current-source README](https://github.com/letta-ai/letta-code#readme), [migration notice in the former main repository](https://github.com/letta-ai/letta#readme) | The former main repository points to `letta-code`. Current documentation describes CLI, memory, channels, scheduling, and local/Cloud backends; the listing therefore uses the current source and flags data location. |
| nanobot | [Official README](https://github.com/HKUDS/nanobot#readme) | Read about WebUI/terminal/messaging interfaces, file tools, memory, scheduling, and user-supplied models. Official documentation explicitly distinguishes main-branch README features from the stable release. |
| NanoClaw | [Official README](https://github.com/nanocoai/nanoclaw#readme) | The old `qwibitai/nanoclaw` address redirects to `nanocoai/nanoclaw`. Read about container execution, custom code, on-demand channels, memory, and scheduled jobs. Did not repeat absolute security claims. |
| OpenClaw | [Official README](https://github.com/openclaw/openclaw#readme) | Read about the Gateway, channels, state, models, and extensions. The Security section explicitly states that main-session tools run on the host without configured sandboxing. |
| Mika | [Official Chinese README](https://github.com/wangzan101/Mika#readme), [raw README](https://raw.githubusercontent.com/wangzan101/Mika/main/README.md) | Read about the background display, browser, sandbox, scheduling, and beta status; Android 11+ installation, Android 14+ recommendation, arm64 sandbox, and requests going to the configured model provider. Readings of the minimum OS for app control differed; see the recheck below. Did not adopt the broad promise of controlling every app. |
| Mobile-Agent | [Official README](https://github.com/X-PLUG/MobileAgent#readme) | A collection of versions, models, papers, and cross-platform GUI projects. Classified as research/framework; did not generalize one demo's success to the whole family. |
| Mobilerun | [Current official README](https://github.com/droidrun/mobilerun#readme) | `droidrun/droidrun` redirects to `droidrun/mobilerun`. Read about CLI/Python, interface trees/screenshots, and separate Android/iOS paths; distinguished the framework from Cloud. |
| Agent Zero | [Official README](https://github.com/agent0ai/agent-zero#readme) | Read about the Docker Linux desktop, browser, projects, memory, and host bridge. The Safety Model advises isolated execution, limited mounts, and review of sensitive actions. |
| Browser Use | [Official README](https://github.com/browser-use/browser-use#readme) | Documentation provides separate Hosted Cloud, CLI, and Python Library paths. Preserved these distinctions and avoided fixing prices that can change. |
| UI-TARS Desktop / Agent TARS | [Official README](https://github.com/bytedance/UI-TARS-desktop#readme) | The Introduction distinguishes the two products and their interfaces. Did not treat remote demonstrations or historical release notes as guarantees of current availability. |
| LangGraph | [Official README](https://github.com/langchain-ai/langgraph#readme) | Read about stateful orchestration, durable execution, human intervention, and memory. Classified as development infrastructure, not a consumer assistant. |
| Mem0 | [Official README](https://github.com/mem0ai/mem0#readme) | Read about user/session/agent memory and library, self-hosted, and cloud-platform paths. Did not cite performance figures or present memory as a task executor. |

### Mika system-requirements recheck

- **2026-10-31 20:35 UTC**: re-read the official repository page and raw README. Their requirements table stated Android 11+ for installation/chat/web/sandbox, Android 12+ for app control, and Android 14+ recommended. The FAQ agreed with that table.
- An earlier reading record at **01:59 UTC** on the same date had stated Android 13+ for tasks. The page evidence differs between readings and was not pinned to the same commit; this does not establish which release changed the requirement.
- The README therefore retains the common installation requirement and recommended version, while directing readers to **check the documentation for their installed release** for the minimum OS for app control. Neither main-branch snapshot is treated as a compatibility promise for every release.

## Candidate discovery and related lists

The following lists were read to understand their scope and discover candidates. Project descriptions in this repository were written independently from the official sources above.

- [ahmadyan/awesome-personal-agents](https://github.com/ahmadyan/awesome-personal-agents): persistent assistants, memory layers, runtimes, and messaging bridges.
- [upgundecha/awesome-personal-agents](https://github.com/upgundecha/awesome-personal-agents): self-hosted and commercial options, with selection criteria.
- [cubxxw/awesome-personal-agent-practices](https://github.com/cubxxw/awesome-personal-agent-practices): products, use cases, source projects, and research, with Chinese and English content.

## Review scope and maintenance

- The initial README source-project snapshot contains **14 projects across four main use categories**. This count excludes the product and paper directories and is not a complete market survey.
- Star counts, latest-commit times, and quantitative reliability were not recorded. Unverified metrics are not inferred.
- A main-branch README does not establish that every version supports a capability. Check the specific release again before installation.
- A readable page shows only that the source was accessible at review time—not software security, service availability, or future link stability.
- Adding product and paper directories does not mean the source projects were tested again or that research systems are automatically publicly available products.
- Update an entry's sources and review date together. Reviewing only part of the list should not refresh the review date for the whole list.
- The maintainer has not selected a content license for this repository. No `LICENSE` file was added during this work.
