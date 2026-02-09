# #469: Commands, out of the terminal!

## Show intro

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 10am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

## **Michael #1: [Command Book App](https://commandbookapp.com)**

- New app from Michael
- Command Book App is a native macOS app for developers, data scientists, AI enthusiasts and more.
- This is a tool I've been using lately to help build Talk Python, Python Bytes, Talk Python Training, and many more applications.
- It's a bit like advanced terminal commands or complex shell aliases, but hosted outside of your terminal. This leaves the terminal there for interactive commands, exploration, short actions.
- Command Book manages commands like "tail this log while I'm developing the app", "Run the dev web server with true auto-reload", and even "Run MongoDB in Docker with exactly the settings I need"
- I'd love it if you gave it a look, shared it with your team, and send me feedback.
- Has a free version and paid version.
- Build with Swift and [Swift UI](https://developer.apple.com/swiftui/)
- Check it out at https://commandbookapp.com

## **Brian #2: [uvx.sh: Install Python tools without uv or Python](https://pydevtools.com/blog/uvx-sh-install-python-tools-without-uv-or-python/)**

- Tim Hopper

## **Michael #3: [Ending 15 years of subprocess polling](https://gmpy.dev/blog/2026/event-driven-process-waiting)**

- by Giampaolo Rodola
- The standard library's `subprocess` module has relied on a busy-loop polling approach since the *timeout* parameter was added to [Popen.wait()](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait) in Python 3.3, around 15 years ago
- The problem with busy-polling
  - CPU wake-ups: even with exponential backoff (starting at 0.1ms, capping at 40ms), the system constantly wakes up to check process status, wasting CPU cycles and draining batteries.
  - Latency: there's always a gap between when a process actually terminates and when you detect it.
  - Scalability: monitoring many processes simultaneously magnifies all of the above.
  - **+** L1/L2 CPU cache invalidations
- It’s interesting to note that waiting via `poll()` (or `kqueue()`) puts the process into the exact same sleeping state as a plain `time.sleep()` call. From the kernel's perspective, both are interruptible sleeps.
- Here is [the merged PR](https://github.com/python/cpython/pull/144047) for this change.

## **Brian #4:** monty: A minimal, secure Python interpreter written in Rust for use by AI

- Samuel Colvin and others at Pydantic
- Still experimental
- “Monty avoids the cost, latency, complexity and general faff of using a full container based sandbox for running LLM generated code. “
- “Instead, it lets you safely run Python code written by an LLM embedded in your agent, with startup times measured in single digit microseconds not hundreds of milliseconds.”

## **Extras**

Brian:
- [Expertise is the art of ignoring](https://www.loopwerk.io/articles/2026/expertise/) - Kevin Renskers
  - You don’t need to master the language. You need to master your slice.
  - Learning everything up front is wasted effort.
  - Experience changes what you pay attention to.
- [I hate fish - Rands (Michael Lopp)](https://randsinrepose.com/archives/i-hate-fish/)
  - Really about productivity systems
  - And a nice process for dealing with email

Michael:
- [Talk Python now has a CLI](https://talkpython.fm/blog/posts/talk-python-now-has-a-cli/)
- New essay: [It's not vibe coding - Agentic engineering](https://mkennedy.codes/posts/its-not-vibe-coding-agentic-engineering/)
- GitHub is [having a day](https://blobs.pythonbytes.fm/github-having-a-day-2026-02-09.png?cache_id=c4353a)
- [Python 3.14.3 and 3.13.12 are available](https://pythoninsider.blogspot.com/2026/02/python-3143-and-31312-are-now-available.html)
- Wall Street just lost $285 billion [because of 13 markdown files](https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files)

## **Joke: [Silence, current side project!](https://devhumor.com/media/silence-curent-project)**

## Links

- [Command Book App](https://commandbookapp.com)
- [Swift UI](https://developer.apple.com/swiftui/)
- [uvx.sh: Install Python tools without uv or Python](https://pydevtools.com/blog/uvx-sh-install-python-tools-without-uv-or-python/)
- [uvx.sh](https://uvx.sh)
- [Popen.wait()](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait)
- [the merged PR](https://github.com/python/cpython/pull/144047)
- [Expertise is the art of ignoring](https://www.loopwerk.io/articles/2026/expertise/)
- [I hate fish - Rands (Michael Lopp)](https://randsinrepose.com/archives/i-hate-fish/)
- [Talk Python now has a CLI](https://talkpython.fm/blog/posts/talk-python-now-has-a-cli/)
- [Its not vibe coding - Agentic engineering](https://mkennedy.codes/posts/its-not-vibe-coding-agentic-engineering/)
- [having a day](https://blobs.pythonbytes.fm/github-having-a-day-2026-02-09.png?cache_id=c4353a)
- [Python 3.14.3 and 3.13.12 are available](https://pythoninsider.blogspot.com/2026/02/python-3143-and-31312-are-now-available.html)
- [because of 13 markdown files](https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files)
- [Silence, current side project](https://devhumor.com/media/silence-curent-project)
- [Ending 15 years of subprocess polling](https://gmpy.dev/blog/2026/event-driven-process-waiting)
