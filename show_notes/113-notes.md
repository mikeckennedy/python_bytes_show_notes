# Python Bytes 113
Sponsored by [https://pythonbytes.fm/digitalocean](https://pythonbytes.fm/datadog)

**Brian #1:** [**Advent of Code 2018 Solutions**](https://www.michaelfogleman.com/aoc18/)

- Michael Fogleman
- Even if you didn’t have time or energy to do the 2018 AoC, you can learn from other peoples solutions. Here’s one set written up in a nice blog post.

**Michael #2:** [**Python Lands on the Windows 10 App Store**](https://www.thurrott.com/windows/windows-10/196830/python-lands-on-the-windows-10-app-store#)

- Python Software Foundation recently released Python 3.7 as an app on the official Windows 10 app store. 
- Python 3.7 is now available to install from the Microsoft Store, meaning you no longer need to manually download and install the app from the official Python website.
- there is one limitation. “Because of restrictions on Microsoft Store apps, Python scripts may not have full write access to shared locations such as TEMP and the registry. 
- Discussed with Steve Dower over on [Talk Python 191](https://talkpython.fm/episodes/show/191/python-s-journey-at-microsoft)

**Brian #3:** [**How I Built A Python Web Framework And Became An Open Source Maintainer**](https://blog.florimondmanca.com/how-i-built-a-web-framework-and-became-an-open-source-maintainer)

- Florimond Manca
- [Bocadillo](https://bocadilloproject.github.io/) - “A modern Python web framework filled with asynchronous salsa”
- ”**maintaining an open source project is a marathon, not a sprint**.”
- Tips at the end of the article include tips for the following topics, including recommendations and tool choices:
	- **Project definition**
	- **Marketing & Communication**
	- **Community**
	- **Project management**
	- **Code quality**
	- **Documentation**
	- **Versioning and releasing**


**Michael #4: Python maintainability score via** [**Wily**](https://github.com/tonybaloney/wily)

- via Anthony Shaw
- A Python application for tracking, reporting on timing and complexity in tests
- Easiest way to calculate it is with wily https://github.com/tonybaloney/wily … the metrics are ‘maintainability.mi’ and ‘maintainability.rank’ for a numeric and the A-F scale.
	- Build an index: wily build src
	- Inspect report: wily report file
	- Graph: wily graph file metric

**Brian #5:** **A couple fun awesome lists**

- [Awesome Python Security resources](https://github.com/guardrailsio/awesome-python-security)
	- Tools
		- web framework hardening, ex: secure.py
		- multi tools
		- static code analysis, ex: bandit
		- vulnerabilities and security advisories
		- cryptography
		- app templates
	- Education
		- lots of resources for learning
	- Companies
- [Awesome Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
	- clean code
	- testing, including 
		- [flake8-pytest](https://github.com/vikingco/flake8-pytest) - Enforces to use `pytest`-style assertions
		- [flake8-mock](https://github.com/aleGpereira/flake8-mock) - Provides checking mock non-existent methods
	- security
	- documentation
	- enhancements
	- copyrights

**Michael #6:** [**fastlogging**](https://brmmm3.github.io/posts/2019/01/08/fastlogging/)

- via Robert Young
- A faster replacement of the standard logging module with a mostly compatible API.
- For a single log file it is ~5x faster and for rotating log file ~13x faster.
- It comes with the following features:
	- (colored, if `colorama` is installed) logging to console
	- logging to file (maximum file size with rotating/history feature can be configured)
	- old log files can be compressed (the compression algorithm can be configured)
	- count same successive messages within a 30s time frame and log only once the message with the counted value.
	- log domains
	- log to different files
	- writing to log files is done in (per file) background threads, if configured
	- configure callback function for custom detection of same successive log messages
	- configure callback function for custom message formatter
	- configure callback function for custom log writer

Extras:

Michael: [My webcast on async](https://www.wintellect.com/webinar/master-pythons-async-features-with-async-and-await/), Jan 24, 11am PT
Michael: [Watch your YAML](https://twitter.com/anthonypjshaw/status/1081297735968378880)! 

Joke: `>>> import antigravity`
