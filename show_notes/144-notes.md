# Python Bytes 144
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

 **Chris #1:** [**Why your mock doesn’t work**](https://nedbatchelder.com//blog/201908/why_your_mock_doesnt_work.html)

- Ned Batchelder
- TDD is an important practice for development, and as my team is finding out, mocking objects is not as easy at it seems at first.
- I love that Ned gives an overview of how Mock works
- But also gives two resources to show you alternatives to Mock, when you really don’t need it.
- From reading these articles and video, I’ve learned that it’s hard to make mocks but it’s important to:
	- Create only one mock for each object you’re mocking
	- that mocks only what you need
	- have tests that run the mock against your code and your mock against the third party 

**Mahmoud #2**: [**Vermin**](https://github.com/netromdk/vermin)

- By Morten Kristensen
- Rules-based Python version compatibility detector
- caniuse is cool, but it’s based on classifiers. When it comes to your own code, it’ll only tell you what you tell it.
- If you’ve got legacy libraries, or like most companies, an application, then you’ll need something more powerful.
- Vermin tells you the minimum compatible Python version, all the way down to the module and even function level.

**Brian #3:** [**The nonlocal statement in Python**](https://blog.araj.me/til-nonlocal-statement-in-python/)

- Abhilash Raj
- When `global` is too big of a hammer.
- This doesn’t work:

```
    def function():
        x = 100
        def incr(y):
            x = x + y
        incr(100)
```

- This does:

```
    def function():
        x = 100
        def incr(y):
            nonlocal x
            x = x + y
        incr(100)
        print(x)
```

**Chris #4:** **[twitter.com/brettsky/status/1163860672762933249](https://twitter.com/brettsky/status/1163860672762933249)**

- Brett Cannon
- Microsoft Azure improves python support
	- 2 key points about the new Python support in Azure Functions: 
		- it's debuting w/ 3.6, but 3.7 support is actively being worked on and 3.8 support won't take nearly as long, and 
		- native async/await support!

**Mahmoud #5**: [**Awesome Python Applications**](https://github.com/mahmoud/awesome-python-applications) update

- Presented at PyBay 2019
- Slides/summary (video forthcoming): [http://sedimental.org/talks.html#ask-the-ecosystem-lessons-from-250-foss-python-applications](http://sedimental.org/talks.html#ask-the-ecosystem-lessons-from-250-foss-python-applications)
- 250+ applications, dating back to 1998 (mailman, gedit)
- 95% of applications have commits in 2019
- 65% of applications support Python 3 (even the ones with a long history!)
- Other interesting findings
- Presenting these findings and more at PyGotham 2019. NYC in early October.

**Brian #6:**  [**pre-commit now has a quick start guide**](https://pre-commit.com/#quick-start)

- Wanna use pre-commit but don’t know how to start? Here ya go!
- Runs through 
	- install
	- configuration
	- installing hooks
	- running hooks against your project
- I’d like to add
	- Add hooks to your project one at a time
	- For each new hook
		- add to `pre-commit-config.yml`
		- run `pre-commit install` to install hook
		- run `pre-commit run`  `--``all-files`
		- review changes made to your project
			- if good, commit
			- if bad
		    - revert
		    - modify config of tools, such as `pyproject.toml` for black, `.flake8` for flake8, etc.
		    - try again

**Extras**

Chris: 
- [Humble Bundle by No Starch supports the Python Software Foundation](http://pyfound.blogspot.com/2019/08/humble-bundle-by-no-starch-supports.html)
- [https://codechalleng.es/](https://codechalleng.es/) released Newbie Bites… challenges that are intended for people brand new to python. [[direct link](https://gumroad.com/l/Xhxeo)]

Mahmoud:
- PyGotham 2019 October (Maintainers Conf in Washington DC, too)
- Real Python Pandas course

Brian:
- [http://py3readiness.org/](http://py3readiness.org/) shows 360 of the top downloaded Python packages are all Python 3 ready.

**Jokes** 

- I was looking for some programming one liners online; looked on a reddit thread; read a great answer;  which was “any joke can be a one-liner with enough semicolons.”
- A SQL statement walks into to a bar and up to two tables and asks, “Mind if I join you?”
    
