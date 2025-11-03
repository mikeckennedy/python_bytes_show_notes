# Python Bytes 450

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 10am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Brian #1: [pandas is getting `pd.col` expressions](https://labs.quansight.org/blog/pandas_expressions)**

- Marco Gorelli
- Next release of Pandas will have `pd.col()`, inspired by some of the other frameworks
  - I’m guessing Pandas 2.3.3? or 2.4.0? or 3.0.0? (depending on which version they bump?)
- “The output of `pd.col` is called an *expression*. You can think of it as a delayed column - it only produces a result once it's evaluated inside a dataframe context.”
- It replaces many contexts where lambda expressions were used

**Michael #2: [Cline, At-Cost Agentic IDE Tooling](https://cline.bot)**

- Free and [open-source](https://github.com/cline/cline)
- Probably supports your IDE (if your IDE isn’t a terminal)
  - VS Code
  - VS Code Insiders
  - Cursor
  - Windsurf
  - JetBrains IDEs (including PyCharm)
- You pick plan or act (very important)
- It shows you the price as the AI works, per request, right in the UI

**Brian #3: [uv cheatsheet](https://mathspp.com/blog/uv-cheatsheet)**

- Rodgrigo at [mathspp.com](http://mathspp.com)
- Nice compact cheat sheet of commands for
  - Creating projects
  - Managing dependencies
  - Lifecycle stuff like build, publish, bumping version
  - uv tool (uvx) commands
  - working with scripts
  - Installing and updating Python versions
  - plus venv, pip, format, help and update

**Michael #4:** [Ducky Network UI](https://github.com/thecmdguy/Ducky)

- Ducky is a powerful, open-source, all-in-one desktop application built with Python and PySide6.
- It is designed to be the perfect companion for network engineers, students, and tech enthusiasts, combining several essential utilities into a single, intuitive graphical interface.
- **Features**
  - **Multi-Protocol Terminal**: Connect via SSH, Telnet, and Serial (COM) in a modern, tabbed interface.
  - **SNMP Topology Mapper**: Automatically discover your network with a ping and SNMP sweep. See a graphical map of your devices, color-coded by type, and click to view detailed information.
  - **Network Diagnostics**: A full suite of tools including a Subnet Calculator, Network Monitor (Ping, Traceroute), and a multi-threaded Port Scanner.
  - **Security Toolkit**: Look up CVEs from the NIST database, check password strength, and calculate file hashes (MD5, SHA1, SHA256, SHA512).
  - **Rich-Text Notepad**: Keep notes and reminders in a dockable widget with formatting tools and auto-save.
  - **Customizable UI**: Switch between a sleek dark theme and a clean light theme. Customize terminal colors and fonts to your liking.

**Extras**

Brian:

- Where are the cool kids hosting static sites these days?
  - [Moving from Netlify to Cloudflare Pages](https://willvincent.com/2024/02/18/moving-from-netlify-to-cloudflare-pages/) - Will Vincent from Feb 2024
  - Traffic is a concern now for even low-ish traffic sites since so many bots are out there
  - Netlify free plan is less than 30 GB/mo allowed (grandfathered plans are 100 GB/mo)
  - GH Pages have a soft limit of 100 GB/mo
  - Cloudflare pages says unlimited

Michael:

- [PyCon Brazil](https://2025.pythonbrasil.org.br) needs some help with reduced funding from the PSF
  - Get a ticket to donate for a student to attend (at the button of the buy ticket checkout dialog)
- I upgraded to macOS Tahoe
  - Loving it so far.
  - Only issue I’ve seen so far has been with [alt-tab](https://github.com/lwouis/alt-tab-macos) for macOS

**Joke:** [Hiring in 2025 vs 2021](https://www.youtube.com/watch?v=4R4uTrA1vQ8)

- 2021:
  - “Do you have an in-house kombucha sommelier?”
  - “Let’s talk about pets, are you donkey-friendly?”, “Oh you think this is a joke?”
- 2025:
  - “Round 8/7”
  - “Out of 12,000 resumes, the AI picked yours”
  - “Binary tree? Build me a foundational model!”
  - “Healthcare? What, you want to live forever?”