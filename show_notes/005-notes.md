# Python Bytes Episode 5

This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 5, recorded on December 5, 2016. In this episode we discuss Legacy Python vs Python and why words matter and Request's 5 Whys retrospective. [more] 

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

## News items

**#1 The Five Why’s of Requests 2.12**
[https://lukasa.co.uk/2016/11/Five_Whys_Requests_212/](https://lukasa.co.uk/2016/11/Five_Whys_Requests_212/)

- Some decision we made breaks a whole bunch of people’s code, and then each fix we attempt to make produces new, unforseen problems. These releases can be very dispiriting for project maintainers, because they make it seem like every time we try to improve something we get stuck on the mistakes our past selves made.
- Requests has had a few of these in the past, and right now we appear to be in the middle of another one. So far the 2.12 release series has caused problems for a number of users
- Problem: The current release of Requests, v2.12.2, breaks anyone who uses a URL with a scheme that isn’t “http” or “https” and who passes the params keyword to a Requests URL.
- Ultimately, our current issue comes from the fact that we have been inconsistent on our stance regarding URLs with weird schemes


**#2 Planning an Early Death for Python 2**
[https://carreau.github.io/posts/planning-an-early-death-for-python-2.html](https://carreau.github.io/posts/planning-an-early-death-for-python-2.html)
via [https://twitter.com/mbussonn](https://twitter.com/mbussonn)

- From Data Structure for Data Science workshop gathered at UC Berkeley's BIDS [Berkeley Institute for Data Science]
- Out of the discussion arose a topic that has long plagued the python community at large: code that requires legacy Python 2.7 is holding back the development of data-science toolsets and – by extension – the progress of data science as a whole. Python 2.7 was an important part of the history of scientific computing, but now it should be left as part of that history. Thus, we convened a small working group to plan an early death for Legacy Python.
- So what are the step we can do to push the transition forward?
- Choose your words:
  - Assume that Python 3 is just Python, and refer to Python 2 as legacy python.
  - Refer to Legacy Python in the past tense (reinforce the old and deprecated state of Legacy Python)
- Make your examples/documentation Python 3 only
  - Sprinkle with function annotation, and async/await keyword can help with communicating your example are Python 3 only…
- Ask user to reproduce but on up-to-date Python version
- Testing: Make sure that all the project you care about have continuous integration on Python 3


**#3 Simplifying complex business logic with Python's Kanren**
[https://jeffersonheard.github.io/2016/11/simplifying-complex-business-logic-with-pythons-kanren/](https://jeffersonheard.github.io/2016/11/simplifying-complex-business-logic-with-pythons-kanren/)

**#4 If Reddit were written from scratch today, which Python web framework would it use and why?**
[https://www.reddit.com/r/Python/comments/5gdckn/if_reddit_were_written_from_scratch_today_which/](https://www.reddit.com/r/Python/comments/5gdckn/if_reddit_were_written_from_scratch_today_which/) 

- Today (from SQLAlchemy's page): Reddit is one of the biggest social news aggregators on the internet. Reddit is built using Pylons, Mako templates, and a custom, non-ORM database abstraction layer built on SQLAlchemy Core.
- Ergo14: I would say that the most sane option would be Pyramid. It is faster than Django in tests and it doesn't repeat mistakes with threadlocals that flask or pylons did in past. I did some both small and medium-big (20+ million user applications) and it just feels right. It doesn't try to get in your way and give you magic solutions to your problems.
- Wting: I'm assuming you're talking about reddit at its current scale.
  Not Flask. Too many global variables and it's not thread safe (for async).
  Not Django. It's too opinionated and everything is in-housed for scaling reasons.
  My guess is Pyramid (the successor to Pylons). In fact, that's what reddit's current and future services are built with.
- So, Python web frameworks tend to cause a very strong, very subjective split in opinion.

**#5: Two testing related articles**

- **Getting started with pytest**
[https://jacobian.org/writing/getting-started-with-pytest/](https://jacobian.org/writing/getting-started-with-pytest/)
	- Anything that promotes pytest without presenting wrong information is good
- **The Best New Feature in unittest You Didn’t Know You Need**
[https://hackernoon.com/the-best-new-feature-in-unittest-you-didnt-know-you-need-e0d26c213dce](https://hackernoon.com/the-best-new-feature-in-unittest-you-didnt-know-you-need-e0d26c213dce)

	- First article I’ve seen explaining subtest
	- Subtest was added in Python 3.4

**#6 PyTone**
[https://www.luga.de/pytone/](https://www.luga.de/pytone/) 
PyTone is a music jukebox written in Python with a curses based GUI. While providing advanced features like crossfading and multiple players, special emphasis is put on ease of use, turning PyTone into an ideal jukebox system for use at parties.

Thx @kidpixo: [https://twitter.com/kidpixo/status/803345072414740480](https://twitter.com/kidpixo/status/803345072414740480) 


