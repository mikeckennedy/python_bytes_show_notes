# 473: A clean room rewrite?

## Show Intro

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

## **Michael #1: chardet ,AI, and licensing**

- Thanks Ian Lessing
- Wow, where to start?
- A bit of [legal precedence research](https://blobs.pythonbytes.fm/chardet-precedence-2026.html?cache_id=7ccbb8).
- [Chardet dispute shows how AI will kill software licensing, argues Bruce Perens](https://www.theregister.com/2026/03/06/ai_kills_software_licensing/) on the Register
- Also see [this GitHub issue](https://github.com/chardet/chardet/issues/331).
- Dan Blanchard, **maintainer** of a Python character encoding detection library called chardet, released a new version of the library under a new software license. (LGPL → MIT)
- Dan is allowed to make this change because v7 is a complete “clean room” rewrite using AI
- BTW, v7 is WAY better:
    - The result is a 48x increase in detection speed for a project that lives in the hot loops of many projects. That will lead to noticeable performance increases for literally millions of users (the package gets ~130M downloads per month).
    - It paves a path towards inclusion in the standard library (assuming they don’t institute policies against using AI tools).
    - Thread-safe detect() and detect_all() with no measurable overhead; scales on free-threaded Python 3.13t+
- An individual claiming to be Mark Pilgrim, the original creator of the library, opened an issue in the project's GitHub repo arguing that Blanchard had no right to change the software license, citing the LPGL requirement that the license remain unchanged.
- A 'complete rewrite' is irrelevant, since they had ample exposure to the originally licensed code (i.e. this is not a 'clean room' implementation).
- Blanchard disagreed, [citing](https://github.com/chardet/chardet/issues/327#issuecomment-4005195078) how version 7.0.0 and 6.0.0 compare when subjected to [JPlag](https://github.com/jplag/JPlag), a library for detecting plagiarism.
- Blanchard told The Register he had wanted to get chardet added to the Python standard library for more than a decade since it’s a core dependency to most Python projects.

## **Brian #2: [refined-github](https://github.com/refined-github/refined-github)**

- Suggested by Matthias Schöttle
- A browser plugin that improves the GitHub experience
- A sampling
    - Adds a build/CI status icon next to the repo’s name.
    - Adds a link back to the PR that ran the workflow.
    - Enables tab and shift tab for indentation in comment fields.
    - Auto-resizes comment fields to fit their content and no longer show scroll bars.
    - Highlights the most useful comment in issues.
    - Changes the default sort order of issues/PRs to Recently updated.
- But really, it’s a huge list of improvements

## **Michael #3: pgdog: PostgreSQL connection pooler, load balancer and database sharder**

- PgDog is a proxy for scaling PostgreSQL.
- It supports connection pooling, load balancing queries and sharding entire databases.
- Written in Rust, PgDog is fast, secure and can manage thousands of connections on commodity hardware.
- Features
    - PgDog is an application layer load balancer for PostgreSQL
    - Health Checks: PgDog maintains a real-time list of healthy hosts. When a database fails a health check, it's removed from the active rotation and queries are re-routed to other replicas
    - Single Endpoint: PgDog can detect writes (e.g. INSERT, UPDATE, CREATE TABLE, etc.) and send them to the primary, leaving the replicas to serve reads
    - Failover: PgDog monitors Postgres replication state and can automatically redirect writes to a different database if a replica is promoted
    - Sharding: PgDog is able to manage databases with multiple shards

## **Brian #4: [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)**

- Simon Willison
- So much great stuff here, especially
    - [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
    - And 3 sections on testing
        - [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
        - [First run the test](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)
        - [Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)

## **Extras**

Brian:
- [`uv python upgrade`](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions)  will upgrade all versions of Python installed with uv to latest patch release
    - suggested by John Hagen
- [Coding After Coders: The End of Computer Programming as We Know It](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=nytcore-ios-share)
    - NY Times Article
    - [Suggested by Christopher](https://oldbytes.space/@feoh/116223895301033633)
    - Best quote: “Pushing code that fails pytest is unacceptable and embarrassing.”

Michael:
- Talk Python Training users get [a better account dashboard](https://training.talkpython.fm/account/)
- [Package Managers Need to Cool Down](https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html?utm_source=tldrnewsletter)
- [Will AI Kill Open Source](https://mkennedy.codes/posts/will-ai-kill-open-source/), article + video
- My [Always activate the venv](https://mkennedy.codes/posts/always-activate-the-venv-a-shell-script/) is [now a zsh-plugin](https://www.linkedin.com/feed/update/urn:li:activity:7432574562208227328/), sorta.

## **Joke: [Ergonomic keyboard](https://x.com/mattrothenberg/status/2031383560062370235)**

![](https://blobs.pythonbytes.fm/keyboard-joke.jpeg?cache_id=a6026b)
Also pretty good and related:
- [`Claude Code Mandated`](https://hachyderm.io/@prcutler/116238970854696785)
    ![claude-mandated.png](473/claude-mandated.png)

## Links

- [legal precedence research](https://blobs.pythonbytes.fm/chardet-precedence-2026.html?cache_id=7ccbb8)
- [Chardet dispute shows how AI will kill software licensing, argues Bruce Perens](https://www.theregister.com/2026/03/06/ai_kills_software_licensing/)
- [this GitHub issue](https://github.com/chardet/chardet/issues/331)
- [citing](https://github.com/chardet/chardet/issues/327#issuecomment-4005195078)
- [JPlag](https://github.com/jplag/JPlag)
- [refined-github](https://github.com/refined-github/refined-github)
- [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
- [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
- [First run the test](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)
- [Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)
- [`uv python upgrade`](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions)
- [Coding After Coders: The End of Computer Programming as We Know It](https://www.nytimes.com/2026/03/12/magazine/ai-coding-programming-jobs-claude-chatgpt.html?smid=nytcore-ios-share)
- [Suggested by Christopher](https://oldbytes.space/@feoh/116223895301033633)
- [a better account dashboard](https://training.talkpython.fm/account/)
- [Package Managers Need to Cool Down](https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html?utm_source=tldrnewsletter)
- [Will AI Kill Open Source](https://mkennedy.codes/posts/will-ai-kill-open-source/)
- [Always activate the venv](https://mkennedy.codes/posts/always-activate-the-venv-a-shell-script/)
- [now a zsh-plugin](https://www.linkedin.com/feed/update/urn:li:activity:7432574562208227328/)
- [Ergonomic keyboard](https://x.com/mattrothenberg/status/2031383560062370235)
- [`Claude Code Mandated`](https://hachyderm.io/@prcutler/116238970854696785)
- [claude-mandated.png](https://473/claude-mandated.png)
- [blobs.pythonbytes.fm/keyboard-joke.jpeg?cache_id=a6026b](https://blobs.pythonbytes.fm/keyboard-joke.jpeg?cache_id=a6026b)
