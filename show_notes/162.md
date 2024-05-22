# Python Bytes 162

**Sponsored by DataDog: pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)**

[Special guest: Aly](https://twitter.com/CaiusSivjus)

**Aly** **#1:** [**A**](https://www.youtube.com/watch?v=d9BAUBEyFgM)[**ndrew Godwin - Just Add Await: Retrofitting Async into Django — DjangoCon 2019**](https://www.youtube.com/watch?v=d9BAUBEyFgM)

- Andrew is leading the implementation of asynchronous support for Django
- Overview of Async Landscape
	- How synchronous and asynchronous code interact
	- Async functions are different than sync functions which makes it hard to design APIs
- Difficulties in adding Async support to Django
	- Django is a project that a lot of people are familiar with; it’s new async implementation also needs to feel familiar
- Plan was Implement async capabilities in three phases
- Phase 1: ASGI Support (Django 3.0)
	- This phase lays the groundwork for future changes
	- ORM is async-aware: using it from async code raises a `SynchronousOnlyOperation` exception
- Phase 2: Async Views, Async Handlers, and Async Middleware (Django 3.1)
	- Add async capabilities for the core part of the request path
	- There is a branch where things are mostly working, just need to fix a couple of tests
- Phase 3: Async ORM (Django 3.2 / 4.0)
	- Largest, most difficult and most unbounded part of the project
	- ORM queries can result in lots of database lookups; have to be careful here
- [Async Project Wiki](https://code.djangoproject.com/wiki/AsyncProject) - project status, find out how to contribute

**Brian** **#2:**  [**gamesbyexample**](https://pypi.org/project/gamesbyexample/)

- Al Sweigart
- “PythonStdioGames : A collection of games (with source code) to use for example programming lessons. Written in Python 3. Click on the src folder to view all of the programs.”
- I first learned programming by modifying games written by others and seeing what the different parts do when I change them. For me it was Lunar Lander on a TRS-80, and it took forever to type in the listing from the back of a magazine.
- But now, you can just clone a repo and play with existing files.
- Cool features:
	- They're short, with a limit of 256 lines of code. 
	- They fit into a single source code file and have no installer. 
	- They only use the Python standard library. 
	- They only use stdio text; `print()` and `input()` in Python. 
	- They're well commented. 
	- They use as few programming concepts as possible. *If classes, list comprehensions, recursion, aren't necessary for the program, then they are't used.*
	- **Elegant** and **efficient** code is worthless next to code that is **easy to understand** and **readable**. *These programs are for education, not production. Standard best practices, like not using global variables, can be ignored to make it easier to understand.*
	- They do input validation and are bug free. 
	- All functions have docstrings. 
- There’s also a todo list if people want to help out.

**Aly** **#3:** [**Bulwark**](https://github.com/zaxr/bulwark)

- Open-source library that allows users to property test pandas DataFrames
	- Goal is to make it easy for data analysts and data scientists to write tests
- Tests around data are different; they are not deterministic, they requires us to think about testing in a different way
	- With property tests, we can check an object has a certain property
- Property tests for DataFrames includes validating the shape of the `DataFrame`, checking that a column is within a certain range, verifying a `DataFrame` has no `NaN`s, etc
- Bulwark allows you to implement property tests as checks. Each check
	- Takes a `DataFrame` and optional arguments
	- The check will make an assertion about a `DataFrame` property
	- If the assertion passes, the check will return the original, unaltered DataFrame
	- If the check fails, an AssertionError is raised  and you have context around why it failed
- Bulwark also allows you to implement property checks as decorators
	- This is useful if you design data pipelines as functions
		- Each function take in input data, performs an action, returns output
	- Add decorators validate properties of input DataFrame to pipeline functions
- Lots of builtin [checks](https://bulwark.readthedocs.io/en/latest/bulwark.checks.html#module-bulwark.checks) and [decorators](https://bulwark.readthedocs.io/en/latest/bulwark.decorators.html); easy to add your own
- Slides with example usage and tips: [Property Testing with Pandas with Bulwark](https://docs.google.com/presentation/d/1hPJUIPpn2DZybj_m74j33DYt-6c7XUlQpD_Ga_CH_Jo/)

**Brian** **#4:** [**Poetry 1.0.0**](https://python-poetry.org/blog/announcing-poetry-1-0-0.html)

- Sebastien Eustace
- caution: not backwards compatible
- [full change log](https://python-poetry.org/history/)
- Highlights:
	- Poetry is getting serious.
	- more ways to manage environments
		- switch between python versions in a project with `poetry env use /path/to/python` 
		- or `poetry env use python3.7`
	- Imroved support for private indices (instead of just pypi)
		- can specify index per dependency
		- can specify a secondary index
		- can specify a non-pypi index as default, avoiding pypi
	- Env variable support to more easily work with poetry in a CI environment
	- Improved `add` command to allow for constraints, paths, directories, etc for a dependency
	- publishing allows api tokens
	- marker specifiers on dependencies.
    
**Aly** **#5:** [**Kubernetes for Full-Stack Developers**](https://www.digitalocean.com/community/curriculums/kubernetes-for-full-stack-developers)

- With the rise of containers, Kubenetes has become the defacto platform for running and coordinating containerized applications across multiple machines
- With the rise of containers, Kubenetes is the defacto platform for running and coordinating applications across multiple machines
- This guide follows steps new users would take when learning how to deploy applications to Kubernetes:
	- Learn Kubernetes core concepts
	- Build modern [12 Factor web applications](https://12factor.net/)
	- Get applications working inside of containers
	- Deploy applications to Kubernetes
	- Manage cluster operations
- New to containers? Check out my [Introduction to Docker talk](https://www.youtube.com/watch?v=oO8n3y23b6M)

**Brian** **#6:** [**testmon**](https://testmon.org/)[:](https://testmon.org/) [**selects tests affected by changed files and methods**](https://testmon.org/)

- On a previous episode (159) we mentioned pytest-picked and I incorrectly assumed it would run tests related to code that has changed, ‘cause it says “Run the tests related to the unstaged files or the current branch (according to Git)”.
- I was wrong, Michael was right. It runs the tests that are in modified test files.
- What I was thinking of is “testmon” which does what I was hoping for.
	- “pytest-testmon is a pytest plugin which selects and executes only tests you need to run. It does this by collecting dependencies between tests and all executed code (internally using Coverage.py) and comparing the dependencies against changes. testmon updates its database on each test execution, so it works independently of version control.”
- If you had tried testmon before, like me, be aware that there have been [significant changes in 1.0.0](https://testmon.org/new-in-testmon-100.html)
- Very cool to see continued effort on this project.

Extras:

- Aly:
	- Finding local Python User Groups
		- [PyCon.org Events Calendar](https://pycon.org/#calendar)
		- [Meetup.com](https://www.meetup.com/) search for Python
	- [PyTennessee 2019 on March 7 - 8](https://2020.pytennessee.org/). Tickets on sale now!
		- I will be giving a talk on the [Facade Design Pattern](https://2020.pytennessee.org/talks/everyday-design-patterns-facade-pattern)

- Brian:
	- Next episode is planned to be a live recording during the Jan 7 Python PDX West meetup.
	- There will also be 1-2 other talks.

Joke:

- From Tyler Matteson 
	- Two coroutines walk into a bar.
	- RuntimeError: 'bar' was never awaited.
- From Ben Sandofsky
	- Q: How many developers on a message board does it take to screw in a light bulb?
	- A: “Why are you trying to do that?”
