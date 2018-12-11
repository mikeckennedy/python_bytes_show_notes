# Python Bytes 109
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Python Descriptors Are Magical Creatures**](https://pabloariasal.github.io/2018/11/25/python-descriptors/)

- an excellent discussion of understanding `@property` and Python’s descriptor protocol.
- discussion includes getter, setter, and deleter methods you can override.

**Michael #2:** [**Data Science Survey 2018 JetBrains**](https://www.jetbrains.com/research/data-science-2018/)

- JetBrains polled over 1,600 people involved in Data Science and based in the US, Europe, Japan, and China, in order to gain insight into how this industry sector is evolving
- Key Takeaways
	- Most people assume that **Python will remain the primary programming language in the field for the next 5 years**.
	- Python is currently the **most popular language among data scientists**.  
	- Data Science **professionals tend to use Keras and Tableau**, while amateur data scientists are more likely to prefer Microsoft Azure ML. 
- Most common activities among pros and amateurs: 
	- Data processing
	- Data visualization
- Main programming language for data analysis
	- Python 57%
	- R 15%
	- Julia 0%
- IDEs and Editors
	- Jupyter 43%
	- PyCharm 38%
	- RStudio 23%
	- …

**Brian #3:** [**cache.py**](https://github.com/bwasti/cache.py)

- `cache.py` is a one file python library that extends [memoization](https://en.wikipedia.org/wiki/Memoization) across runs using a cache file.
- memoization is an incredibly useful technique that many self taught or on the job taught developers don’t know about, because it’s not obvious.
- example:

```
    import cache
    
    @cache.cache()
    def expensive_func(arg, kwarg=None):
      # Expensive stuff here
      return arg
```

- The `@cache.cache()` function can take multiple arguments.
	- `@cache.cache(timeout=20)` - Only caches the function for 20 seconds.
	- `@cache.cache(fname="my_cache.pkl")` - Saves cache to a custom filename (defaults to hidden file `.cache.pkl`)
	- `@cache.cache(key=cache.ARGS[KWARGS,NONE])` - Check against args, kwargs or neither of them when doing a cache lookup.

**Michael #4:** [**Setting up the data science tools**](https://www.youtube.com/watch?v=Ksu5zZIdfH0)

- part of a larger video series
- set up. Tools to keras ultimately
- Tools
	- anaconda
	- tensorflow
	- Jupyter
	- Keras
- good for true beginners 
- setup and activate a condo venv 
- Start up a notebook and switch envs 
- use conda, rather than pip

**Brian #5:** [**chartify**](https://github.com/spotify/chartify)

- “Python library that makes it easy for data scientists to create charts.”
- from the docs:
	- Consistent input data format: Spend less time transforming data to get your charts to work. All plotting functions use a consistent tidy input data format.
	- Smart default styles: Create pretty charts with very little customization required.
	- Simple API: We've attempted to make to the API as intuitive and easy to learn as possible.
	- Flexibility: Chartify is built on top of [Bokeh](http://bokeh.pydata.org/en/latest/), so if you do need more control you can always fall back on Bokeh's API.

**Michael #6:** [**CPython byte code explorer**](https://github.com/jtpio/jupyterlab-python-bytecode)

- JupyterLab extension to inspect Python Bytecode
- via [Anton Helm](https://twitter.com/HelmAnton/status/1043892163942199297)
- by Jeremy Tuloup
- You’ll see exactly what it’s about if you watch the GIF movie at the github repo.
- Can’t think of a better way to understand Python bytecode quickly than to play a little with this
- Comparing versions of CPython: If you have several versions of Python installed on your machine (let's say in different conda environments), you can use the extension to check how the bytecode might differ.
- Nice visualization of different performance aspects of while vs. for at the end

Extras:

Brian: 

-  [“How the Internet is made.”](https://www.reddit.com/r/funny/comments/a1vxu0/how_the_internet_is_made/) 
