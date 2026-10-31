# Public commercial products

[中文](PRODUCTS.md) · [Main list](../README.en.md)

**Verified: 2026-10-31 (UTC).** This page adds ready-to-use commercial / proprietary personal-agent products alongside, not instead of, the open-source applications, runtimes, and frameworks in the main list. Order reflects usage patterns, not rankings.

## Reading this page

- **Evidence: official-documentation review.** Capabilities and safeguards below are vendor descriptions, **not repository test results**. We did not install products, sign in, purchase plans, or perform external actions.
- **Available does not mean available to everyone.** Plans, rollouts, region, age, administrators, devices, and third-party services can restrict access. Experimental and preview features are explicitly marked, not presented as general availability.
- **Commercial does not imply open source; free of charge does not imply open source.** Entries describe complete products. Open models, public SDKs, or Chromium do not make the whole service open source. We do not claim these products have complete self-hostable source distributions.
- **“Regional coverage unconfirmed”** means the reviewed official sources did not establish a complete list, not that access is worldwide. A Chinese interface does not establish availability in mainland China.
- Prices and quotas are intentionally not frozen here: check current official plans and checkout. Product versions, orchestrators, subagent models, and image / voice models are different things.

## At a glance

| Product | Main interaction / output | Status / key requirement |
| --- | --- | --- |
| [ChatGPT Work](#chatgpt-work) | Multi-step tasks, files, cloud browsing | Available; eligible paid plans and workspace permissions |
| [Claude Cowork](#claude-cowork) | Documents, files, browsers, desktop tools | Available; some platforms / team experiences in beta |
| [Manus](#manus) | Cloud-computer tasks and deliverables | Available; credits and task permissions |
| [Genspark Super Agent](#genspark) | Deliverables, connected apps, phone calls | Available; calls need a paid plan, verification, and regional support |
| [Perplexity Computer](#perplexity-computer) | Background work, research, files, local extensions | Available; Brain memory remains a research preview |
| [Comet Assistant](#comet) | Tasks inside a signed-in browser | Available; browser downloads and agent quotas differ |
| [Lindy](#lindy) | Email, scheduling, and messaging-based assistance | Available; oriented toward personal work / teams |
| [Alexa+](#alexa) | Household voice, schedules, devices, services | Open in the US; stages and capabilities differ elsewhere |
| [Gemini Tasks](#gemini) | Google context, browsers, scheduled work | Available but experimental; substantial regional restrictions |
| [Copilot Cowork for personal accounts](#copilot) | Microsoft 365 files, email, calendars | **Preview**; US / Canada, Premium / Pro |

See the corresponding entries for supporting sources, platforms, and permission boundaries.

## Available products

<a id="chatgpt-work"></a>
### ChatGPT Work — general tasks and deliverables

- **Access:** Web, mobile, and eligible desktop accounts; paid-plan and workspace rules apply. Check [supported regions](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries).
- **Tasks / models:** Research, documents, spreadsheets, presentations, and other outputs. Model options depend on account settings; Work is not one model. [Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- **Data / permissions:** Cloud-browser cookies and logins are separate from the local browser. Website access and consequential-action approval are separate. Local execution does not guarantee local-only messages or task context. [Cloud browser](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
- **Limits:** Sites may block automation or require takeover. The old [ChatGPT agent page](https://help.openai.com/en/articles/11752874-chatgpt-agent) announces retirement in its Overview but retains older text; its old quotas are not reused here.

**Suggested first test—not performed:** Produce a sourced one-page comparison from three public documents, without signing in anywhere.

<a id="claude-cowork"></a>
### Claude Cowork — files and knowledge work

- **Access:** Paid plans; macOS, Windows, Linux beta, web, and mobile. Some Team experiences are beta; Enterprise requires administrator enablement. Check [supported regions](https://support.claude.com/en/articles/8461763-where-can-i-access-claude). [Getting started](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- **Tasks / models:** File organization, office documents, research, schedules, and browsing, using Claude. Check the account for model versions; this is not the developer computer-use API.
- **Data / permissions:** Current sessions run in the cloud. Desktop connections expose local resources; opened local files are processed on Anthropic servers. Isolation is not local-only processing. [Safety guidance](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- **Limits:** Direct computer-use clicks do not necessarily pass ordinary tool permission checks. Exclude sensitive folders. Continuing cloud work does not imply access to an offline computer.

**Suggested first test—not performed:** Propose organization for test files, then organize copies after approval; prohibit deleting originals.

<a id="manus"></a>
### Manus — cloud computers and deliverables

- **Access:** Web, macOS, Windows, iOS, Android; free / paid credit plans. Regional coverage unconfirmed. [Downloads](https://manus.im/download) · [Plans](https://manus.im/docs/introduction/plans)
- **Tasks / models:** Research, files, slides, and websites in a cloud sandbox; the 2.0 announcement also describes event automations. A product version is not a model version; the complete model-routing setup was not verified. [Execution environment](https://manus.im/docs/introduction/welcome) · [2.0 announcement](https://manus.im/blog/introducing-manus-2-0)
- **Data / permissions:** Browser Operator separately uses local signed-in sessions, with per-session authorization and an online desktop browser. Chrome / Edge are recommended. It differs from isolated cloud browsing. [Browser Operator](https://manus.im/docs/features/browser-operator)
- **Limits:** Website generation, paid Cloud Computers, browsing, and cloud research do not share one cost or permission boundary. “Autonomous” is not a reliability result.

**Suggested first test—not performed:** Research a public topic and deliver a downloadable document; verify sources, files, and credits consumed.

<a id="genspark"></a>
### Genspark Super Agent — deliverables and connected actions

- **Access:** Web; Super App on Apple Silicon macOS, Windows, and Linux. Free download does not mean free execution; plans and credits apply. Regional coverage unconfirmed. [Desktop app](https://www.genspark.ai/helpcenter/super-app)
- **Tasks / models:** Cloud sandbox, browser, files, research, spreadsheets, slides, reusable skills. Product orchestration selects tools / models; a fixed model for every step was not verified. [Super Agent](https://www.genspark.ai/helpcenter/super-agent)
- **Data / permissions:** Connected accounts can enable writes. OAuth scopes vary and can be fixed; selecting writable files does not necessarily restrict all reading to those files. [Connector permissions](https://www.genspark.ai/helpcenter/connectors-and-integrations)
- **Difference / limits:** Call For Me makes real calls and returns summaries; paid access, number verification, and supported destinations are required. Marketing, harassment, and concealed AI identity are prohibited. No calls were placed. [Calling documentation](https://www.genspark.ai/helpcenter/call-for-me)

**Suggested first test—not performed:** Generate a spreadsheet and explanation from sanitized data, without email connections, sending, or calls.

<a id="perplexity-computer"></a>
### Perplexity Computer — background work and desktop extensions

- **Access:** Computer for Pro / Max; Personal Computer has Mac and Windows access. Regional coverage unconfirmed. Earlier Windows waitlist descriptions are outdated. [Product](https://www.perplexity.ai/en-GB/products/computer) · [Windows launch](https://www.perplexity.ai/changelog/shared-workspaces-personal-computer-for-windows-and-model-council)
- **Tasks / models:** Research, files, apps, connected tools, and ongoing work; multi-model orchestration with supported model / effort options. Brain remains a research preview, not a universal default. [Runtime / model updates](https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace) · [Max and Brain](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)
- **Data / permissions:** Local extensions access connected folders, apps, and sessions. Mac setup includes accessibility, recording, and disk permissions. Standard cloud Computer is not all-local inference. [Local setup](https://www.perplexity.ai/personal-computer-setup)
- **Limits:** Personal, Hybrid, and Portable Computer have different hardware and data flows. Check their specific documentation; “Personal” is not a privacy guarantee.

**Suggested first test—not performed:** Summarize a dedicated test folder, list every file read, and prohibit modifications.

<a id="comet"></a>
### Comet Assistant — browser-based execution

- **Access:** macOS, Windows, iOS, Android. Regional coverage unconfirmed; platform feature parity is not assumed. [Platforms and download](https://www.perplexity.ai/comet)
- **Tasks / models:** Research and actions using tabs, webpages, and signed-in sessions. Browser installation and agent queries are separate; the current plan table excludes Browser Agent queries from Free. Models vary by mode / plan. [Plan comparison](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you) · [Max Assistant](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)
- **Data / permissions:** The vendor describes local credential storage, but relevant tab content and history can reach Perplexity. Site restrictions and an Assistant off switch are available. **Local credentials do not mean local-only page content.** [Privacy Snapshot](https://www.perplexity.ai/en-GB/hub/blog/introducing-privacy-snapshot)
- **Limits:** A browser agent is neither arbitrary mobile-app control nor the complete Computer environment above.

**Suggested first test—not performed:** Compare one metric across three public pages; verify citations without logins or form submissions.

<a id="lindy"></a>
### Lindy — email and scheduling assistance

- **Access:** Web, Slack, and phone messaging / voice entry points; trial credits and paid plans. Primarily personal work / teams. Complete messaging / calling regional support remains unconfirmed. [Assistant use cases](https://www.lindy.ai/hire/executive-assistant) · [Plans](https://www.lindy.ai/pricing)
- **Tasks / models:** Inbox work, scheduling, meeting preparation, recurring briefings. Plans describe per-task model choice; no fixed model version is asserted. [Product, memory, routines](https://www.lindy.ai/)
- **Data / permissions:** Connect email, calendars, and other tools. Lindy states permissions are revocable, actions logged, and customer data not used for model training by Lindy or providers. These are vendor statements, not our audit. [Security](https://www.lindy.ai/security)
- **Limits:** Account access is not blanket sending approval. Check drafts, autosending, invitations, and sharing; a shared workspace is not a private-memory vault.

**Suggested first test—not performed:** Create a briefing and drafts from a test mailbox; prohibit sending, archiving, and deletion.

<a id="alexa"></a>
### Alexa+ — household voice and services

- **Access:** Open to US customers through compatible devices, Alexa app, and web. Full Prime benefits differ from limited free chat; do not export US terms to other regions. [US access and plans](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)
- **Tasks / models:** Family calendars, smart homes, shopping, supported services. Amazon identifies Nova and Anthropic models, without one fixed version commitment.
- **Regions / stage:** Japan entered Early Access on 2026-10-29 and requires requesting access. Restaurant bookings and food delivery remain future plans there. Check each country's stage and features. [International / Japan update](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)
- **Data / permissions:** Household preferences, voice, shared material, and connected services supply context. The privacy dashboard manages interactions, attachments, and recording retention. Check which household members can use purchases, calendars, and devices. [Privacy section](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)

**Suggested first test—not performed:** In a supported region, add and remove a nonsensitive test reminder before enabling purchasing or lock control.

## Experimental and preview—not general availability

<a id="gemini"></a>
### Gemini Tasks — Google context and multi-step work

- **Stage / access:** Experimental; 18+, personal Google account, AI Pro / Ultra, Keep Activity and Personal Intelligence required. Web, mobile, Mac; not work / school accounts. Excludes EEA, Nigeria, Switzerland, and UK from supported regions. [Tasks and availability](https://support.google.com/gemini/answer/17094507?hl=en)
- **Tasks / models:** Inbox, files, browsing, schedules; check account model / thinking options. [Models](https://support.google.com/gemini/answer/18648722) · [Task schedules](https://support.google.com/gemini/answer/17094710)
- **Data / permissions:** Connected-app and signed-in context can be used. Manage local Chrome sessions and saved remote-browser data separately. Supervise sensitive actions; scheduling does not replace authorization.
- **Naming / limits:** The FAQ says Spark became Task. This is not the Google Tasks to-do app or a promise to control every Android app. [Task documentation](https://support.google.com/gemini/answer/17094507?hl=en)

**Suggested first test—not performed:** Schedule a public-page change check; verify notification and cancellation before using personal email.

<a id="copilot"></a>
### Microsoft Copilot Cowork for personal accounts — Microsoft 365 workflows

- **Stage / access:** **Preview**. The October 2026 plan table lists Premium / Pro in the US / Canada, excludes Personal / Family, and limits benefits to the subscription owner. [Plans and regions](https://support.microsoft.com/en-gb/microsoft-365-copilot/ai-credits-and-limits-for-microsoft-365-subscriptions)
- **Tasks / platforms:** Browser and Copilot desktop access; documents, Excel, PowerPoint, Outlook mail / calendars, OneDrive, schedules. Device / platform availability varies. [Personal-account setup](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork)
- **Models / data:** A fixed personal-Cowork model combination was not verified. Enterprise model or privacy claims must not be extrapolated. Connected files / accounts enable real writes; review or take over sensitive actions.
- **Naming / limits:** Copilot Tasks is migrating to Cowork. Work / school general availability does not mean personal-account general availability. [Migration](https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app)

**Suggested first test—not performed:** Summarize a test OneDrive file into a new copy; do not overwrite originals or send mail.

## Six checks beyond “can it do this?”

1. **Actual access:** Opening a website, downloading an app, subscribing, and having a particular agent feature enabled are four separate checks.
2. **Completion:** A plan or “done” message is not proof. Open outputs and verify sources or changes in the target system.
3. **Permissions and memory:** Record reading, writing, sending, purchasing, background execution, retention, and team sharing separately.
4. **Local versus cloud:** Distinguish execution, inference, uploads, cookies, third-party models, and logs. A local client is not an all-local system.
5. **Failure and exit:** Test stop, denial, takeover, schedule cancellation, and connection revocation. Check whether queued work remains after stopping.
6. **Real cost:** Record plan, credits, model, duration, interventions, and outputs. One demonstration is not a success rate.

Contributions should include a verification date and official sources. Claims of hands-on testing additionally need task inputs, environment / versions, account region and plan, permissions, process records, and verifiable results. Never submit credentials or private account data.
