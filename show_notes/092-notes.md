# Python Bytes 92

Sponsored by Digital Ocean -- [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Brian #1:** [**IEEE Survey Ranks Programming Languages**](https://www.eetimes.com/document.asp?doc_id=1333572)

- via Martin Rowe, [@measureentblue](https://twitter.com/measurementblue)
- Python on top. Was last year also, but this year it’s on top even for embedded.
- Some people dispute the numbers but I believe it.
- Projects contributing to the rise of Python in embedded:
	- [MicroPython](https://micropython.org/)
	- [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)
	- [micro:bit](https://microbit.org/code/)
	- [Mu](https://codewith.mu/en/tutorials/)

**Michael #2:** [**MyPyC**](https://mail.python.org/pipermail/python-dev/2018-August/154951.html)

- Thread on Python-Dev: Use of Cython
- *It'd be *really* nice to at least be able to write some of the C API tests directly in Cython rather than having to fiddle about with splitting the test between the regrtest parts that actually define the test case and the extension module parts that expose the interfaces that we want to test.*
- Later in the thread, Yury Selivanov dropped a bomb shell.
	- Speaking of which, Dropbox is working on a new compiler they call "mypyc".
	- **mypyc will compile type-annotated Python code to an optimized C.** 
	- Essentially, mypyc will be similar to Cython, but mypyc is a *subset of Python*, not a superset.
	- Interfacing with C libraries can be easily achieved with cffi. Being a strict subset of Python means that mypyc code will execute just fine in PyPy. They can even apply some optimizations to it eventually, as it has a strict and static type system.

**Brian #3:** [**Beyond Interactive: Notebook Innovation at Netflix**](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233)

- Netflix is doing some very cool things with Jupyter, and sharing much of it through open source projects.
- Netflix has growing their use of Jupyter notebooks for many data related roles:
	- business, data, & quantitative analysts
	- algorithm, analytics, & data engineers
	- data, machine learning, & research scientists
- All of these roles have common needs that are solved by Jupyter and related projects:
	- data exploration, preparation, validation, and productionalization (is that a word?)
- To help solve their use cases and make notebooks even easier to use for everyone at Netflix, they’ve started many open source projects that can be used by non-Netflix folks as well:
	- “[**nteract**](https://github.com/nteract) is a next-gen React-based UI for Jupyter notebooks.”
	- “[**Papermill**](https://github.com/nteract/papermill) is a library for parameterizing, executing, and analyzing Jupyter notebooks. “
	- “[**Commuter**](https://github.com/nteract/nteract/blob/master/applications/commuter/README.md) is a lightweight, vertically-scalable service for viewing and sharing notebooks.”
	- “[**Titus**](https://netflix.github.io/titus/) is a container management platform that provides scalable and reliable container execution and cloud-native integration with Amazon AWS. “
- There’s a follow-on post that discusses how Netflix is scheduling notebook execution: [Scheduling Notebooks](https://medium.com/@NetflixTechBlog/scheduling-notebooks-348e6c14cfd6)

**Michael #4:** [**How to create a Windows Service in Python**](https://www.thepythoncorner.com/2018/08/how-to-create-windows-service-in-hi.html)

-  We have spoken about how to [**run Python script as systemd service**](https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c)
- Here’s the Windows edition
	- Run Python code on boo
	- When logged out or logged in as another user
	- As a restricted or different account
- Based on [pywin32](https://github.com/mhammond/pywin32)  (very little documentation)
- Derive from a given base class then override the three main methods:
	- `def start(self)` : if you need to do something at the service initialization.
	- A good idea is to put here the initialization of the running condition
	- `def stop(self)` : if you need to do something just before the service is stopped.
	- A good idea is to put here the invalidation of the running condition
	- `def main(self)` : your actual run loop. Just create a loop based on your running condition

**Brian #5:** [**An Overview of Packaging for Python**](https://packaging.python.org/overview/)

- [Started from an essay by Mahmoud Hashemi](https://twitter.com/mhashemi/status/1029071335513677824), [@mhashemi](https://twitter.com/mhashemi)
- Now part of PyPA documentation
	- Different techniques and tools for different types of Python projects
	- modules
	- packages
		- source distributions
		- wheels
		- binary distributions
	- applications
		- this is the hairy part where a bullet point summary just won’t be enough. :)

**Michael #6:** [**PEP 505 -- None-aware operators**](https://www.python.org/dev/peps/pep-0505/)

- Several modern programming languages have so-called "null-coalescing" or "null- aware" operators, including C# and Swift. These operators provide syntactic sugar for common patterns involving null references.
- Why not Python?
- Two cases:
	- The "null-coalescing" operator: To replace inline conditionals such as this `value if value is not None else` `"``MISSING``"` can now be just `value ??` `"``MISSING``"`
	- The "null-aware member access" operator: Chain calls into a fluent interface without testing for None: `return user?.orders.first()?.name` would replace this

```
    if user is None:
        return None
    
    first_order = user.orders.first()
    if first_order is None:
        return None
    
    return first_order.name
```

Extras:

- PyCascades: [https://2019.pycascades.com/](https://2019.pycascades.com/)
- Test and Code episode with DHH: [http://testandcode.com/45
](http://testandcode.com/45)
