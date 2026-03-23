# #474: Astral to join OpenAI

**Show Intro**

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

**Brian #1: [Starlette 1.0.0](https://starlette.dev/release-notes/#100rc1-february-23-2026)**

- As a reminder, Starlette is the foundation for FastAPI
- [Starlette 1.0 is here!](https://marcelotryle.com/blog/2026/03/22/starlette-10-is-here/) - fun blog post from Marcello Trylesinski
- “The changes in 1.0 were limited to removing old deprecated code that had been on the way out for years, along with a few bug fixes. From now on we'll follow SemVer strictly.”
- Fun comment in the “What’s next?” section:
  - “Oh, and Sebastián, Starlette is now out of your way to release FastAPI 1.0. 😉”
- Related: [Experimenting with Starlette 1.0 with Claude skills](https://simonwillison.net/2026/Mar/22/starlette/)
  - Simon Willison
  - example of the new lifespan mechanism, very pytest fixture-like
  ```python
  @contextlib.asynccontextmanager
  async def lifespan(app):
      async with some_async_resource():
          print("Run at startup!")
          yield
          print("Run on shutdown!")
  app = Starlette(
      routes=routes,
      lifespan=lifespan
  )
  ```

**Michael #2: [Astral to join OpenAI](https://astral.sh/blog/openai)**

- via John Hagen, thanks
- Astral has agreed to join [**OpenAI**](https://openai.com/) as part of the [**Codex**](https://chatgpt.com/codex) team
- Congrats Charlie and team
- Seems like [**Ruff](https://github.com/astral-sh/ruff)** and [**uv](https://github.com/astral-sh/uv)** play an important roll.
- Perhaps [**ty**](https://github.com/astral-sh/ty) holds the most value to directly boost Codex (understanding codebases for the AI)
- All that said, these were open source so there is way more to the motivations than just using the tools.
- After joining the Codex team, we'll continue building our open source tools.
- [Simon Willison has thoughts](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/)
- [d](http://discuss.python.org)[iscuss.python.org also has thoughts](https://discuss.python.org/t/openai-to-acquire-astral/106605)
- The [Ars Technica article](https://arstechnica.com/ai/2026/03/openai-is-acquiring-open-source-python-tool-maker-astral/) has interesting comments too
- It’s probably the death [pyx](https://astral.sh/pyx)
  - Simon points out “pyx is notably absent from both the Astral and OpenAI announcement posts.”

**Brian #3: uv audit**

- Submitted by Owen Lemont
- Pieces of `uv audit` have been trickling in. [uv 0.10.12 exposes it to the cli help](https://github.com/astral-sh/uv/releases)
- Here’s the [roadmap for uv audit](https://github.com/astral-sh/uv/issues/18506)
- I tried it out on a package and found a security issue with a dependency
  - not of the project, but of the testing dependencies
  - but only if using Python < 3.10, even though I’m using 3.14
- Kinda cool
- Looks like it generates a uv.lock file, which includes dependencies for all project supported versions of Python and systems, which is a very thorough way to check for vulnerabilities.
- But also, maybe some pointers on how to fix the problem would be good. No `--fix` yet.

**Michael #4: [Fire and forget (or never) with Python’s asyncio](https://mkennedy.codes/posts/fire-and-forget-or-never-with-python-s-asyncio/)**

- Python’s `asyncio.create_task()` can silently garbage collect your fire-and-forget tasks starting in Python 3.12
- Formerly fine async code can now stop working, so heads up
- The fix? Use a set to upgrade to a strong ref and a callback to remove it
- Is there a chance of task-based memory leaks? Yeah, maybe.

**Extras**

Brian:
- [Nobody Gets Promoted for Simplicity](https://terriblesoftware.org/2026/03/03/nobody-gets-promoted-for-simplicity/) - interesting read and unfortunate truth in too many places.
- [pytest-check](https://github.com/okken/pytest-check) - All built-in check helper functions in this list also accept an optional `xfail` reason.
  - example: `check.equal(actual, expected, xfail="known issue #123")`
  - Allows some checks to still cause a failure to happen because you no longer have to mark the whole test as xfail
  Michael:
- [TurboAPI](https://x.com/rachpradhan/status/2034191434182738096) - FastAPI + Pydantic compatible framework in Zig (see [follow up](https://x.com/rachpradhan/status/2035928730242371716))
- [Pyramid 2.1](https://docs.pylonsproject.org/projects/pyramid/en/2.1-branch/whatsnew-2.1.html) is out (yes really! :) first release in 3 years)
- [Vivaldi 7.9 adds](https://vivaldi.com/blog/vivaldi-on-desktop-7-9/) minimalist hide mode.
- Migrated [pythonbytes.fm](http://pythonbytes.fm) and [talkpython.fm](http://talkpython.fm) to [Raw+DC design pattern](https://mkennedy.codes/posts/raw-dc-the-orm-pattern-of-2026/)
- [Robyn + Chameleon package](https://mkennedy.codes/posts/use-chameleon-templates-in-the-robyn-web-framework/)

**Joke: We now have [translation services](https://translate.kagi.com)**

Links

- [Starlette 1.0.0](https://starlette.dev/release-notes/#100rc1-february-23-2026)
- [Starlette 1.0 is here](https://marcelotryle.com/blog/2026/03/22/starlette-10-is-here/)
- [Experimenting with Starlette 1.0 with Claude skills](https://simonwillison.net/2026/Mar/22/starlette/)
- [Astral to join OpenAI](https://astral.sh/blog/openai)
- [OpenAI](https://openai.com/)
- [Codex](https://chatgpt.com/codex)
- [Ruff](https://github.com/astral-sh/ruff)
- [uv](https://github.com/astral-sh/uv)
- [ty](https://github.com/astral-sh/ty)
- [Simon Willison has thoughts](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/)
- [d](http://discuss.python.org)
- [iscuss.python.org also has thoughts](https://discuss.python.org/t/openai-to-acquire-astral/106605)
- [Ars Technica article](https://arstechnica.com/ai/2026/03/openai-is-acquiring-open-source-python-tool-maker-astral/)
- [pyx](https://astral.sh/pyx)
- [iscuss.python.org](https://iscuss.python.org)
- [uv 0.10.12 exposes it to the cli help](https://github.com/astral-sh/uv/releases)
- [roadmap for uv audit](https://github.com/astral-sh/uv/issues/18506)
- [Fire and forget (or never) with Python’s asyncio](https://mkennedy.codes/posts/fire-and-forget-or-never-with-python-s-asyncio/)
- [Nobody Gets Promoted for Simplicity](https://terriblesoftware.org/2026/03/03/nobody-gets-promoted-for-simplicity/)
- [pytest-check](https://github.com/okken/pytest-check)
- [TurboAPI](https://x.com/rachpradhan/status/2034191434182738096)
- [follow up](https://x.com/rachpradhan/status/2035928730242371716)
- [Pyramid 2.1](https://docs.pylonsproject.org/projects/pyramid/en/2.1-branch/whatsnew-2.1.html)
- [Vivaldi 7.9 adds](https://vivaldi.com/blog/vivaldi-on-desktop-7-9/)
- [talkpython.fm](http://talkpython.fm)
- [Raw+DC design pattern](https://mkennedy.codes/posts/raw-dc-the-orm-pattern-of-2026/)
- [Robyn + Chameleon package](https://mkennedy.codes/posts/use-chameleon-templates-in-the-robyn-web-framework/)
- [translation services](https://translate.kagi.com)
