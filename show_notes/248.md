# Python Bytes 248

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Paul Everitt**

**Brain #1:** [**Why I use attrs instead of pydantic**](https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/)

- **Tin Tvrtković,** [@tintvrtkovic](https://twitter.com/tintvrtkovic)
- attrs vs dataclasses
	- Since dataclasses are a strict subset of attrs functionality. Recommend using attrs in most cases over dataclasses
	- attrs is faster, has more features, releases more frequently, offers over a wider range of Python versions.
- attrs vs Pydantic 
	- attrs is a library for generating the boring parts of writing classes; 
		- Pydantic is that but also
	    - a complex validation library.
	    - a structuring/unstructuring library, ex converting to json and back
	- attrs has opt-in validation that you have more control over
	- cattrs can be used for structuring/unstructuring
	- converters are opt-in for attrs, built into Pydantic, and can be wrong.
		- example using Pendulum that Pydantic mishandles
- Summary
	- attrs + cattrs + validators where necessary, converters where necessary
	- will be faster
	- you’ll have more control
	- Kind of a “small, sharp, specialized tools” vs “swiss army knife” comparison.

**Michael #2:**  [**mclfy**](https://twitter.com/whereismyjetpac/status/1430694757320347648)

- via __dann__
- Mcfly is an incredible Ctrl+r replacement
- McFly replaces your default `ctrl-r` shell history search with an intelligent search engine that takes into account your working directory and the context of recently executed commands. 
- McFly's suggestions are prioritized in real time with a small neural network.
- Features
	- Rebinds `ctrl-r` to bring up a full-screen reverse history search prioritized with a small neural network.
	- Augments your shell history to track command exit status, timestamp, and execution directory in a SQLite database.
	- Maintains your normal shell history file as well so that you can stop using McFly whenever you want.
	- Includes a simple action to scrub any history item from the McFly database and your shell history files.
	- Designed to be extensible for other shells in the future.
	- Written in Rust, so it's fast and safe.

**Paul #3: Textual and** [**boilerplate removal**](https://twitter.com/willmcgugan/status/1426267903733768193)

- In the race to make Textual the most talked-about package in Python Bytes history…
- I’d like to zoom in on a Twitter discussion he had about removing boilerplate
- I have traditionally been opposed to the convention-over-configuration approach that most successful Python projects have taken
- I dislike magic variable and file names, prefer explicit is better than implicit, actual *symbols*
- Lately, because of…tooling
- But Will’s approach to “boilerplate removal” is compelling, as it remains mypy friendly
- Still, I find it flawed…code meant to be read 2 years from now…that stuff that is implied-away, worries me
- Will is great at working-in-the-open, being a gentle, encouraging public figure

**Brian #4:** [**xdoctest**](https://github.com/Erotemic/xdoctest) 

- “The `xdoctest` package is a re-write of Python's builtin `doctest` module. It replaces the old regex-based parser with a new abstract-syntax-tree based parser (using Python's `ast` module). The goal is to make doctests easier to write, simpler to configure, and encourage the pattern of test driven development.”
- “The main enhancements `xdoctest` offers over `doctest` are:
	1. All lines in the doctest can now be prefixed with `>>>`.  Old-style doctests with `...` are still valid.
	2. Additionally, the multi-line strings don't require any prefix (but its ok if they do have either prefix).
	3. Tests are executed in blocks, rather than line-by-line, thus comment-based directives (e.g. `# doctest: +SKIP`) are now applied to an entire block, rather than just a single line.
	4. Tests without a "want" statement will ignore any stdout / final evaluated value. This makes it easy to use simple assert statements to perform checks in code that might write to stdout.
	5. If your test has a "want" statement and ends with both a value and stdout, both are checked, and the test will pass if either matches.
	6. Output from multiple sequential print statements can now be checked by a single "got" statement. (new in 0.4.0).”
- Features I love
	- “The new got/want tester is very permissive by default; it ignores differences in whitespace”
	- You can make doctest normalize whitespace, but why should you have to?

**Michael #5:** [**Automate the standing desk with python**](https://medium.com/@davidkongfilm/how-i-hacked-my-standing-desk-with-a-raspberry-pi-a50ed14c7f6f)

- via Joe Riedley, by David Kong
- “When I first started using it, I was very excited, but I quickly found myself sitting all day, in spite of the fancy desk.”
- I took off a few screws and … voila! A row of pins neatly exposed right in front.
- The pins in my control box, when connected correctly, simulate the pressing of the buttons on the front of the box.
- [**Raspberry Pi Zero**](https://www.raspberrypi.org/products/raspberry-pi-zero/), the simplest, most basic version. It doesn’t have all the bells and whistles, but it does everything I needed for this simple project, and it’s just $5(!).
- And the code
```
    from gpiozero import LED # The LED library allows easy pin control
    from time import sleep
    import randomrelay = LED(17) # I connected the relay to pin 17 and groundwhile True:
            relay.on()
            sleep(1)
            relay.off()
            sleep(random.randint(45, 60) * 60)
```

**Paul #6:** [**Hypermodern Python Cookiecutter**](https://cookiecutter-hypermodern-python.readthedocs.io/en/2021.4.15/)

- I’ve been noodling with some code the last two years about bringing frontend DX to Python web dev
- Learning and talking more than adoption
- Running a modern Python project is a LOT of housekeeping
- Hypermodern Python Cookiecutter from Claudio Jolowicz teleported me to a state of the art I was looking for
- Poetry, Nox, GHA, pre-commit, flake8, PyPI uploads from CI, release drafter, Black, prettier, pytest, mypy, Sphinx and friends, GitHub labeler
- It’s NOT AT ALL just a cookiecutter
- The best part…it’s an enormously-detailed user guide, some blog posts with the “why”, it’s actively maintained
- The PR workflow is really well explained and wired up
- This could be…a course, a webinar
- Thanks Claudio

**Extras**

Michael:

- [**ActiveState's 2021 Software Supply Chain Security Survey**](https://www.surveymonkey.com/r/secure-your-supply-chain)
- [**Python 3.9.7 and 3.8.12 are now available**](https://pythoninsider.blogspot.com/2021/08/python-397-and-3812-are-now-available.html)
- From Shlomi Lanton, on your #2 Brian talked about having a history of all files to find the ones that were updated last, so I created [**granpa**](https://github.com/shlomiLan/grampa) 
- caffinate: you mentioned the MacOS `/usr/bin/caffeinate` tool on "[https://pythonbytes.fm/episodes/show/247/do-you-dare-to-press-](https://t.co/oNU0ltVclf?amp=1).". Follow `caffeinate` with long-running command to keep awake until done (`caffeinate python -c 'import time; time.sleep(10)'`), or `caffeinate -w "$PID"` for an already running task. - via [Nathan Henrie](https://twitter.com/n8henrie)
- Also: [**wakepy**](https://github.com/np-8/wakepy) now works correctly on macOS

**Joke:** [**Meaning**](https://twitter.com/ismonkeyuser/status/1430413027950612481/)
