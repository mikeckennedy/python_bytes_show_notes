# Python Bytes 66
Sponsored by Rollbar: **[https://pythonbytes.fm/rollbar](https://pythonbytes.fm/rollbar)**

**Brian #1:** [**Object-Oriented Programming (OOP) in Python 3**](https://realpython.com/blog/python/python3-object-oriented-programming/)

- Real Python
- Nice modern introduction to classes, inheritance, and OOP.
- Classes, objects, attributes, instances, and inheritance.
- One gotcha not mentioned
	- The `__init__()` method of a base class is not called automatically by derived classes. If you override it, you need to call `super().__init__()`.
- Also, check out [attrs](http://www.attrs.org) for much of our OOP needs

**Michael #2:** [**ScriptedForms**](https://github.com/SimonBiggs/scriptedforms)

- Quickly create live-update GUIs for Python packages using Markdown and a few custom HTML elements. 
- Just write in markdown + variables / UI types
- Based on Jupyter

**Brian #3:** [**MongoDB to add multi-document transactions and ACID**](https://www.mongodb.com/blog/post/multi-document-transactions-in-mongodb)

- Mind blown. Didn’t see this coming
- “MongoDB 4.0 will add support for multi-document transactions, making it the only database to combine the speed, flexibility, and power of the document model with ACID data integrity guarantees. Through snapshot isolation, transactions provide a globally consistent view of data, and enforce all-or-nothing execution to maintain data integrity.”
- Due out this summer.

**Michael #4:** [**Python packaging pitfalls**](https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/)

- Just a short list of packaging blunders
	- Forgetting to clean the build dir
	- Forgetting to specify package data
	- Fine grained MANIFEST.in
	- Using package_data, or worse: fine grained package_data
	- Listing excludes/prunes before includes/grafts
	- Hardcoding packages list in setup.py
	- Hardcoding py_modules list in setup.py
	- Importing your package in setup.py
	- Importing unavailable tools in setup.py
	- Messing with the environment
	- Your tests do not test the installed code

**Brian #5:** [**Blogging principles**](https://jvns.ca/blog/2017/03/20/blogging-principles/)

- Julia Evans @b0rk
- Be honest about what you know
- Try not to write anything too long.
	- (My note: don’t shy away from long tutorials. Just don’t only do long stuff)
- Be positive.
- Write for the past you. 
- Stick with your own experience.
- It’s ok if not everyone likes it
  - Don’t try to keep one upping yourself.

**Michael #6:** [**pipenv is officially official**](https://github.com/pypa/pipenv)

- Pipenv — the officially recommended Python packaging tool from Python.org, free (as in freedom).
	- Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. 
	- Windows is a first–class citizen, in our world.
- Benefits?
	- It automatically creates and manages a virtualenv for your projects
	- adds/removes packages from your Pipfile as you install/uninstall packages
	- generates the ever–important Pipfile.lock, which is used to produce deterministic builds.

Follow up and other news

**Brian**

- Productive pytest with PyCharm webinar was recorded Thursday 22nd of Feb. 
- Will be available here: [**https://www.jetbrains.com/community/webinars/**](https://www.jetbrains.com/community/webinars/)

Michael:

- Embed Python in Unreal Engine 4 **[https://github.com/20tab/UnrealEnginePython](https://github.com/20tab/UnrealEnginePython)**
- Pandas documentation sprint **[https://python-sprints.github.io/pandas](https://python-sprints.github.io/pandas)**

