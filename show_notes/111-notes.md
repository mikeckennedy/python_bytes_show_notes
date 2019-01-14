# Python Bytes 111
Sponsored by [https://pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Brian #1:** [**loguru:**](https://github.com/Delgan/loguru) [**Python logging made (stupidly) simple**](https://github.com/Delgan/loguru)

- Finally, a logging interface that is just slightly more syntax than print to do mostly the right thing, and all that fancy stuff like log rotation is easy to figure out.
- i.e. a logging API that fits in my brain.
- bonus: README is a nice tour of features with examples.
- Features:
	- Ready to use out of the box without boilerplate
	- No Handler, no Formatter, no Filter: one function to rule them all
	- Easier file logging with rotation / retention / compression
	- Modern string formatting using braces style
	- Exceptions catching within threads or main
	- Pretty logging with colors
	- Asynchronous, Thread-safe, Multiprocess-safe
	- Fully descriptive exceptions
	- Structured logging as needed
	- Lazy evaluation of expensive functions
	- Customizable levels
	- Better datetime handling
	- Suitable for scripts and libraries
	- Entirely compatible with standard logging
	- Personalizable defaults through environment variables
	- Convenient parser
	- Exhaustive notifier

**Michael #2:** [**Python gets a new governance model**](https://mail.python.org/pipermail/python-committers/2018-December/006479.html)

- by Brett Canon
- July 2018, Guido steps down
- Python progress has basically been on hold since then
- ended up with [7 governance proposals](https://www.python.org/dev/peps/pep-8000/)
- Voting was open to all core developers as we couldn't come up with a reasonable criteria that we all agreed to as to what defined an "active" core dev
- And the winner is ... In the end PEP 8016, the steering council proposal, won.
- it was a decisive win against second place
- PEP 8016 is heavily modeled on the Django project's organization (to the point that the PEP had stuff copy-and-pasted from the original Django governance proposal).
	- What it establishes is a steering council of five people who are to determine how to run the Python project. Short of not being able to influence how the council itself is elected (which includes how the electorate is selected), the council has absolute power.
	- result of the vote prevents us from ever having the Python *project* be leaderless again, it doesn't directly solve how to guide the *language's* design.
- What's next? The next step is we elect the council. It's looking like nominations will be from Monday, January 07 to Sunday, January 20 and voting from Monday, January 21 to Sunday, February 03
- A key point I hope people understand is that while we solved the issue of project management that stemmed from Guido's retirement, the council will need to be given some time to solve the other issue of how to manage the design of Python itself.

**Brian #3:** [**Why you should be using pathlib**](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)

- Tour of pathlib from Trey Hunner
- pathlib combines most of the commonly used file and directory operations from `os`, `os.path`, and `glob`.
- uses objects instead of strings
- as of Python 3.6, many parts of stdlib support pathlib
- since `pathlib.Path` methods return `Path` objects, chaining is possible
- convert back to strings if you really need to for pre-3.6 code
- Examples:
	- make a directory: `Path('src/__pypackages__').mkdir(parents=True, exist_ok=True)`
	- rename a file: `Path('.editorconfig').rename('src/.editorconfig')`
	- find some files: `top_level_csv_files = Path.cwd().glob('*.csv')`
	- recursively: `all_csv_files = Path.cwd().rglob('*.csv')`
	- read a file: `Path('some/file').read_text()`
	- write to a file: `Path('.editorconfig').write_text('# config goes here')`
	- `with open(path, mode) as x` works with Path objects as of 3.6
  
**Michael #4:** [**Altair**](https://github.com/altair-viz/altair) **and** [**Altair Recipes**](https://github.com/piccolbo/altair_recipes)

- via Antonio Piccolboni (he wrote altair_recipes)
- Altair: Declarative statistical visualization library for Python
  - Altair is developed by Jake Vanderplas and Brian Granger
  - By statistical visualization they mean:
		- The data source is a DataFrame that consists of columns of different data types (quantitative, ordinal, nominal and date/time).
		- The DataFrame is in a tidy format where the rows correspond to samples and the columns correspond to the observed variables.
		- The data is mapped to the visual properties (position, color, size, shape, faceting, etc.) using the group-by data transformation.
  - Nice example that I can get behind

```
    # cars = some Pandas data frame
    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )
```

- altair_recipes
	- Altair allows generating a wide variety of statistical graphics in a concise language, but lacks, by design, pre-cooked and ready to eat statistical graphics, like the boxplot or the histogram. 
	- Examples: [https://altair-recipes.readthedocs.io/en/latest/examples.html](https://altair-recipes.readthedocs.io/en/latest/examples.html) 
	- They take a few lines only in altair, but I think they deserve to be one-liners. altair_recipes provides that level on top of altair. The idea is not to provide a multitude of creative plots with fantasy names (the way seaborn does) but a solid collection of classics that everyone understands and cover most major use cases: the scatter plot, the boxplot, the histogram etc.  
	- Fully documented, highly consistent API (see next package), 90%+ test coverage, maintainability grade A, this is professional stuff if I may say so myself.

**Brian #5:** **A couple fun pytest plugins**

- [pytest-picked](https://github.com/anapaulagomes/pytest-picked)
	- Using `git status`, this plugin allows you to:
		- Run only tests from modified test files
		- Run tests from modified test files first, followed by all unmodified tests
	- Kinda hard to overstate the usefulness of this plugin to anyone developing or debugging a test. Very, very cool.
- [pytest-clarity](https://github.com/darrenburns/pytest-clarity)
	- Colorized left/right comparisons
	- Early in development, but already helpful.
	- I recommend running it with -qq if you don’t normally run with -v/--verbose since it overrides the verbosity currently.

**Michael #6:** [**Secure 🔒 headers and cookies for Python web frameworks**](https://github.com/cakinney/secure.py)

- Python package called Secure, which sets security headers and cookies (as a start) for Python web frameworks.
- I was listening to the Talk Python To Me episode “Flask goes 1.0” with Flask maintainer David Lord. At the end of the interview he was asked about notable PyPI packages and spoke about Flask-Talisman, a third-party package to set security headers in Flask. As a security professional, it was surprising and encouraging to hear the maintainer of the most popular Python web framework speak passionately about a security package. 
- Had been recently experimenting with emerging Python web frameworks and realized there was a gap in security packages. That inspired Caleb to (humbly) see if it were possible to make a package to correct that and I started with Responder and then expanded to support more frameworks. 
- The outcome was Secure with functions to support aiohttp, Bottle, CherryPy, Falcon, hug, Pyramid, Quart, Responder, Sanic, Starlette and Tornado (most of these, if not all have been featured on Talk Python) and can also be utilized by frameworks not officially supported. The goal is to be minimalistic, lightweight and be implemented in a way that does not disrupt an individual framework’s design. 
- I have had some great feedback and suggestions from the developer and OWASP community, including some awesome discussions with the OWASP Secure Project and the Sanic core team. 
- Added support for Flask and Django too.
- Secure Cookies is nice in the mix

**Extras:**

**Michael:** [**SQLite bug impacts thousands of apps, including all Chromium-based browsers**](https://www.zdnet.com/article/sqlite-bug-impacts-thousands-of-apps-including-all-chromium-based-browsers/)

- See [https://twitter.com/mborus/status/1080874700924964864](https://twitter.com/mborus/status/1080874700924964864)
- Since this bug is triggered by an SQL command, general CPython usage should not be affected, and long as you don’t run arbitrary SQL-commands provided by the outside.
- Seems to NOT be a problem in CPython: [https://twitter.com/mborus/status/1080883549308362753](https://twitter.com/mborus/status/1080883549308362753)

**Michael: Follow up to our AI and healthcare conversation**

- via Bradley Hintze
- I found your discussion of deep learning in healthcare interesting, no doubt because that is my area. I am the data scientist for the National Oncology Program at the Veterans Health Administration. 
- I work directly with clinicians and it is my strong opinion that AI cannot take the job from the MD. It will however make caring for patients much more efficient as AI takes care of the low hanging fruit, it you will.
- Healthcare, believe it or not, is a science and an art. This is why AI is never going to make doctors obsolete. It will, however, make doctors more efficient and demanded a more sophisticated doctor -- one that understands AI enough to not only trust it but, crucially, comprehend its limits.

**Michael: Upgrade to Python 3.7.2**

- If you install via home brew, it’s time for `brew update && brew upgrade`

**Michael: New course!** 

- [Introduction to Ansible](https://training.talkpython.fm/courses/explore_ansible/introduction-to-ansible-with-python)

