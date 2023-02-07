# Python Bytes 322

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)
- Special guest: [**@calvinhp@fosstodon.org**](https://fosstodon.org/@calvinhp)

Join us on YouTube at [**pythonbytes.fm/stream/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Packaging Python Projects**](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

- Tutorial from PyPA
- This is a really good starting point to understand how to share Python code through packaging.
- Includes discussion of
    - directory layout
    - creating package files, LICENSE, pyproject.toml, README.md, tests and src dir
    - how to fill out `build-system` section of `pyproject.toml` 
        - using either hatchling, setuptools, flit, or pdm as backends
    - metadata
    - using `build` to generate wheels and tarballs
    - uploading with `twine`
- However
    - For small-ish pure Python projects, I still prefer [flit](https://flit.pypa.io/en/latest/)
        - `flit init` creates pyproject.toml and LICENSE
            - will probably still need to hand tweak pyproject.toml
        - `flit build` replaces `build`
        - `flit publish` replaces `twine`
    - The process [can be confusing, even for seasoned professionals.](https://hachyderm.io/@doughellmann/109807100255088176)
- Further discussion later in the show


**Michael #2:**  [**untangle xml**](https://github.com/stchris/untangle)

- Convert XML to Python objects
- Children can be accessed with `parent.child`, attributes with `element['attribute']`.
- Call the `parse()` method with a filename, an URL or an XML string.
- Given this XML:

```
    <?xml version="1.0"?>
    <root>
      <child name="child1"/>
    </root>
```

Access the document:

```
    obj.root.child['name'] # u'child1'
```

- A little cleaner that [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) perhaps.

**Calvin** **#3:** [**Mypy 1.0 Released**](https://mypy-lang.blogspot.com/2023/02/mypy-10-released.html)

- Mypy is a static type checker for Python, basically a Python linter on steroids
- Started in 2012 and developed by a team at Dropbox lead by https://github.com/JukkaL
- What’s New?
    - New Release Numbering Scheme
        - not using symver
        - Significant backward incompatible changes will be announced in the blog post for the previous feature release
        - feature flags will allow users to upgrade and turn on the new behavior
    - Mypy 1.0 is 40% faster than 0.991 against the Dropbox internal codebase
        - 20 optimizations included in this release
    - Mypy now warns about errors used before definition or possibly undefined variables
        - for example if a variable is used outside of a block of code that may not execute
    - Mypy now supports the new `Self` type introduced in PEP 673 and Python 3.11
    - Support `ParamSpec` in Type Aliases
    - Also, `ParamSpec` and Generic `Self` types are no loner experimental
    - Lots of Miscellaneous New Features
    - Fixes to crashes
    - Support for compiling Python `match` statements introduced in Python 3.10


**Brian #4:** [**Thoughts on the Python packaging ecosystem**](https://pradyunsg.me/blog/2023/01/21/thoughts-on-python-packaging)

- Pradyun Gedam
- Some great background on the internal tension around packaging. 
- Brian’s note: in the meantime
    - people are struggling to share Python code
    - the “best practice” answer seems to shift regularly
    - this might be healthy to arrive at better tooling in the long term, but in the short term, it’s hurting us. 
- From the article: 
    - The Python packaging ecosystem *unintentionally* became the type of competitive space that it is today.
    - The community needs to make an explicit decision if it should continue operating under the model that led to status quo.
    - Pick from N different tools that do N different things is a good model.
    - Pick from N ~equivalent choices is a *really bad* user experience.
    - Picking a default doesn’t make other approaches illegal.
    - Communication about the Python packaging ecosystem is fragmented, and we should improve that.
- Pradyun: “Many of the users who write Python code are *not* primarily full-time software engineers or “developers”.”
- from Thea: “The reason there are so many tools for managing Python dependencies is because Python is not a monoculture and different folks need different things.”
- opening up the build backend through pyproject.toml-based builds was good
- but the fracturing of multiple “workflow” tools seems bad.
- “I am certain that it is not possible to create a single “workflow” tool for Python software. What we have today, an ecosystem of tooling where each makes different design choices and technical trade-offs, is a part of why Python is as widespread as it is today. This flexibility and availability of choice is, however, both a blessing and a curse.”
- On building a default workflow tool around pip
    - interesting idea
- There’s tension between “we need a default workflow tool” and “unix philosophy: many focused tools that can work together”.
  

**Michael #5:** [**Top PyPI Packages**](https://hugovk.github.io/top-pypi-packages/)

- A monthly dump of the 5,000 most-downloaded packages from PyPI.
- Also, a [full copy of PyPI info](https://github.com/hugovk/top-pypi-packages) from the same person.

**Calvin** **#6:** [**SQLAlchemy 2.0 Released**](https://www.sqlalchemy.org/blog/2023/01/26/sqlalchemy-2.0.0-released/)

- #57 on the Top PyPI Packages 😸 
- Will be giving a SQLAlchemy tutorial at Python Web Conf
- What’s New?
    - Significant API change from 1.4
    - You’ll want to follow the [migration guide](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html) and see also the [what’s new in 2.0 guide](https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html)
    - Fully takes advantage of Python 3 features such as dataclasses, enums and inline annotations
    - Typing support in Core and ORM, but still should be considered **beta**
        - **all SQLAlchemy stubs packages must be uninstalled all SQLAlchemy stubs packages must be uninstalled** for typing to work
        - [Mypy Plugin](https://docs.sqlalchemy.org/en/20/orm/extensions/mypy.html) is considered deprecated now
    - Major speed increase in the all new fully ORM-integrated bulk `INSERT`s
        - sorry if you are on MySQL, they don’t support `INSERT RETURNING` yet
        - but MariaDB does support this
    -  All new bulk optimized schema reflection architecture
        - Currently enabled for PostgreSQL and Oracle
        - 250% perf increase for Postgres
        - 900% per increase for Oracle
    - Native extensions ported to Cython
        - C extensions have been replaced by Cython
        - Benchmarks as fast or sometimes faster than the previous C extensions
        - Removes some risk of memory or stability issues introduced by C
    - SQLAlchemy is now pep-517 enabled and has a `pyproject.toml`  at the root
        - means that local source building with `pip` can auto install the Cython dependancy

**Extras** 

Brian:

- Nothing to share yet, but I’m building a new alternative Python build backend.
    - which if course will be followed with a new workflow tool that follows “my workflow”.

Michael:

- “Create shortcut: New window” tip:
    - [In the dock/task bar](https://talk-python-static.nyc3.digitaloceanspaces.com/window-apps.png)
    - [Running as an app](https://talk-python-static.nyc3.digitaloceanspaces.com/proton-app.png)
- Speaking of Proton, started using [simplelogin.io](https://simplelogin.io)
- What’s all this banning chips about? [Great documentary](https://youtu.be/k_zz3239DA0)
- [Talk Python is hiring](https://fosstodon.org/@mkennedy/109803554690967616)!

Calvin: 

- 5th Annual [Python Web Conf 2023](https://2023.pythonwebconf.com)
