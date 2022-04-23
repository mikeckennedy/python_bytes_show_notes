# Python Bytes 275

Sponsored by [**Microsoft for Startups Founders Hub**](https://pythonbytes.fm/foundershub).

Special guest: [**Emily Morehouse-Valcarcel**](https://twitter.com/emilyemorehouse)

**Michael #1:** [**Async and await with subprocesses**](https://fredrikaverpil.github.io/2017/06/20/async-and-await-with-subprocesses/)

- by [**Fredrik Averpil**](https://fredrikaverpil.github.io/)
- People know I do all sorts of stuff with async
- Lots of cool async things are not necessarily built into Python, but our instead third-party packages
- E.g. files via [aiofiles](https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio)
- But asyncio has `asyncio.create_subprocess_exec` 
- Fredrik’s article has some nice examples
- I started using this for mp3 uploads and behind the scenes processing for us

**Brian #2:** [**Typesplainer**](https://typesplainer.herokuapp.com/)

- Arian Mollik Wasi, [@wasi_master](https://twitter.com/wasi_master) 
- Suggested by Will McGugan
- Now released [a vscode extension](https://twitter.com/wasi_master/status/1503103913070764032) for that! Available on vscode as typesplainer

**Emily** **#3:**  [**Ibis Project**](https://ibis-project.org/ibis-for-sql-programmers/)

- via [Marlene Mhangami](https://twitter.com/marlene_zw)
- “Productivity-centric Python data analysis framework for SQL engines and Hadoop” focused on:
    - Type safety
    - Expressiveness
    - Composability
    - Familiarity
- Marlene wrote an excellent [blog post](https://marlenemhangami.com/an-introduction-to-ibis-for-python-programmers) as an introduction
- Works with tons of different [backends](https://ibis-project.org/backends/), either directly or via compilation
    - Depending on the backend, it actually uses [SQLAlchemy](https://www.sqlalchemy.org/) under the hood
- There’s a ton of options for interacting with a SQL database from Python, but Ibis has some interesting features geared towards performance and analyzing large sets of data. It’s a great tool for simple projects, but an excellent tool for anything data science related since it plays so nicely with things like pandas

**Michael #4:** [**ASV**](https://asv.readthedocs.io/en/stable/)

- via Will McGugan
- AirSpeed Velocity (asv) is a tool for benchmarking Python packages over their lifetime.
- Runtime, memory consumption and even custom-computed values may be tracked.
- See [quickstart](https://asv.readthedocs.io/en/stable/using.html)
- Example of [astropy here](https://asv.readthedocs.io/en/stable/using.htmlhttps://www.astropy.org/astropy-benchmarks/).
- [Finding a commit that produces a large regression](https://asv.readthedocs.io/en/stable/using.html#finding-a-commit-that-produces-a-large-regression)

**Brian #5:** [**perflint**](https://github.com/tonybaloney/perflint)

- Anthony Shaw
- pylint extension for performance anti patterns
    - curious why a pylint extension and not a flake8 plugin.
- I think the normal advice of “beware premature optimization” is good advice.
- But also, having a linter show you some code habits you may have that just slow things down is a nice learning tool.
- Many of these items are also not going to be the big show stopper performance problems, but they add unnecessary performance hits.
- To use this, you also have to use pylint, and that can be a bit painful to start up with, as it’s pretty picky.
    - Tried it on a tutorial project today, and it complained about any variable, or parameter under 3 characters. Seems a bit picky to me for tutorials, but probably good advice for production code.
    - These are all configurable though, so you can dial back the strictness if necessary.
- perflint checks:
    - W8101 : Unnessecary list() on already iterable type
    - W8102: Incorrect iterator method for dictionary
    - W8201: Loop invariant statement (loop-invariant-statement) ←- very cool
    - W8202: Global name usage in a loop (loop-invariant-global-usage)
    - R8203 : Try..except blocks have a significant overhead. Avoid using them inside a loop (loop-try-except-usage).
    - W8204 : Looped slicing of bytes objects is inefficient. Use a memoryview() instead (memoryview-over-bytes)
    - W8205 : Importing the "%s" name directly is more efficient in this loop. (dotted-import-in-loop)

**Emily** **#6:** [**PEP 594 Acceptance**](https://peps.python.org/pep-0594/)

- “Removing dead batteries from the standard library”
- Written by [Christian Heimes](https://twitter.com/christianheimes) and [Brett Cannon](https://twitter.com/brettsky) back in 2019, though the conversation goes back further than that
    - It’s a very thin line for modules that might still be useful to someone versus the development effort needed to maintain them. 
- Recently accepted, targeting Python 3.11 (final release planned for October 2022, development begins in May 2021. See the [full release schedule](https://peps.python.org/pep-0664/))
- Deprecations will begin in 3.11 and modules won’t be fully removed until 3.13 (~October 2024)
- See the [full list of deprecated modules](https://peps.python.org/pep-0594/#deprecated-modules)
- Bonus: new [PEP site and theme](https://twitter.com/brettsky/status/1501671557503983617)!

**Extras** 

Brian:
Michael:

Emily: 

- Riff off of one of Brian’s topics from last week:
    - Automate your interactive rebases with [fixups and auto-squashing](https://thoughtbot.com/blog/autosquashing-git-commits)
- Cool award that The PSF just received: https://twitter.com/di_codes/status/1503186146137980930
- [PSF Spring Fundraiser](https://psfmember.org/civicrm/contribute/transact?reset=1&id=37)
- Cuttlesoft is hiring! https://cut.tl/careers

**Jokes:** 

- [**Changing \**](https://twitter.com/tenderlove/status/1498354428734107649) (via Ruslan)
- [Please hire me](https://twitter.com/PR0GRAMMERHUM0R/status/1502962705023520776)
