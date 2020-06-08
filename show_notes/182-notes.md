# Python Bytes 182: PSF Survey is out!

Sponsored by Datadog

**Michael #1:** [**PSF / JetBrains Survey**](https://www.jetbrains.com/lp/python-developers-survey-2019/)

- via Jose Nario
- Let’s talk results:
- 84% of people who use Python do so as their primary language [unchanged]
- Other languages: JavaScript (down), Bash (down), HTML (down), C++ (down)
- Web vs Data Science languages:
	- More C++ / Java / R / C# on Data Science side
	- More  SQL / JavaScript / HTML
- Why do you mainly use Python? 58% work and personal
- What do you use Python for?
	- Average answers was 3.9
	- Data analysis [59% / 59% — now vs. last year]
	- Web Development [51% / 55%]
	- ML [40% / 39%]
	- DevOps [39% / 43%]
- What do you use Python for the most?
	- Web [28% / 29%]
	- Data analysis [18% / 17%]
	- Machine Learning [13% / 11%]
- Python 3 vs Python 2: 90% Python 3, 10% Python 2
- Widest disparity of versions (pro 3) is in data science.
- Web Frameworks:
	- Flask [48%]
	- Django [44%]
- Data Science
	- NumPy 63%
	- Pandas 55%
	- Matplotlib 46%
- Testing
	- pytest 49%
	- unittest 30%
	- none 34%
- Cloud
	- AWS 55%
	- Google 33%
	- DigitalOcean 22%
	- Heroku 20%
	- Azure 19%
- How do you run code in the cloud (in the production environment)
	- Containers 47%
	- VMs 46%
	- PAAS 25%
- Editors
	- PyCharm 33%
	- VS Code 24%
	- Vim 9%
- tool use
	- version control 90%
	- write tests 80%
	- code linting 80%
	- use type hints 65%
	- code coverage 52%

**Brian #2:** **Hypermodern Python**

-  Claudio Jolowicz, [@cjolowicz](https://twitter.com/cjolowicz/)
- An opinionated and fun tour of Python development practices.
- [Chapter 1: Setup](https://cjolowicz.github.io/posts/hypermodern-python-01-setup)
	- Setup a project with pyenv and Poetry, src layout, virtual environments, dependency management, click for CLI, using requests for a REST API.
- [Chapter 2: Testing](https://cjolowicz.github.io/posts/hypermodern-python-02-testing)
	- Unit testing with pytest, using coverage.py, nox for automation, pytest-mock. Plus refactoring, handling exceptions, fakes, end-to-end testing opinions.
- [Chapter 3: Linting](https://cjolowicz.github.io/posts/hypermodern-python-03-linting)
	- Flake8, Black, import-order, bugbear, bandit, Safety. Plus  more on managing dependencies, and using pre-commit for git hooks.
- [Chapter 4: Typing](https://cjolowicz.github.io/posts/hypermodern-python-04-typing)
	- mypy and pytype, adding annotations, data validation with Desert & Marshmallow, Typeguard, flake8-annotations, adding checks to test suite
- [Chapter 5: Documentation](https://cjolowicz.github.io/posts/hypermodern-python-05-documentation)
	- docstrings, linting docstrings, docstrings in nox sessions and test suites, darglint, xdoctest, Sphinx, reStructuredText, and autodoc
- [Chapter 6: CI/CD](https://cjolowicz.github.io/posts/hypermodern-python-06-ci-cd) 
	- CI with GithHub Actions, reporting coverage with Codecov, uploading to PyPI, Release Drafter for release documentation, single-sourcing the package version, using TestPyPI, docs  on RTD
- The series is worth it even for just the artwork.
- Lots of fun tools to try, lots to learn.

**Michael #3:** [**Open AI Jukebox**](https://openai.com/blog/jukebox/)

- via Dan Bader
- Listen to the songs under “Curated samples.”
- A neural net that generates music, including rudimentary singing, as raw audio in a variety of genres and artist styles. 
- Code is available on [github](https://github.com/openai/jukebox/).
- Dataset: To train this model, we crawled the web to curate a new dataset of 1.2 million songs (600,000 of which are in English), paired with the corresponding lyrics and metadata from [LyricWiki](https://lyrics.fandom.com/wiki/LyricWiki).
- The top-level transformer is trained on the task of predicting compressed audio tokens. We can provide additional information, such as the artist and genre for each song. 
- Two advantages: first, it reduces the entropy of the audio prediction, so the model is able to achieve better quality in any particular style; second, at generation time, we are able to steer the model to generate in a style of our choosing.


**Brian #4:** [**The Curious Case of Python's Context Manager**](https://rednafi.github.io/digressions/python/2020/03/26/python-contextmanager.html)

- Redowan Delowar, [@rednafi](https://twitter.com/rednafi)
- A quick tour of context managers that goes deeper than most introducitons.
- Writing custom context managers with `__init__`, `__enter__`, `__exit__`.
- Using the decorator `contextlib.contextmanager`
- Then it gets even more fun
	- Context managers as decorators
	- Nesting contexts within one `with` statement.
	- Combining context managers into new ones
- Examples
	- Context managers for SQLAlchemy sessions
	- Context managers for exception handling
	- Persistent parameters across http requests

**Michael #5:** [**nbstripout**](https://pypi.org/project/nbstripout/)

- via Clément Robert
- In the latest episode, you praised NBDev for having a git hook that strips out notebook outputs.
- strip output from Jupyter and IPython notebooks
- Opens a notebook, strips its output, and writes the outputless version to the original file.
- Useful mainly as a git filter or pre-commit hook for users who don’t want to track output in VCS.
- This does mostly the same thing as the Clear All Output command in the notebook UI.
- Has a nice youtube tutorial right in the pypi listing
- Just do `nbstripout` `--``install` in a git repo!

**Brian #6:** **Write ups for** [**The 2020 Python Language Summit**](http://pyfound.blogspot.com/2020/04/the-2020-python-language-summit.html)

- Guido talked about this in [episode 179](https://pythonbytes.fm/episodes/show/179/guido-van-rossum-drops-in-on-python-bytes)
- But these write-ups are excellent and really interesting.
	- [**Should All Strings Become f-strings?**](https://pyfound.blogspot.com/2020/04/all-strings-become-f-strings-python.html), Eric V. Smith
	- [**Replacing CPython’s Parser with a PEG-based parser**](https://pyfound.blogspot.com/2020/04/replacing-cpythons-parser-python.html), Pablo Galindo, Lysandros Nikolaou, Guido van Rossum
	- [**A Formal Specification for the (C)Python Virtual Machine**](https://pyfound.blogspot.com/2020/04/a-formal-specification-for-cpython.html), Mark Shannon
	- [**HPy: a Future-Proof Way of Extending Python?**](https://pyfound.blogspot.com/2020/04/hpy-future-proof-way-of-extending.html), Antonio Cuni
	- [**CPython Documentation: The Next 5 Years**](https://pyfound.blogspot.com/2020/04/cpython-documentation-next-5-years.html), Carol Willing, Ned Batchelder
	- [**Lightning talks (pre-selected)**](https://pyfound.blogspot.com/2020/04/lightning-talks-part-1.html)
		- What do you need from pip, PyPI, and packaging?, Sumana Harihareswara
		- A Retrospective on My "Multi-Core Python" Project, Eric Snow
	- [**The Path Forward for Typing,**](https://pyfound.blogspot.com/2020/04/the-path-forward-for-typing-python.html) Guido van Rossum
	- [**Property-Based Testing for Python Builtins and the Standard Library,**](https://pyfound.blogspot.com/2020/05/property-based-testing-for-python.html) Zac Hatfield-Dodds
	- [**Core Workflow Updates,**](https://pyfound.blogspot.com/2020/05/core-workflow-updates-python-language.html) Mariatta Wijaya
	- [**CPython on Mobile Platforms,**](https://pyfound.blogspot.com/2020/05/cpython-on-mobile-platforms.html) Russell Keith-Magee
- Wanted to bring this up because Python is a living language and it’s important to pay attention and get involved, or at least pay attention to where Python might be going.

Also, another way to get involved is to become a member of the PSF board of directors

- [What’s a PSF board of directors member do? video](https://www.youtube.com/watch?v=ZLKj6FaQA4M)
- There are some open seats, [Nominations are open until May 31](https://www.python.org/nominations/elections/)
    

Extras:

Michael:

- Updated search engine for better result ranking
- Windel Bouwman wrote a nice little script for speedscope https://github.com/windelbouwman/pyspeedscope (follow up from Austin profiler)

Jokes:

- “Due to social distancing, I wonder how many projects are migrating to UDP and away from TLS to avoid all the handshakes?” - From [Sviatoslav Sydorenko](https://twitter.com/webKnjaZ) 
- “A chef and a vagrant walk into a bar.  Within a few seconds, it was identical to the last bar they went to.” - From [Benjamin Jones](https://twitter.com/bluefiddleguy), crediting [@lufcraft](https://twitter.com/luvcraft)
- Understanding both of these jokes is left as an exercise for the reader.



