# Python Bytes 9
This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 9, recorded on **Tuesday, January 17th**. In this episode we discuss **TOPICS** [more]


**#1 (Brian): [Python Asynchronous I/O Walkthrough](http://pgbovine.net/python-async-io-walkthrough.htm)**

- In July, there was an open source book published called [500 Lines or Less](http://aosabook.org/en/index.html).
- One of the chapters was called [A Web Crawler With asyncio Coroutines](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html), written by A. Jesse Jiryu Davis and Guido van Rossum. It explains async networking, showing how non-blocking sockets work and how Python 3’s coroutines improve asynchronous network programs.
- As mentioned recently on A. Jesse Jiryu Davis’s blog [emptysqua.re](https://emptysqua.re/blog/video-walkthrough-web-crawler-with-coroutines/), the chapter may be difficult for a novice or intermediate developer to follow.
- This month, Philip Guo, an Assistant Professor at UC San Diego, has released an 8 part video series, 90 minutes total, so on the order of 10 minutes each, that walks through the article, including some coding examples that he walks through.
- Since async is something that takes a while to get your head around, I appreciate the multi-sensory education experience. Listening to Philip talk about it, watching him walk through the code and talk about the article, and having the article as a reference, is super helpful.
- [Talk Python #22: CPython Internals and Learning Python with pythontutor.com](https://talkpython.fm/episodes/show/22/cpython-internals-and-learning-python-with-pythontutor.com)
- [Talk Python #69: Write an Excellent Programming Blog](https://talkpython.fm/episodes/show/69/write-an-excellent-programming-blog)

**#2 (Michael):** [**4 likely future twists for Python**](http://www.infoworld.com/article/3146967/application-development/4-likely-future-twists-for-python.html)
by *Serdar Yegulalp*

1. **Python 2.x may live on**
	  * Python 2.x might also get a continued lease on life if independent developers decide to keep the branch going on their own.
	  * At least one such effort exists -- Naftali Harris's "[Python 2.8](https://github.com/naftaliharris/python2.8)" project, which backports improvements and bug fixes from Python 3 into the Python 2.x branch.
	  * it makes sense to make the 3.x leap, but it's likely we'll see a lot of keep-the-2.x-flame-alive efforts

2. **Requirements.txt may be replaced with something better**
	  * [Pipfile](https://github.com/pypa/pipfile) has been proposed as a possible replacement by the folks at the Python Packaging Authority, which is "the working group that maintains many of the relevant projects in Python packaging."
	  * Pipfile will be superior to requirements.txt file in a number of ways:
		    1. TOML syntax for declaring all types of Python dependencies.
		    2. One Pipfile (as opposed to multiple requirements.txt files).
		    3. Existing requirements files tend to proliferate into multiple files - e.g. dev-requirements.txt, test-requirements.txt, etc. - but a Pipfile will allow seamlessly specifying groups of dependencies in one place.
		    4. This will be surfaced as only two built-in groups (default & development). (see note below)
		    5. Fully specified (and deterministic) environments in the form of Pipfile.freeze. A deployed application can then be completely redeployed with the same exact versions of all recursive dependencies, by referencing the Pipfile.freeze file.
	  * Example pipfile:  
	
	    [[source]]
	    url = 'https://pypi.org/'
	    verify_ssl = true
	    
	    [requires]
	    python_version = '2.7'
	    
	    [packages]
	    requests = { extras = ['socks'] }
	    Django = '>1.10'
	    pinax = { git = 'git://github.com/pinax/pinax.git', ref = '1.4', editable = true }
	    
	    [dev-packages]
	    nose = '*'  
	
3. **Python could get more enterprise editions**
	* As the language has gained traction across the board, it's also appearing in versions aimed specifically at solving enterprise-grade problems.
	* Intel, for instance, elected to [repackage](http://www.infoworld.com/article/3117239/data-science/intels-python-distribution-turbocharges-data-science.html) the Anaconda science-and-math distribution of Python after outfitting it with extensions that give it a speed boost, albeit only on Intel processors. 
	* Anaconda is itself produced by Continuum Analytics, no stranger to enterprise data-analysis needs.
4. **Python's new software repository system could lead to enterprise-friendly Python package management**
	* One possibility being floated in this vein is the concept of an enterprise-grade package index for Python, as [discussed by Cristian Medina of Nimble Storage](https://medium.com/python-pandemonium/the-trusted-packaging-index-d16986de73c6):
	* Businesses always have a need for an on-premises, secure, encrypted and highly available distribution mechanism of compiled binaries. Together with setuptools providing various install capabilities that can cover non-Python code just as well, it seems like we could put together a decent product. Something like a Docker Trusted Registry.
	* I’m working on something here too that come out of the discussion of Talk Python #84

**#3 (Brian) [From Python to Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)**

- Nicolas P. Rougier - labri.fr
- “Nicolas P. Rougier is a full-time research scientist at Inria which is the French national institute for research in computer science and control.”
- Creative commons book for people who are intermediate level Python developers and want to use numpy for science or engineering.


**#4 (Michael):** [**openai/universe**](https://github.com/openai/universe)

- Universe: a software platform for measuring and training an AI's general intelligence across the world's supply of games, websites and other applications. [https://universe.openai.com](https://universe.openai.com/)
- Universe allows anyone to train and evaluate AI agents on an extremely wide range of real-time, complex environments.
- Universe makes it possible for any existing program to become an OpenAI Gym environment, without needing special access to the program's internals, source code, or APIs. 
  - It does this by packaging the program into a Docker container
  - presenting the AI with the same interface a human uses: 
    - sending keyboard
    - mouse events
    - receiving screen pixels
  - Our initial release contains over 1,000 environments in which an AI agent can take actions and gather observations.

**#5: (Brian): [Python requests deep dive](https://medium.com/@anthonypjshaw/python-requests-deep-dive-a0a5c5c1e093)**

- Anthony Shaw - on medium.com
- Converted a large project from httplib to requests
- Apache Libcloud
  - needed to provide a set of base classes that would handle HTTP and HTTPS REST/JSON, REST/XML and various other bizarre HTTP APIs. 
  - Libcloud has over 80 client libraries for every major cloud service out there. 
  - single Connection class that handles encoding and decoding of JSON, XML or Raw data.
- Anthony walks through the types of changes made, including authentication, session handling, testing, prepared requests, streams, … 
- uses  [requests-mock](https://github.com/openstack/requests-mock) 
  - very cool API

**#6 (Michael):** [What's the community favorite for developing OSX desktop applications with Python?](https://www.reddit.com/r/Python/comments/5n7p3p/whats_the_community_favorite_for_developing_osx/)

- [**bangeron**](https://www.reddit.com/user/bangeron)**:** I've been using PyQt for all my projects with a GUI: - It has a native look and feel - It's cross-platform (I do everything on macOS) - It's a whole framework, including modules for plotting charts, networking, SQL, etc. - It has *excellent* documentation. - It has a GUI editor (Qt Creator) that is pretty good, once you figure it out.
- [**Omnius**](https://www.reddit.com/user/Omnius): Same but using pyside to avoid license fees.
- [**spinwizard69**](https://www.reddit.com/user/spinwizard69): Use TK for simple apps! It is included with Python and avoids dependency hell.
- [**EssaAlshammri**](https://www.reddit.com/user/EssaAlshammri): Take a look at [Toga](http://pybee.org/project/projects/libraries/toga/) its idea is great.
- [**Ruditorres**](https://www.reddit.com/user/Ruditorres): Kivy hands down, it is pythonic, easy, and beautiful
- [**bangeron**](https://www.reddit.com/user/bangeron): Kivy is anything but beautiful. At least, not without spending some time creating your own theme.
- Personally, I want py_electron (modeled after [electronjs](http://electron.atom.io)).
- Notable mention, related: [cx_Freeze released](http://cx-freeze.readthedocs.io/en/latest/releasenotes.html) (Version 5.0.1 (January 2017))
