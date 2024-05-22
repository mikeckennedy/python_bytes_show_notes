# Python Bytes 127
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**inline_python (for rust)**](https://docs.rs/inline-python/0.2.0/inline_python/)

- “I just made a Frankenstein's monster: Python code embedded directly in rustlang code. Should I kill it before it escapes the lab?” - [Mara Bos](https://twitter.com/m_ou_se/status/1118234121745174536)
- Writing some rust, and need a little Python?
- Maybe want to pop open a matplotlib window?
- This may be just the thing you need.
- see also:
    - [https://pypi.org/project/bash/](https://pypi.org/project/bash/)    

**Kenneth #2**: **Requests3: Under Way!**

- Requests 2.x that you know and love is going into CVE-only mode (which it has been for a long time).
- Requests III is a new project which will bring async/await keywords to Requests.
- installable as `requests3`.
- Type-Annotations
- Python 3.6+

**Michael #3: 🔥 [Pyflame**](https://github.com/uber/pyflame): *A Ptracing Profiler For Python*

- Pyflame is a high performance profiling tool that generates [flame graphs](http://www.brendangregg.com/flamegraphs.html) for Python.
- Pyflame is implemented in C++, and uses the Linux [ptrace(2)](http://man7.org/linux/man-pages/man2/ptrace.2.html) system call to collect profiling information.
- It can take snapshots of the Python call stack without explicit instrumentation
- Capable of profiling embedded Python interpreters like [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/). 
- Fully supports profiling multi-threaded Python programs.
- Why use it?
	- Pyflame usually introduces significantly less overhead than the builtin `profile` (or `cProfile`) modules, and emits richer profiling data. 
	- The profiling overhead is low enough that you can use it to profile live processes in production.

**Brian #4:  [flit + src**](https://github.com/takluyver/flit/pull/260)

- Currently a WIP PR.
- `flit` is easy. 
	- Given a module or a source package.
	- `flit init` creates  `pyproject.toml` and `LICENSE` files.
	- commit those to git
	- `flit build` creates a wheel
	- `flit publish` (builds and) publishes to whatever you have in your `[.pypirc](https://docs.python.org/3/distutils/packageindex.html#the-pypirc-file)`
- Changes in this PR
	- The flit project already has 2 types of projects.
		- just a module, like foo.py
		- a package (directory with `__init__.py`), like `foo/__init__.py`
	- This would add a 3rd and 4th.
		- just a module, but in src, like `src/foo.py`
		- a package in src, like `src/foo/__init__.py`
- May be cracking open a can of worms, but I’m ok with that.


**Kenneth #5**: $ **pipx install pipenv**

**Michael #6:** [**cheat.sh**](https://github.com/chubin/cheat.sh)

- via Jon Bultmeyer
- Nothing to install, but works on the CLI
	- $ [**http cht.sh/python/sort+list**](http://http cht.sh/python/sort+list)
	- $ [**http cht.sh/python/connect+to+database**](http://http cht.sh/python/connect+to+database)
- Has a CLI client too with a proper shell
- Get started with [**http cht.sh/python/:learn**](http://http cht.sh/python/:learn)
- Has a funky stealth mode too
- Editor integration VS Code & Vim
- *cheat.sh* uses selected community driven cheat sheet repositories and information sources, maintained by thousands of users, developers and authors all over the world

**Extras**

Brian:

- [vi is good for beginners](http://dougsheehan.com/ViGoodForBeginners.html) - fun read, for all you haters out there. 
	- But use vim, not vi.
	- Better yet, IdeaVim for PyCharm or VSCodeVim for VS Code.
- [nbstripout](https://github.com/kynan/nbstripout) - command line tool to strip output from Jupyter Notebook files.
- We covered [pyodide](https://github.com/iodide-project/pyodide/) on [episode 93](https://pythonbytes.fm/93), but here’s a cool article on it
	- [Pyodide: Bringing the scientific Python stack to the browser](https://hacks.mozilla.org/2019/04/pyodide-bringing-the-scientific-python-stack-to-the-browser/)

Michael:

- PyCon AU CFP
- LIGO Blackhole collision follow up: https://www.youtube.com/watch?v=BXID4teFfDc
	- via Dave Kirby and Matthew Feickert
- https://github.com/kylebebak/questionnaire like Bullet but for windows too
	- via Sander Teunissen

Kenneth (optional):

- PyColorado CFP
- PyOhio CFP
- PyRemote!

**Jokes**

Don’t know if I’ll do all of these, but I like them. 🙂 Brian and Kenneth, feel free to add yours if you have some!

MK: Ubuntu users are apt to get these jokes.
MK: How many programmers does it take to kill a cockroach? Two: one holds, the other installs Windows on it.
MK: A programmer had a problem. He thought to himself, 'I know, I'll solve it with threads!'. has Now problems. two he

(mildly offensive) KR: What’s the difference between a musician and a pizza? A pizza can feed a family of four.

(In collaboration with Jonatan Skogsfors)
Python used to be directed by the BDFL, Guido. 
Now it’s directed by a steering council, GUIDs[0:4].
