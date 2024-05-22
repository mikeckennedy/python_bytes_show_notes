# Python Bytes 327

Sponsored by [**Compiler Podcast from Red Hat**](https://pythonbytes.fm/compiler).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**pydantic-xml extension**](https://pydantic-xml.readthedocs.io/en/latest/)

- via Ilan
- Recall untangle. How about some pydantic in the mix?
- pydantic-xml is a pydantic extension providing model fields xml binding and xml serialization / deserialization. It is closely integrated with pydantic which means it supports most of its features.

**Brian #2:** [**How virtual environments work**](https://snarky.ca/how-virtual-environments-work)

- Brett Cannon
- This should be required reading for anyone learning Python.
    - Maybe right after “Hello World” and right before “My first pytest test”, approximately.
- Some history of environments
    - Back in the day, there was global and your directory.
- How environments work
    - structure: bin, include, and lib
    - pyvenv.cfg configuration file 
- How Python uses virtual environments
- What activation does, and that it’s **optional.**
    - Yes, activation is optional. 
- A new project called microvenv that helps VS Code.
    - Mostly to fix the “Debian doesn’t ship python3 with venv” problem.
    - It doesn’t include script activation stuff
    - It’s super small, less than 100 lines of code, in one file.

**Michael #3:** [**DbDeclare**](https://github.com/raaidarshad/dbdeclare)

- Declarative layer for your database.
- https://raaidarshad.github.io/dbdeclare/guide/controller/#example
- Sent in by creator raaid
- DbDeclare is a Python package that helps you create and manage entities in your database cluster, like databases, roles, access control, and (eventually) more. 
- It aims to fill the gap between SQLAlchemy (SQLA) and infrastructure as code (IaC).
- You can:
    - Declare desired state in Python
    - Avoid maintaining raw SQL
    - Tightly integrate your databases, roles, access control, and more with your tables
- Migrations like alembic coming too.

**Brian #4:** [**Testing multiple Python versions with nox and pyenv**](https://sethmlarson.dev/nox-pyenv-all-python-versions)

- Seth Michael Larson
- This is a cool “what to do first” with nox.
- Specifically, how to use it to run pytest against your project on multiple versions of Python.
- Example noxfile.py is super small

```
    import nox
    
    @nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "pypy3"])
    def test(session):
        session.install(".")
        session.install("-rdev-requirements.txt")
        session.run("pytest", "tests/")
```

- How to run everything, `nox` or `nox -s test`.
- How to run single sessions, `nox -s test-311` for just Python 3.11
- Also how to get this to work with pyenv.
    - `pyenv global 3.8 3.9 3.10 3.11 3.12-dev`
- This reminds me that I keep meaning to write a workflow comparison post about nox and tox.


**Extras** 

Michael:

- [GitHub makes 2FA mandatory next week for active developers](https://www.bleepingcomputer.com/news/security/github-makes-2fa-mandatory-next-week-for-active-developers/)
- New adventure bike [[image 1](https://python-bytes-static.nyc3.digitaloceanspaces.com/IMG_0205.jpeg), [image 2](https://python-bytes-static.nyc3.digitaloceanspaces.com/IMG_1002.jpeg)]. 
    - Who’s got good ideas for where to ride in the PNW? 
    - Wondering why I got it, here’s [a fun video](https://www.youtube.com/watch?v=U1HfsqjnEc0).

**Joke:** [Case of the Mondays](https://www.reddit.com/r/ProgrammerHumor/comments/10p4wo0/anybody_else_having_this_kind_of_colleague_way_to/)
