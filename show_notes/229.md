# Python Bytes 229

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guests: 

- [**Gwendolyn Faraday**](https://twitter.com/gwen_faraday)
- Gwendolyn’s **[YouTube](https://www.youtube.com/channel/UCxA99Yr6P_tZF9_BgtMGAWA)**

**Brian #1:** [**Coverage.py**](https://nedbatchelder.com/blog/202104/coveragepy_and_thirdparty_code.html) [**(5.6b1)**](https://nedbatchelder.com/blog/202104/coveragepy_and_thirdparty_code.html) [**and third-party code**](https://nedbatchelder.com/blog/202104/coveragepy_and_thirdparty_code.html)

- Problems
	- If you put your virtual environment in the same directory as your code, and try to run coverage, it’s tricky to get coverage to not attempt to cover everything in your venv also.
	- Or even just running `coverage run -m pytest` with no `--source` specified, it just kinda reports on everything, even stuff in `site-packages`, not just your code.
- Solution
	- `pip install coverage==5.6b1`
	- As of 5.6b1, coverage knows where third party code is and doesn’t measure it.
- Super awesome
- Also, it’s still beta. Net wants help testing it out and making sure it works right.
- I’m curious if it still works right with pytest plugins and such, so I’ll be testing a bunch of stuff to make sure it still makes sense.  

**Michael #2:** [**So you want your own PaaS? Piku!**](https://github.com/piku/piku)

- via Ian Mauer
- The tiniest PaaS you've ever seen. 
- Piku allows you to do git push deployments to your own servers. 
- Allows you do `git push` deployments to your own servers.
- Motivation: I kept finding myself wanting an Heroku/CloudFoundry-like way to deploy stuff on a few remote ARM boards and [my Raspberry Pi cluster](https://github.com/rcarmo/raspi-cluster)
- **Core values**
	- Runs on low end devices.
	- Accessible to hobbyists and K-12 schools.
	- ~1,000 lines readable code.
	- Functional code style.
	- Few (single?) dependencies
	- [12 factor app](https://12factor.net).
	- Simplify user experience.
	- Cover 80% of common use cases.
	- Sensible defaults.
	- Leverage distro packages in Raspbian/Debian/Ubuntu (Alpine and RHEL support is WIP)
	- Leverage standard tooling (`git`, `ssh`, `uwsgi`, `nginx`).
	- Preserve backwards compatibility where possible

**Gwen #3:** ****

- Web3.py - Library for building Dapps in Python with Ethereum
	- Need to connect to a blockchain service (e.g. BlockCypher) or [run your own locally](https://www.trufflesuite.com/docs/ganache/overview)
- Can create contracts and interact with them or get general blockchain information in Python
- [Vyper](https://vyper.readthedocs.io/en/stable/) is a pythonic language for the blockchain that can be used for smart contracts

**Brian #4:** [**Deadpendency**](https://deadpendency.com/)

- Suggested by Johannes Lippmann
- In [episode 277](https://pythonbytes.fm/episodes/show/227/no-more-awaiting-async-comes-to-sqlalchemy) we talked about the Snyk (Python) Package Advisor which tells us how healthy a python package is.
- [Deadpendency](https://deadpendency.com/) is a similar thing, but tells you about the health of the packages you depend on. It’s a GitHub app that runs on PRs and commits.
- Let’s say someone has a PR that adds a dependency. The PR checks will include a health check of the new dependency. 
- What’s more, on each commit or PR, all of your dependencies will be checked.
- Checks for:
	- no recent releases (warn at 18 months, fail at 24 months)
	- no recent commits (warn at 12 months, fail at 18 months)
	- few yearly commits (warn at 2)
	- archived repository (fail)
	- repository is a fork (warn)
	- package deprecated (fail)
	- single recent author (warn)
- Everything is configurable
- Temporary problems:
	- only supports requirements.txt and Pipfile, for Python
	- Kinda need it to support pyproject.toml, maybe setup.py
	- I’d like to be able to just run this on a project without having to have a commit or push trigger it, to try it out. I’ve got some CI tools that allow that. Maybe it’s common for them to not. not sure.
- Also be neat if:
	- it did the snyk checks for at least security and  maintenance on the dependency. Not just release and commit frequency.
- Bottom line: 
	- Neat idea. Waiting for support for pyproject.toml

**Michael #5:** [**All The Important Features and Changes in Python 3.10**](https://martinheinz.dev/blog/46)

- Python 3.10 beta is coming soon. What will be in it?
	- or install here: [https://www.python.org/downloads/release/python-3100a6/](https://www.python.org/downloads/release/python-3100a6/)
- Under Installing Alpha/Beta Version it has the steps to build from source. I strongly recommend replacing `make install` with `make altinstall`.
- Lots of comments and examples of pattern matching (aka switch).
- Type Checking Improvements
- 
```
    # Function that accepts either `int` or `float`
    # Old:
    def func(value: Union[int, float]) -> Union[int, float]:
        return value
```

``` 
    # New:
    def func(value: int | float) -> int | float:
        return value
```

- Type Aliases Syntax Change: `FileName = str` → `FileName: TypeAlias = str`
- distutils Are Being Deprecated (deprecated in 3.10 and will be removed in 3.12). This package has been replaced by `setuptools` and `packaging` for a while now.
- Parenthesized context managers to span multiple lines

```
    with (
        open("somefile.txt") as some_file,
        open("otherfile.txt") as other_file,
    ):
        ...
```

**Gwen #6:**: **freeCodeCamp’s Python Curriculum**

- Thousands of hours of Curriculum
	- Python basics
	- Data Science
	- Machine Learning
	- Algorithms
	- Projects
	- Certifications
- YouTube supplementary material with 100s of hours of Python
- Quincy Larsen and the team worked on this for years and launched last year.
- [New Data Science and ML curriculum](https://www.freecodecamp.org/news/building-a-data-science-curriculum-with-advanced-math-and-machine-learning/) coming soon…
    
**Extras**

**Michael**

- [**Microsoft unveils its own Java distribution**](https://www.arnnet.com.au/article/687438/microsoft-unveils-its-own-java-distribution/): Microsoft Build of OpenJDK could set up the vendor to compete with Oracle in the Java distribution space, for Windows, Linux, and MacOS.
- [**PyCharm 2021.1**](https://blog.jetbrains.com/pycharm/2021/04/pycharm-2021-1/)
- [**Beanie ODM now has migrations**](https://twitter.com/roman_the_right/status/1382344202839859201)!

**Gwen**

- [Mem.dev](https://mem.dev/): For developers to use spaced-repetition learning to learn concepts and syntax.
- [Graphene Django](https://docs.graphene-python.org/projects/django/en/latest/): Testing it out to replace DRF for future development projects.
