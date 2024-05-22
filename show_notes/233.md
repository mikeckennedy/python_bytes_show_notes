# Python Bytes 233

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: [**Marlene Mhangami**](https://marlenemhangami.com/)

**Brian #1:** [**readme.so**](https://readme.so/)

- Recommended by Johnny Metz
- This is not only useful, it’s fun
- Interactively create a README.md file
- Suggested sections great 
- There are lots of sections though, so really only pick the ones you are willing to fill in.
- I think this is nicer than the old stand by of “copying the README.md of another project” because that other project might not have some of these great sections, like:
	- Acknowledgements
	- API Reference
	- Authors
	- FAQ
	- Features
	- Logo
	- Roadmap
	- Usage/Examples
	- Running Tests
- Note, these sections are listed in alphabetical order, not necessarily the right order for how they should go in your README.md
- Produces a markdown file you can copy or download
- Also an editor so you can edit right there. (But I’d probably throw together the skeleton with dummy text and edit it in something with vim emulation.


**Michael #2:** [**Wafer-scale Python**](https://www.anandtech.com/show/16626/cerebras-unveils-wafer-scale-engine-two-wse2-26-trillion-transistors-100-yield)

- via Galen Swint
- Many new processors with the sole purpose of accelerating artificial intelligence and machine learning workloads.
- Cerebras, a chip company, built an AI-oriented chip that is 12”x12” (30cm^2) with 850,000 AI cores on board.
- Another way to look at it is that’s 2.6T transistors vs. my M1’s 0.0016T.
- Built through TSMC, as so many things seem to be these days.
- What’s the Python angle here? A key to the design is **the custom graph compiler**, that takes PyTorch or TensorFlow and maps each layer to a physical part of the chip, allowing for asynchronous compute as the data flows through.
- Shipping soon for just $3M+.

**Marlene** **#3:** [**RAPIDS**](https://rapids.ai/)

- This is the library I’m currently working on at NVIDIA. I work specifically on [CuDF](https://docs.rapids.ai/api/cudf/stable/10min.html) which is a Python GPU DataFrame library for loading, joining, aggregating, filtering, and manipulating tabular data using a DataFrame style API. 
- It mirrors the [Pandas API](https://pandas.pydata.org/) but operations are done on the GPU
- I gave a talk at PyCon Sweden a few months ago called [‘A Beginners Guide to GPU’s for Pythonista’s’](https://www.youtube.com/watch?v=5s8PljqLdkA). 
- Here’s an example of how long it takes for pandas vs. cudf to calculate the mean of a group of numbers in a column in a DataFrame:
```
    #we'll be calculating the mean of the data in a dataframe (table)
    import cudf
    import pandas as pd
    import numpy as np
    import time
    
    #lets create a data frame using pandas, that has two columns, a and b 
    #we're generating a dataframe where each column contains one hundred million rows
    #each row is filled with a random integer that can be between 0 to one hundred million
    pandas_df = pd.DataFrame({"a": np.random.randint(0, 100000000, size=100000000),
    "b": np.random.randint(0, 100000000, size=100000000)})
    
    #next we want to create a cudf version of this dataframe
    cudf_df = cudf.DataFrame.from_pandas(pandas_df)
    
    #now we'll use timeit to compare the time it takes to calculate the mean 
    #of the numbers in the column "a" of the dataframe. 
    
    #Lets time Pandas
    %timeit pandas_df.a.mean()
    
    #Lets time CuDF
    %timeit cudf_df.a.mean()
    
    #These were the results I got (might be a little slower if you're using the notebook on Colab)
    # pandas: 105 ms ± 298 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
    #cudf: 1.83 ms ± 4.51 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

- You can test this out for right now using the RAPIDS, [GPU powered notebook](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true) for free on Google Colab. 

**Brian #4:** [**datefinder**](https://datefinder.readthedocs.io/en/latest/) **and** [**dateutil**](https://dateutil.readthedocs.io/en/stable/index.html#)

- Recommended by **Ira Horecka**
- [Great calmcode.io video on datefinder](https://calmcode.io/shorts/datefinder.py.html)
- Neat use of comprehensions to explore sending a bunch of data into a tool:

```
    import datefinder
    date_strings = [
        "March 12 2010",
        "2010-03-12",
        "03/12/2010 12:42:12"
    ]
    [list(datefinder.find_dates(d)) for d in date_strings]
    # [[datetime.datetime(2010, 3, 12, 0, 0)],
    #  [datetime.datetime(2010, 3, 12, 0, 0)],
    #  [datetime.datetime(2010, 3, 12, 12, 42, 12)]]
```

- Nice focused library, used by 662 projects, according to GitHub
- datefinder finds dates in strings, then uses dateutil to parse them into datetime objects.
- dateutil is actually kind of amazing also, great for
	- parsing date strings
	- computing relative delas (next month, last week of the month, etc)
	- relative deltas between date and/or datetimes
	- amazing timezone support
	- comprehensive test suite
    - nice mix of both pytest and unittest. I’ll have to ask Paul Ganssle about that sometime.

**Michael #5:** [**Cinder - Instagram's performance oriented fork of CPython**](https://github.com/facebookincubator/cinder)

- via Anthony Shaw
- Instagram's performance oriented fork of CPython.
- They use a multi-process webserver architecture; the parent process starts, performs initialization work (e.g. loading code), and forks tens of worker processes to handle client requests.
- The overhead due to copy-on-write from reference counting long-lived objects turned out to be significant. They developed a solution called "**immortal instances**" to provide a way to opt-out objects from reference counting.
- "Shadowcode" or “**shadow bytecode**" is their inline caching implementation. It observes particular optimizable cases in the execution of generic Python opcodes and (for hot functions) dynamically replaces those opcodes with specialized versions.
- **Eager coroutine evaluation:** If a call to an async function is immediately awaited, we immediately execute the called function up to its first `await`.
- The **Cinder JIT** is a method-at-a-time custom JIT implemented in C++. And can achieve 1.5-4x speed improvements on many Python performance benchmarks.
- **Strict modules** is a few things rolled into one
- **Static Python** is an experimental bytecode compiler that makes use of type annotations to emit type-specialized and type-checked Python bytecode.
- Static Python plus Cinder JIT achieves 7x the performance of stock CPython on a typed version of the Richards benchmark.

**Marlene #6:** [**PyCon US 2021**](https://us.pycon.org/2021/)

- PyCon US starts today. Its the largest gathering of the Python community on earth!
- I’ll be hosting the [Diversity and Inclusion Work Group Meet and Greet](https://us.pycon.org/2021/events/diversity-inclusion/). I recently became the chair of this WG, which focuses on helping increase global diversity and inclusion in the python community. We’ll be going live on the main stage at PyCon on Saturday 15 May at 12pm EST. There will be lots of time for discussion, so I hope to see some of you there! 
- I’ll also be hosting the PSF EMEA members meeting, which will be on Saturday at 10am CAT. You can register on the [Meet up page](https://www.meetup.com/python-software-foundation-meetup-group/events/277616272/?rv=ce1&_xtd=gatlbWFpbF9jbGlja9oAJGJiZmYxZDQ3LWQ0ZDAtNGRhOC04YjgyLTI5M2ZlMmQ2YjJiNg&_af=event&_af_eid=277616272) or watch the livestream on the [PSF Youtube channel](https://www.youtube.com/channel/UCUAVDPguRzqHySnZw64CcOg). You can also find me in the PSF booth on Friday and Saturday morning, if you’d like to meet there!
- Some other talks I’m looking forward to attending are:
	- **Python Performance at Scale - Making Python Faster at Instagram**
	- **More Fun With Hardware and CircuitPython - IoT, Wearables, and more!**
	- **Large Scale Data Validation (with Spark and Dask)**
- Registration will be open all through the conference, so if you haven’t yet you can register [here](https://us.pycon.org/2021/registration/information/)

And of course all the keynotes this year! 

**Extras**

**Michael**

- [**Keep your fork in sync at GitHub**](https://twitter.com/github/status/1390382527588798477)
- [**Flask 2.0**](https://pypi.org/project/Flask/) is out! ([**Just interviewed David and Phil**](https://www.youtube.com/watch?v=G54QyX_lWo8) for Talk Python) (thanks Adam Parkin)
	- [New Major Versions Released! Flask 2.0, Werkzeug 2.0, Jinja 3.0, Click 8.0, ItsDangerous 2.0, and MarkupSafe 2.0](https://palletsprojects.com/blog/flask-2-0-released/)

**Brian**

- Lots of great feedback about last weeks [Test & Code interview with Brett Cannon about packaging](https://testandcode.com/152). I’m glad it was helpful to people. This week I’m talking with Ryan Howard about Playwright for automated browser testing. 
- Did you know we have 71 patrons on patreon? 
	- So cool. You too can support the show at [**patreon.com/pythonbytes**](https://www.patreon.com/pythonbytes)

**Marlene**

-  If you’d like to connect you can find me on twitter @marlene_zw
- You can also check out my site [marlenemhangami.com](https://marlenemhangami.com/)

**Joke** 

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/606c86cf22266a6168ba9770/64e57c479d236c5d805846f534d5273a/Image.jpeg)
