# Python Bytes 142

Special guest: **[Brett Thomas](https://twitter.com/the_quark)**

Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Writing sustainable Python scripts**](https://vincent.bernat.ch/en/blog/2019-sustainable-python-script)

- Vincent Bernat
- Turning a quick Python script into a maintainable bit of software.
- Topics covered:
	- Documentation as a docstring helps future users/maintainers know what problem you are solving.
	- CLI arguments with defaults instead of hardcoded values help extend the usability of the script.
	- Logging. Including debug logging (and how to turn them on with CLI arguments), and system logging for unattended scripts.
	- Tests. Simple doctests, and pytest tests utilizing parametrize to have one test and many test cases.

**Brett #2:** **Static Analysis and** [**Bandit**](https://bandit.readthedocs.io/en/latest/)

**Michael #3:** [**jupyter-black**](https://github.com/drillan/jupyter-black)

- Black formatter for Jupyter Notebook 
- One of the big gripes I have about these online editors is their formatting (often entirely absent)
- Then the extension provides
	- a toolbar button
	- a keyboard shortcut for reformatting the current code-cell (default: Ctrl-B)
	- a keyboard shortcut for reformatting whole code-cells (default: Ctrl-Shift-B)

**Brian #4:** **Report Generation workflow with papermill, jupyter, rclone, nbconvert, …**

- Chris Moffitt articles
- [Automated Report Generation with Papermill: Part 1](https://pbpython.com/papermil-rclone-report-1.html)
- [Automated Report Generation with Papermill: Part 2](https://pbpython.com/papermil-rclone-report-2.html)
- Jupyter Notebooks used to create a report with pandas and matplotlib
- nbconvert to create an html report
- Papermill to parametrize the process with different data, and execute the notebook
- Copy the reports to shared cloud folders using Rclone.
- Set up a process to automate everything.
- Hook it up to cron to run regularly

**Brett #5**: Rant on time deltas

- `datetime.timedelta(months=1)` # Boom, too bad.
- Use: **[https://dateutil.readthedocs.io/en/stable/](https://dateutil.readthedocs.io/en/stable/)**

**Michael #6:** [**How — and why — you should use Python Generators**](https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/)

- by Radu Raicea
- Generator functions allow you to declare a function that behaves like an iterator. 
- They allow programmers to make an iterator in a fast, easy, and clean way.
- They only compute it when you ask for it. This is known as [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation).
- If you’re not using generators, you’re missing a powerful feature
- Often they result in simpler code than with lists and standard functions

**Extras**

Brian:

- [**PyPI now supports uploading via API token**](http://pyfound.blogspot.com/2019/07/pypi-now-supports-uploading-via-api.html) ****
	- also on [Test PyPI](http://pyfound.blogspot.com/2019/07/pypi-now-supports-uploading-via-api.html)

Michael:

- [**Chocolatey package manager**](https://chocolatey.org/packages/python/3.7.4) on windows via [Prayson Daniel](https://twitter.com/Proteusiq)
- GvM’s Next [**PEG article**](https://medium.com/@gvanrossum_83706/building-a-peg-parser-d4869b5958fb)
    

**Jokes** 

A good programmer is someone who always looks both ways before crossing a one-way street.

(reminds me of another joke: Adulthood is like looking both ways before crossing the street, then getting hit by an airplane)

[**Little bobby tables**](https://xkcd.com/327/)
