# Python Bytes 297

Sponsored by the [**IRL Podcast from Mozilla**](https://pythonbytes.fm/irl)

**Michael #1:** [**SQLCodeGen**](https://github.com/agronholm/sqlacodegen)

- via Josh Thurston
- This is a tool that reads the structure of an existing database and generates the appropriate SQLAlchemy model code, using the declarative style if possible.
- This tool was written as a replacement for [sqlautocode](http://code.google.com/p/sqlautocode/), which was suffering from several issues (including, but not limited to, incompatibility with Python 3 and the latest SQLAlchemy version).
- Features:
    - Supports SQLAlchemy 1.4.x
    - Produces declarative code that almost looks like it was hand written
    - Produces [PEP 8](http://www.python.org/dev/peps/pep-0008/) compliant code
    - Accurately determines relationships, including many-to-many, one-to-one
    - Automatically detects joined table inheritance
    - Excellent test coverage

**Brian #2:** **The death of setup.py*, long live pyproject.toml** 

- for Python-only projects
- [Juan Luis Cano Rodriguez tweet](https://twitter.com/juanluisback/status/1557734536586625025?s=20&t=OxIrS2c-blRHouZygbCjCQ)
- `pip install` `--``editable .` [now works with setuptools, as of version 64.0.0](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
- To be clear, `setup.cfg` also not required.
- So everything can be in `pyproject.toml`
- The * part: projects with non-Python bits may still need `setup.py`
- See also the newly updated tutorial by the [PyPA: Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
    - Now with absolutely no mention of `setup.py` or `setup.cfg`
    - It’s all `pyproject.toml`
- Commentary: 
    - For Python only projects, is setuptools a decent flit contender???
    - stay tuned


**Michael #4:** [**aiocache**](https://pypi.org/project/aiocache/)

- via [Owen Lamont](https://twitter.com/owenrlamont)
- In the same vein as async-cache you might also be interested in [aiocache](https://t.co/V1uGBlDzYS). 
- It has some cool functionality like an optional Redis backend for multi process caching.
- his library aims for simplicity over specialization. All caches contain the same minimum interface which consists on the following functions:
    - add: Only adds key/value if key does not exist.
    - get: Retrieve value identified by key.
    - set: Sets key/value.
    - multi_get: Retrieves multiple key/values.
    - multi_set: Sets multiple key/values.
    - exists: Returns True if key exists False otherwise.
    - increment: Increment the value stored in the given key.
    - delete: Deletes key and returns number of deleted items.
    - clear: Clears the items stored.
    - raw: Executes the specified command using the underlying client.

**Brian #5:** [**Hatch : a modern, extensible Python project manager.**](https://hatch.pypa.io/latest/)

- Another flit contender?
- While reading [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) tutorial update, I noticed some examples for `hatchling`, as an alternative to `setuptools`, `flit-core`, and `pdm`.
- Played with it some, but still have some exploring to do.
- features
    - Standardized [build system](https://hatch.pypa.io/latest/build/#packaging-ecosystem) with reproducible builds by default
    - Robust [environment management](https://hatch.pypa.io/latest/environment/) with support for custom scripts
    - Easy [publishing](https://hatch.pypa.io/latest/publish/) to PyPI **or other sources**
        - includes `--repo` flag to be able to publish to alternative indices. 
        - Awesome for internal systems.
    - [Version management](https://hatch.pypa.io/latest/version/)
    - Configurable [project generation](https://hatch.pypa.io/latest/config/project-templates/) with sane defaults
    - Responsive [CLI](https://hatch.pypa.io/latest/cli/about/), ~2-3x faster than equivalent tools
        - This sounds great. I haven’t verified this
- Commentary:
    - Good to see more packaging tools and user workflow explorations around packaging.

**Extras** 

Michael:

- [**M1 Support for PyPy Announced**](https://www.pypy.org/posts/2022/07/m1-support-for-pypy.html) (via PyCoders)

**Joke:** [**I am the docs**](https://twitter.com/PR0GRAMMERHUM0R/status/1557109490775883778)

