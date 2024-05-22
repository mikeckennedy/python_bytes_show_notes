# Python Bytes 69

Sponsored by DigitalOcean: **[https://do.co/python](https://do.co/python)**

**Brian #1:** [**pynb: Jupyter Notebooks as plain Python code with embedded Markdown text**](https://github.com/minodes/pynb)

-  `pynb` lets you manage Jupyter notebooks as plain Python code with embedded Markdown text, enabling:
	- **Python development environment**: Use your preferred IDE/editor, ensure style compliance, navigate, refactor, and test your notebooks as regular Python code.
	- **Version control**: Track changes, review pull requests and merge conflicts as with regular Python code. The cell outputs are stored separately and don't interfere with versioning.
	- **Consistent execution state**: Never lose track again of the execution state. Notebooks are always executed from clean iPython kernels and the cell execution is cached.
- You also get parameterized notebooks with batch and programmatic execution.

**Michael #2:** [**Microsoft’s quantum computing language is now available for**](https://www.digitaltrends.com/computing/microsoft-quantum-computing-q-available-macos-linux/) [**m**](https://www.digitaltrends.com/computing/microsoft-quantum-computing-q-available-macos-linux/)[**acOS**](https://www.digitaltrends.com/computing/microsoft-quantum-computing-q-available-macos-linux/)

- New language Q# ([snippet examples](https://docs.microsoft.com/en-us/quantum/quantum-qr-statements?view=qsharp-preview))
- How do you run a quantum app?
- Based on topological qubits and quantum computers
- Now out on macOS & Linux
- Need to use VS Code (and vs code extension)
- Comes with Python interoperability (only other language)
- Also in Jupyter
- Some real-world examples. See [this Wired article](https://www.wired.co.uk/article/quantum-computing-explained).
	- [D-wave](https://www.dwavesys.com/home)
	- IBM is making quantum computers commercially available. Since 2016, it has offered researchers the chance to run experiments on a five-qubit quantum computer via the cloud and at the end of 2017 started making its 20-qubit system available online too.


**Brian #3: pytest talk in Spanish** 

- "pytest: recommendations, basic packages for testing in Python and Django"
- By A. Vallbona ([@avallbona](https://twitter.com/avallbona)) From PyConES 2017
- with  [English slides](http://talks.apsl.io/testing-pycones-2017), and [video in Spanish](https://www.youtube.com/watch?v=K20GeR-lXDk&feature=youtu.be).
- Some of the topics covered:
	- `pytest-django`
	- `model-mommy` to easily create fixtures based on django models
	- `pytest-lazy-fixture` allows the use the fixtures as parameters to parameterize
	- `pytest-mock`, `pytest-cov`, `pytest-flake8`
	- `freezegun` to helps us to "freeze" time
	- `eradicate` to eliminate commented code
	- `pytest-xdist` to run tests in parallel
  

**Bonus pytest topic:**

- [pytest.org just added a Reference page](https://docs.pytest.org/en/latest/reference.html), a full reference to pytest’s API.

**Michael #4:** [**StackOverflow Developer Survey Results 2018**](https://insights.stackoverflow.com/survey/2018/)

- Sample size: Over 100,000 developers
- 55% contribute to open source
- 64% have CS degrees
- Experience and Belonging
	- Connection to other devs (increasing over time)
	- Competing with peers (decreasing over time)
	- Not as good as my peers (decreasing over time)
- How Much Time Do Developers Spend on a Computer? Most: 9-12 hours
- Python beats C# in usage for the first time
- Languages:
	- Most loved: #1 Rust, #2 Kotlin, #3 Python
	- Most dreaded: VB 6 and CoffeeScript
	- Most wanted: #1 Python 25%, #JavaScript 19%, #3 Go 16%
- Databases:
	- Loved: PostgreSQL
	- Dreaded: IBM Db2, Memcached, and Oracle
	- Most wanted: MongoDB
- Editor: VS Code
- Dev OSes:
	- Windows: 49%
	- macOS: 27%
	- Linux: 23%

**Brian #5:** [**demoshell**](https://pypi.python.org/pypi/demoshell/)

- [**@**](https://twitter.com/doughellmann)[doughellmann](https://twitter.com/doughellmann)
- Doug Hellman ([**@**](https://twitter.com/doughellmann)[doughellmann](https://twitter.com/doughellmann)) [announces demoshell](https://doughellmann.com/blog/2018/03/11/demoshell-0-1-0/)
	- Inspired by a tweet from [@genehack](https://twitter.com/genehack) “Hey, speakers, if you're doing live demos in a shell, clear the screen after *every* *command* to get the prompt back at the top, so folks in the back can see what you're doing.”
- demoshell is a simplified shell for live demonstrations. It always shows the command prompt at the top of the screen and pushes command output down instead of letting it scroll up.
- In his words: “I put it up there to start a discussion. I’d be happy if a bunch of people showed up and wanted to take it over and actually turn it into something useful. I invite people to give it a look. And warn them that too much interest is going to be met with commit privileges on the repo. :-)”

**Michael #6: Clear statement on Python 2 EOL**

- Will there be a period where Py2.7 is in security-only status before hitting EOL?
- via Nicola Iarocci‏ [@nicolaiarocci](https://twitter.com/nicolaiarocci)
  - Yay, @gvanrossum makes it adamantly clear: “Let's not play games with semantics. The way I see the situation for **2.7 is that EOL is January 1st, 2020**, and there will be no updates, **not even source-only security patches**, after that date.” **https://buff.ly/2pbZmBZ** 
- Support (from the core devs, the PSF, and python.org) stops completely on that date.

**Follow up and other news**

**Michael:**

- Eve: MongoDB & Flask-backed RESTful APIs course is out!
	- **[https://training.talkpython.fm/courses/explore_eve/eve-building-restful-mongodb-backed-apis-course](https://training.talkpython.fm/courses/explore_eve/eve-building-restful-mongodb-backed-apis-course)**
- Shoutout to everyone I met at [PyCon Slovakia](https://2018.pycon.sk/en/)

**Brian:** 

- A couple of recent episodes on Test & Code focusing on project test development:
	- [What tests to write first](http://testandcode.com/37) 
	- [Prioritize software tests with RCRCRC](http://testandcode.com/38)
	- Upcoming topics will include beefing up test coverage with things like equivalence partitioning, boundary value analysis, state transition diagrams, state tables, negative testing, …
	- Also learning a lot about developing an open source project and all the tools surrounding that. I’ll discuss those topics in episodes as well.
	- Project used in both episodes, [cards : a project task tracking / todo list app](https://github.com/okken/cards) that will be expanded as I go along talking about different test and software development topics. 

