# Python Bytes 311

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

Special guest: **Murilo Cunha**

**Michael #1:** [**Latexify**](https://twitter.com/btskinn/status/1592892053364805632)

- We are used to turning beautiful math into programming symbols.
- For example: [amitness.com/2019/08/math-for-programmers/#sigma](https://amitness.com/2019/08/math-for-programmers/#sigma)
- Take this code:
    def do_math(a, b, c):
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
- Add `@latexify.function` decorator
- display `do_math` in a notebook
- Get this latex: `\mathrm{do_math}(a, b, c) = \frac{-b + \sqrt{b^{{2}} - {4} a c}}{{2} a}`
- Which renders as
![](https://python-bytes-static.nyc3.digitaloceanspaces.com/latex-math.png)

- I could only get it to install with:
    `pip install git+https://github.com/google/latexify_py`


**Brian #2:** [**prefixed**](https://pypi.org/project/prefixed/)

- From **Avram Lubkin**
- “Prefixed provides an alternative implementation of the built-in [float](https://docs.python.org/3/library/functions.html#float) which supports formatted output with [SI (decimal)](https://en.wikipedia.org/wiki/Metric_prefix) and [IEC (binary)](https://en.wikipedia.org/wiki/Binary_prefix) prefixes.”

```
>>> from prefixed import Float
>>> f'{Float(3250):.2h}'
'3.25k'
>>> '{:.2h}s'.format(Float(.00001534))
'15.34μs'
>>> '{:.2k}B'.format(Float(42467328))
'40.50MiB'
>>> f'{Float(2048):.2m}B'
'2.00KB'
```

- Because [prefixed.Float](https://prefixed.readthedocs.io/en/stable/api.html#prefixed.Float) inherits from the built-in [float](https://docs.python.org/3/library/functions.html#float), it behaves exactly the same in most cases.
- When a math operation is performed with another real number type ([float](https://docs.python.org/3/library/functions.html#float), [int](https://docs.python.org/3/library/functions.html#int)), the result will be a [prefixed.Float](https://prefixed.readthedocs.io/en/stable/api.html#prefixed.Float) instance.
- also interesting
    - [First new SI prefixes for over 30 years](https://metricviews.uk/2022/11/20/first-new-si-prefixes-for-over-30-years/)
    - [new prefixes also show up here](https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes)
- 

**Murilo #3:** [**dbt**](https://www.getdbt.com/)

- Open source tool
- CLI tool
- Built with Python 🐍
- Applies “best practices” to SQL projects
- Combines git + `.sql` files + `jinja`
- [Support many data platforms](https://docs.getdbt.com/docs/supported-data-platforms)
- Let’s you
    - Template SQL queries
        - Including loops
    - Execute DAGs
    - Data validation
    - Easily build docs (data lineage, visualize DAGs, etc.)
- Now you can also run [Python models](https://docs.getdbt.com/docs/build/python-models)
    - Useful if there’s a convenient python function for your data transformation or some more complex logic (i.e.:fuzzy string matching, machine learning models, etc.)
    - [Available for Snowflake, Databricks, BigQuery](https://docs.getdbt.com/docs/build/python-models#supported-data-platforms)
    - dbt’s coalesce’s announcement https://www.youtube.com/watch?v=rVprdyxcGUo

**Michael #4:** [**Memray**](https://twitter.com/roman_the_right/status/1592938538214912000) [**p**](https://twitter.com/roman_the_right/status/1592938538214912000)[**ytest plugin**](https://twitter.com/roman_the_right/status/1592938538214912000)

- [pytest-memray](https://github.com/bloomberg/pytest-memray) is the pytest plugin for, well, [memray](https://github.com/bloomberg/memray). :)
- You can ensure that not too much memory is used with `@pytest``**.**``mark``**.**``limit_memory``**(**``"24 MB"``**)**` 
- And you get an allocation report with `pytest --memray file.py`
- But coming soon, we’ll have memory leak checking too.
```
@pytest.mark.check_leaks()
def test_foobar():
  # Do some stuff and ensure
  # it does not leak memory
  pass
```

**Brian #5:**  [**Stealing Open Source code from Textual**](https://textual.textualize.io/blog/2022/11/20/stealing-open-source-code-from-textual/)

- Will McGugan
- Will reminds us of one of the great benefits of open source code, stealing code
    - (when allowed by the license, of course)
- Goes as far as to point out some bits of textual that you might want to lift
    - looping with indication of when you’ve hit the first or last item
    - a LRUCache with more flexibility than lru_cache
    - a Color class with conversions for css, hex, monochrome, hsl
    - 2d geometry

**Murilo #6:** [**Shed**](https://github.com/Zac-HD/shed)

- Superset of black
- "`shed` is the *maximally opinionated* autoformatting tool. It's *all about* [convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration), and designed to be a single opinionated tool that fully canonicalises my code - formatting, imports, updates, and every other fix I can possibly automate.”
- Also format code snippets in docstrings, markdown, restructured text
- No configuration options
- pre-commit hooks available
- Bundles together:
    - `black`
    - `isort`
    - `autoflake`
    - `pyupgrade`
    - `blacken-docs`

**Extras** 

Brian: 

- [pytest-check](https://pypi.org/project/pytest-check/) (version 1.1.3) changes now live 
    - New README, hopefully makes it clear how to use.
    - Use `check` from
        - `from pytest_check import check`
        - or from the `check` fixture: `def test_foo(check): …`
    - Either form returns the same object.
    - From that `check` object, you can 
        - use helper functions like `check.equal(a, b)`, etc.
        - use it as a context manager, `with check: assert a == b`
        - even grab the `raises` context manager: `with check.raises(Exception): …`
    - Intended to be backwards compatible
        - although some old use cases might be deprecated/removed in the future.

Michael:

- New YouTube Video: [**Best Native App for Mastodon is ...**](https://www.youtube.com/watch?v=oNT2Sa_0YJU)
- Nearly 50% of macOS malware [**comes from one app**](https://www.laptopmag.com/news/nearly-50-of-macos-malware-comes-from-one-app-do-you-have-it-on-your-macbook) — do you have it on your MacBook?
- [PyCascades CfP](https://pretalx.com/pycascades-2023/cfp)
- A fresh take on blogging (for Michael): [**mkennedy.codes**](https://mkennedy.codes)
    - Based on [**Hugo**](https://gohugo.io) - which is *so* good.
    - Hosted on [**netlify.com**](https://www.netlify.com)


Murilo:

- [mastodon.py](https://github.com/halcy/Mastodon.py) -  a Python wrapper around [Mastodon’s API](https://github.com/mastodon/mastodon/)
- Nice [notebook diffs in Github PRs](https://twitter.com/hamelhusain/status/1590956886496419840?s=46&t=QBEo8HahEDTKEhJrsnlcgA) 🚀
- [flake8 is not on Gitlab anymore](https://www.youtube.com/watch?v=1FIgj9Q5e6A)
- [Who’s gonna win the world cup?](https://www.youtube.com/watch?v=KjISuZ5o06Q)
- [lancer](https://github.com/LeviBorodenko/lancer)

**Joke:** 

- [**Messing with the algorithm**](https://twitter.com/PR0GRAMMERHUM0R/status/1588939225180905478) 
- Let’s start this one with [some history](https://despair.com/collections/demotivators)
- [Recusion joke](https://twitter.com/btskinn/status/1593002791978422272)

