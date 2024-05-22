# Python Bytes 265


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: Matt Kramer ([@__matt_kramer__](https://twitter.com/__matt_kramer__))

**Michael #1: Survey results**

- Question 1:
![](https://paper-attachments.dropbox.com/s_3370DBC8B17DDD025FB99F5F8E61DB76EED1D134B78707EFC4676F383C096EF5_1641344127195_q1.png)


Question 2:

![](https://paper-attachments.dropbox.com/s_3370DBC8B17DDD025FB99F5F8E61DB76EED1D134B78707EFC4676F383C096EF5_1641344142950_q2.png)

- In terms of too long, the “extras” section has started at these times in the last 4 episodes:
  - 39m, 32m, 35m, and 33m ~= 34m on average 

**Brian #2:** **Modern attrs API**

- [attrs overview](https://www.attrs.org/en/latest/overview.html) now focus on using `@define`
- History of attrs article: [import attrs](https://hynek.me/articles/import-attrs/), by Hynek
  - predecessor was called `characteristic`. 
  - A discussion between Glyph and Hynek in 2015 about where to take the idea.
  - `attrs`  popularity takes off in 2016 after a post by Glyph: [*‌The One Python Library Everyone Needs*](https://glyph.twistedmatrix.com/2016/08/attrs.html)
	- In 2017 people started wanting something like attrs in std library. Thus PEP 557 and dataclasses. Hynek, Eric Smith, and Guido discuss it at PyCon US 2017. 
    - dataclasses, with a subset of attrs functionality, was introduced in Python 3.7. 
    - Types take off. attrs starts supporting type hints as well, even before Python 3.7
    - Post 3.7, some people start wondering if they still need attrs, since they have dataclasses.
    - `@define`, `field()` and other API improvements came with attrs 20.1.0 in 2020.
    - attrs 21.3.0 released in December, with what Hynek calls “Modern attrs”.
- OG attrs:

```python
import attr

@attr.s
class Point:
  x = attr.ib()
  y = attr.ib()
```

- modern attrs:
```python
from attr import define

@define
class Point:
  x: int
  y: int
```

- Many reasons to use attrs listed in [Why not…](https://www.attrs.org/en/latest/why.html), which is an excellent read.
  - why not dataclasses?
    - less powerful than attrs, intentionally
      - attrs has validators, converters, equality customization, …
    - attrs doesn’t force type annotation if you don’t like them
    - slots on by default, dataclasses only support slots in Python 3.10 and are off by default
        - attrs can and will move faster
    - See also comparisons with pydantic, named tuples, tuples, dicts, hand-written classes

**Matt** **#3:** [**Crafting Interpreters**](https://craftinginterpreters.com/)

- Wanting to learn more about how Python works “under the hood”, I first read Anthony Shaw’s [CPython internals](https://realpython.com/products/cpython-internals-book/) book
  - A fantastic, detailed overview of how CPython is implemented
- Since I don’t have a formal CS background, I found myself wanting to learn a bit more about the fundamentals
  - Parsing, Tokenization, Bytecode, data structures, etc.
- Crafting Interpreters is an incredible book by Bob Nystrom (on Dart team at Google)
- Although not Python, you walk through the implementation of a dynamic, interpreted language from scratch
- Implement same language (called lox) in two interpreters
  - First a direct evaluation of Abstract Syntax Tree, written in Java
  - Second is a bytecode interpreter, written from the ground up in C, including a compiler
- Every line of code is in the book, it is incredibly well-written and beautifully rendered
- I highly recommend to anyone wanting to learn more about language design & implementation


**Michael #4:** [**Yamele - A schema and validator for YAML**](https://github.com/23andMe/Yamale)

- via Andrew Simon
- A basic schema:
```
name: str()
age: int(max=200)
height: num()
awesome: bool()
```
- And some YAML that validates:

```
name: Bill
age: 26
height: 6.2
awesome: True
```

- Take a look at the [Examples](https://github.com/23andMe/Yamale#examples) section for more complex schema ideas.
- ⚠️ Ensure that your schema definitions come from internal or trusted sources. Yamale does not protect against intentionally malicious schemas.

**Brian #5:** [**pympler**](https://pympler.readthedocs.io/en/latest/)

- Inspired by something Bob Belderbos wrote about sizes of objects, I think.
- “Pympler is a development tool to measure, monitor and analyze the memory behavior of Python objects in a running Python application.
- By pympling a Python application, detailed insight in the size and the lifetime of Python objects can be obtained. Undesirable or unexpected runtime behavior like memory bloat and other “pymples” can easily be identified.”
- 3 separate modules for profiling
  - [asizeof](https://pympler.readthedocs.io/en/latest/asizeof.html#asizeof) module provides basic size information for one or several Python objects
  - [muppy](https://pympler.readthedocs.io/en/latest/muppy.html#muppy) is used for on-line monitoring of a Python application
  - [Class Tracker](https://pympler.readthedocs.io/en/latest/classtracker.html#classtracker) provides off-line analysis of the lifetime of selected Python objects.
- asizeof is what I looked at recently
  - In contrast to `sys.getsizeof`, `asizeof` sizes objects recursively. 
  - You can use one of the [asizeof](https://pympler.readthedocs.io/en/latest/asizeof.html#asizeof) functions to get the size of these objects and all associated referents:

```
>>> from pympler import asizeof
>>> obj = [1, 2, (3, 4), 'text']
>>> asizeof.asizeof(obj)
176
>>> print(asizeof.asized(obj, detail=1).format())
[1, 2, (3, 4), 'text'] size=176 flat=48
  (3, 4) size=64 flat=32
  'text' size=32 flat=32
  1 size=16 flat=16
  2 size=16 flat=16
```

- “Function **flatsize** returns the *flat size* of a Python object in bytes defined as the *basic size* plus the *item size* times the *length* of the given object.”

**Matt** **#6:** [**hvPlot Interactive**](https://hvplot.holoviz.org/user_guide/Interactive.html#)

- hvPlot is a high-level plotting API that is part of the PyData ecosystem, built on HoloViews
- My colleague Phillip Rudiger recently gave a talk at PyData Global on a new `.interactive` feature
- [Here’s an announcement in the HoloViz forum](https://discourse.holoviz.org/t/pydata-2021-build-polished-data-driven-applications-directly-from-your-pandas-or-xarray-pipelines/3017)
- Allows integration of widgets directly into `pandas` analysis pipeline (method-chain), so you can add interactivity to your notebook for exploratory data analysis, or serve it as a [Panel app](https://panel.holoviz.org/)
- [Gist & video](https://gist.github.com/MarcSkovMadsen/ffb273636dced88705c8c88d5ee28f23) by Marc Skov Madsen

**Extras** 

Michael:

- [**Typora app**](https://typora.io/), recommended!
- [**Congrats Will**](https://twitter.com/willmcgugan/status/1474342602665304076?s=12)
- Got a chance to solve a race condition with [**Tenacity**](https://tenacity.readthedocs.io/en/latest/)
- New [**project management at GitHub**](https://docs.github.com/en/issues/trying-out-the-new-projects-experience)

Matt: 

- Check out new [Anaconda Nucleus Community](https://community.anaconda.cloud/) forums!
- We’re hiring, and remote-first. Check out [anaconda.com/careers](http://anaconda.com/careers)
- [Pre-compiled packages now available for Pyston](https://blog.pyston.org/2021/12/07/pre-compiled-packages-now-available-for-pyston/)
- We have an upcoming webinar from Martin Durant: [When Your Big Problem is I/O Bound](https://event.on24.com/wcc/r/3544490/FB8F3D77C106DBA907A895338C3F6881?partnerref=anacondacom)

**Joke:** 

![](https://paper-attachments.dropbox.com/s_3370DBC8B17DDD025FB99F5F8E61DB76EED1D134B78707EFC4676F383C096EF5_1641345305415_Screen_Shot_2020-06-08_at_10.42.24_PM.png)

