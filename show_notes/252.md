# Python Bytes 252


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Ethan Swan** 

**Michael #0: [Changing themes to DIY](https://twitter.com/shacharmirkin/status/1441291234937491459)**

**Brian #1:** [**SQLFluff**](https://www.sqlfluff.com/)

- Suggested by Dave Kotchessa.
- A SQL Linter, written in Python, tested with pytest
- Configurable, and configuration can live in many places including `tox.ini` and `pyproject.toml`.
- [Great docs](https://docs.sqlfluff.com/en/stable/)
- [Rule reference](https://docs.sqlfluff.com/en/stable/rules.html) with anti-pattern/best practice format
- Includes dialects for ANSI, PostgreSQL, MySQL, Teradata, BigQuery, Snoflake
- Note in docs: “**SQLFluff** is still in an open alpha phase - expect the tool to change significantly over the coming months, and expect potentially non-backward compatible api changes to happen at any point.”

**Michael #2:** [**JupyterLab Desktop**](https://blog.jupyter.org/jupyterlab-desktop-app-now-available-b8b661b17e9a)

- [JupyterLab App](https://github.com/jupyterlab/jupyterlab_app) is the cross-platform standalone application distribution of [JupyterLab](https://github.com/jupyterlab/jupyterlab).
- Bundles a Python environment with several popular Python libraries ready to use in scientific computing and data science workflows.
- JupyterLab App works on Debian and Fedora based Linux, macOS and Windows operating systems.

**Ethan #3:** [**Requests Cache**](https://github.com/reclosedev/requests-cache/)

- Create a requests_cache session and call HTTP methods from there
	- You can also do it without a session but that’s a bit weird, looks like it’s monkey patching requests or something…
- Results are cached
- Very handy for repeatedly calling endpoints
	- especially if the returned data is large, or the server has to do some compute
- Reminds me of @functools.lru_cache 
- Can set things like how long the cache should last (when to invalidate)
- Funny easter egg in example: “# Cache 400 responses as a solemn reminder of your failures”


**Brian #4:** [**pypi-rename**](https://github.com/simonw/pypi-rename)

- This is a cookiecutter template from Simon Willison
- Backstory:
	- To refresh my memory on how to publish a new package with flit I created [a new pytest plugin](https://pypi.org/project/pytest-skip-slow/).
	- Brian Skinn noticed it somehow, and suggested a better name. Thanks Brian.
	- So, how to nicely rename. I searched and found Simon’s template, which is…
- A cookiecutter template. So you can use cookiecutter to do some of this work for you.
- But it’s based on setuptools, and I kinda like flit lately, so I just used the instructions.
- The README.md includes instructions for the steps needed: 
	- Create renamed version
	- Publish under new name
	- Change old one to depend on new one, but be mostly empty
	- Modify readme to tell people what's going on
	- Publish old name as a notice
- Now people looking for old one will find new one.
- People just installing old one will end up with new one also since it’s a dependency.

**Michael #5:** [**Django 4 coming with Redis Adapter**](https://github.com/django/django/pull/14437)

- #33012 closed New feature (fixed) → Add a Redis cache backend. 
- Adds support for Redis to be used as a caching backend with Django. 
- Redis is the most popular caching backend, adding it to django.core.cache module would be a great addition for developers who previously had to rely on the use of third party packages.
- It will be simpler than that provided by `django-redis`, for instance customising the serialiser is out-of-scope for the initial pass.

**Ethan #6:** [**PEP 612**](https://www.python.org/dev/peps/pep-0612/)

- It wasn’t possible to type a function that took in a function and returned a function with the same signature (which is what many decorators do)
	- This creates a ParamSpec – which is much like a TypeVar, for anyone who has used them to type generic functions/classes
- It’s a reminder that typing is still missing features and evolving, and it’s good to accept the edge cases for now – “gradual typing”
	- Reading Fluent Python by Ramalho has influenced my view on this – don’t lose your mind trying to type crazy stuff, just accept that it’s “gradual”
- Mention how typing is still evolving in Python and it’s good to keep an eye out for new features that help you (see also [PEP 645](https://www.python.org/dev/peps/pep-0645/) – using `int?` for `Optional[int]`; and [PEP 655](https://www.python.org/dev/peps/pep-0655/) – annotating some TypedDict keys as required and others not required)

**Extras**

**Michael**

- [**Earsketch**](https://twitter.com/AntonioAndrade/status/1440637306558316546)
- **Django Critical CVE:** [**CVE-2021-35042**](https://github.com/advisories/GHSA-xpfp-f569-q3p2)
	- **Vulnerable versions:** >= 3.0.0, < 3.1.13
	- **Patched version:** 3.1.13
	- Django 3.1.x before 3.1.13 and 3.2.x before 3.2.5 allows QuerySet.order_by SQL injection if order_by is untrusted input from a client of a web application.

**Ethan**
- [**Pedalboard**](https://github.com/spotify/pedalboard)
	- I happened upon this project recently and checked back, only to see that Brett Cannon was the last committer! A doc fix, like he suggested last episode

Brian

- [**Zero Cost Exceptions in Python 3.11**](https://docs.python.org/3.11/whatsnew/3.11.html#optimizations)
	- Suggested by John Hagen
	- Guido, Mark Shannon, and others at Microsoft are working on speeding up Python
	- [faster-cpython/ideas repo](https://github.com/faster-cpython/ideas) includes a slide deck from Guido which includes “Zero overhead” exception handling.
	- [Python 3.11 “What’s New” page, Optimizations section](https://docs.python.org/3.11/whatsnew/3.11.html#optimizations) includes:
    - “Zero-cost” exceptions are implemented. The cost of `try` statements is almost eliminated when no exception is raised. (Contributed by Mark Shannon in [bpo-40222](https://bugs.python.org/issue40222).)
	- MK: I [**played with this a bit**](https://gist.github.com/mikeckennedy/f516c9cf2f7a69a02a815e3799b42f95).

**Joke:** [**QA 101**](https://geek-and-poke.com/geekandpoke/2021/1/31/qa-101)

