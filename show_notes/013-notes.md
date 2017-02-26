# Python Bytes 13
This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 13, recorded on February 13, 2017. In this episode we discuss Python making the move to GitHub and Dropbox stepping back from Pyston. [more]

This episode was brought to you by [Metis: The Data Science Bootcamp company](http://thisismetis.com/talkpython).

[**#1 Brian:Pyston no longer sponsored by Dropbox**](https://blog.pyston.org/2017/01/31/pyston-0-6-1-released-and-future-plans/)

Personal follow up post by Kevin Modzelewski
[http://blog.kevmod.com/2017/02/personal-thoughts-about-pystons-outcome/](http://blog.kevmod.com/2017/02/personal-thoughts-about-pystons-outcome/)

- Pyston (pronounced piston) is a Python JIT implementation started at Dropbox
- It was based on CPython and supported a bunch of 2.7, but wasn’t complete.
- Bottom line: It’s open source, and the repo will be left for whoever wants to work on it. But the core developers from Dropbox won’t be working on it, and Dropbox won’t be spending any more time/money on it.

[**#2 Michael: CPython is coming to GitHub**](https://github.com/python/cpython)

- Mailing list announcment: [https://mail.python.org/pipermail/python-dev/2017-February/147341.html](https://mail.python.org/pipermail/python-dev/2017-February/147341.html)
- Reddit discussion [https://www.reddit.com/r/Python/comments/5ssx9w/cpython_moves_to_github_this_friday/](https://www.reddit.com/r/Python/comments/5ssx9w/cpython_moves_to_github_this_friday/)

Brett Cannon’s excellent background story: [https://snarky.ca/the-history-behind-the-decision-to-move-python-to-github/](https://snarky.ca/the-history-behind-the-decision-to-move-python-to-github/)

- Interesting that some people (voiced via reddit) sadness about leaving Hg…
- 2006: Python moves to SVN
- 2011: Python moves to Hg
- 2017: Python moves to GitHub
- By 2014 it had become obvious to some of us that the Python development process had in fact become a burden. The rate at which patches were being submitted was much greater than the rate at which they were being reviewed. This was leading to external contributors getting frustrated because they would put in the effort to write a patch but would occasionally end up with waiting years for a review from a core developer.
- I wanted was the ability to review an external contribution -- from submission to commit -- all on a tablet while at a beach with WiFi (which I actually have in Vancouver so this wasn't entirely a silly request). My thinking was that if we got the process to be that simple, core developers could do a review at lunch time while at work, or when they had some down time at home without having to be on some special machine that had their SSH keys installed on it.


[**#3 Brian: Using functional programming in Python like a boss: Generators, Iterators and Decorators**](http://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/func_py/func_py.ipynb)

- I’m liking the trend of more Jupiter notebook based articles. This one is a pretty gentle introduction into functions, generators, iterators, decorators, containers, and how they all work together to make your code more expressive.

[**#4 Michael: It's metaclasses all the way down**](https://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/meta_alltheway/meta_alltheway.ipynb)

- What is metaprogramming? Metaprogramming is a technique of writing computer programs that can treat themselves as data, so you can introspect, generate, and/or modify them while running
- Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don’t (Tim Peters)
- However: The potential uses for metaclasses are boundless. Some ideas that have been explored include logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization. 
- Nice examples: 
  - Django ORM models
  - Abstract vehicle class

[**#5 Brian: Lambda Functions in Python: What Are They Good For?**](https://dbader.org/blog/python-lambda-functions)
- Lambdas are part of the language, and if used sparingly and in the right context, can make your code more readable. It’s super important for intermediate and experienced Python folks to understand lambdas and not be afraid of them.
- This article is a good tutorial on them.
- When you finally grok them, you might be tempted to use them all over the place. Dan presents a couple of places where using lambdas is a bad choice:
  - creating class methods. Definitions are definitely preferred over assigning lambdas to attributes. 
  - generating a list with `list(fliter(<lambda expression>, <iterable>))` . I agree with Dan that comprehensions are way easier to read.

[**#6 Michael: Multi-threaded SQLite without the OperationalErrors**](http://charlesleifer.com/blog/multi-threaded-sqlite-without-the-operationalerrors/)

- Unless you are very diligent about keeping your write transactions as short as possible, you can easily wind up with one thread accidentally holding a write transaction open for an unnecessarily long time. 
- I've had success using a very simple approach: I eliminate the possibility of lock contention by dedicating one thread to the task of issuing all writes for the application.
- The entire source listing can be found here, if you're curious: [https://github.com/coleifer/peewee/blob/master/playhouse/sqliteq.py](https://github.com/coleifer/peewee/blob/master/playhouse/sqliteq.py)

[**Followup:**](https://www.reddit.com/r/Python/comments/5ryiq7/sticking_with_flask_vs_switching_to_one_of_the/) [**J**](https://www.reddit.com/r/Python/comments/5ryiq7/sticking_with_flask_vs_switching_to_one_of_the/)[**apronto not production ready**](https://www.reddit.com/r/Python/comments/5ryiq7/sticking_with_flask_vs_switching_to_one_of_the/):
“Japronto author here: As stated in the README you should not build anything serious with Japronto now because it's gonna probably eat your laundry. Remember it's hand coded in C and this needs a lot of testing. On the top of that I plan to do several iterations of API changes in a largely incompatible ways. I hope though it's gonna make a serious player in the field one day.

If you wanna a decent async framework then go with aiohttp or Sanic. If you are gonna do typical REST app frontend to a database go with Flask or Pyramid. If you need a scaffolded admin go with Django.”