# Python Bytes 123
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**Deconstructing xkcd.com/1987/**](https://snarky.ca/deconstructing-xkcd-com-1987/)

- Brett Cannon
- Breakdown of the infamous [xkcd comic poking fun at the authors Python Environment on his computer](https://xkcd.com/1987/).
	- The interpreters listed
	- Homebrew description
	- python.org binaries
	- A discussion of pip, easy_install
	- The paths and the `$PATH` and `$PYTHONPATH`
- Actually quite an educational history lesson, and the abuse some people put their computers through.
- “So the next time someone decides to link to this comic as proof that Python has a problem, you can say that it's actually Randall's problem.”


**Michael #2:** [**Python package as a CLI option**](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/)

- Wanted to make [**this little app**](https://github.com/mikeckennedy/wakeup) available via a CLI as a dedicated command. Really tired of `python3 script.py` or `./script.py`
- Turns out, pip and Python already solve this problem, if you structure your package correctly
- Thanks to everyone on Twitter!
- The trick turns out to be to have entrypoints in your package

```
    entry_points = {
      "console_scripts": ['bootstrap = bootstrap.bootstrap:main']
    } ...
```

This should even register it with `pipx install package` ;)

**Brian #3**: [**pyright**](https://github.com/Microsoft/pyright/blob/master/README.md)

- a Microsoft static type checker for the Python language.
- “Pyright was created to address gaps in existing Python type checkers like [mypy](http://mypy-lang.org/).”
- 5x faster than mypy
- meant for large code bases
- written in TypeScript and runs within node.

**Michael #4:**  [**Refactoring Python Applications for Simplicity**](https://realpython.com/python-refactoring/)

- If you can write and maintain clean, simple Python code, then it’ll save you lots of time in the long term. You can spend less time testing, finding bugs, and making changes when your code is well laid out and simple to follow.
- **Is your code complex**?
- Metrics for Measuring Complexity
	- **Lines of Code**
	- **Cyclomatic complexity** is the measure of how many independent code paths there are through your application.
	- **Maintainability Index**
- **Refactoring**: The technique of changing an application (either the code or the architecture) so that it behaves the same way on the outside, but internally has improved.
- Nice overview of tooling (PyCharm, VS Code plugins, etc)
- Anti-patterns and ways out of them (best part of the article IMO)

**Brian #5:** [**FastAPI**](https://fastapi.tiangolo.com/)

- Thanks Colin Sullivan for suggesting the topic
- “*FastAPI framework, high performance, easy to learn, fast to code, ready for production”*
- “Sales pitch / key features:
	- **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
	- **Fast to code**: Increase the speed to develop features by about 200% to 300%. (estimated)
	- **Fewer bugs**: Reduce about 40% of human (developer) induced errors. (estimated)
	- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
	- **Easy**: Designed to be easy to use and learn. Less time reading docs.
	- **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
	- **Robust**: Get production-ready code. With automatic interactive documentation.
	- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification)(previously known as Swagger) and [JSON Schema](http://json-schema.org/).”
- uses:
	- [Starlette](https://www.starlette.io/) for the web parts.
	- [Pydantic](https://pydantic-docs.helpmanual.io/) for the data parts.
- document REST apis with both
	- Swagger
	- ReDoc
- looks like quite a fun contender in the “put together a REST API quickly” set of solutions out there.
- Just the front page demo is quite informative. There’s also a tutorial that seems like it might be a crash course in API best practices.

**Michael #6:**  [**Bleach: stepping down as maintainer**](https://bluesock.org/~willkg/blog/dev/bleach_stepping_down.html#)

- by Will Kahn-Greene
- [Bleach](https://bleach.readthedocs.io/) is a Python library for sanitizing and linkifying text from untrusted sources for safe usage in HTML.
- A retrospective on OSS project maintenance
- Picked up maintenance of the project because 
	- I was familiar with it
	- current maintainer really wanted to step down
	- Mozilla was using it on a bunch of sites
	- I felt an obligation to make sure it didn't drop on the floor and I knew I could do it.
- Never really *liked* working on Bleach
- He did a bunch of work on a project I don't really use, but felt obligated to make sure it didn't fall on the floor, that has a pain-in-the-ass problem domain. Did that for 3+ years.
- Is [he] getting paid to work on it? Not really.
- Does [he] like working on it? No.
- Seems like [he] shouldn't be working on it anymore.

**Extras**

**Brian**

- **[sleepsort](https://github.com/tdhopper/sleepsort)**

**Michael**: 

- [**Passbolt**](https://www.passbolt.com/)
- [**Python 3.7.3 is now available**](https://pythoninsider.blogspot.com/2019/03/python-373-is-now-available.html)
- [**stackroboflow**](https://stackroboflow.com) via Alexander Allori

**Joke**

