# Python Bytes 39
**Mahmoud #1:** [**The New PyPI**](https://pypi.org/)

- Donald Stufft and his PyPA team have been hard at work replacing the old pypi.python.org
- The new site is now handling almost all the old functionality (excepting deprecated features, of course): [https://pypi.org/](https://pypi.org/)
- The new site has handled downloads (presently exceeding 1PB monthly bandwidth) for a while now, and uploads as of recently.
- A nice full-fledged, open-source Python application, eagerly awaiting your review and contribution: [https://github.com/pypa/warehouse/](https://github.com/pypa/warehouse/)
- More updates at: [https://mail.python.org/pipermail/distutils-sig/](https://mail.python.org/pipermail/distutils-sig/)

**Brian #2:** [**CircuitPython Snakes its Way onto Adafruit Hardware**](http://makezine.com/2017/08/11/circuitpython-snakes-way-adafruit-hardware/)

- [Adafruit announced CircuitPython in January](https://blog.adafruit.com/2017/01/09/welcome-to-the-adafruit-circuitpython-beta/)
  - “CircuitPython is based on the [open-source](https://github.com/micropython/micropython) [MicroPython](https://micropython.org/) which brings the popular Python language to microcontrollers. The goal of CircuitPython is to make hardware as simple and easy as possible.”
  - Already runs on [Metro M0 Express](https://www.adafruit.com/product/3505), [Feather M0 Express](https://www.adafruit.com/product/3403), and they are working on support for [Circuit Playground Express](https://www.adafruit.com/product/3333), and now Gemma M0
- New product is [Gemma M0](https://www.adafruit.com/product/3501):
  - [Announced](https://blog.adafruit.com/2017/07/27/new-product-adafruit-gemma-m0-miniature-wearable-electronic-platform/) at the end of July.
  - It’s about the size of a quarter and is considered a wearable computer.
  - “When you plug it in, it will show up as a very small disk drive with **main.py** on it. Edit **main.py** with your favorite text editor to build your project using Python, the most popular programming language. No installs, IDE or compiler needed, so you can use it on any computer, even ChromeBooks or computers you can’t install software on. When you’re done, unplug the Gemma M0 and your code will go with you."
  - They’re under $10. I gotta get one of these and play with it. (Anyone from Adafruit listening, want to send me one?)
  - Here's the intro video for it: [https://www.youtube.com/watch?v=nRE_cryQJ5c&feature=youtu.be](https://www.youtube.com/watch?v=nRE_cryQJ5c&feature=youtu.be)
- [Creating and sharing a CircuitPython Library](https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library) is a good introduction to the Python open source community, including:
  - Creating a library (package or module)
  - Sharing on GitHub
  - Sharing docs on ReadTheDocs
  - Testing with Travis CI
  - Releasing on GitHub

**Mahmoud #3:** **Dataclasses**

- Python has had classes for a long time, but maybe it’s time for some updated syntax and semantics, something higher level perhaps?
- dataclasses is an interesting case of Python’s core dev doing their own take on community innovation (Hynek’s attrs: https://attrs.org)
- Code, issues, and draft PEP at https://github.com/ericvsmith/dataclasses

**Brian #4:** [**Pandas in a Nutshell**](http://kanoki.org/2017/07/16/pandas-in-a-nutshell/)

- Jupyter Notebook style post. Tutorial by example with just a bit of extra text for explanation.
- Data structures:
  - Series – it’s a one dimensional array with indexes, it stores a single column or row of data in a Dataframe
  - Dataframe – it’s a tabular spreadsheet like structure representing rows each of which contains one or multiple columns
- Series: Custom indices, adding two series, naming series, …
- Dataframes: using .head() and .tail(), info(), adding columns, adding a column as a calculation of another column, deleting a column, creating a dataframe from a dictionary, reindexing, summing columns and rows, .describe() for simple statistics, corr() for correlations, dealing with missing values, dropping rows, selecting, sorting, multi-indexing, grouping, 

**Mahmoud** **#5:** **Static Typing**

- PyBay 2017, which ended a day before recording, featured a neat panel on static typing in Python.
- One member each from Google, Quora, PyCharm, Facebook, and University of California
- Three different static analysis tools (four, if you count PyLint)
- They’re all collaborating already, and open to much more, as we can see on this collection of the stdlib’s type defs: [https://github.com/python/typeshed](https://github.com/python/typeshed)
- A fair degree of consensus around static types being most useful for testable documentation, like doctests, but with more systemic implications
- Not intended to be an algebraic type system (like Haskell, etc.)

**Brian** **#6:**  [**Full Stack Python Explains ORMs**](https://www.fullstackpython.com/object-relational-mappers-orms.html)

- What are Object Relational Mappers?
  - “An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational databases tables into objects that are more commonly used in application code.”
- Why are they useful?
  - “ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.”
- Do you need to use them?
- Downsides to ORMs:
  - Impedance mismatch : “the way a developer uses objects is different from how data is stored and joined in relational tables”
  - Potential for reduced performance: code in the middle isn’t free
  - Shifting complexity from the database into the application code : people usually don’t use database stored procedures when working with ORMs.
- A handful of popular ones including Django ORM, SQLAlchemy, Peewee, Pony, and SQLObject. Mostly listed as pointing out that they are active projects, brief description, and links for more info.
- Matt also has a [SQLAlchemy page](https://www.fullstackpython.com/sqlalchemy.html) and a [peewee page](https://www.fullstackpython.com/peewee.html) for more info on them.

 
**Extra Mahmoud:**

- [hyperlink](https://github.com/python-hyper/hyperlink)
- [riot.im](https://riot.im) + [](https://riot.im)[(server code in Python)](https://github.com/matrix-org/synapse)

**Extra Brian:**

- [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) has a [Discussion Forum](https://forums.pragprog.com/forums/438). It’s something that I think all Pragmatic books have. Just this morning I answered a question about the difference between monkeypatch and mock and when you would use one over the other.





