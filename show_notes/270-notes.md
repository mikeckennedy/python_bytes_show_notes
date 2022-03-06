# Python Bytes 270

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: Dean Langsam

**Brian #1:** [**A Better Pygame Mainloop**](https://glyph.twistedmatrix.com/2022/02/a-better-pygame-mainloop.html)

- Glyph
- Doing some game programming is a great way to work on coding for early devs (and experienced devs).
- pygame is a popular package for writing games in Python
- But… the normal example of a main loop, which listens for events and dispatches actions based on events, has some problems:
    - it’s got a `while 1:`
        - that wastes power, too much busy waiting
        - looks bad, due to “screen tearing” which is writing to a screen while your in the middle of drawing it
- This post discusses the problems, and walks through to an async main loop that creates a better gaming experience.

**Michael #2:** [**awesome sqlalchemy**](https://github.com/dahlia/awesome-sqlalchemy)

- A few notable ones
- [SQLAlchemy-Continuum](https://sqlalchemy-continuum.readthedocs.io/): Versioning and auditing extension for SQLAlchemy.
- [SQLAlchemy-Utc](https://github.com/spoqa/sqlalchemy-utc): SQLAlchemy type to store aware `datetime.datetime` values.
- [SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/): Various utility functions, new data types and helpers for SQLAlchemy
- [filedepot](https://depot.readthedocs.io/): DEPOT is a framework for easily storing and serving files in web applications.
- [SQLAlchemy-ImageAttach](https://sqlalchemy-imageattach.readthedocs.io/): SQLAlchemy-ImageAttach is a SQLAlchemy extension for attaching images to entity objects.
- [SQLAlchemy-Searchable](https://sqlalchemy-searchable.readthedocs.io/): Full-text searchable models for SQLAlchemy.
- [sqlalchemy_schemadisplay](https://github.com/fschulze/sqlalchemy_schemadisplay): This module generates images from SQLAlchemy models.
- Can we also get a shoutout to [SQLModel](https://sqlmodel.tiangolo.com/)?

**Dean #3:** [**ThreadPoolExecutor in Python: The Complete Guide**](https://superfastpython.com/threadpoolexecutor-in-python/) 

- Long, but worth it (80-120 minutes). Could be consumed in parts. It’s mostly a collection of other blogposts on superfastpython
- Many examples
- LifeCycle
- Usage patterns
    - Map and was
    - as_completed vs sequentially
    - callbacks
- IO-Bound vs CPU-bound
- [**Common Questions**](https://superfastpython.com/threadpoolexecutor-in-python/#Common_Questions_When_Using_the_ThreadPoolExecutor)
- Comparison
    - vs. ProcessPoolExecutor
    - vs. threading.Thread
    - vs. AsyncIO


**Brian #4:** [**Chaining comparison operators**](https://mathspp.com/blog/pydonts/chaining-comparison-operators)

- Rodrigo Girão Serrão
- I use chained expressions all the time, mostly with ranges:
    - `min <= x <= max`, which is like `(min <=x) and (x <= max)`
- There are lots of chained expressions available, and some not so obvious.
- `a == b == c`
    - all are equal, no prob
- what abut `a != b != c` ?
    - This actually can return `True` if `a == c`
- Lots of other issues with chaining discussed in the article, like non-constant expressions and side effects

**Michael #5:** [**Create Beautiful Tracebacks with Python’s Exception Hooks**](https://martinheinz.dev/blog/66)

```
    def exception_hook(exc_type, exc_value, tb):
        ...
    
    sys.excepthook = exception_hook
```

- Libraries
- [**rich.traceback**](https://rich.readthedocs.io/en/latest/traceback.html)
- [**better-exceptions**](https://github.com/Qix-/better-exceptions)
- [**Pretty Errors**](https://github.com/onelivesleft/PrettyErrors/)
- [**IPython.core.ultratb**](https://ipython.readthedocs.io/en/stable/api/generated/IPython.core.ultratb.html)
- [**stackprinter**](https://github.com/cknd/stackprinter)

**Dean#6:** [Ways I Use Testing as a Data Scientist](https://www.peterbaumgartner.com/blog/testing-for-data-science/)

- The importance of knowing what to test for
- using `assert` in code on ad-hoc things. Do it while coding.
- Us numpy `np.isclose` to test “almost equal” on entire arrays. also `[assert_frame_equal](https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html)`
- Use hypothesis for bombarding the function with smart tests.
- [Pandera](https://pandera.readthedocs.io/en/stable/) and [Great Expectations](https://docs.greatexpectations.io/docs/)
- tests are documentation!
- Work with [Arrange-Act-Assert](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)
- **Even if we’re not sure what to assert, writing a test that executes the code is still valuable.**

**Extras** 

Dean:

- [Deprecate urllib out of stdlib?](https://twitter.com/VictorStinner/status/1490328160210231302?t=OHeX6BbBgm-L5waX2oGRYA&s=19)
- [IPython 8 is out](https://blog.jupyter.org/release-of-ipython-8-0-6e034ff122ef)
    - **It’s less code!**
        - 37,500 LOC across 348 files → 36,100 across 294 files
            “I’m sorry I wrote you such a long letter. I didn’t have time to write you a short one.” – Blaise Pascal
    - This was all done thanks to a developer hired through [**Small Development Grants**](https://numfocus.org/programs/small-development-grants) [](https://numfocus.org/programs/small-development-grants)
    - coloring exceptions
    

Michael:

- Python Shorts New videos
    - [**Beyond the List Comprehension**](https://www.youtube.com/watch?v=PTMt1VJPdFc)
    - [**Combining dictionaries, the Python 3.10 way**](https://www.youtube.com/watch?v=TwNGHa0-6ik)
- `/` on pypi.org

**Joke:** [**Spelling**](https://twitter.com/PR0GRAMMERHUM0R/status/1486383458775715847)
