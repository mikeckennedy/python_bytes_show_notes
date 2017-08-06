# Python Bytes 37
**Brian #1:** [**New URL for Python Developer’s Guide**](https://devguide.python.org/)

- How to contribute to CPython

Some really useful links that I hadn’t noticed before. Also great ideas to include in a contributing guide for any large open source project:

- Core developers and contributors alike will find the following guides useful:
  - [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) (from https://opensource.guide)
  - [Building Welcoming Communities](https://opensource.guide/building-community/) (from https://opensource.guide)
- Guide for contributing to Python:
  - [Getting Started](https://devguide.python.org/setup/)
  - [Where to Get Help](https://devguide.python.org/help/)
  - [Lifecycle of a Pull Request](https://devguide.python.org/pullrequest/)
  - [Running & Writing Tests](https://devguide.python.org/runtests/)
  - Beginner tasks to become familiar with the development process
    - [Helping with Documentation](https://devguide.python.org/docquality/)
    - [Increase Test Coverage](https://devguide.python.org/coverage/)
  - Advanced tasks for once you are comfortable
    - [Silence Warnings From the Test Suite](https://devguide.python.org/silencewarnings/)
    - Fixing issues found by the [buildbots](https://devguide.python.org/buildbots/)
    - [Fixing “easy” Issues (and Beyond)](https://devguide.python.org/fixingissues/)
  - [Using the Issue Tracker](https://devguide.python.org/tracker/#tracker) and [Helping Triage Issues](https://devguide.python.org/tracker/#helptriage)
    - [Triaging an Issue](https://devguide.python.org/triaging/)
    - [Experts Index](https://devguide.python.org/experts/)
  - [Following Python’s Development](https://devguide.python.org/communication/)
  - [How to Become a Core Developer](https://devguide.python.org/coredev/)
    - [Committing and Pushing Changes](https://devguide.python.org/committing/)
    - [Development Cycle](https://devguide.python.org/devcycle/)
    - [Continuous Integration](https://devguide.python.org/buildbots/)
  - [Git Bootcamp and Cheat Sheet](https://devguide.python.org/gitbootcamp/)

**Michael #2:** [**Sultan: Command and Rule Over Your Shell**](https://sultan.readthedocs.io/en/latest/)

- Python package for interfacing with command-line utilities, like yum, apt-get, or ls, in a Pythonic manner

Simple example

    from sultan.api import Sultan
    s = Sultan()
    s.sudo("yum install -y tree").run()

Better in a context manager:

    from sultan.api import Sultan
    
    with Sultan.load(sudo=True) as s:
      s.yum("install -y tree").run()

Even works remotely:

    from sultan.api import Sultan
    
    with Sultan.load(sudo=True, hostname="myserver.com") as sultan:
      sultan.yum("install -y tree").run()

**Brian #3:** [**Flake8Lint**](https://github.com/dreadatour/Flake8Lint)

- Sublime Text plugin for lint Python files.
- Includes these linters and style checkers:
  - [**Flake8**](http://pypi.python.org/pypi/flake8) (used in "Python Flake8 Lint") is a wrapper around these tools:
    - [**pep8**](http://pypi.python.org/pypi/pep8) is a tool to check your Python code against some of the style conventions in [PEP8](http://www.python.org/dev/peps/pep-0008/).
    - [**PyFlakes**](https://launchpad.net/pyflakes) checks only for logical errors in programs; it does not perform any check on style.
    - [**mccabe**](http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html) is a code complexity checker. It is quite useful to detect over-complex code. According to McCabe, anything that goes beyond 10 is too complex. See [Cyclomatic_complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity).
  - There are additional tools used to lint Python files:
    - [**pydocstyle**](https://github.com/PyCQA/pydocstyle) is a static analysis tool for checking compliance with Python [PEP257](http://www.python.org/dev/peps/pep-0257/).
    - [**pep8-naming**](https://github.com/flintwork/pep8-naming) is a naming convention checker for Python.
    - [**flake8-debugger**](https://github.com/JBKahn/flake8-debugger) is a flake8 debug statement checker.
    - [**flake8-import-order**](https://github.com/public/flake8-import-order) is a flake8 plugin that checks import order in the fashion of the Google Python Style Guide (turned off by default).

**Michael #4:** [**Magic Wormhole**](https://github.com/warner/magic-wormhole)

- Get things from one computer to another, safely.
- A library and a command-line tool named `wormhole`, which makes it possible to get arbitrary-sized files and directories (or short pieces of text) from one computer to another.
- The two endpoints are identified by using identical "wormhole codes”
- Video from PyCon 2016: [https://www.youtube.com/watch?v=oFrTqQw0_3c](https://www.youtube.com/watch?v=oFrTqQw0_3c)
- The codes are short and human-pronounceable, using a phonetically-distinct wordlist.
- As a library too: The wormhole module makes it possible for other applications to use these code-protected channels. 

**Brian #5:** [**Python Virtual Environments Primer**](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

- why do we need virtual environments
- what are they
- how to use them / how do they work
- also
  - virtualenvwrapper
  - using different versions of python
  - pyvenv

**Michael #6:** [**How Rust can replace C, with Python's help**](http://www.infoworld.com/article/3208391/python/how-rust-can-replace-c-with-pythons-help.html)

- Why Rust? Rust has
  - a type system feature that helps eliminate memory leaks,
  - proper interfaces, called 'traits',
  - better type inference,
  - better support for concurrency,
  - (almost) first-class functions that can be passed as arguments.
- It isn’t difficult to expose Rust code to Python. A Rust library can expose a C ABI (application binary interface) to Python without too much work. 
- Some Rust crates (as Rust packages are called) already expose Python bindings to make them useful in Python.
- A new spate of projects are making it easier to develop Rust libraries with convenient bindings to Python – and to deploy Python packages that have Rust binaries
- [**Rust-CPython**](https://github.com/dgrunwald/rust-cpython)**:** 
  - **What it is:** A set of bindings in Rust for the CPython runtime. This allows a Rust program to connect to CPython, use its ABI, run Python programs through it, and work with representations of Python objects in Rust itself.
  - **Who it’s for:** Rust programmers who want to hook into CPython and control it from the inside out.
- [**PyO3**](https://github.com/PyO3/PyO3)
  - **What it is:** For Rust developers, the PyO3 project provides a basic way to write Rust software with bindings to Python in both directions. A Rust program can interface with Python objects and the Python interpreter, and can expose Rust methods to a Python program in the same way a C module does.
  - **Who it’s for:** Those writing modules that work closely with the Python runtime, and need to interact directly with it.
- [**Snaek**](https://github.com/mitsuhiko/snaek/)
  - **What it is:** Another project in the early stages, Snaek lets developers create Rust libraries that are loaded dynamically into Python as needed, but don’t rely on being linked statically against Python’s runtime.
  - Doesn’t use CTypes but CFFI
  - **Who it’s for:** Those who want to expose methods written in Rust to a Python script, or for Rust developers who don’t want or need to become familiar with Python.
- And there is a cookiecutter project / template too
  - [https://github.com/mckaymatt/cookiecutter-pypackage-rust-cross-platform-publish](https://github.com/mckaymatt/cookiecutter-pypackage-rust-cross-platform-publish)
  - “A very important goal of the project,” writes its maintainers, “is that it be able to produce a binary distribution (Wheel) which will not require the end user to actually compile the Rust code themselves.”

Our news:

Michael is officially on vacation now.

