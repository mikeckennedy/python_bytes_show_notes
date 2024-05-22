Sponsored by Datadog: [**pythonbytes.**](https://pythonbytes.fm/datadog)[**fm**](https://pythonbytes.fm/datadog)[**/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Unlearning toxic behaviors in a code review culture**](https://medium.freecodecamp.org/unlearning-toxic-behaviors-in-a-code-review-culture-b7c295452a3c)

- unhelpful behaviors:
	- passing off opinion as fact
	- overwhelming with an avalanche of comments
	- asking people to fix problems they didn’t cause “while they’re at it”.
	- asking judgmental questions
	- being sarcastic
	- using emojis
	- not replying to comments
	- ignoring (not calling out) toxic behavior from high performers
- helpful:
	- use questions or recommendations to drive dialog
	- collaborate, don’t back-seat drive
	- respond to every comment
	- know when to take a discussion offline
	- use opportunities to teach, and don’t show off
	- don’t show surprise of lack of knowledge by others
	- automate what can be
	- refuse to normalize toxic behavior
	- managers: hire carefully, listen to your team, and enforce
	- set the standard as your team is small and growing
	- understand you might be part of the problem

**Michael #2:** [Flask 1.0 Released](https://www.palletsprojects.com/blog/flask-1-0-released/)

  - Dropped support for Python 2.6 and 3.3.
  - The CLI is more flexible. `FLASK_APP` can point to an app factory, optionally with arguments. It understands import names in more cases where filenames were previously used. It automatically detects common filenames, app names, and factory names. `FLASK_ENV` describes the environment the app is running in, like `development`, and replaces `FLASK_DEBUG` in most cases. [See the docs to learn more.](http://flask.pocoo.org/docs/1.0/cli/)
  - If python-dotenv is installed, the `flask` CLI will load environment variables from `.flaskenv` and `.env` files rather than having to export them in each new terminal.
  - The development server is multi-threaded by default to handle concurrent requests during development.
  - flask.ext, which was previously deprecated, is completely removed. Import extensions by their actual package names.
  - Accessing missing keys from `request.form` shows a more helpful error message in debug mode, addressing a very common source of confusion for developers.
  - Error handlers are looked up by code then exception class, on the blueprint then application. This gives more predictable control over handlers, including being able to handle `HTTPException`.
  - The behavior of `app.logger` has been greatly simplified and should be much easier to customize. The logger is always named `flask.app`, it only adds a handler if none are registered, and it never removes existing handlers. [See the docs to learn more.](http://flask.pocoo.org/docs/1.0/logging/)
  - The `test_client` gained a `json` argument for posting JSON data, and the `Response` object gained a `get_json` method to decode the data as JSON in tests.
  - A new `test_cli_runner` is added for testing an app's CLI commands.
  - Many documentation sections have been rewritten to improve clarity and relevance. This is an ongoing effort.
  - The [tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) and corresponding [example](https://github.com/pallets/flask/tree/1.0/examples/tutorial) have been rewritten. They use a structured layout and go into more detail about each aspect in order to help new users avoid common issues and become comfortable with Flask.
- There are many more changes throughout the framework. [Read the full](http://flask.pocoo.org/docs/1.0/changelog/) 

**Brian** **#3:** **So, I still don’t quite get pipenv, ….**

- Best discussion of why pipenv is useful for applications I’ve come across so far is [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/)
- Starts with a discussion of situations where `pip`, `pip freeze`, and `requirements.txt` fall apart.
	- `requirements.txt` often just have an applications direct dependencies, not sub-dependencies.
	- `pip freeze > requirements.txt` will pin your versions to specific versions, but then you’ve got to keep track of dependencies and sub-dependencies.
	- `Pipfile` intends to replace `requirements.txt`, with a simple-ish human readable format. Also includes extra things like dev environment support.
	- `Pipfile.lock` intends to replace pinned `requirements.txt` files. Also includes hashes to validate versions haven’t been corrupted.
	- `pipenv` also includes cool tools like dependency graphing, checking for updates, etc.
- `pipenv` should be used for applications, but not packages intended to be included in other applications. But you can use it during package development, just probably not include the Pipfile and Pipfile.lock in the repo or package distribution. - Brian’s comment

Bonus extra: 

- [cookiecutter-pipenv: Cookiecutter Python Package Template with Pipenv](https://github.com/elgertam/cookiecutter-pipenv) 

**Michael #4**[**:**](https://edgedb.com/blog/edgedb-a-new-beginning) [GraalVM: Run Programs Faster Anywhere](https://blogs.oracle.com/developers/announcing-graalvm)

- Why?
	- Current production virtual machines (VMs) provide high performance execution of programs only for a specific language or a very small set of languages.
	- Compilation, memory management, and tooling are maintained separately for different languages, violating the ‘don’t repeat yourself’ (DRY) principle.
	- high performance VMs are heavyweight processes with high memory footprint and difficult to embed.
- Oracle Labs started a new research project for exploring a novel architecture for virtual machines. Our vision was to create a single VM that would provide high performance for all programming languages, therefore facilitating communication between programs.
- Released: [GraalVM](http://www.graalvm.org/), a universal virtual machine designed for a polyglot world.
- GraalVM provides high performance for individual languages and interoperability with zero performance overhead for creating polyglot applications.
- GraalVM 1.0 allows you to run:
	- JVM-based languages like Java, Scala, Groovy, or Kotlin
	- JavaScript (including Node.js)
	- LLVM bitcode (created from programs written in e.g. C, C++, or Rust)
	- Experimental versions of Ruby, R, and **Python**
- Future: This first release is only the beginning. We are working on improving all aspects of GraalVM; in particular the support for Python

**Brian** **#5:** [**Testing a Flask Application using pytest**](http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)

- Small demo project, and article, that teaches the use of pytest in Flask.
- unit testing and functional testing
- Article covers testing models, with an example of a new user.
- project also has examples of using a test client to check the login page, password authentication, and a lot more.
- Very cool project.

**Bonus:** [**A cool new pytest plugin: pytest-caprng**](https://github.com/jbn/pytest-caprng)

- Tests that use `random` or `np.random` may fail, but when you re-run them, they don’t fail, which makes them hard to debug.
- This plugin adds pytest flags `--caprng-global-stdlib` and `--caprng-global-np`, which saves the random state before each test so that if you re-run the test, the random-ness is not so random, and you can reproduce your failure.
- Also, thanks John for reminding me what “stochastic” means.
  
**Michael #6:** [How to have a great first PyCon](http://treyhunner.com/2018/04/how-to-make-the-most-of-your-first-pycon/)

- Spending your time: which talks should I go to? The talks at PyCon are typically uploaded to YouTube within 24 hours after the talk ends. I am suggesting that you don’t need to worry about attending every talk.
- Open spaces: attend them and consider hosting your own! 
- There are a few reasons I often pick open spaces over talks:
	- Often the open spaces are more niche and topical than the talks: there are some subjects that exist in open spaces every year but which I’ve never seen a talk on
	- Open spaces are all about interaction and discussion whereas talks are a monologue that often evolves into subsequent dialogues
	- Open spaces aren’t recorded whereas the talks are, meaning you can’t really catch up on them later
- Tips for starting conversation, breakfast and lunch time…
- The hallway track 👣
	- Something you might consider doing while at PyCon is taking breaks in the hallway. 
	- In addition to joining or starting a table in the hallway, consider identifying groups that have [a PacMan opening](http://ericholscher.com/blog/2017/aug/2/pacman-rule-conferences/) to join and make sure the groups you’re in are PacMan-friendly.
- Interacting online during PyCon 🐦
	- I recommend getting a Twitter account to make it easier to passively keep up with folks from PyCon after the conference ends.
	- Sometimes people on Twitter will ask if anyone would like to join them for dinner and you might decide to reply and say you’d like to join.
- Networking isn’t a dirty word: it means making friends 👥
- I hear two opposing concerns sometimes expressed about PyCon:
	- Isn’t everyone here to get a job or hire people?
	- Is it acceptable to go to PyCon looking for a job?
	- PyCon is a networking event. That doesn’t necessarily mean everyone is there to get a job, but it also definitely doesn’t mean it’s unacceptable to job-seek at Python.
- Other topics include
	- Volunteering
	- Evening events: dinners and board games
	- Give a lightning talk ⚡
	- Take care of yourself
- Final tip from commentor: If you are on windows, it's helpful to install a virtual image of a linux like the current ubuntu on your laptop, because you could run into situations where you want to follow a talk / training which doesn't work on windows and then you're missing a great opportunity to learn.

**Our news**

- Come see us at PyCon!!! We’ll have stickers! 
- Brian’s talk is Friday at 5 something. 
- We are doing a live Python Bytes open session, join “friends of the show” to get notified
- I’ll be at Microsoft BUILD too
- PyGotham 2018 Call for Proposals
- [http://PyCon.DE](http://PyCon.DE)  (24-26 October 2018 in Karlsruhe, Germany) starting our CfP tomorrow until May 20. [http://de.pycon.org](http://de.pycon.org)

