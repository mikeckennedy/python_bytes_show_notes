# Python Bytes 72
Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**ZeroVer: 0-based Versioning**](https://0ver.org/)

- “Software's most popular versioning scheme!”
- “*Cutting-edge software versioning for minimalists”*
- My favorite April Fools prank this year.
  - Calls out many popular projects for never reaching 1.0
- From the about page: 
	- “ZeroVer is the world's most popular software versioning convention, and the only one shown to harness the innovative power of zero. The benefits are innumerable and the effects on the software world are profound.”
	- “Version 0.0.1 of ZeroVer was published by [Mahmoud Hashemi](https://github.com/mahmoud/), with help from Moshe, Mark, Kurt, and other patient collaborators, on 2018-04-01. ZeroVer is satire, [please do not use it](https://en.wikipedia.org/wiki/Poe%27s_law). We sincerely hope no project release schedules were harmed as a result of this humble attempt at programmer humor.”

**Michael #2:** [**GitHub Security Alerts Detected over Four Million Vulnerabilities**](https://www.infoq.com/news/2018/03/github-vulnerability-alerts-resp)

- Last year GitHub launched “GitHub security alerts”
- GitHub’s security alerts notify repository admins when library vulnerabilities from the Common Vulnerabilities and Exposures (CVEs) list are detected in their repositories. 
- Nearly half of all displayed alerts are responded to within a week and the rate of vulnerabilities resolved in the first seven days has been about 30%. 
- When that statistics is restricted to only repositories with recent contributions, i.e., contributions in the last 90 days, things look even brighter, GitHub says, with 98% of such repositories being patched in fewer than seven days. 
- More than four million vulnerabilities in over 500,000 repositories have been reported.
- Security alerts are only currently supported for repositories written in Ruby or JavaScript, while support for Python is planned for 2018.
- I also recommend [pyup.io](http://pyup.io)

**Brian #3:** [**Markdown Descriptions on PyPI**](https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi)

- Dustin Ingram provides detailed steps on how to get this to work.
- README.md now supported by pypi.org
	- “Only [https://pypi.org](https://pypi.org/) will correctly render your new Markdown description.
	- Legacy PyPI ([http://pypi.python.org/](http://pypi.python.org/)) will still render your description as plaintext, but don’t worry, [it’s going away real soon](https://wiki.python.org/psf/WarehouseRoadmap).
- And also,  [Github-Flavored Markdown Descriptions are supported](http://blog.jonparrott.com/github-flavored-markdown-on-pypi/).
  - Another post, this one by Jon Wayne Parrot

**Michael #4:** [**Concurrency comparison between NGINX-unit and uWSGI**](https://itnext.io/performance-comparison-between-nginx-unit-and-uwsgi-python3-4511fc172a4c)

- show performance of two web application servers 
	- nginx-unit (a new modern application web server)
	- uWSGI (the best one application server)
- uWSGI and nginx-unit configured with 4 workers because test system has 4 cores.
- Effectively an empty “Hello world” Flask app
- Have a look at the pictures here: https://itnext.io/performance-comparison-between-nginx-unit-and-uwsgi-python3-4511fc172a4c
- Take away: I’m going to start paying attention to NGINX-unit

**Brian #5:** [**Loop better: A deeper look at iteration in Python**](https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python)

- via Trey Hunner
- Generators are a great way to loop, but have a few gotchas
	- Looping twice doesn’t work
	- Containment checks muck up the generator “contents”.
	- Unpacking has odd results.
- This article describes Python loops in detail and then applies that do describe why the gotchas act like they do.
- Covered:
	- iterators, iterables, sequences, generators
	- the iterator protocol
- Reading this will make you a better programmer, but might hurt your head.

**Michael #6:** [**Misconfigured Django Apps Are Exposing Secret API Keys, Database Passwords**](https://www.bleepingcomputer.com/news/security/misconfigured-django-apps-are-exposing-secret-api-keys-database-passwords/)

- Security researchers have been stumbling upon misconfigured Django applications that are exposing sensitive information such as API keys, server passwords, or AWS access tokens.
- He discovered 28,165 Django apps just this week where admins left debug mode enabled.
- Just by skimming through a few of the servers, the researcher found that the debug mode of many of these apps were exposing extremely sensitive information that would have allowed a malicious actor full access to the app owner's data. 
- This is **not a failure from Django's side**. My recommendation is to disable debugging mode when deploying the application to production.
- Security researcher Victor Gevers said some of the servers running Django apps have already been compromised.
- He found at least one compromised server, running the Weevely web shell. Some servers Gevers found leaking sensitive data belonged to various government agencies carrying out critical operations.
- Gevers said he started notifying servers owners about their leaky Django apps. "At this moment we have reported 1,822 servers," Gevers said. "143 were fixed or taken offline."

**Extra:**

- We covered wagtail on [episode 70](https://pythonbytes.fm/70). They are running [a kickstarter campaign](https://www.kickstarter.com/projects/noripyt/wagtails-first-hatch) to get some new features out. There’s a video there.

