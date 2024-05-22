# Python Bytes 165
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**iterators, generators, coroutines**](https://www.integralist.co.uk/posts/python-generators/)

- Cool quick read article by Mark McDonnell.
- Starts with an attempt at a gentle introduction to the iterator protocol (why does everyone think that users need to start with this info?) Muscle through this part or just skim it. Should be an appendix.
- Generators (start here): functions that use `yield`
- Unbound generators: they don’t stop
- Generator Expressions: Like `for v in ("foo" for i in range(5)): …`
	- Use parens instead of brackets, otherwise they are like list comprehensions.
	- Specifically: `(expression for item in collection if condition)`
- Generators using generators / nested generators : `yield from`
- Given `bar()` and `baz()` are generators, this works:
```
    def foo():
        yield from bar()
        yield from baz()
```
- Coroutines are an extension of generators
	- “Generators use the yield keyword to return a value at some point in time within a function, but with coroutines the yield directive can also be used on the right-hand side of an = operator to signify it will accept a value at that point in time.”
- Then….. coroutine example, some asyncio stuff, … honestly I got lost.
- Bottom line: 
	- I’m still looking for a great tutorial on coroutines that
		- doesn’t explain the iterator protocol (boring!)
		- shows an example NOT using asyncio and NOT a REPL example
	- I want to know how I can make use of coroutines in an actual program (toy ok) where the use of coroutines actually helps the structure and makes it more maintainable, etc.

**Michael #2:** [**requests-toolbelt**](https://github.com/requests/toolbelt)

- A toolbelt of useful classes and functions to be used with requests
- **multipart/form-data encoder** - The main attraction is a streaming multipart form-data object, `MultipartEncoder`.
- **User-Agent constructor** - You can easily construct a requests-style User-Agent string
- **SSLAdapter** - Allows the user to choose one of the SSL protocols made available in Python's ssl module for outgoing HTTPS connections
- **ForgetfulCookieJar** - prevents a particular requests session from storing cookies

**Brian #3:** **Pandas Validation**

- We covered Bulwark in [episode 162](https://pythonbytes.fm/162)
- There are other approaches and projects looking at the same problem.
- [pandas-validation](https://github.com/jmenglund/pandas-validation)
	- Suggested by Lance
	- “… pandas-validation lets you create a template of what your pandas dataframe should look like and it'll validate the entire dataframe against that template. So if you have a dataframe with first column being strings second column being dates and the third being address, you can use a mixture of built in validate types to ensure your data conforms to that. It will even let you set up some regex and make sure that the data in a column conforms to that regex.” - Lance
	- supports dates, timestamps, numeric values, strings
- [pandera](https://github.com/pandera-dev/pandera)
	- “pandera provides a flexible and expressive API for performing data validation on tidy (long-form) and wide data to make data processing pipelines more readable and robust."
	- “pandas data structures contain information that pandera explicitly validates at runtime. This is useful in production-critical or reproducible research settings.
	- “pandera enables users to:
		- Check the types and properties of columns in a DataFrame or values in a Series.
		- Perform more complex statistical validation.
		- Seamlessly integrate with existing data analysis/processing pipelines via function decorators.”
- A few different approaches. I can’t really tell from the outside if there is a clear winner or solution that’s working better for most cases. I’d like to hear from listeners which they use, if any. Or if we missed the obvious validation method most people are using.

**Michael #4:** [**qtpy**](https://github.com/spyder-ide/qtpy)

- I have been inspired to check out Qt again, but the libraries and versions a confusing.
- Provides an uniform layer to support PyQt5, PySide2, PyQt4 and PySide with a single codebase
- Basically, you can write your code as if you were using PySide2 but import Qt modules from `qtpy` instead of `PySide2` (or `PyQt5`).

**Brian #5:** [**pylightxl**](https://github.com/PydPiper/pylightxl)

- Viktor Kis submission
- “A light weight, zero dependency, minimal functionality excel read/writer python library”
- Well. Reader right now. Writing coming soon. :)
- Some cool examples in the [docs](https://pylightxl.readthedocs.io/en/latest/index.html) to get you started grabbing data from spreadsheets right away.
- Features:
	- Zero non-standard library dependencies 
	- Single source code that supports both Python37 and Python27. The light weight library is only 3 source files that can be easily copied directly into a project for those that have installation/download restrictions. In addition the library’s size and zero dependency makes pyinstaller compilation small and easy!
	- 100% test-driven development for highest reliability/maintainability with 100% coverage on all supported versions
	- API aimed to be user friendly, intuitive and to the point with no bells and whistles. Structure: database > worksheet > indexing
		- example: `db.ws('Sheet1').index(row=1,col=2)` or `db.ws('Sheet1').address(address='B1')`
	- Read excel files (.xlsx, .xlsm), all sheets or selective few for speed/memory management
	- Index cells data by row/col number or address
	- Calling an entire row/col of data returns an easy to use list output:
		- db.ws('Sheet1').row(1) or db.ws('Sheet1').rows
	- Worksheet data size is consistent for each row/col. Any data that is empty will return a ‘’

**Michael #6:** [**python-ranges**](https://github.com/Superbird11/ranges)

- via Aiden Price
- Continuous Range, RangeSet, and RangeDict data structures for Python
- Best understood as an example:

```
    tax_info = RangeDict({
        Range(0, 9701):        (0,        0.10, 0),
        Range(9701,   39476):  (970,      0.12, 9700), 
        ... })
    
    income = int(input("What is your income? $"))
    base, marginal_rate, bracket_floor = tax_info[income]
```

- 
- `Range` and `RangeSet` objects are mutually compatible for things like `union()`, `intersection()`, `difference()`, and `symmetric_difference()`

Extras:

- Brian:
    - [pytest-check](https://github.com/okken/pytest-check) works with [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)
			- with other plugins, it may not.
			- known incompatibility with flaky and retry
- Michael:
    - Pandas goes 1.0 (via Jeremy Schendel). Just put out a release candidate for 1.0, and will be using SemVer going forward.
    - [PyCharm security](https://twitter.com/anthonypjshaw/status/1215732790051782656) from Anthony Shaw.
    - Video for Python for Decision Makers **webcast** [is out](https://www.crowdcast.io/e/python-for-decision).

Joke: 

- Optimist: The glass is half full.
- Pessimist: The glass is half empty.
- **Engineer**: The glass is twice as large as it needs to be.
