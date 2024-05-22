# Python Bytes 328
Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**zipapp**](https://docs.python.org/3/library/zipapp.html)

- Part of standard library since 3.5
- Yet another thing I learned recently from Brett Cannon
- “This module provides tools to manage the creation of zip files containing Python code, which can be executed directly by the Python interpreter. The module provides both a Command-Line Interface and a Python API.”
- Including: [Creating Standalone Applications with zipapp](https://docs.python.org/3/library/zipapp.html?utm_source=pocket_reader#creating-standalone-applications-with-zipapp)

**Michael #2:** [**Reverse engineering the Apple News app with #python and #nerd power**](https://fosstodon.org/@RhetTbull/110019719917842546)

- As we navigate the digital world, we often come across articles we don't have time to read but still want to save for later. 
- One way to accomplish this is by using the Read Later feature in Apple News. 
- But what if you want to access those articles outside the Apple News app, such as on a different device or with someone who doesn't use Apple News? 
- Or what if you want to automatically post links to those articles on your blog? That's where the nerd powers come in.
- The linked article shows how to use Python to solve your own problem
- Leading to Rhet Turnbull’s CLI: [**apple-news-to-sqlite**](https://github.com/RhetTbull/apple-news-to-sqlite)

**Brian #3:** [**What is a context manager?**](https://docs.python.org/3/library/zipapp.html?utm_source=pocket_reader#exampleshttps://www.pythonmorsels.com/what-is-a-context-manager/)

- Trey Hunner
- Also look at all the cool goodies in [contextlib](https://docs.python.org/3/library/contextlib.html) from standard library
    - `@contextmanager`
    - `closing`
    - `suppress`
    - `redirect_stdout`, `redirect_stderr`
    - `chdir`

**Michael #4:** [**nox-poetry: Use Poetry inside Nox sessions**](https://github.com/cjolowicz/nox-poetry)

- via 2 people: John Hagen and Marc Prewitt
- This package provides a drop-in replacement for the `nox.session` decorator, and for the `nox.Session` object passed to user-defined session functions.
- Comes from Claudio Jolowicz's [hypermodern python cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
    - Covered this on Talk Python: [talkpython.fm/episodes/show/362/hypermodern-python-projects](https://talkpython.fm/episodes/show/362/hypermodern-python-projects)
- This session performs the following steps:
    - Build a wheel from the local package.
    - Install the wheel as well as the `pytest` package.
    - Invoke `pytest` to run the test suite against the installation.
- Consider what would happen in this session if we had imported `@session` from `nox` instead of `nox_poetry`:
    - Package dependencies would only be constrained by the wheel metadata, not by the lock file. In other words, their versions would not be *pinned*.
    - The `pytest` dependency would not be constrained at all.
    - Poetry would be installed as a build backend every time.

**Extras** 

Brian:

- [Sharing is Caring: Sharing pytest fixtures](https://pythontest.com/pycascades-2023/) talk availabe at a[bout 2:40:58 on Day 2 video of PyCascades 2023](https://www.youtube.com/live/bCGyj8n5F6k?feature=share&t=9656). 
    - Also full [Day 1](https://www.youtube.com/watch?v=c_kAvhsQKJg) and [Day 2](https://www.youtube.com/watch?v=bCGyj8n5F6k)

Michael:

- Wired connection to remote mesh router == wow!
    - Using the [Linksys Atlas Max 6E](https://www.linksys.com/mx8503---tri-band-axe8400-mesh-wifi-6e-system-3-pack/MX8503.html)

**Joke:** [**UnsafeWarnings**](https://www.etsy.com/nz/shop/UnsafeWarnings)



