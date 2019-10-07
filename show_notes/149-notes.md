# Python Bytes 149
Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Dropbox: Our journey to type checking 4 million lines of Python**](https://blogs.dropbox.com/tech/2019/09/our-journey-to-type-checking-4-million-lines-of-python/)

- Continuing saga, but this is a cool write up.
- Benefits
	- “Experience tells us that understanding code becomes the key to maintaining developer productivity. Without type annotations, basic reasoning such as figuring out the valid arguments to a function, or the possible return value types, becomes a hard problem. Here are typical questions that are often tricky to answer without type annotations:
		- Can this function return None?
		- What is this items argument supposed to be?
		- What is the type of the id attribute: is it int, str, or perhaps some custom type?
		- Does this argument need to be a list, or can I give a tuple or a set?”
	- Type checker will find many subtle bugs.
	- Refactoring is easier.
	- Running type checking is faster than running large suites of unit tests, so feedback can be faster.
	- Typing helps IDEs with better completion, static error checking, and more.
- Long story, but really cool learnings of how and why to tackle adding type hints to a large project with many developers.
- Conclusion. mypy is great now, because DropBox needed it to be.

**Michael #2:** [**Setting Up a Flask Application in Visual Studio Code**](https://www.youtube.com/watch?v=UXqiVe6h3lA)

- Video, but also as a post: https://blog.miguelgrinberg.com/post/setting-up-a-flask-application-in-visual-studio-code
- Follow on to the same in PyCharm:
	- [video](https://www.youtube.com/watch?v=bZUokrYanFM) and [post](https://blog.miguelgrinberg.com/post/setting-up-a-flask-application-in-pycharm)
- Steps outside VS Code
	- Clone repo
	- Create a virtual env (via venv)
	- Install requirements (via requirements.txt)
	- Setup flask app ENV variable
	- flask deploy ← custom command for DB
- VS Code
	- Open the folder where the repo and venv live
	- Open any Python file to trigger the Python subsystem
	- Ensure the correct VENV is selected (bottom left)
	- Open the debugger tab, add config, pick Flask, choose your app.py file
	- Debug menu, start without debugging (or with)
- Adding tests via VS Code
	- Open command pallet (CMD SHIFT P), Python: Discover Tests, select framework, select directory of tests, file pattern, new tests bottle on the right bar

**Brian #3:** [**Multiprocessing vs. Threading in Python: What Every Data Scientist Needs to Know**](https://sumit-ghosh.com/articles/multiprocessing-vs-threading-python-data-science/)

- How data scientists can go about choosing between the multiprocessing and threading and which factors should be kept in mind while doing so.
- Does not consider async, but still some great info.
- Overview of both concepts in general and some of the pitfalls of parallel computing.
- The specifics in Python, with the GIL
- Use threads for waiting on IO or waiting on users.
- Use multiprocessing for CPU intensive work.
- The surprising bit for me was the benchmarks
	- Using something speeds up the code. That’s obvious.
	- The difference between the two isn’t as great as I would have expected.
- A discussion of merits and benefits of both.
- And from the perspective of data science.
- A few more examples, with code, included.

**Michael #4:** [**ORM - async ORM**](https://github.com/encode/orm)

- And [https://github.com/encode/databases](https://github.com/encode/databases)
- The orm package is an async ORM for Python, with support for Postgres, MySQL, and SQLite.
- [SQLAlchemy core](https://docs.sqlalchemy.org/en/latest/core/) for query building.
- `[databases](https://github.com/encode/databases)` for cross-database async support.
- `[typesystem](https://github.com/encode/typesystem)` for data validation.
- Because ORM is built on SQLAlchemy core, you can use Alembic to provide database migrations.
- Need to be pretty async savy

**Brian #5:** [**Getting Started with APIs**](https://www.dataquest.io/blog/python-api-tutorial/)

- dataquest.io post
- Conceptual introduction of web APIs
- Discussion of GET status codes, including a nice list with descriptions. 
	- examples:
		- `301`: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
		- `400`: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
- endpoints
- endpoints that take query parameters
- JSON data
- Examples in Python for using:
	- `requests` to query endpoints.
	- `json` to load and dump JSON data.

**Michael #6:** [**Memory management in Python**](https://rushter.com/blog/python-memory-managment/)

- This article describes memory management in Python 3.6.
- Everything in Python is an object. Some objects can hold other objects, such as lists, tuples, dicts, classes, etc.
- such an approach requires a lot of small memory allocations
- To speed-up memory operations and reduce fragmentation Python uses a special manager on top of the general-purpose allocator, called PyMalloc.
- Layered managers
	- RAM
	- OS VMM
	- C-malloc
	- PyMem
	- Python Object allocator
	- Object memory
- Three levels of organization
	- To reduce overhead for small objects (less than 512 bytes) Python sub-allocates big blocks of memory.
	- Larger objects are routed to standard C allocator.
	- three levels of abstraction — `arena`, `pool`, and `block`.
	- **Block** is a chunk of memory of a certain size. Each block can keep only one Python object of a fixed size. The size of the block can vary from 8 to 512 bytes and must be a multiple of eight
	- A collection of blocks of the same size is called a pool. Normally, the size of the **pool** is equal to the size of a [memory page](https://en.wikipedia.org/wiki/Page_(computer_memory)), i.e., 4Kb.
	- The **arena** is a chunk of 256kB memory allocated on the heap, which provides memory for 64 pools.
- Python's small object manager rarely returns memory back to the Operating System.
- An arena gets fully released If and only if all the pools in it are empty.

**Extras**

Brian:

- Tuesday, Oct 6, [Python PDX West](https://www.meetup.com/Python-PDX-West/events/264793338/), 
- Thursday, Sept 26, I’ll be speaking at [PDX Python](https://www.meetup.com/pdxpython/events/gmxlbqyzmbjc/), downtown.
- Both events, mostly, I’ll be working on new programming jokes unless I come up with something better. :)

Michael:

- [Gitbook](https://www.gitbook.com/)
- [Call for Proposals for PyCon 2020 Is Open](https://pycon.blogspot.com/2019/09/call-for-proposals-for-pycon-2020-is.html)

**Jokes:**
A few I liked from the dad joke list.

- What do you call a 3.14 foot long snake? A π-thon
- What if it’s 3.14 inches, instead of feet? A μ-π-thon
- Why doesn't Hollywood make more Big Data movies? NoSQL.
- Why didn't the `<div />` get invited to the dinner party? Because it had no class.
