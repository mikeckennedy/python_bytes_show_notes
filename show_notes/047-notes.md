# Python Bytes 47
Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #****1****:** [**PyPy v5.9 Released, Now Supports Pandas, NumPy**](https://morepypy.blogspot.com/2017/10/pypy-v59-released-now-supports-pandas.html)

- NumPy and Pandas work on PyPy2.7 v5.9
- Cython 0.27.1 (released very recently) supports more projects with PyPy, both on PyPy2.7 and PyPy3.5 beta
- Optimized JSON parser for both memory and speed.
- CFFI updated
- Nice to see continued improvements and work on PyPy

**Michael #2:** [**WTF Python?**](https://github.com/satwikkansal/wtfpython/blob/master/README.md)

- Python, being awesome by design high-level and interpreter-based programming language, provides us with many features for the programmer's comfort. 
- But sometimes, the outcomes of a Python snippet may not seem obvious to a regular user at first sight.
- Here is a fun project attempting to collect such classic and tricky examples of unexpected behaviors in Python and discuss what exactly is happening under the hood!
- Examples:
	  - [**Skipping lines?**](https://github.com/satwikkansal/wtfpython/blob/master/README.md#skipping-lines)
	  - **​​**[**Modifying a dictionary while iterating over it**](https://github.com/satwikkansal/wtfpython/blob/master/README.md#modifying-a-dictionary-while-iterating-over-it)
	  - [**Backslashes at the end of string**](https://github.com/satwikkansal/wtfpython/blob/master/README.md#backslashes-at-the-end-of-string)
	  - [**is is not what it is!**](https://github.com/satwikkansal/wtfpython/blob/master/README.md#is-is-not-what-it-is)
- I’m thinking of doing some fun follow on projects with this. More on that later.

**Brian #3:** [**Python Exercises**](https://www.ynonperek.com/2017/09/21/python-exercises/amp/)

- “… focus on the language itself and the standard library.”
- Some non-obvious Python exercises to help hone your Python skills, and possibly use in coding exercises of a job interview or maybe pre-interview screen.
- Topics
  - Basic syntax
  - Text Processing
  - OS Integration
  - Functions
  - Decorators & Generators
  - Classes, Modules, 
  - Exceptions, Lists, Dictionaries, Multiprocessing
  - & Testing! always including testing when ~~interviewing someone~~ practicing your coding.

**Michael #4:** [**Exploiting misuse of Python's "pickle"**](https://blog.nelhage.com/2011/03/exploiting-pickle/)

- If you program in Python, you’re probably familiar with the pickle serialization library, which provides for efficient binary serialization and loading of Python datatypes.
- Hopefully, you’re also familiar with the warning printed prominently near the start of pickle’s documentation:

*Warning: The pickle module is not intended to be secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.*


- this blog post will describe exactly how trivial it is to exploit such a service, using a simplified version of the code I recently encountered as an example. 
- Executing Code: So, what can we do with a vulnerable service? Well, pickle is supposed to allow us to represent arbitrary objects. An obvious target is Python’s `subprocess.Popen` objects!

**Brian #5:** [**A Complete Beginner's Guide to Django**](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)

- Lots of Django tutorials already, but this may appeal to folks with a more academic bent.
- Complete with wireframes, UML class hierarchies and use case diagrams.
- Series with 6 parts done, a 7th part planned, which will be the last part.
- Some fun comic like drawings, and lots of screenshots.

**Michael #6:** [**pypi-parker**](https://github.com/mattsb42/pypi-parker)

- Helper tooling for parking PyPI namespaces to combat typosquatting.
- pypi-parker lets you easily park package names on PyPI to protect users of your packages from typosquatting.
- Typosquatting is a problem: in general, but also on PyPI. 
- There are efforts being taken by pypa to protect core library names, but this does not (and really cannot and probably should not attempt to) help individual package owners.
- For example, `reqeusts` rather than `requests`, or `crytpography` rather than `cryptography`.
- Why? Self-serve is a good thing. Let's not try and get rid of that. Work with it instead.
- What? pypi-parker provides a custom distutils command park that interprets a provided config file to generate empty Python package source distributables. These packages will always throw an ImportError when someone tries to install them. You can customize the ImportError message to help guide users to the correct package.

Our news

Michael: 

- Just launched [**freemongodbcourse.com**](http://freemongodbcourse.com) Come and sign up to learn MongoDB and some Python
- [**Python3 usage has doubled in the past year**](https://twitter.com/dstufft/status/917703274966536192?t=1&cn=ZmxleGlibGVfcmVjc18y&refsrc=email&iid=94524f9448ff4f01905c15700bf2cc1c&uid=3098427092&nid=244+272699400) (thanks Donald Stufft) 


