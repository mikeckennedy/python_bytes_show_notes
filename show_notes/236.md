# Python Bytes 236

Sponsored by Sentry:

- Sign up at [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)
- And please, when signing up, click ***Got a promo code? Redeem*** and enter **PYTHONBYTES**

Special guest: [**Anastasiia Tymoshchuk**](https://twitter.com/anastasiatymo)

**Brian #1:** **Using accessible colors,** [**monolens**](https://github.com/HDembinski/monolens) **&** [**CMasher**](https://github.com/1313e/CMasher)

- Tweet by Matthew Feickert, [@HEPfeickert](https://twitter.com/HEPfeickert) 
	- “I need to give some serious praise to fellow Scikit-HEP dev Hans Dembinski on his excellent [monolens](https://github.com/HDembinski/monolens) tool for interactive simulation of kinds of color blindness. It works really quite well and the fact that is a pipx install away is awesome!
- [monolens](https://github.com/HDembinski/monolens) lets you “view part of your screen in greyscale or simulated colorblindness”
	- So simple. Just pops up a box that you can drag around your monitor and view stuff in greyscale.
- Reply tweet by Niko, [@NikoSercevic](https://twitter.com/NikoSarcevic)
	- “I mean to use cmasher so I know it’s cb friendly”
- [CMasher](https://github.com/1313e/CMasher) : “Scientific colormaps for making accessible, informative and *cmashing* plots”
	- Provides a collection of scientific colormaps and utility functions to be used by different Python packages and projects, mainly in combination with matplotlib.
	- Lots of great colormaps that are color blindness friendly.
	- Just specify the CB friendly colormaps with plots, super easy.
    
```
    # Import CMasher to register colormaps
    import cmasher as cmr
    
    # Import packages for plotting
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Access rainforest colormap through CMasher or MPL
    cmap = cmr.rainforest                   # CMasher
    cmap = plt.get_cmap('cmr.rainforest')   # MPL
    
    # Generate some data to plot
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = x**2+y**2
    
    # Make scatter plot of data with colormap
    plt.scatter(x, y, c=z, cmap=cmap, s=300)
    plt.show()
```

**Michael #2:** [**rapidfuzz: Rapid fuzzy string matching in Python and C++**](https://pypi.org/project/rapidfuzz/)

- via **Mikael Honkala**
- Rapid fuzzy string matching in Python and C++ using the Levenshtein Distance
- “you mention fuzzywuzzy for fuzzy text matching in the last episode, and wanted to mention the rapidfuzz package as a high-performance alternative.”
- “non-rigorous performance testing of several alternatives (including fuzzywuzzy), and rapidfuzz came out on top with a sizable margin.”
- Simple Ratio example:

```
    > fuzz.ratio("this is a test", "this is a test!")
    96.55171966552734
```

**Anastasiia #3:** [**Structlog to improve your logs**](https://www.structlog.org/en/stable/)

- One of the best ways to improve logs is to add more structure to them
- Why do we even need to care about logs?
	- logs can provide visibility to production, what is actually happening
	- logs can help to improve tracing of a bug, especially if logs are machine-readable and easy parseable
	- logs can give you a clue why a bug or an exception occurred
- It’s super easy to start with Structlog, also easy to integrate it with ELK stack for further processing
- Features that you will get if switch your logs to use structlog:
	- readable structure of logs in key-value pairs
	- easy to parse with any post processor to visualise logs and to have more visibility for your code
	- you can create custom log levels and separate specific logs with event keys for each log
- I am working with structured logs for a couple of years and recommend everyone to try

**Brian #4:** **xfail now works with pytest-subtests**

- Admittedly, there may be few people that care about this, but I’m one of them.
- [subtests are a kinda weird feature of unittest that came in with Python 3.4](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests)
- They’re really a context manager that you can use within a test function 
- pytest started supporting them through a plugin, [pytest-subtests](https://github.com/pytest-dev/pytest-subtests), sometime in 2019
- With the plugin, you can use either the unittest style, or a fixture fixture style, without unittest.
- It’s a similar problem/solution that [pytest-check](https://pypi.org/project/pytest-check/) solves to allow multiple failures per test case.
- But, like I said, they have some quirks.
	- See Paul Ganssle’s [Subtests in Python](https://blog.ganssle.io/articles/2020/04/subtests-in-python.html) 
	- [T&C 111: Subtests in Python with unittest and pytest](https://testandcode.com/111)
- One quirk is that xfail didn’t work right. It’s discussed in both links above.
- Anyway, it’s fixed now, [thanks to maybe-sybr](https://github.com/pytest-dev/pytest-subtests/pull/40), as of version 0.5.0
- So you can now trust that xfail will work properly with subtest

**Michael #5:** [**BaseSettings in Pydantic**](https://pydantic-docs.helpmanual.io/usage/settings/)

- via Denis Roy
- Create a model that inherits from `BaseSettings`
- The model initialiser will attempt to determine the values of any fields not passed as keyword arguments by reading from the environment.
- This makes it easy to:
	- Create a clearly-defined, type-hinted application configuration class
	- Automatically read modifications to the configuration from environment variables
	- Manually override specific settings in the initialiser where desired (e.g. in unit tests)
- Get values from OS ENV or .env files
- Also has support for secrets files

**Anastasiia #6:** **Take care of the documentation on your team will thank you later**

- [Sphinx and ReadTheDocs](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) will make life of developers so much easier
- Everyone knows importance of documentation, but how to keep it up to date?
- In my experience, I tried to use Confluence, describe new features in detailed Jira tickets, write some hints in Google docs and sharing them with the team. It does not work, as documentation is getting outdated and piles up drastically
- Benefits of implementing continuous documentation for the code:
	- easy to support by writing docstrings, updating them when needed
	- easy to find needed information in a centralised documentation
	- easy to keep versioning for each new release of the code
	- [ReadTheDocs](http://readthedocs.org/) if free for open source code
	- [Sphinx](https://www.sphinx-doc.org/en/master/) will generate code reference documentation for the code
    

**Extras**

**Michael**

- `pipx` is now part of the PyPA ([**via Matthew Feickert**](https://twitter.com/HEPfeickert/status/1397940429690183680))
- I’ll be “speaking” at [**Manning’s Developer Productivity conference**](https://freecontent.manning.com/livemanning-conferences-developer-productivity/). It’s free, so feel free to sign up.
- [**Cloud bills, they do pile up**](https://twitter.com/alexwlchan/status/1399095011178958851)!
- [**Flake8-FastAPI**](https://twitter.com/btskinn/status/1400078775543533574) (via Brian Skinn)
- Want to contribute to Jupyter? [**Add a localization**](https://twitter.com/SShanabrook/status/1293621116968112128).

**Brian**

- pytest uses. Please comment on [this thread](https://twitter.com/brianokken/status/1399955798596341763?s=20) if you know of some great projects that use pytest, if they converted from something else, or just find it interesting that they use pytest.


**Joke** 

First time recursion

![](https://trello-attachments.s3.amazonaws.com/5edf2fa473187d5cbdab9803/1110x808/24997ebb3c63092991390c47d4784ed4/Screen_Shot_2020-06-08_at_10.35.09_PM.png)
