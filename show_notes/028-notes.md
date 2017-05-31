# Python Bytes 28
**Brian #1:**  [**pep8.org : PEP 8 — the Style Guide for Python Code**](http://pep8.org/)

- "This stylized presentation of the well-established PEP 8 was created by Kenneth Reitz (for humans)."
- From PEP 8: "This document gives coding conventions for the Python code comprising the standard library in the main Python distribution."
- PEP8 is not only used for the standard library. Many if not most open source Python packages adhere to at least most of the PEP8 recommendations
- testing plugins can help you make sure your code meets the guidelines (for good or bad).
- The pep8.org presentation is easy to read, with a left side clickable table of contents.
- Nice color coded examples. Green for good, Red for bad.
- links to specific items make it easy to share with others something specific.
- Good advice, but don't be a pep8-bully.
  

**Michael #2:** [**Tokio: Asyncio event loop written in Rust language**](https://pypi.python.org/pypi/tokio)

- Asyncio event loop written in Rust language
- It is still in alpha stage. 
- It provides most of asyncio event loop apis, except udp. 
- TCP api is more or less stable
- Aiohttp tests pass with tokio loop (~1800 tests)
- Mostly interesting as an example of Rust + Python
- Project is still in early stage of development

**Brian #3:** [**Python Boilerplate**](https://www.python-boilerplate.com)

- Interactive online tool for creating script and small project boilerplate code.
- Just starting, with "how to help" link.
- Select
  - Python 2 or 3
  - executable script or not
  - argparse
  - logging
  - .gitignore
  - Flask
  - unittest or pytest
  - tox
- fills in main.py, plus other files like test_sample.py, requirements.txt, tox.ini, etc.

**Michael #4:** [**Instagram switching to Python 3 on one branch**](https://www.youtube.com/watch?v=66XoCk79kjM)

- Ancient Django but still productive
- Ran out of 32-bit user IDs before they ran out of Django power. 
- Added sharing support to Django Orem
- Turned off GC for perf
- Upgraded entirely to 3.6 in a few months
- Why?
  - Type hints
  - Scaling server perf
  - asyncio
- Python 3 is where the future community work is happening 
- Strategies 
  - No user impact
  - Still shipping
  - Testing process was interesting
-  This is a concrete roadmap for every large company

**Brian #5:** [**The Meaning of Underscores in Python**](https://dbader.org/blog/meaning-of-underscores-in-python) 

  - single and double underscore meanings
  - dunder is "double underscore"
- Single Leading Underscore: `_var`
  - method or variable for internal use
  - convention only
  - doesn't apply to `collection.namedtuple`
- Single Trailing Underscore: `var_`
  - used to avoid name collision with keywords
- Double Leading Underscore: `__var`
  - internal use by a single class level.
  - Python will name mangle this so that subclasses don't have to avoid parent class double leading underscore names
- Double Leading and Trailing Underscore: `__var__`
  - no name mangling
  - special names. dunder methods
  - `__call__` and `__init__`, etc.
- Single Underscore: `_`
  - in code : temp variable, don't care variable
  - won't get a warning if you don't reference it again
  - in REPL: last value

**Michael #6:** [**The future is looking bright for Python**](https://medium.com/@trstringer/the-future-is-looking-bright-for-python-95a748a4ef3e)

- Stack Overflow recently released a cool new tool called [Trends](https://insights.stackoverflow.com/trends) (previously covered)
- Check out the [Most Popular Languages](https://insights.stackoverflow.com/trends?utm_source=so-owned&utm_medium=blog&utm_campaign=trends&utm_content=blog-link&tags=java%2Cc%2Cc%2B%2B%2Cpython%2Cc%23%2Cvb.net%2Cjavascript%2Cassembly%2Cphp%2Cperl%2Cruby%2Cswift%2Cr%2Cobjective-c) trend chart
- Python has, by a very large margin, the greatest positive slope (future?)
- And [Py3 vs Py2](https://insights.stackoverflow.com/trends?tags=python-2.7%2Cpython-3.x)

