# Python Bytes 73
Sponsored by Datadog: [**pythonbytes.**](https://pythonbytes.fm/datadog)[**fm**](https://pythonbytes.fm/datadog)[**/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Set Theory and Python**](http://www.idiotinside.com/2017/08/19/set-theory-and-python-tips-tricks/)

- “Let’s talk about sets, baby …” is what I have in my head while reading this.
- Great overview of set theory and how to use the set data type in Python.
- Covered:
	- Creating sets
	- Checking for containment (in, not in)
	- union : set of things in either set or in both
	- intersection: set of things in 2 sets
	- difference: set of things in one set but not the other
	- symmetric difference: set of things in either set but not in both

**Michael #2:** [**Trio: async programming for humans and snake people**](https://trio.readthedocs.io/en/latest/index.html)

-  The Trio project’s goal is to produce a production-quality, permissively licensed, async/await-native I/O library for Python. Like all async libraries, its main purpose is to help you write programs that do multiple things at the same time with parallelized I/O. 
- Compared to other libraries, Trio attempts to distinguish itself with an obsessive focus on usability and correctness. 
- Concurrency is complicated; we try to make it easy to get things right.
- Trio was built from the ground up to take advantage of the latest Python features
- Inspiration from [many sources](https://github.com/python-trio/trio/wiki/Reading-list), in particular Dave Beazley’s [Curio](https://curio.readthedocs.io/)
- Resulting design is radically simpler than older competitors like asyncio and Twisted, yet just as capable.
- We *do* encourage you do use it, but you should [read and subscribe to issue #1](https://github.com/python-trio/trio/issues/1) to get warning and a chance to give feedback about any compatibility-breaking changes.
- Excellent scalability: trio can run 10,000+ tasks simultaneously without breaking a sweat, so long as their total CPU demands don’t exceed what a single core can provide.
- Supports Python 3.5+ and PyPy
- Uses

```
    trio.run(async_method, 3)
    trio.sleep(1.5) # Sleep, non-blocking
    
    async with trio.open_nursery() as nursery:
        print("parent: spawning child...")
        nursery.start_soon(child_func1)
        print("parent: spawning child...")
        nursery.start_soon(child_func2)
        print("parent: waiting for children to finish...")
        # -- we exit the nursery block here --
    print("parent: child_func1 and child_func2 done!")
```

- trio provides a [rich set of tools for inspecting and debugging your programs](https://trio.readthedocs.io/en/latest/reference-hazmat.html#instrumentation).
- Consider [trio-asyncio](https://github.com/python-trio/trio-asyncio) for compatibility

**Brian #3:** [**black: The uncompromising Python code formatter**](https://github.com/ambv/black)

- An amusing take on code formatting. From the readme:
	- “*Black* is the uncompromising Python code formatter. By using it, you agree to cease control over minutiae of hand-formatting. In return, *Black* gives you speed, determinism, and freedom from `pycodestyle` nagging about formatting. You will save time and mental energy for more important matters.”
	- “Blackened code looks the same regardless of the project you're reading. Formatting becomes transparent after a while and you can focus on the content instead.”
	- “*Black* makes code review faster by producing the smallest diffs possible.”

- Datadog is a monitoring solution that provides deep visibility and tracks down issues quickly with distributed tracing for your Python apps.
- Within minutes, you'll be able to investigate bottlenecks in your code by exploring interactive flame graphs and rich dashboards.
- Visualize your Python performance today, get started with a free trial with Datadog and they'll send you a free T-shirt.

See for yourself, visit pythonbytes.fm/datadog. 

**Michael #4:** [**gain: Web crawling framework based on asyncio**](https://github.com/gaojiuli/gain)

- Web crawling framework for everyone. Written with asyncio, uvloop and aiohttp.
- Simple and mostly automated
	- Define class mapped to CSS selectors and data to save
	- Concurrently level
	- Start URL
	- Page templates to match URLs
	- Run

**Brian #5:** [**Generic Function in Python with Singledispatch**](https://rafiqul.rocks/generic-function-in-python-with-singledispatch/)

- “Imagine, you can write different implementations of a function of the same name in the same scope, depending on the types of arguments. Wouldn’t it be great? Of course, it would be. There is a term for this. It is called “Generic Function”. Python recently added support for generic function in Python 3.4 ([PEP 443](https://www.python.org/dev/peps/pep-0443/)). They did this to the `functools` module by adding `@singledispatch` decorator.”
- For people less familiar with “generic functions”. I think of this as providing similar functionality as C++’s function overloading.
- Allows you do things like this (full code example is in the article):

```
    from functools import singledispatch
    
    @singledispatch
    def fprint(data):
        "code for default functionality"
    
    @fprint.register(list)
    @fprint.register(set)
    @fprint.register(tuple)
    def _(data):
        "code for list, set, tuple"
    
    @fprint.register(dict)
    def _(data):
        "code for dict"
```

More complete code example: 

```
    from functools import singledispatch
    
    @singledispatch
    def fprint(data):
        print(f'({type(data).__name__}) {data}')
    
    @fprint.register(list)
    @fprint.register(set)
    @fprint.register(tuple)
    def _(data):
        formatted_header = f'{type(data).__name__} -> index : value'
        print(formatted_header)
        print('-' * len(formatted_header))
        for index, value in enumerate(data):
            print(f'{index} : ({type(value).__name__}) {value}')
    
    @fprint.register(dict)
    def _(data):
        formatted_header = f'{type(data).__name__} -> key : value'
        print(formatted_header)
        print('-' * len(formatted_header))
        for key, value in data.items():
            print(f'({type(key).__name__}) {key}: ({type(value).__name__}) {value}')
    
    # >>> fprint('hello')
    # (str) hello
    
    # >>> fprint(21)
    # (int) 21
    
    #...
    
    # >>> fprint({'name': 'John Doe', 'age': 32, 'location': 'New York'})
    # dict -> key : value
    # -------------------
    # (str) name: (str) John Doe
    # (str) age: (int) 32
    # (str) location: (str) New York
```

**Michael #6:** [**Unsync: Unsynchronizing async/await in Python 3.6**](http://asherman.io/projects/unsync.html)

- A rant about async/await in Python (by Alex Sherman)
- What’s wrong?
	- The two big friction points I’ve had are:
		- Difficult to “fire and forget” async calls (need to specifically run the event loop)
		- Can’t do blocking calls to asyncio.Future.result() (it throws an exception)
  - We need to acquire an even loop, do some weird call to execute the async function in that event loop, and then synchronously execute the event loop ourselves. 
- What can we do?
	- C# had this great idea of executing each Task (their version of a Future) first synchronously in the main thread until an await is hit, and then queueing it into an ambient thread pool to continue later possibly in a separate thread. 
	- Python did not take this approach and my hunch is that the Python maintainers didn’t want to add an ambient thread pool to their language (which makes sense). 
	- Alex, however, is not the Python maintainers and did add an ambient thread (singular). I stuffed all the boiler plate into a decorator and the result looks like this:

```
    @unsync
    async def unsync_async():
        await asyncio.sleep(0.1)
        return 'I like decorators'
    
    print(unsync_async().result())
```

- using @unsync on a regular function (not an async one) will cause it to be executed in a ThreadPoolExecutor. 
- To support CPU bound workloads, you can use @unsync(cpu_bound=True) to decorate functions which will be executed in a ProcessPoolExecutor

