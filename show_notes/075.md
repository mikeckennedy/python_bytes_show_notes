# Python Bytes 75
Sponsored by Datadog: [**pythonbytes.**](https://pythonbytes.fm/datadog)[**fm**](https://pythonbytes.fm/datadog)[**/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**numba**](https://pypi.org/project/numba/)

- From the numba readme:
	- “The easiest way to install numba and get updates is by using the Anaconda Distribution: [https://www.anaconda.com/download](https://www.anaconda.com/download)”
- [The need for speed without bothering too much: An introduction to numba](http://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/numba/numba.ipynb?utm_source=newsletter_mailer&utm_medium=email&utm_campaign=weekly#The-need-for-speed-without-bothering-too-much:-An-introduction-to-numba)
- Can get huge speed up for some computation heavy loops or algorithms.

**Michael #2:** [**pip 10 is out**](https://blog.python.org/2018/04/pip-10-has-been-released.html)**!**

- Time for: `python -m pip install --upgrade pip`
- Features:
	- Python 2.6 is no longer supported - if you need pip on Python 2.6, you should stay on pip 9, which is the last version to support Python 2.6.
	- Support for PEP 518, which allows projects to specify what packages they require in order to build from source. (PEP 518 support is currently limited, with full support coming in future versions - see the documentation for details).
	- Significant improvements in Unicode handling for non-ASCII locales on Windows.
	- A new "pip config" command.
	- The default upgrade strategy has become "only-if-needed"
	- Many bug fixes and minor improvements.

**Brian** **#3:** [**Keyword (Named) Arguments in Python: How to Use Them**](http://treyhunner.com/2018/04/keyword-arguments-in-python/)

- Using keyword arguments is often seen when there are many arguments to a function that have useful defaults, and you only want to override the default with some of the arguments.
- Example:
```python
    >>> print('comma', 'separated', 'words', sep=', ')
    comma, separated, words
```
- You can take positional arguments and require some to be named with various uses of `*`
```
    def foo(*, bar, baz):
      print(f'{bar} {baz}') 
```
- Lots of other useful tricks in this article.

**Michael #4**[**:**](https://edgedb.com/blog/edgedb-a-new-beginning) [**pypi.org officially launches**](https://pythoninsider.blogspot.ca/2018/04/new-pypi-launched-legacy-pypi-shutting.html)

- Legacy PyPI shutting down April 30
- Listen to talk python 159
- Starting April 16, the canonical Python Package Index is at [https://pypi.org](https://pypi.org) and uses the new Warehouse codebase.
- Launched the new PyPI, redirecting browser traffic and API calls (including "pip install") from pypi.python.org to the new site. The old codebase is still available at [https://legacy.pypi.org](https://legacy.pypi.org) for now.
- Monday April 30 (2018-04-30): We plan to shut down legacy PyPI https://legacy.pypi.org . The address pypi.python.org will continue to redirect to Warehouse.
- If your site/service links to or uses [pypi.python.org](http://pypi.python.org), you should start using pypi.org instead: [https://warehouse.readthedocs.io/api-reference/integration-guide/#migrating-to-the-new-pypi](https://warehouse.readthedocs.io/api-reference/integration-guide/#migrating-to-the-new-pypi) 

**Brian** **#5:** [**Python Modules and Packages – An Introduction**](https://realpython.com/python-modules-packages/)

- In Python, it is, and understanding modules and packages is key to getting a good footing when learning Python. It’s also an area that trips up people when they start trying to create reusable code.
- How to create a Python **module**
- Locations where the Python interpreter searches for a module
- How to obtain access to the objects defined in a module with the `import` statement
- How to create a module that is executable as a standalone script
- How to organize modules into **packages** and **subpackages**
- How to control package initialization

**Michael #6: Pandas only like modern Python**

- From December 31st, 2018, Pandas will drop support for Python 2.7. This includes no backports of security or bug fixes (unless someone volunteers to do those)
- The final release before December 31, 2018 will be the last release to support Python 2. The released package will continue to be available on PyPI and through conda.
- Starting January 1, 2019, all releases will be Python 3 only.
- The full [reddit discussion](https://www.reddit.com/r/Python/comments/8c883i/from_december_31st_2018_pandas_will_drop_support/) is interesting.

**Our news**

- Just launched: Python 3, an illustrated tour! [**talkpython.fm/illustrated**](https://talkpython.fm/illustrated)



