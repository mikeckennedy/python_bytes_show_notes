# Python Bytes 169

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**D-Tale**](https://pypi.org/project/dtale/)

- suggested by @davidouglasmit via twitter
- “D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures. It integrates seamlessly with ipython notebooks & python/ipython terminals. Currently this tool supports such Pandas objects as DataFrame, Series, MultiIndex, DatetimeIndex & RangeIndex.”
- way cool UI for visualizing data
- [Live Demo](http://andrewschonfeld.pythonanywhere.com/) shows
	- Describe shows column statistics, graph, and top 100 values
	- filter, correlations, charts, heat map

**Michael #2:** [**Carnets**](https://holzschu.github.io/Carnets_Jupyter/)

- by Nicolas Holzschuch
- A standalone Jupyter notebooks implementation for iOS.
- The power of Jupyter notebooks. In your pocket. Anywhere. Everything runs on your device. No need to setup a server, no need for an internet connection.
- Standard packages like Numpy, Matplotlib, Sympy and Pandas are already installed. You're ready to edit notebooks.
- Carnets uses iOS 11 filesharing ability. You can store your notebooks in iCloud, access them using other apps, share them.
- Extended keyboard on iPads, you get an extended toolbar with basic actions on your keyboard.
- Install more packages: Add more Python packages with %pip (if they are pure Python).
- OpenSource: Carnets is entirely OpenSource, and released under the FreeBSD license.

**Brian #3:** [**BeeWare Podium**](https://github.com/beeware/podium)

- suggested by Katie McLaughlin, @glasnt on twitter
- NOT a pip install, download a binary from https://github.com/beeware/podium/releases
- Linux and macOS
- Still early, so you gotta do the open and trust from the apps directory thing for running stuff not from the app store. But Oh man is it worth it.
- HTML5 based presentation frameworks are cool. run a presentation right in your browser. My favorite has been [remark.js](https://remarkjs.com/#1)
	- presenter mode, 
		- notes are especially useful while practicing a talk
		- running timer super helpful while giving a talk
	- write talk in markdown, so it’s super easy to version control
	- issues: 
		- presenter mode, full screen, with extended monitor hard to do.
		- notes and timer on laptop, full presentation on extended screen
	    - super cool but requires full screening with mouse 
- Podium 
	- uses similar syntax as remark.js and I think uses remark under the hood.
	- but it’s a native app, not a browser
	- Handles the presenter mode and extended screen smoothly, like keynote and others.
	- Removes the need for boilerplate html in your markdown file (remark.js md files have cruft).
- Can’t wait to try this out for my next presentation

**Michael #4:** [**pytest-mock-resources**](https://github.com/schireson/pytest-mock-resources/)

- via Daniel Cardin
- pytest fixture factories to make it easier to test against code that depends on external resources like Postgres, Redshift, and MongoDB.
- Code which depends on external resources such a databases (postgres, redshift, etc) can be difficult to write automated tests for. 
- Conventional wisdom might be to mock or stub out the actual database calls and assert that the code works correctly before/after the calls.
- Whether the actual query did the correct thing truly requires that you execute the query.
- Having tests depend upon a **real** postgres instance running somewhere is a pain, very fragile, and prone to issues across machines and test failures.
- Therefore `pytest-mock-resources` (primarily) works by managing the lifecycle of docker containers and providing access to them inside your tests.

**Brian #5:** [**How James Bennet is testing in 2020**](https://www.b-list.org/weblog/2020/feb/03/how-im-testing-2020/)

- Follow up from Testing Django applications in 2018
- Favors unittest over pytest. 
- tox for testing over multiple Django and Python versions, including tox-travis plugin 
- pyenv for local Python installation management and pyenv-virtualenv plugin for venvs.
- Custom `runtests.py` for setting up environment and running tests. 
- Changed to `src/` directory layout.
- Coverage and reporting failure if coverage dips, with a healthy perspective: “… this *isn’t* because I have 100% coverage as a goal. Achieving that is so easy in most projects that it’s meaningless as a way to measure quality. Instead, I use the coverage report as a canary. It’s a thing that shouldn’t change, and if it ever does change I want to know, because it will almost always mean something else has gone wrong, and the coverage report will give me some pointers for where to look as I start investigating.”
- Testing is more than tests, it’s also black, isort, flake8, mypy, and even spell checking sphinx documentation.
- Using tox.ini for utility scripts, like cleanup, pipupgrade, …

**Michael #6:** [**Python and PyQt: Building a GUI Desktop Calculator**](https://realpython.com/python-pyqt-gui-calculator/)

- by by [Leodanis Pozo Ramos](https://realpython.com/python-pyqt-gui-calculator/#author) at realpython
- Some interesting take-aways:
- Basics of PyQt
	- Widgets: QWidget is the base class for all user interface objects, or widgets. These are rectangular-shaped graphical components that you can place on your application’s windows to build the GUI. 
	- Layout Managers: Layout managers are classes that allow you to size and position your widgets at the places you want them to be on the application’s form.
	- Main Windows: Most of the time, your GUI applications will be Main Window-Style. This means that they’ll have a menu bar, some toolbars, a status bar, and a central widget that will be the GUI’s main element.
	- Applications: The most basic class you’ll use when developing PyQt GUI applications is QApplication. This class is at the core of any PyQt application. It manages the application’s control flow as well as its main settings.
	- Signals and Slots: PyQt widgets act as event-catchers. Widgets always emit a signal, which is a kind of message that announces a change in its state.
- Due to Qt licensing, you can only use the free version for non-commercial projects or internal non-redistributed or purchase a commercial license for $5,500/yr/dev.

**Extras**

**Brian**

- [PyCascades 2020 livestream videos](https://www.youtube.com/channel/UCtWI06j1EADmEOGj2iJhSyA/videos) of day 1 & day 2 are available.
	- Huge shout-out and thank you to all of the volunteers for this event.
	- In particular Nina Zakharenko for calming me down before my talk.
    

**Michael**

- [Recording for Python for .NET devs webcast available](https://www.crowdcast.io/e/python-for-dotnet-devs-webcast).
- [Take some of our free courses with our mobile app](https://training.talkpython.fm/apps).

**Joke**

- Why do programmers confuse Halloween with Christmas? Because `OCT 31 == DEC 25`.
- Speed dating is useless. 5 minutes is not enough to properly explain the benefits of the Unix philosophy.

