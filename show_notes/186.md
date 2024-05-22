# Python Bytes 186
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

**Michael #1:** [sidetable - Create Simple Summary Tables in Pandas](https://pbpython.com/sidetable.html) 

- by [Chris Moffitt](https://pbpython.com/author/chris-moffitt.html)
- Makes it easy to build a frequency table and simple summary of missing values in a DataFrame.
- Example without and with
![](https://pbpython.com/images/stb_table_header.png)

- A useful tool when starting data exploration on a new data set
- At its core, sidetable is a super-charged version of pandas `value_counts` with a little bit of `crosstab` mixed in.
- With sidetable is imported, you have a new accessor on all your DataFrames - `stb` that you can use to build summary tables.

**Brian #2:** [**tabulate**](https://github.com/astanin/python-tabulate)

- suggested by Tom McDermott
- Pretty-print tabular data in Python, a library and a command-line utility.

```
    from tabulate import tabulate
    
    table = [["Sun",696000,1989100000],
             ["Earth",6371,5973.6],
             ["Moon",1737,73.5],
             ["Mars",3390,641.85]]
    headers=["Planet","R (km)", "mass (x 10^29 kg)"]
    table_str = tabulate(table, headers=headers)
    print(table_str)
```

```
    Planet      R (km)    mass (x 10^29 kg)
    --------  --------  -------------------
    Sun         696000           1.9891e+09
    Earth         6371        5973.6
    Moon          1737          73.5
    Mars          3390         641.85
```

- lots of table formats, including
	- simple (Markdown extended)
	- github (github flavored markdown)
	- pipe
	- jira
	- mediawiki
	- html
	- plain (just spaces)
- different column alignment options
- number formatting

**Michael #3:**  [treebeard - ci for notebooks](https://github.com/treebeardtech/treebeard)

- via [Brian Skinn](https://twitter.com/btskinn/status/1264910913280389120)
- Continuous Integration for binder-ready repos
- A solution for setting up continuous integration on data science projects requiring minimal configuration.
- **Functionality:**
- Automatically installs dependencies for binder-ready repos (which can use conda, pip, or pipenv)
- Runs notebooks in the repo (using papermill)
- Uploads outputs, providing versioned URLs and nbcoverted output notebooks
- Integrates with repos via a [GitHub App](https://github.com/marketplace/treebeard-build)
- Slack notifications
- A secret store for integrating with existing infrastructure
- A notebook that can run all code cells successfully will be tagged as successful. Treebeard shows a summary of all notebook statuses once execution is finished.


**Brian #4:** **Upcoming features in venv/virtualenv**

- In [episode 184](https://pythonbytes.fm/184), we discussed how virtualenv and venv
- [Coming in Python 3.9,](https://docs.python.org/3.9/library/venv.html?highlight=venv#creating-virtual-environments) venv will get `--upgrade-deps` flag.
	- `--upgrade-deps Upgrade core dependencies: pip setuptools to the             latest version in PyPI``
	- It’s listed as being changed in 3.8, but it just missed 3.8 by a smidge and will have to wait until 3.9, which is available as beta now. Here’s [beta 3](https://www.python.org/downloads/release/python-390b3/). 
	- Automatically updates pip and setuptools in the new environment.
- virtualenv is also getting a new goodie, [periodic update](https://github.com/pypa/virtualenv/pull/1841).
	- Not only does it create environments with updated setuptools, pip, wheel packages, it will periodically go out and check for updates to make sure it’s ready for your next virtual environment.
	- You can also manually have it update, with the `--upgrade-embed-wheels` flag.


**Michael #5:** [**PEP 582 now!**](https://github.com/David-OConnor/pyflow)

- via Luiz Irber
- This PEP proposes to add to Python a mechanism to automatically recognize a __pypackages__ directory and prefer importing packages installed in this location over user or global site-packages.
- How virtual environments work is a lot of information for anyone new. It takes a lot of extra time and effort to explain them.
- Different platforms and shell environments require different sets of commands to activate the virtual environments.
- Virtual environments need to be activated on each opened terminal.
- Tools like pip can be used to install the required dependencies directly into this directory.
- Still in draft mode but Python 3.8?
- https://github.com/David-OConnor/pyflow implements PEP 582
- Unfortunately requires everything running via `pyflow` for now.

**Brian #6:** [**awesome pyproject.toml projects**](https://github.com/carlosperate/awesome-pyproject)

- “We think `pyproject.toml` is pretty awesome, so this [awesome list](https://github.com/topics/awesome-list) contains projects already using it, or discussing its inclusion.”
- Testing and formatting apparently switched pretty quick
	- coverage.py
	- pytest
	- tox
	- [ward](https://wardpy.com/) (new to me, no test names, test names are strings)
	- black
	- isort
- code analysis projects
	- pylint
	- unimport
	- wemake-python-styleguide
- packaging projects
- some articles on pyproject.toml
- and a list of projects discussing the switch
- [Python bytes awesome list](https://github.com/JackMcKew/awesome-python-bytes)

Extras:

Brian:

- new website for [Pragmatic](https://pragprog.com/titles/bopytest/)

Michael:

- Check out our [latest episode on pytest-plugins](https://talkpython.fm/episodes/show/267/15-amazing-pytest-plugins)
- [Managing Secrets and your Environment with 1Password](https://sixfeetup.com/blog/managing-secrets-and-your-environment-with-1password)

Joke:

- **Spouse**: Stop by the store on the way home from work, "Honey, please stop at the market and buy 1 bottle of milk. If they have eggs, bring 6"
- **Me**: I came back with 6 bottles of milk.
- **Spouse**: "Why the hell did you buy 6 bottles of milk? It's just the two of us!"
- **Me**: "Why do you think? Because they had eggs!"

