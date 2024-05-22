# Python Bytes 70
Sponsored by DigitalOcean: [**do.co/python**](https://do.co/python)

**Brian #1:** [**Online CookieCutter Generator**](https://generator.kpavlovsky.pro/)

- “Get a ZIP-archive with project by filling out the form.”
- By [@kpavlovsky_pro](https://twitter.com/kpavlovsky_pro) Konstantin Pavlovsky

**Michael #2:** [**cutelog – GUI for Python's logging module**](https://github.com/busimus/cutelog)

- This is a graphical log viewer for Python's standard logging module. 
- Features
	- Allows any number of simultaneous connections
	- Fully customizable look of log levels and columns
	- Filtering based on level and name of the logger, as well as filtering by searching
	- Search through all records or only through filtered ones
	- View exception tracebacks or messages in a separate window
	- Dark theme (with its own set of colors for levels)
	- Pop tabs out of the window, merge records of multiple tabs into one
- Based on PyQt5 speaking of GUIs

**Brian #3:** [**wagtail 2.0**](https://wagtail.io/blog/wagtail-2/)

- “Wagtail is a content management system built on Django. It’s focused on user experience, and offers precise control for designers and developers.”
- [The Zen of Wagtail](http://docs.wagtail.io/en/v2.0/getting_started/the_zen_of_wagtail.html) - nice philosophy of the project page to let you know if this kind of thing is right for you and your project.
- In 2.0
  - a new text editor
  - Django 2 support 
  - better scheduled publishing
  - …
- [wagtail docs](http://docs.wagtail.io/en/v2.0/getting_started/index.html)
- [gallery of sites made with wagtail](https://madewithwagtail.org/)

**Michael #4:** [**peewee 3.0 is out**](http://charlesleifer.com/blog/peewee-3-0-released/)

- Peewee is a simple and small ORM. It has few (but expressive) concepts, making it easy to learn and intuitive to use.
	- A small, expressive ORM
	- Written in python with support for versions 2.7+ and 3.4+ (developed with 3.6)
	- Built-in support for SQLite, MySQL and Postgresql.
	- Numerous extensions available (postgres hstore/json/arrays, sqlite full-text-search, schema migrations, and much more).
- Although this was pretty much a complete rewrite of the 2.x codebase, I have tried to maintain backwards-compatibility for the public APIs.
- Exciting because of its async support via **peewee-async**
	- **peewee-async** is a library providing asynchronous interface powered by [asyncio](https://docs.python.org/3/library/asyncio.html) for [peewee](https://github.com/coleifer/peewee) ORM.

```python
    database.set_allow_sync(False)
    
    async def handler():
        await objects.create(TestModel, text="Not bad. Watch this, I'm async!")
        all_objects = await objects.execute(TestModel.select())
        for obj in all_objects:
            print(obj.text)
```

**Brian #5:** [**Machine Learning Basics**](https://github.com/zotroneneis/machine_learning_basics)

- “Plain python implementations of basic machine learning algorithms”
- From the repo:
	- A repository of implementations of basic machine learning algorithms in plain Python (Python Version 3.6+). All algorithms are implemented from scratch without using additional machine learning libraries. The intention of these notebooks is to provide a basic understanding of the algorithms and their underlying structure, not to provide the most efficient implementations.
		- Linear Regression
		- Logistic Regression
		- Perceptron
		- k-nearest-neighbor
		- k-Means clustering
		- Simple neural network with one hidden layer
		- Multinomial Logistic Regression

**Michael #6:** [**Cerberus**](http://docs.python-cerberus.org/en/stable/)

- Cerberus provides powerful yet simple and lightweight data validation functionality out of the box
- designed to be easily extensible, allowing for custom validation
- Origin of the name: CERBERUS, n. The watch-dog of Hades, whose duty it was to guard the entrance;

```python
    schema = {'name': {'type': 'string'}, 'age': {'type': 'integer', 'min': 10}}
    v = Validator(schema)
    
    document = {'name': 'Little Joe', 'age': 5}
    v.validate(document)  # False
    v.errors  # {'age': ['min value is 10']}
```

**Follow up and other news**

**Michael:**

**#100DaysOfCode in Python course**: **[talkpython.fm/100days](https://talkpython.fm/100days)**
