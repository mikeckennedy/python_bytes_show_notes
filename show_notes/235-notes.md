# Python Bytes 235


Sponsored by Sentry:

- Sign up at [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)
- And please, when signing up, click ***Got a promo code? Redeem*** and enter **PYTHONBYTES**

Special guest: Vincent D. Warmerdam [koaning.io](https://koaning.io/), Research Advocate @ Rasa and maintainer of a [whole](https://scikit-lego.netlify.app/) [bunch](https://github.com/koaning/human-learn) of [projects](https://calmcode.io/). 


**Brian #1:** **Flask 2.0 articles and reactions**

- [Change list](https://flask.palletsprojects.com/en/2.0.x/changes/)
- [Async in Flask 2.0](https://testdriven.io/blog/flask-async/)
	- Patrick Kennedy on testdriven.io blog
	- Great description
	- discussion of how the async works in Flask 2.0
	- examples
	- how to test async routes
- [An opinionated review of the most interesting aspects of Flask 2.0](https://www.youtube.com/watch?v=0KU67snMjtQ)
	- Miguel Grinberg video
	- covers
		- route decorators for common methods, 
	    - ex `@app.post(``"``/``"``)` instead of `@app.route("/", methods=["POST"])`
	- web socket support
	- async support
	- Also includes some extensions Miguel has written to make things easier
	- Great discussion, worth the 25 min play time.
- See also: [Talk Python Episode 316](https://talkpython.fm/episodes/show/316/flask-2.0)

**Michael #2:** [**Python 3.11 will be 2x faster?**](https://twitter.com/driscollis/status/1392947869657731072?s=12)

- via [Mike Driscoll](https://twitter.com/driscollis)
- From the Python Language summit
- Guido asks "Can we make CPython faster?”
- We covered the [Shannon Plan for speedups](https://github.com/markshannon/faster-cpython).
- Small team funded by Microsoft: Eric Snow, Mark Shannon, myself (might grow)
- Constrains: Mostly don’t break things.
- How to reach 2x speedup in 3.11
	- Adaptive, specializing bytecode interpreter
	- “Zero overhead” exception handling
	- Faster integer internals
	- Put __dict__ at a fixed offset (-1?)
- There’s machine code generation in our future
- Who will benefit
	- Users running CPU-intensive pure Python code •Users of websites built in Python
	- Users of tools that happen to use Python

**Vincent #3:**

- DEON, a project with [meaningful checklists](https://deon.drivendata.org/#default-checklist) for data science projects! 
	- It’s a command line app that can generate checklists.
	- You customize checklists
	- There’s a [set of examples](https://deon.drivendata.org/examples/) (one for for each check) that explain why the checks it is matter. 
	- Make a little course on [calmcode](https://calmcode.io/deon/introduction.html) to cover it.

**Brian #4:** [**3 Tools to Track and Visualize the Execution of your Python Code**](https://towardsdatascience.com/3-tools-to-track-and-visualize-the-execution-of-your-python-code-666a153e435e)

- Khuyen Tran
- [Loguru](https://github.com/Delgan/loguru) — print better exceptions
	- we covered in [episode 111](https://pythonbytes.fm/episodes/show/111/loguru-python-logging-made-simple),  Jan 2019, but still super cool
- [snoop](https://github.com/alexmojaki/snoop) — print the lines of code being executed in a function
	- covered in [episode 141](https://pythonbytes.fm/episodes/show/141/debugging-with-f-strings-coming-in-python-3.8), July 2019, also still super cool
- [heartrate](https://github.com/alexmojaki/heartrate) — visualize the execution of a Python program in real-time
	- this is new to us, woohoo
- Nice to have one persons take on a group of useful tools
	- Plus great images of them in action.

**Michael #5:** [**DuckDB + Pandas**](https://duckdb.org/2021/05/14/sql-on-pandas.html)

- via [**__AlexMonahan__**](https://twitter.com/__AlexMonahan__/status/1393206122291503105)
- What’s [**DuckDB**](https://duckdb.org/)? An in-process SQL OLAP database management system
- SQL on Pandas: After your data has been converted into a Pandas DataFrame often additional data wrangling and analysis still need to be performed. Using DuckDB, it is possible to run SQL efficiently right on top of Pandas DataFrames.
- Example

```
    import pandas as pd
    import duckdb
    
    mydf = pd.DataFrame({'a' : [1, 2, 3]})
    print(duckdb.query("SELECT SUM(a) FROM mydf").to_df())
```

- When you run a query in SQL, DuckDB will look for Python variables whose name matches the table names in your query and automatically start reading your Pandas DataFrames.
- For many queries, you can use DuckDB to process data faster than Pandas, and with a much lower total memory usage, *without ever leaving the Pandas DataFrame binary format* (“Pandas-in, Pandas-out”).
- The automatic query optimizer in DuckDB does lots of the hard, expert work you’d need in Pandas.

**Vincent #6:**

- I work for a company called [Rasa](https://rasa.com/). We make a python library to make virtual assistants and there’s a few community projects. There’s a bunch of cool showcases, but one stood out when I was checking our community showcase last week. There’s a project that warns folks about forest fire updates over text. The project is open-sourced on GitHub and can be found [here](https://github.com/amittallapragada/CalFireAlertChatBot). There’s also a GIF demo [here](https://rasa.com/showcase/wildfire/).
	- Amit Tallapragada and Arvind Sankar observed that in the early days of the fires, news outlets and local governments provided a confusing mix of updates about fire containment and evacuation zones, leading some residents to evacuate unnecessarily. They teamed up to build a chatbot that would return accurate information about conditions in individual cities, including nearby fires, air quality, and weather data.
	- What’s cool here isn’t just that Vincent is biased (again, he works for Rasa), it’s also a nice example of grass-roots impact. You can make a lot of impact if there’s open APIs around.
	- They host a scraper that scrapes fire/weather info every 10 seconds. It also fetches evacuation information.
	- You can text a number and it will send you up-to-date info based on your city. It will also notify you if there’s an evacuation order/plan. 
	- They even do some fuzzy matching to make sure that your city is matched even when you make a typo. 
    

**Extras**

**Michael**

- [PyCon US 2024 and 2025 Announced](https://pycon.blogspot.com/2021/05/pycon-us-2024-and-2025-announcement.html)

**Vincent**: Human-Learn: a suite of tools to have humans define models before resorting to machines.
- It’s scikit-learn compatible. 
- One of the main features is that you’re able to [draw a model](https://koaning.github.io/human-learn/guide/drawing-classifier/drawing.html#lets-draw)! 
- There’s a small guide that shows how to outperform a deep learning implementation by doing exploratory data analysis. It turns out, you can [outperform Keras sometimes](https://koaning.github.io/human-learn/examples/model-mining.html). 
- There’s a suite of tools to turn python functions into [scikit-learn compatible models](https://koaning.github.io/human-learn/guide/function-classifier/function-classifier.html#functionclassifier). Keyword arguments become grid-search-able. 
- Tutorial on [calmcode.io](https://calmcode.io/human-learn/introduction.html) to anybody interested.
- Can also be used for [Bulk Labelling](https://github.com/RasaHQ/rasalit#bulk-labelling).

**Joke** 

![](https://trello-attachments.s3.amazonaws.com/606b944eaaa94067a63fa7b6/1079x1179/baa563951b9965eef7f552a2d27329c5/Programming-Life-Strongest-Programmer.jpg)

