# Python Bytes 168

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest: [**Kojo Idrissa**](https://twitter.com/transitionswpz)!

**Michael #1:** [**donkeycar**](https://github.com/autorope/donkeycar)

- Have you ever seen a [proper RC car race](https://www.youtube.com/watch?v=qhefnHZFouM)?
- Donkeycar is minimalist and modular self driving library for Python. 
- It is developed for hobbyists and students with a focus on allowing fast experimentation and easy community contributions.
- Use Donkey if you want to:
	- Make an RC car drive its self.
	- Compete in self driving races like DIY Robocars
	- Experiment with autopilots, mapping computer vision and neural networks.
	- Log sensor data (images, user inputs, sensor readings).
	- Drive your car via a web or game controller.
	- Leverage community contributed driving data.
	- Use existing CAD models for design upgrades.

**Brian #2:** [**RIP Pipenv: Tried Too Hard. Do what you need with pip-tools.**](https://medium.com/telnyx-engineering/rip-pipenv-tried-too-hard-do-what-you-need-with-pip-tools-d500edc161d4)

- Nick Timkovich
- No releases of pipenv in 2019. It “[has been held back](https://github.com/pypa/pipenv/issues/4058#issuecomment-565550646) by several subdependencies and a complicated release process”
- main benefits of pipenv: pin everything and use hashes for verifying packages
	- The two file concept (Pipfile Pipfile.lock) is pretty cool and useful
- But we can do that with `pip-tools` command line tool `pip-compile`, which is also used by pipenv:
	- `pip-compile --generate-hashes --ouptut-file requirements.txt requirements.in`
- What about virtual environment support?
	- `python -m venv venv --prompt $(basename $PWD)` or equivalent for your shell works fine, and it’s built in.

**Kojo #3:** [**str.casefold()**](https://docs.python.org/3/library/stdtypes.html?highlight=casefold#str.casefold)

- used for caseless matching
- “Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string.”
- especially helpful for Unicode characters

```
    firstString = "der Fluß"
    secondString = "der Fluss"
    
    # ß is equivalent to ss
    if firstString.casefold() == secondString.casefold():
        print('The strings are equal.')
    else:
        print('The strings are not equal.')
    
    # prints "The strings are equal."
```

**Michael #4:** [**Virtualenv**](https://discuss.python.org/t/virtualenv-20-0-0-beta1-is-available/3077)

- via Brian Skinn
- Virtualenv 20.0.0 beta1 is available
- Announcement by [Bernat Gabor](https://discuss.python.org/u/bernatgabor)
- Why the major release
- I identified three main pain points:
	- Creating a virtual environment is slow (takes around 3 seconds, even in offline mode; while 3 seconds does not seem that long if you need to create tens of virtual environments, it quickly adds up).
	- The API used within PEP-405 is excellent if you want to create virtual environments; however, only that. It does not allow us to describe the target environment flexibly or to do that without actually creating the environment.
	- The duality of virtualenv versus venv. Right, python3.4 has the venv module as defined by PEP-405. In theory, we could switch to that and forget virtualenv. However, it is not that simple. virtualenv offers a few benefits that venv does not
- Benefits over venv
	- Ability to discover alternate versions (`-p 2` creates a python 2 virtual environment, `-p 3.8` a python 3.8, `-p pypy3` a PyPy 3, and so on).
	- virtualenv packages out of the box the wheel package as part of the seed packages, this significantly improves package installation speed as pip can now use its wheel cache when installing packages.
	- You are guaranteed to work even when distributions decide not to ship venv (Debian derivates notably make venv an extra package, and not part of the core binary).
	- Can be upgraded out of band from the host python (often via just pip/curl - so can pull in bug fixes and improvements without needing to wait until the platform upgrades venv).
	- Easier to extend, e.g., we added Xonsh activation script generation without much pushback, support for PowerShell activation on POSIX platforms.

**Brian #5:** [**Property-based tests for the Python standard library (and builtins)**](https://github.com/Zac-HD/stdlib-property-tests)

- Zac Hatfield-Dodds and Paul Ganssle, so far.
- Goal: Find and fix bugs in Python, *before* they ship to users.
- “CPython's existing test suite is good, but bugs still slip through occasionally. We think that using property-based testing tools - i.e. [Hypothesis](https://hypothesis.readthedocs.io/) - can help with this. They're no magic bullet, but computer-assisted testing techniques routinely try inputs that humans wouldn't think of (or bother trying), and turn up bugs that humans missed.”
- “Writing tests that describe *every valid input* often leads to tighter validation and cleaner designs too, even when no counterexamples are found!”
- “We aim to have a compelling proof-of-concept by [PyCon US](https://us.pycon.org/2020/), and be running as part of the CPython CI suite by the end of the sprints.”
- Hypothesis and property based testing is superb to throw at algorithmic pure functions, and the test criteria is relatively straightforward for function pairs that have round trip logic, like tokenize/untokenize, encode/decode, compress/decompress, etc. And there’s probably tons of those types of methods in Python. 
- At the very least, I’m interested in this to watch how other people are using hypothesis.

**Kojo #6:** **PyCon US Tutorial Schedule & Registration**

- Find the schedule at [https://us.pycon.org/2020/schedule/tutorials/](https://us.pycon.org/2020/schedule/tutorials/)
- They tend to sell out FAST
- Videos are up fast afterwards
- What’s interesting to me?
	- Migration from Python 2 to 3
	- Welcome to Circuit Python (Kattni Rembor)
	- Intro to Property-Based Testing
	- Minimum Viable Documentation (Heidi Waterhouse)

Extras

Michael:

- [Foreword for Mastering Python Networking](https://www.amazon.com/gp/product/1839214678/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1839214678&linkCode=as2&tag=pythfornetwen-20&linkId=b188f06ab7c5017394c7b8d675cb9df3)
- Pyramid (Waitress) and Django both issued security CVEs. You should upgrade!
- [StackOverflow Survey 2020](https://stackoverflow.az1.qualtrics.com/jfe/form/SV_eL0mFVwuo7KWeXP?utm_source=pythonbytespodcast) is open. Go fill it out!

**Joke**

See the cartoon:

[https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5df14f77efb5642d017a593f/31cba5cdf0e9805d47837916555dd7ab/b5cb6570af72883f06c3dcbf47679e9d.jpg](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5df14f77efb5642d017a593f/31cba5cdf0e9805d47837916555dd7ab/b5cb6570af72883f06c3dcbf47679e9d.jpg) 

