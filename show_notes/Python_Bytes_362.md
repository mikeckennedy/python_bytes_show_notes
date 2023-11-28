# Python Bytes 362

Sponsored by [**Scout APM**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Habits of great software engineers**](https://vadimkravcenko.com/shorts/habits-of-great-software-engineers)

- As we wind up the year, many people are thinking about goals for the new year.
- Here’s a decent list to think about
    - Focusing beyond the code 
    - Efficiency / Antifragility
    - Joy of tinkering 
    - Knowing the why 
    - Thinking in systems 
    - Tech detox 
    - The art of approximation
    - Transferring Knowledge to Other Problems
    - Making Hard Things Easy
    - Playing the Long Game
    - Developing a Code Nose
    - Strong Opinions loosely held

**Michael #2:** [**Flask 3.0**](https://flask.palletsprojects.com/en/3.0.x/changes/)

- Deprecate the `__version__` attribute. Use feature detection, or `importlib.metadata.version("flask")`, instead. #5230
    - How do you [even do that](https://github.com/pallets/flask/pull/5242/files)?
- This is news to me:

```
[build-system]
    requires = ["setuptools", "wheel"]
    build-backend = "setuptools.build_meta"
    
    [metadata]
    name = "your-package-name"
    version = "0.1.0"
```

- Remove previously deprecated code. [#5223](https://github.com/pallets/flask/pull/5223)



**Brian #3:** [**Build Conway's Game of Life With Python**](https://realpython.com/conway-game-of-life-python)

- Leodanis Pozo Ramos
- CLI curses version
- Nice walk through of breaking the problem into parts.

**Michael #4:** ****[**polars business**](https://github.com/MarcoGorelli/polars-business)

- It's a plugin for Polars, which allows you to do business day arithmetic.
- The big advantage of using this directly (as opposed to converting to pandas/numpy, using their business day tools, and then converting back) is that polars-business fits right in with the Polars lazy API. This means you'll still be able to get the gains from the Polars query optimiser without having to step into eager execution.
- All you need to use is it is `pip install polars-business`
- Written in Rust, but end-users doesn't need Rust to run it, Python is all you need.

**Extras** 

Brian:

- BLACKFRIDAY code still works for 50% off [The Complete pytest Course,](https://courses.pythontest.com/p/complete-pytest-course) Full Course + Community Access, through Nov 30
- Also Debugging chapter is up, and it includes a small TDD example.

Michael:

- [Dear Python Community](https://twitter.com/kennethreitz42/status/1726816318303752511) by Kenneth Reitz
- [Python 3.13a2 out and Major new features of the 3.13 series, compared to 3.12](https://discuss.python.org/t/python-3-13-0-alpha-2/39379)
- Thank you Black Friday supporters. 

**Joke:** 

- [ai vs dev](https://www.reddit.com/r/programminghumor/comments/171i41r/select/)

