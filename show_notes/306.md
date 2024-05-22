# Python Bytes 306

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).



**Brian #1:** [**Awesome pytest speedup**](https://github.com/zupo/awesome-pytest-speedup)

- Neyts Zupan
- A checklist of best practices to speed up your pytest suite.
- as a talk at [Plone NAMUR 2022](https://www.youtube.com/watch?v=uvkSOaFYsLo)
- Measure first
- Then make sure (all items have explanations)
    -  Hardware is fast
        - use a faster computer
        - also try a self-hosted runner
            - seriously, a dedicated computer (or a few) for making test runs faster might be worth it. CI resources are usually slower in cloud than local, and even expensive VM farms are often slower. Try local 
    -  Collection is fast
        - utilize `norecursedirs` and specifying the location of the tests, either on the command line or with `[testpaths](https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-testpaths)`
    -  PYTHONDONTWRITEBYTECODE=1 is set
        - might help
    -  Built-in pytest plugins are disabled
        - try `-p no:pastebin -p no:nose -p no:doctest`
    -  Only a subset of tests are executed
        - Especially when developing or debugging, run a subset and [skip the slow tests](https://pypi.org/project/pytest-skip-slow/).
    -  Network access is disabled
        - `[pytest-socket](https://pypi.org/project/pytest-socket/)` can make sure of that
    -  Disk access is disabled
        - interesting idea
    -  Database access is optimized
        - great discussion here, including using truncate and rollback.
    -  Tests run in parallel
        - [pytest-xdist](https://pypi.org/project/pytest-xdist) or similar
- Then keep them fast
    - monitor test speed

**Michael #2:** Strive to travel without a laptop

- [**Prompt from Panic**](https://panic.com/prompt/) for SSH on iThings
- [**github.dev**](https://github.dev) for an editor on iPad
- Push to branch for continuous deployment
- BTW, Apple could just make M1 iPads boot to macOS rather than chase silly multi windowing systems (stage manager, etc, etc)


**Brian #3:** **Some fun tools from the previous testing article**

- [hyperfine](https://github.com/sharkdp/hyperfine) for timing the whole suite
-  `pytest` `--``durations 10` for finding test times of slowest 10 tests
    - leave the `10` off to find times of everything, sorted
- [pyinstrument](https://pyinstrument.readthedocs.io/en/latest/home.html) for profiling with nice tree structures
    - and [how to use it with pytest](https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-pytest-tests)
- [pytest-socket](https://pypi.org/project/pytest-socket/) disables network calls with `--disable-socket`, helping to find tests that use network calls.
- [pyfakefs](https://github.com/pytest-dev/pyfakefs), a fake file system that mocks the Python file system modules. “Using pyfakefs, your tests operate on a fake file system in memory without touching the real disk.”
- [BlueRacer.io](https://github.com/apps/blueracer-io)

**Michael #4:** [**Refurb**](https://github.com/dosisod/refurb)

- A tool for refurbishing and modernizing Python codebases
- Think of it as suggesting the pythonic line of code.
- A little sampling of what I got on Talk Python Training
    - file.py:186:25 [FURB106]: Replace `x.replace("\t", " ")` with `x.expandtabs(1)`
    - file.py:128:17 [FURB131]: Replace `del x[y]` with `x.pop(y)`
    - file.py:103:17 [FURB131]: Replace `del x[y]` with `x.pop(y)`
    - file.py:112:39 [FURB109]: Replace `not in [x, y, z]` with `not in (x, y, z)`
    - file.py:45:5 [FURB131]: Replace `del x[y]` with `x.pop(y)`
    - file.py:81:21 [FURB131]: Replace `del x[y]` with `x.pop(y)`
    - file.py:143:9 [FURB131]: Replace `del x[y]` with `x.pop(y)`
    - file.py:8:50 [FURB123]: Replace `list(x)` with `x.copy()`
- You don’t always want the change, can suppress the recommendation with either a CLI flag or comment.

**Extras** 


Michael:

- Back on [**episode 54**](https://pythonbytes.fm/episodes/show/54/pyannotate-your-way-to-the-future) in 2017 we discussed python apps in systemd daemons.
    - Multiprocessing allows for a cool way to save on server memory
    - Do the scheduled work a multiprocessing.Process
    - Here’s [**an example from Talk Python Training**](https://python-bytes-static.nyc3.digitaloceanspaces.com/glances-view.png)
- Completely rewrote [**search UI for Talk Python courses**](https://twitter.com/TalkPython/status/1580691498416615426)
- [**Google analytics is now illegal**](https://youtu.be/9K--N8frWq0)? 
- [**Fleet**](https://www.jetbrains.com/fleet/) is *finally* in public preview
- I’ll be on [**a JetBrains/PyCharm webcast**](https://blog.jetbrains.com/pycharm/2022/10/webinar-django-in-pycharm/) Thursday.

**Joke:** [**Tests pass**](https://twitter.com/PR0GRAMMERHUM0R/status/1578943360705781762)
