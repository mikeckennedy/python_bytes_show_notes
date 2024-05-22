# Python Bytes 54
Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1:** [**The PSF awarded $170,000 grant from Mozilla Open Source Program to improve sustainability of PyPI**](http://pyfound.blogspot.com/2017/11/the-psf-awarded-moss-grant-pypi.html?m=1)

- Situation
	- The Python Packaging Index (PyPI) is the principal repository of software packages for the Python programming language.
	- There are over 100 million Python packages are downloaded from PyPI every week.
	- The Python community depends on PyPI for the ongoing functioning of the entire Python ecosystem.
	- There are no paid staff at the PSF who work on PyPI, and there are only a handful of people who contribute regularly.
	- This leads to a situation where we have to depend on volunteers to be on-call for outages and respond to critical security vulnerabilities in core Python Infrastructure.
- Next steps
	- The first milestone for Warehouse is redirecting portions of the production pypi.python.org to Warehouse including traffic for the simple index and package downloads. At that milestone Warehouse will be the main entryway to Python packages for all but a small fraction of the interactions PyPI sees.
	- The bulk of the work will be bringing Warehouse to feature parity with the administrative capabilities users need from the Package Index. We'll keep you posted as we figure out when you can expect that to be true.


**Michael #2:** [**Dropbox releases PyAnnotate**](https://twitter.com/gvanrossum/status/930906528042827776)

- Mypy is an experimental optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing
- You can develop programs with dynamic typing and add static typing after your code has matured, or migrate existing Python code to static typing.
- [mypy](http://www.mypy-lang.org/) is great, but it only works after you have added type annotations to your codebase.
- To easy the pain of adding type annotations to existing code, we’ve developed a tool, [PyAnnotate](https://github.com/dropbox/pyannotate), that observes what types are actually used at runtime, and inserts annotations into your source code based on those observations. We’ve now open-sourced the tool.
- run your code with a special [profiling hook](https://docs.python.org/3.6/library/sys.html#sys.setprofile) enabled. 
- This observes all call arguments and return values and records the observed types in memory. At the end of a run the data is dumped to a file in JSON format. 
- A separate command-line utility can then read this JSON file and use it to add inline annotations to your source code.

**Brian #3:** [**pytest-annotate is now open-source!**](https://blog.kensho.com/pytest-annotate-is-now-open-source-5dd6f6d51d0f)

- Use pyannotate without a driver file:
- 
```
    pip install pytest-annotate
    
    # to run code while collecting types
    pytest --annotate-output=./annotate.json
    
    # to see what will change with type hint comments
    pyannotate --type-info ./annotate.json <path_to_code>
    
    # to modify code
    pyannotate -w --type-info ./annotate.json <path_to_code>
```


**Michael #4:** [**Run Python script as systemd service**](https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c)

- Great for making your own “services” on Linux
- Incredibly easy, just follow the gist linked above

**Brian #5:** **[pytest 3.3.0 released](https://docs.pytest.org/en/latest/changelog.html)**

  - [changelog](https://docs.pytest.org/en/latest/changelog.html) includes 12 new features
  - Most excited about:
    - Now pytest displays the total progress percentage while running tests. 
    - Now captures and displays output from the standard logging module.

**Michael #6:** [**Why `d = {}` is faster than `d = dict()`**](https://blog.bordum.dk/fast-empty-sequences-in-python.html) 

- It turns out that using `str()`, `list()`, `dict()` and `tuple()` for creating empty sequences isn't as fast as their shorthand counterparts (`''`, `[]`, `{}`, `()`).
- We can inspect what happens with the dis module…

**Extras**

- F1 eSports now more exciting than real F1: [https://arstechnica.com/cars/2017/11/formula-1-esports-now-more-exciting-than-the-real-thing-and-thats-a-problem/](https://arstechnica.com/cars/2017/11/formula-1-esports-now-more-exciting-than-the-real-thing-and-thats-a-problem/)

