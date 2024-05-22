# Python Bytes 223


Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: [**Sebastián Ramírez**](https://twitter.com/tiangolo)

**Brian #1:** [**Python Developers Survey 2020 Results**](https://www.jetbrains.com/lp/python-developers-survey-2020/)

- Using Python for? 
	- Lots of reductions in percentages. 
	- Increases in Education, Desktop, Games, Mobile, and Other
- Python 3 vs 2
	- 94% Python3 vs 90% last year
	- Python 3.8 has 44% of Python 3 usage, 3.5 or lower down to 3%
- environment isolation
	- 54% virtualenv (I assume that includes venv)
	- 32% Docker 
	- 22% Conda
- Web frameworks
	- 46% Flask
	- 43% Django
	- 12% FastAPI
	- …
	- 2% Pyramid :(
	- …
- Unit testing 
	- 49% pytest
	- 28% unittest
	- 13% mock
- OS
	- 68% Linux, 48% Windows, 29% Mac, 2% BSD, 1% other
- CI: Gitlab, Jenkins, Travis, CircleCI … (Where’s GH Actions?)
- Editors: PyCharm, VS Code, Vim, …
- Lots of other great stuff in there

**Michael #2:** [**Django Ninja - Fast Django REST Framework**](https://django-ninja.rest-framework.com/)

-  via Marcus Sharp and Adam Parkin (Codependent Codr) independently
- Django Ninja is a web framework for building APIs with Django and Python 3.6+ type hints.
- This project was heavily inspired by [FastAPI](https://fastapi.tiangolo.com/) (developed by [Sebastián Ramírez](https://github.com/tiangolo))
- Key features:
	- **Easy**: Designed to be easy to use and intuitive.
	- **FAST execution**: Very high performance thanks to [**Pydantic**](https://pydantic-docs.helpmanual.io) and [**async support**](https://django-ninja.rest-framework.com/async-support/).
	- **Fast to code**: Type hints and automatic docs lets you focus only on business logic.
	- **Standards-based**: Based on the open standards for APIs: **OpenAPI** (previously known as Swagger) and **JSON Schema**.
	- **Django friendly**: (obviously) has good integration with the Django core and ORM.
	- **Production ready**: Used by multiple companies on live projects.
- Benchmarks are interesting
- Example

```
    api = NinjaAPI()
    
    @api.get("/add")
    def add(request, a: int, b: int):
        return {"result": a + b}
```

**Sebastian #3:** [**Pydantic 1.8**](https://pydantic-docs.helpmanual.io/changelog/#v18-2021-02-26)

-  Hypothesis plugin (for property-based testing).
- Support for `[NamedTuple](https://pydantic-docs.helpmanual.io/usage/types/#namedtuple)` and `[TypedDict](https://pydantic-docs.helpmanual.io/usage/types/#typeddict)` in models.
- Support for `[Annotated](https://pydantic-docs.helpmanual.io/usage/schema/#typingannotated-fields)` types, e.g.:

```
    def some_func(name: Annotated[str, Field(max_length=256)] = 'Bar'): pass
```

`Annotated` makes default and required values more “correct” in terms of types. E.g. the editor won't assume that a function's parameter is optional because it has a default value of `Field(``'``Bar``'``, max_length=256)`, this will be especially useful for FastAPI dependency functions that could be called directly in other places in the code.


**Michael #4:** [**Google, Microsoft back Python and Rust programming languages**](https://searchapparchitecture.techtarget.com/news/252496553/Google-Microsoft-back-Python-and-Rust-programming-languages?utm_source=flipboard&utm_medium=syndication&utm_campaign=searchAppArchitecture&utm_term=0&utm_content=image-y)

- Partially via Will Shanks
- Google and Microsoft join and strengthen forces with the foundations behind the Python and Rust programming languages
- The companies will get to help shape their future.
- Microsoft has joined Mozilla, AWS, Huawei and Google as founding members of the Rust Foundation.
- Google donated $350,000 to the Python Software Foundation (PSF), making the company the organization's first visionary sponsor.
- Google is investing in improved PyPI malware detection, better foundational Python tools and services, and hiring a CPython Developer-in-Residence for 2021.
- Other PSF sponsors include Salesforce, a sustainability sponsor contributing $90,000. Microsoft, Fastly, Bloomberg and Capital One are maintaining sponsors contributing $60,000 apiece.
- You’ll find Talk Python Training over at the PSF Sponsors as well.
- Microsoft has shown an interest in Rust, particularly for writing secure code: “Rust programming changes the game when it comes to writing safe systems software”
- Microsoft is forming a Rust programming team to contribute engineering efforts to the language's ecosystem, focusing on the compiler, core tooling, documentation and more.

**Brian #5:** [**Semantic Versioning Will Not Save You**](https://hynek.me/articles/semver-will-not-save-you/)

- Hynek Schlawack
- Version numbers are usually 3 decimals separated by dots. 
- SemVer is Major.Minor.Micro
- Implied promise is that if you depend on something and anything other than the Major version changes, your code won’t break.
- In practice, you have to be proactive
	- Have tests with good coverage
	- Pin your dependencies
	- Regularly try to update your dependencies and retest
    - If they pass, pin new versions
    - If not, notify the maintainer of a bug or fix your code
    - Block the versions that don’t work
- Consequences:
	- ZeroVer
	- Version conflicts
	- mayhem
- Consider CalVer

**Sebastian #6:** [**OpenAPI 3.1.0**](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md)
[](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md)
- It was released on February.
- Now the OpenAPI schemas are in sync and based on the latest version of JSON Schema. That improves compatibility with other tools. E.g. frontend components auto-generated from JSON Schema.
- Very small details to adjust in Pydantic and FastAPI, but they are actually more “strictly compatible” with OpenAPI 3.1.0, as they were made with the most recent JSON Schema available at the moment. The differences are mainly in one or two very specific corner cases.

**Note**: OpenAPI 3.1.0 might not be Python-specific enough, so, in that case, I have an alternative topic: [IDOM](https://github.com/idom-team/idom), which is more or less React in Python on the server with live syncing with the browser.

**Extras**

Michael

- Installing Python - [**training.talkpython.fm/installing-python**](https://training.talkpython.fm/installing-python)
- boto3 types update (via  Dean Langsam) - seems like boto type annotations is not maintained anymore, and the rabbit hole of github links sends you to ****[**mypy_boto3_builder**](https://github.com/vemel/mypy_boto3_builder) ****(they have a gif example).
- [Traverse up from the cwd to look for `.venv` virtual environments #75 [](https://github.com/brettcannon/python-launcher/issues/75)[**CLOSED**](https://github.com/brettcannon/python-launcher/issues/75)[]](https://github.com/brettcannon/python-launcher/issues/75)
- [Talk Python: AMA 2021 Episode](https://docs.google.com/forms/d/e/1FAIpQLScFtfHLsjxExgwvO_jQ9pwb8IpNezEdSjsIwnEQz0vb5il16w/viewform)

Brian

- Thanks to Matthew Casari and NOAA for the great shirts.

**Joke**

More [code comments](https://betterprogramming.pub/56-funny-code-comments-that-people-actually-wrote-6074215ab387) jokes

```
    try {
    } finally { 
       // should never happen
    }
```

```
    /* You may think you know what the following code does.
    * But you dont. Trust me.
    * Fiddle with it, and you'll spend many a sleepless
    * night cursing the moment you thought youd be clever
    * enough to "optimize" the code below.
    * Now close this file and go play with something else.
    */
```

```
    const int TEN=10; // As if the value of 10 will fluctuate...
```

```
    // I am not responsible for this code.
    // They made me write it, against my will.
```

```
    // If this code works, it was written by Paul DiLascia.
    // If not, we don't know who wrote it
```

```
    options.BatchSize = 300; //Madness? THIS IS SPARTA!
```
