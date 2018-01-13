# Python Bytes 61
Sponsored by DigitalOcean: **[http://do.co/python](http://do.co/python)**

**Brian #1:** [**PEP 412's dict key sharing for classes**](https://www.python.org/dev/peps/pep-0412/)

- "memory use is reduced by 10% to 20% for object-oriented programs with no significant change in memory use for other programs."
- To benefit from this, make sure all attributes used in life of class instances are initialized within `__init__()`. 
- Video from PyCon 2017
	- [Brandon Rhodes The Dictionary Even Mightier PyCon 2017](https://www.youtube.com/watch?v=66P5FMkWoVU)
	- Look at description at about 14 minutes on in the video
- Suggested by [Ned Letcher](https://twitter.com/nletcher/status/950184503116365825)

**Michael #2:** [**Python Hunter**](https://python-hunter.readthedocs.io/en/latest/cookbook.html#walkthrough)

- via Ivan Pejić
- Hunter is a flexible code tracing toolkit, not for measuring coverage, but for debugging, logging, inspection and other nefarious purposes. It has a Python API, terminal activation (see Environment variable activation). and supports tracing other processes (see Tracing processes).
- The default action is to just print the code being executed
- Based on cython

**Brian #3:** [**Ten Things I Wish I’d Known About bash**](https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/)

- I started with ksh on Solaris/HP-UX, used zsh for few years.
- Mostly now, I use bash, because it’s everywhere. Mac/Windows/Linux
- For windows: [**git for windows**](http://gitforwindows.org/)
	- Even if you don't need git, git for windows comes with fully integrated unix tools and bash and it just works as you expect.
	- you can launch windows applications
	- most of the frequent bash commands are there
	- If you really don’t want bash, consider [**cmder**](http://cmder.net/)

**Michael #4:** [**Snakefooding Python Code For Complexity Visualization**](http://www.grokcode.com/864/snakefooding-python-code-for-complexity-visualization/)

- [Snakefood](http://furius.ca/snakefood/) is a tool written by Martin Blais to create Python dependency graphs. 
- Combined with GraphViz, snakefood can create beautiful visualizations of Python codebases.
- Python Web Frameworks: The different development philosophies of Bottle, Django, Flask, and Pyramid are apparent by looking at their snakefood graphs.
- Bottle: A fast and simple micro framework for Python web applications.
- Django: A batteries-included web framework for perfectionists with deadlines.
- Flask: A microframework for Python.
- Pyramid: A small, fast, down-to-earth, open source Python web framework. It makes real-world web application development and deployment more fun, more predictable, and more productive.
- Also Queueing Implementations

**Brian #5:** [**On Being a Senior Engineer**](https://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/)

- 2012 article that's still very valid
- Obligatory Pithy Characteristics of Mature Engineers
- Mature engineers ...
	- seek out constructive criticism of their designs.
	- understand the non-technical areas of how they are perceived.
	- do not shy away from making estimates, and are always trying to get better at it.
	- have an innate sense of anticipation, even if they don’t know they do.
	- understand that not all of their projects are filled with rockstar-on-stage work.
	- lift the skills and expertise of those around them.
	- make their trade-offs explicit when making judgements and decisions.
	- don’t practice CYAE (“Cover Your Ass Engineering”)
	- are empathetic.
	- don’t make empty complaints.
	- are aware of cognitive biases:
		- Self-Serving Bias
		- Fundamental Attribution Error
		- Hindsight Bias
		- Outcome Bias
		- Planning Fallacy
- The Ten Commandments of Egoless Programming
	1. Understand and accept that you will make mistakes.
	2. You are not your code.
	3. No matter how much “karate” you know, someone else will always know more. 
	4. Don’t rewrite code without consultation. 
	5. Treat people who know less than you with respect, deference, and patience. 
	6. The only constant in the world is change. 
	7. The only true authority stems from knowledge, not from position. 
	8. Fight for what you believe, but gracefully accept defeat. 
	9. Don’t be “the coder in the corner.” 
	10. Critique code instead of people – be kind to the coder, not to the code.
- also:
	- Novices versus Experts 
	- Dirty secret: mature engineers know the importance of (sometimes irrational) feelings people have. (gasp!)
	- “It is amazing what you can accomplish if you do not care who gets credit.”

**Michael #6: Python UI frameworks**

- TkInter ([tutorial](https://www.tutorialspoint.com/python/python_gui_programming.htm)) - not amazing, not at all ([example](https://i.stack.imgur.com/Qdbsi.png)).
- [PySide](https://github.com/pyside) and Qt - hard to install, weird licensing and versioning, but has a nice designer
- Kivy and PyGame/PyOpenGL - game / simulation like
- [wxPython](https://www.wxpython.org/) seems not bad actually
	- [example](https://www.blog.pythonlibrary.org/wp-content/uploads/2011/07/events_in_style.png)
	- [widgets](https://wxwidgets.org/)
	- [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder) - a RAD tool for wxWidgets GUI design
	- [wxGlade](http://wxglade.sourceforge.net/) is a GUI designer
- What else? A few platform specific examples
- The problem: was discussed last week
- Some more Electron.JS like solutions
- https://github.com/ChrisKnott/Eel
	- Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with full access to Python capabilities and libraries.
	- It hosts a local webserver, then lets you annotate functions in Python so that they can be called from Javascript, and vice versa.
- [CEFPython](https://github.com/cztomczak/cefpython) - Chrome browser control, a HTML 5 based Python GUI framework.
