# Python Bytes 171
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: [**David Amos**](https://twitter.com/somacdivad)

**David #1:** [**PEP 614 – Relaxing Grammar Restrictions on Decorators**](https://www.python.org/dev/peps/pep-0614/)

- Python currently requires that all decorators consist of a dotted name, optionally followed by a single call.
	- E.g., can’t use subscripts or chained calls
- PEP proposes allowing any valid expression.
- Motivation for limitation is not a technical requirement:
	- *“I have a gut feeling about this one. I'm not sure where it comes from, but I have it... So while it would be quite easy to change the syntax in the future, I'd like to stick to the more restricted form unless a real use case is presented where [changing the syntax] would increase readability.”*
	- *(Guido van Rossom,* [*Source*](https://mail.python.org/archives/list/python-dev@python.org/message/P3JD24UFFPZUUDANOAI6GZAPIGY4CVK7/)*)*
- Use case highlighted by PEP:
	- List of Qt buttons: `buttons = [button0, button1, …]`
	- Decorator is a method on a class attribute: `button.clicked.connect`
	- Under current restrictions you can’t do `@button[0].clicked.connect`
	- Workarounds involve assigning list element to a variable first:
		- `button0 = buttons[0]`
		- `@button0.clicked.connect`
- Author points out grammar is already loose enough to hack around:
	- Define function `def _(x): return x`
	- Then use _ as your decorator: `@_(buttons[0].clicked.connect)`
	- That’s less readable than just using the subscript
- PEP proposes relaxing grammar to “any valid expression” (sort of), i.e. anything that you can use as a test in `if`, `elif`, or `while` blocks (as opposed to valid string input to `eval`)
	- Some things wouldn’t be allowed, though
	- E.g., tuples require parentheses, `@f, g` doesn’t make sense
	- Does a tuple as a decorator make sense in the first place, though?
- CPython implementation on GitHub:
	- [https://github.com/brandtbucher/cpython/tree/decorators](https://github.com/brandtbucher/cpython/tree/decorators)

**Michael #2:** [**Create a macOS Menu Bar App with Python (Pomodoro Timer)**](https://camillovisini.com/create-macos-menu-bar-app-pomodoro/)

- by **Camillo Visini**
- Nice article: Learn how to create your very own macOS Menu Bar App using Python, rumps and py2app
- The mac menu bar is super useful. I leverage the heck out of this thing. Why not write Python for it?
- Tools:
	- **Python 3** and **PyCharm** as an IDE
	- [**Rumps**](https://github.com/jaredks/rumps) → Ridiculously Uncomplicated macOS Python Statusbar apps
	- [**py2app**](https://py2app.readthedocs.io/en/latest/) → For creating standalone macOS apps from Python code *(how cool is that?)*
- Get started with the code:
```
    app = rumps.App("Pomodoro", "🍅")
    app.run()
```

- Then easily use Py2App to convert this into a full macOS app.
- Would love to see somebody try to submit one of these to the mac app store.

**Brian #3:** [**Conditional Coverage**](https://sobolevn.me/2020/02/conditional-coverage)

- Nikita Sobolev - CTO of wemake.services
- [announcement post](https://sobolevn.me/2020/02/conditional-coverage), [repo](https://github.com/wemake-services/coverage-conditional-plugin)
- suggested from [@OpensourceF](https://twitter.com/OpensourceF):
	- [https://twitter.com/OpensourceF/status/1232264318323957760](https://twitter.com/OpensourceF/status/1232264318323957760)
- From README.md:
	- Conditional coverage based on any rules you define!
	- Some project have different parts that relies on different environments:
		- Python version, some code is only executed on specific versions and ignored on others
		- OS version, some code might be Windows, Mac, or Linux only
		- External packages, some code is only executed when some 3rd party package is installed
- Traditional method:
	- [combine](https://coverage.readthedocs.io/en/v4.5.x/cmd.html#combining-data-files) coverage data before reporting. This works ok on CI systems or with tox for multiple Python/package version.
		- Doesn’t help much locally if wanting split is due to OS dependencies
		- Requires multiple test runs to get full coverage
- New coverage plugin 
	- allows you to maintain coverage while developing locally. 
	- single test run and a reasonable coverage report
	- So cool.
- Recommend to keep conditionals to a minimum and somewhat isolated. I wouldn’t want this all over my code base.
- Still want real full coverage on CI.

**David** **#4:** [**Pycel – A library for compiling excel spreadsheets to python code & visualizing them as a graph**](https://github.com/dgorissen/pycel)

- Compile an Excel file with formulas as a Python object
- The compiler converts formulas in the spreadsheet to executable code
- Once compiled, you can set values for cells and inspect the output in other cells
	- This is all happening in Python now, not touching Excel anymore
- You can visualize all of the formulas as a graph to explore how formulas depend on one another
- The author of the package wrote it to solve a problem in civilian aerospace engineering
	- Blog post here: [https://dirkgorissen.com/2011/10/19/pycel-compiling-excel-spreadsheets-to-python-and-making-pretty-pictures/](https://dirkgorissen.com/2011/10/19/pycel-compiling-excel-spreadsheets-to-python-and-making-pretty-pictures/)
	- From 2011, but still relevant!
- Finally, with all the formulas compiled, the package can solve for variables using an optimization process
	- In original use case this was to optimize engineering parameters to produce aircraft that could actually fly
	- Author describes how using Python he increased the cases that could be optimized from 65% to 98% and reduced calculation time from 10 minutes to around 30 seconds to 1 minute.

**Michael** **#5:** [**markdown-subtemplate**](https://github.com/mikeckennedy/markdown-subtemplate)

- A template engine to render Markdown with external template imports and basic variable replacements.
- Choice between data-driven server apps (typical Flask app), CMSes that let us edit content on the web such as WordPress, and even flat file systems like Pelican.
- This should not be a black and white decision.
- Here's how it works:
	1. You write standard markdown files for content.
	2. Markdown files can be shared and imported into your top-level markdown.
	3. Fragments of HTML can be used when css classes and other specializations are needed, but generally HTML is avoided.
	4. A dictionary of variables and their values to replace in the merged markdown is processes.
	5. Markdown content is converted to HTML and embedded in your larger site layout (e.g. within a Jinja2 template).
	6. Markdown transforms are cached to achieve very high performance regardless of the complexity of the content.
- Extensible logging and caching. Extensible storage coming soon.
- PRs and contributions are welcome. More to come

**Brian** **#6:** [**FlakeHell**](https://github.com/life4/flakehell)

- wemake.services, from Conditional Coverage, also makes the [wemake-python-styleguide](https://wemake-python-stylegui.de/en/latest/index.html), and [recommends using FlakeHell](https://wemake-python-stylegui.de/en/latest/pages/usage/integrations/flakehell.html)
- Allows you to configure flake8 and plugins more easily in pyproject.toml files.
- Provides a ramp to start using linting tools with “[legacy first](https://wemake-python-stylegui.de/en/latest/pages/usage/integrations/flakehell.html#flakehell-legacy)”:
	- `flakehell baseline > .flakehell_baseline`
	- specify that file in your `pyproject.toml`
	- flakehell lint will run your liniting tools and only report new failures
	- you can start fixing older stuff later, or just apply style guide to new code.
- Lots of awesome shortcuts for configuration with wildcards and such.
- Can specify a shared config in one repo and use it multiple projects as a starting point with local changes.
- FlakeHell:
	- It's a [Flake8](https://gitlab.com/pycqa/flake8) wrapper to make it cool.
	- Shareable and remote configs.
	- Legacy-friendly: ability to get report only about new errors.
	- Caching for much better performance.
	- Use only specified plugins, not everything installed.
	- Manage codes per plugin.
	- Enable and disable plugins and codes by wildcard.
	- Make output beautiful.
	- [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) support.
	- Show codes for installed plugins.
	- Show all messages and codes for a plugin.
	- Check that all required plugins are installed.
	- Syntax highlighting in messages and code snippets.
	- [PyLint](https://github.com/PyCQA/pylint) integration.
	- Allow codes intersection for different plugins.

**Extras:**

**Brian:**

- Lots of great new content weekly on [**Test & Code Podcast**](https://testandcode.com)

**Michael**

- Qt follow up
- [**Moon base geekout**](https://talkpython.fm/episodes/show/253/moon-base-geekout)

David:
- [**PyTexas 2020 Registration Opening**](https://www.pytexas.org/)
- [**Registration page**](https://ti.to/pytexas/pytexas-2020)


**Joke:**


- [**Why does it work**](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e442dc752f3572d29117c2a/efc7007a1aa68fb3fe7da1c90259c6d2/58fccf71fab91928d160d9344163397c.jpg)!?! 
