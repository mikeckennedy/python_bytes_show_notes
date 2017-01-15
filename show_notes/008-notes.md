# Python Bytes 8

This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 8, recorded on **January 10th, 2017**. In this episode we discuss **Python is Grumpy, avoiding burnout, Postman for API testing and more**. [more]

**#1 (Brian): [Jessica McKellar, "Breaking The Rules", PyBay2016](https://youtu.be/9UnMZYMaosw)[
](https://youtu.be/p33CVV29OG8)**

- Jessica 
  - was directory of PSF for several years, was involved with Boston Python UG, is diversity chair for PyCon, is an engineering director at dropbox
- Powerful keynote
  - Her extra work with Python is not about Python, it’s about studying systems.
  - “Learning how to program changes the way you think about, debug, and interact with the world”
  - “You learn a set of rules to build software, … then you learn that you can change the rules.”
  - “Programmers master a system they know they can change.”
  - “This comes from the tenets of free software.”
  - “We take for granted that changing something to make it better is just a thing you do when you need to.”
- This can and should carry over to the rest of your life.
- Jessica takes this idea and applies it to politics, voting, and polling stations, and ran a polling station herself.
- That’s pretty incredible. About half the time is Q&A with some great questions.
- Listen to this talk and apply it to every part of your work and life.

**#2 (Michael): [Grumpy is a Python to Go](https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html)**

- By Dylan Trotter from YouTube
- Grumpy is a Python to Go source code transcompiler and runtime.
- intended to be a near drop in replacement for CPython 2.7
- The key difference is that it compiles Python source code to Go source code which is then compiled to native code, rather than to bytecode. This means that Grumpy has no VM.
- 6,000 stars on Github in 3 weeks
- Look for him on Talk Python To Me (episode 95?)

**#3 (Brian): [Finding dead code with Vulture - Dougal Mathews](http://www.dougalmatthews.com/2016/Dec/16/finding-dead-code-with-vulture/)**

- `pip install vulture` , then `vulture some/directory/of/code` 
- Reports unused code.
- vs coverage.py. You can get similar information from coverage if your test suite or the code you run during the coverage inspection is fairly complete. However, what if a unit test is the only thing calling some function? vulture allows you to exclude your test code when looking for unused code.
- vs static analyzers like flake8. With some of my own code that I have in progress, vulture found the same stuff that flake8 did. However, if you are only looking for dead code, it’s easier to find with vulture if you have other flake8 violations. Also some folks don’t like style checkers.
- I’d like to hear what other people think. But I like the idea of having a focused dead code tool. And vulture is a great name for such a tool.

**#4 (Michael): [Postman: Developing APIs is hard. Postman makes it easy](https://www.getpostman.com/)**

- A powerful GUI platform to make your API development faster & easier, from building API requests through testing, documentation and sharing.
- Cross platform and free
- A simple and effective way to share details about your public-facing API 
- Testing
  - Run Postman Collections directly from the command line
  - integrating with continuous integration servers and builds
  - Monitor uptime, performance and correctness of your APIs.
- Notable mention goes to [paw.cloud](https://paw.cloud/) (macOS only)

**#5 (Brian): [The Reality of Developer Burnout](https://www.kennethreitz.org/essays/the-reality-of-developer-burnout)[ by ](https://www.kennethreitz.org/essays/the-reality-of-developer-burnout)[Kenneth Reitz](https://www.kennethreitz.org/essays/the-reality-of-developer-burnout)**

- Author of [Requests](http://docs.python-requests.org/en/master/) and of [Maya (datetime for humans)](https://github.com/kennethreitz/maya), covered in the [last episode](http://pythonbytes.fm/7).
- This is an article about getting overwhelmed as a maintainer of an open source project. But applies to anyone supporting a tool, even for your coworkers. And really applicable to all sorts of developer burnout. 
- Advice:
  - Keep producing, but stop consuming so much on social networks. twitter, reddit, etc.
  - Delegate more.
  - Have hobbies other than coding
- side note:
  - On the maya github page, I noticed a link [saythanks.io](https://saythanks.io/), a Kenneth project where you can set up a way for people to just send you a thank-you note. I think this is cool. I wrote about [the power of “thank you”](http://pythontesting.net/community/power-of-thank-you/) a few years ago. It’s really important in open source, and really all the time. 

**#6 (Michael): [Jinja 2.9 Released by Armin Ronacher](https://www.palletsprojects.com/blog/jinja-29-released/)**

- From Hugh Blandford (thanks!)
- New release, 2.9 codename "Derivation" of the Jinja template engine for Python is out
- While Jinja2 supported Python 3 for years now it never really embraced functionality that the language provides on 3.x that it does not do on 2.x
  - However 3.6 now added async generators which permits Jinja2 to fully support the async and await keywords on 3.6 and later.
  - In particular it means that you can now return coroutines from functions passed to Jinja2 templates and the template engine will automatically await them.
  - Likewise all filters were updated to work with iterators as well as async iterators alike.
