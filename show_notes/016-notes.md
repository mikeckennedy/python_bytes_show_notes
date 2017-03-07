This is Python Bytes, Python headlines and news delivered directly to your earbuds: episode 16, recorded on March 6th, 2017. [more]

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

**#1 Brian**: [**Postmodern Error Handling in Python 3.6**](http://journalpanic.com/post/postmodern-error-handling/)
- On "Journal Panic"
- An amusing look at error prevention
  - Enum class usage
  - NamedTuple class usage
  - type hints
  - mypy
- Bonus, another recent pretty darn good mypy walkthrough: [Python Type Annotations](https://www.caktusgroup.com/blog/2017/02/22/python-type-annotations/) 

**#2 Michael:** [**Mozilla Awards $585,000 to Nine Open Source Projects in Q2 2016**](https://blog.mozilla.org/blog/2016/08/04/mozilla-awards-585000-to-nine-open-source-projects-in-q2-2016/)

- One of the new tracks is “[Mission Partners](https://wiki.mozilla.org/MOSS/Mission_Partners)”, which supports any open source project which meaningfully advances the Mozilla mission. We had a large number of applications in the initial round, of which we have [already funded eight](https://blog.mozilla.org/blog/2016/06/22/mozilla-awards-385000-to-open-source-projects-as-part-of-moss-mission-partners-program/) (for a total of $385,000) and are still considering several more. Applications for “Mission Partners” [remain open](https://docs.google.com/forms/d/1rwYQTT-9-eldS-kElY646bMwMzJpxfL8lDskX86xgCQ/viewform) on an ongoing basis.
- The second is our “[Secure Open Source](https://wiki.mozilla.org/MOSS/Secure_Open_Source)” track, which works on improving the security of open source software by providing manual source code audits for important and widely-used pieces of free software.
- Our initial track, “[Foundational Technology](https://wiki.mozilla.org/MOSS/Foundational_Technology)”, which supports projects that Mozilla already uses, integrates or deploys in our infrastructure, was launched late last year and remained open during this quarter.
  - We made one additional award – to PyPy, the Python JIT compiler, for $200,000. 
  - Applications for a “Foundational Technology” award [remain open](https://docs.google.com/a/mozilla.com/forms/d/1Pa5IsuhT6vMUfg0HUXxr7SzrSwq5fpiZfZIJVPxN1Mc/viewform).

**#3 Brian:** [**Intel Distribution for Python 2017 Update 2 accelerates five key areas for impressive performance gains**](https://software.intel.com/en-us/articles/intelr-distribution-for-python-2017-update-2)

- “Benchmarks for all these accelerations will be published soon. “
- "..widespread optimizations for NumPy and SciPy FFT." "..performance may improve up to 60x over Update 1 and is now close to native C/Intel MKL."
- "Arithmetic and transcendental expressions" from NumPy can now use`umath` primitives which enables support for all available cores.
- Memory management optimizations
- Faster Machine Learning with Scikit-learn
- Looks like there is a free standalone version and a paid version.
- Supports Python 2.7 and 3.5. (When’s 3.6 coming, folks?)
- Supports Windows, Linux, OSX

**#4 Michael:** [**Async HTTP benchmarks on PyPy3**](https://morepypy.blogspot.com/2017/03/async-http-benchmarks-on-pypy3.html)

 - Thanks for the heads up [Guy Fighel, @guyfig](https://twitter.com/guyfig)
-  Since [Mozilla announced funding](https://blog.mozilla.org/blog/2016/08/04/mozilla-awards-585000-to-nine-open-source-projects-in-q2-2016/), we've been working quite hard on delivering you a working Python 3.5.
- We are almost ready to release an alpha version of PyPy 3.5
- Pyston faded and PyPy is surging. 
- To show that the heart of Python 3 (asyncio) is already working we have prepared some benchmarks.
- HTTP workload on several asynchronous IO libraries, namely the relatively new *asyncio and* *curio libraries* and the battle-tested *tornado*, *gevent and Twisted libraries*
- The purpose of the presented benchmarks is showing that the upcoming PyPy release is already working with unmodified code that runs on CPython 3.5
- Summary: 5-10x improvement across the board

**#5 Brian**: [**A tale of two exceptions, part 1**](https://nedbatchelder.com/blog/201701/a_tale_of_two_exceptions.html), [**and part2**](https://nedbatchelder.com/blog/201702/a_tale_of_two_exceptions_continued.html)

- Ned Batchelder tried to get the `coverage.py` test suite to run on Jython.
- Jython doesn't have whatever coverage needs for the reporting part of coverage, so Ned went through some attempts to get the exceptions working ok and try to skip tests that required reporting.
- Headaches start and raise lots of design questions with a normal set of pragmatic decisions that have to be made. And following Ned's thought process is a cool look at problem solving.
- The first post ends with a solution that includes production code raising test exceptions.
- The second post replaces that with a solution that uses a metaclass to apply a decorator to each test function at object instantiation. The decorator looks for a custom exception and raises SkipTest. 

**#6 Michael:** [**Asynchronous HTTP Requests in Python**](http://terriblecode.com/post/using_aiohttp/)

- If you’re familiar with the popular Python library `requests` you can consider `aiohttp` as the asynchronous version of `requests`.
- Usage is very similar to `requests` but the potential performance benefits are, in some cases, absolutely insane.
- Requests: It’s a fairly straightforward program and takes around 12 minutes of total time.
- `aiohttp`'s `ClientSession.get()` and `aiofiles`: execution time is about *22 seconds*, which in my opinion is a ridiculous performance boost (that’s 33x faster).



