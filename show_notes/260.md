# Python Bytes 260

Sponsored by **Shortcut - Get started at** [**shortcut.com/pythonbytes**](http://shortcut.com/pythonbytes)

Special guest: Chris Patti

**Brian #1:** [**Using cog to update --help in a Markdown README file**](https://til.simonwillison.net/python/cog-to-update-help-in-readme)

- Simon Willison
- I’ve wanted to have a use case for Ned Batchelder’s [cog](https://nedbatchelder.com/code/cog)
    - Cog is a utility that looks for specially blocks
```
    [[[cog
    some code
    ]]]
```
and 

```
    [[[end]]]
```

- These block can be in comments, `<!-- -->` for markdown.
- When you run cog on a file, it runs the “some code” and puts the output after the middle `]]]` and before the `[[[end]]]`.
- Simon has come up with an excellent use, running `--help` and capturing the output for a `README.md` file for a CLI project.
- He even wrote a test, pytest of course, to check if the README.md needs updated.

**Michael #2:** [**An oral history of Bank Python**](https://calpaterson.com/bank-python.html)

- Bank Python implementations are effectively proprietary forks of the *entire* Python ecosystem which are in use at many (but not all) of the biggest investment banks.
- The first thing to know about Minerva is that it is built on a global database of Python objects.
    - Barbara is a simple key value store with a hierarchical key space. It's brutally simple: made just from [pickle](https://docs.python.org/3/library/pickle.html) and [zip](https://docs.python.org/3/library/zlib.html).
- Applications also commonly store their *internal* state in Barbara - writing dataclasses straight in and out with only very simple locking and transactions (if any). 
- There is no filesystem available to Minerva scripts and the little bits of data that scripts pick up has to be put into Barbara.
- Barbara also has some "overlay" features:

```
    # connect to multiple rings: keys are 'overlaid' in order of
    # the provided ring names
    db = barbara.open("middleoffice;ficc;default")
    
    # get /Etc/Something from the 'middleoffice' ring if it exists there,
    # otherwise try 'ficc' and finally the default ring
    some_obj = db["/Etc/Something"]
```

- Lots of info about modeling with classes (instruments, books, etc)
- If you understand excel you will be starting to recognize similarities. 
- In Excel, spreadsheets cells are also updated based on their dependencies, also as a directed acyclic graph. Dagger allows people to put their Excel-style modelling calculations into Python, write tests for them, control their versioning without having to mess around with files like CDS-OF-CDS EURO DESK 20180103 Final (final) (2).xlsx. 
- Dagger is a key technology to get financial models out of Excel, into a programming language and under tests and version control.
- Time to drop a bit of a bombshell: the source code is in Barbara too, not on disk. Remain composed. It's kept in a special Barbara ring called sourcecode.
- Interesting table structures, like Pandas, but closer to a DB (MnTable)
- Over time the divergence between Bank Python and Open Source Python grows. Technology churns on both sides, much faster outside than in of course, but they do not get closer.
- Minerva has its own IDE - no other IDEs work if you keep your source files in a giant global database. 
- What I can't understand is why it contains its own web framework. Investment banks have a one-way approach to open source software: (some of) it can come in, but none of it can go out
- BTW, I “read” this with [**naturalreaders app**](https://www.naturalreaders.com/)

C**hris #3:** [**Pyxel**](https://github.com/kitao/pyxel)

- Pyxel is a ‘retro gaming console’ written in Python!
- This might seem old and un-shiny, but the restrictions imposed by the environment gift **simplicity**
    - Vastly decreased learning time and effort compared to something like Unity or even Pygame
    - Straight forward simple commands, just like it was for micro-computers in the 80s
        - cls(), line(), rect(), circ() etc.
- Pyxel is somewhat more Python and less console than others like PICO-8 or TIC-80 but this is a feature! Use your regular development environment to build.


**Brian #4:** [**How to Ditch Codecov for Python Projects**](https://hynek.me/til/ditch-codecov-python)

- Hynek Schlawack
- Codecov is a third party service that checks your coverage output and fails a build if coverage dropped. 
- It’s not without issues.
- Hynek is using [coverage.py](https://coverage.readthedocs.io/) `--fail-under` flag in place of this in GitHub actions.
- It’s not as simple as just adding a flag if you are using `--parallel` to combine coverage for multiple test runs into one report.
- Hynek is utilizing the coverage output as an artifact for each test, then pulling them all together in a `coverage` stage combine and check coverage.
- He provides the snippet of GH Action, and even links to a [working workflow file](https://github.com/hynek/structlog/blob/main/.github/workflows/main.yml) using this process. Nice!

**Michael #5:** [**tiptop (like glances)**](https://github.com/nschloe/tiptop)

-  via Zach Villers
- tiptop is a command-line system monitoring tool in the spirit of [top](https://en.wikipedia.org/wiki/Top_(software)). It displays various interesting system stats, graphs it, and works on all operating systems.
- Really nice visualization for your servers
- Good candidate for **pipx** install tiptop

**Chris #6:** [**pyc64**](https://github.com/irmen/pyc64)

- A Commodore 64 emulator written in pure Python!
- Not 100% complete - screen drawing is PETSCII character mode only
    - This still allows for a lot of interesting apps & exploration
- Actual machine emulation using [py65](https://github.com/mnaberez/py65) - a pure Python 6502 chip emulator!
- You can pop to a Python REPL from inside the emulator and examine data structures like memory, registers, etc!
- An incredible example of what Python is capable of
- 0.6 Mhz with CPython and over 2Mhz with pypy!



**Extras**


Michael:

- Michael’s [**FlaskCon 2021 HTMX Talk**](https://twitter.com/FlaskCon/status/1461245426082799618)

**Chris**: 

- [Amazon OpsTech IT is hiring!](https://amazon.jobs/en/internal/search?offset=0&result_limit=10&sort=relevant&distanceType=Mi&radius=1024km&hiring_manager[]=Sean%20Stewart%20(zjamste)&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&) (If deemed appropriate :)
[](https://amazon.jobs/en/internal/search?offset=0&result_limit=10&sort=relevant&distanceType=Mi&radius=1024km&hiring_manager[]=Sean%20Stewart%20(zjamste)&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&)

**Joke:**  [**I hate how the screens get bright so early this time of year**](https://www.newyorker.com/cartoons/daily-cartoon/wednesday-november-17th-daylight-saving-screens)

