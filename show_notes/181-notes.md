# Python Bytes 181
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)


----------

**Brian #1:** [**interrogate: checks your code base for missing docstrings**](https://pypi.org/project/interrogate/)

- Suggested by Herbert Beemster
- Written and Maintained by Lynn Root, [@roguelynn](https://twitter.com/roguelynn)
- Having docstrings helps you understand code.
- They can be on methods, functions, classes, and modules, and even packages, if you put a docstring in `__init__.py` files.
- I love how docstrings pop up in editors like VS Code & PyCharm do with them. If you hover over a function call, a popup shows up which includes the docstring for the function.
- Other tools like Sphinx, pydoc, docutils can generate documentation with the help of docstrings.
- But good is your project at including docstrings?
- `interrogate` is a command line tool that checks your code to make sure everything has docstrings. Neato.
- What’s missing? -vv will tell you which pieces are covered and not.
- Don’t want to have everything forced to include docstrings? There are options to select what needs a docstring and what doesn’t.
- Also can be incorporated into tox testing, and CI workflows.



----------

**Michael #2:** [**Streamlit: Turn Python Scripts into Beautiful ML Tools**](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)

- via [Daniel Hoadley](https://twitter.com/DanHLawReporter/status/1179431747647397890)
- Many folks come to Python from “scripting” angles
- The gap between that and interactive, high perf SPA web apps is gigantic
- Streamlit let’s you build these as if they were imperative top-to-bottom code
- Really neat tricks make callbacks act like blocking methods
- Use existing data science toolkits


----------

**Brian #3:** [**Why You Should Document Your Tests**](https://hynek.me/articles/document-your-tests/)

- Hynek Schlawack, [@hyneck](https://twitter.com/hynek) 
- All test_ methods should include a docstring telling you or someone else the what and why of the test.
- The test name should be descriptive, and the code should be clear. But still, you can get confused in the future.
- Hynek includes a great example of a simple test that is not obvious what it’s doing because the test is checking for a side effect of an action.
- “This is quite common in testing: very often, **you can’t ask questions directly**. Instead you verify certain properties that prove that your code is achieving its goals.”
- “If you don’t explain *what* you’re actually testing, you force the reader (possibly future you) to deduce the main intent by looking at all of its properties. This makes it tiring and time-consuming to quickly scan a file for a certain test or to understand what you’ve *actually* broken if a test starts failing.”
- Want to make sure all of your test methods have docstrings? 
	- `interrogate -vv --fail-under 100 --whitelist-regex "test_.*" tests` will do the trick.
- See also: [How to write docstrings for tests](https://jml.io/pages/test-docstrings.html)


----------

 **Michael #4:** [**HoloViz project**](https://holoviz.org/)

- HoloViz is a coordinated effort to make browser-based data visualization in Python easier to use, easier to learn, and more powerful.
- HoloViz provides:
	- High-level tools that make it easier to apply Python plotting libraries to your data.
	- A comprehensive [tutorial](https://holoviz.org/tutorial) showing how to use the available tools together to do a wide range of different tasks.
	- A [Conda](https://conda.io) metapackage "holoviz" that makes it simple to install matching versions of libraries that work well together.
	- Sample datasets to work with.
- Comprised of a bunch of cool independent projects
- [Panel](https://panel.pyviz.org) for making apps and dashboards for your plots from any supported plotting library
- [hvPlot](https://hvplot.pyviz.org) to quickly generate interactive plots from your data
- [HoloViews](https://holoviews.org) to help you make all of your data instantly visualizable
- [GeoViews](http://geoviews.org) to extend HoloViews for geographic data
- [Datashader](http://datashader.org) for rendering even the largest datasets
- [Param](https://param.pyviz.org) to create declarative user-configurable objects
- [Colorcet](https://colorcet.pyviz.org) for perceptually uniform colormaps.


----------

**Brian #5:**  [**A cool new progress bar for python**](https://dev.to/rsalmei/a-cool-new-progress-bar-for-python-1c0g)

- Rogério Sampaio, [@rsalmei](https://twitter.com/rsalmei)
- project: [alive-progress](https://github.com/rsalmei/alive-progress)
- Way cool CLI progress bars with or without spinners
- Clean coding interface.
- Fun features and options like sequential framing, scrolling, bouncing, delays, pausing and restarting.
- Repo README notes:
	- Great animations in the README. (we love this)
	- “To do” list, encourages contributions
	- “Interesting facts”
		- functional style
		- extensive use of closures and generators
		- no dependencies
- “Changelog highlights”
	- I love this. 1-2 lines of semicolon separated features added per version. 


----------

**Michael #6:** [**Awesome Panel**](https://awesome-panel.org/app)

- by Marc Skov Madsen
- Awesome Panel Project is to share knowledge on how awesome Panel is and can become.
- A curated list of awesome Panel **resources**.
- A **gallery** of awesome panel applications.
- This app as a **best practice multi page app** with a nice layout developed in Panel.
- Kind of meta as it’s built with Panel. :)
- Browse the gallery to get a sense of what it can do



----------

**Extras:**

Michael:

- Kevin Vanderveen created a cool COVID explorer with Streamlit
	- app: [https://analysis-covid-19.herokuapp.com](https://analysis-covid-19.herokuapp.com)
	- repo: [https://github.com/kvanderveen/analysis_covid_19](https://github.com/kvanderveen/analysis_covid_19)
- [Code Together for editor sharing](https://www.codetogether.com)

Brian:  

- [PyCon 2020 online](https://us.pycon.org/2020/online/)
	- new content still being posted, through first few weeks of May.
	- My talk is up. yay!
		- Multiply your Testing Effectiveness with Parameterized Testing
		- [description](https://us.pycon.org/2020/schedule/presentation/172/), [video](https://www.youtube.com/watch?v=2R1HELARjUk), [github repo](https://github.com/okken/talks/tree/master/2020/pycon_2020) with slides and code
	- Plus lots of other great talks, tutorials, charlas, sponsor workshops, online poster hall
- pytest resolution
	- [https://twitter.com/pytestdotorg/status/1257940818255462408](https://twitter.com/pytestdotorg/status/1257940818255462408)


----------

**Joke:**

O’Really book covers

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5eb2e04105fe8e58259d7f36/076f9b8d56c523d8d5babad9b8502e15/Screen_Shot_2020-05-06_at_9.03.54_AM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5eb2e04105fe8e58259d7f36/f92e82c70e306ab8f05be4b5b606b0a6/Screen_Shot_2020-05-06_at_9.03.48_AM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5eb2e04105fe8e58259d7f36/0055543eef640bada670f84eadc4f9d5/Screen_Shot_2020-05-06_at_9.04.49_AM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5eb2e04105fe8e58259d7f36/e568594f4ae3c54ad9ca72ebe38a52c8/Screen_Shot_2020-05-06_at_9.04.17_AM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5eb2e04105fe8e58259d7f36/c85fedc404e22aa9f30a1547527a3df0/Screen_Shot_2020-05-06_at_9.04.28_AM.png)



