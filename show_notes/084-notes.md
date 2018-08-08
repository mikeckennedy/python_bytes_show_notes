# Python Bytes 84
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest [Nina Zakharenko](http://nnja.io) ([@nnja](http://twitter.com/nnja)) is a Cloud Developer Advocate at Microsoft!

**Brian #1:** [**Correcting Documentation for a Deployed Python Package**](https://www.loganasherjones.com/2018/06/correcting-documentation-for-a-deployed-python-package/)

- "A clever way to release new documentation without releasing a new package that might confuse your user base.”
- Upload changes to pypi without bumping the version by using post release version numbers: `0.3.2` => `0.3.2.post1`
- Prevent documentation issues by using `restview --long-description` before uploading. (or use md and really any md converter)

Also:

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) : revamped pypa tutorial that works pretty darned well.
- [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/) : more detailed instructions on testing with TestPyPI before pushing to final spot.

**Nina #2:** [**Flask Mega Tutorial**](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

- Amazing resource for developers who’d like to learn about building web applications with Flask in Python.
- Covers important topics like databases, internationalization, and dates and times. 
- Three full sections on deploying your web app using Linux, Heroku, or containers. 
- [VS Code IDE has great Flask support](https://aka.ms/pythonbytes-vscodeflask).
- Try Azure with a [$200 credit to deploy Flask apps](http://aka.ms/azurepythonbytes).

**Michael** **#3:** [**10 common security gotchas in Python and how to avoid them**](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03)

- Article by Anthony Shaw (congrats on being a 2018 PSF Fellow)
- The 10 topics 
	- Input injection (see [little bobby tables](https://xkcd.com/327/))
	- Use an ORM (db) or shlex module to escape input correctly (process)
	- Parsing XML
	- Assert statements
	- Timing attacks
	- A polluted site-packages or import path
	- Temporary files
	- Using yaml.load
	- Pickles
	- Using the system Python runtime and not patching it
	- Not patching your dependencies

**Brian #4:** [**pre-commit**](https://pre-commit.com/)
“A framework for managing and maintaining multi-language pre-commit hooks.”

- Describe pre-commit actions using yaml.
- Lots of projects already use it, like black. 
- Does the work for you so you don’t have to read up on git commit hooks and such.
- Test out hooks ahead of time with `pre-commit run <hook id>`

**Nina #5: Python 3.7 release and PSF board members**

- Python 3.7 has just been released today! 🎉
- [New Features Overview Blog Post](https://realpython.com/python37-new-features/)
- Debugging improvements - new `breakpoint()` built-in function allows you to start an interactive session, like IPython. 
- 4 New PSF Board members elected - Congratulations to them!
	- Anna Ossowski
	- Christopher Neugebauer
	- Jeff Triplett
	- Katie McLaughlin

**Michael #6:** [**Vibora web framework**](https://vibora.io/)

- A new speedy web framework
- Only 14 days old, but has 21 contributors and 2k stars
- Just like Flask: Vibora APIs were heavily inspired by the awesome Flask.
- Schemas validation, template engine, sessions and many more features were written from scratch to provide great performance along with an elegant async interface.
- Vibora also take advantage of multiple CPU cores by default thanks to the multi-processed architecture. Uvloop and other C speed-ups are used when available.
- Virtual Hosts: Maybe you have different domains and you want to host them all with a single Vibora application. 
- Deployment has its own HTTP app server
- Docs need help

Our news and extras:

- [Qt for Python Webinar](https://www.qt.io/qt-for-python)
  - via [Fredrik Averpil](https://twitter.com/fredrikaverpil)
[](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
