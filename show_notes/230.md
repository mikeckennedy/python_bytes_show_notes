# Python Bytes 230

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guests: 
[**Peter Kazarinoff**](https://twitter.com/pkazarinoff)

**Brian #1:** [**calmcode.io**](https://calmcode.io/)

- by [Vincent D. Warmerdam](https://twitter.com/fishnets88)
- Suggested by [Rens Dimmendaal](https://twitter.com/R_Dimm)
- Great short intro tutorials & videos. Not deep dives, but not too shallow either.
- Suggestions:
	- [pytest](https://calmcode.io/pytest/introduction.html)
	- [rich](https://calmcode.io/rich/introduction.html)
	- [datasette](https://calmcode.io/datasette/introduction.html)
- I watched the whole series on datasette this morning and learned how to
	- turn a csv data file into a sqlite database
	- use datasette to open a server to explore the data
	- filter the data
	- visualize the data with datasette-vega plugin and charting options
	- learn how I can run random SQL, but it’s safe because it’s read only
	- use it as an API that serves either CSV or json
	- deploy it to a cloud provider by wrapping it in a docker container and deploying that
	- add user authentication to protect the service
	- explore tons of available data sets that have been turned into live services with datasette

**Michael #2:** [**Natural sort (aka natsort)**](https://github.com/SethMMorton/natsort)

- via [Brian Skinn](https://twitter.com/btskinn/status/1381718159116406785)
- Simple yet flexible natural sorting in Python.
- Python sort algorithm sorts lexicographically
    
```
    >>> a = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
    >>> sorted(a)
    ['1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '2 ft 7 in', '7 ft 6 in']
```

- `natsort` provides a function `natsorted` that helps sort lists "naturally”

```
    >>> natsorted(a)
    ['1 ft 5 in', '2 ft 7 in', '2 ft 11 in', '7 ft 6 in', '10 ft 2 in']
```

- Other things that can be sorted:
- versions
- file paths (via `os_sorted`)
- signed floats (via `realsorted`)
- Can go faster using [fastnumbers](https://pypi.org/project/fastnumbers/)

**Peter #3:** **Python controlling a helicopter on Mars.**

- First Flight of the Mars Drone/Helicopter was April 19: [https://mars.nasa.gov/technology/helicopter/#Overview](https://mars.nasa.gov/technology/helicopter/#Overview). The Drone/Helicopter is called [Ingenuity](https://mars.nasa.gov/news/8659/alabama-high-school-student-names-nasas-mars-helicopter/). The helicopter rode to Mars attached to the belly of the [Perseverance rover](https://mars.nasa.gov/mars2020/).
-  Community powers NASA’s Ingenuity Helicopter: DEVELOPERS AROUND THE WORLD CONTRIBUTE TO HISTORIC FLIGHT: [https://github.com/readme/nasa-ingenuity-helicopter](https://github.com/readme/nasa-ingenuity-helicopter)
- The Drone/Helicopter flight control software is called F’  (pronounced f-prime, sounds like Python f’strings :). You can clone and install the flight control software from GitHub. Make sure you have Python and pip installed. [https://github.com/nasa/fprime](https://github.com/nasa/fprime)

**Brian #4:** **Pydantic, FastAPI, Typer will all run on 3.10, 3.11, and into the future**

- suggested by an Angry Dwarf
- It’s a bit of an emotional roller coaster this last week even for those of us on the sidelines watching. I’m sure it was even more so for those involved.
- Short version:
	- Pydantic, FastAPI, Typer, etc will continue to run as is in 3.10
	- Minor changes might be necessary in 3.11, but most likely all of us bystanders and users of these packages won’t even see the change, or we will be given specific instructions on what we need to change well ahead of time.
	-  If things change in 3.11, your code might still work fine, and you can test that today if you are worried about it.
	- All project leads are involved and talking with the Steering Council.
	- The Steering Council has all of our interests and Pythons in mind and wants to make improvements to Python in a sane way. 
	- So don’t freak out. Smart and kind people are involved and know what they are doing.
    
- Slightly more detail that I don’t really want to read, and summarized to my perspective:
	- Something about an existing [PEP 563](https://www.python.org/dev/peps/pep-0563/), titled Postponed Evaluation of Annotations
	- It was part of 3.7 and it included:
		- “In Python 3.10, function and variable annotations will no longer be evaluated at definition time. Instead, …”
	- This would have implications on Pydantic and projects using it and similar methods, like FastAPI, Typer, …
	- Panic ensues, people wringing their hands, bystanders confused.
	- BTW, the Python steering council knows what they are doing and is aware of all of this already. But lots of people jumped on the bandwagon anyway and freaked out.
	- Even I was thinking “Ugh. I use Typer and FastAPI, can I still use them in 3.10?”
	- Luckily, Sebastian Ramirez [posted](https://twitter.com/tiangolo/status/1384512012768759810?s=20):
    - I've seen some incorrect conclusions that FastAPI and pydantic "can't be used with Python 3.10". Let's clear that up. In the worst-case scenario (which hasn't been decided), some corner cases would not work and require small refactors.
	- And also if you are worried about the future and your own use as is, you can use `from __future__ import annotations` to try the new system out. Also [thanks Sebastian](https://twitter.com/tiangolo/status/1384512019756376064?s=20)
	- Then there is this [message by Thomas Wouters about PEP 563 and 3.10](https://mail.python.org/archives/list/python-dev@python.org/thread/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/)
    - “The Steering Council has considered the issue carefully, along with many of the proposed alternatives and solutions, and we’ve decided that at this point, we simply can’t risk the compatibility breakage of PEP 563. We need to roll back the change that made stringified annotations the default, at least for 3.10. (Pablo is already working on this.) 
    - “To be clear, we are not reverting PEP 563 itself. The future import will keep working like it did since Python 3.7. We’re delaying making PEP 563 string-based annotations the default until Python 3.11. This will give us time to find a solution that works for everyone (or to find a feasible upgrade path for users who currently rely on evaluated annotations). Some considerations that led us to this decision: …”

**Michael #5: Extra, Extra, Extra, Extra hear all about it**

- No social trackers on Python Bytes or Talk Python.
- [Python packages on Mars](https://twitter.com/AikidoUke/status/1384287997621723139)
- [More Mars](https://twitter.com/HalAtWork/status/1384609038319591426)
- [NordVPN and “going dark”](https://nordvpn.com/)
- Nobody wants anything to do with Google's new tracking mechanism FLoC ([Android Police](https://www.androidpolice.com/2021/04/19/the-folks-behind-brave-browser-slam-google-for-its-new-tracking-policy/), [Ars Technica](https://arstechnica.com/gadgets/2021/04/everybody-hates-floc-googles-tracking-plan-for-chrome-ads/)). [From EFF](https://www.eff.org/deeplinks/2021/03/googles-floc-terrible-idea): *Google’s pitch to privacy advocates is that a world with FLoC  will be better than the world we have today, where data brokers and ad-tech giants track and profile with impunity. But that framing is based on a false premise that we have to choose between “old tracking” and “new tracking.” It’s not either-or. Instead of re-inventing the tracking wheel, we should imagine a better world without the myriad problems of targeted ads.* 

**Peter #6:** **Build Python books with Jupyter-Book**

- There are many static site generators for Python: Sphinx, Pelican, MkDocs…
- [Jupyter-Book](https://github.com/executablebooks/jupyter-book) is a static site generator that makes online books from Jupyter notebooks and markdown files. See the [Jupyter-book docs](https://jupyterbook.org/intro.html).
- Books can be [published on GitHub pages](https://jupyterbook.org/publish/gh-pages.html) and there is a GitHub action to automatically re-publish your book with each git push.
- [A gallery of Jupyter-books](https://executablebooks.org/en/latest/gallery.html) includes: Geographic Data Science with Python, Quantitative Economics with Python, the UW Data Visualization Curriculum, and a book on Algorithms for Automated Driving. All the books are free an online.
    

**Extras**

**Brian**

- 2021 South African Pycon, PyConZA - [https://za.pycon.org/](https://za.pycon.org/). The conference will be on 7 and 8 October entirely online
- [deadpendency update](https://twitter.com/deadpendency/status/1382594389445255169) . Within a day of us talking about deadpendency last week, the project maintainer added support for pyproject.toml. So projects using poetry, flit should work now. I imagine setuptools with pyproject.toml should also work.

**Peter**

- Peter’s Book: [Problem Solving with Python](https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415) (dead trees) or [free online](https://problemsolvingwithpython.com/)

**Joke** 

[More code comments](https://betterprogramming.pub/56-funny-code-comments-that-people-actually-wrote-6074215ab387)

```
    // Dear future me. Please forgive me.
    // I can't even begin to express how sorry I am.
```

```
    try {
       ...
    } catch (SQLException ex) {
       // Basically, without saying too much, you're screwed. Royally and totally.
    } catch(Exception ex){
       //If you thought you were screwed before, boy have I news for you!!!
    }
```

```
    // This is crap code but it's 3 a.m. and I need to get this working.
```

One more:

From [TwoHardThings by Martin Fowler](https://martinfowler.com/bliki/TwoHardThings.html):
Original saying:
*There are only two hard things in Computer Science: cache invalidation and naming things.*
*-- Phil Karlton*
Then there’s [This tweet](https://twitter.com/pbowden/status/468855097879830528).



