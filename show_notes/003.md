Welcome to Python Bytes. Python headlines delivered directly to your earbuds. In this episode we cover the new features in Python 3.6, text processing with Pynini, Python is 2nd most popular language on GitHub and more. [more]

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

## News items

[**How to get superior text processing with Pynini**](https://www.oreilly.com/ideas/how-to-get-superior-text-processing-in-python-with-pynini)

- how to change your thinking from regular expression matching to FSAs (finite-state acceptor), then FSTs.
- Example using cheese names (love the Python tradition with that).
- library developed at Google called pynini for easily using FSTs




[**Python 3.6 b4 Is out! (beta!!!)**](https://docs.python.org/3.6/whatsnew/3.6.html)

- [PEP 498](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep498), formatted string literals.
- [PEP 515](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep515), underscores in numeric literals.
- [PEP 525](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep525), asynchronous generators.
- [PEP 530](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep530): asynchronous comprehensions.
- The **dict** type has been reimplemented to use a faster, more compact representation similar to the PyPy dict implementation. This resulted in dictionaries using 20% to 25% less memory when compared to Python 3.5.
- The class attribute definition order is now preserved.
- **Security**: The new secrets module has been added to simplify the generation of cryptographically strong pseudo-random numbers suitable for managing secrets such as account authentication, tokens, and similar.
- **Windows**: python.exe and pythonw.exe have been marked as long-path aware, which means that when the 260 character path limit may no longer apply. See removing the MAX_PATH limitation for details.



[**Create an Excellent Python Dev Env**](http://www.dougalmatthews.com/2016/Nov/12/create-an-excellent-python-dev-env/)

- pyenv, like virtualenv, I think, but independent of Python.
- pyenv-virtualenv instead of virtualenvwrapper
- pipsi - a tool to let you install python based CLI utilities in their own virtualenv easily. 
- Tools he installs with pipsi:
	- tox - testing multiple environments
	- mkdocs - documentation static site generator
	- git-review - gerrit integration with git. 
	- flake8 - static analysis
- He also mentions a shell called fish, which I hadn’t heard of before.



[**GitHub language statistics, Python is 2nd most popular language**](https://www.reddit.com/r/Python/comments/5craf4/github_language_statistics_python_is_2nd_most/)

- An active repository should meet this requirements:
created or updated during the evaluated period,
	- at least one star
	- at least one fork
	- a size larger than 10 Kb
- JavaScript is likely over counted



[**Handling Unicode Strings in Python**](http://blog.emacsos.com/unicode-in-python.html)
- Text Representation in Python and the differences between 2.7 and 3.4+
- Converting between unicode strings and bytes
- IO boundary issues with databases, file system, or network services
- Logging
- JSON encoding
- Redis
- A pointer to a 2012 article from Ned Batchelder called Pragmatic Unicode.


[**Python extensions for VS Code for Mac / PC / Linux**](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python)

- Linting (Prospector, Pylint, pycodestyle/Pep8, Flake8, pylama, pydocstyle with config files and plugins)
- Intellisense (autocompletion with support for PEP-0484)
- Scientific tools (Jupyter/IPython)
- Auto indenting
- Code formatting (autopep8, yapf, with config files)
- Code refactoring (Rename, Extract Variable, Extract Method, Sort Imports)
- Viewing references, code navigation, view signature
- Excellent debugging support (remote debugging over SSH, mutliple threads, django, flask)
- Unit testing, including debugging (unittest, pytest, nosetests, with config files)
- Execute file or code in a python terminal
- Local help file (offline documentation)
- Snippets


## Our personal news

### Brian
- Lot’s of writing. My target is to get the book in print by PyCon US 2017 in May. But that’s an aggressive schedule with the rest of my projects.
- Still working on getting #25 out the door. Interview with Dave Hunt from Mozilla about Selenium, Mozilla, pytest, tox, CI, and much more. Should go out within the next couple of days. 
- Next interview scheduled is with David Hussman from DevJam. This will be a higher level discussion about software development practices. Look for that this month also.


### Michael
- Shipped: [Episode #85: Parsing horrible things with Python](https://talkpython.fm/episodes/show/85/parsing-horrible-things-with-python)
- Quick correction: github's awesome-python isn't the newsletter, that's [https://python.libhunt.com](https://python.libhunt.com)