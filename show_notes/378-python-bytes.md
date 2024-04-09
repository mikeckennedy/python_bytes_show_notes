# Python Bytes 378

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Brian #1:** [**pacemaker**](https://github.com/brohrer/pacemaker) - For controlling time per iteration loop in Python.

- Brandon Rohrer
- Good example of a small bit of code made into a small package.
- With speedups to dependencies, like with uv, for example, I think we’ll see more small projects.
- Cool stuff
  - Great README, including quirks that need to be understood by users. 
    - “If the pacemaker experiences a delay, it will allow faster iterations to try to catch up. Heads up: because of this, any individual iteration might end up being much shorter than suggested by the pacemaker's target rate.”
  - Nice use of [time.monotonic()](https://docs.python.org/3/library/time.html#time.monotonic)
    - deltas are guaranteed to never go back in time regardless of what adjustments are made to the system clock.
- Watch out for
  - pip install pacemaker-lite
    - NOT pacemaker
    - pacemaker is taken by a package named PaceMaker with a repo named pace-maker, that hasn’t been updated in 3 years. Not sure if it’s alive. 
  - No tests (yet). I’m sure they’re coming. ;)
    - Seriously though, Brandon says this is “a glorified snippet”. And I love the use of packaging to encapsulate shared code. Realistically, small snippet like packages have functionality that’s probably going to be tested by end user code.
    - And even if there are tests, users should test the functionality they are depending on.

**Michael #2:** [PyPI suspends new user registration to block malware campaign](https://www.bleepingcomputer.com/news/security/pypi-suspends-new-user-registration-to-block-malware-campaign/)

- [Incident Report for Python Infrastructure](https://status.python.org/incidents/dc9zsqzrs0bv)
- [PyPi Is Under Attack: Project Creation and User Registration Suspended — Here’s the details](https://medium.com/checkmarx-security/pypi-is-under-attack-project-creation-and-user-registration-suspended-heres-the-details-c3b6291d4579)
  - I hate medium, but it’s the best details I’ve found so far

**Brian #3:** [**Python Project-Local Virtualenv Management Redux**](https://hynek.me/articles/python-virtualenv-redux/)

- Hynek
- Concise writeup of how Hynek uses various tools for dealing with environments
- Covers (paren notes are from Brian)
  - In project .venv directories
  - direnv for handling .envrc files per project (time for me to try this again)
  - uv for pip and pip-compile functionality
  - Installing Python via python.org
  - Using a .python-version-default file (I’ll need to play with this a bit)
    - Works with GH Action setup-python. (ok. that’s cool)
  - Some fish shell scripting
  - Bonus tip on using requires-python in .pyproject.toml and extracting it in GH actions to be able to get the python exe name, and then be able to pass it to Docker and reference it in a Dockerfile. (very cool)

**Michael #4:** [Python Edge Workers at Cloudflare](https://blog.cloudflare.com/python-workers)

- What are [edge workers](https://developers.cloudflare.com/workers/)?
- Based on workers using Pyodide and WebAssembly
- This new support for Python is different from how Workers have historically supported languages beyond JavaScript — in this case, we have directly integrated a Python implementation into [workerd](https://github.com/cloudflare/workerd), the open-source Workers runtime.
- Python Workers can import a subset of popular Python [packages](https://developers.cloudflare.com/workers/languages/python/packages/) including [FastAPI](https://fastapi.tiangolo.com/), [Langchain](https://python.langchain.com/docs/get_started/introduction), [numpy](https://numpy.org/)
- Check out the [examples repo](https://github.com/cloudflare/python-workers-examples).

**Extras** 

Michael:

- [LPython follow up](https://fosstodon.org/@btskinn/112226004327304352) from Brian Skinn
- [Featured on Python Bytes badge](https://github.com/epogrebnyak/justpath/issues/26)
- [A little downtime](https://twitter.com/TalkPython/status/1777505296807850101), thanks for the understanding
  - We were rocking a [99.98% uptime](https://python-bytes-static.nyc3.digitaloceanspaces.com/python-bytes-health.png) until then. :)

**Joke:** 

- [C++ is not safe for people under 18](https://devhumor.com/media/gemini-says-that-c-is-not-safe-for-people-under-18)
- Baseball joke