# #487: Minimum requirements

Show Intro

Sponsored by us! Support our work through:
- Our [**courses at Talk Python**](https://training.talkpython.fm/)
- Consulting from [**Six Feet Up**](https://sixfeetup.com/)

**Connect with the hosts**
- Michael: [Mastodon](https://fosstodon.org/@mkennedy) / [BlueSky](https://bsky.app/profile/mkennedy.codes) / [X](https://x.com/mkennedy) / [LinkedIn](https://www.linkedin.com/in/mkennedy/)
- Calvin: [Mastodon](https://sixfeetup.social/@calvin) / [BlueSky](https://bsky.app/profile/calvinhp.com) / [X](https://x.com/calvinhp) / [LinkedIn](https://www.linkedin.com/in/calvinhp/)
- Show: [Mastodon](https://fosstodon.org/@pythonbytes) / [BlueSky](https://bsky.app/profile/pythonbytes.fm) / [X](https://x.com/PythonBytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Tuesday at 7am PT**. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1: [dust](https://github.com/bootandy/dust) -** a better du

- `du` + Rust = `dust` - a fast, visual, intuitive disk-usage CLI
- Run `dust` and immediately see the biggest directories and files without piping through `sort`, `head`, or `awk`
- Smart recursive output focuses on what matters instead of dumping every folder
- Colored bars show relative size and parent/child hierarchy, making “where did the space go?” obvious
- Perfect for Python projects bloated by `.venv`, caches, Docker volumes, downloaded datasets, and local AI models
- Install via `brew`, `cargo install du-dust`, `conda-forge`, Scoop, Snap, deb-get, or GitHub releases

**Calvin #2**: [A Way better ARchive format for Python packaging](https://github.com/astral-sh/war/blob/main/SPEC.md)

- **war** - new archive format spec from Astral (same team as uv/ruff), v0.0.2, still no binary encoding defined yet
- Header-Index-Store layout: header IDs the file, index maps names to store offsets, store holds compressed data
- Index uses a finite-state transducer (FST) to dedupe common path prefixes across entry names
- Supports three entry types (file, directory, link) and three compression modes (store/DEFLATE/zstd), plus an "executable" metadata flag
- Unpacking is atomic - writes to a temp dir, then renames into place, so a failed extract never leaves a half-unpacked directory
- Strict name-segment rules (no NUL/control chars, no leading/trailing whitespace, blocks Windows-reserved names like CON/PRN) to avoid path traversal and cross-platform footguns

**Michael #3:** [Hermes Agent](https://hermes-agent.org/): The AI agent that grows with you

- Hermes Agent is an open-source, Python-built AI agent framework from Nous Research - think ChatGPT-style assistant, but connected to your tools, files, shell, browser, calendar, memory, and messaging apps
- I’m using it in Discord as a long-running agent conversation, not just a one-off chatbot session
- Hermes can connect through a gateway to platforms like Discord, Telegram, Slack, WhatsApp, email, webhooks, and more - so the same assistant can follow you across surfaces
- In my setup, I can send Hermes voice/text from Discord, keep project context across turns as threads, and ask it to actually do things: read GitHub repos, run commands, edit files, schedule calendar events, generate drafts, and verify results
- A fun workflow: I can trigger one-shot actions from an Apple Watch shortcut - dictate a request, send it to Hermes, and have the agent execute it asynchronously
- Hermes has persistent memory, so it can remember durable preferences and facts - for example, how I like my research formatted
- It also has “skills,” which are reusable procedures the agent can load later, so Hermes can self-improve over time instead of rediscovering the same workflow repeatedly
- It supports scheduled jobs / cron-style automations, so it can proactively watch for releases, send summaries, run checks, or remind you about things
- It’s provider-agnostic: OpenRouter, Anthropic, Google, xAI, local models, Nous Portal, and others
- The big idea: Hermes turns an LLM from “a chat box I visit” into “an agent I can reach from anywhere that knows my workflows and can take real actions and learns over time.”

**Calvin #4: [llm-coding-agent 0.1a0](https://github.com/simonw/llm-coding-agent/releases/tag/0.1a0)**

- Simon Willison built a Claude/Codex-style coding agent on top of his `llm` library, using an alpha of the `llm` package plus his python-lib-template-repo
- Built almost entirely via prompted TDD - asked an agent to write a [spec.md](http://spec.md), then commit + implement with red/green tests, occasionally hitting a real OpenAI key to sanity-check
- Shipped to PyPI as an alpha: `uvx --prerelease=allow --with llm-coding-agent llm code`
- Tool set mirrors familiar coding-agent primitives: read_file, edit_file (exact string replace + diff), write_file, list_files, search_files, execute_command
- Also exposes a Python API - `CodingAgent(model="gpt-5.5", root=..., approve=True).run(...)` - which Simon didn't ask for but got anyway
- Demo: `llm code --yolo` told GPT-5.5 to build a SwiftUI CLI clock; model correctly noted SwiftUI isn't really CLI-friendly and still produced an ASCII-art time display

**Extras**

Calvin:
- Slides, but for developers https://sli.dev/
- Wanna reduce your token usage…. only issue is that its lossy https://github.com/teamchong/pxpipe
- **PEP 772 - Python Packaging Council inaugural election dates set, nominations open July 28, voting September 1-15**

Michael:
- [What the pls?](https://mkennedy.codes/posts/what-the-pls/) revisited!

**Joke:** [Min requirements for Linux](https://x.com/AlfinCodes/status/2057443209127903456)

Links

- [dust](https://github.com/bootandy/dust)
- [A Way better ARchive format for Python packaging](https://github.com/astral-sh/war/blob/main/SPEC.md)
- [Hermes Agent](https://hermes-agent.org/)
- [llm-coding-agent 0.1a0](https://github.com/simonw/llm-coding-agent/releases/tag/0.1a0)
- [spec.md](http://spec.md)
- [What the pls](https://mkennedy.codes/posts/what-the-pls/)
- [sli.dev](https://sli.dev/)
- [github.com/teamchong/pxpipe](https://github.com/teamchong/pxpipe)
- [Min requirements for Linux](https://x.com/AlfinCodes/status/2057443209127903456)
