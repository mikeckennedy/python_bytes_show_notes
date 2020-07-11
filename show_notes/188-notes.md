# Python Bytes 188
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

**Michael #1:** [**Making a trading bot asynchronous using Python’s “unsync” library**](https://medium.com/@MattGosden/tutorial-using-pythons-unsync-library-to-make-an-asynchronous-trading-bot-9ee2ae881272)

- by [Matt Gosden](https://twitter.com/MattGosden/status/1272222637851377666)
- **The older way** — using the **threading** and **multiprocessing** libraries
- **The newer way** — using `async` and `await` from the **asyncio** library embedded into core Python from 3.7 onwards
- **The easier way (I think)**— using the `@unsync` decorator from the Python **unsync** library
- Somewhat realistic example worth looking at.
- Could discuss scalability more
- Also, proper def async and asyncio.sleep() for those playing at home
- But its absence kind shows unsync winning anyway. 🙂 It does work, right?

**Brian #2:** ****[**Fruit salad scrum estimation scale**](https://fberriman.com/2020/01/22/fruit-salad-a-scrum-estimation-scale/)

- From twitter question by Lacy Henschel, answered by Kathleen Jones
- Fruit related to work
	- how easy
	- potential for mess 
	- how many seeds, possible problems
	- does it need divided
- The scale
	- 1 - grape - trivial
	- 2 - apple - may take a bit of time but everyone knows how to divide it
	- 3 - cherry - easy but with some unknowns (what do you do with the pit?)
	- 5 - pineapple - somewhat undefined, no major unknowns, still a lot of work (lots of opinions on how to cut it)
	- 8 - watermelon - lots of work, some unknowns, messy (don’t know what you are getting into until you cut it open)
	- ?? - tomato - unknown task, needs more info before estimating (doesn’t belong in a fruit salad)
	- ?? - avacado - not scopable, probably urgent (goes bad quickly)

**Michael #3:** [**Math to Code**](https://mathtocode.com/)

- **Math to Code** is an interactive Python tutorial to teach engineers how to read and implement math using the NumPy library.
- by [vernon thommeret](https://thommeret.com/)
- Nice flashcard style of learning the building blocks of np for standard math
- Give it a try, solutions if you get stuck
- Python and NP together
- [Source at github](https://github.com/vthommeret/mathtocode)
- Interesting building blocks
1. [Skulpt](https://github.com/skulpt/skulpt) for interpreting Python
2. [Skulpt NumPy](https://github.com/ebertmi/skulpt_numpy) for a subset of NumPy
3. [KaTex](https://github.com/KaTeX/KaTeX) for rendering LaTeX
4. [Next.js](https://github.com/vercel/next.js) for frontend framework
5. [Tailwind CSS](https://github.com/tailwindcss/tailwindcss) for styling
6. [remark](https://github.com/remarkjs/remark) for rendering Markdown questions
7. [gray-matter](https://github.com/jonschlinkert/gray-matter) for extracting Markdown frontmatter
8. [RealFavIconGenerator](https://realfavicongenerator.net/) for generating favicons

**Brian #4:** [**PEP 622 -- Structural Pattern Matching**](https://www.python.org/dev/peps/pep-0622/)

- Draft status, targeted for Python 3.10
- Syntax looks similar to switch/case statement, even though two switch PEPs were rejected earlier
- Designed not only to optimize if/elif/else statements but also to focus on sequence, mapping, and object destructuring. 
- match/case statement with many allowed patterns:
	- literal pattern: would then act similar to a switch/case statement
	- name pattern: assigns expression to new variable if previous case doesn’t succeed
	- constant value pattern: enums, similar to literal
	- sequence pattern: works like unpacking assignment
	- mapping pattern: like sequence unpacking, but for mappings, like dictionaries
	- class pattern: create objects for each case and call `__match__()`
	- combining patterns: `|` for multiple patterns. including binding patterns like name
	- guards: `if expression` to further clarify a case
	- named sub-patterns: ok. still getting my head around this

**Michael #5:** [**CodeArtifact from AWS**](https://aws.amazon.com/about-aws/whats-new/2020/06/introducing-aws-codeartifact-a-fully-managed-software-artifact-repository-service/)

- via Tormod Macleod
- AWS CodeArtifact is a fully managed software artifact repository service that makes it easy for organizations of any size to securely store, publish, and share packages used in their software development process
- AWS CodeArtifact works with commonly used package managers and build tools such as Maven and Gradle (Java), npm and yarn (JavaScript), pip and twine (Python), making it easy to integrate CodeArtifact into your existing development workflows.
- Can be configured to automatically fetch software packages from public artifact repositories such as npm public registry, Maven Central, and Python Package Index (PyPI), ensuring teams have reliable access to the most up-to-date packages.


**Brian #6:** [**invoke**](https://www.pyinvoke.org/)

- suggested by Joreg Benesch
- replacement for Makefiles
- Confusion:
	- documentation is at [pyinvoke.org](http://pyinvoke.org)
	- install with `pip install invoke`
	- there’s also another pypi package, called `pyinvoke`, which is NOT what we are talking about.
- invoke:
	- task execution library
	- Write `tasks.py` files in Python for Makefile like things
	- tasks are Python functions decorated with `@task`, like

```
    @task
    def build(c, clean=False):
        if clean:
            print("Cleaning!")
        print("Building!")
    - invoke tasks with `invoke`
    $ invoke build -c
    $ invoke build --clean
- you can
    - run shell commands with `c.run()`
    - declare pre-tasks, tasks that need to run before this one. like “build” requires “clean”, etc.
- namespaces with multiple files
- tool intended for building documentation, but could probably run lots of stuff with it, like deployment, testing, etc.

Extras:

Brian:

- 

Michael:

- [From Guido](https://twitter.com/gvanrossum/status/1270487300099551232): Python 3.9.0 beta 3 is out now, for your immediate testing. Wait, what happened to beta 2? Interesting story. 
- The next pre-release, the fourth beta release of Python 3.9, will be 3.9.0b4. It is currently scheduled for 2020-06-29.

Joke:

- [**Parenting a geek**](http://geek-and-poke.com/geekandpoke/2012/11/28/parenting-a-geek.html)
![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5ee2b071b2427c53fec09f10/0f0c01ec786838aab418d385a686ad17/Screen_Shot_2020-06-11_at_1.54.07_PM.png)


