# Python Bytes 59
Sponsored by DigitalOcean: **http://do.co/python**

**Brian #1:** **gc.freeze() and Copy-on-write friendly Python garbage collection**

- [Copy-on-write friendly Python garbage collection](https://engineering.instagram.com/copy-on-write-friendly-python-garbage-collection-ad6ed5233ddf) - Instagram
- [gc.freeze() now part of Python 3.7](https://github.com/python/cpython/pull/3705) - github pull request

**Michael #2:** [**SpeechPy - A Library for Speech Processing and Recognition**](https://github.com/astorfi/speechpy)

- A Library for Speech Processing and Recognition
- More foundation for data science than shooting out words.
- Based on MFCC (Mel Frequency Cepstral Coefficient)
  - The first step in any automatic speech recognition system is to extract features i.e. identify the components of the audio signal that are good for identifying the linguistic content and discarding all the other stuff which carries information like background noise, emotion etc. 
- Citation section is a nice touch

**Brian #3:** [**PyBites Code Challenges : Bites of Py**](https://codechalleng.es/)

- Like code katas, coding challenges you can do on your own.
- “Bites of Py are self contained 20-60 min Python (3.6) code challenges you can code and verify in the browser.”
- Use pytest to check answers
- See pytest output so you can partially solve challenges and see where it fails.
- BTW, min() takes a key, like sort() and sorted(). I learned that this morning.

**Michael #4:** [**How big is the Python Family**](https://py.checkio.org/blog/how-big-is-the-python-family/)

- CPython, Jython, IronPython, Python for .NET, Cython, PyPy, MicroPython, and recently Grumpy
- This is why I don’t like the word “Python interpreter” but rather use “Python runtime” even though it’s less common.

**Brian #5:** [**Dramatiq: simple task processing**](https://dramatiq.io/index.html)

- [Interview on Podcast.init](https://www.podcastinit.com/dramatiq-with-bogdan-popa-episode-141/)
- [Cookbook](https://dramatiq.io/cookbook.html#) included in documentation to get started pretty quick.
- Inspired by [Celery](http://www.celeryproject.org/), but probably a bit easier to get into if you are new to task processing.
- License is interesting

**Michael #6:** [**Controlling Python Async Creep**](https://hackernoon.com/controlling-python-async-creep-ec0a0f4b79ba)

- From friend of the show Cristian Medina
- Boundary between sync and async can get tricky
- The complication arises when invoking awaitable functions. Doing so requires an async defined code block or coroutine. A non-issue except that if your caller has to be async, then you can’t call it either unless its caller is async. Which then forces its caller into an async block as well, and so on. This is “async creep”.
- Solutions or techniques
	- Waiting for blocks of async code
		- The general guideline is to start with things that wait on I/O, like file or socket access, HTTP requests, etc.
		- Once you know which pieces to optimize, start identifying the ones that can run on top of each other.
		- Nice example using a web service
	- Use a thread
		- Next example creating a dedicated asyncio loop in the secondary thread
	- Mixing sync and async
		- Let’s look at something more complicated. What if you have a library or module where most functions can run in parallel, but you only want to do so if the caller is async?
		- This could prove useful to any python packages that are wanting to add support for asynchronous execution while still supporting legacy code. 

**Extra (michael)**: The **PyTennessee conference** will be held February 10-11, 2018. We recently announced our schedule ([https://www.pytennessee.org/schedule/](https://www.pytennessee.org/schedule/)), and tickets are on sale now ([https://pytn2018.eventbrite.com/](https://pytn2018.eventbrite.com/)). A smaller, regional conference is a great way to meet people, make new Python friends, and hear some great talks without having to fight the crowds of the larger conferences.

If anyone wants to buy a ticket and wants a 10% discount, they can use the code `PythonBytes` during checkout.

**In the news**

- Not much to do about this but pay attention: A critical design flaw in virtually all microprocessors allows attackers to dump the entire memory contents off of a machine/mobile device/PC/cloud server etc.
  - [https://twitter.com/nicoleperlroth/status/948684376249962496](https://twitter.com/nicoleperlroth/status/948684376249962496)
  - [https://www.nytimes.com/2018/01/03/business/computer-flaws.html](https://www.nytimes.com/2018/01/03/business/computer-flaws.html)
  - Probably excellent coverage on https://risky.biz/
- From NY Times:
	- *The two problems, called Meltdown and Spectre, could allow hackers to steal the entire memory contents of computers, including mobile devices, personal computers and servers running in so-called cloud computer networks.*
	- *There is no easy fix for Spectre, which could require redesigning the processors, according to researchers. As for Meltdown, the software patch needed to fix the issue could slow down computers by as much as 30 percent — an ugly situation for people used to fast downloads from their favorite online services.*

**Our news**

Michael: **Everything Bundle**: **[talkpython.fm/everything](https://talkpython.fm/everything)**

Includes Mastering PyCharm, Python 3: An Illustrated Tour, Intro to Ansible, and much more.