# Python Bytes 119
Sponsored by [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Special guests**

* [Eric Chou](https://twitter.com/ericchou/)
* [Dan Bader](https://twitter.com/dbader_org/)
* [Trey Hunner](https://twitter.com/treyhunner)

**Michael #1:** [**Incrementally migrating over one million lines of code from Python 2 to Python 3**](https://blogs.dropbox.com/tech/2019/02/incrementally-migrating-over-one-million-lines-of-code-from-python-2-to-python-3/)

- Weighing in at over 1 million lines of Python logic, we had a massive surface area for potential issues in our migration from Python 2 to Python 3
- First Py3 commit, hack week 2015
	- Unfortunately, it was clear that many features were completely broken by the upgrade
- Official start H1 2017
- Armed with [Mypy](http://mypy-lang.org/), a static type-checking tool that we had adopted in the interim year, they made substantial strides towards enabling the Python 3 migration:
	- Ported our custom fork of Python to version 3.5
	- Upgraded some Python dependencies to Python 3-compatible versions, and forked some others (e.g. `babel`)
	- Modified some Dropbox client code to be Python 3 compatible
	- Set up automated jobs in our continuous integration (CI) to run the existing unit tests with the Python 3 interpreter, and Mypy type-checking in Python 3 mode
- Crucially, the automated tests meant that we could be certain that the limited Python 3 compatibility that existed would not have regressed when the project was picked up again.
- **Prerequisites**
- Before we could begin working on migrating any of our application logic, we had to ensure that we could load the Python 3 interpreter and run until the entry point of the application. In the past, we had used “freezer” scripts to do this for us. However, none of these had support for Python 3 around this time, so in late 2016, we built a custom, more native solution which we internally referred to as “Anti-freeze” (more on that in [the initial Python 3 migration blog post](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/)).
- Incrementally enabling unit tests and type-checking
- ‘Straddling’ Python 2 and Python 3
- Letting it bake
- Learnings (tl;dr)
	- Unit tests and typing are invaluable.
	- String encoding in Python is hard.
	- Incrementally migrate to Python 3 for great profit.

**Eric #2:** **Network Automation Development with Python (for fun and for profit)**

- Terms: NetDevOps (Cisco), NRE (Network Reliability Engineer)
- Libraires: [Netmiko](https://github.com/ktbyers/netmiko), [NAPALM](https://napalm-automation.net/), [Nornir](https://github.com/nornir-automation/nornir) 
- Free Lab Resources: [NRE Labs](https://labs.networkreliability.engineering/), [dCloud](https://dcloud.cisco.com/), [DevNet](https://developer.cisco.com/)
- Conferences: AnsibleFest (network automation track), [Cisco DevnetCreate](https://developer.cisco.com/devnetcreate/2019)

**Trey #3**: [Alkali file as DB](https://github.com/kneufeld/alkali)

- If you have structured data you want to query (like RSS feed, CSV, JSON, or any custom format of your own creation) you can use a Django ORM-like syntax to query it
- Save it to the same format or a different format because you control both the reading and the writing
- Kurt is at PyCascades so I got to chat with him about this

**Dan #4:** [**Carnegie Mellon Launches Undergraduate Degree in Artificial Intelligence**](https://www.cs.cmu.edu/news/carnegie-mellon-launches-undergraduate-degree-artificial-intelligence) ****

- Carnegie Mellon University's School of Computer Science will offer a new [undergraduate degree in artificial intelligence](https://www.cs.cmu.edu/bs-in-artificial-intelligence) beginning this fall
- The first offered by a U.S. university
- "Specialists in artificial intelligence have never been more important, in shorter supply or in greater demand by employers," said Andrew Moore, dean of the School of Computer Science.
- The bachelor's degree in AI will focus more on how complex inputs — such as vision, language and huge databases — are used to make decisions or enhance human capabilities

**Michael #5:** [**asyncio + PyQt5/PySide2**](https://github.com/gmarull/asyncqt)

- via [Florian Dahlitz](https://twitter.com/DahlitzF)
- `asyncqt` is an implementation of the `PEP 3156` event-loop with Qt. 
- This package is a fork of `quamash` focusing on modern Python versions, with some extra utilities, examples and simplified CI.
- Allows wiring events to Qt’s event loop that run on asyncio and leverage it internally.
- Example: [https://github.com/gmarull/asyncqt/blob/master/examples/aiohttp_fetch.py](https://github.com/gmarull/asyncqt/blob/master/examples/aiohttp_fetch.py)

**Dan #6:** [**4 things I want to see in Python 4.0**](https://hackernoon.com/4-things-i-want-to-see-in-python-4-0-85b853e86a88)

1. JIT as a first class feature
2. A stable .0 release
3. Static type hinting
4. A GPU story for multiprocessing
5. More community contributions

**Extras:**

Michael: My Python Async webcast [**recording is now available**](https://twitter.com/pycharm/status/1098662428030709762).
Michael: PyCon Israel in the first week of June ([https://il.pycon.org/2019/](https://il.pycon.org/2019/)), and the CFP opened today: [https://cfp.pycon.org.il/conference/cfp](https://cfp.pycon.org.il/conference/cfp)
Dan: [Python Basics Book](https://realpython.com/products/python-basics-book/)

**Joke:**

- **Q:** Why did the developer ground their kid?
- **A:** They weren't telling the **truthy**

