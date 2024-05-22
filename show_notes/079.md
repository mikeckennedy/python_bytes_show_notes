# Python Bytes 79
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**pytest 3.6.0**](https://docs.pytest.org/en/latest/changelog.html#pytest-3-6-0-2018-05-23)

  - Revamp the internals of the `pytest.mark` implementation with correct per node handling which fixes a number of long standing bugs caused by the old design. This introduces new `Node.iter_markers(name)` and `Node.get_closest_mark(name)` APIs. 
		- Depricating `Node.get_marker(name)`. 
		- [reasons for the revamp](https://docs.pytest.org/en/latest/mark.html#marker-revamp-and-iteration)
		- [updating existing code to use the new APIs](https://docs.pytest.org/en/latest/mark.html#updating-code)
		- Now when `@pytest.fixture` is applied more than once to the same function a `ValueError` is raised. This buggy behavior would cause surprising problems and if was working for a test suite it was mostly by accident.
  - Support for Python 3.7’s builtin `breakpoint()` method, 
		- see [Using the builtin breakpoint function](https://docs.pytest.org/en/latest/usage.html#breakpoint-builtin) for details.
		- Provided by friend of the show Anthony Shaw
  - `monkeypatch` now supports a `context()` function which acts as a context manager which undoes all patching done within the `with` block.
  - whitespace only diffs in failed assertions include escaped characters to be easier to read.
  - plus more… see [changelog](https://docs.pytest.org/en/latest/changelog.html#pytest-3-6-0-2018-05-23)

**Michael #2: Hello** [**Qt for Python**](https://blog.qt.io/blog/2018/05/04/hello-qt-for-python/)

- The first Qt for Python technology preview release is almost here, and for this reason we want to give a brief example on how it will open the doors to the Python world.
- The real question is: how to access the methods of a Qt class? To simplify the process, we kept Qt APIs. (basically change -> to . in the API)
- Can it be more pythonic? “We want to include more Python flavor features to Qt for Python in the near future, but at the moment we are focusing on the TP.”
- The wheels situation: we are planning a set of wheels for Linux, macOS and Windows for 64bit and a 32bit version only for windows. 
- AFAIK, this is Pyside2 reborn

**Brian #3:** [**MongoDB 4.0.0-rc0 available**](https://groups.google.com/forum/m/#!msg/mongodb-user/UWIPZEAKYiw/C5twgBwrCwAJ)

- MongoDB 4.0.0-rc0, the first release candidate of MongoDB 4.0, is out and is ready for testing. 
	- Multi-document ACID transactions
	- Non-Blocking Secondary Reads
	- lots of other goodies, see [announcement](http://MongoDB 4.0.0-rc0, the first release candidate of MongoDB 4.0, is out and is ready for testing.)
	- Did we mention [Transactions](https://www.mongodb.com/transactions)!

**Michael #4:** [**Pipenv review, after using it in production**](https://medium.com/@DJetelina/pipenv-review-after-using-in-production-a05e7176f3f0)

- Nice summary:
  “The current state of python’s packaging is awful, I don’t think there’s anyone who could disagree with that. This problem is recognized and there are many attempts at trying to solve the mess. Pipenv was the first and it has gained a lot of traction, however it doesn’t sit well with everyone. And it’s also not suited for every project — like libraries.”
- The multiple environment problem:
  The tl;dr is — supporting multiple environments goes against Pipenv’s (therefore also Pipfile’s) philosophy of deterministic reproducible application environments. So if you want to use Pipenvfor a library, you’re out of luck. That means many projects just can not use Pipenv for their dependency managment.
- The good
	- Pipfile and Pipfile.lock really are superior to requirements.txt. By a ton.
	- While I disliked it at first, having flake8 and security check builtin in a single tool is great
	- Installing (exclusively) from a private respository works very well. Instead of replacing a dotfile somewhere in the system, specifying the repository in Pipfile is great
	- Creating a new Pipfile is very easy
	- No problems introducing Pipenv to it’s new users
	- No problems installing from a mixture of indexes, git repositores…
	- With --sequential it is actually deterministic, as advertised
	- Virtualenv is much easier to get into and understand
	- Dependencies can be installed into system (e.g. in Docker) — our case.
	- At no point did anyone in the team even mentioned getting rid of Pipenv — which is a lot better than it sounds
- Related:
	- [PyCon 2018 talk about the history and future of Python packaging, including pipenv](https://www.youtube.com/watch?v=GBQAKldqgZs).
	- [Recent changes to the official wording around pipenv](https://github.com/pypa/pipenv/commit/71bf8e51300abe5c57117cc47fba1807cd4465fa#diff-88b99bb28683bd5b7e3a204826ead112) (removes the statement that it’s the official way of managing **application** dependencies)

**Brian** **#5:** [**15 Tips to Enhance your Github Flow**](https://hackernoon.com/15-tips-to-enhance-your-github-flow-6af7ceb0d8a3)

- using github projects to prioritize issues and track progress
- using tags on issues
- templates
- using hub and git-extras on command line
- commit message standards
- scoped commits
- style standards with pre-commit hooks
- automated tests and checks on pull requests
- protect master branch
- requiring code reviews
- squash pull requests
- …. more great topics

**Michael #6:** [**Pandas goes Python 3 only**](https://twitter.com/randal_olson/status/985215366891646976)

- Via Randy Olseon
- It's official: Starting January 1, 2019, pandas will drop support for #Python 2. This includes no backports of security or bug fixes. 
- Basically following NumPy’s lead
- The final release before **December 31, 2018** will be the last release to support Python 2. The released package will continue to be available on PyPI and through conda.
- Starting **January 1, 2019**, all releases will be Python 3 only.

**Our news**

- It’s GDPR eve, are you ready? 
- Need a GDPR laugh? See [https://twitter.com/nadimpatel_/status/999111866633871361](https://twitter.com/nadimpatel_/status/999111866633871361)
- XKCD Python Environments: [https://xkcd.com/1987/](https://xkcd.com/1987/) 


