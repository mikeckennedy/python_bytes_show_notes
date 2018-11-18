# Python Bytes 104
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Michael #0.1: Chapters and play at**

- Chapters are now in the mp3 file
- Play at button on the website (doesn’t work on iOS unless you click the play to start it)

**Michael #0.2: [Become a friend of the show](https://pythonbytes.fm/friends-of-the-show)**

- [https://pythonbytes.fm/friends-of-the-show](https://pythonbytes.fm/friends-of-the-show)
- Or just click “friends of the show” in the navbar

**Brian #1:** [**wily: A Python application for tracking, reporting on timing and complexity in tests and applications.**](https://github.com/tonybaloney/wily)

- Anthony Shaw (aka “Friend of the Show”, aka “Ant”)
- *(if listing 2 “aliases, do you just put one “aka” or one per alias?)*
- I should cover this on Test & Code for the content of the package. But it’s the actual packaging that I want to talk about today.
- Wily is a code base that can be used as an example of embracing `pyproject.toml` (pyproject.toml discussed on [PB 100](https://pythonbytes.fm/100) and [T&C 52](https://testandcode.com/52))
- A real nice clean project using newer packaging tools that also has some frequently used bells and whistles
- NO setup.py file
- wily’s pyproject.toml includes
	- flit packaging, metadata, scripts 
	- tox configuration
	- black configuration
- project also has 
	- testing done on TravisCI
	- rst based docs and readthedocs updates
	- code coverage
	- black pre-commit for wily
	- pre-commit hook for your project to run wily
	- CONTRIBUTING.md that includes code of conduct
	- HISTORY.md with a nice format
	- tests using pytest

**Michael #2:** [**Latest VS Code has Juypter support**](https://blogs.msdn.microsoft.com/pythonengineering/2018/11/08/python-in-visual-studio-code-october-2018-release/)

- In this release, closed a total of 49 issues, including:
	- Jupyter support: import notebooks and run code cells in a Python Interactive window
	- Use new virtual environments without having to restart Visual Studio Code
	- Code completions in the debug console window
	- Improved completions in language server, including recognition of namedtuple, and generic types
- The extension now contains new editor-centric interactive programming capabilities built on top of Jupyter.
- have Jupyter installed in your environment (e.g. set your environment to Anaconda) and type #%% into a Python file to define a Cell. You will notice a “Run Cell” code lens will appear above the #%% line:
- Cells in the Jupyter Notebook will be converted to cells in a Python file by adding #%% lines. You can run the cells to view the notebook output in Visual Studio code, including plots

**Brian #3:**  [**API Evolution the Right Way**](https://emptysqua.re/blog/api-evolution-the-right-way/)

- A. Jesse Jiryu Davis
- adding features
- removing features
- adding parameters
- changing behavior

**Michael #4:** [**PySimpleGUI now on Qt**](https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/PySimpleGUIQt)

- Project by Mike B
- Covered back on [https://pythonbytes.fm/episodes/show/90/a-django-async-roadmap](https://pythonbytes.fm/episodes/show/90/a-django-async-roadmap)
- Simple declarative UI “builder”
- Looking to take your Python code from the world of command lines and into the convenience of a GUI?
- Have a Raspberry Pi with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?
- Look no further, you've found your GUI package.
- Now supports Qt
- Modern Python only
- More frameworks likely coming

**Brian #5:** [**Comparison of the 7 governance PEPs**](https://discuss.python.org/t/comparison-of-the-7-governance-peps/392)

- Started by [Victor Stinner](https://twitter.com/VictorStinner)
- The different PEPs are compared by:
	- hierarchy
	- number of people involved
	- requirements for candidates to be considered for certain positions
	- elections: who votes, and how
	- term limits
	- no confidence vote
	- teams/experts
	- PEP process
	- core dev promotion and ejection
	- how governance will be updated
	- code of conduct
-  [PEP 8000](https://www.python.org/dev/peps/pep-8000/), **Python Language Governance Proposal Overview**:
	- [PEP 8010](https://www.python.org/dev/peps/pep-8010) - **The Technical Leader Governance Model**
	- continue status quo (ish)
	- [PEP 8011](https://www.python.org/dev/peps/pep-8011) - **Python Governance Model Lead by Trio of Pythonistas**
	- like status quo but with 3 co-leaders
	- [PEP 8012](https://www.python.org/dev/peps/pep-8012) - **The Community Governance Model**
	- no central authority
	- [PEP 8013](https://www.python.org/dev/peps/pep-8013) - **The External Governance Model**
	- non-core oversight
	- [PEP 8014](https://www.python.org/dev/peps/pep-8014) - **The Commons Governance Model**
	- core oversight
	- [PEP 8015](https://www.python.org/dev/peps/pep-8015) - **Organization of the Python community**
	- push most decision-making to teams
	- [PEP 8016](https://www.python.org/dev/peps/pep-8016) - **The Steering Council Model**
	- bootstrap iterating on governance


**Michael #6:** [**Shiboken**](http://doc.qt.io/qtforpython/shiboken2/) (from Qt for Python project)

- From PySide2 (AKA Qt for Python) project
- Generate Python bindings from arbitrary C/C++ code
- Has a Typesystem (based on XML) which allows modifying the obtained information to properly represent and manipulate the C++ classes into the Python World.
- Can remove and add methods to certain classes, and even modify the arguments of each function, which is really necessary when both C++ and Python collide and a decision needs to be made to properly handle the data structures or types.
- [Qt for Python: under the hood](http://blog.qt.io/blog/2018/05/24/qt-for-python-under-the-hood/)
- [Write your own Python bindings](http://blog.qt.io/blog/2018/05/31/write-python-bindings/)
- Other options include:
	- CFFI (example [dbader.org](https://dbader.org/blog/python-cffi))
	- Cython (example:  [via shamir.stav](https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3))

**Extras:** 

- Michael: [**Mission Python: Code a Space Adventure Game! book**](https://www.amazon.com/Mission-Python-Code-Space-Adventure-ebook/dp/B072STNXT8)
- Michael: [**PyCon tickets are on sale**](https://twitter.com/pycon/status/1062031566468190208)
- Michael: [**PyCascade tickets are on sale**](https://2019.pycascades.com/)
