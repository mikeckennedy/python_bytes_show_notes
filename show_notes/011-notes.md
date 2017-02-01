This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 11, recorded on **January 30th, 2017**. In this episode we discuss **pipenv for profile functionality, Django 2.0 is dropping Python 2 entirely, and Pythonic home automation** [more] 

**#1 (Brian) [pipenv](https://www.kennethreitz.org/essays/announcing-pipenv) - Pipfile, pip, and virtualenv**

- [announcement from Kenneth Reitz](https://www.kennethreitz.org/essays/announcing-pipenv) 
- [reddit thread](https://www.reddit.com/r/Python/comments/5pmb8o/announcing_pipenv_from_kenneth_reitz/) 
- Features
  - Automatically finds your project home, recursively, by looking for a Pipfile.
  - Automatically generates a Pipfile, if one doesn't exist.
  - Automatically generates a Pipfile.lock, if one doesn't exist.
  - Automatically creates a virtualenv in a standard location (project/.venv).
  - Automatically adds packages to a Pipfile when they are installed.
  - Automatically removes packages from a Pipfile when they are un-installed.
  - Also automatically updates pip.

**#2 (Michael):** [**Django 2.0 is dropping support for legacy Python**](https://news.ycombinator.com/item?id=13433927)

- Django changing docs to default to Python 3
- The next release, Django 1.11, will be a long-term support release, and the one after that, Django 2.0, will no longer support Python 2.

**#3 (Brian)** [**attrs**](https://attrs.readthedocs.io/en/stable/overview.html)

- Hynek Schlawack
- pypi: [https://pypi.python.org/pypi/attrs](https://home-assistant.io/demo/)
- readthedocs: [https://attrs.readthedocs.io/en/stable/overview.html](https://home-assistant.io/demo/)
- I know this has been around for a while. But I’ve just stumbled across it while reading a [blog post about requests](http://www.coglib.com/~icordasc/blog/2017/01/some-better-practices-for-using-requests-in-api-clients.html), which was good, but we’ve covered requests a lot lately, so I’m gonna skip that article today.
- pip install attrs, with an s, even though you import without the s
- Does all of the grunt work of writing dunder functions for you so you can write classes with a small amount of code that behave like classes and objects should. Especially if you come from a C++ background, this makes writing classes more intuitive.

**#4 (Michael):** [**Go faster Python**](https://alimanfoo.github.io/2017/01/23/go-faster-python.html)

- This blog post gives an introduction to some techniques for benchmarking, profiling and optimising Python code.
-  If you have a Python program that’s running slowly, what are your options?
  - Benchmarking and profiling
    - Our intuition is often wrong
  - Benchmarking: %time, %timeit, timeit
  - Function profiling: %prun, cProfile
  - Line profiling: %lprun, line_profiler (requires  [line_profiler](https://github.com/rkern/line_profiler))
  - Cython

**#5 (Brian):** **Getting Python 3 into distributions**

- Not an article but a couple of pleas.
- Many OS distributions, including Red Hat, ship with Python 2.7.
- Many developers don’t have the authority to install Python 3.x for projects.
- Two pleas:
  - distributions: ship with both if you have to, but let 3.6  be an option for people.
  - companies: install Python 3.6 and let some projects use that
- We can’t just encourage users to switch to Python 3 if it’s not their choice.


**#6 (Michael)** [**Home Assistant**](https://home-assistant.io/)

- Home Assistant is an open-source home automation platform running on Python 3. 
  - Track and control all devices at home and automate control
  - Installation in less than a minute.
  - Observe: Track the state of all the devices in your home, so you don't have to.
  - Control: All your devices from a single, mobile-friendly, interface.
  - Automate: Setup advanced rules to control devices and bring your home alive.
    - have the lights turn on when the sun sets and you are home?
    - have the lights turn on when anyone comes home and it is dark?
    - dim the lights when you start watching a movie on your Chromecast?
    - receive a message when the lights turn on while you are not at home?
- Demo: [https://home-assistant.io/demo/](https://home-assistant.io/demo/)
- [aiohttp](https://aiohttp.readthedocs.io/en/stable/): Asynchronous HTTP Client/Server
