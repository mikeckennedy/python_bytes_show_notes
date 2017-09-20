# Python Bytes 44
This episode is brought to you by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Michael #1:** [**Ten Malicious Libraries Found on PyPI**](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/)

- Code packages available in PyPI contained modified installation scripts.
- Vulnerabilities were introduced into the setup.py execution of packages for approximately 20 packages on PyPI
- Package names that closely resembled those used for packages found in the standard Python library (e.g. `urlib` vs `urllib`)
- The packages contained the exact same code as the upstream libraries except for an installation script.
- Officials with the Slovak authority said they recently notified PyPI administrators of the activity, and all identified packages were taken down immediately. Removal of the infected libraries, however, does nothing to purge them from servers that installed them.
- From PSF: *Unlike some language package management systems, PyPI does not have any full time staff devoted to it. It is a volunteer run project with only two active administrators. As such, it doesn't currently have resources for some of the proposed solutions such as actively monitoring or approving every new project published to PyPI. Historically and by necessity we've relied on a reactive strategy of taking down potentially malicious projects as we've become aware of them.*
- Comments
	  - [pip gets more paranoid in the install process](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/?comments=1&post=33997861)
	  - [Downloads were not super bad](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/?comments=1&post=34000031)
	  - [Stestagg is sitting on lots of misspellings](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/?comments=1&post=33999957)
	  -[Undergrad thesis compromised Ruby and NodeJS too](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository/?comments=1&post=33999819)
- related: 
	  - original warning: http://www.nbu.gov.sk/skcsirt-sa-20170909-pypi/
	  - stdlib names no longer allowed: https://github.com/pypa/warehouse/pull/2409

**Brian #2: PyPI migration to Warehouse is in progress**

- Thanks to Jonas Neubert for researching this topic and writing a blog post titled [Publishing your First PyPI Package by/for the Absolute Beginner](https://jonemo.github.io/neubertify/2017/09/13/publishing-your-first-pypi-package/)
- The steps to publish to PyPI have changed with the move to warehouse and pypi.org.
- [pypi.org](http://pypi.org/) is no longer in read-only mode, it is where you publish packages
- The old APIs at [pypi.python.org/pypi](http://pypi.python.org/pypi) are disabled, if you have a .pypirc file you'll have to update the URLs
- You no longer need to register package names before first uploading, the project gets created on the fly during the first upload of the package.
- The best way to update anything in a package is to change your local package and upload it again, see https://github.com/pypa/warehouse/issues/2170. 
  - This includes even just changes to the description.
  - Manual file upload is gone.
- As of right now it looks like you still need to register through pypi.python.org, then do the rest of the interactions with pypi.org. See https://github.com/pypa/warehouse/issues/2065
- Markdown support for package descriptions, like README.md seems to be coming: https://packaging.python.org/specifications/#description-content-type
- Jonas’ [blog post](https://jonemo.github.io/neubertify/2017/09/13/publishing-your-first-pypi-package/) is from 13 Sep 2017, so it might be the most up to date tutorial on all the steps to get a package onto PyPI.

**Brian #3:** **Live coding in a presentation**

- Last week’s discussion of [David Beazley’s Fun of Reinvention talk](https://www.youtube.com/watch?v=js_0wjzuMfc) got me thinking about doing live coding during a presentation since he did it so well.
- Several links regarding how to do various levels of live coding:
	  - Advice for live coding: [https://code.tutsplus.com/articles/the-holy-grail-of-conference-talks-live-coding--net-30217](https://code.tutsplus.com/articles/the-holy-grail-of-conference-talks-live-coding--net-30217)
	  - Not quite live coding: [https://vanslaars.io/post/not-quite-live-coding/](https://vanslaars.io/post/not-quite-live-coding/)
	  - Avoiding live coding: [https://codeplanet.io/techniques-avoid-live-coding-part/](https://codeplanet.io/techniques-avoid-live-coding-part/)
- Live coding:
	  - practice, have a backup plan, don’t forget to talk, plan content
- not quite: 
	  - use git tags
- avoiding it:
	  - My favorite effect is fade-in slideshows where part of the code is shown at a time so you can talk about it and people know which bit to look at

**Michael #4: Notable REST / Web Frameworks**

- **Falcon: [https://falconframework.org/](https://falconframework.org/)**
  - Unburdening APIs for over 4.70 x 10-2 centuries. (4.7 years)
    - Falcon is a bare-metal Python web API framework for building very fast app backends and microservices.
    - **Complementary:** Falcon complements more general Python web frameworks by providing bare-metal performance and flexibility wherever you need it.
    - **Compatible**: Thanks to WSGI, Falcon runs on a large variety of web servers and platforms. Falcon works great with CPython 2.6, 2.7, and 3.3+. Try PyPy for an extra speed boost.
  
- **Hug: [http://hug.rest](http://hug.rest)**
  - Drastically simplify API development over multiple interfaces. 
  - With hug, design and develop your API once, then expose it however your clients need to consume it. Be it locally, over HTTP, or through the command line.
  - Built-in documentation


**Brian #5:** **Tox**

- “The name of the [tox automation project](https://pypi.python.org/pypi/tox) derives from "testing out of the box". It aims to "automate and standardize testing in Python". Conceptually it is one level above pytest and serves as a command line frontend for running tests and automate all kinds of tasks around the project. It also acts as a frontend for [Continuous Integration Systems](https://en.wikipedia.org/wiki/Continuous_integration) to unify what you do locally and what happens in e.g. Jenkins or Travis CI.” - Oliver Bestweller
- a small tox.ini file:
    [tox]
    envlist = py27,py35, py36
    [testenv]
    deps=pytest 
    commands=pytest
- You place this in your package source directory and then run tox, which will:
  - Use setup.py to create a sdist
  - create a virtual environment for each environment in envlist
  - Install dependencies in the environments
  - Install your package into the environment
  - Run the tests
  - Do this for multiple environments, so multiple Python versions (as an example)
- Much more powerful than that, but that’s how many people use it.
- Further Reading:
  - [http://tox.readthedocs.io/en/latest/index.html](http://tox.readthedocs.io/en/latest/index.html)
  - [http://tox.readthedocs.io/en/latest/example/basic.html](http://tox.readthedocs.io/en/latest/example/basic.html) 
  - [https://blog.ionelmc.ro/2015/04/14/tox-tricks-and-patterns/](https://blog.ionelmc.ro/2015/04/14/tox-tricks-and-patterns/)


**Michael #6: flake8-tidy-imports** [**deprecated imports**](https://pypi.python.org/pypi/flake8-tidy-imports#options)

- You can declare {python2to3} as a banned-module import, and it will check against a long list of import moves and removals between python 2 and python 3, suggesting relevant replacements if available. 
- I meticulously compiled this list by reading release notes from Python 3.0-3.6 as well as testing in a large legacy python codebase, but I presumably missed a few.
- Example:
    flake8 file.py
    file.py:1:1: I201 Banned import 'mock' used - use unittest.mock instead.

**Michael #7 (bonus!):** [**Help Me Offer Coaching to First-Time PyGotham Speakers**](https://emptysqua.re/blog/coaching-for-first-time-pygotham-speakers/)

- Via A. Jesse Jiru Davis
- I want to raise $1200 for public-speaking coaching for first-time speakers at PyGotham, the New York City Python conference. Will you chip in?
- Jesse is a PyGotham conference organizer, but I’m launching this fundraiser independently of PyGotham.
- As of September 19, I have raised my goal. Thanks to everyone who donated!
## Our news

**Michael**: 

- Finished writing my **free MongoDB course** (subscribe to get notified of release at **https://training.talkpython.fm/getnotified** )
- [**python-switch**](https://github.com/mikeckennedy/python-switch) kind of went off the hook (see [this](https://github.com/mikeckennedy/python-switch) and [that](https://www.reddit.com/r/Python/comments/70413x/adding_a_switch_statement_to_python/))

**Brian**: 

- Book is shipping: [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)

