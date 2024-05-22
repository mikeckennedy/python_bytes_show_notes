# Python Bytes 239

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pytestbook.com)!

Special guest: [**Nick Muoh**](https://twitter.com/Spirix3)


**Brain #1:** [ormar : an async mini ORM for Python, with support for Postgres, MySQL, and SQLite.](https://github.com/collerek/ormar)

- suggested by John Hagen
- From John: “It's a really cool ORM that combines Pydantic models and SQL models into a single definition. What is great about this, is it can be used to reduce repetitive duplication between Models for an ORM and the Pydantic Models that FastAPI needs to describe serialization. … If you have very pure-data heavy abstractions where your input and outputs through the API are roughly equivalent to your database, this helps you avoid needing to duplicate tons of SQLAlchemy classes and Pydantic that look identical and now you need to keep them in sync (DRY issue).”

**Michael #2:** [**No module named**](https://twitter.com/garettmd/status/1405005338726834177)

- via [Garett Dunn](https://twitter.com/garettmd/status/1405005338726834177)
- Website: [**nomodulenamed.com**](https://nomodulenamed.com/)
- Get an error like `Python Error: No module named dateutil`, maybe you need `pip install python_dateutil` ([reference](https://nomodulenamed.com/m/dateutil))

**Nick #3:**  [**JupyterLite**](https://jupyterlite.readthedocs.io/en/latest/)

- [Jeremy Tuloup](https://github.com/jtpio)
- JupyterLite is a JupyterLab distribution that **runs entirely in the browser** built from the ground-up using JupyterLab components and extensions.
- Python kernel backed by [Pyodide](https://pyodide.org/) running in a Web Worker
- Kernels include
	- Python 3.8 (pyolite implementation)
	- Javascript
	- P5.js
- Data is written to in-browser storage
- Data doesn’t leave the browser unless you are using extensions or use browser’s `fetch` API

**Brian #4:** [**Lot of plots**](https://nbviewer.jupyter.org/github/dylanjcastillo/random/blob/main/cheatsheet_data_viz_python.ipynb)

- Dylan Castillo
- Side by side comparison of plots.
- with: pandas, matplotlib, seaborn, plotly.express
- plotting: line, grouped bars, stacked bars, area, pie/donut, histogram, scatter, and box
- Many plotting articles talk about cool stuff you can do with a particular library.
- This is nice in that they all can do these things, so you can
	- see the output of each and compare
	- see the code that goes into making each, and see what style of api you might like to work with


**Michael #5:** [**Monty, Mongo tinified. MongoDB implemented in Python**](https://github.com/davidlatwe/montydb)

- Monty, Mongo tinified. MongoDB implemented in Python
- Inspired by [TinyDB](https://github.com/msiemens/tinydb) and it's extension [TinyMongo](https://github.com/schapman1974/tinymongo)
- A pure Python-implemented database that looks and works like [MongoDB](https://www.mongodb.com/).
- 🦄 Available storage engines:
	- in-memory
	- flat-file
	- sqlite
	- lmdb (lightning memory-mapped db)
- [**Tools and utilities like mongodump**](https://github.com/davidlatwe/montydb#utilities).

**Nick #6:** [**Exhaustiveness Checking with Mypy**](https://hakibenita.com/python-mypy-exhaustive-checking)

- [Haki Benita](https://hakibenita.com/pages/about)
- **Exhaustiveness checking** is a common feature of type checkers where the type checker guarantees that the programmer has covered all cases.
- Using Mypy, you can be warned at compile time about missing cases that should be handled in your code.
- Works great when using Enums, Union Types, or Literals
- Mypy leverage a concept called “type narrowing” where the type of a variable becomes more and more confined based on the control flow of a program.
- Can be useful when using ModelChoices in Django.

**Extras**

**Michael**

- [**Plan2Scene**](https://3dlg-hcvc.github.io/plan2scene/)
- [**A new podcast interview about big picture Python on TCast**](https://open.spotify.com/episode/0ndeCY8nxsbcqRPCirAyMh)

**Brian**

- [Python Testing with pytest, 2nd edition](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) is in Beta 🎉 
	- eBook available during Beta, through Pragmatic
	- Paperback available after Beta, “wherever fine books are sold”

**Nick**

- Join us virtually at the Cleveland’s Python Meetup [CLEpy](https://www.clepy.org/)
- Registration for [PyOhio 2021](https://www.pyohio.org/2021/) is open and the national conference begins July 31 (We have cool T-Shirts)

**Joke** 

**Rootbeer float**

- A programmer walks into a bar...
- He orders 1.000000119 root beers.
- The bartender says, “ I’m gonna have to charge you extra, that’s a root beer float.”
- The programmer says, “Well in that case make it a double.”

**It Haunts Us**

![It haunts us | CommitStrip](https://www.commitstrip.com/wp-content/uploads/2021/06/Strip-Refractoring-du-code-650-finalenglish.jpg)


How much does a chimney cost? It's free, it's on the house.


