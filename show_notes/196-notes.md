# Python Bytes 196
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**Surviving Django (if you care about databases)**](https://www.varrazzo.com/blog/2020/07/25/surviving-django/)

- Daniele Varazzo
- Hard to summarize, but this is an interesting perspective on getting to know your database better and using database migrations and database schemas, etc. instead of relying on Django’s seemingly agnostic view of databases.
- Following the article is a nice civilized discussion in the comments between the author, Paolo Melchiorre, Andrew Godwin, and others.
- Interesting comment by Andrew: “I agree that at some point in a project/company's life, if it's big enough, SQL migrations are the way to go. … Migrations in the out-of-the-box state are mostly there to supplement rapid prototyping, and then like a lot of Django, can be removed/ignored progressively if and when you outgrow the single set of design constraints we had to choose for them.”

**Michael #2: Python Numbers and the Flyweight design pattern**

- Working on allocation and other memory internals from my upcoming Python Memory Management and Tips course
- Flyweight design pattern [**via Wikipedia**](https://en.wikipedia.org/wiki/Flyweight_pattern) 
- Python numbers are expensive ( `>= 28 bytes` each)
- Python does not allocate more than one int in the range `[-5, 256]`
- Example code: [**app_flyweight.py**](https://github.com/talkpython/python-memory-management-course/blob/master/code/ch03-mem-and-variables/app_flyweight.py)
- Also working on a Python Design Patterns course and Flyweight is back there too.

**Brian #3:** [**What Are Python Wheels and Why Should You Care?**](https://realpython.com/python-wheels/)

- Brad Solomon
- Second half is about creating wheels
- I’m more interested in the first half, a discussion of wheels from the users perspective.
- Most package authors now all this stuff, or most of it. But this is a nice quick intro for the rest of the Python ecosystem as package users.
- If you `pip install` something that isn’t a wheel, it’s probably a tarball.
	- pip downloads the `tar.gz` file
	- builds a wheel, which includes calling setup.py
	- labels it
	- then installs it
- For pre-wheeled packages, the build and label aren’t needed, so it’ s faster
- Also, the download size is usually smaller, so that part is also faster.
- Wheels are essentially zip files with specially crafted filenames that tell installers what Python versions and platforms the wheel will support: 
	- `{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl`
	- ex: `cryptography-2.9.2-cp35-abi3-macosx_10_9_x86_64.whl`
- Wheels can have platform specific builds, like for macosx vs unix, etc.
- Advantages of wheels:
	- install faster
	- smaller
	- cut the setup.py execution out
	- no need for compiler as they can be os specific
	- auto generated .pyc files
	- provide consistency

Michael #4:  [Pandas_Alive](https://github.com/JackMcKew/pandas_alive)

- By Jake McKew
- Pandas_Alive is intended to provide a plotting backend for animated matplotlib charts for Pandas DataFrames, similar to the already existing Visualization feature of Pandas.
- With Pandas_Alive, creating stunning, animated visualizations is as easy as calling `df.plot_animated()`
- Also supports: GeoSpatialData with geopandas, basemaps with contextily, writing to GIF in memory (no external dependencies), progress bars with tqdm
- Since release 3 weeks ago, Pandas-Alive has been downloaded over 11,000 times off PyPI which is absolutely unreal
- Comes with visuals :)


**Brian #5:** [**How To Use the Python Map Function**](https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function)

- Kathryn Hancox
- `map()` is so useful, but not obvious to people coming from other languages. If you don’t use it much, that’s fine, but it’s nice to review occasionally because it does more than I originally gave it credit for.
- This tutorial walks through:
	- Normal map use with a lambda function applied to a list.
	- Using user defined functions. 
		- Actually this bit is more confusing than it needs to be as it has a function returning a map object, which is kinda weird in the particular circumstance. But doesn’t detract from the rest too much.
	- Using built in functions to map.
	- Using functions that take more than one argument and using map across multiple iterables.
- Takeaways
	- `map()` only applies the function one element at a time during iteration, so it’s efficient with large data sets and with sequences that won’t reach the end.
	- Remember you can use lambdas, built in functions, and you own functions with map.
	- You can use functions that take multiple arguments, but that requires passing in multiple iterables, one for each function argument.
	- Comprehensions are often just as useful, especially for small data sets, but don’t forget about map.

**Michael #6:** [**Version your SQL schemas with git + automatically migrate them**](https://github.com/abe-winter/automigrate)

- `automigrate` project
- Automigrate is a command-line tool for SQL migrations. Unlike other migration tools, it uses git history to do diffs on `create table` statements instead of forcing you to write up/down diffs for every change.
- This tool doesn't make you write & manage a giant folder of up/down migrations. It uses git history to infer them instead, and to version production databases.
- Not as nice as alembic (even though it portrays itself otherwise). But if you are writing DDL by hand, this is much better!
- Speaking of which: Generate ORM definitions from SQL: Experimental sqlalchemy generator in sa_harness.py. Try it out with:

```
    python -m automig.lib.sa_harness 'test/schema/*.sql'
```

Extras:

Michael:

- Get notified of release for new courses at [**training.talkpython.fm/getnotified**](https://training.talkpython.fm/getnotified)
	- Excel to Python
	- Getting Started in Data Science
	- Python Memory Management and Tips
	- Getting started with Git
	- Python Design Patterns

Jokes!

[“Engineers remove dead code after dropping a feature flag”, Sir Frank Bernard Dicksee, 1893, Oil on canvas](https://classicprogrammerpaintings.com/post/624257359339995136/engineers-remove-dead-code-after-dropping-a)

[“CSS without comments”, Pablo Picasso, 1912](https://classicprogrammerpaintings.com/post/621448927941689344/css-without-comments-pablo-picasso-1912)

[“Experienced developer deploys hotfix on production”, Francisco Goya, Oil on canvas, circa 1788](https://classicprogrammerpaintings.com/post/613838825589030912/experienced-developer-deploys-hotfix-on)
