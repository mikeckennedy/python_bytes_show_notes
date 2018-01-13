# Python Bytes 60
Brought to you by Datadog [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Brian #1:** [**Who's at nine?**](https://www.youtube.com/watch?v=Qu76Xlq2J0k&feature=youtu.be)

- Organic Idiocy
- Inspired by [Michael talking about programming Alexa in episode 33](https://pythonbytes.fm/episodes/show/33/you-should-build-an-alexa-skill)
  - [Twitter thread](https://twitter.com/GregQuinlan/status/950138396445376513)
- Using 
	- [Flask-Ask](http://flask-ask.readthedocs.io/en/latest/) for Alexa
	- [Flask-Assistant](http://flask-assistant.readthedocs.io/en/latest/) for Google Home
- [Talk Python 146](https://talkpython.fm/146) is all about Flask Ask and Assistant this week. ;)

**Michael #2:** [**Retiring Python as a teaching language**](http://prog21.dadgum.com/203.html)

- Why did he write this?
	- Then one day a student will innocently ask "Instead of running the poker simulator from the command line, how can I put it in a window with a button to deal the next hand?"
- The ensuing Twitter conversation was very interesting. Scroll this status, it’s pretty comprehensive [https://twitter.com/mkennedy/status/949688651058835456](https://twitter.com/mkennedy/status/949688651058835456)

**Brian #3:** **Don't dismiss SQLite as just a starter DB**

- SQLite is a single file db that [comes with Python](https://docs.python.org/3.6/library/sqlite3.html).
- A listener pointed us to a couple cool things about SQLite
- A great interview with the developer [The Changelog, episode 201](https://changelog.com/podcast/201).
- It's extensive documentation on how [SQLite is tested](http://sqlite.org/testing.html).
- Of course, for web applications and other applications that have to deal with extreme concurrency, you need a client server database 
- Many applications don't have extreme concurrency needs.
- Sticking with SQLite might be just fine for quite a long time for many apps.

**Michael #4:** [**Chalice: Python Serverless Microframework for AWS**](https://github.com/aws/chalice)

- Chalice is a python serverless microframework for AWS. It allows you to quickly create and deploy applications that use Amazon API Gateway and AWS Lambda. 
- It provides:
	- A command line tool for creating, deploying, and managing your app
	- A familiar and easy to use API for declaring views in python code (Flask)
	- Automatic IAM policy generation
- Compare to Zappa: [https://github.com/Miserlou/Zappa](https://github.com/Miserlou/Zappa)

**Brian #5:** [**Fastest way to uniquely a list in Python >=3.6**](https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6)

- Nice analysis of different ways to uniquify a list.
- Punchline:
	- The fastest way to uniqify a list of hashable objects (basically immutable things) is: `list(set(seq))`
	- And the fastest way, if the order is important is: `list(dict.fromkeys(seq))`

**Michael #6: PyTexas and PyCon AU vidoes are up**

- [PyTexas](https://www.youtube.com/playlist?list=PL0MRiRrXAvRiwQUUwTTh5g8rhbQyYlubo)
	- Notable PyTexas videos
		- Micropython
		- What is ML?
		- C for yourself
		- Python and .NET
- [PyCon AU](http://pyvideo.org/events/pycon-au-2017.html)
	- Notable PyCon AU videos
		- Gradual typing
		- Hot reloading Python web-servers at scale 
		- Prototyping Python Microservices in Production 
		- Secrets of a WSGI master. 
		- Python 3 for People Who Haven't Been Paying Attention 
		- Identity 2.0: the what, why and how of social and federated login 
		- Python: Ludicrous mode (with Django) 
		- Scaling Down: Running Large Sites Locally 

**Our news**

Michael

[**Mastering PyCharm is out**](https://training.talkpython.fm/courses/explore_pycharm/mastering-pycharm-ide). Includes

- Learn to manage Python projects in PyCharm (large and small)
- Create web applications (Pyramid, Flask, Django, and more)
- Use PyCharm's special data science mode
- Refactor your Python code with confidence
- Learn about code smells and duplicate code tooling
- Access git, github, and use git flow
- Use the visual debugger to understand code flow and state
- Make your code more reliable with unit testing and pytest
- Create new Python packages
- And lots more

Webcast with JetBrains: [**MongoDB Quickstart with Python and PyCharm**](https://info.jetbrains.com/PyCharm-Webinar-January2018.html) **Jan 30**


