# Python Bytes 30
Sponsored by Datadog: Try Datadog and get a free shirt at [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog).

**Brian #1:** **Problems and Solutions are different at different scales**

- [You are not Google](https://blog.bradfieldcs.com/you-are-not-google-84912cf44afb)
- [Enough with microservices](https://aadrake.com/posts/2017-05-20-enough-with-the-microservices.html)

**Michael #2:** [**Introducing NoDB - a Pythonic Object Store for S3**](https://blog.zappa.io/posts/introducing-nodb-pythonic-data-store-s3)

- Released in April 2017 by Rich Jones
- An incredibly simple, Pythonic object store based on Amazon's S3 static file storage.
- NoDB isn't a database.. but it sort of looks like one!
- Kind of like a document database, supports indexing
- Can use Pickling or JSON
- Mostly useful for **prototyping**, **casual hacking**, and (maybe) even low-traffic **server-less databases** for [**Zappa**](https://github.com/Miserlou/Zappa) **apps**!
- Can see a few use cases for **NoDB**:
  - Prototyping schemas
  - Storing API event responses for later replay
  - Capturing event logs
  - Storing simple form data (email addresses, etc.)
  - Storing non-relational analytics data
  - Firing Lambda event triggers
  - Version controlling evolving Python objects
  - Storing and loading trained machine learning models
- https://github.com/Miserlou/NoDB

**Brian #3:** [**Elizabeth for mock data**](https://github.com/lk-geimfari/elizabeth)
Part 1: https://medium.com/wemake-services/generating-mock-data-using-elizabeth-part-i-ca5a55b8027c
Part 2: https://medium.com/wemake-services/generating-mock-data-with-elizabeth-part-ii-bb16a3f3106f
pytest plugin: https://github.com/lk-geimfari/pytest-elizabeth

**Michael #4:** [**What’s New In Python 3.7**](https://docs.python.org/3.7/whatsnew/3.7.html)

- Lang: More than 255 arguments can now be passed to a function, and a function can now have more than 255 parameters.
- Lang: `bytes.fromhex()` and `bytearray.fromhex()` now ignore all ASCII whitespace, not only spaces.
- Lang: Circular imports involving absolute imports with binding a submodule to a name are now supported.
- Module: `contextlib.asynccontextmanager()` has been added.
  - Similar to `contextmanager()`, but creates an asynchronous context manager.
  - This function is a decorator that can be used to define a factory function for async with statement asynchronous context managers, without needing to create a class or separate `__aenter__()` and `__aexit__()` methods.
- Module:The dis() function now is able to disassemble nested code objects (the code of comprehensions, generator expressions and nested functions, and the code used for building nested classes).
- Module: math: New `remainder()` function, implementing the IEEE 754-style remainder operation.
- Optimization: Added two new opcodes: `LOAD_METHOD` and `CALL_METHOD` to avoid instantiation of bound method objects for method calls, which **results in** **method calls being faster up to 20%**.
- Optimization: The `os.fwalk()` function has been sped up by 2 times.

**Brian #5: Hypothesis Testing**

- [Unleash the Test Army](http://wordaligned.org/articles/unleash-the-test-army)

**Michael #6:** [**Heroku switching default to v3.6.1**](https://www.reddit.com/r/Python/comments/6fvgrf/heroku_switching_default_to_v361/)

- Effective Tuesday, June 20th, 2017, new Python applications pushed to Heroku will use the python-3.6.1 runtime by default (instead of python-2.7.13).
- Existing applications will not be affected by this change.
- “Lots of new projects start out on heroku all the time, so this is really great news for python 3 adoption.”
- “Python 3 is really happening. I was actually a little worried about the future of Python for a while.”

