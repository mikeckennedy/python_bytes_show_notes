# Python Bytes 273

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)


**Michael #1:** [**Physics Breakthrough as AI Successfully Controls Plasma in Nuclear Fusion Experiment**](https://www.sciencealert.com/physics-breakthrough-as-ai-successfully-controls-plasma-in-nuclear-fusion-experiment?utm_campaign=AppleNews&utm_medium=referral&utm_source=AppleNews)

**Brian #2:** [**PEP 680 -- tomllib: Support for Parsing TOML in the Standard Library**](https://www.python.org/dev/peps/pep-0680/)

- Accepted for Python 3.11
- This PEP proposes basing the standard library support for reading TOML on the third-party library [tomli](https://github.com/hukkin/tomli)

**Michael** **#3: [Thread local](https://www.slinkp.com/python-thread-locals-20171201.html)**

- `threading.local`: A class that represents thread-local data. Thread-local data are data whose values are thread specific.
- Just create an instance of `local` (or a subclass) and store attributes on it
- You can even subclass it.


**Brian #4:** [**What is a generator function?**](https://www.pythonmorsels.com/topics/what-is-a-generator-function)

- Trey Hunner
- Super handy, and way easier than you think, if you’ve never written your own.
- Really, it’s just a function that uses `yield` instead of `return` and supplies one element at a time instead of returning a list or dict or tuple or other large structure.
- Some details
    - generator functions return generator objects
    - generator objects are on pause and use the built in `next()` function to get next item.
    - they raise `StopIteration` when done.
    - Most generally used from `for` loops.
    - Generator objects cannot be re-used when exhausted
        - but you can get a new one with the next `for` loop you use. So, it’s all good.

**Michael #5:**  [**dirty-equals**](https://dirty-equals.helpmanual.io)

- via Will McGugan, by Samual Colvin
- Doing dirty (but extremely useful) things with equals.

```python
from dirty_equals import IsPositive

assert 1 == IsPositive 
assert -2 == IsPositive  # this will fail!
```

```python
  user_data = db_conn.fetchrow('select * from users')
  assert user_data == {
       'id': IsPositiveInt, 
       'username': 'samuelcolvin', 
       'avatar_file': IsStr(regex=r'/[a-z0-9\-]{10}/example\.png'), 
       'settings_json': IsJson({'theme': 'dark', 'language': 'en'}), 
       'created_ts': IsNow(delta=3), 
   }
```



**Brian #6:** [**Commitizen**](https://commitizen-tools.github.io/commitizen/)

- from the docs
    - Command-line utility to create commits with your rules. Defaults: [Conventional commits](https://www.conventionalcommits.org/)
    - Display information about your commit rules (commands: schema, example, info)
    - Bump version automatically using [semantic versioning](https://semver.org/) based on the commits. [Read More](https://commitizen-tools.github.io/commitizen/bump/)
    - Generate a changelog using [Keep a changelog](https://keepachangelog.com/)
- considering using for consistent commit message formatting
- can be used with [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) for automatic semantic versioning 
- learned about it in [10 Tools I Wish I Knew When I Started Working with Python](https://python.plainenglish.io/10-tools-to-help-claw-your-way-back-to-sanity-while-coding-python-df0af160c33e)
- questions
    - anyone using this or something similar?
    - does this make sense for small to medium sized projects? or overkill?

Extras:

- [pytest book](https://pythontest.com/pytest-book/)
    - 40% off sale continues through March 19 for eBook
    - [Amazon](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680508601) lists the book as “shipping in 1-2 days”, as of March 2

Michael:

- [**Pronouncing the Python Walrus operator := as “becomes”**](https://twitter.com/willmcgugan/status/1497503795097522180)
- Via [John Sheehan](https://www.linkedin.com/feed/update/urn:li:activity:6903314731617071104/): String methods `startswith()` and `endswith()` can take a tuple as its first argument that lets you check for multiple values with one call:

```
    >>> x = "abcdefg"
    >>> x.startswith(("ab", "cd", "ef"), 2)
    True
```

**Joke:** [CS Background](https://twitter.com/PR0GRAMMERHUM0R/status/1491789078819344392)

