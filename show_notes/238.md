# Python Bytes 238

Sponsored by Sentry:

- Sign up at [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)
- And please, when signing up, click ***Got a promo code? Redeem*** and enter **PYTHONBYTES**

Special guest: [**Julia Signell**](https://twitter.com/JSignell)


**Brain #1:** [**Practical SQL for Data Analysis**](https://hakibenita.com/sql-for-data-analysis)

- Haki Benita
- Pandas is awesome, but … “In this article I demonstrate how to use SQL to perform fast and efficient data analysis.”
- First part of the article. 
	- SQL is faster than Pandas
	- But they are great together
- Then tons of examples showing exactly how to best use SQL queries and Pandas in data analysis::
	- Basics including random data and sampling
	- Descriptive statistics
	- Subtotals including rollup and groupign sets
	- Pivot tables, both conditional expressions and aggregate expressions
	- Running and cumulative agregation
	- Linear Regression
	- Interpolation
- Super cheat sheet for useful SQL queries


**Michael #2:** [**Git Blame in your Python Tracebacks**](https://twitter.com/ruslanoid/status/1396890700634066945)

- via Ruslan Portnoy, by Ofer Koren
- Helpful Modules: traceback & linecache
- traceback uses linecache, and we can change linecache line’s text
- They create a git blame bit of functionality to add to line’s source
- Turns out this flows to things like PDB.
- Ripe for a proper package we can add to requirements-dev.txt

**Julia #3:** [**fsspec: a unified file system library**](https://filesystem-spec.readthedocs.io/en/latest/)

- Martin Durant
- Other libraries conform to the interface so that each part of the analysis pipeline is like an interchangeable building block (for example s3fs, gcsfs)
- With the cloud providers competing to host data, fsspec makes it easy to swap out the read layer so that you can hop clouds.

**Brian #4:** [**The need for slimmer containers**](https://iximiuz.com/en/posts/thick-container-vulnerabilities/)
or I’m even more confused now as to the usefulness of official base images on Docker Hub

- **Ivan Velichko** [**@iximiuz**](https://twitter.com/iximiuz)
- I read this article recently and it had me concerned. Then just yesterday read it again and there are some updates. I’m still concerned, but now also confused. So let’s run it down.
- `docker scan` can be run on official Python images. 
	- It uses [Snyk Container](https://snyk.io/product/container-vulnerability-management/). We talked about [one form of Snyk on Episode 227](https://pythonbytes.fm/episodes/show/227/no-more-awaiting-async-comes-to-sqlalchemy).
- Spoiler, all of the official Python containers have vulnerabilities except alpine.
	- But. In an update, the author says that Alpine has a bunch of problems.
- The update includes some discussion on Hacker News
	- vulnerability scanners tend to have lots of false positives
	- official base images are rarely updated
	- some people suggest adding an upgrade command in the beginning of every Dockerfile.
	- but others object saying that the practice leads to unrepeatable builds
- So, I’m left with wondering if using official Python images are even worth it.
- Michael: [Python’s official image on docker hub](https://hub.docker.com/_/python)
- Michael: [PEP 656 -- Platform Tag for Linux Distributions Using Musl](https://www.python.org/dev/peps/pep-0656/)
- Michael: We dive a lot into this in our latest Talk Python recording (not out yet, but [**live stream is available**](https://www.youtube.com/watch?v=yDend6I9nwE))
- Some stats:
- Ubuntu: Found 32 vulnerabilities, 31 with upgrade.
- `python:latest`: Found 364 vulnerabilities, 353 with upgrade
- Ubuntu with source Python: 35 total, 28 low, 7 medium, several from intermediate tools such as wget, gcc, etc.
- Removing many dev tools SHOULD lower the count, but doesn’t (e.g. wget, gcc)
- Switching from `python:3-9` to `python:3.9-slim-buster` dropped the issues to 69.

**Michael #5:** [**PandasGUI: A GUI for analyzing Pandas DataFrames**](https://github.com/adamerose/pandasgui)

- Features
- View DataFrames and Series (with MultiIndex support)
- Interactive plotting
- Filtering
- Statistics summary
- Data editing and copy / paste
- Import CSV files with drag & drop
- Search toolbar
- Best way to see what it’s about is to [**watch the video**](https://www.youtube.com/watch?v=NKXdolMxW2Y).

**Julia #6:** [**xarray: pandas-like API for labeled N-dimensional data**](https://pypi.org/project/xarray/)

- We’ve been talking a lot about the pandas API and how it’s a common target for dataframe libraries.
- Xarray is not a dataframe library, it’s for labeled N-dimensional data. 
- People use it in geosciences, and in image processing where they don’t have tabular data, but the axes mean something (lat, lon, time, band…)
- You can select, aggregate, resample, using the real dimension labels. 
- It can be backed with dask arrays or numpy arrays (or other types of arrays).
- It supports plotting with `.plot`

**Extras**

**Michael**

- [Python 3.10.0b2 is available](https://www.python.org/downloads/release/python-3100b1/) (even [windows store](https://www.microsoft.com/en-us/p/python-310-beta/9pjpw5ldxlz5?activetab=pivot:overviewtab))
- Django security releases issued: 3.2.4, 3.1.12, and 2.2.24
- [**Another method overloading library**](https://twitter.com/Fronkan/status/1403350583260684292)?
- Recently moved to **pip-compile** requirements.in style after last week
- I’m [**running PyCharm EAP**](https://blog.jetbrains.com/pycharm/2021/06/pycharm-2021-2-eap/)

**Brian**

- Someone responded to me the other day on twitter with an emoji that I was not clear on the meaning of. So I looked it up on [emojipedia.org](https://emojipedia.org/).  Super useful for occasionally out of touch people like myself.
- [pytestbook.com](https://pytestbook.com) (redirects to [pythontest.com/pytest-book/)](https://pythontest.com/pytest-book/) has a facelift and a new home, to get ready for an announcement later this week. It’s built on markdown, hugo, github, and Netlify, so changes can be done super quick with just a commit and push. I just needed a nice readable theme, and [Pradyun’s blog](https://pradyunsg.me/) looked great, so I copied his choices.
- The blog will eventually also have writing, the legacy posts worth keeping from pythontesting.net, and probably transcripts from [Test & Code](https://testandcode.com/).

**Julia**

- GH CLI
- entrypoints - they are so cool! Example - with pandas you can plot with different backends not just matplotlib and the logic for those backends is contained in the plotting libraries not pandas.

**Joke** 

From **[https://upjoke.com/programmer-jokes](https://upjoke.com/programmer-jokes)**


- I asked a programmer what her New Year's resolution will be.
- She answered: 1920x1080.


- How does a programmer confuse a mathematician?
- x = x + 1


- Why do Python programmers have low self esteem?
- They're constantly comparing their `self` to `other`.
