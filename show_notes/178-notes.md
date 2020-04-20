# Python Bytes 178

This episode is brought to you by Digital Ocean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

YouTube is going strong over at [**pythonbytes.fm/youtube**](http://pythonbytes.fm/youtube)

**Michael #1**: [**Python String Format Website**](https://pystrftime.com/)

- by [Lachlan Eagling](https://twitter.com/LachlanEagling)
- Have you ever forgotten the arguments to `datetime.str``f``time()`?
- Quick: What’s the format for `Wed April 15, 10:30am`? 
- I don’t know but the site says `'%a %B %H, %M:%Sam'` and it’s right!

Brian #2: [**Pandas-Bokeh**](https://github.com/PatrikHlobil/Pandas-Bokeh)

- Suggested by Jack McKew
- “Pandas-Bokeh provides a Bokeh plotting backend for Pandas, GeoPandas and Pyspark DataFrames, similar to the already existing Visualization feature of Pandas. Importing the library **adds** a complementary plotting method **plot_bokeh() on DataFrames and Series.**”
- “With **Pandas-Bokeh**, creating stunning, interactive, HTML-based visualization is as easy as calling: `df.plot_bokeh()`"
- You can also switch the default plotting of pandas to Bokeh with `pd.set_option('plotting.backend', 'pandas_bokeh')`
- This interface looks a lot easier to me, instead of frames and plots and shows and such.
- Lots of options, and all collected in parameters to the plot call.
- Can also export a notebook or a standalone html file.
- Plus, the combined install of `pip install pandas-bokeh` pulls in everything you need.

**Michael #3**: [**NBDev**](https://github.com/fastai/nbdev)

- nbdev is a library that allows you to fully develop a library in Jupyter Notebooks, putting all your code, tests and documentation in one place.
- That is: you now have a true [literate programming](https://en.wikipedia.org/wiki/Literate_programming) environment, as envisioned by Donald Knuth back in 1983!
- This seems to be a massive upgrade for notebooks and related tooling
- Creates Python packages out of a notebook
- Creates documentation from the notebook
- Solves the git perma-conflict issues with git pre-commit hooks
- Use #export to declare a cell should become a function in the package
- Manages the boilerplate issues for creating Python packages (setup.py, etc)
- Makes testing possible inside notebooks
- Navigate and edit your code in a standard text editor or IDE, and sync any changes automatically back into your notebooks (reverse basically)
- Follow [**getting started instructions**](https://github.com/fastai/nbdev#getting-started).
- Docs render slightly better at [**nbdev.fast.ai**](https://nbdev.fast.ai/)

Brian #4: [**Stop naming your python modules “utils”**](https://breadcrumbscollector.tech/stop-naming-your-python-modules-utils/)

- Sebastian Buczyński, [@EnforcerPL](https://twitter.com/EnforcerPL)
- Lots of projects, public and private, end up having a `utils.py`.
- “*utils* is arguably one of the worst names for a module because it is very blurry and imprecise. Such a name does not say what is the purpose of code inside. On the contrary, a *utils* module can as well contain almost anything. By naming a module *utils*, a software developer lays down perfect conditions for an incohesive code blob. Since the module name does not hint team members if something fits there or not, it is likely that unrelated code will eventually appear there, as more *utils*.”
- one occurrence of misbehavior invites more of them
	- I have seen this in action. I’ve put 2-3 hard to classify methods, but used in lots of modules, into a `utils.py`, only to come back in a few months and see a couple dozen completely unrelated methods, now that the team has a junk drawer to throw things in.
- Excuses:
	- It’s just one function
	- There is no other place to put this code
	- I need a place for company commons
	- But Django does it
- Instead:
	- Try naming based on role of the code or group functions by theme.
	- If you see a `utils.py` crop up in a code review, request that it be renamed or split and renamed.

**Michael #5**: [**Scalene**](https://github.com/emeryberger/scalene)

- A high-performance, high-precision **CPU and memory** profiler for Python
- It runs orders of magnitude faster than other profilers while delivering far more detailed information.
- Scalene is *fast*. It uses sampling instead of instrumentation or relying on Python's tracing facilities. Its overhead is typically no more than 10-20% (and often less).
- Scalene is *precise*. Unlike most other Python profilers, Scalene performs CPU profiling *at the line level*, pointing to the specific lines of code that are responsible for the execution time in your program.
- Scalene separates out time spent running in Python from time spent in native code (including libraries).
- Scalene *profiles memory usage*. In addition to tracking CPU usage, Scalene also points to the specific lines of code responsible for memory growth. It accomplishes this via an included specialized memory allocator.
	- Requires special install, not just pip (see brew install instructions for the docs)
- Scalene profiles *copying volume*, making it easy to spot inadvertent copying, especially due to crossing Python/library boundaries (e.g., accidentally converting `numpy` arrays into Python arrays, and vice versa).
- See the [**performance comparison chart**](https://github.com/emeryberger/scalene#comparison-to-other-profilers).
- Would be nice to have integrated in the editors (PyCharm and VS Code)

**Brian #6:** [**From 1 to 10,000 test cases in under an hour: A beginner's guide to property-based testing**](https://dev.to/meeshkan/from-1-to-10-000-test-cases-in-under-an-hour-a-beginner-s-guide-to-property-based-testing-1jf8)

- Carolyn Stransky, [@carolynstran](https://twitter.com/carolstran)
- Excellent intro to property based testing and hypothesis
- Starts with a unit test that uses example based testing.
- Before showing similar test using hypothesis, she talks about the different mindset of testing for properties instead of exact examples.
	- Like not the exact sorted list you should
	- but instead, 
		- the length should be the same
		- the contents should contain the same things, for instance, using set for that assertion
		- you could element-wise walk the list and make sure i <= i+1
- She walks through the hypothesis decorators to come up with input and shows how to use `some.lists` and `some.integers` and `max_examples`
- Goes on to discuss coming up with properties to test for, which really is the hard part of property based testing.
- Checking for expected exceptions
- Using a naive method technique, useful in property based testing, to compare two versions of a method. This is super useful for refactoring and testing new vs old versions on tons of input data.
- [**json5 lib**](https://pypi.org/project/json5/)

**Extras**

- [John Conway, inventor of the Game of Life, has died of COVID-19](https://arstechnica.com/science/2020/04/john-conway-inventor-of-the-game-of-life-has-died-of-covid-19/)
- [GitHub is now free for all teams](https://techcrunch.com/2020/04/14/github-is-now-free-for-all-teams/) (and individuals)
	- including 2,000 Actions minutes/month 
	- unlimited collaborators, even on private repos
- [GitLab has a similar free tier](https://about.gitlab.com/pricing/)
- [PyCon US 2020 Online](https://us.pycon.org/2020/online/)
	- Lots of talks already up, more on the way.
[](https://us.pycon.org/2020/online/)

**Joke**

PyJoke delivers:

*How many QAs does it take to change a lightbulb? They noticed that the room was dark. They don't fix problems, they find them.*

