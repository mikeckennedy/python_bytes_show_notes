# Python Bytes 240

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pytestbook.com)!

Special guest: [**Chris Moffit**](https://twitter.com/chris1610)

**Brain #1:** [**Subclassing in Python Redux**](https://hynek.me/articles/python-subclassing-redux/)

- Hynek Schlawack
- Prefer composition over inheritance,
- But if you must subclass, there are 3 types
	- subclassing for code sharing
    - bad. don’t do it.
    - read the article and included linked articles if you aren’t convinced
	- Interfaces / Abstract Data Types
    - Can be useful, but Python has tools that make this work without subclassing
	- Specialization
    - Exception hierarchies
    - There’s also an interesting discussion of structuring data classes with common elements
    - This is the only type of subclassing that Hynek deems worthy
- This is a well written, useful, and long-ish article that I cannot summarize and do it justice. 
- My summary: If you even consider sublcassing other than for exceptions, read this article first.

**Michael #2: Extra, Extra, Extra*7, Hear all about it!**

- New course! [**Python-powered chat apps with Twilio and SendGrid**](https://training.talkpython.fm/courses/python-powered-chat-apps-with-twilio-sendgrid-and-flask)
- [**Pyodide is now an independent project**](https://hacks.mozilla.org/2021/04/pyodide-spin-out-and-0-17-release/)
- [**Wow textual**](https://twitter.com/Spirix3/status/1408213749505441797) from Nick Mouh
- [**#NoFLOC for real**](https://arstechnica.com/gadgets/2021/06/google-delays-floc-rollout-until-2023/)!
- Need to protect your Python source? [**SourceDefender**](https://pypi.org/project/sourcedefender/) ****(commercial product, but neat)
- I was a guest on **A Day in a Life of a WFH Pythonista**. Full episode [**starts here**](https://youtu.be/oNydUs4KnAo?t=536), and [**the studio/office tour here**](https://youtu.be/oNydUs4KnAo?t=1882).
- [**Python 3.9.6 is out**](https://www.python.org/downloads/release/python-396/)
- [**Python Web Conf 2021 videos**](https://sixfeetup.com/company/news/pwc2021-videos-released) are out, including [**mine on memory**](https://www.youtube.com/watch?v=A-3_Iw6KNCw&list=PLt4L3V8wVnF4iB8pGfkR7eozIJPwCM7vv&index=20).
- `pip install pythonbytes` via [**pythonbytes package**](https://github.com/stoltzmaniac/pythonbytes).

**Chris #3:** [**klib**](https://github.com/akanz1/klib)

- Perform automated cleaning and analyzing of data in a pandas DataFrame
- Missing value plot and correlation data plots are similar to other tools but the visualizations are nicely done and useful. 
- The data cleaning functions are really nice. In some testing, the automated data type conversion can save a meaningful amount of data.
- For large data sets, you can drop columns with lots of null values or highly correlated values.
- The clean_column_names function also performs several cleanups on column names such as removing spaces, standardizing CamelCase, etc. 
- You have control to use as much or as little of the automated process as possible.

**Brian #4:** [**Don’t forget about functools**](https://docs.python.org/3/library/functools.html)

- “functools — Higher-order functions and operations on callable objects” 
	- in English: cool decorators and other functions that act on functions
- A [recent article by Martin Heinz](https://martinheinz.dev/blog/52) reminded me to review [functools](https://docs.python.org/3/library/functools.html)
- We’ve talked about `singledispatch` recently, and I’m sure we’ve talked about `lru_cache` before. These are in `functools`.
- `functools` is an interesting library in that you kind of use it more and more as you increase your Python experience. As a new Python dev, I would have been rather lost looking at this, but as you work through different projects, come back to this and have a look, it’ll have stuff you probably could have used, and will use in the future.
- What’s in there? Here’s a few:
	- `@singledispatch` & `@singledispatchmethod` - function/method overloading 
	- `@wraps` - A must for creating your own decorators that makes the decorated function act just like the original function (attributes, docstring, and all, with just the added behavior you are adding. 
	- `@lru_cache` - memoization made easy 
    - LRU = least recently used. It’s what it throws away when it’s full
	- `@cache` - like `@lru_cache` but with no max size. New in 3.9
	- `@cached_property` - only run the read code once. New in 3.8
    - `del(obj.property)` to clear it. Yes this is weird, but also cool.
	- `@total_ordering` - Define `__eq__()` and one other ordering function and get the other ordering functions for “free”.
	    - not free. cost is slower execution and confusing stack traces if things go wrong. but still, when prototyping something, or when comparisons are very rare, this is cool
	- `partial` / `partialmethod` - create a new function with some of the arguments of the old function already filled in. 
    - super cool for callbacks or defining convenience functions


**Michael #5:** [**GitHub Copilot**](https://copilot.github.com/)

- Get suggestions for whole lines or entire functions right inside your editor.
- Available today as a Visual Studio Code extension.
- The technical preview does especially well for Python, JavaScript, TypeScript, Ruby, and Go, but it understands dozens of languages and can help you find your way around almost anything.
- You can cycle through alternative suggestions
- Powered by Codex, the new AI system created by OpenAI
- Based on gpt3.

**Chris #6:** [**Kats**](https://facebookresearch.github.io/Kats/)

- New tool from facebook for Time Series analysis
- Can use Facebook’s Prophet as well as other algorithms such as Sarima and Holt-Winters for prediction. Here’s my [old post](https://pbpython.com/prophet-accuracy.html) on prophet.
- Some controversy about how well prophet performs in real life. Very detailed article [here](https://www.microprediction.com/blog/prophet).
- Provides utilities for analyzing time series including outlier and seasonality detection
- Offers advanced ensemble methods and access to deep learning algorithms

**Extras**

**Chris**

-  [Unyt](https://unyt.readthedocs.io/en/stable/) - library for working with  units of measure. [Pint](https://pint.readthedocs.io/en/stable/) is another similar one with a different API.

**Jokes** 

[**Italian Aysnc**](https://twitter.com/Dean_La/status/1286411422264700928) (from Dean Langsam)

**Q:** Why aren't cryptocurrency engineers allowed to vote?
**A:** Because they're miners!
