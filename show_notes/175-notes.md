# Python Bytes 175

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special Guest: [**Matt Harrison**](https://twitter.com/__mharrison__)

**Topic #0: Quick chat about COVID 19.**

- What does your world look like?
- Amusing to see news channels, daily shows, etc, learning what we podcasters have figured out years ago

**Brian #1:** [**Dictionary Merging and Updating in Python 3.9**](https://medium.com/better-programming/dictionary-merging-and-updating-in-python-3-9-4ac67c667ce)

- Yong Cui, Ph.D.
- Python 3.9, scheduled for Oct release, will introduce new merge `(|)` and update `(|=)` operators, a.k.a. union operators
- Available in [alpha 4 and later](https://www.python.org/downloads/release/python-390a5/)
- see also [pep 584](https://www.python.org/dev/peps/pep-0584/)

```
    # merge
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    d3 = d1 | d2
    # d3 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    # update
    d1 = {'a': 1, 'b': 2}
    d1 |= {'c': 3, 'd': 4}
    # d1 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    # last one wins if contention for both | and |=
    d1 = {'a': 1, 'b': 2}
    d1 |= {'a': 10, 'c': 3, 'd': 4}
    # d1 is now {'a': 10, 'b': 2, 'c': 3, 'd': 4}
```

**Matt #2:** [**superstring**](https://github.com/btwael/superstring.py)

- An efficient library for heavy-text manipulation in Python, that achieves a remarkable memory and CPU optimization.
- Uses Rope (data structure) and optimization techniques.
- Performance comparisons for 50,000 char text
	- memory: 1/20th
	- speed: 1/5th
- Features
	- Fast and Memory-optimized
	- Rich API
		- concatenation  (a + b)
		- len() and .length()
		- indexing
		- slicing
		- strip
		- lower
		- upper
- Similar functionalities to python built-in string
- Easy to embed and use.
- I wonder if any of these optimizations could be brought into CPython
- Beware, it’s lacking tests

**Michael #3:** [**New pip resolver to roll out this year**](https://pyfound.blogspot.com/2020/03/new-pip-resolver-to-roll-out-this-year.html)

- via PyCoders
- The developers of pip are in the process of developing a new resolver for pip (as [announced on the PSF blog](https://pyfound.blogspot.com/2019/12/moss-czi-support-pip.html) last year).
- As part of that work, there will be some major changes to how pip determines what to install, based on package requirements.
- What will change:
	- It will **reduce inconsistency**: it will *no longer install a combination of packages that is mutually inconsistent*.
	- It will be **stricter** - if you ask pip to install two packages with incompatible requirements, it will refuse (rather than installing a broken combination, like it does now).
- What you can do to help
	- First and most fundamentally, [please help us understand how you use pip by](https://bit.ly/pip-ux-studies) [**talking with our user experience researchers**](https://bit.ly/pip-ux-studies).
	- Even before we release the new resolver as a beta, you can help by **running** `**pip check**` **on your current environment**.
	- Please make time to ***test*** **the new version of pip, probably in May.**
	- **Spread the word!**
	- And if you develop or support a tool that wraps pip or uses it to deliver part of your functionality, please make time to **test your integration with our beta in May**

**Matt** **#4:** **Covid-19** 
https://www.kaggle.com/saga21/covid-global-forecast-sir-model-ml-regressions
Think global act local
Problem - No local data
Made my own plots - current status no predictions
ML works ok for basic model
Implementing SIR Model with ordinary differential equations **scipy odeint function** 

**Brian #5:** [**Why does all() return True if the iterable is empty?**](https://blog.carlmjohnson.net/post/2020/python-square-of-opposition/)

- Carl Johnson
- Q: “Why does `all()` return `True` if the iterable is empty? Shouldn’t it return `False` just like `if my_list:`would evaluate to `False` if the list is empty? What’s the thinking behind it returning `True`?”
- Lesson 1: "… basically doesn’t matter. The Python core team chose to make `all([])`return `True`, and whatever their reasons, you can program your way around by adding wrapper functions or `if` tests. ”
- Lesson 2: “all unicorns are blue”
- Lesson 3: “This is literally a 2,500 year old debate in philosophy. The ancients thought “all unicorns are blue” should be false because there are no unicorns, but modern logic says it is true because there are no unicorns that aren’t blue. Python is just siding with modern predicate logic, but your intuition is also quite common and was the orthodox position until the last few hundred years.”
- Blog post goes into teaching about predicate logic, Socrates, Aristotelean syllogisms, and such.
- And, really, no answer to why. But now, I’ll never forget that `all([]) == True`.

**Michael #6:** [**pytest-monitor**](https://github.com/CFMTech/pytest-monitor)

- written by Jean-Sébastien Dieu
- pytest plugin for analyzing resource usage during test sessions
- Analyze your resources consumption through test functions:
	- memory consumption
	- time duration
	- CPU usage
- Keep a history of your resource consumption measurements.
- Compare how your code behaves between different environments.
- Usage: Simply run *pytest* as usual: *pytest-monitor* is active by default as soon as it is installed. 
- After running your first session, a .pymon sqlite database will be accessible in the directory where pytest was run.
- You will need a valid Python 3.5+ interpreter. To get measures, we rely on:
	- *psutil* to extract CPU usage
	- *memory_profiler* to collect memory usage
	- and *pytest* (obviously!)

Extras:

Michael:

- `switchlang` is now [**on pypi**](https://pypi.org/project/switchlang/) **:** `pip install switchlang`
- `markdown-subtemplate` is now [**on pypi**](https://pypi.org/project/markdown-subtemplate/): `pip install markdown-subtemplate`

Joke:

Light timer fix:
[https://twitter.com/Sarcastic_Pharm/status/1238060786658009089](https://twitter.com/Sarcastic_Pharm/status/1238060786658009089)

