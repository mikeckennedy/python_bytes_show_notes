# Python Bytes 293


Sponsored by [**Microsoft for Startups Founders Hub**](https://pythonbytes.fm/foundershub).

Special guest: [**Ashley Anderson**](https://twitter.com/aganders3)

**Ashley #1:** [**PSF security key giveaway for critical package maintainers**](https://pypi.org/security-key-giveaway/)

- Giving away 4000 2FA hardware keys
- Surely a team effort but I found it via @di_codes twitter (Dustin Ingram)
    - links to previous talks on PyPI/supply chain security
- Interesting idea for helping with supply-chain vulnerabilities
- At least one dev pulled a critical package in response
- Previously: <add some links to prior discussions>
- I don’t have any critical projects
- Armin Ronacher has an [**interesting take**](https://lucumr.pocoo.org/2022/7/9/congratulations/)

**Michael #2:** [**PyLeft-Pad**](https://old.reddit.com/r/Python/comments/vuh41q/pypi_moves_to_require_2fa_for_critical_projects/)

- via Dan Bader
- [**Markus Unterwaditzer**](https://twitter.com/untitaker) was maintaining  [atomicwrites](https://github.com/untitaker/python-atomicwrites/issues/61)
- [**More on how this relates to a project**](https://twitter.com/balloob/status/1545509863651811333?s=12&t=1zyCGa__JDTcBqaUXjEXGQ) (Home Assistant)
- I wonder if PyPI will become immutable once an item is published

**Brian #3:** [**FastAPI Filter**](https://twitter.com/arthur_rio/status/1542563206807183362?s=20&t=2HGsp6qnIA1lk2uYTuVQMghttps://fastapi-filter.netlify.app/)

- Suggested and created by  [Arthur Rio](https://twitter.com/arthur_rio/status/1542563206807183362?s=20&t=2HGsp6qnIA1lk2uYTuVQMg)
- “I loved using django-filter with DRF and wanted an equivalent for FastAPI.” - Arthur
- Add query string filters to your api endpoints and show them in the swagger UI.
- Supports SQLAlchemy and MongoEngine.
- Supports operators: gt, gte, in, isnull, it, lte, not/ne, not_in/nin

**Ashley #4:** 

- Tools for building Python extensions in Rust
    - [PyO3](https://github.com/PyO3)
        - pyo3 - Python/Rust FFI bindings
            - nice list of examples people might recognize in the PyO3 [README](https://github.com/PyO3/pyo3)
            - Pydantic V2 will use it for [pydantic-core](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/)
        - maturin - PEP 621 wheel builder (pyproject.toml)
            - pretty light weight, feels like flit for Rust or python/Rust
        - rust-numpy (+ndarray) for scientific computing
        - setuptools-rust for integrating with existing Python projects using setuptools
    - Rust project and community place high value on good tooling, relatively young language/community with a coherent story from early on
    - Rust macro system allows for really nice ergonomics (writing macros is very hard, using them is very easy)
    - The performance/safety/simplicity tradeoffs Python and Rust make are very different, but both really appeal to me
    - 

**Michael #5:** [**AutoRegEx**](https://twitter.com/wburn/status/1545820348821782528?s=12&t=1zyCGa__JDTcBqaUXjEXGQ)

- via Jason Washburn
- Enter an english phrase, it’ll try to generate a regex for you
- You can do the reverse too, explain a regex
- You must sign in and are limited to 100 queries / [some time frame]
- Related from Simon Willison: [Using GPT-3 to explain how code works](https://simonwillison.net/2022/Jul/9/gpt-3-explain-code/)

**Brian #6:** [**Anaconda Acquires PythonAnywhere**](https://www.anaconda.com/press/anaconda-acquires-pythonanywhere)

- Suggested by Filip Łajszczak
- See also [Anaconda Acquisition FAQs](https://blog.pythonanywhere.com/204/) from PythonAnywhere blog
- From announcement: “The acquisition comes on the heels of Anaconda’s release of [PyScript](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fwww.anaconda.com%2Fblog%2Fpyscript-python-in-the-browser&esheet=52757715&newsitemid=20220621006125&lan=en-US&anchor=PyScript&index=3&md5=dead5ee3af54b0512aa9bec13bfa3375), an open-source framework running Python applications within the HTML environment. The PythonAnywhere acquisition and the development of PyScript are central to Anaconda’s focus on democratizing Python and data science.”
- My take:
    - We don’t hear a lot about PA much, even their own blog has had 3 posts in 2022, including the acquisition announcement. 
    - Their [home page](https://www.pythonanywhere.com/) boasts “Python versions 2.7, 3.5, 3.6, 3.7 and 3.8”, although I think they support 3.9 as well, but not 3.10 yet, [seems like from the forum](https://www.pythonanywhere.com/forums/topic/30463/). Also, [no ASGI, so FastAPI won’t work, for example.](https://www.pythonanywhere.com/forums/topic/14918/)
    - Still, I think PA is a cool idea, and I’d like to see it stay around, and stay up to date. Hopefully this acquisition is the shot in the arm it needed.

**Extras** 

Michael:

- [**Python becomes the most sought after for employers hiring**](https://www.devjobsscanner.com/blog/top-8-most-demanded-languages-in-2022/) (by some metric)

Ashley:

- [**PEP691**](https://peps.python.org/pep-0691/) JSON Simple API for PyPI
- [**Rich Codex**](https://github.com/ewels/rich-codex) - automatic terminal “screenshots” 

**Joke:** [**Neta is a programmer**](https://www.neta.mk/archive)

