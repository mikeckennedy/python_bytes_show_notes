# Python Bytes 58
Sponsored by DigitalOcean: **[http://do.co/python](http://do.co/python)**

**Brian #1:** [**Instagram open sources MonkeyType**](https://engineering.instagram.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881)

- *Carl Meyer, an engineer on Instagram’s infrastructure team.*
- (Note: [we talked about Dropbox’s pyannotate in episode 54](https://pythonbytes.fm/episodes/show/54/pyannotate-your-way-to-the-future). pyannotate is not on Python3 yet and generates comment style annotations that are Py2 compatible)
- MonkeyType is Instagram’s tool for automatically adding type annotations to your Python 3 code via runtime tracing of types seen.
- Requires Python 3.6+
- Generates only Python 3 style type annotations (no type comments)

**Michael #2:** [**cachetools**](https://cachetools.readthedocs.io/en/latest/)

- Extensible memoizing collections and decorators
- Think variants of Python 3 Standard Library @lru_cache function decorator
- Caching types:
	- `cachetools.Cache` Mutable mapping to serve as a simple cache or cache base class.
	-  `cachetools.LFUCache` Least Frequently Used (LFU) cache implementation
	-  `cachetools.LRUCache` Least Recently Used (LRU) cache implementation
	- `cachetools.TTLCache` LRU Cache implementation with per-item time-to-live (TTL) value.
	- And more
- Memoizing decorators
	- `cachetools.cached` Decorator to wrap a function with a memoizing callable that saves results in a cache.
	- Note that cache need not be an instance of the cache implementations provided by the `cachetools` module. cached() will work with any mutable mapping type, including plain dict and `weakref.WeakValueDictionary`.
	- Can pass key function for hash insertions and lock object for thread safety.

**Brian #3:** [**Going Fast with SQLite and Python**](http://charlesleifer.com/blog/going-fast-with-sqlite-and-python/)

- Charles Leifer
- Many projects start with SQLite, as it’s distributed with Python as [sqlite3](https://docs.python.org/3/library/sqlite3.html).
- This article discusses some ways to achieve better performance from SQLite and shares some tricks.
  - transactions, concurrency, and autocommit
  - user-defined functions
  - using pragmas
  - compilation flags

**Michael #4: [The graphing calculator that makes learning math easier.](https://www.numworks.com/features/)**

- A full graphing calculator
- Programmable in Python
- Exam approved: Take the SAT and the ACT.
- Free browser emulator

**Brian #5:** [**Installing Python Packages from a Jupyter Notebook**](http://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/index.html)

- Jake VanderPlas
- using conda
    import sys
    !conda install --yes --prefix {sys.prefix} numpy
- using pip 
    import sys
    {sys.executable} -m pip install numpy
- plus a discussion of why this is weird in Jupyter

**Michael #6:** [**Videos from PyConDE 2017 are online**](https://www.youtube.com/user/PyConDE/videos)

- via Miroslav Šedivý [@eumiro](https://twitter.com/eumiro/status/936671094429364225)
- Lots of interesting talk titles
- Almost all in English
