# Python Bytes 80
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Packaging Python Projects**](https://packaging.python.org/tutorials/packaging-projects/)

- Tutorial on the PyPA has been updated.
- Includes `README.md` instead of `REAMDE.rst`
- Initial example of `setup.py` no longer too minimal or too scary.
- Discussion of using `twine` to upload to test.pypi.org/legacy before uploading to non-test pypi
- [Related project, flit](https://pypi.org/project/flit/)
[](https://pypi.org/project/flit/)

**Dan #2:** [gidgethub — An async library for calling GitHub’s API](https://gidgethub.readthedocs.io/en/latest/)
- Talk to GitHub API to add/modify issues, pull-requests, comments, …
- Also helpers to parse GitHub’s webhook events so you can write bots that react to new issues, comments, commits etc.
- Used it in @Mariatta’s GitHub Bot tutorial: https://github.com/Mariatta/github-bot-tutorial
- Cool architecture for a “modern” Python web API library (async, sansio, decorator based event callbacks)
	- supports different async backends: aiohttp, treq, Tornado
		- sans-I/O: “protocol implementations written in Python that perform **no** I/O (this means libraries that operate directly on text or bytes)”
		- Why? → “*reusability*. By implementing network protocols without any I/O and instead operating on bytes or text alone, libraries allow for reuse by other code regardless of their I/O decisions. In other words by leaving I/O out of the picture a network protocol library allows itself to be used by both synchronous and asynchronous I/O code”
- (Biggest issue in that workshop was getting everyone upgraded to Python 3.6…but more on that later)

**Michael #3:** [**Pysystemd**](https://twitter.com/aleivag/status/999470427012386816)

- Recall I recently build a Python-based systemd service for geo syncing my course materials
- A thin Cython-based wrapper on top of libsystemd, focused on exposing the dbus API via sd-bus in an automated and easy to consume way.
- By Alvaro Leiva, a production engineer at Facebook / Instagram
- [Presented at PyCon 2018](https://www.youtube.com/watch?v=ZUX9Fx8Rwzg)
- Systemd:
	- Manages your services and their lifetimes
	- e.g. I want my web app to start on boot but only after mongodb has started
- [PySystemd](https://github.com/facebookincubator/pystemd) lets you control and query these from a Python API

**Brian #4:** [**PyCharm 2018.2 EAP 1 includes improved pytest support**](https://blog.jetbrains.com/pycharm/2018/05/pycharm-2018-2-eap-1/)

- From [Bruno Oliveira](https://twitter.com/nicoddemus/status/999424505171849221)
	- “Oh my, full support for [~~#~~](https://twitter.com/hashtag/pytest?src=hash)[pytest](https://twitter.com/hashtag/pytest?src=hash) fixtures and parametrized tests coming in [~~@~~](https://twitter.com/pycharm)[pycharm](https://twitter.com/pycharm) 2018.2. “
- “PyCharm 2018.2 supports [using fixtures in Pytest](https://docs.pytest.org/en/latest/fixture.html). Using fixtures allows you to separate your setup code from the actual tests, making for more concise, and more readable tests. Additionally, there have been improvements to code navigation and refactoring Pytest tests, and to using parametrized tests.”
- It’s hard for me to fully express how FREAKING EXCITED I am about this.
- auto-complete now works with fixtures to test functions
- goto declaration now works with fixtures to test functions
  - (not fixtures of fixtures, but they know about that already)
- re-running a failed parametrization works (yay!)
- re-running a single parametrization works (yay!)

**Dan #5:**

- Why is installing Python 3.6 so hard? (Recent GitHub Bot workshop experience)
- Sometimes hard to tell what’s easy/difficult for beginners
- People hit crazy edge cases:
	- running Linux Subsystem for Windows (WSL) on Windows host, install Python into wrong environment
	- broken PPAs + bad StackOverflow advice → broken SSL and no pip on Ubuntu (deadsnakes PPA is the way to go)
	- People install multiple Python environments: Anaconda + python.org distribution
	- Hard to find instructions for compiling from source on Linux
- Shameless plug: https://realpython.com/installing-python/

**Michael #6:** [**30 amazing Python projects (2018 edition)**](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)
[](https://realpython.com/installing-python/)
- Mybridge AI evaluates the quality by considering popularity, engagement and recency. To give you an idea about the quality, the average number of Github stars is 3,707.
- [**No 30**](https://github.com/WZBSocialScienceCenter/pdftabextract?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** PDFTabExtract: A set of tools for extracting tables from PDF files helping to do data mining on scanned documents. 
- [**No 28**](https://github.com/NicolasHug/Surprise?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Surprise v1.0: A Python scikit for building and analyzing recommender systems 
- [**No 27**](https://github.com/ChrisKnott/Eel?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Eel: A little Python library for making simple Electron-like HTML/JS GUI apps 
- [**No 25**](https://github.com/anfederico/Clairvoyant?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Clairvoyant: A Python program that identifies and monitors historical cues for short term stock movement — Have you seen [The Wall Street Code - VPRO documentary](https://www.youtube.com/watch?v=kFQJNeQDDHA)?
- [**No 21**](https://github.com/Manisso/fsociety?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Fsociety: Hacking Tools Pack. A Penetration Testing Framework.
- [**No 18**](https://github.com/kennethreitz/maya?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Maya: Datetime for Humans in Python
- [**No 16**](https://github.com/Qix-/better-exceptions?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Better-exceptions: Pretty and useful exceptions in Python, automatically 
- [**No 13**](https://github.com/tomchristie/apistar?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Apistar: A fast and expressive API framework. For Python
- [**No 8**](https://github.com/micropython/micropython?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** MicroPython: A lean and efficient Python implementation for microcontrollers and constrained systems
- [**No 6**](https://github.com/explosion/spaCy?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** spaCy (v2.0): Industrial-strength Natural Language Processing (NLP) with Python and Cython
- [**No 2**](https://github.com/pytorch/pytorch?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Pytorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [**No 1**](https://github.com/home-assistant/home-assistant?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**:** Home-assistant (v0.6+): Open-source home automation platform running on Python 3

**Our news**

- Michael: Notable mention Cris’s GDPR writeup: [http://tryexceptpass.org/article/gdpr/](http://tryexceptpass.org/article/gdpr/) 
- Did you know about dropbox smart sync? [https://www.dropbox.com/smartsync](https://www.dropbox.com/smartsync)

