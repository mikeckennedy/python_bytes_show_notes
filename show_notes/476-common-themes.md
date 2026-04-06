# PB 476

## **Show Intro**

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

## **Brian #1: [Migrating from mypy to ty: Lessons from FastAPI](https://pydevtools.com/blog/migrating-from-mypy-to-ty-lessons-from-fastapi/)**

- Tim Hopper

## **Michael #2: [Oxyde ORM](https://oxyde.fatalyst.dev/latest/)**

- **Oxyde ORM** is a type-safe, Pydantic-centric asynchronous ORM with a high-performance Rust core.
- Note: Oxyde is a young project under active development. The API may evolve between minor versions.
- No sync wrappers or thread pools. Oxyde is async from the ground up
- Includes [**oxyde-admin**](https://github.com/mr-fatalyst/oxyde-admin)
- Features
    - **Django-style API** - Familiar `Model.objects.filter()` syntax
    - **Pydantic v2 models** - Full validation, type hints, serialization
    - **Async-first** - Built for modern async Python with `asyncio`
    - **Rust performance** - SQL generation and execution in native Rust
    - **Multi-database** - PostgreSQL, SQLite, MySQL support
    - **Transactions** - `transaction.atomic()` context manager with savepoints
    - **Migrations** - Django-style `makemigrations` and `migrate` CLI

## Brian #3: [Typeshedded CPython docs](https://guoci.github.io/typeshedded_CPython_docs/library/functions.html)

-

## **Michael #4:** [Raw+DC Database Pattern: A Retrospective](https://mkennedy.codes/posts/raw-dc-a-retrospective/)

- A new design pattern I’m seeing gain traction in the software space: [Raw+DC: The ORM pattern of 2026](https://mkennedy.codes/posts/raw-dc-the-orm-pattern-of-2026/)
- I’ve had a chance to migrate three of my most important web app.
- Thrilled to report that yes, **the web app is much faster using Raw+DC**
- Plus, this was part of the journey to move from 1.3 GB memory usage to 0.45 GB (more on this next week)
![](https://cdn.mkennedy.codes/posts/raw-dc-a-retrospective/raw-dc-vs-mongoengine-graph.webp)

## **Extras**

Brian:
- 
Michael:
- [pytest-just](https://github.com/databooth/pytest-just) (for [just command file](https://github.com/casey/just?featured_on=pythonbytes) testing), by Michael Booth
- Something going on with Encode
    - **httpx**: [Anyone know what's up with HTTPX?](https://www.reddit.com/r/Python/comments/1rl5kuq/anyone_know_whats_up_with_httpx/) And [forked](https://tildeweb.nl/~michiel/httpxyz.html)
    - **starlette** and **uvicorn**: [Transfer of Uvicorn & Starlette](https://github.com/Kludex/starlette/discussions/2997)
    - **mkdocs**: [The Slow Collapse of MkDocs](https://fpgmaas.com/blog/collapse-of-mkdocs/)
    - **django-rest-framework:** [Move to django commons?](https://github.com/django-commons/membership/issues/188#issue-3070631761)
- [Certificates at Talk Python Training](https://talkpython.fm/blog/posts/announcing-course-completion-certificates/)

## **Joke:**

- [**Neue Rich**](https://x.com/PR0GRAMMERHUM0R/status/2021509552504525304)
- A nice April  1 joke: [HumanDB](https://motherduck.com/blog/introducing-humandb/), including [Demo](https://motherduck.com/humandb/)

## Links

- [Migrating from mypy to ty: Lessons from FastAPI](https://pydevtools.com/blog/migrating-from-mypy-to-ty-lessons-from-fastapi/)
- [Oxyde ORM](https://oxyde.fatalyst.dev/latest/)
- [oxyde-admin](https://github.com/mr-fatalyst/oxyde-admin)
- [Raw+DC Database Pattern: A Retrospective](https://mkennedy.codes/posts/raw-dc-a-retrospective/)
- [Raw+DC: The ORM pattern of 2026](https://mkennedy.codes/posts/raw-dc-the-orm-pattern-of-2026/)
- [cdn.mkennedy.codes/posts/raw-dc-a-retrospective/raw-dc-vs-mongoengine-graph.webp](https://cdn.mkennedy.codes/posts/raw-dc-a-retrospective/raw-dc-vs-mongoengine-graph.webp)
- [pytest-just](https://github.com/databooth/pytest-just)
- [just command file](https://github.com/casey/just?featured_on=pythonbytes)
- [Anyone know whats up with HTTPX](https://www.reddit.com/r/Python/comments/1rl5kuq/anyone_know_whats_up_with_httpx/)
- [forked](https://tildeweb.nl/~michiel/httpxyz.html)
- [Transfer of Uvicorn & Starlette](https://github.com/Kludex/starlette/discussions/2997)
- [The Slow Collapse of MkDocs](https://fpgmaas.com/blog/collapse-of-mkdocs/)
- [Move to django commons](https://github.com/django-commons/membership/issues/188#issue-3070631761)
- [Certificates at Talk Python Training](https://talkpython.fm/blog/posts/announcing-course-completion-certificates/)
- [Neue Rich](https://x.com/PR0GRAMMERHUM0R/status/2021509552504525304)
- [HumanDB](https://motherduck.com/blog/introducing-humandb/)
- [Demo](https://motherduck.com/humandb/)
