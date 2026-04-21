# #477: Lazy, Frozen, and 31% Lighter

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

## **Michael #1: [Django Modern Rest](https://django-modern-rest.readthedocs.io/en/latest/)**

- Modern REST framework for Django with types and async support
- Supports Pydantic, Attrs, and msgspec
- Has ai coding support with llms.txt
- See an example at the [“showcase” section](https://django-modern-rest.readthedocs.io/en/latest/pages/getting-started.html#showcase)

## **Brian #2: Already playing with Python 3.15**

- [3.15.0a8, 2.14.4 and 3.13.13 are out](https://blog.python.org/2026/04/python-3150a8-3144-31313/)
  - Hugo von Kemenade
- beta comes in May, CRs in Sept, and Final planned for October
- But still, there’s awesome stuff here already, here’s what I’m looking forward to:
  - [**PEP 810**](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-lazy-imports): Explicit lazy imports
  - [**PEP 814**](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-frozendict): `frozendict` built-in type
  - [**PEP 798**](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-unpacking-in-comprehensions): Unpacking in comprehensions with `*` and `**`
  - [**PEP 686**](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-utf8-default): Python now uses UTF-8 as the default encoding

## **Michael #3: [Cutting Python Web App Memory Over 31%](https://mkennedy.codes/posts/cutting-python-web-app-memory-over-31-percent/)**

- I cut 3.2 GB of memory usage from our Python web apps using five techniques:
  - async workers
  - import isolation
  - the Raw+DC database pattern
  - local imports for heavy libraries
  - disk-based caching
- [See the full article](https://mkennedy.codes/posts/cutting-python-web-app-memory-over-31-percent/) for details.

## **Brian #4: [tryke - A Rust-based Ptyhon test runner with a Jest-style API](https://tryke.dev)**

- Justin Chapman
- Watch mode, Native async support, Fast test discovery, In-source testing, Support for doctests, Client/server mode for fast editor integrations, Pretty, per-assertion diagnostics, Filtering and marks, Changed mode (like pytest-picked), Concurrent tests, Soft assertions,
- JSON, JUnit, Dot, and LLM reporters
- Honestly haven’t tried it yet, but you know, I’m kinda a fan of thinking outside the box with testing strategies so I welcome new ideas.

## **Extras**

Brian:
- [Why are’t we uv yet?](https://aleyan.com/blog/2026-why-arent-we-uv-yet/)
  - Interesting take on the “agents prefer pip”
  - Problem with analysis.
    - Many projects are libraries and don’t publish uv.lock file
    - Even with uv, it still often seen as a developer preference for non-libarries. You can sitll use uv with requirements.txt
- [PyCon US 2026 talks schedule is up](https://us.pycon.org/2026/schedule/talks/)
  - Interesting that there’s an AI track now. I won’t be attending, but I might have a bot watch the videos and summarize for me. :)
- [What has technology done to us?](https://justinjackson.ca/tech-done-to-us)
  - Justin Jackson
- [Lean TDD new cover](https://courses.pythontest.com/lean-tdd/)
  - Also, 0.6.1 is so ready for me to start f-ing reading the audio book and get on with this shipping the actual f-ing book and yes I realize I seem like I’m old because I use “f-ing” while typing.
Michael:
- [Python 3.14.4 is out](https://docs.python.org/release/3.14.4/whatsnew/changelog.html)
- [Beanie 2.1 release](https://github.com/BeanieODM/beanie/releases/tag/2.1.0)

## **Joke: [HumanDB](https://motherduck.com/humandb/) - Blazingly slow. Emotionally consistent.**

## Links

- [Django Modern Rest](https://django-modern-rest.readthedocs.io/en/latest/)
- [“showcase” section](https://django-modern-rest.readthedocs.io/en/latest/pages/getting-started.html#showcase)
- [3.15.0a8, 2.14.4 and 3.13.13 are out](https://blog.python.org/2026/04/python-3150a8-3144-31313/)
- [PEP 810](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-lazy-imports)
- [PEP 814](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-frozendict)
- [PEP 798](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-unpacking-in-comprehensions)
- [PEP 686](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-utf8-default)
- [Cutting Python Web App Memory Over 31%](https://mkennedy.codes/posts/cutting-python-web-app-memory-over-31-percent/)
- [tryke - A rRust-based Ptyhon test runner with a Jest-style API](https://tryke.dev)
- [Why are’t we uv yet](https://aleyan.com/blog/2026-why-arent-we-uv-yet/)
- [PyCon US 2026 talks schedule is up](https://us.pycon.org/2026/schedule/talks/)
- [What has technology done to us](https://justinjackson.ca/tech-done-to-us)
- [Lean TDD new cover](https://courses.pythontest.com/lean-tdd/)
- [Python 3.14.4 is out](https://docs.python.org/release/3.14.4/whatsnew/changelog.html)
- [Beanie 2.1 release](https://github.com/BeanieODM/beanie/releases/tag/2.1.0)
- [HumanDB](https://motherduck.com/humandb/)
