# Python Bytes 57
Sponsored by DigitalOcean: [**http://digitalocean.com**](http://digitalocean.com)

**Brian #1:** [**Testing Python 3 and 2 simultaneously with retox**](https://medium.com/@anthonypjshaw/testing-python-3-and-2-simultaneously-with-retox-3e7c4b41453f)

- Anthony Shaw
- [tox](https://tox.readthedocs.io/en/latest/) allows you to run the same tests in multiple configurations.
  - For example, multiple Python interpreters (2 vs 3), or on different hardware, or using different options, etc.
  - tox can also tests your packaging code (on by default, but can be disabled)
- [detox](https://pypi.python.org/pypi/detox) allows multiple configurations to be tested in parallel with multiprocessing
  - typically running all tests 2-4 times faster
- [retox](https://github.com/tonybaloney/retox) does this with a GUI
  - also adds “watch” capability

**Michael #2:** [**Robo 3T / RoboMongo**](https://robomongo.org/)

- MongoDB GUI with embedded shell
- CLI interaction
- GUI when you want it
- No. 34 repository on GitHub

**Brian #3:** **regular expressions**

- [Regular Expressions Practical Guide](http://devarea.com/python-regular-expressions-practical-guide)
  - Python examples for some common expressions
  - How to use the built in re package for email addresses, URLs, phone numbers
  - substitution with `re.sub()`
  - splitting a string with `re.split()`
  - what some of the escape shortcuts mean, like `\w` for word, `\s` for whitespace, etc.
  - iterating through matches with `re.finditer()`
  - Using compiled expressions
- [Regular Expressions for Data Scientists](https://www.dataquest.io/blog/regular-expressions-data-scientists/)
  - another great intro, that also talks about:
    - `re.search()`
    - `re.findall()`
    - match groups

**Michael #4:** [**MongoEngine**](http://mongoengine.org/)

- MongoEngine is a Document-Object Mapper (think ORM, but for document databases) for working with MongoDB from Python.
- Map classes to MongoDB (think SQLAlchemy but for document databases)
- Adds features lacking from MongoDB
  - Schema
  - Required fields
  - Constraints
  - Relationships

**Brian #5:** [**Introducing PrettyPrinter for Python**](http://tommikaikkonen.github.io/introducing-prettyprinter-for-python/)

- a powerful, syntax-highlighting, and declarative pretty printer for Python 3.6
- goals
  - Implement an algorithm that tries very hard to produce pretty output, even if it takes a bit more work.
  - Implement a dead simple, declarative interface to writing your own pretty printers. Python developers rarely write `__repr__` methods because they're a pain; no one will definitely write pretty printing rules for user-defined types unless it's super simple.
  - Implement syntax-highlighting that doesn't break on invalid Python syntax.

**Michael #6:** [**Excel and Python**](https://excel.uservoice.com/forums/304921-excel-for-windows-desktop-application/suggestions/10549005-python-as-an-excel-scripting-language)

- Replace VBA
- Python in Excel as the main scripting language
- They need feedback (fill out their survey, upvote the issue)

Our news

Michael: 
* Webcast: **[https://www.wintellect.com/webinar/lets-build-something-mongodb-python/](https://www.wintellect.com/webinar/lets-build-something-mongodb-python/)**


