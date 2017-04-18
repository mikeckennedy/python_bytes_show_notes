**Sponsored by [ADVANCE DIGITAL](http://python.advance.net/)**. Find your rewarding Python job at [http://python.advance.net/](http://python.advance.net/)

**#1 Brian:** [**PYTHONPATH considered harmful**](https://orbifold.xyz/pythonpath.html)

- Don’t do it.
- You might not regret it today. But later you will.
- Mucks up distribution searches, etc.
  - “For one, most directories are poorly suited to be on the Python search path. Consider, for example, the root directory of a typical Python project: it contains `setup.py` -- and so, if it were added to the current search path, `import setup` would become possible. (This is one reason to have `src/` directories.) Often, directories added unwisely to the Python search path cause files to be imported from paths they do not expect to, and surprisingly conflict.”

**#2 Michael:** [keon/algorithms](https://github.com/keon/algorithms)

- Minimal examples of data structures and algorithms in Python
- Topics include
  - Array
    - circular_counter
    - flatten
    - garage
    - merge_intervals
  - graphs
    - clone_graph
    - find_path
    - traversal
  - trees
  - etc.

**#3 Brian:** **[Glyph on attrs](https://glyph.twistedmatrix.com/2016/08/attrs.html)**

- We talked about `attrs` in [episode 11](https://pythonbytes.fm/11), and pointed to the project and the docs.
- I came across good article introducing why you should use `attrs`, by glyph, from 2016.
- The one Python library everyone needs: [https://glyph.twistedmatrix.com/2016/08/attrs.html](https://glyph.twistedmatrix.com/2016/08/attrs.html)
- Discusses 
  - problems with using lists and tuples as data structures.
  - creating your own classes properly. 
  - possible problems with `namedtuple` (-ish. I still love `namedtuple`).

**Sponsored by [ADVANCE DIGITAL](http://python.advance.net/)**

- A small team of developers who work in an agile/devops environment– you will make an impact with your work quickly
- Are mostly a python shop, but there is an opportunity to introduce and run other technologies at scale
- Fund employee development and conference attendance
- Are located in beautiful Jersey City, one stop from Manhattan on the PATH
- Are one of the 10 largest news sites by traffic in the US
- Apply at [http://python.advance.net/](http://python.advance.net/)

**#4 Michael:** [**Curio for Python 3.5+ concurrency**](https://github.com/dabeaz/curio)

- Curio is a library for performing concurrent I/O and common system programming tasks such as launching subprocesses and farming work out to thread and process pools. 
- Curio is solely concerned with the execution of coroutines. A coroutine is a function defined using async def.
- It uses Python coroutines and the explicit `async`/`await` syntax introduced in Python 3.5. 
- Its programming model is based on cooperative multitasking and existing programming abstractions such as threads, sockets, files, subprocesses, locks, and queues. 
- All sorts of cool constructs: `AsyncThreads`, `UniversalQueues`, async file I/O, `Tasks`, and more.

**#5 Brian:** **Python Package src-ery**

- "Use the src, Luke"
- "To src, or not to src, that is the question"

Answering a listener question about Python packaging.
In episode 15: Digging into Python Packaging, we mentioned to articles about getting started with packaging. 
In the comments, Kristof Claes noted that these references were in conflict with a couple of other references:

  - pytest “Good Integration Practices”, [https://docs.pytest.org/en/latest/goodpractices.html](https://docs.pytest.org/en/latest/goodpractices.html)
  - ionel’s “Packaging a Python library”, [https://blog.ionelmc.ro/2014/05/25/python-packaging/](https://blog.ionelmc.ro/2014/05/25/python-packaging/)

Both of these strongly encourage the use of a “src” directory when setting up a package for distribution.
There seems to be good reasons to use “src”. Many of the reasons are around the idea that during testing, you should be testing an installed version of the code. I have no reason to disagree with Ionel’s arguments and the pytest documentation recommendation.

However:

  - The pypa doesn’t bring this up when discussing distribution: 
    - [https://packaging.python.org/distributing/](https://packaging.python.org/distributing/)
  - The pypa sample project doesn’t use “src”:
    - [https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)
  - Many popular packages don’t:
    - requests: [https://github.com/kennethreitz/requests](https://github.com/kennethreitz/requests)
    - pytest itself: [https://github.com/pytest-dev/pytest](https://github.com/pytest-dev/pytest)
    

Why not?

  - The pytest recommendation is subtle. It recommends using “src” if you need to include a dunder init file in the tests directory. Otherwise, the local code will be tested instead of the installed code, in part to test the installation and to test a library from the perspective of a user.
  - pytest also recommends against having a top level dunder init in the tests directory. And this is a stronger recommendation.
  - But Ionel’s points are not just around the use of pytest.
  - So this is still really an open question to the Python community.
    - If it’s great to use “src” instead of top level packages, why aren’t more projects doing this?
    - Why doesn’t the PyPA mention it?

**# 6 Michael:** [**Intel Pulls Funding from OpenStack Effort It Founded With Rackspace**](http://fortune.com/2017/04/14/intel-openstack-project-rackspace/)

- Intel and Rackspace were collaborating on a project called OpenStack Innovation Center
- Launched in July 2015. 
- A source close to the effort said initial funding was supposed to last through 2018, but Intel pulled it early.
- A Rackspace spokeswoman said “OSIC’s objective was to create the world’s largest OpenStack developer cloud and develop enterprise capabilities within OpenStack. It quickly accomplished the first goal, and has made great progress toward the second.”
- Some 30 Rackspace employees who had been working at the innovation center have been given two weeks to find new jobs at the San Antonio-based company.
- Story here is we all need to think about funding projects and diversification.

**Our news:**

**Michael**: 
Hurry up and register for EuroPython: [https://ep2017.europython.eu/en/](https://ep2017.europython.eu/en/) Earlybird sold out.

