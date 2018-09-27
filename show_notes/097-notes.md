# Python Bytes 97
Sponsored by DataDog -- [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Making a PyPI-friendly README**](https://packaging.python.org/guides/making-a-pypi-friendly-readme/)

- twine now checks for rendering problems with README
1. Install the latest version of [twine](https://github.com/pypa/twine); version 1.12.0 or higher is required: `pip install --upgrade twine`
2. Build the sdist and wheel for your project as described under [Packaging your project](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project).
3. Run `twine check` on the sdist and wheel: `twine check dist/*`
1. This command will report any problems rendering your README. If your markup renders fine, the command will output `Checking distribution FILENAME: Passed`.

**Michael #2:** [**Java goes paid**](https://www.theregister.co.uk/2018/06/22/oracle_java_se_subscriptions/)

- Oracle's new Java SE subs: Code and support for $25/processor/month
- Prepare for audit after inevitable change, says Oracle licensing consultant
- There’s also a little bit of stick to go with the carrot, because come January 2019 Java SE 8 on the desktop won’t be updated any more … unless you buy a sub.
- The short version is that every commercial enterprise needs to look at their Java SE (Standard Edition) usage to see if they need to do something with licensing.

**Brian #3:** [**Absolute vs Relative Imports in Python**](https://realpython.com/absolute-vs-relative-python-imports/)

- Review of how imports are used, along with subpackages  and `from`
	- ex: `from package.sub import func`
- Relative: what does this mean:

```
from .some_module import some_class
from ..some_package import some_function
from . import some_class
```

**Michael #4:** [**pyxel - A retro game engine for Python**](https://github.com/kitao/pyxel) 

- Thanks to its simple specifications inspired by retro gaming consoles, such as only 16 colors can be displayed and only 4 sounds can be played back at the same time, you can feel free to enjoy making pixel art style games.
- Run on Windows, Mac, and Linux
- Code writing with Python3
- After installing Pyxel, the examples of Pyxel will be copied to the current directory with the following command: `install_pyxel_examples` 

**Brian #5:** [**Click 7.0 Released**](https://palletsprojects.com/blog/click-7-0-released/)

- [Changelog](https://click.palletsprojects.com/en/master/changelog/#version-7-0)
- Drop support for Python 2.6 and 3.3.
- Add native ZSH autocompletion support. 
- Usage errors now hint at the `--help` option
- Really long list of changes since the last release at the beginning of 2017

**Michael #6:** [**How we spent 30k USD in Firebase in less than 72 hours**](https://hackernoon.com/how-we-spent-30k-usd-in-firebase-in-less-than-72-hours-307490bd24d)

- the largest crowdfunding campaign in Colombia, collecting 3 times more than the previous record so far in only two days!
- Run on the Vaki platform -- subject of this article
- We had reached more than 2 million sessions, more than 20 million pages visited and received more than 15 thousand supports. This averages to a thousand users active on the site in average and collecting more than 20 supports per minute.
- Site was running slow, tried things like upgraded the frontend frameworks 
- Logged into Firebase: had spent $30,356.56 USD in just 72 hours! Going at $600/hr
- All came down to a very bad implementation of `this.loadPayments()`.
- Comments are interesting
- It could happen to any of us, it happened to me this month.

Extras:

- [**Dropbox has upgraded from Python 2 → 3**](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/)!
- Michael’s async course is live: [**Async Techniques and Examples in Python**](https://training.talkpython.fm/courses/explore_async_python/async-in-python-with-threading-and-multiprocessing)
- [**2019 PyCon CFPs open**](https://us.pycon.org/2019/speaking/)
- [PyCascades CFP is open until mid-Oct](https://2019.pycascades.com/)



