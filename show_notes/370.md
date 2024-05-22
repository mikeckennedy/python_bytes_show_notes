# Python Bytes 370
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:**  [**Dokku**](https://dokku.com)

- An open source PAAS alternative to Heroku.
- Dokku helps you build and manage the lifecycle of applications from building to scaling.
- Powered by Docker, you can install Dokku on any hardware.
- Once it's set up on a host, you can push Heroku-compatible applications to it via Git. 
- Rich [plug in architecture](https://dokku.com/docs/community/plugins/).

**Brian #2:** [**Summary of Major Changes Between Python Versions**](https://www.nicholashairs.com/posts/major-changes-between-python-versions/)

- Nicholas Hairs
- Changes between versions & Tools & utilities to help with switching
- Hopefully you’re already at least at 3.8, but come on, 3.11 & 3.12 are so fun!
- Useful things
    - `pyupgrade` can automatically upgrade code base
        - (However, I frequently just upgrade and run tests and let my old code be as-is until it bugs me. - Brian)
    - `black` checks `pyproject.toml` `requires-python` setting and uses version specific rules.
- Versions (way more highlights listed in the article)
    - 3.8 
        - Assignment expressions `:=` walrus
        - `f"{variable=}"` now works
    - 3.9 
        - Typing has built in generics like `dict[]`, so no more `from typing import Dict`
        - Dict union operator
        - Strings can `removeprefix` and `removesuffix`
    - 3.10
        - Structural pattern matching `match/case`
        - Typing: Union using pipe `|`
        - Dataclasses support `slots=True` and `kw_only=True`
    - 3.11
        - `tomllib` included as a standard TOMP parser
        - Exception groups
        - Exception Notes `add_note()`
        - Typing: A `Self` type
        - Star unpacking expressions allowed in `for` statements: `for x in *a, *b:`
    - 3.12
        - f-strings can re-use quotes
        - Typing: better type parameter syntax
        - Typing: `@override` decorator ensures a method being overridden by a child class actually exists.

**Michael #3:**  How to check Internet Speed via Terminal? [speedtest-cli](https://github.com/sivel/speedtest-cli)

- Command line interface for testing internet bandwidth using speedtest.net
- Just `pipx install speedtest-cli`
- Has a [Python API](https://github.com/sivel/speedtest-cli/wiki) too

**Brian #4:** **Blogs: We all should blog more**

- Jeff Triplett is attempting one post per day in February
    - Feb 1: [Choosing the Right Python and Django Versions for Your Projects](https://micro.webology.dev/2024/02/01/choosing-the-right.html)
    - Feb 2: [My First Mac](https://micro.webology.dev/2024/02/02/my-first-mac.html)
        - Which also links to a quite interesting Personal: [Default Apps 2023](https://jefftriplett.com/2023/default-apps-2023/)
    - Feb 3: [What’s Your Go-to Comfort Media? [rough cut]](https://micro.webology.dev/2024/02/03/whats-your-goto.html)
    - Feb 4: [The Django apps I actually use (rough cut)](https://micro.webology.dev/2024/02/04/the-django-apps.html)
    - Feb 5: [How to test with Django and pytest fixtures](https://micro.webology.dev/2024/02/05/how-to-test.html)
- Need ideas? 
    - Check out [Build an idea bank and never run out of blog ideas](https://hamatti.org/posts/build-an-idea-bank-and-never-run-out-of-blog-ideas/)
- Not using AI? Thanks. We appreciate that.
    - Maybe tag it as [Not By AI](https://notbyai.fyi/)


**Extras** 

Brian:

- If upgrading to pytest 8, be aware that running individual tests with parametrization will result in a reverse order. 
    - It shouldn’t matter. [You shouldn’t be depending on test order.](https://podcast.pythontest.com/episodes/211-stamp-out-test-dependencies-with-pytest-plugins)
    - But it was surprising to me.
    - [Issue has been logged](https://github.com/pytest-dev/pytest/issues/11937)

Michael:

- [Orbstack](https://orbstack.dev) follow up

**Joke:** [White Lies](https://workchronicles.com/white-lies/)

