# Python Bytes 337

----------

CONNECTION INFO:
**Streamyard video call/stream:     TBD**
**Zencastr HQ audio:                           TBD**
Public YouTube stream:                  TBD

----------

Intro:
Hello and Welcome to Python Bytes
Where we deliver Python news and headlines directly to your earbuds.
This is episode 337 recorded May 23, 2023
I’m Brian Okken
<and I’m Michael Kennedy>

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)
- Special guest: GUEST_PROFILE

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** ****[**Ruff PyCharm plugin**](https://github.com/koxudaxi/ruff-pycharm-plugin)

- via John Hagen
- Ruff PyCharm plugin has great integration, it will highlight Ruff lint errors in the IDE as you type and you can even apply Alt+Enter (`⌥⏎` on Mac) quick fixes through the IDE.
- Ruff will automatically fix the fixable issues. 
- John also added additional [**PyCharm-specific instructions for black/Ruff**](https://github.com/johnthagen/python-blueprint#integrate-code-formatters)

**Brian #2:**  [**Writing Python like it's Rust**](https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html)

- Kobzol
- Rust lessons guiding use of types and type hints in Python
    - Add type hints tun function signatures
    - Use dataclasses instead of tuples or dictionaries to increase clarity and type safety
    - Union types to clarify `|` typing
    - …

**Michael #****3****:** ****[**Pip 23.1 Released - Massive improvement to backtracking**](https://old.reddit.com/r/Python/comments/12n5lai/pip_231_released_massive_improvement_to/) ****

- Pip 23.1 was released last month
- Highlight the **significant improvement in backtracking** that is part of the requirement resolver process in Pip. This process involves Pip finding a set of packages that meet your requirements and whose requirements themselves don't conflict.
- Prior to Pip 20.3, the default process for Pip would allow conflicting requirements to install if they were transitive dependencies where the last one specified would be the one installed.
- Once the new resolver was turned on by default it immediately hit problems where backtracking would get stuck for a long time.
- Pip separates out the resolution logic into a library called [resolvelib](https://github.com/sarugaku/resolvelib). It had been discovered that there was a [logical error](https://github.com/sarugaku/resolvelib/issues/91) under certain circumstances, and also there was a known better backtracking technique it could employ called [backjumping](https://en.wikipedia.org/wiki/Backjumping). 
- Both of these were recently [fixed](https://github.com/sarugaku/resolvelib/pull/111) and [implemented](https://github.com/sarugaku/resolvelib/pull/113) in resolvelib, which were then vendored in to Pip 23.1.

**Brian #****4****:** [**Markdown Code Runner**](https://github.com/basnijholt/markdown-code-runner)

- `markdown-code-runner` is a Python package that automatically executes code blocks within a Markdown file, including hidden code blocks, and updates the output in-place.
- Works with Python & Bash
- see also [cog](https://cog.readthedocs.io/en/latest/index.html)

**Extras** 

Brian:

Michael:

- [Python 3.12.0a7](https://docs.python.org/3.12/whatsnew/3.12.html) is out
- `python3 -m venv --upgrade-deps venv` (via John Hagen)
- Talk submissions are now open for both remote and in-person talks at the 2023 PyConZA? The conference will be held on 5 and 6 October 2023 in Durban, South Africa. South Africa is GMT+2, so the times are convenient for Africa, Europe and much of Asia, although probably less so for the rest of the world. All details are on [za.pycon.org](http://za.pycon.org/) - via Kim van Wik

**Joke:** [**User Inyerface**](https://userinyerface.com)

