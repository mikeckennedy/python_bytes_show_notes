# Python Bytes 202
Sponsored by DataDog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**New in Python 3.9**](https://docs.python.org/3.9/whatsnew/3.9.html) 

- scheduled to be released Oct 5
- [Python 3.9.0rc2 released Sept 17](https://www.python.org/downloads/release/python-390rc2/) 
- New features (highlights)
	- Dictionary merge (`|`) and update (`|=`) operators.
	- String `str.removeprefix(prefix)` and `str.removesuffix(suffix)`. This have also been added to `bytes`, `bytearray`, and `collections.UserString`.
	- In type annotations you can now use built-in collection types such as `list` and `dict` as generic types instead of importing the corresponding capitalized types (e.g. `List` or `Dict`) from `typing`.
	- New PEG parser
	- Any valid expression can be used as a decorator. see [PEP 614](https://www.python.org/dev/peps/pep-0614/). Haven’t quite wrapped my head around the possibilities yet.
	-  `[zoneinfo](https://docs.python.org/3.9/library/zoneinfo.html#module-zoneinfo)` module brings support for the IANA time zone database to the standard library.
- Lots of other great stuff too, please check out the [changelog](https://docs.python.org/3.9/whatsnew/3.9.html) and give 3.9 a spin

**Michael #2:** [**jupyter-black**](https://github.com/drillan/jupyter-black)

- via Mary Hoang
- I recently tuned into the auto racing episode on Talk Python and liked Kane’s pypi suggestion of blackcellmagic. 
- There are a couple of other pypi packages that envelop the idea of black formatting Jupyter Notebooks and I recently started using a new pypi tool called jupyterblack! 
- This tool lets you black format Notebooks like you would Python files, only you call jblack instead of black.
- Then the extension provides
	- a toolbar button
	- a keyboard shortcut for reformatting the current code-cell (default: Ctrl-B)
	- a keyboard shortcut for reformatting whole code-cells (default: Ctrl-Shift-B)
- It will also point basic syntax errors.


**Brian #3:** [**Understanding and preventing DoS in web applications**](https://r2c.dev/blog/2020/understanding-and-preventing-dos-in-web-apps/)

- listener submitted suggestion, which led me to a bit of a rabbit hole
- by Jacob Kaplan-Moss
- Great discussion of what a DoS attack is, and how to check for and prevent problems, including a focus on Python and django.
- One example is ReDoS, regular expression DoS
- “ReDoS bugs occur when certain types of strings can cause improperly crafted regular expressions to perform extremely poorly.”
- Links to [Finding Python ReDoS bugs at scale using Dlint and r2c](https://r2c.dev/blog/2020/finding-python-redos-bugs-at-scale-using-dlint-and-r2c/), which talks about using [dlint](https://github.com/dlint-py/dlint).
- dlint
	- DoS linter plugin for flake8
	- Checks for a [huge number of security problems](https://github.com/dlint-py/dlint/tree/master/docs) in Python code.
	- Can be used alongside [Bandit](https://bandit.readthedocs.io/en/latest/).

**Michael #4:** [**bbox-visualizer**](https://github.com/shoumikchow/bbox-visualizer)

- via Shoumik Sharar Chowdhury (SHOH-mik CHOW-duh-ree)
- I work with computer vision, and one of the pain points of working with something like object detection or object recognition is positioning the labels once you get the bounding boxes.
- So for example, in the first image in the README, you get the positions of the boxes around the objects using any object-detection method. That part isn't hard. Positioning the labels like "person", "bicycle", "car" right on top of the boxes, however, is quite annoying. You have to do some clumsy math to make it work like that.
- This library helps make that very easy. You just use the bounding box locations and their corresponding labels and the library takes care of everything. Moreover, there are some other cool visualizations that you can use, other than the standard label on top of the boxes.
- Uses Open CV in Python to work with the image files and in memory drawing
- Define the bounds, set the label text and you’re off.
```
    bbv.draw_rectangle(img, bbox)
    bbv.add_T_label(img, label, bbox)
```

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5f6ee35c87894b83358ddf70/c9f4721a835a93a3efe7c1fdf604bdf6/Screen_Shot_2020-09-30_at_8.54.11_AM.png)


**Brian #5:** [**How to NEVER use lambdas.**](https://gist.github.com/MineRobber9000/19c331a9f5d8e994a4ed251f0ffa1e98)

- Another listener suggestion.
- Starts off with a brief example showing how to rewrite a power function as a lambda.
- Then jumps right into crazy code
- Replacing import statements with `__import__(``'``library``'``)` expressions
- Moving on to lambda-ifying class definitions
- Ending with a complete Flask application as a lambda expression.
- Truly horrible stuff

**Michael #6:** [**Uncommon Contributions: Making impact without touching the core of a library**](https://koaning.io/posts/cool-commits/)

- via Alexander, by [Vincent Warmerdam](https://koaning.io/posts/cool-commits/koaning.io)
- Different ways that people can contribute to open source software besides the typical code contribution. 
- Often, contributions include adding features to a library, fixing bugs, or providing examples to a documentation page. But consider:
- **Info**
	-  `rasa --version`
	- Before, this command would list the current version of Rasa. In the new version, it lists:
    1. The version of python.
    2. The path to your virtual environment.
    3. The versions of related packages.
- **Cron on Dependencies**
	- A user for [scikit-lego](https://scikit-lego.readthedocs.io/en/latest/), a package that I maintain, discovered that the reason the code wasn’t working was because scikit-learn introduced a minor, but breaking, change. To fix this the user added [a cronjob with Github actions](https://github.com/koaning/scikit-lego/pull/378) to the project.
- **Spellcheck**
	- Run a spellchecker, not just against our docs, but also on our source code! It turns out we had some issues in our docstrings as well.
- **Error Messages**
	- In [whatlies](https://github.com/RasaHQ/whatlies/pull/141), we’ve recently allowed for optional dependencies. If you try to use a part of the library that requires a dependency that is not part of the base package, then you’ll get this error message.
```
    In order to use ConveRTLanguage you'll need to install via;
    > pip install whatlies[tfhub]
    See installation guide here: https://rasahq.github.io/whatlies/#installation
```

- I added something like this to fluentcheck: [github.com/csparpa/fluentcheck/pull/22](https://github.com/csparpa/fluentcheck/pull/22)
- **Failing Unit Tests**
	- There’s a lovely plugin for [mkdocs](https://www.mkdocs.org) called [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter). It allows you to easily add jupyter notebooks to your documentation pages. When I was playing with it, I noticed that it wasn’t compatible with a new version of `mkdocs`. Instead of just submitting a bug to Github, I went the extra mile. I created a PR that contained a failing unit-test for this issue.
- **Renaming files**
	- Is there a file.py and a class File in file within a package? Careful there.  

**Extras:**

- Brian: 
	- [Learn to code with Wonder Woman, Smithsonian Learning Labs, and NASA](https://educationblog.microsoft.com/en-us/2020/09/learn-to-code-with-wonder-woman-smithsonian-learning-labs-and-nasa/)
	    - Microsoft Education
	    - Direct link: https://www.microsoft.com/inculture/wonderwoman-1984/
	    - At least some of the tutorials are Python. Not sure if all are.
- Michael: [IndyPy: Python Memory Deep Dive with Michael Kennedy](https://twitter.com/indypy/status/1308874183703760897) 

**Joke:**

- Suggested by Tim Skov Jacobsen
	- Kelsey Hightower’s project [nocode](https://github.com/kelseyhightower/nocode)
	- “**No Code:** No code is the best way to write secure and reliable applications. Write nothing; deploy nowhere.”
	- “**No Code Style Guide:** All no code programs are the same, regardless of use case, any code you write is a liability.”
	- 43.6k stars
	- 3.2k issues
	- 426 PRs
