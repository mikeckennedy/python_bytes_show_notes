# Python Bytes 117
Sponsored by [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1**: [**Goodbye Virtual Environments?**](https://medium.com/@grassfedcode/goodbye-virtual-environments-b9f8115bc2b6)

- by [Chad Smith](https://medium.com/@grassfedcode)
- venv’s are great but they introduce some problems as well:
	- **Learning curve:** explaining “virtual environments” to people who just want to jump in and code is not always easy
	- **Terminal isolation:** Virtual Environments are activated and deactivated on a per-terminal basis
	- **Cognitive overhead:** Setting up, remembering installation location, activating/deactivating
- [PEP 582 — Python local packages directory](https://www.python.org/dev/peps/pep-0582/)
	- This PEP proposes to add to Python a mechanism to automatically recognize a `__pypackages__`directory and prefer importing packages installed in this location over user or global site-packages. This will avoid the steps to create, activate or deactivate “virtual environments”. Python will use the `__pypackages__` from the base directory of the script when present.
- Try it now with [**pythonloc**](https://github.com/cs01/pythonloc)
	- **pythonloc** is a drop in replacement for `python` and `pip` that automatically recognizes a `__pypackages__` directory and prefers importing packages installed in this location over user or global site-packages. If you are familiar with node, `__pypackages__` works similarly to `node_modules`.
	- Instead of running `python` you run `pythonloc` and the `__pypackages__` path will automatically be searched first for packages. And instead of running `pip` you run `piploc` and it will install/uninstall from `__pypackages__`.

**Michael #2**: [**webassets**](https://webassets.readthedocs.io/en/latest/index.html)

- Bundles and minifies CSS & JS files
- Been doing a lot of work to rank higher on the sites
- That lead me to [**Google’s Lighthouse**](https://developers.google.com/speed/pagespeed/insights)
- Despite 25ms response time to the network, Google thought my site was “kinda slow”, yikes!
- webassets has integration for the big three: Django, Flask, & Pyramid.
	- But I prefer to just generate them and serve them off disk

```
    def build_asset(env: webassets.Environment, 
                   files: List[str], 
                   filters: str, 
                   output: str):
        bundle = webassets.Bundle(
            *files,
            filters=filters,
            output=output,
            env=env
        )
        bundle.build(force=True)
```

**Brian #3**: **Bernat on Python Packaging**

- 3 part series by Bernat Gabor
	- Maintainer of tox and virtualenv Python packages.
- [The State of Python Packaging](https://www.bernat.tech/pep-517-and-python-packaging/)
- [Python packaging - Past, Present, Future](https://www.bernat.tech/pep-517-518/)
- [Python packaging - Growing Pains](https://www.bernat.tech/growing-pain/)

**Michael #4**: [**What the mock? — A cheatsheet for mocking in Python**](https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832)

- Nice introduction
- Some examples

```
    @mock.patch('work.os')
        def test_using_decorator(self, mocked_os):
            work_on()
    mocked_os.getcwd.assert_called_once()
```

And

```
        def test_using_context_manager(self):
            with mock.patch('work.os') as mocked_os:
                work_on()
    mocked_os.getcwd.assert_called_once()
```

**Brian #5**:  [**Transitions: The easiest way to improve your tech talk**](https://medium.com/@saronyitbarek/transitions-the-easiest-way-to-improve-your-tech-talk-ebe4d40a3257)

- By Saron Yitbarek
- Jeff Atwood of CodingHorror noted “The people who can write and communicate effectively are, all too often, the only people who get heard. They get to set the terms of the debate.”
- Effectively presenting is part of effective communication.
- I love the focus of this article. Focused on one little aspect of improving the performance of a tech talk.

**Michael #6**: [**Steering council announced**](https://discuss.python.org/t/2019-steering-council-election-results/824)

- Our new leaders are
	- Barry Warsaw
	- Brett Cannon
	- Carol Willing
	- Guido van Rossum
	- Nick Coghlan
- Via Joe Carey
- We both think it’s great Guido is on the council.

Extras: 

- Brian: Got interviewed on IT Energizer Podcast:
  - The one with Brian: [https://itcareerenergizer.com/e123/](https://itcareerenergizer.com/e123/)
  - The one with Michael: [https://itcareerenergizer.com/e83/](https://itcareerenergizer.com/e83/)
- [PyCon LATAM](https://www.pylatam.org/)
  - August 29, Puerto Vallarta, Mexico
  - We should go. Anyone want to sponsor our travel/hotel to this event?
  - CFP open till May 31, 2019,  [https://www.pylatam.org/en/speaking/](https://www.pylatam.org/en/speaking/)

Joke:

From the list from Ant, my votes. 

- **Q:** What's the second movie about a database engineer called?
  **A:** The SQL.

- **!false**
  It's funny 'cause it's true.

- A programmer's spouse tells them, "Run to the store and pick up a loaf of bread. If they have eggs, get a dozen."
  The programmer comes home with 12 loaves of bread.
