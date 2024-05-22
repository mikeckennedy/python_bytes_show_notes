# Python Bytes 145
Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Special guests**

- [**Matt Harrison**](https://twitter.com/__mharrison__)
- [**Anthony Sottile**](https://twitter.com/codewithanthony)

Michael #1: [**friendly-traceback**](https://twitter.com/quobit/status/1161926740236800000)

- via Jose Carlos Garcia (I think 🙂 )
- Aimed at Python beginners: replacing standard traceback by something easier to understand
- Shows help for exception type
- Shows local variable values
- Shows code in a cleaner form with more context
- [3 ways to install](https://aroberge.github.io/friendly-traceback-docs/docs/html/usage.html)
	- As an exception hook
	- Explicit explain
	- When running an app

**Matt #2: [Pandas Users Survey](https://dev.pandas.io/pandas-blog/2019-pandas-user-survey.html)** 

- Most use it almost everyday but have less than 2 years experience
- Linux 61%, Windows 60%, Mac 42%
- 93% Python 3

**Anthony #3: python3 “Y2K” problem (python3.10 / python4.0)**

- with python3.8 close to release and python3.9 right around the corner, what comes after?
- both python3.10 and python4.0 present some problems
	-  `sys.version[:3]` which will suddenly report `'``3.1``'` in 3.10
	- a lot of code (including `six.PY3`!) uses `sys.version_info[0] == 3` which will suddenly be false in python4.0 (and start running python2 code!)
- early-to-mid 2020 we should start seeing the next version in the wild as [python3.9 reaches beta](https://www.python.org/dev/peps/pep-0596/#id6)
- easy ways to start testing this early:
	- [python3.10](https://github.com/asottile/python3.10) - a build of cpython for ubuntu with the version number changed
	- [flake8-2020](https://github.com/asottile/flake8-2020) - a flake8 plugin which checks for these common issues-

Michael #4: [**pypi research**](https://arxiv.org/pdf/1907.11073.pdf)

- via Adam (Codependent Codr)
- Really interesting research paper on the current state of Pypi from a couple authors at the University of Michigan: "An Empirical Analysis of the Python Package Index" - https://arxiv.org/pdf/1907.11073.pdf
- Comprehensive empirical summary of the Python Package Repository, PyPI, including both package metadata and source code covering 178,592 packages, 1,745,744 releases, 76,997 contributors, and 156,816,750 import statements. 
- We provide counts and trends for packages, releases, dependencies, category classifications, licenses, and package imports, as well as authors, maintainers, and organizations.
- Within PyPI, we find that the growth of the repository has been robust under all measures, with a compound annual growth rate of 47% for active packages, 39% for new authors, and 61% for new import statements over the last 15 years. 
- In 2005, there were 96 active packages, 96!
- MIT is the most common license
- (Matt) I saw this and was surprised at most commonly used libraries. What do you think the most common 3rd party library is?


**Matt #5: [DaPy](https://github.com/JacksonWuxs/DaPy)**

- “Pandas for humans” - Matt’s words
- Has portions of pandas, scikit-learn, yellowbrick, and numpy
- Designed for “data analysis, not for coders”


Anthony #6: [**python-remote-pdb**](https://github.com/ionelmc/python-remote-pdb)

- very small over-the-network remote debugger
- thin wrapper around `pdb` in a single file (easy to drop the file on `PYTHONPATH` if you can’t `pip install`)
- not as fully featured as other remote debuggers such as `pudb`  / `rpdb` / pycharm’s debugger but very easy to drop in
- fully supports `[breakpoint()](https://www.python.org/dev/peps/pep-0553/)` (python3.7+ or via [future-breakpoint](https://github.com/asottile/future-breakpoint))
- access `pdb` via `telnet` / `nc` / `socat`
- I’m using it to debug a text editor I’m writing to learn `curses`!

Extras:

Michael:

- [Hacker Gets $12,000 In Parking Tickets After 'NULL' License Plate Trick Backfires](https://www.forbes.com/sites/zakdoffman/2019/08/14/hacker-gets-12000-in-parking-tickets-after-null-license-plate-trick-backfires/)
- [PyCon 2020 site is up](https://us.pycon.org/2020/)

Matt

- [http://bit.ly/psxgb](http://bit.ly/psxgb) - My new course on Machine Learning with XGBoost

Anthony:

- [https://github.com/DRMacIver/hecate](https://github.com/DRMacIver/hecate) “like selenium webdriver for the terminal”

Jokes:

Michael: Two mathematicians are sitting at a table in a pub having an argument about the level of math education among the general public.

The one defending overall math knowledge gets up to go to the washroom. On the way back, he encounters their waitress and says, "I'll add an extra $10 to your tip, if you'll answer a question for me when I ask it. All you have to say is 'x-squared'." She agrees.

A few minutes later the populist mathematician says to his buddy, "I'll bet you $20 that even our waitress can tell us the integral of 2x."
The cynic agrees to the bet.

So the schemer beckons the waitress to their table and asks the question, to which she replies "x-squared". As he begins to gloat and demand his winnings, the waitress continues, "Plus a constant."


Anthony: I had a golang joke prepared, but then I `panic()`d

