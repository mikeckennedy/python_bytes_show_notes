# Python Bytes 96
Sponsored by DigitalOcean -- [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Plumbum: Shell Combinators and More**](https://plumbum.readthedocs.io/en/latest/)

- Toolbox of goodies to do shell-like things from Python.
- “The motto of the library is **“Never write shell scripts again”**, and thus it attempts to mimic the **shell syntax** (*shell combinators*) where it makes sense, while keeping it all **Pythonic and cross-platform**.”

Example:

    >>> from plumbum.cmd import grep, wc, cat, head
    >>> chain = ls["-a"] | grep["-v", "\\.py"] | wc["-l"]
    >>> print chain
    /bin/ls -a | /bin/grep -v '\.py' | /usr/bin/wc -l
    >>> chain()
    u'13\n'
    >>> ((cat < "setup.py") | head["-n", 4])()
    u'#!/usr/bin/env python\nimport os\n\ntry:\n'
    >>> (ls["-a"] > "file.list")()
    u''
    >>> (cat["file.list"] | wc["-l"])()
    u'17\n'

**Michael #2:** [Windows 10 Linux subsystem for Python developers](https://www.betteridiot.tech/blog/pop/betterblog/2018/9/windows-10-linux-subsystem-for-python-developers)

- via [Marcus Sherman](https://twitter.com/better_idiot/status/1036762663953620992)
- “One of the hardest days in teaching introduction to bioinformatics material is the first day: Setting up your machine.”
- While I have seen a very large bias towards Macs in academia, there are plenty of people that keep their Windows machines as a badge of pride... Marcus included.
- Even though Anaconda is cross platform and helpful, how does this work on Windows?
	- `python3 -m venv .env` and `source .env/bin/activate`?
	- Spoiler alert: Not well.
- Step by step getting Ubuntu on Windows
- Shows how to setup an x-server 

**Brian #3:** [**Type hints cheat sheet (Python 3)**](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

- Do you remember how to type hint duck types?
	- Something accessed like an array (list or tuple or …) and holds strings → `Sequence[str`]
	- Something that works like a dictionary mapping integers to strings → `Mapping[int, str]`
- As I’m adding more and more typing to interface functions, I keep this cheat sheet bookmarked.

**Michael #4:** [**Python driving new languages**](https://www.techrepublic.com/article/how-programming-will-change-over-the-next-10-years-5-predictions/)

-  Here are five predictions for what programming will look like 10 years from now.
	- Programming will be more abstract
	- Trends like serverless technologies, containers, and low code platforms suggest that many developers may work at higher levels of abstraction in the future
	- AI will become part of every developer's toolkit—but won't replace them
  - A universal programming language will arise
	- To reap the benefits of emerging technologies like AI, programming has to be easy to learn and easy to build upon
	- "Python may be remembered as being the great-great-great grandmother of languages of the future, which underneath the hood may look like the English language, but are far easier to use,"
  - Every developer will need to work with data
  - Programming will be a core tenet of the education system

**Brian #5:** [**asyncio documentation rewritten from scratch**](https://docs.python.org/3/library/asyncio.html)

- [twitter thread](https://twitter.com/1st1/status/1041855362402541568) by [**Yury Selivanov**](https://twitter.com/1st1)[**‏**](https://twitter.com/1st1)
	- “Big news! asyncio documentation has been rewritten from scratch! Read the new version here: [https://docs.python.org/3/library/asyncio.html …](https://t.co/Hoa08x3Y3Z).
    Huge thanks to [@WillingCarol](https://twitter.com/WillingCarol), [@elprans](https://twitter.com/elprans), and [@andrew_svetlov](https://twitter.com/andrew_svetlov) for support, ideas, and reviews!’
	- “BTW, this is just the beginning. We'll continue to refine and update the documentation. Next up is adding two tutorials: one teaching high-level concepts and APIs, and another teaching how to use protocols and transports. A section about asyncio architecture is also planned.”
	- “And this is just the beginning not only for asyncio documentation, but for asyncio itself.  Just for Python 3.8 we plan to add:
		* new streaming API
		* TaskGroups and cancel scopes
		* Supervisors and tracing API
		* new SSL implementation
		* many usability improvements”

**Michael #6:** [**The 2018 Python Language Summit**](https://lwn.net/Articles/754152/)

- Here are the sessions:
	- [Subinterpreter support for Python](https://lwn.net/Articles/754162/): a way to have a better story for multicore scalability using an existing feature of the language.
		- Subinterpreters will allow multiple Python interpreters per process and there is the potential for zero-copy data sharing between them. 
		- But subinterpreters share the GIL, so that needs to be changed in order to make it multicore friendly.
	- [Modifying the Python object model](https://lwn.net/Articles/754163/): looking at changes to CPython data structures to increase the performance of the interpreter.
			- via Instagram and Carl Shapiro
			- By modifying the Python object model fairly substantially, they were able to roughly double the performance
			- A little controversial
			- Shapiro's overall point was that he felt Python sacrificed its performance for flexibility and generality, but the dynamic features are typically not used heavily in performance-sensitive production workloads.
	- [A Gilectomy update](https://lwn.net/Articles/754577/): a status report on the effort to remove the GIL from CPython.
		- Larry Hastings updated attendees on the status of his [Gilectomy](https://lwn.net/Articles/689548/) project.
		- Since his [status report](https://lwn.net/Articles/723514/) at last year's summit, little has happened, which is part of why the session was so short. He hasn't given up on the overall idea, but it needs a new approach.
	- [Using GitHub Issues for Python](https://lwn.net/Articles/754779/): a discussion on moving from bugs.python.org to GitHub Issues.
		- Mariatta Wijaya described her reasoning for advocating moving Python away from its [current bug tracker](https://bugs.python.org/) to GitHub Issues.
		- it would complete Python's [journey to GitHub](https://lwn.net/Articles/689937/) that [started a ways back](https://lwn.net/Articles/623905/).
	- [Shortening the Python release schedule](https://lwn.net/Articles/755224/): a discussion on possibly changing from an 18-month to a yearly cadence.
		- The Python release cycle has an 18-month cadence; a new major release (e.g. Python 3.7) is made roughly on that schedule. 
		- But Łukasz Langa, who is the release manager for Python 3.8 and 3.9, would like to see things move more quickly—perhaps on a yearly cadence.
	- [Unplugging old batteries](https://lwn.net/Articles/755229/): should some older, unloved modules be removed from the standard library?
		- Python is famous for being a "batteries included" language—its standard library provides a versatile set of modules with the language
		- There may be times when some of those batteries have reached their end of life.
		- Christian Heimes wanted to suggest a few batteries that may have outlived their usefulness and to discuss how the process of retiring standard library modules should work.
	- [Linux distributions and Python 2](https://lwn.net/Articles/756628/): the end of life for Python 2 is coming, what distributions are doing to prepare.
		- Christian Heimes wanted to suggest a few batteries that may have outlived their usefulness and to discuss how the process of retiring standard library modules should work.
		- To figure out how to help the Python downstreams so that Python 2 can be fully discontinued.
	- [Python static typing update](https://lwn.net/Articles/757218/): a look at where static typing is now and where it is headed for Python 3.7.
		- Started things off by talking about [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files), which contain type information for libraries and other modules.
		- Right now, static typing is only partially useful for large projects because they tend to use a lot of packages from the Python Package Index (PyPI), which has limited stub coverage. There are only 35 stubs for third-party modules in the [typeshed](https://github.com/python/typeshed) library, which is Python's stub repository.
		- He suggested that perhaps a centralized library for stubs is not the right development model. Some projects have stubs that live outside of typeshed, such as Django and SQLAlchemy.
		- [PEP 561](https://www.python.org/dev/peps/pep-0561/) ("Distributing and Packaging Type Information") will provide a way to pip install stubs from packages that advertise that they have them.
	- [Python virtual environments](https://lwn.net/Articles/757354/): a short session on virtual environments and ideas for other ways to isolate local installations.
		- Steve Dower brought up the shortcomings of Python [virtual environments](https://virtualenv.pypa.io/en/stable/), which are meant to create isolated installations of the language and its modules.
		-  Thomas Wouters defended virtual environments in a response: The correct justification is that for the average person, not using a virtualenv all too soon creates confusion, pain, and very difficult to fix breakage. Starting with a virtualenv is the easiest way to avoid that, at *very* little cost.
		- But Beazley and others (including Dower) think that starting Python tutorials or training classes with a 20-minute digression on setting up a virtual environment is wasted time. 
	- [PEP 572 and decision-making in Python](https://lwn.net/Articles/757713/): a discussion of the controversy around PEP 572 and how to avoid the thread explosion that it caused in the future.
		- The "PEP 572 mess" was the topic of a 2018 Python Language Summit session led by benevolent dictator for life (BDFL) Guido van Rossum.
	- [Getting along in the Python community](https://lwn.net/Articles/757714/): trying to find ways to keep the mailing list welcoming even in the face of rudeness.
		- About tkinter…
	- [Mentoring and diversity for Python](https://lwn.net/Articles/757715/): a discussion on how to increase the diversity of the core development team.
		- Victor Stinner outlined some work he has been doing to mentor new developers on their path toward joining the core development ranks
		- Mariatta Wijaya gave a very personal talk that described the diversity problem while also providing some concrete action items that the project and individuals could take to help make Python more welcoming to minorities.

**Extras**

Listener feedback: CUDA is NVidia only, so no MacBook pro unless you have a custom external GPU.

