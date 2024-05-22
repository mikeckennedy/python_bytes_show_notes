# Python Bytes 53
Sponsored by Rollbar! Get the bootstrap plan at [pythonbytes.fm/rollbar](https://pythonbytes.fm/rollbar)

**Brian #1:** [**Exploring Line Lengths in Python Packages**](http://jakevdp.github.io/blog/2017/11/09/exploring-line-lengths-in-python-packages/)

- Jake VanderPlas [**@**](https://twitter.com/jakevdp)[jakevdp](https://twitter.com/jakevdp)
- PEP8 recommends 79 character line lengths.
- This article looks at line lenghts used in NumPy, SciPy, Pandas, ScikitLearn, Matplotlib, and AstroPy
- In the form of a Jupyter notebook so you can follow along with all the code and graphs.
- Fitting the graphs to distributions.
- Closing questions from Jake:
	- Where do other Python packages fit on the mode/spread graph?
	- Has the coding style in these packages, reflected in line length, evolved over time?
	- How do individual contributors behave? Do they tend to have similar habits across packages?
	- What do these distributions look like for code written in other languages?

**Michael #2:** [**NumPy: Plan for dropping Python 2.7 support**](https://github.com/numpy/numpy/blob/master/doc/neps/dropping-python2.7-proposal.rst)

- The Python core team plans to stop supporting Python 2 in 2020. 
- We found that supporting Python 2 is an increasing burden on our limited resources; thus, we plan to eventually drop Python 2.
- Our current plan is as follows.
  - Until **December 31, 2018**, all NumPy releases will fully support both Python2 and Python3.
  - Starting on **January 1, 2019**, any new feature releases will support only Python3.

**Brian #3:** [**How to Learn Pandas**](https://towardsdatascience.com/how-to-learn-pandas-108905ab4955)

- Ted Petrou [@TedPetrou](https://twitter.com/TedPetrou)
- Alternating between reading documentation and using it for small projects.
- Getting the most out of documentation
- Using Jupyter Notebook
- Using Kaggle kernels, which are datasets in the form of Jupyter notebooks.
- Creating your own kernels
- Try answering questions on SO to test your knowledge
- Set up some projects.

**Michael #4:** [Microsoft and GitHub team up to take Git virtual file system to macOS, Linux](https://arstechnica.com/gadgets/2017/11/microsoft-and-github-team-up-to-take-git-virtual-file-system-to-macos-linux/)

- Watch the [10 min Microsoft presentation](https://channel9.msdn.com/Events/Connect/2017/T179) to understand this quickly.
- Git doesn’t work that well for larger projects
	- Yes, it was built for Linux (640 MB) 
	- But there are larger projects
		- Visual Studio and related tools: 3,000 MB (5x)
		- Windows: 270 GB (421x), 4,000 people committing per day.
	- solution was to develop Git Virtual File System (GVFS)
- Before virtual:
	- 12 hours to clone
	- 3 hours to checkout
	- 8 min for `git status`
	- 30 min to commit
- After virtual:
	- 90 sec clone
	- 30 sec checkout
	- 3 sec `git status`
	- 8 sec commit
- Microsoft says that, so far, about half of its modifications have been accepted upstream, with upstream Git developers broadly approving of the approach the company has taken to improve the software's scaling.
- GitHub is interested in this for the paid, enterprise side
- Currently Windows only but Microsoft and GitHub are also working to bring similar capabilities to other platforms, with macOS coming first, and later Linux.

**Brian #5:** [**Getting started with devpi**](https://stefan.sofa-rockers.org/2017/11/09/getting-started-with-devpi/)

- Stefan Scherfke [**@**](https://twitter.com/sscherfke)[sscherfke](https://twitter.com/sscherfke)
- A walkthrough of setting up and using [devpi](https://docs.devpi.net/) , a local mirror/cache/local store PyPI server.
- Setting up the server
- User management
- Working with package indexes
- Uploading packages
- Using it to point your pip at


**Michael #6:** [**Marketing-for-Engineers**](https://github.com/LisaDziuba/Marketing-for-Engineers)

- A curated list of marketing tools and resources to grow your product
- such as:
	- finding beta testers
	- growing first user base
	- advertising project without a budget
	- scaling marketing activities for building constant revenue streams.
- What is the hardest part of creating a successful product / web app? (hint: it’s not programming or having the idea)

**Extras**

- Black Friday Sale for [**Python Testing with pytest**](https://pragprog.com/book/bopytest/python-testing-with-pytest) & all other pragmatic eBooks.
	- From 11/22 through Friday 12/1, all ebooks at [pragprog.com](http://pragprog.com/) are 40% off.
	- That makes the pytest book about $14
	- Use coupon code **turkeysale2017** to get the discount.
- [**PyCon Columbia**](https://www.pycon.co/), [**@**](https://twitter.com/pyconcolombia)[pyconcolombia](https://twitter.com/pyconcolombia), is February 9, 10 and 11 - 2018 and tickets are available now. (Recommended by Oscar Arbelaez)
