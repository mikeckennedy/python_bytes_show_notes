# Python Bytes 71

Sponsored by DigitalOcean: **[do.co/python](https://do.co/python)**

**Trey #1:** [**The Conservative Python 3 Porting Guide**](https://portingguide.readthedocs.io/en/latest/)

- by [various Red Hat folks](https://github.com/fedora-python/portingguide/graphs/contributors) mostly
- Python 2 is coming to the end of its life on January 1, 2020. Are you ready?
- This is one of the best guides I’ve found to porting your code from Python 2 to Python 3
- One of the issues with many of the Python 3 porting guides is that the old ones recommend dropping Python 2 support suddenly, which isn’t recommended anymore.
- I do wish this guide recommended the future library instead of python-modernize. They’re both great, but modernize is a little less focused on writing things the Python 3 way and a little more focused on just getting your code working in both 2 and 3.

**Michael #2:** [**World-Class Software Companies That Use Python**](https://realpython.com/world-class-companies-using-python/)

- by [Jason Reynolds](https://realpython.com/world-class-companies-using-python/#author) 
- While it’s easy to see how you can tinker with Python, you might be wondering how this translates to actual business and real world applications.
- **Industrial Light and Magic**
	- The studio has used Python in multiple other facets of their work. Developers use Python to track and audit pipeline functionality, maintaining a database of every image produced for each film.
- **Google**
	- In the beginning, the founders of Google made the decision of “Python where we can, C++ where we must.”
	- Currently powers YouTube among other things
- **Facebook**
	- Ensures that the infrastructure of Facebook is able to scale efficiently
- **Instagram**
	- the Instagram engineering team boasted that they were [running the world’s largest deployment of the Django web framework, which is written entirely in Python](https://engineering.instagram.com/web-service-efficiency-at-instagram-with-python-4976d078e366).
	- Instagram’s engineering team has invested time and resources into keeping their Python deployment viable at the massive scale ([~800 million monthly active users](https://www.statista.com/statistics/253577/number-of-monthly-active-instagram-users/)) they’re operating at.
	-  [PyCon 2017 keynote talk](https://www.youtube.com/watch?v=66XoCk79kjM) by Lisa Guo and Hui Ding
- **Spotify**
	- This music streaming giant is a [huge proponent of Python](https://labs.spotify.com/2013/03/20/how-we-use-python-at-spotify/), using the language primarily for data analysis and back end services. 
	- On the back end, there are a large number of services that all communicate over 0MQ, or [ZeroMQ](http://zguide.zeromq.org/page:all), an open source networking library and framework that is written in Python and C++(among other languages).
- **Quora**
	- choosing to use Python where they could because of its ease of writing and readability, and implemented C++ for the performance critical sections. 
	- They got around Python’s lack of typechecking by writing unit tests that accomplish much the same thing.
	- Another key consideration for using Python was the existence of several good frameworks at the time including Django and Pylons. 
- **Netflix**
	- Lots of infrastructure and ops work done via Python https://talkpython.fm/episodes/show/16/python-at-netflix
- **Dropbox**
	- Dropbox makes heavy use of Python
	- Guido van Rossum works there!
	- Lots of open source projects
	- Client app in Python too
- **Reddit**
	- This website had 542 million visitors every month across 2017, making it the fourth most visited website in the United States and seventh most visited in the world. 
	- In 2015, there were 73.15 million submissions and 82.54 billion pageviews. 
	- Behind it all, forming the software backbone, was Python.

**Trey #3:** [**Stop Writing Classes**](https://www.youtube.com/watch?v=o9pEzgHorH0)

- by [Jack Diederich](https://twitter.com/jackdied)
- This is one of my favorite PyCon talks to recommend to folks switching to Python from other programming languages. I especially like to recommend this talk to folks moving to Python from Java and C++.
- This is kind of an old talk. It's from 2012, so it's from the days of Python 2 but everything in it is still *very applicable today*.
- One of the great things about this talk is it doesn’t just show times that you should write functions instead of classes, it also shows an example or two of when classes really make sense.
- The big advice from this talk: if you have a class that only has two methods and one is the initializer, you probably need a function instead.

**Michael #4:** [**PyPi.org is alive**](https://pypi.org/)

- For the LONGest time, pypi has been run out of [http://pypi.python.org/pypi](http://pypi.python.org/pypi)
- Now the new version of pypi is out at pypi.org
- Rewritten in Pyramid
- Do you want to contribute? Now the barriers have come down
- **[Tweet with graphs](https://twitter.com/EWDurbin/status/974424840429080578)**

**Trey** **#5:** [**Pragmatic Unicode**](https://nedbatchelder.com/text/unipain.html)

- by [Ned Batchelder](https://twitter.com/nedbat)
- Another PyCon 2012 talk that is still relevant today, though it does use quite a bit of Python 2 syntax
- Ned describes the unicode sandwich in this talk. Talks with good metaphors really help shape your mental model of a topic. This was the talk that helped me really understand the unicode vs bytes issue that Python 3 largely solves for us (or at least forces us to do so upfront).

**Michael #6:** [**pygame on pypy usable**](https://renesd.blogspot.com/2018/03/pygame-on-pypy-usable.html)

- via René Dudfield
- 0.5x to 30x the speed
- That is pygame (same one that runs on cpython), works on pypy through its C extension API
- **This is exciting because**:
	- pure python code being fast on pypy(after warmup), also mixed with the fast bits in C/asm.
	- cpyext is getting faster in pypy. There is already work and discussion towards it being faster than CPython.
	- maintaining one pygame code base is easier than maintaining several (pygame cffi/ctypes/cython, ...).
	- with one code base it should be fast on both pygame, and pypy(in time).
- **Where it can be slower**: if you are going into C code for a lot of small operations. Like when using lots of pygame.Rect in a tight loop. This is because (currently) the cost of going from PyPy code into and out of CPython API code (like pygame) is a bit slow.
- Ray tracing in PyGame:
	- On PyPy - 18.6 seconds.
	- On Python 2.7 - 9 minutes, 28.1 seconds (30x slower)

**Follow up and other news**

**Michael:**
**#100DaysOfCode in Python course**: **[talkpython.fm/100days](https://talkpython.fm/100days)**

**Trey:** 
Python Morsels: **[pythonmorsels.com](http://pythonmorsels.com)**

