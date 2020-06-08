# Python Bytes 185

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)


----------

**Brian #1:**  [**MyST - Markedly Structured Text**](https://myst-parser.readthedocs.io/en/latest/)

- I think this came from a tweet from [Chris Holdgraf](https://twitter.com/choldgraf)
- A fully-functional markdown flavor and parser for Sphinx.
- MyST allows you to write Sphinx documentation entirely in markdown. MyST markdown provides a markdown equivalent of the reStructuredText syntax, meaning that you can do anything in MyST that you can do with reStructuredText. It is an attempt to have the best of both worlds: the flexibility and extensibility of Sphinx with the simplicity and readability of Markdown.
- MyST has the following main features:
	- [**A markdown parser for Sphinx**](https://myst-parser.readthedocs.io/en/latest/using/intro.html#parse-with-sphinx). You can write your entire [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html) in markdown.
	- [**Call Sphinx directives and roles from within Markdown**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#syntax-directives), allowing you to extend your document via Sphinx extensions.
	- [**Extended Markdown syntax for useful rST features**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#extended-block-tokens), such as line commenting and footnotes.
	- [**A Sphinx-independent parser of MyST markdown**](https://myst-parser.readthedocs.io/en/latest/using/use_api.html) that can be extended to add new functionality and outputs for MyST.
	- [**A superset of CommonMark markdown**](https://commonmark.org/). Any CommonMark markdown (such as Jupyter Notebook markdown) is natively supported by the MyST parser.


----------

**Michael #2:** [**direnv**](https://direnv.net/)

- [via __dann__](https://twitter.com/whereismyjetpac/status/1260623498030067717)
- `direnv` is an extension for your shell. It augments existing shells with a new feature that can load and unload environment variables depending on the current directory.
- Use cases
	- Load 12factor apps environment variables
	- Create per-project isolated development environments
	- Load secrets for deployment
- Before each prompt, direnv checks for the existence of a `.envrc` file in the current and parent directories.
- If the file exists, it is loaded into a **bash** sub-shell and all exported variables are then captured by direnv and then made available to the current shell.
- It supports hooks for all the common shells like bash, zsh, tcsh and fish. This allows project-specific environment variables without cluttering the `~/.profile` file.
- Because direnv is compiled into a single static executable, it is fast enough to be unnoticeable on each prompt.

----------

**Brian #3:** [**Convert a Python Enum to JSON**](https://hultner.se/quickbits/2018-03-12-python-json-serializable-enum.html)

- Alexander Hultner

Problem:

- Enum values by default are not serializable.
- So you can't use them as values in JSON.
- and can't use them as values passed to databases.

Solution:

- Derived enumerations, like [IntEnum](https://docs.python.org/3/library/enum.html#derived-enumerations) or [custom derived enumerations](https://docs.python.org/3/library/enum.html#others) are simple to define and serializable.
- You can convert them to json and store them as database values.

Example: 

```
    >>> from enum import Enum, IntEnum
    >>> import json
    >>> class Color(Enum):
    ...   red = 1
    ...   blue = 2
    ...
    >>> c = Color.red
    >>> c
    <Color.red: 1>
    >>>
    >>> json.dumps(c)
    Traceback (most recent call last):
    ...
    TypeError: Object of type Color is not JSON serializable


    >>> class Color(IntEnum):
    ...   red = 1
    ...   blue = 2
    ...
    >>> c = Color.red
    >>> c
    <Color.red: 1>
    >>> json.dumps(c)
    '1'


    >>> class Color(str, Enum):
    ...   red = "red"
    ...   blue = "blue"
    ...
    >>> c = Color.red
    >>> c
    <Color.red: 'red'>
    >>> json.dumps(c)
    '"red"'
```

----------

**Michael #4:** [**Pendulum: Python datetimes made easy**](https://pendulum.eustace.io/)

- via [tuckerbeck](https://twitter.com/tuckerbeck/status/1159503255925170176)
- Drop-in replacement for the standard datetime class.
- Time deltas

```
    dur = pendulum.duration(days=15)
    
    # More properties
    dur.weeks
    dur.hours
    
    # Handy methods
    dur.in_hours()
    360
    dur.in_words(locale="en_us")
    '2 weeks 1 day'
```

- Intervals

```
    dt = pendulum.now()
    
    # A period is the difference between 2 instances
    period = dt - dt.subtract(days=3)
    
    period.in_weekdays()
    
    # A period is iterable
    for dt in period:
        print(dt)
```

----------

**Brian #5:**  ****[PySnooper - Never use print for debugging again](https://github.com/cool-RR/pysnooper)

- Thanks [@pylang23](https://twitter.com/pylang23) for [the suggestion](https://twitter.com/pylang23/status/1267639151295414273?s=20).
- With **PySnooper** you can just add one decorator line to a function and you get a play-by-play log of your function, including which lines ran and when, and exactly when local variables were changed.
- Logs
	- every modified variable with value
	- which line of code is being run
	- return value
	- passed in parameters
	- elapsed time
- Options to:
	- isolate logging to a section of a function with a with block
	- log to a file instead of stdout
	- extend watch to a list of non-local variables
	- extend watch to functions called by the function being decorated
- All with a simple decorator and a pretty simple API


----------

**Michael #6:** [**Fil: A New Python Memory Profiler for Data Scientists and Scientists**](https://pythonspeed.com/articles/memory-profiler-data-scientists/)

- via PyCoders
- If your Python data pipeline is using too much memory, it can be very difficult to figure where exactly all that memory is going.
- Yes, there are existing memory profilers for Python that help you measure memory usage, but none of them are designed for batch processing applications that read in data, process it, and write out the result.
- **What you need is some way to know exactly where peak memory usage is, and what code was responsible for memory at that point.** And that’s exactly what the [Fil memory profiler](https://pythonspeed.com/products/filmemoryprofiler/) does.
- Because of this difference in lifetime, the impact of memory usage is different.
	- **Servers:** Because they run forever, memory leaks are a common cause of memory problems. Even a small amount of leakage can add up over tens of thousands of calls. Most servers just process small amounts of data at a time, so actual business logic memory usage is usually less of a concern.
	- **Data pipelines:** With a limited lifetime, small memory leaks are less of a concern with pipelines. Spikes in memory usage due to processing large chunks of data are a more common problem.
- **This is Fil’s primary goal: diagnosing spikes in memory usage.**
- Many tools track just Python memory. ****Fil captures *all* allocations going to the standard C memory allocation APIs.


----------

**Extras:**

Michael:

- Student cohorts: [training.talkpython.fm/cohorts/apply](https://training.talkpython.fm/cohorts/apply), but had to [close after just a day due to high volume](https://twitter.com/TalkPython/status/1267226093880139776)



----------

**Joke:**


- **Senior dev**: Where did you get the code that does this from?
- *Junior dev*: Stack Overflow
- **Senior dev**: Was it from the question part or from the answer part?
