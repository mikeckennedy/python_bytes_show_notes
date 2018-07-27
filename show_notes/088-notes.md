# Python Bytes 88
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** *[**Documenting Python Code: A Complete Guide**](https://realpython.com/documenting-python-code/)

- Article describes the why you should document, comments vs docstrings vs separate documentation.
- Let’s zoom in on comments, because I don’t think many people get how to use comments effectively.
- Commenting
	- comments are for you and other developers to help maintain the code. They can also help users understand your mental model and design. the source is often used as documentation if the other docs are lacking or confusing or incomplete.
	- Comments start with `#` and are not accessible at runtime.
	- Comment uses:
		- planning and reviewing
		- explaining intent
		- explaining complicated algorithms
		- tagging TODO, BUG, or FIXME sections.
	- Article includes some good tips:
	    - keep comments as close to code it’s describing as possible.
	    - don’t try to format it with ascii alignment or whatever
	    - minimal, most of your code shouldn’t need comments.
	    - remove planning comments when they aren’t needed any more
- Docstrings:
	- available at runtime via `help()`, `thing.__doc__`, and through many code completion tools in IDEs
	- Can be used at function, class, module, and package level.
	- Should help the user as if they don’t have the source available to look at.
- Also covered:
	- Commenting with type hints
	- How to use docstrings.
	- Docstring standard practices and formatting.
- Necessary elements of documenting projects
- Using tools like Sphinx, MkDocs, etc.

**Michael #2: [Security vulnerability alerts for Python at Github](https://blog.github.com/2018-07-12-security-vulnerability-alerts-for-python/)**

- Last year, GitHub released security alerts that track security vulnerabilities in Ruby and JavaScript packages. 
- They have identified millions of vulnerabilities and have prompted many patches.
- As of this week, Python users can now access the dependency graph and receive security alerts whenever their repositories depend on packages with known security vulnerabilities.
- See it under insights > dependency graph
- Using it:
	- Ensure that you have checked in a requirements.txt or Pipfile.lock file inside of repositories that have Python code.
	- Give access to private repos

**Brian #3:** [**How virtual environment libraries work in Python**](https://rushter.com/blog/python-virtualenv/)

- “Have you ever wondered what happens when you activate a virtual environment and how it works internally? Here is a quick overview of internals behind popular virtual environments, e.g., virtualenv, virtualenvwrapper, conda, pipenv.”
- “When Python starts its interpreter, it searches for the site-specific directory where all packages are stored. The search starts at the parent directory of a Python executable location and continues by backtracking the path (i.e., looking at the parent directories) until it reaches the root directory. To determine if it's a site-specific directory, Python looks for the `os.py` module, which is a mandatory requirement by Python in order to work.”
- virtualenv creates a directory with some bin files, and the lib that mostly points to the parent Python site versions using symbolic links.
- Python 3.3, with PEP 405, added a pyvenv.cfg file that allows the interpreter itself to be a symbolic link, as well as an option to use system site packages, saving on lots of symbolic links at the start.

**Michael** 4:** [**Qt for Python available at PyPi**](http://blog.qt.io/blog/2018/07/17/qt-python-available-pypi/)

- Announcement: Finally the technical preview of Qt for Python is available at the Python Package Index (PyPI).
- `pip install PySide2`
- Try it at one of the demo apps **[http://blog.qt.io/blog/2018/05/04/hello-qt-for-python/](http://blog.qt.io/blog/2018/05/04/hello-qt-for-python/)**
  

**Brian #5:** [**Learning (not) to Handle Exceptions**](https://www.pythonforthelab.com/blog/learning-not-to-handle-exceptions/)

- Understanding exceptions is important even if you never throw your own, since much of Python and 3rd party packages utilize them quite a bit.
- Try to catch specific exceptions. Don’t have `except:` catch everything.
- If you really need to intercept any exception, consider re-raising it with `raise`
- Some tips with handling multiple exceptions.
- `finally` can be used for stuff that needs to run regardless of an exception or not
- `else` runs if no exception occurs.
- You can use both `finally` and `else`
- Also:
	- tracebacks
	- custom exceptions
	- best practices
	- adding arguments to exceptions

**Michael #6:** [**Python has brought computer programming to a vast new audience**](https://www.economist.com/science-and-technology/2018/07/21/python-has-brought-computer-programming-to-a-vast-new-audience)

- Features quotes from Guido van Rossum
- Interesting history
- Seeing with “outside eyes” is pretty novel and something we don’t often get to do.
- More about the meteoric growth of Python
- Warnings about AI in the hands of half educated novices
