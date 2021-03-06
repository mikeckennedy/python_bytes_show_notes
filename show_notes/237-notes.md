# Python Bytes 237

Sponsored by Sentry:

- Sign up at [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)
- And please, when signing up, click ***Got a promo code? Redeem*** and enter **PYTHONBYTES**

Special guest: **Mike Groves**

**Michael #1:** [**Textual**](https://github.com/willmcgugan/textual)

- Textual (Rich.tui) is a TUI (Text User Interface) framework for Python using Rich as a renderer.
- Rich TUI will integrate tightly with its parent project, Rich.
- This project is currently a work in progress and may not be usable for a while.

**Brian #2:** **Pinning application dependencies with pip-tools compile**

- via John Hagen
- [pip-tools](https://github.com/jazzband/pip-tools) has more functionality than this, but compile alone is quite useful
- Start with a loose list of dependencies in `requirements.in`:
```
    typer
    rich
```
- Can have things like >= and such if you have fixed dependencies.
- Now `pip install pip-tools`, and `pip-compile requirements.in`
- or `python -m piptools compile requirements.in`
	- both have same effect.
- Now you’ll have a `requirements.txt` file with pinned dependencies:
```
    # autogenerated by: pip-compile requirements.in
    click==7.1.2
        # via typer
    colorama==0.4.4
        # via rich
    commonmark==0.9.1
        # via rich
    pygments==2.9.0
        # via rich
    rich==10.2.2
        # via -r requirements.in
    typer==0.3.2
        # via -r requirements.in
```
- Now, do the same with a `dev-requirements.ini` to create `dev-requirements.txt`.
- Then, of course:
```
    - `pip install -r requirements.txt`
    - `pip install -r dev-requirements.txt`
    - And test your application.
    - All good? Push changes.
```
- To force `pip-compile` to update all packages in an existing `requirements.txt`, run `pip-compile --upgrade`.
- John provided an example project that uses this workflow: [python-blueprint](https://github.com/johnthagen/python-blueprint)

**Mike #3:** [**Pynguin**](https://github.com/se2p/pynguin)

-  Automated test generation
- **Pynguin** is a framework that allows automated unit test generation for Python. It is an extensible tool that allows the implementation of various test-generation approaches.

**Michael #4:** [**Python Advisory DB**](https://github.com/pypa/advisory-db)

- via [**Brian Skinn**](https://twitter.com/btskinn/status/1400212636193542147)
- A community owned repository of advisories for packages published on [**pypi.org**](https://pypi.org)**.**
- Much of the existing set of vulnerabilities are collected from the [National Vulnerability Database CVE](https://nvd.nist.gov/vuln/data-feeds) feed.
- Vulnerabilities are integrated into the [Open Source Vulnerabilities](https://osv.dev) project, which provides an API to query for vulnerabilities.
- Longer term, we are working with the PyPI team to [build a pipeline](https://github.com/pypa/warehouse/issues/9407) to automatically get these vulnerabilities [listed] into PyPI.
- Tracks known security issues with the packages, for example:
```
    PYSEC-2020-28.yaml
    id: PYSEC-2020-28
    package:
      name: bleach
      ecosystem: PyPI
    details: In Mozilla Bleach before 3.12, a mutation XSS in bleach.clean when RCDATA
      and either svg or math tags are whitelisted and the keyword argument strip=False.
    affects:
      ranges:
      - type: ECOSYSTEM
        fixed: 3.1.2
      versions:
      - '0.1'
      - 0.1.1
      - 0.1.2
      - '0.2'
    ...
```

**Brian #5:** [**Function Overloading with singledispatch and multipledispatch**](https://towardsdatascience.com/the-correct-way-to-overload-functions-in-python-b11b50ca7336)

- by Martin Heinz
- I kinda avoid using the phrase “The Correct Way to …”, but you do you, Martin.
- In C/C++, we can overload functions, which means multiple functions with the same name but different parameter types just work. 
- In Python, you can’t do that automatically, but you can do it.
- It’s in the stdlib with `functools` and `singledispatch`:
```
    from functools import singledispatch
    from datetime import date, time
    
    @singledispatch
    def format(arg):
        return arg
    
    @format.register
    def _(arg: date):
        return f"{arg.day}-{arg.month}-{arg.year}"
    
    @format.register(time)
    def _(arg):
        return f"{arg.hour}:{arg.minute}:{arg.second}"
```

- Now `format` works like two functions:
```
    print(format(date(2021, 5, 26)))
    # 26-5-2021
    print(format(time(19, 22, 15)))
    # 19:22:15
```


- What if you want to switch on the type of multiple parameters? [multipledispatch](https://pypi.org/project/multipledispatch/), a third party package, does the trick:
```
    from multipledispatch import dispatch
    
    @dispatch(list, str)
    def concatenate(a, b):
        a.append(b)
        return a
    
    @dispatch(str, str)
    def concatenate(a, b):
        return a + b
    
    print(concatenate(["a", "b"], "c"))
    # ['a', 'b', 'c']
    print(concatenate("Hello", "World"))
    # HelloWorld
```

**Mike #6:** [**Aiosql**](https://nackjicholson.github.io/aiosql/)

- Fast Async SQL Template Engine
- Lightweight replacement for ORM libraries such as SQLAlchemy.
    

**Extras**

**Michael**

- SoftwareX Journal, Elsevier has had an open-access software journal, via Daniel Mulkey. There's even a [**special issue collection**](https://www.sciencedirect.com/journal/softwarex/special-issue/103XKC9DRLV) on software contributing to gravitational wave discovery.
- Python 3.10.0b2 is available
- Django security releases issued: 3.2.4, 3.1.12, and 2.2.24
- Talks [**on YouTube**](https://www.youtube.com/watch?v=z_hm5oX7ZlE&list=PL2Uw4_HvXqvYk1Y5P8kryoyd83L_0Uk5K) for PyCon 2021.
- [**aicsimageio**](https://twitter.com/jmaxfieldbrown/status/1401933861081124874) [4.0 released](https://twitter.com/jmaxfieldbrown/status/1401933861081124874), lots of goodness for bio-image analysis and microscopy, thanks Madison Swain-Bowden.

**Mike**

- **[Postponement of PEP 563 in 3.10](https://www.prettyfwd.com/t/c7l72nBxQjqGATzdz9DDLA/)**

**Joke** 

[**Bank robbers**](https://twitter.com/AikidoUke/status/1397406450377543683)


- [A book about Rich](https://twitter.com/brianokken/status/1402293369007534080?s=20)
![](https://paper-attachments.dropbox.com/s_ED0B2ECD3F3EA9A0A3D6DE8B7AA3BCAD34DD73FCC6E4174A711517C16C525C25_1623258891709_rich.png)


