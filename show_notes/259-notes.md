# Python Bytes 259

Sponsored by **Shortcut - Get started at** [**shortcut.com/pythonbytes**](http://shortcut.com/pythonbytes)

Special guest: **Renee Teate**

**Michael #1:** [**pypi-changes**](https://twitter.com/btskinn/status/1456293623599935490)

- [**via Brian Skinn**](https://twitter.com/btskinn/status/1456293623599935490)**,** created by ****[**Bernát Gábor**](https://twitter.com/gjbernat/status/1456207118470684674)
- Visually show you which dependencies in an environment are out of date.
- See the age of everything you depend upon. 
- Also, shoutout again to [**pipdeptree**](https://github.com/naiquevin/pipdeptree)

**Brian #2:** [**Late-bound argument defaults for Python**](https://lwn.net/SubscriberLink/875441/c29a2006cf489b7f/)

- Default values for arguments to functions are evaluated at function definition time.
- If a value is a short expression that uses a variable, that variable is in the scope of the function definition.
- The expression cannot use other arguments.
- Example of what you cannot do:
```
    def foo(a, b = None, c = len(a)):
        ...
```
- There’s a proposal by Chris Angelico to add a `=:` operator for late default evaluation.
    - syntax still up in the air. `=>` and `?=` also discussed
- However, it’s non-trivial to add syntax to an established language, and this article notes:
    - At first blush, Angelico's idea to fix this "wart" in Python seems fairly straightforward, but the discussion has shown that there are multiple facets to consider. It is not quite as simple as "let's add a way to evaluate default arguments when the function is called"—likely how it was seen at the outset. That is often the case when looking at new features for an established language like Python; there is a huge body of code that needs to stay working, but there are also, sometimes conflicting, aspirations for features that could be added. It is a tricky balancing act.

**Renee #3:** [**pandas.read_sql**](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
Since I wrote my book SQL for Data Scientists, I’ve gotten several questions about how I use SQL in my python scripts. It’s really simple: You can save your SQL as a text file and then import the dataset into a pandas dataframe to do the rest of my data cleaning, feature engineering, etc. Pandas has a built-in way to use SQL as a data source. You set up a connection to your database using another package like SQL Alchemy, then send the SQL string and the connection to the pandas.read_sql function. It returns a dataframe with the results of your query. 
[I can give an example of how I use SQL at work in my predictive modeling process]

**Michael #4:** [**pyjion**](https://talkpython.fm/episodes/show/340/time-to-jit-your-python-with-pyjion)

- by Anthony Shaw
- Pyjion is a JIT for Python based upon CoreCLR
- Check out [**live.trypyjion.com**](https://live.trypyjion.com/) ****to see it in action**.**
- Requires Python 3.10, .NET Core 6
- Enable with just a couple of lines:
```
    >>> import pyjion
    >>> pyjion.enable()
```

**Brian #5:** [**Tips for debugging with print()**](https://adamj.eu/tech/2021/10/08/tips-for-debugging-with-print/)

- Adam Johnson
- 7 tips altogether, but I’ll highlight a few I loved reading about
- Debug variables with f-strings and `=`
    - `print(f``"``{myvar=}``"`)  
    - Saves typing over  `print(f``"``myvar={myvar}`") with the same result
- Make output “pop” with emoji (Brilliant!)
    - `print("👉 spam()")`
    - Here’s some cool ones to use
        - 👉 ❌ ✅ 
- Use `rich.print` or `pprint` for pretty printing
    - Also, cool rename example to have both print and rich.print available
        - `from rich import print as rprint`
    - Both `rich.print` and `pprint.pprint` are essential for printing structures nicely
- Brian’s addition
    - In pytest, failed tests report the stdout contents by default from the test
    - I love the idea of using `rich.print` and emoji for print statements in tests themselves.
    - Even though you can use `--showlocals` to print local variables for failed tests, having control of some output to help you debug something if it ever fails is a good thing.

**Renee #6:** [**SHAP**](https://shap.readthedocs.io/en/latest/index.html) (and [beeswarm plot](https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/beeswarm.html?highlight=beeswarm))

- Brought to my attention by my team member Brian Richards at HelioCampus, and now they’re becoming a standard part of some of our model evaluation/explanation outputs
- SHapley Additive exPlanations
    - Shapley values from game theory
- Additive: “SHAP values of all the input features will always sum up to the difference between baseline (expected) model output and the current model output for the prediction being explained”
    - Negative/positive - pushing the prediction towards one class or the other
        - There’s a SHAP value for every feature for every prediction
    - Waterfall plots
    - Scatterplots of input value vs SHAP value
    - SHAP value can be outputted and pulled into other tools (I use them in Tableau)
- Correlation not causation
- [Beeswarm plots](https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/beeswarm.html?highlight=beeswarm) for feature importance with input value vs SHAP value

**Extras**

Brian:

- Matthew Feickert recommended `pip index` and specifically `pip index versions`  as a cool thing to try.
    - Example. `pip index versions pyhf` reports
        - all versions of `pyhf` available on pypi
        - the latest version
        - your installed version
    - It’s currently “experimental” so conceptually the pypa could yank it. But we like it. I hope it stays.

Michael:

- My [**PyCharm webcast**](https://twitter.com/pycharm/status/1460975261948723208?s=12) 

**Renee**: 

- My book and companion website with interactive query editor: [SQL for Data Scientists](https://sqlfordatascientists.com/)


**Joke:** [**git messages**](https://twitter.com/fvoron/status/1455979278936444930)
