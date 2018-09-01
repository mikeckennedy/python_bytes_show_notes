# Python Bytes 93
Sponsored by DataDog -- [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Replacing Bash Scripting with Python**](https://github.com/ninjaaron/replacing-bash-scripting-with-python).

- reading & writing files
- CLI’s and working with stdin, stdout, stderr
- Path and shutil
- replacing sed, grep, awk, with regex
- running processes
- dealing with datetime
- see also:
	- [regex search and replace example scripts](http://pythontesting.net/python/regex-search-replace-examples/)
	
**Michael #2:** [**PyIodide**](https://iodide.io/pyodide-demo/python.html)

- Scientific Python in the browser
	- *ALL* of CPython (allowed in the browser)
	- NumPy
	- MatPlotLib
	- ...
- Project by Mozilla
- We asked “[Will there be a PyBlazor?](https://pythonbytes.fm/episodes/show/91/will-there-be-a-pyblazor)” just two weeks ago. I think we are on a path…

**Brian #3:** [**The subset of reStructuredText worth committing to memory**](https://simonwillison.net/2018/Aug/25/restructuredtext/)

- A lot of Python packages document with reStructuredText, a lot of reStructuredText tutorials are overwhelming. This post is the answer.
- paragraphs are with two newlines
- headings use a weird underlined method of above and below and =, -, and ~
- bulleted lists work with asterisks but spacing is important
- italics and bold are with one or two surrounding asterisks
- inline code uses two backticks
- links and code snippets are weird and I have to always look this up, as with images, and internal references.
- so I’ll bookmark this link

**Michael #4:** [**bandit**](https://github.com/PyCQA/bandit)

- via Anthony Shaw
- Bandit is a tool designed to find common security issues in Python code. 
- To do this Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files it generates a report.
- Issues detected:
	- B312  telnetlib
	- B307  eval
	- B110  try_except_pass
	- B602  subprocess_popen_with_shell_equals_true

**Brian #5:** [**Learn Python 3 within Jupyter Notebooks**](https://github.com/jerry-git/learn-python3/blob/master/README.md)

- just fun
- Also shows how to run `pytest` in a cell.

**Michael #6:** [**detect-secrets**](https://github.com/Yelp/detect-secrets)

- An enterprise friendly way of detecting and preventing secrets in code. 
- From Yelp
- detect-secrets is an aptly named module for (surprise, surprise) detecting secrets within a code base.
- However, unlike other similar packages that solely focus on finding secrets, this package is designed with the enterprise client in mind: providing a **backwards compatible**, systematic means of:
	1. Preventing new secrets from entering the code base,
	2. Detecting if such preventions are explicitly bypassed, and
	3. Providing a checklist of secrets to roll, and migrate off to a more secure storage.
- Allows you to set a baseline
- set it up as a git commit hook


