# Python Bytes 253

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

**Michael #1:** [**awesome-htmx**](https://github.com/rajasegar/awesome-htmx)

- An awesome list of resources about **htmx** such as articles, posts, videos, talks and more.
- Good for all sorts of examples and multiple languages
- We get a few nice shoutouts, thanks

**Brian #2:** [**Python 3.10 is here !!!!**](https://www.python.org/downloads/release/python-3100/) 

- As of Monday. Of course I have it installed on Mac and Windows. Running like a charm.
- You can watch the [Release Party recording](https://t.co/sK5SmgXpif?amp=1). It’s like 3 hours. And starts with hats. Pablo’s is my fav.
- Also a [What’s New video](https://www.youtube.com/watch?v=JteTO3EE7y0&t=1s) which aired before that with Brandt Bucher, Lukasz Llanga ,and Sebastian Ramirez (33 min)
	- Includes a deep dive into structural pattern matching that I highly recommend.
- Reminder of new features:
	- [PEP 623](https://www.python.org/dev/peps/pep-0623/) -- Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
	- PEP 604 -- Allow writing union types as X | Y
	- [PEP 612](https://www.python.org/dev/peps/pep-0612/) -- Parameter Specification Variables
	- [PEP 626](https://www.python.org/dev/peps/pep-0626/) -- Precise line numbers for debugging and other tools.
	- [PEP 618](https://www.python.org/dev/peps/pep-0618/) -- Add Optional Length-Checking To zip.
	- [bpo-12782](https://bugs.python.org/issue12782): Parenthesized context managers are now officially allowed.
	- [PEP 632](https://www.python.org/dev/peps/pep-0632/) -- Deprecate distutils module.
	- [PEP 613](https://www.python.org/dev/peps/pep-0613/) -- Explicit Type Aliases
	- [PEP 634](https://www.python.org/dev/peps/pep-0634/) -- Structural Pattern Matching: Specification
	- [PEP 635](https://www.python.org/dev/peps/pep-0635/) -- Structural Pattern Matching: Motivation and Rationale
	- [PEP 636](https://www.python.org/dev/peps/pep-0636/) -- Structural Pattern Matching: Tutorial
	- [PEP 644](https://www.python.org/dev/peps/pep-0644/) -- Require OpenSSL 1.1.1 or newer
	- [PEP 624](https://www.python.org/dev/peps/pep-0624/) -- Remove Py_UNICODE encoder APIs
	- [PEP 597](https://www.python.org/dev/peps/pep-0597/) -- Add optional EncodingWarning
- Takeaway I wasn’t expecting: `black` doesn’t handle Structural Pattern Matching yet. 

**Yael #3:** [Prospector -](https://github.com/PyCQA/prospector) [(almost)](https://github.com/PyCQA/prospectors) [All Python analysis tools together](https://github.com/PyCQA/prospector)

- Instead of running pylint, pycodestyle, mccabe and other separately, prospector allows you to bundle them all together 
- Includes the common [Pylint](https://www.pylint.org/) and [Pydocstyle / Pep257](https://github.com/PyCQA/pydocstyle), but also some other less common goodies, such as [Mccabe](https://github.com/PyCQA/mccabe), [Dodgy](https://github.com/landscapeio/dodgy), [Vulture](https://github.com/jendrikseipp/vulture), [Bandit](https://github.com/PyCQA/bandit), [Pyroma](https://github.com/regebro/pyroma) and many others 
- Relatively easy configuration that supports profiles, for different cases
- Built-in support for celery, Flask and Django frameworks
- [https://soshace.com/how-to-use-prospector-for-python-static-code-analysis/](https://soshace.com/how-to-use-prospector-for-python-static-code-analysis/)


**Michael #****4****:** [**Rich Pandas DataFrames**](https://twitter.com/__aviperl__/status/1442542251817652228)

- via Avi Perl, by Khuyen Tran
- Create animated and pretty Pandas Dataframe or Pandas Series (in the terminal, using Rich)
- I just had Will over on Talk Python last week BTW: [**Terminal magic with Rich and Textual**](https://talkpython.fm/episodes/show/336/terminal-magic-with-rich-and-textual)
- Can limit rows, control the animation speed, show head or tail, go “full screen” with clear, etc.
- Example:
```
    from sklearn.datasets import fetch_openml
    from rich_dataframe import prettify
    
    speed_dating = fetch_openml(name='SpeedDating', version=1)['frame']
    table = prettify(speed_dating)
```

**Brian #5:**  **Union types, baby!**

- From Python 3.10: “[PEP 604](https://www.python.org/dev/peps/pep-0604/) -- Allow writing union types as X | Y”
- Use as possibly not intended, to avoid Optional:
```
    def foo(x: str | None = None) -> None:
      pass 
```
- 3.9 example:
```
    from typing import Optional
    def foo(x: Optional[str] = None) -> None:
      pass
```
- But here’s the issue. I need to support Python 3.9 at least, and probably early, what should I do?
- For 3.7 and above, you can use `from __future__ import annotations`.
- And of course Anthony Sottile worked this into `pyupgrade` and Adam Johnson wrote about it:
	- [Python Type Hints - How to Upgrade Syntax with pyupgrade](https://adamj.eu/tech/2021/05/21/python-type-hints-how-to-upgrade-syntax-with-pyupgrade/)
- This article covers:
	- [PEP 585](https://www.python.org/dev/peps/pep-0585/) added generic syntax to builtin types. This allows us to write e.g. `list[int]` instead of using `typing.List[int]`.
	- [PEP 604](https://www.python.org/dev/peps/pep-0604/) added the `|` operator as union syntax. This allows us to write e.g. `int | str` instead of `typing.Union[int, str]`, and `int | None` instead of `typing.Optional[int]`.
	- How to use these. What they look like. And how to use `pyupgrade` to just convert your code for you if you’ve already written it the old way. Awesome.


**Yael #6:** [**Make your code darker - Improving Python code incrementally**](https://dev.to/akaihola/improving-python-code-incrementally-3f7a)

- The idea behind [Darker](https://pypi.org/project/darker) is to reformat code using [Black](https://pypi.org/project/black) (and optionally [isort](https://pypi.org/project/isort)), but only apply new formatting to regions which have been modified by the developer
- Instead of having one huge PR,  darker allows you to reformat the code gradually, when you're touching the code for other reasons.. 
- Every modified line, will be black formatted
- Once added to [Git pre-commit-hook](https://github.com/akaihola/darker#using-as-a-pre-commit-hook), or added to [PyCharm](https://github.com/akaihola/darker#pycharmintellij-idea) [****](https://github.com/akaihola/darker#pycharmintellij-idea)/ [VScode](https://github.com/akaihola/darker#visual-studio-code) the formatting will happen automatically


**Extras**

Brian:

- I got a couple PRs accepted into pytest. So that’s fun:
	- [9133: Add a deselected parameter to assert_outcomes()](https://github.com/pytest-dev/pytest/pull/9133)
	- [9134: Add a pythonpath setting to allow paths to be added to sys.path](https://github.com/pytest-dev/pytest/pull/9134)
	- I’ve tested, provided feedback, written about, and submitted issues to the project before. I’ve even contributed some test code. But these are the first source code contributions.
	- It was a cool experience. Great team there at pytest.

Michael:

- New htmx course: [**HTMX + Flask: Modern Python Web Apps, Hold the JavaScript**](https://training.talkpython.fm/courses/htmx-flask-modern-python-web-apps-hold-the-javascript?utm_source=pythonbytes)
- [**auto-optional**](https://pypi.org/project/auto-optional/): Due to the comments on the show I remembered to add support for `Union[X, None]` and python 10’s `X | None` syntax.
- [Coverage 6.0 released](https://nedbatchelder.com/blog/202110/coverage_60.html)
- [Django 3.2.8 released](https://docs.djangoproject.com/en/3.2/releases/3.2.8/)

Yael:

- [data-oriented-programming](https://www.manning.com/books/data-oriented-programming) - an innovative approach to coding without OOP, with an emphasis on code and data separation, which simplifies state management and eases concurrency
- Help us to make [Cornell](https://github.com/hiredscorelabs/cornell) awesome 🙂 - contributors are warmly welcomed

**Joke:** [**Pair CAPTCHAing**](https://geek-and-poke.com/geekandpoke/2021/1/24/pair-captchaing)

