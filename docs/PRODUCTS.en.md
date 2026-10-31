# Public commercial products

[中文](PRODUCTS.md) · [Main list](../README.en.md)

**Verified: 2026-10-31 (UTC).** This page covers **14 commercial / proprietary personal-agent products with official availability documentation**, including explicitly labeled regional rollouts, experimental features, and previews, plus **1 publicly described candidate, Instinct, whose self-service availability is unverified**. The candidate is excluded from the 14. Both groups complement—not replace—the open-source applications, runtimes, and frameworks in the main list. Order reflects usage patterns, not rankings.

## Reading this page

- **Evidence: official-documentation review.** Except for the separately labeled third-party research note, capabilities and safeguards below are vendor descriptions, **not repository test results**. We did not install products, sign in, purchase plans, or perform external actions.
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
| [Town](#town) | Persistent assistant across email, calendars, and messages | Individual free / paid plans; check permissions and regional access |
| [Grok Bot](#grok-bot) | Remembering Bots and a persistent cloud computer | Available on eligible paid plans; one user’s Bots share a computer |
| [Poke](#poke) | Messaging-based personal assistance and everyday tasks | Available; Poke Human is a human service with separate plan requirements |
| [Alexa+](#alexa) | Household voice, schedules, devices, services | Open in the US; stages and capabilities differ elsewhere |
| [Meta Muse](#muse) | Messaging, long-term goals, and cloud-computer execution | Rolling out in the US; not worldwide general availability |
| [Gemini Tasks](#gemini) | Google context, browsers, scheduled work | Available but experimental; substantial regional restrictions |
| [Copilot Cowork for personal accounts](#copilot) | Microsoft 365 files, email, calendars | **Preview**; US / Canada, Premium / Pro |

**Separate candidate: publicly described, self-service availability unverified (1 entry, excluded from the table above).**

| Candidate | Main interaction / output | Verification boundary |
| --- | --- | --- |
| [Instinct](#instinct) | Life administration through messages / calls | Public site; current signup, regions, native apps, and plans unverified |

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

<a id="town"></a>
### Town — Cross-channel memory and personal work assistance

- **Access / gates:** Individual free and paid plans; web, iOS, macOS, email, Slack, texting, WhatsApp, and Telegram. iOS is generally available. Complete regional/phone-number coverage was not verified; messaging support does not establish a native Android app. [Plans](https://www.town.com/pricing) · [Current channels](https://www.town.com/docs/getting-started/reaching-your-townie) · [iOS status](https://www.town.com/docs/using-town/ios)
- **Tasks / models:** Inbox handling, reply drafts, scheduling, meeting preparation, and background routines for personal work. Third-party providers and routing, not one fixed model. [Documentation](https://www.town.com/docs) · [Providers](https://www.town.com/ai-model-providers)
- **Memory / data:** Editable preferences and people notes, with global and routine-specific memories. Connected work and personal accounts contribute context; separate mailboxes are not isolation boundaries. The vendor states training is off by default, Google data is excluded, and hosting is in the US. [Memory](https://www.town.com/docs/features/context-and-memory) · [Data](https://www.town.com/trust)
- **Approvals / limits:** Threads offer Auto, Balanced, and Strict; the documentation says Strict asks before sending, changing, or sharing. Routines and per-tool permissions are configured separately; Auto / Always allow can remove prompts. Do not read the Trust page's shorthand as universal per-action human approval. [Permission modes](https://www.town.com/docs/safety/modes-approvals)

**Suggested first test—not performed:** Prepare a briefing from fictional schedules and preferences, inspect the saved memory, use a Strict thread, leave routines disabled, and make no external changes.

<a id="grok-bot"></a>
### Grok Bot — Persistent cloud computer and durable role memory

- **Access / gates:** macOS, Windows, Linux, iOS, and Android on eligible paid plans, including X Subscription Premium/Super/Ultra and documented legacy Cursor or linked-subscription paths. **Distinct from the ordinary Grok chat app** and Grok Build. [Setup/plans](https://docs.x.ai/grok-bot/get-started) · [App distinction/billing](https://docs.x.ai/grok-bot/faq)
- **Tasks / models:** Research, expense/receipt work, daily work digests, cross-app execution, and routines; cloud work can continue with your laptop closed. Backend model routing is task-dependent, not necessarily a Grok model every time. [Use cases](https://docs.x.ai/grok-bot/use-cases) · [Runtime](https://docs.x.ai/grok-bot/overview) · [Model FAQ](https://docs.x.ai/grok-bot/faq)
- **Memory / data:** Preferences, facts, and work summaries can be queried, corrected, or removed through chat; some personal facts are shared across Bots. All Bots use the user's shared files, browser, and logins: **separate Bots are not security boundaries**. Deleting a Bot does not clean the shared computer. [Memory/deletion](https://docs.x.ai/grok-bot/bots) · [Computer boundary](https://docs.x.ai/grok-bot/overview)
- **Approvals / privacy:** Auto Review can allow actions without human prompts; Ask first rules, review settings, and authorization matter. Saved Vault payment cards can fill checkout without separate approval each time. Cloud storage is required, and training choices follow applicable Cursor account settings—not an all-local or zero-retention guarantee. [Security/data](https://docs.x.ai/grok-bot/approvals-security-and-privacy)
- **Regions:** Complete product coverage remains unverified. The separate X `@bot` handoff excludes X accounts based in Australia, the UK, the EU, Iceland, Liechtenstein, and Norway; that is not the entire app's region list. [X tagging](https://docs.x.ai/grok-bot/tag-on-x)

**Suggested first test—not performed:** Summarize public sources, save a harmless formatting preference, check its reuse, then request removal; connect no private accounts.

<a id="poke"></a>
### Poke — messaging-based personal assistance and everyday tasks

- **Access:** Public signup, with Messages, WhatsApp, and Telegram interfaces; Free, Pro, and Ultra plans. Complete regional / phone-number coverage remains unconfirmed. [Product and signup](https://poke.com/) · [Plans](https://poke.com/pricing)
- **Tasks / models:** Reminders, proactive updates, email / calendars, recipe automations. Gmail / Outlook are supported; iCloud / Yahoo plans are not current support. Models vary by plan; a fixed underlying model was not verified. [FAQ](https://poke.com/faq)
- **Human boundary:** **Poke Human uses real people, not autonomous AI alone.** The FAQ includes it with Ultra for calls, bookings, and other tasks; real-world expenses separately consume credits. Operators reportedly see necessary task details, not chat history, memories, or integrations. [Human service](https://poke.com/faq)
- **Data / permissions:** Mail connections expose private content. Current policy allows model training except for users selecting Maximum Privacy. A restricted operator view does not mean the service avoids processing private data. [Privacy policy](https://poke.com/privacy)

**Suggested first test—not performed:** Create and cancel a test reminder by message; avoid private email connections, human operators, purchases, and external sending.

<a id="alexa"></a>
### Alexa+ — household voice and services

- **Access:** Open to US customers through compatible devices, Alexa app, and web. Full Prime benefits differ from limited free chat; do not export US terms to other regions. [US access and plans](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)
- **Tasks / models:** Family calendars, smart homes, shopping, supported services. Amazon identifies Nova and Anthropic models, without one fixed version commitment.
- **Regions / stage:** Japan entered Early Access on 2026-10-29 and requires requesting access. Restaurant bookings and food delivery remain future plans there. Check each country's stage and features. [International / Japan update](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)
- **Data / permissions:** Household preferences, voice, shared material, and connected services supply context. The privacy dashboard manages interactions, attachments, and recording retention. Check which household members can use purchases, calendars, and devices. [Privacy section](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)

**Suggested first test—not performed:** In a supported region, add and remove a nonsensitive test reminder before enabling purchasing or lock control.

## Regional rollout—not worldwide availability

<a id="muse"></a>
### Meta Muse — long-term goals and a messaging-based cloud agent

- **Stage / access:** Officially **rolling out in the US** on iOS, Android, and web; the current site also lists WhatsApp and Mac. Free capabilities and subscriptions coexist. “Built for everyone” does not establish worldwide or universal account access. [Launch / regions](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [Current product](https://muse.ai/)
- **Tasks / models:** Email, calendars, reservations, shopping, ongoing goals, using a dedicated cloud VM / browser and the named Muse Spark model. The product is not thereby open source or locally inferred.
- **Approvals / data:** Users control connections; sensitive sending and purchases need approval. Sentinel governs connectors and network egress, but low-risk or previously authorized actions need not prompt every time. Audit trails and revocation are available. [Safety architecture](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)
- **Limits:** Meta states VM data is not shared with its ad systems; training requires a separate opt-out. Secure VM does not technically prevent Meta access. Reviewed sources still describe Confidential VM, AI glasses, Shop Pay, and 1Password as future features. [Safety / data](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) · [Announcement](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)

**Suggested first test—not performed:** On an enabled account, organize public material into a plan and inspect task records and stopping; avoid email connections, purchases, and messaging others.

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

## Publicly described, self-service availability unverified

This separate group contains 1 candidate, not a confirmed public-signup offering.

<a id="instinct"></a>
### Instinct — Life administration through messages and calls

- **Stage / entry:** The public site describes texting/calling an assistant. Try resolved to a login page; no login was attempted. Current invitations, regions, native-app availability, exact messaging channels, and free/paid pricing remain unverified. Terms require 18+; their paid-service section is not a verified current plan. [Home](https://instinct.com/) · [Entry](https://app.instinct.com/login) · [Terms](https://instinct.com/terms)
- **Tasks / models:** Vendor examples include train bookings, groceries, flowers, and finding a court, using a phone and computer. These are claims, not repository tests. Fixed models, completion reliability, and internal memory architecture were not verified. [Product](https://instinct.com/)
- **Context / data:** The policy describes personalization using provided/connected data. Training use is permitted; opt-out is prospective with a safety-review exception, while Google Workspace API data and, separately in the terms, Vault materials have no-training commitments. Disconnecting does not automatically remove indexed data. [Privacy](https://instinct.com/privacy-policy) · [Vault terms](https://instinct.com/terms)
- **Approvals / limits:** Terms do not guarantee safeguards prevent mistaken actions. No verified universal confirmation rule for purchases or external messages was found; third-party demos and anecdotes cannot supply that guarantee. [Terms](https://instinct.com/terms)

**Suggested first test—not performed:** Only with confirmed access, research public travel options without booking, paying, or contacting anyone; first inspect access, memory controls, and approval settings.

**Third-party research note—not official documentation or our hands-on test:** Supermemory founder Dhravya Shah’s [September 20, 2026 black-box teardown](https://supermemory.ai/blog/reverse-engineering-instinct-memory/) reports keyword hits, some paraphrase / typo misses, and one roughly 23-hour-16-minute write delay that motivated a daily-batch hypothesis. The author had no source access and operates a memory product. These are historical observations and hypotheses, not proof of current retrieval, a fixed write schedule, complete architecture, deletion guarantees, or self-service availability.

## Six checks beyond “can it do this?”

1. **Actual access:** Opening a website, downloading an app, subscribing, and having a particular agent feature enabled are four separate checks.
2. **Completion:** A plan or “done” message is not proof. Open outputs and verify sources or changes in the target system.
3. **Permissions and memory:** Record reading, writing, sending, purchasing, background execution, retention, and team sharing separately.
4. **Local versus cloud:** Distinguish execution, inference, uploads, cookies, third-party models, and logs. A local client is not an all-local system.
5. **Failure and exit:** Test stop, denial, takeover, schedule cancellation, and connection revocation. Check whether queued work remains after stopping.
6. **Real cost:** Record plan, credits, model, duration, interventions, and outputs. One demonstration is not a success rate.

Contributions should include a verification date and official sources. Claims of hands-on testing additionally need task inputs, environment / versions, account region and plan, permissions, process records, and verifiable results. Never submit credentials or private account data.
