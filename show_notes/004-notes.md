This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 4: recorded on November 28, 2016. In this episode we cover the case for Python 3, asyncio, pyston, pydoc.io, and q. [more] 

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

## News items

[**The Case FOR Python 3**](https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/)
- [https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/](https://eev.ee/blog/2016/11/23/a-rebuttal-for-python-3/)

    >> "It's as simple as that. If you learn Python 2, then you can still work with all the legacy Python 2 code in existence **until Python dies or you (hopefully) move on**. But if you learn Python 3 then your future is very uncertain. You could really be learning a dead language and end up having to learn Python 2 anyway." -- Zed S.

- This is harmful to the Python community.
- Let's stop recommending this book and stop elevating this guy's work
- "Arguments" from Zed:
    - Not In Your Best Interests: "The Python project’s efforts to convince you to start with Python 3 are not in your best interest, but, rather, are only in the best interests of the Python project."
    - You Should Be Able to Run 2 and 3 (in the same process). The fact that no one has (yet) written a Python 3 interpreter that can simultaneously run Python 2 in the same process means Python 3 is not Turing complete
    - Difficult To Use Strings: "The strings in Python 3 are very difficult to use for beginners. In an attempt to make their strings more “international” they turned them into difficult to use types with poor error messages."
    - Final analysis: 
        - You can’t add b"hello" to "hello".
        - Too many formatting choices for strings
        - Bytes aren't automatically decoded to strings
    - Therefore: All newbies should avoid Python 3 like the plague - it will curse your career and cloud your judgement.

[**Reddit discussion of a Feb article on "AsyncIO for the Working Python Developer"**](https://www.reddit.com/r/Python/comments/5ecj2o/asyncio_for_the_working_python_developer_just/?st=IVYVG4CT&sh=34a66cab)
- Article: [AsyncIO for the Working Python Developer](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e#.ft56qol06)

- Article is a nice introduction, but uses Python 3.4 syntax
- Interesting to note that no one in the reddit comments suggests a better 3.5 tutorial. Is async/await just too confusing for a 3.5 intro article? Or is it so simple that no one has thought it needs a tutorial. 
- 23 page article / tutorial on Python 3.4's asyncio
- Not covering Python 3.5's async / await, but great gateway article
- Here’s a call for action. Someone write a similar article but with 3.5+ syntax. Also could we show examples without sleep calls. Sleep is such a lame way to show “do some actual work”. Maybe use a producer/consumer or reader/writer example or something.


[**Pyston 0.6 released**](https://blog.pyston.org/2016/11/11/pyston-0-6-released/)

- Pyston is an open source Python implementation that aims to be both highly compatible and high-performance. 
- It uses modern JIT techniques and natively supports many CPython C extension modules. 
- Pyston is sponsored by Dropbox, and is pronounced "piston".
- main goal was to reduce the overall memory footprint.  It also contains a lot of additional smaller changes for improving compatibility and fixing bugs.
  - We also spent time on making it easier to replace CPython with Pyston, such as by more closely matching its directory structure 
  - following its ‘dict’ ordering.  
  - We can now, for example, run pip and virtualenv unmodified, without requiring any upstream patches like other implementations do.
- Unclear how much of a research project vs an actual project this is at the moment

[**Announcing pydoc.io**](http://blog.readthedocs.com/announcing-pydoc-io/)
- Automatic API documentation from pypi repositories.
- Pydoc.io will eventually auto-generate API reference documentation for every package on PyPI.

[**What one thing took your Python to the next level**](https://www.reddit.com/r/Python/comments/5f6ev8/what_one_thing_took_your_python_to_the_next_level/)

1. Mastering generators
2. Understanding how iteration really works in Python opens up many possibilities for elegant, high performance code. Use iPython. Learn that for does tuple unpacking; play with zip, enumerate, all, any; take a look at the itertools module
3. Unit tests! Pytest in particular! Gives you a whole new perspective on your code and dammit, it's so satisfying to get all those green OKs!
4. list comprehensions
5. For me, all the work of David Beazley, in particular [http://www.dabeaz.com/coroutines/](http://www.dabeaz.com/coroutines/)

[**q : Quick-and-dirty debugging output for tired programmers**](https://pypi.python.org/pypi/q)

- Learned about it from a tweet from Luciano Ramalho.
- [https://twitter.com/ramalhoorg/status/802673217081065472](https://twitter.com/ramalhoorg/status/802673217081065472)
- 5 min lightning talk: [https://youtu.be/OL3De8BAhME?t=25m20s](https://youtu.be/OL3De8BAhME?t=25m20s) 
- q on pypi: [https://pypi.python.org/pypi/q](https://pypi.python.org/pypi/q)

## Our personal news

### Michael
- Follow up: [https://www.python.org/dev/peps/pep-0494/](https://www.python.org/dev/peps/pep-0494/) Python 3.6 Release Schedule Final date: 2016-12-16

### Brian
- Hard at work on pytest book that is a followup to current [Python Testing book](http://pythontesting.net/book).
