# Python Bytes 282

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:** [**pyscript**](https://www.pyscript.net/)

- Python in the browser, from Anaconda. [repo here](https://github.com/pyscript/pyscript)
- Announced at PyConUS
- “During a keynote speech at PyCon US 2022, Anaconda’s CEO Peter Wang unveiled quite a surprising project — [PyScript](https://pyscript.net/). It is a JavaScript framework that allows users to create Python applications in the browser using a mix of Python and standard HTML. The project’s ultimate goal is to allow a much wider audience (for example, front-end developers) to benefit from the power of Python and its various libraries (statistical, ML/DL, etc.).” from a nice article on it, [**PyScript — unleash the power of Python in your browser**](https://towardsdatascience.com/pyscript-unleash-the-power-of-python-in-your-browser-6e0123c6dc3f)
- PyScript is built on [Pyodide](https://pyodide.org/en/stable/), which is a port of CPython based on WebAssembly.
- Demos are cool. 
- Note included in README: “This is an extremely experimental project, so expect things to break!”

**Michael #2:** [**Memray from Bloomberg**](https://github.com/bloomberg/memray)

- Memray is a memory profiler for Python. 
- It can track memory allocations in 
    - Python code
    - native extension modules
    - the Python interpreter itself
- Works both via CLI and focused app calls
- Memray can help with the following problems:
    - Analyze allocations in applications to help discover the cause of high memory usage.
    - Find memory leaks.
    - Find hotspots in code which cause a lot of allocations.
- Notable features:
    - 🕵️‍♀️ Traces every function call so it can accurately represent the call stack, unlike sampling profilers.
    - ℭ Also handles native calls in C/C++ libraries so the entire call stack is present in the results.
    - 🏎 Blazing fast! Profiling causes minimal slowdown in the application. Tracking native code is somewhat slower, but this can be enabled or disabled on demand.
    - 📈 It can generate various reports about the collected memory usage data, like flame graphs.
    - 🧵 Works with Python threads.
    - 👽🧵 Works with native-threads (e.g. C++ threads in native extensions)
- [**Has a live view in the terminal**](https://bloomberg.github.io/memray/run.html#id3).
- Linux only

**Brian #3:** [**pytest-parallel**](https://github.com/browsertron/pytest-parallel)

- I’ve often sped up tests that can be run in parallel by using -n from pytest-xdist.
- I was recommending this to someone on Twitter, and Bruno Oliviera suggested a couple of alternatives. One was pytest-parallel, so I gave it a try.
- pytest-xdist runs using multiprocessing
- pytest-parallel uses both multiprocessing and multithreading.
- This is especially useful for test suites containing threadsafe tests. That is, mostly, pure software tests.
- Lots of unit tests are like this. System tests are often not.
- Use `--workers` flag for multiple processors, `--workers auto` works great.
- Use `--tests-per-worker` for multi-threading. `--tesst-per-worker auto` let’s it pick.
- Very cool alternative to xdist.
- 

**Michael #****4****:** ****[**Pooch: A friend for data files**](https://www.fatiando.org/pooch/v1.6.0/index.html)

- via via Matthew Fieckert
- Just want to download a file without messing with `requests` and `urllib`?
- Who is it for? Scientists/researchers/developers looking to simply download a file.
- Pooch makes it easy to download a file (one function call). On top of that, it also comes with some bonus features:
    - Download and cache your data files locally (so it’s only downloaded once).
    - Make sure everyone running the code has the same version of the data files by verifying cryptographic hashes.
    - Multiple download protocols HTTP/FTP/SFTP and basic authentication.
    - Download from Digital Object Identifiers (DOIs) issued by repositories like figshare and Zenodo.
    - Built-in utilities to unzip/decompress files upon download
- `file_path = pooch.retrieve(url)`

**Extras** 

Michael:

- New course! [**Up and Running with Git - A Pragmatic, UI-based Introduction**](https://training.talkpython.fm/courses/up-and-running-with-git-a-pragmatic-ui-based-introduction).

**Joke:** 

- [**Don’t embarrass me in front of the wizards**](https://www.reddit.com/r/ProgrammerHumor/comments/uh8rsb/happens_to_the_best_of_us/)
- Michael’s [**crashing github**](https://twitter.com/mkennedy/status/1520181145261928448) is embarrassing him in front of the wizards!

