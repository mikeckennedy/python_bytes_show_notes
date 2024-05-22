# Python Bytes 89
Sponsored by Datadog -- [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**tenacity**](https://tenacity.readthedocs.io/en/latest/)

-  “Tenacity is a general-purpose retrying library to simplify the task of adding retry behavior to just about anything.”
- Example (Also, nice Trollhunters reference):

```python
    import random
    from tenacity import retry
    
    @retry
    def do_something_unreliable():
        if random.randint(0, 10) > 1:
            raise IOError("Broken sauce, everything is hosed!!!")
        else:
            return "Awesome sauce!"  # Toby says this frequently
    
    print(do_something_unreliable())
```

- Features:
	- Generic Decorator API
	- Specify stop condition (i.e. limit by number of attempts)
	- Specify wait condition (i.e. exponential backoff sleeping between attempts)
	- Customize retrying on Exceptions
	- Customize retrying on expected returned result
	- Retry on coroutines

**Michael #2:** [**Why is Python so slow?**](https://hackernoon.com/why-is-python-so-slow-e5074b6fe55b)

- Answer this question: *When Python completes a comparable application 2–10x slower than another language, why is it slow and can’t we make it faster?* 
- Here are the top theories:
	- “It’s the GIL (Global Interpreter Lock)”
	- “It’s because its interpreted and not compiled”
	- “It’s because its a dynamically typed language”
- **“It’s the GIL”**
	- Modern computers come with CPU’s that have multiple cores
	- For web apps, it might not matter (e.g. [https://training.talkpython.fm/](https://training.talkpython.fm/) has 16 worker processes, [https://talkpython.fm/](https://talkpython.fm/) has 8 workers)
- **“It’s because its an interpreted language”**
	- I hear this a lot and I find it a gross-simplification of the way CPython actually works.
	- JIT vs. NonJIT is interesting (startup time too)
- **“It’s because its a dynamically typed language”**
	- In a “Statically-Typed” language, you have to specify the type of a variable when it is declared. Those would include C, C++, Java, C#, Go.
	- In a dynamically-typed language, there are still the concept of types, but the type of a variable is dynamic.
	- Not having to declare the type isn’t what makes Python slow
	- It’s this design that makes it incredibly hard to optimize Python.
- **Conclusion**
	- Python is primarily slow because of its dynamic nature and versatility. It can be used as a tool for all sorts of problems, where more optimized and faster alternatives are probably available.

**Brian #3**: [**Keynoting with Mu**](https://madewith.mu/mu/users/2018/07/30/keynoting-mu.html)

-  David Beazley gave his [EuroPython talk/demo “Die Threads”](https://youtu.be/U66KuyD3T0M) using Mu.
- Article also notes that simple tools are great not just for learning, but for teaching, as the extra clutter of a full power editor doesn’t distract too much.

**Michael #4:** [**A multi-core Python HTTP server (much) faster than Go (spoiler: Cython)**](https://www.nexedi.com/NXD-Blog.Multicore.Python.HTTP.Server)

- Exploring  the question, “So, I’ve heard Python is slow… is it?”
- A multi-core Python HTTP server that is about 40% to 110% faster than Go can be built by relying on the Cython language and LWAN C library. 
- Just a proof of concept validates the possibility of high performance system programming in the Cython language. 
- Primarily interesting as a highlight of Cython
	- Cython is both an optimizing static compiler and a hybrid language. It mainly gives the ability to:
	- write Python code that can call back and forth from and to C/C++;
	- add static typing using C declarations to Python code in order to boost performance;
	- release the GIL in some code sections.
- Cython generates very efficient C code, which is then compiled into a module that Python can import. So it is an ideal language for wrapping external C libraries, and for developing C modules that speed up the execution of Python code.
- However, all experiments we are aware that rely on Cython for system programming fail short in at least two ways:
	- as soon as some Python code is invoked (as opposed to pure Cython `cdef` code), [performance degrades by one or two orders of magnitude](https://www.nexedi.com/NXD-Document.Blog.UVLoop.Python.Benchmark);
	- benchmarks are most of the time provided for single core execution only, which is somehow unfair considering Golang's ability to scale up on multiple cores.

**Brian #5**: [**PyCharm  2018.2 beefs up pytest support**](https://www.jetbrains.com/pycharm/whatsnew/#v2018-2-python)

- Honestly, I’m super excited about this release to help my team navigate to all of the fixtures I create on a regular basis.
- This is the release I’ve been waiting for.
- I can now fully utilize the power of pytest from PyCharm
- Here’s the few things that were missing that now work great:
	- Autocomplete fixtures from various sources
	- Quick documentation and navigation to fixtures
	- Renaming a fixture from either the definition or a usage
	- Support for pytest’s parametrize
- See also: [PyCharm 2018.2 and pytest Fixtures](https://blog.jetbrains.com/pycharm/2018/08/pycharm-2018-2-and-pytest-fixtures/)
- But if you really want to understand fixtures quickly, [read chapters 3 and 4 of the pytest book.](https://amzn.to/2KfB9Dz)

**Michael #6**: [**XAR for Facebook**](https://github.com/facebookincubator/xar)

- XAR lets you package many files into a single self-contained executable file. This makes it easy to distribute and install.
- A `.xar` file is a read-only file system image which, when mounted, looks like a regular directory to user-space programs. This requires a one-time installation of a driver for this file system ([SquashFS](https://en.wikipedia.org/wiki/SquashFS)).
- There are two primary use cases for XAR files. 
	- Simply collecting a number of files for automatic, atomic mounting somewhere on the filesystem. 
	- By making the XAR file executable and using the xarexec helper, a XAR becomes a self-contained package of executable code and its data. A popular example is Python application archives that include all Python source code files, as well as native shared libraries, configuration files, other data.
- Advantages of XAR for Python usage
	- SquashFS looks like regular files on disk to Python. This lets it use regular imports which are better supported by CPython.
	- SquashFS looks like regular files to your application, too. You don't need to use `pkg_resources` or other tricks to access data files in your package.
	- SquashFS with Zstandard compression saves disk space, also compared to a ZIP file.
	- SquashFS doesn't require unpacking of `.so` files to a temporary location like ZIP files do.
	- SquashFS is faster to start up than unpacking a ZIP file. You only need to mount the file system once. Subsequent calls to your application will reuse the existing mount.
	- SquashFS only decompresses the pages that are used by the application, and decompressed pages are cached in the page cache.
	- SquashFS is read-only so the integrity of your application is guaranteed compared to using virtualenvs or unpacking to a temporary directory.
- Performance is interesting too

Extras:

Brian:

- [**numpy 1.15.0**](https://github.com/numpy/numpy/releases/tag/v1.15.0) just released recently. Switched testing to pytest.

Michael:

- SciPy 2018 [**videos are out**](https://www.youtube.com/watch?v=y7zGnKzaKIw&index=1&list=PLYx7XA2nY5Gd-tNhm79CNMe_qvi35PgUR)
- PyOhio 2018 [**videos are out**](https://www.youtube.com/playlist?list=PL2k6bbM_wgjvY02EFUMhwHRyaSaEokT2B)
- [**Call for papers**](https://www.papercall.io/pyconca2018) at PyCon Canada in Toronto
- [**PyBay 2018**](https://pybay.com/) conference in a few weeks
- My latest course, [**Building data-driven web apps with Pyramid and SQLAlchemy**](https://training.talkpython.fm/courses/explore_pyramid/building-data-driven-web-applications-in-python-with-pyramid-sqlalchemy-and-bootstrap), is out!

