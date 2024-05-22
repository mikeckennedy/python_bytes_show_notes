# Python Bytes 194
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [Test & Code](https://testandcode.com/) Podcast

**Brian #1:** [**An introduction to mutation testing in Python**](https://opensource.com/article/20/7/mutmut-python)

- Moshe Zadka
- This article uses mutmut, but there are other mutation testing packages.
- The example shows 3 methods, and one test case that actually hits 100% code coverage.
- The mutmut is used and finds 16 surviving mutants.
- “Mutation testing algorithmically modifies source code and checks if any "mutants" survived each test. Any mutant that survives the unit test is a problem: it means that a modification to the code, likely introducing a bug, was not caught by the standard test suite.”
- “For each mutation test, `mutmut` modified portions of your source code that simulates potential bugs. An example of a modification is changing a `>` comparison to `>=` to see what happens. If there is no unit test for this boundary condition, this mutation will "survive": this is a potential bug that none of the tests will detect.”
- Cool example of how to check mission critical parts of your code and the tests around them above and beyond code coverage.
- BTW, mutmut is also used codechalleng.es in the challenges asking users to write the tests.

**Michael #2:** [**asynq**](https://github.com/quora/asynq)

- From Quora, a little old but still interesting and active
- A library for asynchronous programming in Python with a focus on batching requests to external services.
- Also provides seamless interoperability with synchronous code, support for asynchronous context managers, and tools to make writing and testing asynchronous code easier.
- Developed at Quora and is a core component of Quora's architecture.
- The most important use case for `asynq` is batching.
- `asynq`'s asynchronous functions are implemented as Python generator functions. Every time an asynchronous functions yields one or more Futures, it cedes control the asynq scheduler,

**Brian #3:** [**redis: Beyond the Cache**](https://redislabs.com/blog/beyond-the-cache-with-python/) 

- Guy Royse
- Some cool examples with Python code of using redis for more than a cache.
	- as a queue, with rpush and blpop
	- pub/sub, with publish and psubscribe
	- data streaming, with xadd and xread
	- as a search engine
	- and of course, as a primary in-memory database
- examples use aioredis to access with async/await

**Michael #4:** [**LittleTable**](https://github.com/ptmcg/littletable)

- Discovered as part of my multi-key dictionary quest (more on this later)
- By [Paul McGuire](https://github.com/ptmcg)
- A Python module to give ORM-like access to a collection of objects
- Provides a low-overhead, schema-less, in-memory database access to a collection of user objects.
- In addition to basic ORM-style insert/remove/query/delete access to the contents of a `Table`, `littletable` offers:
	- simple indexing for improved retrieval performance, and optional enforcing key uniqueness
	- access to objects using indexed attributes
	- simplified joins using '+' operator syntax between annotated Tables
	- the result of any query or join is a new first-class littletable Table

**Brian #5:** [**pytest-timeout**](https://pypi.org/project/pytest-timeout/)

- listener suggestion
- This is essential, I think.
- Make sure no test runs longer than a certain number of seconds.
- You can set a global timeout either via command line or via a config file.
- You can specify different times for specific tests via a mark decorator
- Great stopgap to make sure no test runs forever.

**Michael #6:** [**Events**](https://pypi.org/project/Events/)

- Call me, maybe
- by Nicola Iarocci
- Adds event subscription and callback to the Python language
- Based on C# language’s events, provides a handy way to declare, subscribe to and fire events. 
- Encapsulates the core to event subscription and event firing and feels like a “natural” part of the language.
- Example:
```
    >>> def something_changed(reason):
    ...     print(f"something changed because {reason}")
    
    >>> from events import Events
    >>> events = Events()
    >>> events.on_change += something_changed
```
- Multiple callback functions can subscribe to the same event. When the event is fired, all attached event handlers are invoked in sequence.
```
    >>> events.on_change('it had to happen')
    'something changed because it had to happen'
```
- Gist for Michael’s example:
- [gist.github.com/mikeckennedy/7235543fd5964bebabe1e3546ce67d91](https://gist.github.com/mikeckennedy/7235543fd5964bebabe1e3546ce67d91)

Extras:

Michael: 

- Finished the memory management course, coming soon. Started one on Python design patterns

Brian:

- [pytest 6.0.1 released](https://docs.pytest.org/en/stable/changelog.html)
    - I walk through some of the changes in [testandcode.com/125](https://testandcode.com/125)
    
Joke:

[https://xkcd.com/327/](https://xkcd.com/327/)
