# Python Bytes 266

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** **Python** [**glossary**](https://docs.python.org/3/glossary.html) **and** [**FAQ**](https://docs.python.org/3/faq/)

- Inspired by a tweet by Trey Hunner that referenced the glossary
- [glossary](https://docs.python.org/3/glossary.html)
    - All the Python and programming terms in one place
    - Often refers to other parts of the documentation.
    - Forget what an “abstract base class” is? [Just look it up](https://docs.python.org/3/glossary.html#term-abstract-base-class) 
- [FAQ](https://docs.python.org/3/faq/)
    - Has sections on
        - [General Python](https://docs.python.org/3/faq/general.html)
        - [Programming](https://docs.python.org/3/faq/programming.html)
        - [Design and History](https://docs.python.org/3/faq/design.html)
        - [Library and Extension](https://docs.python.org/3/faq/library.html)
        - [Extending/Embedding](https://docs.python.org/3/faq/extending.html)
        - [Python on Windows](https://docs.python.org/3/faq/windows.html)
        - [Graphic User Interface](https://docs.python.org/3/faq/gui.html)
        - [“Why is Python Installed on my Computer?”](https://docs.python.org/3/faq/installed.html)
    - Some decent reading here, actually.
    - Example
        - [What is the difference between arguments and parameters?](https://docs.python.org/3/faq/programming.html#id15) - that’s under Programming

**Michael #2:** [Any.io](https://anyio.readthedocs.io/en/stable/basics.html)

- Learned about it via [asyncer](https://github.com/tiangolo/asyncer)
- AnyIO is an asynchronous networking and concurrency library that works on top of either [asyncio](https://docs.python.org/3/library/asyncio.html) or [trio](https://github.com/python-trio/trio). 
- It implements trio-like [structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency) (SC) on top of asyncio
- Works in harmony with the native SC of trio itself
- Check out [the features](https://anyio.readthedocs.io/en/stable/index.html#features)
- AnyIO also comes with its own [pytest](https://docs.pytest.org/en/latest/) plugin which also supports asynchronous fixtures.




**Brian #3:** [**Vaex**](https://github.com/vaexio/vaex) [**:**](https://github.com/vaexio/vaex) [**a high performance Python library for lazy Out-of-Core DataFrames**](https://github.com/vaexio/vaex)

- suggested by Glen Ferguson
- “Vaex is a python library for lazy **Out-of-Core DataFrames** (similar to Pandas), to visualize and explore big tabular datasets.”
- out-of-core: “The term *out-of-core* typically refers to processing data that is too large to fit into a computer’s main memory.” - from [machinelearning.wtf](https://machinelearning.wtf/terms/out-of-core/), a Machine Learning Glossary site. 
    - nice tie in, right?
- Vaex uses memory mapping, a zero memory copy policy, and lazy computations.
- There’s a great intro in the form of a presentation from [SciPy 2019](https://www.youtube.com/watch?v=ELtjRdPT8is)
- Key features
    - 



**Michael #4:** [**Django Community Survey Results**](https://lp.jetbrains.com/django-developer-survey-2021-486/)

- Only 15% of Django developers use it ONLY for work, while two thirds use it both for work and for personal, educational, or side projects.
- Majority use latest Django
- Most devs upgrade every stable release
- Postgres is the primary DB (MongoDB is nowhere in sight)
- Most sites have Redis caching tiers

**Michael #5: Extra, Extra, Extra, Extra:**

- [Django security releases issued: 4.0.1, 3.2.11, and 2.2.26](https://www.djangoproject.com/weblog/2022/jan/04/security-releases/)
- [Static Sites with Sphinx and Markdown](https://talkpython.fm/sphinx) course by Paul Everitt is now out
- [CalDigit Thunderbolt 4 Element Hub](https://www.caldigit.com/thunderbolt-4-element-hub/) review (more info [Video by Doc Rock](https://www.youtube.com/watch?v=OEhnTed0MSk), get it on [Amazon here](https://amzn.to/34wpvUx))
- [StreamDeck setup](https://twitter.com/mkennedy/status/1479523408064909312) for our live streams
- [Michael’s PyBay HTMX talk](http://) is up
- [Python Web Conf 2022](https://2022.pythonwebconf.com/) - I’ll be speaking there and we’re media sponsors of the conference so use code **PythonBytes@PWC2022** for 15% off, March 21-25.
- [PyCascades 2022](https://2022.pycascades.com/) is also happening soon, February 5th-6th, 2022

**Extras** 

Brian:

- Just a fun riddle my kid asked me the other day I want to share. It’s a mental math problem that I thought was fun.

**Joke:** 

![](https://paper-attachments.dropbox.com/s_67096A17659F83D1A0CAC669BBCB58FEC5006BC10F41A506FBC5F05857E4E9C9_1641757150692_Screen_Shot_2021-11-07_at_8.15.29_AM.png)

