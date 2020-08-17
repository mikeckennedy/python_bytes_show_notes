# Python Bytes 193
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

**Brian #1:** **Start using** `**pip install --use-feature=2020-resolver**` **if you aren’t already**

- Mathew Feickert
- You may see something interesting when you run pip
![Image](https://pbs.twimg.com/media/EeERublXoAILPct?format=png&name=small)

- This is not a problem. Do not adjust your sets. 
- But, you should be aware of it.
- Especially if you install from requirements generated with `pip freeze`, you’ll want to use `--use-feature=2020-resolver` everywhere:

```
    $ python -m pip install --use-feature=2020-resolver -r requirements_original.txt
    $ python -m pip freeze > requirements_lock.txt
    $ python -m pip install --use-feature=2020-resolver -r requirements_lock.txt
```

- Otherwise, you may run into issues
	- see [Example of --use-feature=2020-resolver breaking a pip freeze requirements.txt](https://gist.github.com/matthewfeickert/78cd03376435c05b6104f376cd43b537)
	- and [Changes to the pip dependency resolver in 20.2 (2020)](https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-2-2020)

**Michael #2:** [**Profiling Python import statements**](https://twitter.com/mkennedy/status/1276606467156537344)

- Conversation with Brandon Braner lead to [import-profiler](https://pypi.org/project/import-profiler/)
- A basic python import profiler to find bottlenecks in import times. 
- Not often a problem, imports can be an issue for applications that need to start quickly, such as CLI tools. 
- Goal of import profiler is to help find the bottlenecks when importing a given package.
- Example

```
    from import_profiler import profile_import
    
    with profile_import() as context:
        # Anything expensive in here
        import requests
    
    # Print cumulative and inline times. The number of + in the 3rd column
    # indicates the depth of the stack.
    context.print_info()
```

Output:

```
    umtime (ms) intime (ms) name
    83 0.5 requests
    55 0.5 +packages.urllib3.contrib
    54.1 0.3 ++
    53.1 0.7 +++connectionpool
    6.3 1.1 ++++logging
    ...
```


**Brian #3:** [**Django Testing Toolbox**](https://www.mattlayman.com/blog/2020/django-testing-toolbox/)

- Matt Layman
- Testing packages commonly used on Django projects
- Techniques Matt uses
- packages
	- pytest-django - duh
	- factory_boy - fake data
	- django-test-plus - beefed up TestCase with tons of helper utilities
- techniques
	- Using TestCase and test classes instead of functions
	- Arrange, Act Assert structure
	- In-memory SQLite database
	- Disable migrations while testing
	- faster password hasher 
	- Use your editor effectively to run tests

**Michael #4:** [**Pandas-profiling**](https://github.com/pandas-profiling/pandas-profiling)

- Recommended by Oz
- Considering the fact that Data Science users are almost the majority now for Python, I thought it would be nice to spread the word of pandas-profiling package. 
- This package enables you to do Exploratory Data Analysis (EDA) with a single command. It is really useful to understand what percent of the data is NULL, or how it is distributed. 
- I used to do these steps manually and it was quite time consuming. Now it is a breeze.
    
- Generates profile reports from a pandas `DataFrame`. The pandas `df.describe()` function is great but a little basic for serious exploratory data analysis. `pandas_profiling` extends the pandas DataFrame with `df.profile_report()` for quick data analysis.
- Features
	- **Type inference**: detect the [types](https://github.com/pandas-profiling/pandas-profiling#types) of columns in a dataframe.
	- **Essentials**: type, unique values, missing values
	- **Quantile statistics** like minimum value, Q1, median, Q3, maximum, range, interquartile range
	- **Descriptive statistics** like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
	- **Most frequent values**
	- **Histogram**
	- **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
	- **Missing values** matrix, count, heatmap and dendrogram of missing values
	- **Text analysis** learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.
	- **File and Image analysis** extract file sizes, creation dates and dimensions and scan for truncated images or those containing EXIF information.
- Nice examples too
	- [Census Income](https://pandas-profiling.github.io/pandas-profiling/examples/master/census/census_report.html) (US Adult Census data relating income)
	- [NASA Meteorites](https://pandas-profiling.github.io/pandas-profiling/examples/master/meteorites/meteorites_report.html) (comprehensive set of meteorite landings) 
	- [Titanic](https://pandas-profiling.github.io/pandas-profiling/examples/master/titanic/titanic_report.html) (the "Wonderwall" of datasets) 
	- [NZA](https://pandas-profiling.github.io/pandas-profiling/examples/master/nza/nza_report.html) (open data from the Dutch Healthcare Authority)
	- [Stata Auto](https://pandas-profiling.github.io/pandas-profiling/examples/master/stata_auto/stata_auto_report.html) (1978 Automobile data)
	- [Vektis](https://pandas-profiling.github.io/pandas-profiling/examples/master/vektis/vektis_report.html) (Vektis Dutch Healthcare data)
	- [Colors](https://pandas-profiling.github.io/pandas-profiling/examples/master/colors/colors_report.html) (a simple colors dataset)

**Brian #5:** [**Interfaces, Mixins and Building Powerful Custom Data Structures in Python**](https://rednafi.github.io/digressions/python/2020/07/03/python-mixins.html)

- Redowan Delowar
- “Supercharging Python's built-in data structures”
- Discussion of interfaces, abstract base classes, mixins, and Python
- Class hierarchies and utilizing interfaces, ABCs (informal and formal), mixins, etc. are less common in Python than in some other languages, but you can still use them to do some really cool things.
- I especially liked the introduction to the concepts and why they are useful, as well as why ABCs are different than interfaces.
- “Interfaces can be thought of as a special case of Abstract Base Classes

> "It’s imperative that all the methods of an interface are abstract methods and the classes don’t store any state (instance variables). However, in case of abstract base classes, the methods are generally abstract but there can also be methods that provide implementation (concrete methods) and also, these classes can have instance variables."

- Shows an example, and goes on to discuss mixins, a parent class that provides functionality to subclasses but is not intended to be instantiated itself.

**Michael #6:** [**Pickle’s 9 flaws**](https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html)

- Python’s pickle module is a very convenient way to serialize and de-serialize objects. It needs no schema, and can handle arbitrary Python objects. But it has problems. This post briefly explains the problems.
- Via [pycoders.com](https://pycoders.com/)
- Article by Ned Batchelder
	- **Insecure** - The insecurity is not because pickles contain code, but because they create objects by calling constructors named in the pickle. Any callable can be used in place of your class name to construct objects.
	- **Old pickles look like old code** - if your code changes between the time you made the pickle and the time you used it, your objects may not correspond to your code.
	- **Implicit** - they will serialize whatever structure your object has.
	- **Over-serializes** - They serialize everything in your objects, even data you didn’t want to serialize. For example, you might have an attribute that is a cache of computation that you don’t want serialized.
	- **__init__ isn’t called** - Pickles store the entire structure of your objects. When the pickle module recreates your objects, it does not call your __init__ method, since the object has already been created.
	- **Python only** - Pickles are specific to Python, and are only usable by other Python programs.
	- **Unreadable** - A pickle is a binary data stream (actually instructions for an abstract execution engine.) If you open a pickle as a plain file, you cannot read its contents.
	- **Appears to pickle code** - Functions and classes are first-class objects in Python: you can store them in lists, dicts, attributes, and so on. Pickle will gladly serialize objects that contain callables like functions and classes. But it doesn’t store the code in the pickle, just the name of the function or class.
	- **Slow** - Compared to other serialization techniques, pickle can be slow as Ben Frederickson demonstrates in [Don’t pickle your data](https://www.benfrederickson.com/dont-pickle-your-data/).


Extras:

Michael: 

- More on `Pathlib` by [Brett Ables:](https://twitter.com/flutefreak7/status/1287200446847823874) `text = Path(file).read_text()`
- I was a guest on [A Question of Code podcast](https://twitter.com/aQoCode/status/1287826329203810310). Ed, Tom, and I discussed:

Why is coding in Python such fun? And why is it so good for beginners and experts alike? Why might Python give you tangible results faster than JavaScript? And once you've learnt some Python, what are your career options? Find out all this and more in this week's pythonic installment of A Question of Code.

**Joke**


- ([via Aaron Brown](https://twitter.com/ab_was_taken/status/1287884897802006528))
- By Caitlin Hudon 👩🏼‍💻 [@beeonaposy](https://twitter.com/beeonaposy/status/1287797396471193601):
- I have a Python joke, but I don't think this is the right environment.
