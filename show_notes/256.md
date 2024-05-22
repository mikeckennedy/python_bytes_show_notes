# Python Bytes 256


Sponsored by **Shortcut - Get started at** [**shortcut.com/pythonbytes**](http://shortcut.com/pythonbytes)

Special guest: **The Anthony Shaw**

**Michael #0: It’s episode 2^8 (nearly 5 years of podcasting)**

**Brian #1:** [**Where does all the effort go?**](https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/)[**:**](https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/) [**Looking at Python core developer activity**](https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/)
- Łukasz Langa
- A look into CPython repository history and PR data
- Also, nice example of datasette in action and lots of SQL queries. 
- The data, as well as the process, is open for anyone to look at.
- Cool that the process was listed in the article, including helper scripts used.
- Timeframe for data is since Feb 10, 2017, when source moved to GitHub, through Oct 9, 2021.
	- However, some queries in the article are tighter than that.
- Queries
    - Files involved in PRs since 1/1/20
        - top is ceval.c with 259 merged PRs
    - Contributors by number of merged PRs
        - lots of familiar names in the top 50, along with some bots
        - it’d be fun to talk with someone about the bots used to help the Python project
        - nice note: “Clearly, it pays to be a bot … or a release manager since this naturally causes you to make a lot of commits. But Victor Stinner and Serhiy Storchaka are neither of these things and still generate amazing amounts of activity. Kudos! In any case, this is no competition but it was still interesting to see who makes all these recent changes.”
    - Who contributed where?
        - Neat. There’s a self reported [Experts Index](https://devguide.python.org/experts/) in the very nice [Python Developer’s Guide](https://devguide.python.org/). But some libraries don’t have anyone listed. The data does though. 
        - Łukasz generated a [top-5 list](https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/assets/all_experts.txt) for each file. Contributing to some file and have a question. These folks may be able to help.
    - Averages for PR activity
        - core developer authoring and merging their own PR takes on average **~7** days (std dev **±41.96** days);
        - core developer authoring a PR which was merged by somebody else takes on average **20.12** days (std dev **±77.36** days);
        - community member-authored PRs get merged on average after **19.51** days (std dev **±81.74** days).
        - Interesting note on those std deviations: “Well, if we were a company selling code review services, this standard deviation value would be an alarmingly large result. But in our situation which is almost entirely volunteer-driven, the goal of my analysis is to just observe and record data. The large standard deviation reflects the large amount of variation but isn’t necessarily something to worry about. We could do better with more funding but fundamentally our biggest priority is keeping CPython stable. Certain care with integrating changes is required. Erring on the side of caution seems like a wise thing to do.”
- More questions to be asked, especially from the issue tracker
    - Which libraries require most maintenance?

**Michael #2:** [**Why you shouldn't invoke**](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html) `[**setup.py**](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)` [**directly**](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)

- By [Paul Ganssle](https://blog.ganssle.io/author/paul-ganssle.html) (from [**Talk Python #271: Unlock the mysteries of time, Python's datetime that is!**](https://talkpython.fm/episodes/show/271/unlock-the-mysteries-of-time-pythons-datetime-that-is))
- In response to conversation in [**Talk Python’s cibuildwheel episode**](https://talkpython.fm/episodes/show/338/using-cibuildwheel-to-manage-the-scikit-hep-packages)?
- For a long time, [setuptools](https://github.com/pypa/setuptools) and distutils were the only game in town when it came to creating Python packages
- You write a setup.py file that invokes the setup() method, you get a Makefile-like interface exposed by invoking python setup.py <command>
- The last few years **all direct invocations of setup.py are effectively deprecated** in favor of invocations via purpose-built and/or standards-based CLI tools like [pip](https://pip.pypa.io/en/stable/), [build](https://pypa-build.readthedocs.io/en/stable/) and [tox](https://tox.wiki/en/latest/).
- In Python 2.0, the distutils module was introduced as a standard way to convert Python source code into *nix distro packages
- One major problem with this approach, though, is that every Python package *must* use distutils and *only* distutils — there was no standard way for a package author to make it clear that you need *other* packages in order to build or test your package. => Setuptools
- Works, but sometimes you need requirements before the install (see cython example)
- A **build backend** is something like setuptools or [flit](https://flit.readthedocs.io/en/latest/), which is a library that knows how to take a source tree and turn it into a distributable artifact — a source distribution or a wheel.
- A **build frontend** is something like pip or [build](https://pypa-build.readthedocs.io/en/stable/), which is a program (usually a CLI tool) that orchestrates the build environment and invokes the build backend
- In this taxonomy, setuptools has historically been *both* a backend *and* a frontend - that said, setuptools is a *terrible* frontend. It does not implement PEP 517 or PEP 518's requirements for build frontends
- Why am I not seeing deprecation warnings?
- Use [**build package**](https://pypa-build.readthedocs.io/en/latest/).
- Also can be replaced by [tox](https://tox.wiki/en/latest/), [nox](https://nox.thea.codes/en/stable/index.html) or even a Makefile
- Probably should just check out [**the summary table**](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html#summary).

**Anthony #3:** [**OpenTelemetry is going stable soon**](https://opentelemetry.io)

- Cloud Native Computing Foundation project for cross-language event tracing, performance tracing, logging and sampling for distributed applications.
- Engineers from Microsoft, Amazon, Splunk, Google, Elastic, New Relic [and others](https://opentelemetry.io/vendors/) working on standards and specification.
- Formed through a merger of the OpenTracing and OpenCensus projects.
- Python SDK supports instrumentation of [lots of frameworks](https://opentelemetry.io/registry/), like Flask, Django, FastAPI (ASGI), and ORMs like SQLalchemy, or templating engines.
- All data can then be exported onto various platforms : NewRelic, Prometheus, Jaeger, DataDog, Azure Monitor, Google Cloud Monitoring.

If you want to get started and play around, checkout the rich console exporter I submitted recently.


**Brian #4:** [**Understanding all of Python, through its builtins**](https://sadh.life/post/builtins/)

- Tushar Sadhwani
- I really enjoyed the discussion before he actually got to the builtins.
    - LEGB rule defines the order of scopes in which variables are looked up in Python.
        - Local, Enclosing (nonlocal), Global, Builtin
    - Understanding LEGB is a good thing to do for Python beginners or advanced beginners. Takes a lot of the mystery away.
    - Also that all the builtins are in one 
- The rest is a quick scan through the entire list.
    - It’s not detailed everywhere, but pulls over scenic viewpoints at regular intervals to discuss interesting parts of `builtins`.
    - Grouped reasonably. Not alphabetical
- Constants: There’s exactly 5 constants: `True`, `False`, `None`, `Ellipsis`, and `NotImplemented`.
- globals and locals: Where everything is stored
- bytearray and memoryview: Better byte interfaces
- bin, hex, oct, ord, chr and ascii: Basic conversions
- …
- Well, it’s a really long article, so I suggest jumping around and reading a section or two, or three. Luckily there’s a nice TOC at the top.

**Michael #5:** [**FastAPI, Dask, and more Python goodies win best open source titles**](https://www.infoworld.com/article/3637038/the-best-open-source-software-of-2021.html#slide5)

- Things that stood out to me
- FastAPI
- Dask
- Windows Terminal
- minikube - Kubernetes cluster on your PC
- OBS Studio

**Anthony #6:** [Notes From the Meeting On Python GIL Removal Between Python Core and Sam Gross](https://lukasz.langa.pl/5d044f91-49c1-4170-aed1-62b6763e6ad0/)
- Following on from last week’s share on the “nogil” branch by Sam Gross, the Core Dev sprint included an interview.
- Targeted to 3.9 (alpha 3!), needs to at least be updated to 3.9.7. 

Nogil:

- Replaces pymalloc with mimalloc for thread safety
- Ties objects to the thread that created them witha. non-atomic local reference count within the owner thread
- Allows for (slower) reference counting from other threads.
- Immortalized some objects so that references never get inc/dec’ed like True, False, None, etc.
- Deferred reference counting
- Adjusts the GC to wait for all threads to pause at a safe point, doesn’t wait for I/O blocked threads and constructs a list of objects to deallocate using mimalloc
- Relocates the MRO to a thread local (instead of process-local) to avoid contention on ref counting
- Modifies the builtin collections to be thread-safe (lists, dictionaries, etc,) since they could be shared across threads.

IMHO, biggest thing to happen to Python in 5 years. 
Encouragingly, Sam was invited to be a Core Dev and Lukasz will mentor him!

**Extras**

Michael

- [**Python Developers Survey 2021**](https://twitter.com/ThePSF/status/1450168556801380357) is open
- [**More PyPI CLI updates**](https://twitter.com/HenrySchreiner3/status/1451210681827659781)
- [**bump2version**](https://github.com/c4urself/bump2version/) via Bahram Aghaei (youtube comment)
- Was there [**a bee stuck in Brian’s mic**](http://mellifera.cc/wp-content/uploads/2008/10/mic-insertion2.jpg) last time?


Brian

- [**PyCon US 2022 CFP is open until Dec 20**](https://us.pycon.org/2022/speaking/speaking/) 
- [**Python Testing with pytest, 2nd edition, Beta 7.0**](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/)
    - All chapters now there. (Final chapter was “Advanced Parametrization”)
    - It’s in technical review phase now. 
    - If reading, please skip ahead to the chapter you really care about and submit errata if you find anything confusing.

**Joke:**

![](https://paper-attachments.dropbox.com/s_72552CC2D0BCB4B5301750F3A35BC5D00B37A967D1C0E0905E8082299B754EC6_1635372932916_IMG_2873.JPG)
