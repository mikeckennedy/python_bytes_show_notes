# Python Bytes 114
Sponsored by [https://pythonbytes.fm/digitalocean](https://pythonbytes.fm/datadog)

**Brian #1:** [**What should be in the Python standard library?**](https://lwn.net/Articles/776239/)

- on lwn.net by Jake Edge
- There was a discussion recently about what should be in the standard library, triggered by a request to add LZ4 compression.
- Kinda hard to summarize but we’ll try:
	- Jonathan Underwood proposed adding LZ4 compression to stdlib.
	- Can of worms opened
	- zlib and bz2 already in stdlib
	- Brett proposed making something similar to hashlib for compression algorithms.
	- Against adding it:
		- lz4 not needed for stdlib, and actually, bz2 isn’t either, but it’s kinda late to remove.
    - PyPI is easy enough. put stuff there.
	- Led to a discussion of the role of stdlib.
		- If it’s batteries included, shouldn’t we add new batteries
		- Some people don’t have access to PyPI easily
		- Do we never remove elements? really?
		- Maybe we should have a lean stdlib and a thicker standard distribution of selected packages
		  - who would decide?
		  - same problem exists then of depending on it. How to remove stuff?
		  - Steve Dower [would rather see](https://lwn.net/ml/python-dev/34544e1d-fc87-32ab-7b4c-40cb1e59c228@python.org/) a smaller standard library with some kind of "standard distribution" of PyPI modules that is curated by the core developers.
		- A leaner stdlib could speed up Python version schedules and reduce burden on core devs to maintain seldom used packages.
  - See? can of worms.
  - In any case, all this would require a PEP, so we have to wait until we have a PEP process decided on.

**Michael #2:** [**Data Science portal for Home Assistant launched**](https://data.home-assistant.io/)

- via Paul Cutler
- Home Assistant is launching a data science portal to teach you how you can learn from your own smart home data. 
- In 15 minutes you setup a local data science environment running reports.
- A core principle of Home Assistant is that a user has complete ownership of their personal data. A users data lives locally, typically on the SD card in their Raspberry Pi
- The Home Assistant Data Science website is your one-stop-shop for advice on getting started doing data science with your Home Assistant data.
- To accompany the website, we have created a brand new Hass.io Add-on [JupyterLab lite](https://github.com/hassio-addons/addon-jupyterlab-lite), which allows you to run a data science IDE called [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) directly on your Raspberry Pi hosting Home Assistant. You do your data analysis locally, your data never leaves your local machine. 
- When you build something cool, you can share the notebook without the results, so people can run it at their homes too.
- We have also created a Python library called the [HASS-Data-Detective](https://github.com/robmarkcole/HASS-data-detective) which makes it super easy to get started investigating your Home Assistant data using modern data science tools such as [Pandas](https://pandas.pydata.org/).
- Check out the [Getting Started notebook](https://github.com/home-assistant/home-assistant-notebooks/blob/master/~%20GETTING%20STARTED.ipynb)
- IoT aside: I finally found my first IoT project: Recording in progress button.

**Brian #3:** [**What's the future of the pandas library?**](https://www.dataschool.io/future-of-pandas/)

- Kevin Markham over at dataschool.io
- pandas is gearing up to move towards a 1.0 release. Currently rc-ing 0.24
- Plans are to get there “early 2019”.
- Some highlights
	- method chaining - encouraged by core team
		- to encourage further, more methods will support chaining
	- Apache arrow likely to be part of pandas backend sometime after 1.0
	- Extension arrays - allow you to create custom data types
	- deprications
		- `inplace` parameter. It doesn’t work with chaining, doesn’t actually prevent copies, and causes codebase complexity
		- `ix` accessor, use `loc` and `iloc` instead
		- `Panel` data structure. Use `MultiIndex` instead
		- `SparseDataFrame`. Just use a normal `DataFrame`
		- legacy python support


**Michael #4:** [**PyOxidizer**](https://github.com/indygreg/PyOxidizer)

- `PyOxidizer` is a collection of Rust crates that facilitate building libraries and binaries containing Python interpreters.
- `PyOxidizer` is capable of producing a single file executable - with all dependencies statically linked and all resources (like `.pyc` files) embedded in the executable
- The *Oxidizer* part of the name comes from Rust: executables produced by `PyOxidizer` are compiled from Rust and Rust code is responsible for managing the embedded Python interpreter and all its operations.
- `PyOxidizer` is similar in nature to [PyInstaller](http://www.pyinstaller.org/), [Shiv](https://shiv.readthedocs.io/en/latest/), and other tools in this space. What generally sets `PyOxidizer` apart is 
	- Produced executables contain an embedded, statically-linked Python interpreter
	- have no additional run-time dependency on the target system
	- runs everything from memory (as opposed to e.g. extracting Python modules to a temporary directory and loading them from there).

**Brian #5:** [**Working With Files in Python**](https://realpython.com/working-with-files-in-python/)

- by Vuyisile Ndlovu on RealPython
- Very comprehensive write up on working with files and directories
- Includes legacy and modern methods. 
	- Pay attention to pathlib parts if you are using 3.4 plus
	- Also great for “if you used to do x, here’s how to do it with pathlib”.
- Included:
	- Directory listings
	- getting file attributes
	- creating directories
	- file name pattern matching
	- traversing directories doing stuff with the files in there
	- creating temp directories and files
	- deleting, copying, moving, renaming
	- archiving with zip and tar including reading those
	- looping over files

**Michael #6:** [**$ python == $ python3?**](https://github.com/python/peps/pull/630)

- via [David Furphy](https://twitter.com/davidfurphy)
- [Homebrew tried](https://discourse.brew.sh/t/python-and-pep-394/1813) this recently & got "persuaded" to reverse. 
- Also in recent discussion of edits to [PEP394](https://github.com/python/peps/pull/630#issuecomment-384416159), [GvR said](https://github.com/python/peps/pull/630#issuecomment-384416159) absolutely not now, probably not ever.
- Guido van Rossum
	- RE: `python` doesn’t exist on macOS as a command: Did you mean python2 there? In my experience macOS comes with python installed (and invoking Python 2) but no python2 link (hard or soft). In any case I'm not sure how this strengthens your argument.
	- I'm also still unhappy with any kind of endorsement of python pointing to python3. When a user gets bitten by this they should receive an apology from whoever changed that link, not a haughty "the PEP endorses this".
	- Regardless of what macOS does I think I would be happier in a future where python doesn't exist and one always has to specify python2 or python3. Quite possibly there will be an age where Python 2, 3 and 4 all overlap, and EIBTI.

**Extras:**

Michael: [A letter to the Python community in Africa](https://twitter.com/anthonypjshaw/status/1086070538810810368)

- via Anthony Shaw
- Believe the broader international Python and Software community can learn a lot from what so many amazing people are doing across Africa.
- e.g. The attendance of PyCon NA was 50% male and 50% female.

Brian:

**Joke:**
via Luke Russell:
A: “Knock Knock”
B: “Who’s There"
A: ……………………………………………………………………………………….“Java”

Also: Java 4EVER video is amazing: [youtube.com/watch?v=kLO1djacsfg](https://www.youtube.com/watch?v=kLO1djacsfg)
