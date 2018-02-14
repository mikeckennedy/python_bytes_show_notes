# Python Bytes 65
Sponsored by Rollbar: [pythonbytes.fm/rollbar](https://pythonbytes.fm/rollbar)

**Brian #1:** [**pygal**](http://pygal.org/en/stable/) **: Simple Python Charting** 

- Output SVG or PNG
- Example Flask App (also django response) part of documentation.
- Enough other bits of doc to get you a chart in a web page super fast.

**Michael #2:** [**Thoughts on becoming a self-taught programming**](https://www.reddit.com/r/learnprogramming/comments/7udoiv/how_many_of_you_selfstudied_programming_and_are/)

-  Basic format:
- I'm 31 days into self-studying Python and am loving every minute of it!
- A few questions:
	- What were you doing before you began self-studying programming?
	- What made you want to study programming on your own?
	- How did you start (which resources and language)?
	- How long did it take for you to feel confident enough in your skills and knowledge to know you could be employed as a programmer?
	- What else did you do besides self-study that helped you in your journey to becoming a programmer?
	- What's next for you?

**Brian #3:** [**How to speed up Python application startup time (timing imports in 3.7)**](https://dev.to/methane/how-to-speed-up-python-application-startup-time-nkf)

- Python 3.7 includes `-X importtime` option that allows you to profile the time it takes to do all the imports.
- Way cool tool to help optimize the startup time of an application.

**Michael #4:** [AnPyLar - The Python web front-end framework](https://www.anpylar.com/)

- Create web applications with elegance, simplicity and yet full power with Python and components
- MISSION: Empower all Python programmers to work not only on the back-end but also on the front-end with the same language of choice
- Features
	- Reactive programming and Promises
	- Python standard formatting as templates
	- reusable components
	- Scoped styling for component
	- Integrated routing engine

**Brian #5:** [**Migrating to Python 3 with pleasure**](https://github.com/arogozhnikov/python3_with_pleasure/blob/master/README.md)

- **“A short guide on features of Python 3 for data scientists”**
- Quick tutorial through examples of `pathlib`.
- Type hinting and how cool it works with editors (PyCharm example shown)
- Adding runtime type enforcement for specific methods using [enforce](https://github.com/RussBaz/enforce)
- Using function annotations for units, as done in [`astropy`](http://docs.astropy.org/en/stable/units/quantity.html#functions-that-accept-quantities). 
- Matrix multiplication with `@`.
- Globbing with `**`. 
	- `found_images = glob.glob('/path/**/*.jpg', recursive=True)`
- Also … underscores in numeric literals, f-strings, true division with `/`, integer division with `//`, and lots of more fun goodies.

**Michael #6:** [**Moving to Python 3**](https://engineering.ticketea.com/ticketea-migrates-python3-in-two-weeks/)

- Many of these issues were corrected just by running 2to3, which not only fixed many of the compatibility issues
	- Outdated external libraries which needed to be updated to newer versions featuring Python 3 compatibility
    `basestring` to `str`, `urlparse` to `urllib.urlparse` and similar major changes
	- Dictionary change like `iteritems()` to `items()`, or `.items()` now returning a view.
	- Things that weren't needed anymore, like Django's `force_unicode` or `__future__` library tools.
- Once we finished working on the "low-hanging fruits", the next step was to run Aphrodite's test suite and achieve zero errors.
- Lessons learned
	- Code coverage was originally around 70%,
	- Keeping the Python 3 branch up to date with master
	- A non-trivial feature was delivered during the migration (via feature branch)
	- The pickle protocol version in python 3 can be higher than the highest available in Python 2.7. So we needed to add versioning to our Django caches
	- Each modified file had to comply with flake8 linting rules
- Afrodita is currently running on Google App Engine Flexible, and one of the features our team loves with is traffic splitting
- With this feature, we can do [canary releases](https://martinfowler.com/bliki/CanaryRelease.html) with ease: We just deploy our new version of the service, and start redirecting small amounts of traffic traffic while we monitor for unexpected errors.
- After some minor bugfixes, we could bring the traffic of the Python 3.6 version to 100% with confidence. We also had the old version available for instant rollback, thanks to how parallel versions and traffic splitting work in GAE flexible.

**Our news**

Brian:

- Upcoming webinar: [Productive pytest with Pycharm](https://blog.jetbrains.com/pycharm/2018/02/webinar-productive-pytest-with-pycharm-with-brian-okken/)

Michael:

- My GUI example: [https://github.com/mikeckennedy/pyramid-web-builder-python-gui](https://github.com/mikeckennedy/pyramid-web-builder-python-gui)




