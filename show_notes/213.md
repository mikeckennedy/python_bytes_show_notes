# Python Bytes 213: Uh oh, Vulcans have infiltrated Flask

Catch the **video edition live stream** on YouTube:

<iframe width="560" height="315" src="https://www.youtube.com/embed/5noeLbjTz_o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: [**Anthony Shaw**](https://twitter.com/anthonypjshaw/)

Be part of the episode by subscribing and “smashing that bell” over at [**pythonbytes.fm/youtube**](http://pythonbytes.fm/youtube)

**Michael #1:** [**Django Ledger Project**](https://github.com/arrobalytics/django-ledger)

- by Miguel Sanda
- The mission is to provide free and open source accounting software that could easily replace commercial alternatives like QuickBooks.
- Django Ledger supports:
	- Chart of Accounts.
	- Financial Statements (Income Statement & Balance Sheets).
	- Automatic financial ratio & insight calculations.
	- Multi tenancy.
	- Hierarchical entity management.
	- Self-contained Ledgers, Journal Entries & Transactions.
	- Financial Activities Support (operational/financial/investing).
	- Basic OFX & QFX file import.
	- Bills & Invoices with optional *progressible* functionality.
	- Basic navigational templates.
	- Entity administration & entity manager support.
	- Bank Accounts.
- Not *quite* ready for production.
- **This project is actively looking for contributors. Any financial and/or accounting experience is a big plus.** If you have prior accounting experience and want to contribute, don't hesitate to contact.
- Browse the screenshots on the github repo.

**Brian #2:** [**Flask-Meld:**](https://github.com/mikeabrahamsen/Flask-Meld) **simple JavaScript interactive features without all of the JavaScript.**

- [Flask-Meld article with example](https://michaelabrahamsen.com/posts/flask-meld-ditch-javascript-frameworks-for-pure-python-joy/)
	- Michael Abrahamsen, [@MikeAbrahamsen](https://twitter.com/mikeabrahamsen)
	- [working example](https://meld.conveyor.dev/), [code for example](https://github.com/mikeabrahamsen/Flask-Meld-Example)
	- It seems really zippy. Definitely gonna try this.
- Similar project for Django: [django-unicorn](https://www.django-unicorn.com/)
	- Adam Hill, [@adamghill](https://twitter.com/adamghill)
	- [todo example](https://www.django-unicorn.com/documentation/examples/todo)


**Anthony #3:** [**Bitwise operators in Python**](https://realpython.com/python-bitwise-operators/) **(RealPython)**

- Article by **Bartosz Zaczyński**
- Particularly useful for the `enum.IntFlag` and `enum.Flag` classes in the stdlib since 3.7
```
    >>> class Color(Flag):
    ...     RED = auto()
    ...     BLUE = auto()
    ...     GREEN = auto()
    ...     WHITE = RED | BLUE | GREEN
```

**Michael #4:** [**Why should you use an ORM (Object Relational Mapper)?**](https://monadical.com/posts/why-use-orm.html#)

- You may have heard you should use an ORM, but why?
- To get a better understanding of how ORMs work, it’s helpful to work through the kind of problems they can solve.
- Data modeled as classes is great but has some shortcomings
	- How do you query, filter, sort it?
	- How do you store it? Classes live in memory only and pickling isn’t ideal for many reasons
	- There is also concurrency, transactional operations/atomiticity
- Enter the DB
	- But plain SQL is error prone (did you refactor that name? oops)
	- Plain SQL has code written within another language (SQL within Python, tools help but still)
	- Plain SQL has potential security issues (unless you use parameters)
- ORMs
	- ORMs are libraries that sit between the SQL database world and your object-oriented programming language world.
	- For all intents and purposes, they are an abstraction layer that allows, among other things, for the translation of Python to SQL.
- A cycle is formed
	- Define our models in the Python world as objects
	- the ORM layer translates those models to SQL statements with SQL types to create tables and columns. 
	- In our application, we instantiate objects from those models, which creates rows in the aforementioned tables. 
	- Finally, when we want those objects back, we use Python code to retrieve them, which triggers the ORM layer to create the necessary query to retrieve the rows from the database. Then, the ORM layer takes the resulting rows and maps them back to objects.
- And you get migrations

**Brian #5:** [**sqlite-utils: a Python library and CLI tool for building SQLite databases**](https://simonwillison.net/2019/Feb/25/sqlite-utils/)

- Simon Willison, [@simonw](https://twitter.com/simonw)
- “[sqlite-utils](https://github.com/simonw/sqlite-utils) is a combination Python library and command-line tool I’ve been building over the past six months which aims to make creating new SQLite databases as quick and easy as possible.”
- CLI for sqlite
	- Run queries and output JSON, CSV, or tables
	- analyzing tables
	- inserting data
	- creating, dropping, transforming tables
	- creating indexes
	- searching
	- …
- Python API for using as a library
	- way easier interaction with sqlite.
```
    import sqlite_utils
    db = sqlite_utils.Database("demo_database.db")
    # This line creates a "dogs" table if one does not already exist:
    db["dogs"].insert_all([
        {"id": 1, "age": 4, "name": "Cleo"},
        {"id": 2, "age": 2, "name": "Pancakes"}
    ], pk="id")
```
- [sqlite-utils docs](https://sqlite-utils.readthedocs.io/en/stable/)

**Anthony #6:** **Online conferences are not working for me. But this was a good talk,**

- “What the struct?!” by Zachary Anglin at the Pyjamas conference.
- Explains the struct libraries macro-language for converting binary data structures into Python native types (and vice versa) [https://docs.python.org/3/library/struct.html#format-characters](https://docs.python.org/3/library/struct.html#format-characters)
- Really nice if you want to programmatically edit/read binary structure (combining with the bitwise operators).
- If you’re getting into this topic. Save-game hacking is an interesting place to start. 
- I use SynalizeIT! /Synalysis as a binary data grammar explorer. It has some example save game formats [https://www.synalysis.net/formats.xml](https://www.synalysis.net/formats.xml)
- Its also great for hacking/CTF.


[https://youtu.be/QT_NAk_peHQ?t=7130](https://youtu.be/QT_NAk_peHQ?t=7130)

Extras

Brian: 

- Resurrecting [Python PDX West](https://www.meetup.com/Python-PDX-West) as a virtual lunchtime event.
- [January is planned for January 14, 2021](https://www.meetup.com/Python-PDX-West/events/275321561/) 

Michael:

- [**Did a FastAPI webcast**](https://blog.jetbrains.com/pycharm/2020/12/let-s-build-a-fast-modern-python-api-with-fastapi-additional-materials/) people can check out.
- M1 life is getting better and better

Anthony: 

- From February 1 I’ll be the new Python Open Source advocate at Microsoft, working with Nina Zacharenko
- Give us a quick update on Pyjion + .NET Core?

Jokes:

[https://twitter.com/lk012/status/1334390836172378113](https://twitter.com/lk012/status/1334390836172378113)
