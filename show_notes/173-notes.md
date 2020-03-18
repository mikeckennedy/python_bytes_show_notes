# Python Bytes 173

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**Advanced usage of Python requests - timeouts, retries, hooks**](https://hodovi.ch/blog/advanced-usage-python-requests-timeouts-retries-hooks/)

- Dani Hodovic, [@DaniHodovic](https://twitter.com/DaniHodovic)
- “While it's easy to immediately be productive with requests because of the simple API, the library also offers extensibility for advanced use cases. If you're writing an API-heavy client or a web scraper you'll probably need tolerance for network failures, helpful debugging traces and syntactic sugar.”
- Lots of cool tricks I didn’t know you could do with requests.
	- Using hooks to call `raise_for_status()` on every call.
	- Using sessions and setting base URLs
	- Setting default timeouts with transport adapters
	- Retry on failure, with gobs of configuration options.
	- Combining timeouts and retries
	- Debugging http requests by printing out headers or printing everything.
	- Testing and mocking requests
	- Mimicking browser behaviors by overriding the User-Agent header request

**Michael #2:** [Fluent Assertions](https://github.com/csparpa/fluentcheck)

- Via [Dean Agan](https://twitter.com/dean_agan/status/1236231021416202240)
- **fluentcheck** helps you reducing the lines of code providing a human-friendly and fluent way to make assertions.
- Example (for now):
    
```
def my_function(n, obj):
    assert n is not None
    assert instanceof(n, float)
    assert 0. < n < 1
    assert obj is not None
    assert isinstance(obj, MyCustomType)
```

can be

```
def my_function(n, obj):
    Check(n).is_not_None().is_float().is_between(0., 1.)
    Check(obj).is_not_None().is_subtype_of(MyCustomType)
```

With [a PR I’m working on](https://github.com/csparpa/fluentcheck/pull/14) (now accepted), it’ll support:

```
def my_function(n, obj):
    Is(n).not_none.float.between(0., 1.)
    Is(obj).not_none.subtype_of(MyCustomType)
```

**Brian #3:** [**Python in GitHub Actions**](https://hynek.me/articles/python-github-actions/)

- Hynek Schlawack, [@hynek](https://twitter.com/hynek)
- “for an open source Python package, … my current recommendation for most people is to switch to GitHub Actions for its simplicity and better integration.” vs Azure Pipelines.
- Article describes how to get started and some basic configuration for:
	- Running tests through tox, including coverage, for multiple Python versions. Including yml config and tox.ini changes necessary.
	- Nice reminder to clean out old configurations for other CIs.
	- Combining coverage reports and pushing code coverage info to Codecov
	- Building the package.
	- Running twine check to check the long description.
	- Checking the install on Linux, Windows, and Mac
- Related:
	- [How to write good quality Python code with GitHub Actions](https://medium.com/@wkrzywiec/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a)

**Michael #4:** [**VCR.py**](https://vcrpy.readthedocs.io/en/latest/)

- via Tim Head
- VCR.py simplifies and speeds up tests that make HTTP requests. 
- The first time you run code that is inside a VCR.py context manager or decorated function, VCR.py records all HTTP interactions that take place through the libraries it supports and serializes and writes them to a flat file (in yaml format by default). 
- Intercept any HTTP requests that it recognizes from the original test run and return the responses that corresponded to those requests. This means that the requests will not actually result in HTTP traffic, which confers several benefits including:
	- The ability to work offline
	- Completely deterministic tests
	- Increased test execution speed
- If the server you are testing against ever changes its API, all you need to do is delete your existing cassette files, and run your tests again.
- [Test and Code 102](https://testandcode.com/102)
- [pytest-vcr](https://github.com/ktosiek/pytest-vcr): pytest plugin for managing VCR.py cassettes

```
@pytest.mark.vcr()
def test_iana():
    response = urlopen('http://www.iana.org/domains/reserved').read()
    assert b'Example domains' in response
```

**Brian #5:** [**8 Coolest Python Programming Language Features**](https://dev.to/renegadecoder94/8-coolest-python-programming-language-features-58i9)

- Jeremy Grifski, [@RenegadeCoder94](http://twitter.com/RenegadeCoder94)
- Nice reminder of why I love Python and things I miss when I use other languages.
- The list
	- list comprehensions
	- generator expressions
	- slice assignment
	- iterable unpacking
	- negative indexing
	- dictionary comprehensions
	- chaining comparisons
	- f-strings

**Michael #6:** [**Bento**](http://bento.dev)

- Find Python web-app bugs delightfully fast, without changing your workflow
- Find bugs that matter: Checks find security and reliability bugs in your code. They’re vetted across thousands of open source projects and never nit your style.
- Upgrade your tooling: You don’t have to fix existing bugs to adopt Bento. It’s diff-centric, finding new bugs introduced by your changes. And there’s zero config.
- Go delightfully fast: Run Bento automatically locally or in CI. Either way, it runs offline and never sends your code anywhere.
- Checks: [https://bento.dev/checks/](https://bento.dev/checks/) 

**Joke:**

[https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e5ff5b454e93258e907753b/ecd7567c50cc0d073820bf961f489365/debugging.jpg](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e5ff5b454e93258e907753b/ecd7567c50cc0d073820bf961f489365/debugging.jpg)
