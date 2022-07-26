# Python Bytes 294


Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael #1:** [**Specialist: Python 3.11 perf highlighter**](https://github.com/brandtbucher/specialist)

- via Alex Waygood
- Visualize CPython 3.11's specializing, adaptive interpreter. 🔥
- [**PEP 659 – Specializing Adaptive Interpreter**](https://peps.python.org/pep-0659/)
- Specialist uses [fine-grained location](https://peps.python.org/pep-0657/) information to create visual representations of exactly *where* and *how* CPython 3.11's new [specializing, adaptive interpreter](https://peps.python.org/pep-0659/) optimizes your code.
- Dark, rich colors indicate code with many quickened instructions (and, therefore, high specialization potential), while light, pale colors indicate code with relatively few specialization opportunities.

**Brian #2:** [**tomli “A lil’ TOML parser”**](https://pypi.org/project/tomli/)

- Fully compatible with TOML spec 1.0.0
- This is the library that tomllib from Python 3.11 is based on, so great to use for Python 3.7-3.10 applications.
    - We discussed Python 3.11 and PEP 680 on [episode 273](https://pythonbytes.fm/episodes/show/273/getting-dirty-with-eq-self-other)
- Real Python has a great introduction for TOML in Python: [Python and TOML: New Best Friends](https://realpython.com/python-toml/)
    - TOML as a config format, key-value pairs, data types
    - using both tomli and tomllib
    - Loading TOML documents into Python
    - And like, writing, and updating toml docs programatically, which, although cool, I think the bulk of users can kinda skip over. But the the first 3 sections are an excellent reference.
    - Tables are cool, with `[name]` and `[name.subsection]` syntax, as well as arrays of tables with `[[name]]` syntax. I didn’t know how to do that before this article.

**Michael #3:** [**Pydantic V2 Plan**](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/)

- via [**Douglas Nichols**](https://twitter.com/TheNickleMan/status/1546455211350392832) and John Thagen
- A very detailed plan
- Goal to have all this done by the end of October, definitely by the end of the year.
- Samuel Colvin take a sabbatical to work on this (sound familiar?)
- Some details highlighted by John:
    - Moving the core logic to Rust to drastically increase performance (17x) [https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#performance](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#performance)
    - Strict mode (something I've wanted for a long time): [https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#strict-mode](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#strict-mode)
    - Cleaning up required vs nullable: [https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#required-vs-nullable-cleanup](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#required-vs-nullable-cleanup)
    - Naming cleanup: [https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#model-namespace-cleanup](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/#model-namespace-cleanup)
- This is a huge change, but overall it looks very promising for the community. It will likely require refactors by downstream users, so pinning pydantic using Poetry/pip-tools etc like always is a good idea.
- Many things have Pydantic at the core, so this matters, including:
    - FastAPI
    - Beanie
    - SQLModel
    - Pydastic
    - …

**Brian #4:** [**pikepdf**](https://github.com/pikepdf/pikepdf)

- a Python library for reading and writing PDF files
- Based on QPDF, which is written in C++.
- Features:
    - Supports password protected PDFs
    - Creates linearized ("fast web view") PDFs
    - Integrates with Jupyter and IPython notebooks for rapid development
- Some cool uses
    - copy pates from one PDF into another
    - split and merge PDFs
    - extract content
    - replace content, such as replacing images, without altering the rest of the file.
- Documentation mentions that if you only want to write PDFs, consider other libs, such as reportlab.


**Extras** 

Brian:

- pytest-check
    - I’ve set up 2fa for my account, so now I have no excuse for not looking into feature requests and merge requests for pytest-check, other than like all the other things I’m doing. 
    - I don’t have data for the top 3,500 for the last 6 months, but there is a list of the [top 5,000 for last 30 days](https://hugovk.github.io/top-pypi-packages/).
    - pytest-check is #1677 in the last 30 days.
    - pytest is #72 on the [same list](https://hugovk.github.io/top-pypi-packages/).
    - pydantic is #117
    - There are 57 pytest plugins that show up in the top 3,500 python packages. (packages that start with “pytest-”)
    - pytest-check is #20 of those. I guess it’s time to do another top plugins episode of Test & Code.


**Joke:** 

- [**Error, OK, I’ll check the logs**](https://mobile.twitter.com/NetaCodeGirl/status/1522193850323935233)
