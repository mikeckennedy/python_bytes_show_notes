# Python Bytes 143
Special guest: [**Kelly Schuster-Paredes**](https://twitter.com/kellypared)

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Keynote: Python 2020 - Łukasz Langa - PyLondinium19**](https://www.youtube.com/watch?v=KDXhu4rxTNY)

- Enabling Python on new platforms is important.
- Python needs to expand further than just CPython.
    - Web, 3D games, system orchestration, mobile, all have other languages that are more used. Perhaps it’s because the full Python language, like CPython in full is more than is needed, and a limited language is necessary.
- MicroPython and CircuitPython are successful.
    - They are limited implementations of Python
- Łukasz talks about many parts of Python that could probably be trimmed to make targeted platforms very usable without losing too much. 
- It’d be great if more projects tried to implement Python versions for other platforms, even if the Python implementation is limited.

**Kelly #2**: **[Mu Editor](https://codewith.mu/)**
- by [Nicholas Tollervey](https://twitter.com/ntoll)
- Lots of updates happening to the Code with Mu software
- Mu is a Python code editor for beginner programmers
	- originally created as a contribution from the [Python Software Foundation](http://python.org/psf) for the BBC’s [micro:bit project](http://microbit.org/)
- Code with Mu presented at EuroPython and shared a lot of interesting updates and things in the alpha version of Mu, [available on code with Mu](https://codewith.mu/en/download) website.
-  Mu is a modal editor:
	- BBC Microbit
	- Circuit Python
	- ESP Micropython
	- Pygame Zero
	- Python 3
		- Tiago Monte’s recorded presentation at EuroPython
		- Game with Turtle
	- Flask — [release notes](https://madewith.mu/mu/users/2019/07/05/alpha2.html)
- [Made with Mu at EuroPython](https://madewith.mu/mu/users/2019/07/19/europython.html) videos
- Hot off the press: Nick just released [Pypercard](https://pypercard.readthedocs.io/en/latest/) a [HyperCard inspired](https://www.youtube.com/watch?v=CIUQvp2Pnpk) GUI framework for BEGINNER developers in Python based off of [Adafruit’s release](https://blog.adafruit.com/2019/06/18/apples-hypercard-history-and-a-possible-remake-hypercard-iot-internetofthings-circuitpython-adafruit/). 
	- It is a “PyperCard is a [HyperCard](https://en.wikipedia.org/wiki/HyperCard) inspired [Pythonic](https://www.python.org/dev/peps/pep-0020/) and deliberately constrained [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) framework for beginner programmers.
	- linked repos on [GitHub](https://github.com/ntoll/pypercard).
	- module re-uses the JSON specification used to create HyperCard
	- The concept allows user to “create Hypercard like stacks of states” to allow beginner coders to create choose their own adventure games. 

**Michael #3**: [**Understanding the Python Traceback**](https://realpython.com/python-traceback/)

-  by [Chad Hansen](https://realpython.com/python-traceback/#author)
- The Python traceback has a wealth of information that can help you diagnose and fix the reason for the exception being raised in your code.
- What do we learn right away?
	- The type of error
	- A description of the error (hopefully, sometimes)
	- The line of code the error occurred on
	- The call stack (filenames, line numbers, and module names)
	- If the error happened while handling another error
- Read from bottom to top — that was weird to me
- Most common error?  AttributeError: 'NoneType' object has no attribute 'an_attribute'
- Article talks about other common errors
- Are you creating custom exceptions to make your packages more useful?

**Brian #4:** **My oh my,**  [**flake8-mypy**](https://pypi.org/project/flake8-mypy/) **and** [**pytest-mypy**](https://pypi.org/project/pytest-mypy/)

- contributed by Ray Cote via email
- “For some reason, I continually have problems running mypy, getting it to look at the correct paths, etc. However, when I run it from flake8-mypy, I'm getting reasonable, actionable output that is helping me slowly type hint my code (and shake out a few bugs in the process). There's also a pytest-mypy, which I've not yet tried. “ - Ray
- [**flake8-mypy**](https://pypi.org/project/flake8-mypy/) ****
	- Maintained by Łukasz Langa
	- “The idea is to enable limited type checking as a linter inside editors and other tools that already support *Flake8* warning syntax and config.”
- [**pytest-mypy**](https://pypi.org/project/pytest-mypy/)
	- Maintained by Dan Bader and David Tucker
	- “Runs the mypy static type checker on your source files as part of your pytest test runs.”
		- Remind me to do a PR against the README to make pytest lowercase. 

**Kelly #5**: **[Lego Education and Spike](https://education.lego.com/en-us)**

- In March of this year, Lego Education gave news of a new robot being released since the EV3 released of Mindstorms in 2013. 
	- Currently the EV3 Mindstorm can be coded with Python and it is assumed that Spike Prime can be as well. 
- The current EV3 robots can currently be coded in python thanks to [Nigel Ward. He created a site back in 2016](https://sites.google.com/site/ev3devpython/about-this-site) or earlier; through a program called the EV3Dev project.
	- [ev3dev](https://www.ev3dev.org/) is a [Debian Linux](https://www.debian.org/)-based operating system 
- Until recently, Lego had not endorsed the use of Python or had they released documentation. 
	- Lego released a Getting started with EV3 MicroPython [59 page guide Version 1.0.0](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf)
	- EV3 MicroPython runs on top of ev3dev with a new Pybricks MicroPython runtime and library.
	- has its own Visual Studio Code extension
	- no need for terminal
	- Has instruction and lists of different features and classes used to program the PyBricks API- A python wrapper for the Databricks Rest API.
		- Pybricks is on [GitHub](https://github.com/emthomas/pybricks) from one contributor, [**Sebastien Thomas**](https://github.com/emthomas) **under MIT license**
		- [David Lechner](https://lechnology.com/), [Laurens Valk](https://github.com/laurensvalk), and [Anton Vanhoucke](https://github.com/antonvh) are contributors of the Lego MicroPython release.
- This opens up opportunities for students that compete in the First Lego League Competition to code in Python.
- [Example code for the Gyrobot](https://paper.dropbox.com/doc/Python-Bytes-143--AiSIBZ54IMRF_O0sW_~n_7hHAQ-YQpWORTHkAO3hGSnTHAHc)
    
**Michael #6:**  [**Python 3 at Mozilla**](https://ahal.ca/blog/2019/python-3-at-mozilla/)

- From January 2019.
- Mozilla uses a lot of Python.
- In mozilla-central there are over 3500 Python files (excluding third party files), comprising roughly 230k lines of code. 
- Additionally there are 462 repositories labelled with Python in the Mozilla org on Github
- That’s a lot of Python, and most of it is **Python 2**.
- But before tackling those questions, I want to address another one that often comes up right off the bat: Do we need to be 100% migrated by Python 2’s EOL?
- No. But punting the migration into the indefinite future would be a big mistake:
	- Python 2 will no longer receive security fixes.
	- All of the third party packages we rely on (and there are a lot of them) will also stop being supported
	- Delaying means more code to migrate
	- Opportunity cost: Python 3 was first released in 2008 and in that time there have been a huge number of features and improvements that are not available in Python 2.
- The best time to get serious about migrating to Python 3 was five years ago. The second best time is now.
- Moving to Python 3
- We stood up some linters. 
	- One linter that makes sure Python files can at least get imported in Python 3 without failing
	- One that makes sure Python 2 files use appropriate `__future__` statements to make migrating that file slightly easier in the future.
- Pipenv & poetry & [Jetty](https://github.com/ahal/jetty): a little experiment I’ve been building. It is a very thin wrapper around Poetry

**Extras**

Brian:

- [Python 3.8.0b3](https://www.python.org/downloads/release/python-380b3/)
	- “We strongly encourage maintainers of third-party Python projects to test with 3.8 during the beta phase and report issues …”

Michael:

-  pipx now has [**shell completions**](https://twitter.com/grassfedcode/status/1156756021995401221)

Kelly:

- [Teaching Python](https://www.teachingpython.fm/) podcast

**Jokes** 

- via Real Python and Nick Spirit
- Python private method → Joke [**cartoon image**](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5d01751678f28538bd992907/c2f6bf103b9e2b862c2f3d14dd7056b1/Dwn-TyOWkAI5YAm.jpg).

