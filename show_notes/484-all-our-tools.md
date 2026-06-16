# #484: All our tools

**Show Intro**

Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- Six Feet Up is hosting a LinkedIn Live
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Calvin: [@calvinhp@sixfeetup.social](https://sixfeetup.social/@calvin) / [@calvinhp.com](https://bsky.app/profile/calvinhp.com) (bsky)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Tuesday** at 7am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Calvin #1: [pi](https://pi.dev/) + [superpowers](https://github.com/obra/superpowers/tree/main)**

- terminal-first, open-source coding agent
- Session management is a first-class citizen
- Extension model is what makes pi special — it's aggressively composable
- Superpowers brings a structured software development methodology as loadable skills
- Steps back and asks you what you're really trying to do
- “hand you the keys to the car” mode vs guardrails might not be for everyone

**Michael #2: Terminal: [Warp.dev](http://Warp.dev) + [OhMyZSH](https://ohmyz.sh/)**

- If you’re using the base terminal with default settings, you have so much head-room for improvement.
- I’ve been using [Warp.dev](http://Warp.dev) since Elvis talked me into it. ;)
- Remarkable terminal but the AI side of things is a bit junky, can be turned off
- OhMyZSH gives better autocomplete
  - e.g. git branch <TAB> lists all branches in the local repo!
- [Commandbookapp.com](http://Commandbookapp.com) is excellent to keep the terminal focused on terminal things and more server commands and other automation in Command Book.

**Calvin #3: {[Blink](https://blink.sh/),[kitty](https://sw.kovidgoyal.net/kitty/)} + [mosh](https://mosh.org/) + [tmux](https://github.com/tmux/tmux)**

- [**Kitty Terminal**](https://sw.kovidgoyal.net/kitty/) — GPU-accelerated terminal emulator for macOS, Linux, and Windows with support for graphics, ligatures, and a powerful tiling layout system built right in.
- [**Blink Shell**](https://blink.sh/) — The go-to terminal for iPad/iPhone power users; full SSH and Mosh client with a gorgeous interface built specifically for mobile professional workflows.
- [**Mosh**](https://mosh.org/) — Mobile Shell replaces SSH for remote connections, surviving network switches, sleep cycles, and flaky Wi-Fi with zero dropped sessions — essential for staying connected to long-running agentic jobs.
- [**tmux**](https://github.com/tmux/tmux) — Terminal multiplexer that keeps sessions alive on your Linux server indefinitely; detach from a Mosh session on your Mac, reconnect from your iPad, and your agent is right where you left it.
- **The combo** — Kitty or Blink + Mosh + tmux creates a "persistent remote brain" pattern: your beefy Linux homelab runs the compute-heavy agent sessions 24/7, and any device becomes a thin client to drop in and out at will.

**Michael #4: [Claude code](https://www.anthropic.com/product/claude-code)**

- I prefer the IDE experience, the new PyCharm + Claude integration is really good. VS Code too. Why IDE? Because we should still be present with our code and managing context is much easier.
- Use the best/latest models on high thinking. “Speed” is not your friend, it’s just shortcuts.
- Create skills and agents and use them.
- Curate your own rules (e.g. Talk Python’s [Claude.md](http://Claude.md))
- Works well on non-coding things. Just create a folder, put a ton of files in there and it’s like NotebookLM + Chat + more.

**Calvin #5: [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) or [Handy](https://handy.computer)**

- Transcribes your speech using your choice of Whisper or Parakeet models.
- All transcription is done on your device, **no data leaves your machine.**
- Automatic Speaker Recognition with local models.
- Handy is more basic, but open source and runs on all platforms.

**Michael #6: [Tailscale](https://tailscale.com/)**

- No need to open ports at all, Tailscale makes machines inside the same network accessible to each other
- Works great for laptops, desktops, etc. But also available for servers.
  - Though I still use cloud firewalls for servers.
- **How I use it**:
  - **My dev database server**, preloaded with QA data, is always running on my home mac mini m4 pro. All my apps look for that server before looking locally and tailscale makes them always accessible to each other
  - My **local LLMs expose OpenAI API compatible APIs**. Tailscale makes these accessible even while traveling or at a coffee shop.
  - Use my **mini as an exit node**. All traffic is routed outbound from my local fiber network. Great to restricted IPs like accessing my servers without caring about the local IP.
  - Screen share back to my home machines even while traveling.
- Listen to the [Talk Python episode with Alex](https://talkpython.fm/episodes/show/546/self-hosting-apps-for-python-people) for a deeper conversation.

**Extras**

Calvin:
- [Telescopo](https://www.telescopo.app) great Mac Markdown viewer/editor.
Michael:
- One more: [Typora markdown](https://typora.io/) editor.
- Created [formal documentation for many of my open source packages](https://mkennedy.codes/docs/) using [Great Docs](https://posit-dev.github.io/great-docs/).
- Via Mark Little: [Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

**Joke: [No second date](https://x.com/pr0grammerhum0r/status/2063078450311598430?s=12)**

Links

- [@calvinhp@sixfeetup.social](https://sixfeetup.social/@calvin)
- [@calvinhp.com](https://bsky.app/profile/calvinhp.com)
- [calvinhp.com](https://calvinhp.com)
- [pi](https://pi.dev/)
- [superpowers](https://github.com/obra/superpowers/tree/main)
- [Warp.dev](http://Warp.dev)
- [OhMyZSH](https://ohmyz.sh/)
- [Commandbookapp.com](http://Commandbookapp.com)
- [Blink](https://blink.sh/)
- [kitty](https://sw.kovidgoyal.net/kitty/)
- [mosh](https://mosh.org/)
- [tmux](https://github.com/tmux/tmux)
- [Claude code](https://www.anthropic.com/product/claude-code)
- [Claude.md](http://Claude.md)
- [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper)
- [Handy](https://handy.computer)
- [Tailscale](https://tailscale.com/)
- [Talk Python episode with Alex](https://talkpython.fm/episodes/show/546/self-hosting-apps-for-python-people)
- [Telescopo](https://www.telescopo.app)
- [Typora markdown](https://typora.io/)
- [formal documentation for many of my open source packages](https://mkennedy.codes/docs/)
- [Great Docs](https://posit-dev.github.io/great-docs/)
- [Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)
- [No second date](https://x.com/pr0grammerhum0r/status/2063078450311598430?s=12)
