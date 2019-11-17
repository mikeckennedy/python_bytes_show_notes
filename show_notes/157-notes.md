# Python Bytes 157

This episode is sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Michael #1:** [**pydantic**](https://pydantic-docs.helpmanual.io/)

- via [Colin Sullivan](https://twitter.com/sullivancolin/status/1192482220168093697)
- Data validation and settings management using python type annotations.
- (We covered [Cerberus](https://docs.python-cerberus.org/en/stable/), this is similar)
- *pydantic* enforces type hints at runtime, and provides user friendly errors when data is invalid.

```
    class User(pydantic.BaseModel):
        id: int
        name = 'John Doe'
        signup_ts: datetime = None
        friends: List[int] = []
    
    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01 12:22',
        'friends': [1, 2, '3']
    }
    user = User(**external_data)
```

- `id` is of type int; the annotation-only declaration tells *pydantic* that this field is required. Strings, bytes or floats will be coerced to ints if possible; otherwise an exception will be raised.
- `name` is inferred as a string from the provided default; because it has a default, it is not required.
- `signup_ts` is a datetime field which is not required (and takes the value `None` if it's not supplied).
- Why use it?
	- There's no new schema definition micro-language to learn.
	- In [benchmarks](https://pydantic-docs.helpmanual.io/benchmarks/) *pydantic* is faster than all other tested libraries.
	- Use of [recursive](https://pydantic-docs.helpmanual.io/usage/models/#recursive-models) [*pydantic*](https://pydantic-docs.helpmanual.io/usage/models/#recursive-models) [models](https://pydantic-docs.helpmanual.io/usage/models/#recursive-models), `typing`'s [standard types](https://pydantic-docs.helpmanual.io/usage/types/#standard-library-types) (e.g. `List`, `Tuple`, `Dict` etc.) and [validators](https://pydantic-docs.helpmanual.io/usage/validators/) allow complex data schemas to be clearly and easily defined, validated, and parsed.
	- As well as `BaseModel`, *pydantic* provides a `[dataclass](https://pydantic-docs.helpmanual.io/usage/dataclasses/)` decorator which creates (almost) vanilla python dataclasses with input data parsing and validation.

**Brian #2:** **Coverage.py 5.0 beta 1 adds context support**

- Please try out the beta, even without trying contexts, as it helps Ned Batchelder to make sure it’s as backwards compatible as possible while still adding this super cool functionality.
	- [Coverage 5.0 beta 1](https://nedbatchelder.com/blog/201911/coverage_50_beta_1.html) announcement
	- The [changes](https://coverage.readthedocs.io/en/latest/whatsnew5x.html).
	- [Measurement contexts](https://coverage.readthedocs.io/en/latest/contexts.html#contexts) in depth.
- Trying out contexts with pytest and pytest-cov:

```
    (venv) $ pip install coverage==5.0b1
    (venv) $ pip install pytest-cov
    (venv) $ pytest --cov=foo --cov-context=test test_foo.py
    (venv) $ coverage html --show-contexts
    (venv) $ open htmlcov/index.html 
```

- results in coverage report that has little dropdowns on the right for lines that are covered, and what context they were covered.
- For the example above, with pytest-cov, it shows what test caused each line to be hit.
- Contexts can do way more than this. One example, split up different levels of tests, to see which lines are only hit by unit tests, indicating missing higher level tests, or the opposite.
- The stored db could also possibly be mined to see how much overlap there is between tests, and maybe help with higher level tools to predict the harm or benefit from removing some tests.
- I’m excited about the future, with contexts in place.
- Even if you ignore contexts, please go try out the beta ASAP to make sure your old use model still works.

[**Michael #3: PSF is seeking developers for paid contract improving pip**](https://pyfound.blogspot.com/2019/11/seeking-developers-for-paid-contract.html)

- via Brian Rutledge
- The [Python Software Foundation](https://python.org/psf-landing) [Packaging Working Group](https://www.python.org/psf/committees/#packaging-work-group) is receiving funding to work on the design, implementation, and rollout of pip's next-generation dependency resolver.
- This project aims to complete the [design, implementation, and rollout](https://github.com/pypa/pip/issues/6536) of [pip's next-generation dependency resolver](https://github.com/pypa/pip/issues/988). 
- Lower the barriers to installing Python software, empowering users to get a version of a package that works. 
- It will also lower the barriers to distributing Python software, empowering developers to make their work available in an easily reusable form.
- Because of the size of the project, funding has been allocated to secure two contractors, a senior developer and an intermediate developer, to work on development, testing and building test infrastructure, code review, bug triage, and assisting in the rollout of necessary features.
- Total pay: Stage 1: $116,375, Stage 2: $103,700 

**Brian #4:** ****[**dovpanda**](https://github.com/dovpanda-dev/dovpanda) **- Directions OVer PANDAs**

- Dean Langsam
- “Directions are hints and tips for using pandas in an analysis environment. dovpanda is an overlay for working with pandas in an analysis environment.
- "If you think your task is common enough, it probably is, and Pandas probably has a built-in solution. dovpanda is an overlay module that tries to understand what you are trying to do with your data, and help you find easier ways to write your code.”
- “The main usage of `dovpanda` is its hints mechanism, which is very easy and works out-of-the-box. Just import it after you import pandas, whether inside a notebook or in a console.”
- It’s like training wheels for pandas to help you get the most out of pandas and learn while you are doing your work. Very cool.

**Michael #5:** [**removestar**](https://www.asmeurer.com/removestar/) 

- via PyCoders newsletter
- Tool to automatically replace 'import *' in Python files with explicit imports
- Report only mode and modify in place mode.

**Brian #6:**  [**pytest-quarantine**](https://github.com/EnergySage/pytest-quarantine/) **: Save the list of failing tests, so that they can be automatically marked as expected failures on future test runs.**

- Brian Rutlage
- Really nice email from Brian: 
- >"Hi Brian! We've met a couple times at PyCon in Cleveland. Thanks for your podcasts, and your book. I've gone from being a complete pytest newbie, to helping my company adopt it, to writing a plugin. The plugin was something I developed at work, and they let me open-source it. I wanted to share it with you as a way of saying "thank you", and because you seem to be a bit of connoisseur of pytest plugins. ;)"
- Here it is: [https://github.com/EnergySage/pytest-quarantine/](https://github.com/EnergySage/pytest-quarantine/)”
- pytest has a cool feature called xfail, to allow you to mark tests you know fail.
- pytest-quarantine allows you to run your suite and generate a file of all failures, then use that to mark the xfails. 
	- Then you or your team can chip away at these failures until you get rid of them. 
	- But in the meantime, your suite can still be useful for finding new failures.
	- And, the use of an external file to mark failures makes it so you don’t have to edit your test files to mark the tests that are xfail.


Extras:

MK: [Our infrastructure is fully carbon neutral](https://training.talkpython.fm/policies/environment)!

Joke:

A cop pulls Dr. Heisenberg over for speeding. The officer asks, "Do you know how fast you were going?" Heisenberg pauses for a moment, then answers, "No, but I know where I am.” [1]


1. [S](https://www.britannica.com/science/uncertainty-principle)[**ee Uncertainty principle**](https://www.britannica.com/science/uncertainty-principle), also called **Heisenberg uncertainty principle** or indeterminacy **principle**, statement, articulated (1927) by the German physicist Werner **Heisenberg**, that the position and the velocity of an object cannot both be measured exactly, at the same time, even in theory.

