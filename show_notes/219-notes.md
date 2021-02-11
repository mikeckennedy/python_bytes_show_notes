# Python Bytes 219

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: **Jennifer Stark** - [**@_JAStark**](https://twitter.com/_JAStark) & guest on [**talkpython.fm/259**](https://talkpython.fm/259)

**Brian #1:** **Do you really need a virtualenv?**

- Frost Ming doesn’t think so, based on the article [**You don't really need a virtualenv**](https://frostming.com/2021/01-22/introducing-pdm/)
- The link slug is “introducing-pdm”, which I think would be a better title, but the first did work to get people to talk about it. Also, “Try PEP 582 today” may have been appropriate.
- Teaching new people is a problem:
	- Telling them to first type `python -m venv venv`
	- Then type `source venv/bin/activate` or `. venv/bin/activate`
	- Unless you’re on windows, then type `venv\scripts\activate.bat`
	- Then type `pip install -r requirements.txt`
	- Yeah. It’s not pretty, not fun, and good luck not having anyone ask questions about why this is necessary.
- Also the Python version is specified in the venv. So if you upgrade Python versions, what happens to existing venvs? 
- The article also discusses levels of venvs, and global tools that maybe you want not tied to each venv. But we have `pipx` for that, so I don’t think that’s a real issue.
- Enter [PEP 582](https://www.python.org/dev/peps/pep-0582/), still in draft mode.
	- Instead of a venv directory, your project has a `__pypackage__` directory. If you `python -m pip install` in your project directory, stuff just goes there instead of to the global Python.
	- So it kinda acts like a venv for local packages, it just doesn’t include local copies of the Python executables, and such.
	- This is probably a horrible description of 582, but oh well. Something like that.
- [pdm](https://pdm.fming.dev/) supports 582 today
	- PDM stands for Python Development Master
	- “It installs and manages packages in a similar way to `npm` that doesn't need to create a virtualenv at all!”
	- Has a workflow that reminds me of Poetry, but doesn’t use a venv, uses a package directory instead.
- Conclusion:
	- Huge props to Frost for this. It’s cool to see a tool that supports 582 and glimpse a possible Python future.
	- However, this doesn’t solve the “teaching Python” problem. The setup is more complex than venv.
	- I’m personally sticking with venv, well virtualenv, until (and if) 582 is supported by Python and pip.

**Michael #2:**  [**Copier - like cookiecutter**](https://github.com/copier-org/copier)

- A library for rendering project templates.
- Works with **local** paths and **git URLs**.
- Your project can include any file and `Copier` can dynamically replace values in any kind of text file.
- It generates a beautiful output and takes care of not overwrite existing files unless instructed to do so.
- To use as a CLI app: `pipx install copier`
- To use as a library: `pip install copier`
- Has a simple Python API
- Main advantage: Can update existing projects
- Runs from basic YAML files

Jennifer #3: [Pandarallel - run pandas apply in parallel!](https://github.com/nalepae/pandarallel/tree/v1.5.1) 

- simple install  `pip install pandarallel \[--upgrade\] [--user]``
- import `from pandarallel import pandarallel`
- initialise `pandarallel.initialize()`, set progress bar BOOL, set number of workers … (defaults to all cores)
- just use `parallel_apply` where you’d usually put `apply` 

**Brian #4:** [**Stop Using Print to Debug in Python. Use icecream Instead**](https://towardsdatascience.com/stop-using-print-to-debug-in-python-use-icecream-instead-79e17b963fcc)

- Khuyen Tran
- `print(f``"``{x=}``"``)` is better than `print(f``"``x: {x}``"``)` but it’s still a lot of typing.
- With [icecream](https://github.com/gruns/icecream), you can type `ic(x)` insted and git this nice output: `ic| x: 5`
- It’s less typing and just as nice. 
- There’s more.
	- `ic()` with no arguments logs the file, function, line number when it’s hit. Easy program flow tracing without a debugger.
	- You can configure it to do this cool context thing even if you do pass in a value to print.
	- You can configure custom prefix formatting with a callback function, so you can include the time or the user that’s logged in, or whatever else state you want to track.
	- Since all output is prefixed with `ic|`, you can see it easily
	- Writes to stderr by default, so it doesn’t muck up stdout stuff
	- Clean it out of your code by searching for `ic()` statements. If you have normal `print` statements in your code, you don’t want to use `print` for debugging also.

**Michael #5:** [**HTMX: Dynamic and live HTML without JavaScript**](https://htmx.org/)

- htmx allows you to access [AJAX](https://htmx.org/docs#ajax), [CSS Transitions](https://htmx.org/docs#css_transitions), [WebSockets](https://htmx.org/docs#websockets) and [Server Sent Events](https://htmx.org/docs#sse) directly in HTM
- Best seen [**via the examples section**](https://htmx.org/examples/) - try some out live on their site
- Has a cool Server Requests pane for seeing what’s happening in the example

Jennifer #6: [PyLDAvis - Interactive Topic Model Visualisation](https://pyldavis.readthedocs.io/en/latest/readme.html) 

- Port of LDAvis R package (does this mean PyLDAvis is a wrapper? A translation?) by Carson Sievert and Kenny Shirley
- User calls pyLDAvis with fitted model made with your favourite library (eg Gensim, sklearn, GraphLab)
- Outputs include:
	- term frequency within topic bar chart
	- term frequency within whole corpus bar chart
	- next to each bar is a word. You hover over the word and the topic circles adjust size to reflect representation of that term in that topic. 
	- topic circles - one for each topic, whose areas are setto be proportional to the proportions of the topics across the N total tokens in the corpus
	- term-topic circles, with area proportional to the frequencies with which a given term is estimated to have been generated by the topics of whole corpus
	- slider to adjust relevance metric (0 = terms very specific to currently selected topic; 1 = terms frequently seen in many topics).


Extras:

Brian:

- I’m also speaking to a group of NOAA people next week.
- I’m speaking the [Aberdeen Python User Group](https://ti.to/code-the-city/aberdeen-python-user-group-feb-2021/en) on the 10th of Feb. It’s virtual, so everyone can come.
- Excited about both. My kids are more impressed with the NOAA thing. It’s fun to impress your kids.

Michael: 

- Jet Brain’s fifth annual [**Developer Ecosystem survey**](https://blog.jetbrains.com/blog/2021/01/27/take-part-in-the-developer-ecosystem-2021-survey/)

Joke:

**Engineer helping a designer**

![](https://paper-attachments.dropbox.com/s_C6BDBA9FDB88C03FE1A2FCD9F399FEF5DD11602EF9A01D866F3735B88D941F35_1611870453039_DV7tun6VAAURiN3.jpg)

[https://twitter.com/EduardoOrochena/status/1306944019268861953](https://twitter.com/EduardoOrochena/status/1306944019268861953)

