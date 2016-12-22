# Python Bytes Episode 6

This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 6, recorded on Monday, December 12th. In this episode we discuss why Python 3.6 is going to be awesome, kite: your friendly co-developing AI, and more! [more] 

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

This is the last episode of 2016. Thank you everyone for a great launch. We’ll be back early January. 😉 Be sure to check out Talk Python and Test and Code if you want more Pythonic listening over the break.

## News items

[**#1 Make your Python code more readable with custom exception classes**](https://dbader.org/blog/python-custom-exceptions)

- This is a 5 min video + text. Good introduction into why you should define your own exceptions instead of using the built in ones, and how to do it.  
	  - It makes errors from your code more readable.
	  - Better communication between your code and the person using your code.
	  - It allows you to give more context of the error to the caller of the function.
	  - Remember to derive from Exception or from another builtin exception.
- Do people create enough fine-grained exception types? I would say probably not.
- This advice is good because it encourages [EAFP](https://docs.python.org/2/glossary.html#term-eafp) (easier to ask for forgiveness than permission) style of programming which is generally Pythonic.
- Allows for multiple except statements for different errors in one try block
- Dan also featured our show in [The ultimate list of Python Podcasts](https://dbader.org/blog/ultimate-list-of-python-podcasts) (thanks Dan!)
- If you have a package that defines it’s own exceptions, please read another article.
	  - **The definitive guide to Python exceptions**
	    - Julien Danjou
	    - https://julien.danjou.info/blog/2016/python-exceptions-guide
	    - Covers having a common base exception for your package, organization within a package, and some examples of packages that organize their exceptions well, including requests
  

[**#2 Kite**](https://kite.com/)

- Kite augments your coding environment with all the internet’s programming knowledge.
- Is an AI pair programmer, or mentor really.
- Contextual info for
	  - language
	  - packages
	  - e.g. “import r” → shows list of popular packages
	  - then detailed docs, examples, etc.
	  - autocompletions… by global popularity
	  - BYOE
	  - even works on your code
	  - be sure to watch the video
- [kite.com](http://kite.com) is implemented mostly in Go [according to the founder](https://twitter.com/asmith/status/806705380755578880) Adam Smith.
- Thanks Gilberto Diaz for sending this one to us.

[**#3 Tidy Data in Python**](http://www.jeannicholashould.com/tidy-data-in-python.html) (by Jean-Nicholas Hould)

- This article caught my attention because of the notion that the data as you receive it might not be in a form that is ideal to use it. This I am used to. But the article give some attributes of what problems to look for in data sets, and how to transform the data into a more usable structure using pandas.
- Great example of someone taking a good idea from someone else, summarizing it, and showing how to use it in Python.
- Based on a paper named [Tidy Data](http://vita.had.co.nz/papers/tidy-data.pdf) by Hadley Wickham
	  - In this post, I will summarize some tidying examples Wickham uses in his paper 
	  - Will demonstrate how to do so using the Python pandas library
- Tidy data has the following attributes:
	  - Each variable forms a column and contains values
	  - Each observation forms a row
	  - Each type of observational unit forms a table
- A few definitions:
	  - Variable: A measurement or an attribute. Height, weight, sex, etc.
	  - Value: The actual measurement or attribute. 152 cm, 80 kg, female, etc.
	  - Observation: All values measure on the same unit. Each person.


[**#4 What's new in Python 3.6**](https://youtu.be/hk85RUtQsBI)

- By Brett Cannon 
	  - Works at Microsoft Azure Data Science team
	  - Python core developer
- 16 PEPs in Py3.6 - more than any other release than Py 3.0
- PEP 498 Formatted string literals
	  - You learn about internals
	  - That this is actually faster than str.format() because optimizations that can be done on the string itself (f””)
	  - PEP 524: On Py 3.5 would fall back to unsecure. On Py 3.6 os.urandom() now blocks os.urandom() for cryptographically strong random numbers or os.getrandom() raises error if not enough randomness. Usually not a problem, but with things like containers and IoT, it has become one! Fix: use new secrets module.
- There are also other interesting things that aren’t PEPs  
- Python 3.6 is generally significantly faster (than Py3.5 and legacy Python)
- Python 3.6.0 release candidate is now available, final expected end of the week
- Something that hasn’t been as highly publicized is the deprecation of pyvenv.
	  - https://docs.python.org/3.6/library/venv.html
	  - “The `pyvenv` script has been deprecated as of Python 3.6 in favor of using `python3 -m venv` to help prevent any potential confusion as to which Python interpreter a virtual environment will be based on.”
	  - This is important for me and you and anyone who teaches people to use Python. We often recommend virtual environments, and it’s good to recommend -m venv to make sure people know which Python interpreter they are tying to their virtual environment.

[**#5: Who Tests What**](http://nedbatchelder.com//blog/201612/who_tests_what.html)

- I had [Ned Batchelder on Test&Code to discuss coverage](http://pythontesting.net/podcast/coverage-ned-batchelder/). Episode 12.
- Ned is planning a new feature for [coverage.py](https://pypi.python.org/pypi/coverage), which would tell you not just which code has run, but which test (or something else) caused that code to run.
- Discusses the stages of coverage, measurement/storing data/combining/reporting. Discusses the issue of how to decide who is calling the code in question. His current model is based on coverage having a plugin hook for someone to tell coverage a string that defines the “what” that is causing the code to be run. He also discusses some decisions about storage concerns and what coverage does now.
- He has questions remaining that he wants help with:
	  - Today coverage.py keeps everything in memory until the end of the process, then writes it all to disk. **Q:** Will we need something more sophisticated? Can we punt on that problem until later?
	  - **Q:** Is it important to try to conserve memory?
	  - Today, the .coverage data files are basically JSON. This much data might need a different format. **Q:** Is it time for a SQLite data file?
	  - **Q:** How would you use the data?
	  - And a couple more questions regarding reporting.
- I like the direction this is going and I encourage everyone who has some nonstandard usage of coverage to take a look at this and give Ned some feedback.


[**#6 Threaded Asynchronous Magic and How to Wield It**](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32#.8qk30tq31)
(by [Cristian Medina](https://twitter.com/tryexceptpass))

- This is your async programming in Python 3.5+ via async / await article
- Covers: 
	  - Tasks
	  - Scheduling tasks
	  - Scatter / gather example
	  - Moving the asyncio loop to a background thread
- Examples:
	  - Real World Example #1 — Sending Notifications (email)
	  - Real World Example #2 — Parallel Web Requests
	    - via [aiohttp](https://aiohttp.readthedocs.io/en/stable/): HTTP client/server for asyncio (PEP 3156)

**Update: From episode 3: pynini**
[https://en.m.wikipedia.org/wiki/Pāṇini](https://en.m.wikipedia.org/wiki/P%C4%81%E1%B9%87ini)
