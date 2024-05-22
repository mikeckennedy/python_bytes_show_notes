# Python Bytes 245

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: Juan Pedro Araque Espinosa (Youtube Chanel: [Commit that Line](https://www.youtube.com/channel/UCLpaX8JBrJTRBy0R9IM9W7A))


**Michael #1:** [**State of the community (via Jet Brains)**](https://www.jetbrains.com/lp/devecosystem-2021/)

- This report presents the combined results of the fifth annual Developer Ecosystem Survey conducted by JetBrains
- Not just Python, but all of us
- Python is more popular than Java in terms of overall usage, while Java is more popular than Python as a main language.
- The 5 fastest growing languages are Python, TypeScript, Kotlin, SQL, and Go.
- A majority of the respondents (71%) develop for web backend.
- Does fall into the trap of “Hi, I’m a CSS developer, nice to meet you” though
- Women are more likely than men to be involved in data analysis, machine learning, and UX/UI design or research. 
- Women are less likely than men to be involved in infrastructure development and DevOps, system administration, or Deployment.


**Brian #2:** [**Cornell - record & replay mock server**](https://pypi.org/project/cornell/)

- Suggested by Yael Mintz (and it’s her project)
- [Introduction blog post](https://medium.com/hiredscore-engineering/scale-up-your-e2e-tests-using-mock-server-a6872f660288)
	- “Cornell makes it dead simple, via its record and replay features to perform end-to-end testing in a fast and isolated testing environment.
	- When your application integrates with multiple web-based services, end-to-end testing is crucial before deploying to production. Mocking is often a tedious task. It becomes even more tiresome when working with multiple APIs from multiple vendors.
	- [vcrpy](https://github.com/kevin1024/vcrpy) is an awesome library that records and replays HTTP interactions for unit tests. Its output is saved to reusable "cassette" files.
	- By wrapping vcrpy with Flask, Cornell provides a lightweight record and replay server that can be easily used during distributed system testing and simulate all HTTP traffic needed for your tests.”


**Juanpe** **#3:** [**Factory boy**](https://github.com/FactoryBoy/factory_boy) **(with Pydantic by chance)**

- `Factory_boy` allows creating factories to generate objects that could be used as text fixtures
- Briefly mentioned in the past in [episode 193](https://pythonbytes.fm/episodes/show/193/break-out-the-django-testing-toolbox)
- A factory takes a base object and allows to very easily and naturally define default values for each field of the object. 
- One can have many factories for the same object that could be used define different types of fixtures of the same object
- It works with ORM objects (Django, Mongo, SQLAlchemy…)
- If you have a project that uses Pydantic to define your objects, factory boy also supports Pydantic although it is not documented and does it by a side effect
- Internally factory boy generates a parameters dictionary that that is unpacked when constructing the model at hands. This works perfectly with pydantic and can be used to generate pydantic objects on the fly with the full power of factory boy
[](https://github.com/FactoryBoy/factory_boy)


**Michael #4:** [**pyinstrument**](https://github.com/joerick/pyinstrument)

- Call stack profiler for Python. Shows you why your code is slow! 
- Instead of writing `python script.py`, type `pyinstrument script.py` 
- Your script will run as normal, and at the end (or when you press `^C`), Pyinstrument will output a colored summary showing where most of the time was spent.
- Async support! Pyinstrument now detects when an async task hits an await, and tracks time spent outside of the async context under this await.
- Pyinstrument also has a Python API. Just surround your code with Pyinstrument
- Nice middleware examples for Flask & Django


**Brian #5:** [**Python 3.10 is now in Release Candidate phase. RC1 just released.**](https://www.python.org/downloads/release/python-3100rc1/)

- RC2 planned for 2021-09-06
- official release is planned for 2021-10-04
- It is **strongly encourage** maintainers of third-party Python projects to prepare their projects for 3.10 compatibility during this phase
- Reminder of major changes:
	- [PEP 623](https://www.python.org/dev/peps/pep-0623/) -- Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
	- [PEP 604](https://www.python.org/dev/peps/pep-0604/) -- Allow writing union types as X | Y
	- [PEP 612](https://www.python.org/dev/peps/pep-0612/) -- Parameter Specification Variables
	- [PEP 626](https://www.python.org/dev/peps/pep-0626/) -- Precise line numbers for debugging and other tools.
	- [PEP 618](https://www.python.org/dev/peps/pep-0618/) -- Add Optional Length-Checking To zip.
	- [bpo-12782](https://bugs.python.org/issue12782): Parenthesized context managers are now officially allowed.
	- [PEP 632](https://www.python.org/dev/peps/pep-0632/) -- Deprecate distutils module.
	- [PEP 613](https://www.python.org/dev/peps/pep-0613/) -- Explicit Type Aliases
	- [PEP 634](https://www.python.org/dev/peps/pep-0634/) -- Structural Pattern Matching: Specification
	- [PEP 635](https://www.python.org/dev/peps/pep-0635/) -- Structural Pattern Matching: Motivation and Rationale
	- [PEP 636](https://www.python.org/dev/peps/pep-0636/) -- Structural Pattern Matching: Tutorial
	- [PEP 644](https://www.python.org/dev/peps/pep-0644/) -- Require OpenSSL 1.1.1 or newer
	- [PEP 624](https://www.python.org/dev/peps/pep-0624/) -- Remove Py_UNICODE encoder APIs
	- [PEP 597](https://www.python.org/dev/peps/pep-0597/) -- Add optional EncodingWarning


**Juanpe** **#6:** [**time-machine**](https://github.com/adamchainz/time-machine)

- Time-machine mock datetime and time related calls globally noticeably faster than other well known tools like freezgun.
- The mocking is achieved by replacing the c-level calls by whatever value we want which means the library does not need to mock individual imports.
- Mocking datetime cannot be done with patch.object and needs to be patched everywhere it is used which can turn mocking everything into a tedious (and/or slow) process.
- Datetime methods (now, today, utcnow…) can be mocked by setting a frozen time or by letting the time tick since the mock call is made.
- It provides a simple context manager to use it as well as pytest fixture that makes using it very simple

```
    from datetime import datetime 
    import time_machine
    
    @time_machine.travel("2021-01-01 21:00")
    def test_in_the_past():
        assert datetime.now() == datetime(2021, 1, 1, 21, 0)

    ---------------------------------
    # The time_machine fixture can also be used with pytest
    def test_in_the_past(time_machine): 
        time_machine.move_to(datetime(2021, 1, 1, 21, 0))
        assert datetime.now() == datetime(2021, 1, 1, 21, 0)
``` 


**Extras**

Michael

- [Credit-card stealing malware found in official Python repository](https://www.techradar.com/news/credit-card-stealing-malware-found-in-official-python-repository) and [Software downloaded 30,000 times from PyPI ransacked developers’ machines](https://arstechnica.com/gadgets/2021/07/malicious-pypi-packages-caught-stealing-developer-data-and-injecting-code/) (via Joe Riedly)

Brian

- [Flavors of TDD - Test & Code episode 162](https://testandcode.com/162)
- Working on tox and CI chapter of [2nd edition of pytest book](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/), hoping that to be released within the next week.

**Joke** 

[JavaScript Developer Bouncing from framework to framework](https://twitter.com/darkgaro/status/1421208437480906752)
