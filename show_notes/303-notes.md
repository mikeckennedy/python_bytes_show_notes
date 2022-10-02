# Python Bytes 303

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael #1:** [**Human regular expressions revisited**](https://github.com/mikaelho/python-human-regex)

- via Mikael Honkala
- We mentioned of Al Sweigart's humre in Python Bytes… 
- Mikael went on a little search and compiled my findings into this repo.
- A lot of people feel that re needs some help. At least 3 of the "serious" packages I found came out in the last few months.
- Since a package like this is not overly complex to make, all the ways to approach the problem are clearly being explored.
- Unfortunately these seem to be mostly single-person efforts, and many have fallen to the wayside before long.
- Hopefully there's some consolidation on the horizon, to share some of the maintenance effort and establish some of the packages as here for the long haul.
- The list could be useful to you if you are:
    - *Looking for a tool*: Check the list to get a quick idea of the "look and feel" of each package.
    - *Thinking about building a tool*: Check the list for alternative approaches, and maybe consider if contributing to an existing package might be a better way to get what you need.
    - *Building a tool, or already have one*: Use the list to clarify and communicate what the main differences and strengths of your solution are.

**Brian #2:** [**Implicit Optional Types Will Be Disabled by Default**](https://mypy-lang.blogspot.com/2022/09/mypy-0981-released.html)

- … in a future mypy feature release (possibly the next one after 0.98x) …
- Thanks Adam Johnson for spotting this and letting us know
- Stop doing this: `s: str = None`
- Do one of these:
    - `s: str | None = None`
    - `s: Union[str, None] = None` 
    - `s: Optional[str] = None` ← but this has problems
- Optional != optional
    - From [python docs](https://docs.python.org/3/library/typing.html):
        - ”`Optional[X]` is equivalent to `X | None` (or `Union[X, None]`).”
        - “Note that this is not the same concept as an optional argument, which is one that has a default. An optional argument with a default does not require the `Optional` qualifier on its type annotation just because it is optional. “
- Best described in FastAPI docs, [Python Types Intro, starting at “Possibly](https://fastapi.tiangolo.com/python-types/#possibly-none) `[None](https://fastapi.tiangolo.com/python-types/#possibly-none)`["](https://fastapi.tiangolo.com/python-types/#possibly-none)
- Recommendation is to use:
    - `s: str | None = None` for Python 3.10+
    - `s: Union[str, None] = None` for Python 3.9+
- For 3.7, 3.8, you still have `Optional` as an option, I think. 
    - Why haven’t you upgraded to 3.9? We’re almost to 3.11, what’s the problem?!

**Michael #3:** [**cython-lint**](https://github.com/MarcoGorelli/cython-lint)

- by Marco Gorelli
- A tool (and pre-commit hook) to lint Cython files, similar to how flake8 lints Python files, and works by parsing Cython's own AST (abstract syntax tree).
- Found quite a few nice clean-ups which could be applied on:
    - pandas
    - numpy
    - scikit-learn
    - cupy

**Brian #4:** [**difftastic**](https://difftastic.wilfred.me.uk/introduction.html) - structural diff

- “Difftastic is a structural diff tool that understands syntax.”
- “Difftastic [detects the language](https://difftastic.wilfred.me.uk/usage.html#language-detection), parses the code, and then compares the syntax trees.”
- Interesting story about [building difftastic](https://www.wilfred.me.uk/blog/2022/09/06/difftastic-the-fantastic-diff/?utm_source=pocket_mylist)
- For one off `git diff` replacement
    - use `GIT_EXTERNAL_DIFF=difft git diff`
    - or  `GIT_EXTERNAL_DIFF="difft --syntax-highlight=off" git diff`
- To always use `difft` with git, see https://difftastic.wilfred.me.uk/git.html

**Extras** 

Brian:

- [**Oh My Git!**](https://ohmygit.org) - An open source game about learning Git!
- [**Python 3.11.0 is up to rc2**](https://pythoninsider.blogspot.com/2022/09/python-3110rc2-is-now-available.html?utm_source=pocket_mylist)

Michael:

- [**Cppfront project aims to modernize C++**](https://www.infoworld.com/article/3674213/cppfront-project-aims-to-modernize-c.html)
- [**NextDNS**](https://nextdns.io)

**Joke:**  [**I mean, who’s wrong?**](https://twitter.com/PR0GRAMMERHUM0R/status/1570578245048729600)

