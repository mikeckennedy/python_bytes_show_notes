# Python Bytes 15

This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 15, recorded on February 27, 2017.  [more]

**#1 Brian:**  **Packaging**
[**A Simple Guide for Python Packaging**](https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5#.b9ww4h4xt) ****by ****Jie Feng, [@flyfengjie](https://twitter.com/flyfengjie)

- very simple bare bones example and tutorial
- When you create a ‘.py’ file, that is a module.
- One or more modules in a folder with add a __init__.py file is a package (named via the folder)

[**How To Package Your Python Code**](http://python-packaging.readthedocs.io/en/latest/) ****by Scott Torborg, [@storborg](https://twitter.com/storborg)

- The example from the previous article comes from this.
- The best mid level explanation I’ve run across so far to describe packaging and distribution.
- Read the whole thing in a very short time.

**#2 Michael:** [**elasticpypi by**](https://github.com/khornberg/elasticpypi) [**Kyle Hornberg**](https://github.com/khornberg/elasticpypi)

- A mostly functional simple pypi service running on AWS.
- Runs over Elastic Search and AWS Lambda
- Compare to
  - pypiserver: https://pypiserver.readthedocs.io/en/latest/
  - devpi: http://doc.devpi.net/latest/
  - pypiserver: https://pypi.python.org/pypi/pypiserver

**#3 Brian:** **How to get Python new****s (our process)**

- [PythonBytes.fm](https://pythonbytes.fm), of course
* Twitter: 
	* Brian: [https://twitter.com/brianokken](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
	* Michael: [https://twitter.com/mkennedy](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
	* Talk Python: [https://twitter.com/TalkPython](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
	* Python Bytes: [https://twitter.com/PythonBytes](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
- [http://planetpython.org/](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z), check out the titles only link, as well as reading this feed with feedly or some other feed reader
- Newsletters:
	- Awesome Python: [https://python.libhunt.com/newsletter](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
	- Python Weekly: [http://www.PythonWeekly.com](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
	- Pycoders Weekly: [http://www.pycoders.com](http://www.pycoders.com/)
	- Import Python: [http://importpython.com/newsletter/](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
- Reddit: [https://www.reddit.com/r/Python/](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)
- Python Trending on GitHub: [https://github.com/trending?l=python](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)

**#4 Michael:** [**Curio - The coroutine concurrency library**](https://github.com/dabeaz/curio)**, by** **David Beazley,** [**@dabeaz**](https://twitter.com/dabeaz)

- Curio is a library for performing concurrent I/O and common system programming tasks such as launching subprocesses and farming work out to thread and process pools.
- It uses Python coroutines and the explicit async/await syntax introduced in Python 3.5.
- Based on cooperative multitasking and existing programming abstractions such as threads, sockets, files, subprocesses, locks, and queues.
- Only works on POSIX systems
- The Big Question: Why?
	- Python 3.4 and 3.5 have added major new paradigms for async programming.Curio takes full advantage of these features and is not encumbered by issues of backwards compatibility with legacy Python code written 15 years ago.
		- Curio is a ground-up implementation that takes a different approach to the problem while relying upon known programming techniques involving sockets and files.
		- The implementation of Curio aims to be simple. The API for using Curio aims to be intuitive.

**#5 Brian:** [**Pandas switching to use pytest as testing framework**](https://www.reddit.com/r/Python/comments/5v6xsf/pandas_switching_to_use_pytest_as_testing/)

- Interesting look at the challenges and discussion of moving a large, highly visible project

[**#6 Michael: Talk Python #100: Python past, present, and future with Guido van Rossum**](https://talkpython.fm/episodes/show/100/python-past-present-and-future-with-guido-van-rossum)

- Excellent look back and forward with Guido
- Conversation [on reddit](https://www.reddit.com/r/Python/comments/5vmvtj/python_past_present_and_future_with_guido_van/)
- Conversation [on hackernews](https://news.ycombinator.com/item?id=13710803)
- We touch on
	- How he got started
	- Early influences on Python
	- Why Python succeeded
	- How are we doing with: Diversity and moving to Python 3?
	- His favorite features of Python 3
	- Converting legacy code via mypy: [http://mypy-lang.org/](https://paper.dropbox.com/doc/Python-Bytes-16-5K4HDCHfQnVLqOKkhXg6Z)

**In o****ther** **n****ews** **(as in our news)**

- [Test & Code 27 is out, a great talk with Mahmoud Hashemi](http://testandcode.com/27) on different levels of testing, the role of testing in SW development, TDD, and what he’s been up to lately. Test & Code migrating to [testandcode.com](http://testandcode.com), to separate writing and podcast into two sites. When it gets cleaned up a little, I’ll forward podcast related links from [pythontesting](http://pythontesting.net) to [testandcode](http://testandcode.com).

 

- [The pytest book](http://pythontesting.net/book/pytest) got sent out to a few reviewers, and we have a title and some cover art options. It’s getting exciting. The rest of the reviewers will get the book when all chapters have gone through at least one editor iteration.
