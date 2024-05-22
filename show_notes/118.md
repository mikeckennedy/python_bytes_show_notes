# Python Bytes 118
Sponsored by [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1**: [**Frozen-Flask**](https://pythonhosted.org/Frozen-Flask/)

- “Frozen-Flask freezes a [Flask](http://flask.pocoo.org/) application into a set of static files. The result can be hosted without any server-side software other than a traditional web server.”
- 2012 tutorial, [**Dead easy yet powerful static website generator with Flask**](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
- Some of it is out of date, but it does point to the power of Frozen-Flask, as well as highlight a cool plugin, [Flask-FlatPages](https://pythonhosted.org/Flask-FlatPages/), which allows pages from markdown.

**Michael #2**: [**pipx**](https://github.com/pipxproject/pipx)

- by Chad Smith
- Last week we spoke about [pythonloc](https://github.com/cs01/pythonloc)
- Execute binaries from Python packages in isolated environments
- *"binary" to describe a CLI application that can be run directly from the command line*
- Features
	- Safely install packages to isolated virtual environments, while globally exposing their CLI applications so you can run them from anywhere
	- Easily list, upgrade, and uninstall packages that were installed with pipx
	- Run the latest version of a CLI application from a package in a temporary virtual environment, leaving your system untouched after it finishes
	- Run binaries from the `__pypackages__` directory per PEP 582 as companion tool to [pythonloc](https://github.com/cs01/pythonloc)
	- Runs with regular user permissions, never calling `sudo pip install ...` (you aren't doing that, are you? 😄).
- You can globally install a CLI application by running: `pipx install PACKAGE`
- "Just the “pipx upgrade-all” command is already a huge win over pipsi"
- Check out [How does this compare to pipsi?](https://github.com/pipxproject/pipx#how-does-this-compare-to-pipsi)

**Brian #3:** [**Data science is different now**](https://veekaybee.github.io/2019/02/13/data-science-is-different/)

- Vicki Boykis
- There’s lots of buzz around data science.
- This has resulted in loads of new data scientists looking for junior level positions.
	- Coming from boot camps, MOOCs, self taught, remote degrees, and other training.
- “.. now that data science has changed from a buzzword to something even larger companies outside of the Silicon Valley bubble hire for, positions have not only become more codified, but with more rigorous entry requirements that will prefer people with previous data science experience every time.”
- “ … the market can be very hard, and very discouraging for the flood of beginners.”
- Data science is a misleading job req
	- “The reality is that “data science” has never been as much about machine learning as it has about cleaning, shaping data, and moving it from place to place.”
- Advice:
  - Don’t get into data science (this amuses me).
	- “Don’t do what everyone else is doing, because it won’t differentiate you.”
		- “It’s much easier to come into a data science and tech career through the “back door”, i.e. starting out as a junior developer, or in DevOps, project management, and, perhaps most relevant, as a data analyst, information manager, or similar, than it is to apply point-blank for the same 5 positions that everyone else is applying to. It will take longer, but at the same time as you’re working towards that data science job, you’re learning critical IT skills that will be important to you your entire career.”
	- Learn the skills needed for data science today
		- Creating Python packages
		- Putting R in production
		- Optimizing Spark jobs so they run more efficiently
		- Version controlling data
		- Making models and data reproducible
		- Version controlling SQL
		- Building and maintaining clean data in data lakes
		- Tooling for time series forecasting at scale
		- Scaling sharing of Jupyter notebooks
		- Thinking about systems for clean data
		- Lots of JSON
- Data science is turning more and more into a mostly engineering field.
- Data scientists need to have “good generalist engineering skills with a data background.”

**Michael #4**: [**RustPython**](https://github.com/RustPython/RustPython)

- via [Fredrik Averpil](https://twitter.com/fredrikaverpil/status/1091782433987543043)
- A Python-3 (CPython >= 3.5.0) Interpreter written in Rust.
- Seems pretty active: Latest commit ac95b61 an hour ago…
- Goals
	- Full Python-3 environment entirely in Rust (not CPython bindings)
	- A clean implementation without compatibility hacks
- Contributing
	- To start contributing, there are a lot of things that need to be done.
	- Most tasks are listed in the issue tracker. Check issues labeled with good first issue if you wish to start coding.
- Rust does have direct WebAssembly support…

**Brian #5**: [**Jupyter Notebook: An Introduction**](https://realpython.com/jupyter-notebook-introduction/)

- Mike Driscoll on RealPython
- Not the “all the cool things you can do with it”, but the “really, how do I start” tutuorial.
	- I think it should have included a mention of installing it in a venv and how to use `%pip install`, so I’ll include those things in these notes.
- Installing with `pip install jupyter` . 
	- Also a note that Jupyter is included with the Anaconda distribution.
	- Note: Like everything else, I always install it in a virtual environment, if using `pip`, so the real installation instructions I recommend is:
		- `python3 -m venv venv` `--``prompt jupyter`
		- `source venv/bin/activate` OR `venv\scripts\activate.bat` if windows
		- `pip install jupyter`
		- `pip install <any other packages you want to use>`
		- `jupyter notebook`
		- That will launch a localhost web interface.
- Creating a new notebook within the web interface.
- Changing the “Untitled” name by clicking on the name. 
	- This was not obvious to me.
- Running cells, including the shift-enter keyboard shortcut.
- A run through the menu, stopping at non-obvious places
	- “File” has “Save and Checkpoint” which is super cool.
	- “Edit” has cell cut, copy, paste. But also has delete, split, merge, and cell movement.
	- “Cell” menu has lots of cool run options, like “Run all above” and “Run all below” and others.
- Not just Python, but you can have a terminal sessions and more from within Jupyter.
- A look at the “Running” tab.
- Quick overview of the markdown support for markdown cells
- Exporting notebooks using `jupyter nbconvert`


- Extra notes on installing packages from Jupyter:
	- To pip install from the notebook, do this: `%pip install numpy` in a code cell.

**Michael #6**: [**Python Developers Survey 2018 Results**](https://www.jetbrains.com/research/python-developers-survey-2018/)

- Python usage as a main language is up 5 percentage points from 79% in 2017 when Python Software Foundation conducted its previous survey.
- **What do you use Python for? (2018/2017)**
	- 59%/51% Data analysis
	- 56%/54% Web dev
	- 39%/32% ML
	- Web development is the only category with a large gap (56% vs. 36%) separating those using Python as their main language vs. as a supplementary language. For other types of development, the differences are much smaller.
- **What do you use Python for the most? (single answer)**
	- 29%/29% web dev
	- 17%/17% data analysis
	- 11%/8% ML
- **Like last year**:
	- 27% (Web development) ≈ 28% (Scientific development) 
		- Science = 17% + 11% for Data analysis + Machine learning
- **Python 3 vs Python 2**
	- 84% Python 3 vs 16% Python 2. The use of Python 3 continues to grow rapidly. According to the latest research in 2017, 75% were using Python 3 compared with 25% for Python 2.
- **Top 4 web frameworks** (majority to the first two):
	- Flask
	- Django
	- Tornado
	- Pyramid
- **Databases**
	- PostgreSQL
	- MySQL
	- SQLite
	- MongoDB
- ORMs
	- SQLAlchemy and Django ORM tied

**Extras**:

- “Mentored sprints for diverse beginners” at PyCon
	- “**A newcomer’s introduction to contributing to an open source project”**
	- https://us.pycon.org/2019/hatchery/mentoredsprints/
	- Call for applications for projects open Feb 8 to March 14
	- Call for contributors, participants in the sprint also open Feb 8 to March 14
	- “**If you are wondering if this event is for you: it definitely is and we would love to have you taking part in this sprint.”**
	- “This mentored sprint will take place on Saturday, May 4th, 2019 from 2:35pm to 6:30pm”

**Joke**:
via Florian
Q: If you have some pseudo code (say in sample.txt) how do you most easily convert it to Python?
A: Change the extension to .py 

Extra Joke: [**Python Song (with chapters!)**](https://www.youtube.com/watch?v=3UsKYsLSGpU)

