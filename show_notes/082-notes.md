# Python Bytes 82
DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

** GitHub coverage coming at the end! **

**Brian #1:** [**Building and Documenting Python REST APIs With Flask and Connexion**](https://realpython.com/flask-connexion-rest-api/)

- **Doug Farrell, [@writeson](https://twitter.com/writeson), on the RealPython site.**
- Tutorial with example.
	- REST explanation of what REST is and is not
	- [Swagger](https://swagger.io/), swagger.yml to define API
	- Use [Connexion](https://github.com/zalando/connexion) to incorporate swagger.yml into Flask app.
	- Nice succinct explanation of swagger and API configuration.
	- Demo of Swagger UI for API documentation.
	- JavaScript included for MVC implementation.

**Michael #2:** [**MyPy + PyCharm**](https://twitter.com/gvanrossum/status/1001869119937961984)

- Written by Ivan Levkivskyi
- via Guido van Rossum
- Ricky Teachey asks: “What advantages does using mypy bring to pycharm vs just using pycharm's native type checking- which is already pretty good?”
- Response: 
	- mypy is a bit more stricter/precise
	- it is more configurable, lots of options regulating type system "rules"
	- it typechecks the whole program, so that you immediately see errors your change causes in _other_ files
	- people run mypy in CI and want to see the result before push

**Brian #3: Automatic code/doc conversion**

- [pyupgrade](https://github.com/asottile/pyupgrade/blob/master/README.md)
	- “A tool (and pre-commit hook) to automatically upgrade syntax for newer versions of the language.”
	- Can even convert to f-strings with `--py36-plus` option.
- [docs](https://github.com/asottile/blacken-docs)
	- “Run `black` on python code blocks in documentation files.”
	- blacken-docs provides a single executable (blacken-docs) which will modify .rst / .md files in place.

**Michael #4:** [**python3statement**](https://twitter.com/Mbussonn/status/1004177424488132608)

- via Bruno Alla
- Matthias Bussonnier (Talk Python, [episode 44](https://talkpython.fm/episodes/show/44/project-jupyter-and-ipython))
	- *“We now have 44 projects that pledged to drop #python2 in less than 30 months. Some already did ! To see which one, and how to migrate with as few disruption as possible for both Python 2 and 3 users head to http://python3statement.org/ ”*
- Supporting legacy Python: **it is a small but constant friction in the development of a lot of code.
- We are keen to use Python 3 to its full potential, and we currently accept the cost of writing cross-compatible code to allow a smooth transition, but we don’t intend to maintain this compatibility indefinitely. 
- Nice “Why switch to Python 3?” section and resources
- Nice list of participating projects
	- Can we get some that are not data science? :)

**Microsoft buys GitHub**:

- [Everyone complaining about Microsoft buying GitHub needs to offer a better solution](https://arstechnica.com/gadgets/2018/06/everyone-complaining-about-microsoft-buying-github-needs-to-offer-a-better-solution/?comments=1&unread=1)
- [Microsoft to acquire GitHub for $7.5 billion](https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/)
- [Linux Foundation: Microsoft's GitHub buy is a win for open source](https://www.linuxfoundation.org/blog/microsoft-buys-github-the-linux-foundations-reaction/?SSAID=389818)
- Coverage on Exponent podcast: [154 — Legacy Leverage](https://overcast.fm/+BihnqmtgQ)
- [Nat Friedman, future CEO of GitHub, AMA](https://www.reddit.com/r/AMA/comments/8pc8mf/im_nat_friedman_future_ceo_of_github_ama/?utm_source=amp&utm_medium=comment_list)
- Re gitlab:
	- [GitLab congratulates GitHub and Microsoft](https://about.gitlab.com/2018/06/03/microsoft-acquires-github/)
	- [GitLab imports from GitHub going up](https://twitter.com/gitlab/status/1004143715844124673)


Our news and extras:

- PyLadies Cleveland just launched:
	- First meeting June 26
	- (FB Profile) [https://www.facebook.com/cleveland.pyladies.3](https://www.facebook.com/cleveland.pyladies.3)
	- (FB Community Page) [https://www.facebook.com/clepyladies/](https://www.facebook.com/clepyladies/)
	- (Twitter) [https://twitter.com/CLEPyladies](https://twitter.com/CLEPyladies)
	- (Meetup) [https://www.meetup.com/CLE-PyLadies/](https://www.meetup.com/CLE-PyLadies/)
	- (YouTube) [https://www.youtube.com/channel/UCrX6AAcxXO_-8gitJWdjkuw](https://www.youtube.com/channel/UCrX6AAcxXO_-8gitJWdjkuw)

