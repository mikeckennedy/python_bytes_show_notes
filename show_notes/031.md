# Python Bytes 31
**Brian #1:** [**TinyMongo**](https://github.com/schapman1974/tinymongo)

- Like MongoDB, but built on top of TinyDB.
- Even runs on a Raspberry Pi, according to Stephen

**Michael #2:** [**A dead simple Python data validation library**](https://github.com/shopnilsazal/validus)

  - `validus.isemail('someone@example.com')`
- Validation functions include:
  - isrgbcolor()
  - isphone()
  - isisbn()
  - isipv4()
  - isint()
  - isfloat()
  - isslug()
  - isuuid()
- Requires Python 3.3+

**Brian #3:** [**PuDB**](https://documen.tician.de/pudb/index.html)

- In episode 29, [https://pythonbytes.fm/29](https://pythonbytes.fm/29), I talked about launching pdb from pytest failures.
- [@kidpixo](https://twitter.com/kidpixo) pointed out that PuDB was a better debugger and can also be launched from pytest failures.
- Starting pudb from pytest failed tests (from [docs](https://documen.tician.de/pudb/starting.html#usage-with-pytest)): 
    `pytest --pdbcls pudb.debugger:Debugger --pdb --capture=no`
- Using [pytest-pudb](https://pypi.python.org/pypi/pytest-pudb) plugin to do the same:
    `pytest --pudb`

**Michael #4:** [**Analyzing Django requirement files on GitHub**](https://pyup.io/posts/analyzing-django-requirement-files-on-github/)

- From the pyup.io guys
- Django is the most popular Python web framework. 
- It is now almost 12 years old and is used on all kinds of different projects.
- Django developers pin their requirements (64%): Pinned or freezed requirements (Django==1.8.12) make builds predictable and deterministic.
- Django 1.8 is the most popular major release (24%)
  - A bit worrisome are the 1.9 (14%), 1.7 (13%) and 1.6 (13%) releases on the second, third and fourth place. All of them are no longer receiving security updates, 1.7 and 1.6 went EOL over 2 years ago.
- Yikes: Only 2% of all Django projects are on a secure release
  - Among all projects, more than 60% use a Django release with one or more known security vulnerabilities. Only 2% are using a secure Django release.
  - On the remaining part of more than 30% it's unclear what exactly is going to be installed. That's because the Django release is either unpinned or has a range.

**Brian #5:** **Changelogs**

- [http://keepachangelog.com](http://keepachangelog.com)
- [https://github.com/hawkowl/towncrier](https://github.com/hawkowl/towncrier)

**Michael #6:** [**Understanding Asynchronous Programming in Python**](https://dbader.org/blog/understanding-asynchronous-programming-in-python)

- by Doug Farrell via Dan Bader’s site
- A synchronous program is what most of us started out writing, and can be thought of as performing one execution step at a time, one after another.
- Example: A web server
  - Could be synchronous
  - Could be fully optimized but
  - You’re at best still waiting on network IO back to all the web clients
- The Real World is Asynchronous: *Kids are a long running task with high priority, superseding any other task we might be doing, like the checkbook or laundry*.
- Example 1: Synchronous Programming (using queuing)
- Example 2: Simple Cooperative Concurrency (using generators)
- Example 3: Cooperative Concurrency With Blocking Calls (same, but with slow operations)
- Example 4: Cooperative Concurrency With Non-Blocking Calls (gevent)
- Example 5: Synchronous (Blocking) HTTP Downloads
- Example 6: Asynchronous (Non-Blocking) HTTP Downloads With gevent
- Example 7: Asynchronous (Non-Blocking) HTTP Downloads With Twisted
- Example 8: Asynchronous (Non-Blocking) HTTP Downloads With Twisted Callbacks


Errata/Giving Credit:

- Also in episode 29, [https://pythonbytes.fm/29](https://pythonbytes.fm/29), I talked about pipcache as an alias for pip download. I think I said the author of a blog post contacted me. It wasn’t him. It was [@kidpixo](https://twitter.com/kidpixo). Sorry kidpixo, keep the ideas coming.

For fun: Python Private Methods

- [http://turnoff.us/geek/python-private-methods/](http://turnoff.us/geek/python-private-methods/)

Our news

- Beta 3 of [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) should come out this week with Chapter 7: Using pytest with other tools, which includes using it with pdb, coverage.py, mock, tox, and Jenkins.
  - Next beta will be the appendices, including a clean up and rewrite of pip and venv appendices, plus a plugin sampler pack, and a tutorial on packaging.
  - Thanks to everyone who has submitted Errata. 
- Finished recording RESTful and HTTP Services in Pyramid AND MongoDB for Python Developers. Add your email address at [https://training.talkpython.fm](https://training.talkpython.fm) to get notified upon release of each.


