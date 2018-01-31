# Python Bytes 62
Brought to you by Datadog [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Brian #1:** **Dan Bader takes over Real Python**

- [Announcement email](https://mailchi.mp/realpython/final-blast?e=a41501fde5), with what Michael, Fletcher, and Jeremy are doing now
- Dan is on the show and tells us all about it.

**Michael #2: Still more Python GUIs**

- **[https://github.com/wooey/Wooey](https://github.com/wooey/Wooey)**
	  - A Django app that creates automatic web UIs for Python scripts.
	  - Wooey is a simple web interface to run command line Python scripts. Think of it as an easy way to get your scripts up on the web for routine data analysis, file processing, or anything else.
	  - Wooey was envisioned as a system to allow data analysts to be able to easily:
	    - Autodocument workflows for data analysis  (simple model saving).
	    - Enable fellow co-workers with no command line experience to utilize python scripts.
	    - Enable the easy wrapping of any program in simple python instead of having to use language specific  to existing tools such as Galaxy.
	  - Try the demo server: [https://wooey.herokuapp.com/](https://wooey.herokuapp.com/)
- **[https://github.com/chriskiehl/Gooey](https://github.com/chriskiehl/Gooey)**
	- Turn (almost) any Python command line program into a full GUI application with one line
	- See the [**screenshots here**](https://github.com/chriskiehl/Gooey)
	- Gooey converts your Console Applications into end-user-friendly GUI applications. 
	- It lets you focus on building robust, configurable programs in a familiar way, all without having to worry about how it will be presented to and interacted with by your average user.
- And Toga: [https://pybee.org/project/projects/libraries/toga/](https://pybee.org/project/projects/libraries/toga/)

**Brian #3:** [**Python’s misleading readability**](https://nedbatchelder.com//blog/201801/pythons_misleading_readability.html)

- Ned Batchelder
- `is` and `or` are not obvious and can confuse people new to the language, new to programming.
  -  `1000 + 1 is 1001`  → `1000 + 1 == 1001`
  - `answer == "y" or "yes``"` → `answer in {"y", "yes"}`

**Michael #4:** [**warp2 access**](https://haarcuba.github.io/warp2/) 

- python2 code from python3
- It communicates with the subprocess using pickle, so there are limitation to using it - if you need to send unpicklable data, that’s a problem.

**Brian #5:** **Help! My tests can’t see my code!**

- Probably should be an episode on [Test & Code](http://testandcode.com/), and maybe I’ll do that also, but it’s a big enough roadblock to many newcomers to [pytest](http://amzn.to/2DBLFCz), that I want to get the word out on how to fix it.
- A best practice is to put your test code in a folder called tests.
- Now, if you are sitting in the parent directory, where you can see both your modules/packages under test and the `tests` directory, and you run `pytest`, your test code has to have some way to import the code under test.
- If you are in a hurry. Homework due in an hour, project manager breathing down your neck, or whatever, then there are two easy options:
  - `python -m pytest`
    - `python` adds the current directory where you start it to `PYTHONPATH`, `pytest` does not.
  - `pip install pytest-pythonpath`
    - [https://pypi.python.org/pypi/pytest-pythonpath](https://pypi.python.org/pypi/pytest-pythonpath)
    - This plugin adds the current directory to `PYTHONPATH`, and adds some hooks that let you define search paths in your `pytest.ini` file.
- When you have time..
  - Create a `setup.py` file for your code. And…
  - `pip install -e ./your_project`
    - This allows you to continue working on your code while letting your test code see the code under test
  - This method is friendlier to `tox`.


**Michael #6:** [**Cement - Framework for CLI**](https://cement.readthedocs.io/en/latest/)

- Cement is an advanced CLI Application Framework for Python. 
- Its goal is to introduce a standard, and feature-full platform for both simple and complex command line applications 
- Also supports rapid development needs without sacrificing quality.
- Core features
  - Core pieces of the framework are customizable via handlers/interfaces
  - Extension handler interface to easily extend framework functionality
  - Config handler supports parsing multiple config files into one config
  - Argument handler parses command line arguments and merges with config
  - Log handler supports console and file logging
  - Plugin handler provides an interface to easily extend your application
  - Hook support adds a bit of magic to apps and also ties into framework
  - Handler system connects implementation classes with Interfaces
  - Output handler interface renders return dictionaries to console
  - Cache handler interface adds caching support for improved performance

Our news

Michael

- Conferences!
  - PyCascades in Vancouver BC on Jan 22, 23. Was great, get to it next year.
  - [PyColumbia](https://www.pycon.co/), February 9, 10 and 11 Medellin, Colombia - I won't be there but if you are able to make it get your tickets
  - PyCon Slovakia, March 9-11 in Bratislava. I'll be speaking there and doing a workshop. 
  - pycon us: Cleveland OH May 10th. I just finalized all my travel plans. I hope to see you there, please stop by our booth.
  - PyCarribian: Santo Domingo, Dominican Republic, 17-18 February, 2018
- Podcast [http://pythonoutloud.com/](http://pythonoutloud.com/)

