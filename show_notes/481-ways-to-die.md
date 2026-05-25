# #481: Ways to die

## Show Intro

Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 11am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

## **Michael #1: [Dumb Ways for an Open Source Project to Die](https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html)**

- Core categories
  - **The maintainer left**
  - **The maintainer is still there**
  - **Sabotage and capture**
  - **The release pipeline broke**
  - **Force majeure**
  - **The world moved on**
  - **The project split**
  - 
- Examples
  - [Bulma](https://github.com/jgthms/bulma) PRs still from 2023, issues and PRs with no maintainer response for years, last release 1.5 years ago
  - [diskcache](https://github.com/grantjenks/python-diskcache) Similar, got hired by OpenAI, crickets after that

## **Brian #2: [How to create a pylock.toml lockfile](https://pydevtools.com/handbook/how-to/how-to-create-a-pylock-toml-lockfile/)**

- Tim Hopper
- Tim walks through using `uv`, `pip` and `pdm` to create `pylock.toml` files.
- Recommendation: use `uv export --format pylock.toml -o pylock.toml`
- He also has [How to install from a pylock.toml lockfile with pip](https://pydevtools.com/handbook/how-to/how-to-install-from-a-pylock-toml-lockfile-with-pip/) but the short version is:
  - use `-r` because tools treat it like a requirements file

## **Michael #3:** https://github.com/facebook/Lifeguard

- Lifeguard is a static analyzer to detect Lazy Imports incompatibilities and ease the adoption overhead for Lazy Imports in Python.
- I’m more excited about lazy imports after my [Cutting Python Web App Memory Over 31%](https://mkennedy.codes/posts/cutting-python-web-app-memory-over-31-percent/) experience
- Some Python patterns depend on imports executing immediately. For example:
  - **Module-level side effects** — a module that registers a handler or modifies global state at import time will behave differently if that import is deferred.
  - **The registry pattern** — a module that registers itself (e.g., adding to a global dict) when imported will silently fail to register under Lazy Imports.
  - **`sys.modules` manipulation** — code that reads or writes `sys.modules` assumes prior imports have already executed.
  - **Metaclasses and `__init_subclass__`** — class creation side effects may depend on imports being resolved.
- **Project Stage: Beta** Lifeguard is in active development. We are aiming to be ready for general use by the [Python 3.15 final release](https://peps.python.org/pep-0790/).

## **Brian #4: [Choosing a Python Logging Library in 2026](https://www.dash0.com/guides/python-logging-libraries)**

- Ayooluwa Isaiah
- " which libraries matter, how they compare, where they overlap with the standard module, and when each one makes sense.”
- The slant with this article is the need to log json output, which seems reasonable as things like API entry and exit point logging will include json.
- Covered libraries
  - standard library `logging` with a hat tip to [python-json-logger](https://nhairs.github.io/python-json-logger/latest/)
    - Same site has a [guide to setting up python-json-logger](https://www.dash0.com/guides/python-json-logger)
  - [structlog](https://www.structlog.org)
  - [Loguru](https://loguru.readthedocs.io)
  - [Logbook](https://logbook.readthedocs.io/en/stable/)
  - [picologging](https://microsoft.github.io/picologging/)
- Some benchmarks with structlog, stdlib+json, and Loguru, with structlog coming out faster
- I liked the Loguru example
  - I’m going to have to try `@logger.catch` and `logger.exception()` for easily logging exceptions and `serialize=True` to enable JSON output.

## **Extras**

Brian:
- [When Women Stopped Coding](https://www.npr.org/sections/money/2014/10/21/357629765/when-women-stopped-coding) - Planet Money segment , spotted on BlueSky from [Savannah Ostrowski](https://bsky.app/profile/savannah.dev/post/3mml3emj63k22)
- [Lean TDD](https://courses.pythontest.com/lean-tdd/) is now leaner
  - Still working on audio version, but some great changes in 0.7.1 version
    - Ch 6, **TDD Interpretations**, move ATDD and some of BDD to chapter
    - Ch 7, Change name to **TDD with Teams: BDD and ATDD**
    - Ch 9, **Lean TDD**, streamline steps and chapter
    - Ch 10, Change name to **Lean TDD with Teams: Lean ATDD**
    - Ch 11, **Lean** **TDD with AI**, Add short discussion about guardrails and security

Michael:
- New course: [Python Web Security: OWASP Top 10 with Agentic AI](https://training.talkpython.fm/courses/agentic-ai-python-security)
- All courses now with Spanish subtitles, [see announcement](https://talkpython.fm/blog/posts/spanish-subtitles-available-for-all-courses/)

## **Joke: [Stop texting me](https://x.com/pr0grammerhum0r/status/2057733228899823981?s=12)**

## Links

- [Dumb Ways for an Open Source Project to Die](https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html)
- [Bulma](https://github.com/jgthms/bulma)
- [diskcache](https://github.com/grantjenks/python-diskcache)
- [How to create a pylock.toml lockfile](https://pydevtools.com/handbook/how-to/how-to-create-a-pylock-toml-lockfile/)
- [How to install from a pylock.toml lockfile with pip](https://pydevtools.com/handbook/how-to/how-to-install-from-a-pylock-toml-lockfile-with-pip/)
- [Cutting Python Web App Memory Over 31%](https://mkennedy.codes/posts/cutting-python-web-app-memory-over-31-percent/)
- [Python 3.15 final release](https://peps.python.org/pep-0790/)
- [github.com/facebook/Lifeguard](https://github.com/facebook/Lifeguard)
- [Choosing a Python Logging Library in 2026](https://www.dash0.com/guides/python-logging-libraries)
- [python-json-logger](https://nhairs.github.io/python-json-logger/latest/)
- [guide to setting up python-json-logger](https://www.dash0.com/guides/python-json-logger)
- [structlog](https://www.structlog.org)
- [Loguru](https://loguru.readthedocs.io)
- [Logbook](https://logbook.readthedocs.io/en/stable/)
- [picologging](https://microsoft.github.io/picologging/)
- [When Women Stopped Coding](https://www.npr.org/sections/money/2014/10/21/357629765/when-women-stopped-coding)
- [Savannah Ostrowski](https://bsky.app/profile/savannah.dev/post/3mml3emj63k22)
- [Lean TDD](https://courses.pythontest.com/lean-tdd/)
- [Python Web Security: OWASP Top 10 with Agentic AI](https://training.talkpython.fm/courses/agentic-ai-python-security)
- [see announcement](https://talkpython.fm/blog/posts/spanish-subtitles-available-for-all-courses/)
- [Stop texting me](https://x.com/pr0grammerhum0r/status/2057733228899823981?s=12)
