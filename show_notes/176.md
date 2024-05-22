# Python Bytes 176

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Topic #0: Quick chat about COVID 19**

**Brian #1:** [**What the heck is pyproject.toml?**](https://snarky.ca/what-the-heck-is-pyproject-toml/)

- Brett Cannon
- `pyproject.toml` 
	- PEP 517 and 518 define what this file looks like and how to use it to build projects
- We’re familiar with it being used for flit and poetry based projects.
- Not so much with setuptools, but it does work with setuptools.
- You can add configuration for non-build related activities, such as coverage, tox, even though those tools support their own config files.
- Black is gaining popularity, probably more so than the use of flit.
	- Black only uses pyproject.toml for configuration (what little config is available. But there is some.)
- So. Project adds use of black, ends up configuring with with pyproject.toml, but not specifying build steps, No builds are broken. :(
- Brett has the answers. 
- Add the following to pyproject.toml. Then go read the rest of Brett’s article. It’s good.

```
    [build-system]
    requires = ["setuptools >= 40.6.0", "wheel"]
    build-backend = "setuptools.build_meta"
```

**Michael #2:**  [**Awesome Python Bytes Awesome List**](https://github.com/JackMcKew/awesome-python-bytes)

- By Jack McKew
- Will be adding to this repo whenever I hear about awesome packages (in my opinion), PRs are welcome for anyone else though!
- Already has 5 PRs accepted
- Comes with graphics!!! Like all good presentations should.
- Some fun projects this made me recall:
	- Great Expectations - for validating, documenting, and profiling, your data
	- `pandas-vet` - a plugin for `flake8` that provides opinionated linting for pandas code.
	- GeoAlchemy - Using `SQLAlchemy` with Spatial Databases.
	- `vue.py` - Provides `Python` bindings for `Vue.js`. It uses `brython` to run `Python` in the browser.
- Remember we have speedy search for our content over at [**pythonbytes.fm/search**](https://pythonbytes.fm/search)

**Brian #3:** [**Publishing package distribution releases using GitHub Actions CI/CD workflows**](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

- PyPA
- You’ve moved to flit (or not) and started using GitHub actions to build and test whenever you push to GitHub. So awesome. 
- But now, there’s still a manual step to remember to publish to PyPI.
- And maybe we should be checking publish more often with the Test PyPI server.
- This article is a step by step walkthrough.
- It’s a bit dated, 3.7. So I’m trying to walk through all the steps with my [cards project](https://github.com/okken/cards) and it will be finished by the time this episode goes live.
- Stumbling blocks right now: 
	- I’ve left my email blank, no email for author or maintainer in pyproject.toml, because neither flit, nor pip require it. But PyPI still does. grrrr.
		- Trying to decide between: normal email, setting up a new email for it, using a me+pypi gmail alias, setting up a new email address just for pypi, etc.
	- test pypi fails due to “file already exists”, so, that’s always gonna be the case unless I bump the version, so gonna have to try to figure out a way around that.

**Michael #4:** [**Rich text for terminals**](https://github.com/willmcgugan/rich)

- Rich is a Python library for rich text and beautiful formatting in the terminal.
- Add colorful text (up to 16.7 million colors) with styles (bold, italic, underline etc.) to your script or application.
- Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, and tracebacks -- out of the box.
- Centered or justified text
- Tables, tables!
- Syntax highlighted code
- Markdown!
- Can replace `print()` and does pretty printing of dictionaries with color.
- Good Windows support for the [new Windows Terminal](https://www.youtube.com/watch?v=8gw0rXPMMPE&app=desktop)

**Brian #5:** [**psutil: Cross-platform lib for process and system monitoring in Python**](https://github.com/giampaolo/psutil)

- “psutil (process and system utilities) is a cross-platform library for retrieving information on **running processes** and **system utilization** (CPU, memory, disks, network, sensors) in Python. It is useful mainly for **system monitoring**, **profiling and limiting process resources** and **management of running processes**. It implements many functionalities offered by classic UNIX command line tools such as *ps, top, iotop, lsof, netstat, ifconfig, free* and others.”
- Useful for an incredible amount of information about the system you are running on:
	- cpu times, stats, load, number of cores
	- memory size and usage
	- disk partitions, usage
	- sensors, including battery
	- users
	- processes and process management
		- getting ids, names, etc. 
		- cpu, memory, connections, files, threads, etc per process
		- signaling processes, like suspend, resume, kill

**Michael #6:** [**How python implements super long integers?**](https://arpitbhayani.me/blogs/super-long-integers)

- by Arpit Bhayani
- In C, you worry about picking the right data type and qualifiers for your integers; at every step, you need to think if `int` would suffice or should you go for a `long` or even higher to a `long double`.
- In python, you need not worry about these "trivial" things because python supports integers of arbitrary size.
- `2 ** 20000` in C is INF where as in Python’s it’s fine, just at 6,021 digit result. But how!?!
- Integers are represented as:

```
    typedef struct {
        PyObject ob_base;
        Py_ssize_t ob_size; /* Number of items in variable part */
    } PyVarObject;
```

- Other types that has `PyObject_VAR_HEAD` are
    - `PyBytesObject`
    - `PyTupleObject`
    - `PyListObject`

```
    # Python's number:
    struct _longobject {
        PyObject ob_base;
        Py_ssize_t ob_size; /* Number of items in variable part */
        digit ob_digit[1];
    };
```

- A "digit" is base 230 hence if you convert 1152921504606846976 into base 230 you get 100
- Operations on super long integers
	- Addition: Integers are persisted "digit-wise", this means the addition is as simple as what we learned in the grade school 
	- Subtraction: Same
	- Multiplication: In order to keep things efficient implements the [Karatsuba algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm) that multiplies two n-digit numbers in O(nlog23) elementary steps.
- Optimization of commonly-used integers: Python preallocates small integers in a range of -5 to 256. This allocation happens during initialization

Extras:

Michael:

* We're coming to YouTube, probably. :)
* npm is joining GitHub

Joke:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5dea83bee3827f5c467b6898/5214f4ea7ea12031cb0c7e5035928612/d85e1dd68f88abf594905fa3fcc736de.jpg)
