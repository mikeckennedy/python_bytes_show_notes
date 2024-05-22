# Python Bytes 372
Sponsored by ScoutAPM: [**pythonbytes.fm/scout**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

First, we are **likely skipping next week** folks. I’ll be at [PyCon Philippines](https://pycon-2024.python.ph).

**Brian #1:** [uv: Python packaging in Rust](https://astral.sh/blog/uv)

- [Suggested by Collin Sullivan](https://fosstodon.org/@sullivancolin/111937429156415001)
- “uv is designed as a drop-in replacement for pip and pip-tools”
- Intended to support the `pip` and `pip-tools` APIs, just use `uv pip` instead.
- Oh yeah, also replaces `venv` and `virtualenv`.
- And it’s super zippy, as you would expect.
- I’m still getting used to it
    - `uv pip venv` didn’t have `--prompt` at first. But that’s fixed. should get released soon.
        - first thing I tried
    - `uv pip install ./` and `uv pip install pytest` 
        - second. worked awesome
    - `uv pip list` 
        - third thing I tried
        - not there either, but `uv pip freeze` is similar.
        - Issue already filed
- Seriously, I’m excited about this. It’s just that it seems I wasn’t the target workflow for this.
- See also
    - [tox-uv](https://github.com/tox-dev/tox-uv) - speed up tox with uv
    - `[rye](https://lucumr.pocoo.org/2024/2/15/rye-grows-with-uv/)` [from Armin Ronacher, will be supported by Astral](https://lucumr.pocoo.org/2024/2/15/rye-grows-with-uv/)
    [](https://fosstodon.org/@sullivancolin/111937429156415001)- MK: 
    - Switched to this for dev. It’s excellent.
    - For some reason, doesn’t work on Docker?
    - [From Henry](https://twitter.com/HenrySchreiner3/status/1758702295267561608)

**Michael #2:** [**jpterm**](https://fosstodon.org/@davidbrochart@mastodon.top/111926774664674897)

- via David Brochart
- [jpterm](https://github.com/davidbrochart/jpterm) is a JupyterLab-like environment running in the terminal. 
- What sets `jpterm` apart is that it builds on the shoulders of giants, one of which is [Textual](https://textual.textualize.io/).
- It is designed similarly to JupyterLab, where everything is a plugin.

**Brian #3:** [Everything You Can Do with Python's textwrap Module](https://martinheinz.dev/blog/108)

- Martin Heinz
- Nice quick demo of one of my favorite builtin modules.
- Features
    - `shorten` text and insert placeholders
    - `wrap` can split lines to the same length
        - but can also just split a string into equal chunks for batch processing
    - `TextWrapper` class does all sorts of fancy stuff.
    - `dedent` is my fave. Awesome for including a multiline string in a test function as an expected outcome.

**Michael #4:** [HTML First](https://html-first.com)

- HTML First is a set of guidelines for making it **easier**, **faster** and more **maintainable** to build web software
- Principles
    1. Leveraging the default capabilities of modern web browsers.
    2. Leveraging the extreme simplicity of HTML's attribute syntax.
    3. Leveraging the web's ViewSource affordance.
- Practices
    - [Prefer Vanilla approaches](https://html-first.com/#vanilla-approaches)
    - [Use HTML attributes for styling and behaviour](https://html-first.com/#attributes-for-styling-behaviour)
    - [Use libraries that leverage HTML attributes](https://html-first.com/#attributes-for-libraries)
    - [Avoid Build Steps](https://html-first.com/#build-steps)
    - [Prefer Naked HTML](https://html-first.com/#naked-html)
    - [Be View-Source Friendly](https://html-first.com/#view-source)

**Extras** 

Brian:

- [pytest 8.0.1 released](https://github.com/pytest-dev/pytest/releases/tag/8.0.1). Fixes the parametrization order reversal I mentioned a couple episodes ago, plus some other fixes. 
- [Learn about dependency injection from Hynek](https://www.youtube.com/watch?v=uWTvMCra-_Y)
- If you want to jump into some Rust to help speed up Python tools, maybe check out [yarr.fyi](https://yarr.fyi)
    - I just interviewed Nicole, the creator, for [Python Test,](https://podcast.pythontest.com) and this looks pretty cool
    - Her episode should come out in a couple of weeks.
- Ramping up more interviews for [Python People](https://pythonpeople.fm). So please let me know if you’d like to be on the show or if you have suggestions for people you’d like me to interview.
- Also, I know this is weird, some people are still on X, and not like “didn’t close their account when they left”, but actually still using it. This is ironically a reverse of X-Files. “I don’t want to believe”. However, [I’ve left my account open](https://twitter.com/brianokken) for those folks. I check it like twice a month. But eventually I’ll see it if you DM me. But really, there are easier ways to reach me. 

Michael:

- [PyData Pittsburg CFP](https://twitter.com/fishnets88/status/1757499232892698740)
- Wyden: [Data Broker Used Abortion Clinic Visitor Location Data](https://www.techdirt.com/2024/02/15/wyden-data-broker-used-abortion-clinic-visitor-location-data-to-help-send-targeted-misinformation-to-vulnerable-women/) To Help Send Targeted Misinformation To Vulnerable Women
- SciPy 2024 - [Call for Proposals](https://cfp.scipy.org/2024/cfp)

**Joke:**  [Yeti tumbler](https://www.reddit.com/r/programminghumor/comments/196ryaa/yeti_tumblers/)

