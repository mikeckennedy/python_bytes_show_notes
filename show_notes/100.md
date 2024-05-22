# Python Bytes 100

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guests:

* **[Anthony Shaw](https://twitter.com/anthonypjshaw)**
* [**Dan Bader**](https://twitter.com/dbader_org)
* **[Brett Cannon](https://twitter.com/brettsky)**
* **[Nina Zakharenko](https://twitter.com/nnja)**

**Brian #1:** [**poetry**](https://pypi.org/project/poetry/)

- “poetry is a tool to handle dependency installation as well as building and packaging of Python packages. It only needs one file to do all of that: the new, standardized pyproject.toml. 
  In other words, poetry uses pyproject.toml to replace setup.py, requirements.txt, setup.cfg, MANIFEST.in and the newly added Pipfile.”
- poetry 
	- can be used for both application and library development
	- handles dependencies and lock files 
	- strongly encourages virtual environment use (need specifically turn it off)
	- can be used within an existing venv or be used to create a new venv
	- automates package build process
	- automates deployment to PyPI or to another repository
	- CLI and the use model is very different than pipenv. Even if they produced the same files (which they don’t), you’d still want to try both to see which workflow works best for you. For me, I think poetry matches my way of working a bit more than pipenv, but I’m still in the early stages of using either.
- From [**Python's New Package Landscape**](http://andrewsforge.com/article/python-new-package-landscape/)
	- “[PEP 517](https://www.python.org/dev/peps/pep-0517/) and [PEP 518](https://www.python.org/dev/peps/pep-0518/)—accepted in September 2017 and May 2016, respectively—changed this status quo by enabling package authors to select different build systems. Said differently, **for the first time in Python, developers may opt to use a distribution build tool other than** `**distutils**` **or** `**setuptools**`**. The ubiquitous** `**setup.py**` **file is no longer mandatory in Python libraries.”**
- [PEP 517 -- A build-system independent format for source trees](https://www.python.org/dev/peps/pep-0517/)
- [PEP 518 -- Specifying Minimum Build System Requirements for Python Projects](https://www.python.org/dev/peps/pep-0518/)
- Another project that utilizes pyproject.toml is [flit](https://flit.readthedocs.io/en/latest/index.html), which seems to overlap quite a bit with poetry, but I don’t think it does the venv, dependency management, dependency updating, etc.
- See also:
	- [Clarifying PEP 518 (a.k.a. pyproject.toml)](https://snarky.ca/clarifying-pep-518/) - From Brett
- Question for @Brett C 517 and 518 still say “provisional” and not “final”. What’s that mean?
	- We are still allowed to tweak it as necessary before it
- Biggest difference is poetry uses pyproject.toml ([PEP518](https://www.python.org/dev/peps/pep-0518/#id26)) instead of Pipfile. Replaces all others (setup.py, setup.cfg, requirements*.txt, manifest.IN)
	- Even its lock file is in TOML
- Author “does not like” pipenv, or some of the decisions it has made. Note that Kenneth has recently made some calls to introduce more discussion and openness with a PEP-style process called PEEP ([PipEnv Enhancement Proposals](https://github.com/pypa/pipenv/blob/master/peeps/PEEP-001.md)).
	- E.g. uses a more extensive dependency resolver
- Pipenv does not support multiple environments (by design) making it useless for library development. Poetry makes this more open. See https://medium.com/@DJetelina/pipenv-review-after-using-in-production-a05e7176f3f0
- Wait. Why am I doing your notes for you @Brian O ! (awesome. Thanks Ant.)
- Brett has had initial discussions on Twitter with both pipenv and poetry about possibly standardizing on a lockfile format so that’s the artifact these tools produce and everything else is tool preference

**Anthony Shaw #2:** [**pylama**](https://github.com/klen/pylama) **and** [**radon**](https://radon.readthedocs.io/en/latest/)

- Have been investigating tools for measuring complexity and performance of code and how that relates to test
- If you can refactor your code so the tests still pass, the customers are still happy AND it’s simpler then that’s a good thing - right?
- Radon is a Python tool that leverages the AST to give statistics on Cyclomatic Complexity (number of decisions — nested if’s are bad), maintainability index (LoC & Halstead) and Halstead (number of operations an complexity of AST).
- Radon works by adding a ComplexityVisitor to the AST.
- Another option is Ned Batchelder’s McCabe tool which measures the number of possible branches (similar to cyclomatic)
- All of these tools are combined in pylama - a code linter for Python and Javascript. Embeds pycodestyle, mccabe, radon, gjslint and pyflakes. 
- Final goal is to have a pytest plugin that fails tests if you make your code more complicated

**Nina Zakharenko #3:** **Tools for teaching Python**

- Teaching Python can come with hurdles — virtual environments, installing python3, pip, working with the command line.
	- Put out a call on twitter asking - “What software and tools do you use to teach Python?”.
	- 50 Responses, 414 votes, learned about lots of new tools. Read the [thread](https://twitter.com/nnja/status/1047190883064397825).
		- 27% use python or ipython repl
		- 13% use built-in IDLE
		- 39% use an IDE or editor - [Visual Studio Code](https://code.visualstudio.com/docs/languages/python?WT.mc_id=pythonbytes-podcast-ninaz), [PyCharm](https://www.jetbrains.com/pycharm/), [Atom](https://atom.io/).
		- 21% use other (mix of local and [hosted Jupyter notebooks](https://notebooks.azure.com/?WT.mc_id=pythonbytes-podcast-ninaz) and other responses)
- New tools I learned about:
	- [Mu editor](https://codewith.mu) - simple python editor, great for those completely new to programming. 
		- Large buttons with common actions above the editor.
		- Support for educational platforms
		  - Integrates with hardware platforms -- adafruit [Circuit Playground,](https://www.adafruit.com/product/3333) [micro:bit](https://microbit.org/)
		  - PyGame
		- [Awesome tutorials](https://codewith.mu/en/tutorials/)
  - [Neuron plugin for VS Code](https://marketplace.visualstudio.com/items?itemName=neuron.neuron-IPE&WT.mc_id=pythonbytes-podcast-ninaz), [Hydrogen plugin for Atom](https://atom.io/packages/hydrogen)
		- Interactive coding environment, brings a taste of Jupyter notebooks into your editor.
		- Targeted towards data scientists.
		- Show evaluated values, output pane to display charts and graphs
		- Import to/from Jupyter notebooks
  - [repl.it](https://repl.it) - open source hosted cloud repl with reasonable free tier
		- project goal - [zero effort setup](https://twitter.com/replit/status/1048064521460281345)
		- 3 vertical panes: files, editor, repl, and a button to run the current code.
		- no login, no signup needed to get started
		- visual package installation - no running pip, requirements.txt automatically generated
		- includes a debugger
  - [bpython](https://github.com/bpython/bpython) - Used it years ago, still an active project.
		- Fancy curses interface to the Python interactive interpreter. Windows, type hints, expected parameters lists.
		- Really cool feature — you can rewind your session! Pops the last line, and the entire session is reevaluated. 
		- Easily reload imported modules. 
- Honorable mentions: 
	- [Edublocks](https://edublocks.org/) - Teaching tool for kids, visually drag and drop blocks of Python code. [Open source](https://github.com/AllAboutCode/EduBlocks), created by [Joshua Lowe](http://allaboutcode.co.uk/), a brilliant 14 year old maker and programmer.
	- [pythonanywhere](https://www.pythonanywhere.com), [codeskulptor.org](http://www.codeskulptor.org/), [codesters](https://www.codesters.com/).

**Dan Bader #4: My favorite tool of 2018:** [**“Black” code formatter**](https://black.readthedocs.io/en/stable/) by Łukasz Langa

- Black is the “uncompromising Python code formatter”
- An opinionated auto-formatter for your code (like YAPF/autopep for Python, or gofmt for golang who popularized the idea)
- Heard about it [in episode #73 by Brian](https://pythonbytes.fm/episodes/show/73/this-podcast-comes-in-any-color-you-want-as-long-as-it-s-black) 
- Started using it for some small tools, then rolled it out to the whole [realpython.com](https://realpython.com) code base including our public example code repo ([https://github.com/realpython/materials](https://github.com/realpython/materials))
- Benefits are:
	- Auto formatting—Not only does it call you out on formatting violations, it auto-fixes them
	- Code style discussions disappear—just use whatever Black does
	- Super easy to make several code bases look consistent (no more mental gymnastics to format new code to match its surroundings)
	- Automatically enforce consistent formatting on CI with “black --check” (I use a combo of flake8 + black because flake8 also catches syntax errors and some other “code smells”)
		- pro-tip: set up a pre-commit hook/rule to automatically run black before committing to Git. Also add it to your editor workflow (reformat on save / reformat on paste)
- Tool support:
	- [Built into](https://code.visualstudio.com/docs/python/editing#_formatting) the Python extension for VS Code (which Łukasz uses 😉)
	- [Plug-in](https://plugins.jetbrains.com/plugin/10563-black-pycharm) for PyCharm (for Michael and Brian 😁 )
	- Support in [pre-commit](https://pre-commit.com/)
- For the most part I really like the formatting Black applies, if you’re not a fan you might hate this tool because it makes your code look “ugly” 🙂 
- Still in beta but found it very useful and helpful as of October 2018. Give it a try!

**Brett Cannon #5:** [**A Web without JavaScript**](https://www.youtube.com/watch?v=2XSeNQyPlTY): Russell Keith-Magee at PyCon AU

- JavaScript has a monopoly in web browsers for client-side programming
- Mono-language situations are not good for anyone
- Can Python somehow break into the client-side web world?
- Example implementation of Luhn algorithm:
	- JavaScript: 0.4KB
	- [Transcrypt](https://www.transcrypt.org/): transpile to 32KB
	- [Brython](https://brython.info/): Python compiler for 0.5KB + 646KB bootstrap
	- [Batavia](https://pybee.org/project/projects/bridges/batavia/): Eval loop for 1.2KB + 5MB bootstrap
	- [Pyodide](https://github.com/iodide-project/pyodide): CPython compiled to WASM for 0.5KB + 3MB bootstrap
- WASM as a Python target might make this feasible
	- Example written in C compiled to 22KB (w/ a 65KB bootstrap for older browsers)
- Maybe easier to target Electron/Node instead of client-side web initially?
- Scott Hanselman’s blog post [https://www.hanselman.com/blog/JavaScriptIsWebAssemblyLanguageAndThatsOK.aspx](https://www.hanselman.com/blog/JavaScriptIsWebAssemblyLanguageAndThatsOK.aspx)
- Hanselminutes interview [https://hanselminutes.com/638/c-and-browser-monoculture-with-vivaldis-patricia-aas](https://hanselminutes.com/638/c-and-browser-monoculture-with-vivaldis-patricia-aas)

**Michael #6:** [**Async WebDriver implementation for asyncio and asyncio-compatible frameworks**](https://github.com/HDE/arsenic)

- You’ve heard of Selenium but in an async world what do we use? Answer: `arsenic`

```
    # Example: Let's run a local Firefox instance.
    async def example():
        # Runs geckodriver and starts a firefox session
        async with get_session(Geckodriver(), Firefox()) as session:
              # go to example.com
              await session.get('http://example.com')
              # wait up to 5 seconds to get the h1 element from the page
              h1 = await session.wait_for_element(5, 'h1')
              # print the text of the h1 element
              print(await h1.get_text())
```

- Use cases include testing of web applications, load testing, automating websites, web scraping or anything else you need a web browser for. 
- It uses real web browsers using the Webdriver specification.
- Warning: While this library is asynchronous, web drivers are not. You must call the APIs in sequence. The purpose of this library is to allow you to control multiple web drivers asynchronously or to use a web driver in the same thread as an asynchronous web server.
- [Arsenic with pytest](https://arsenic.readthedocs.io/en/latest/howto/pytest.html)
- Supported browsers
	- [Headless Google Chrome](https://arsenic.readthedocs.io/en/latest/reference/supported-browsers.html#headless-google-chrome)
	- [Headless Firefox](https://arsenic.readthedocs.io/en/latest/reference/supported-browsers.html#headless-firefox)
- Everyone’s thoughts on async in Python these days?
- Selenium-Grid https://www.seleniumhq.org/docs/07_selenium_grid.jsp

**Extra:** 

- Take the python survey: [https://talkpython.fm/survey2018](https://talkpython.fm/survey2018) 
- 3.7.1rc1 is out [https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-1-release-candidate-1](https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-1-release-candidate-1) 
- A good review on Python packaging [http://andrewsforge.com/article/python-new-package-landscape/](http://andrewsforge.com/article/python-new-package-landscape/)
- New September release of [Python Extension for Visual Studio Code](https://blogs.msdn.microsoft.com/pythonengineering/2018/10/09/python-in-visual-studio-code-september-2018-release/?WT.mc_id=pythonbytes-podcast-ninaz) — lots of new features, like automatic environment activation in the terminal, debugging improvements, and more!
- [Submit a talk](https://2019.pycascades.com/news/2-cfp-now-open/) to [PyCascades](https://2019.pycascades.com/) happening February 2019 in Seattle. [Call for proposals](https://2019.pycascades.com/news/2-cfp-now-open/) closes October 21st. Mentorship available. 

