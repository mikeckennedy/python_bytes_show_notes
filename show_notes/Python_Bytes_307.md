# Python Bytes 307

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael #1:** [**Python 3.11 is released**](https://www.python.org/downloads/release/python-3110/)

- [**Live stream of the actual release procedure**](https://www.youtube.com/watch?v=PGZPSWZSkJI)
- Talk Python episode coming next week ([**live stream**](https://www.youtube.com/watch?v=Iak-6AsMLsU) on Friday)
- **Major new features of the 3.11 series, compared to 3.10**
- **General changes**
    - [PEP 657](https://www.python.org/dev/peps/pep-0657/) -- Include Fine-Grained Error Locations in Tracebacks
    - [PEP 654](https://www.python.org/dev/peps/pep-0654/) -- Exception Groups and `except*`
    - [PEP 680](https://www.python.org/dev/peps/pep-0680/) -- tomllib: Support for Parsing TOML in the Standard Library
    - [gh-90908](https://github.com/python/cpython/issues/90908) -- Introduce task groups to asyncio
    - [gh-34627](https://github.com/python/cpython/issues/34627/) -- Atomic grouping (`(?>...)`) and possessive quantifiers (`*+, ++, ?+, {m,n}+`) are now supported in regular expressions.
    - The [Faster CPython Project](https://github.com/faster-cpython/) is already yielding some exciting results. Python 3.11 is up to 10-60% faster than Python 3.10. On average, we measured a 1.22x speedup on the standard benchmark suite. See [Faster CPython](https://docs.python.org/3.11/whatsnew/3.11.html#faster-cpython) for details.
- **Typing and typing language changes**
    - [PEP 673](https://www.python.org/dev/peps/pep-0673/) -- Self Type
    - [PEP 646](https://www.python.org/dev/peps/pep-0646/) -- Variadic Generics
    - [PEP 675](https://www.python.org/dev/peps/pep-0675/) -- Arbitrary Literal String Type
    - [PEP 655](https://www.python.org/dev/peps/pep-0655/) -- Marking individual TypedDict items as required or potentially-missing
    - [PEP 681](https://www.python.org/dev/peps/pep-0681/) -- Data Class Transforms

**Brian #2:**  [**Installing Python 3.11 on Mac or Windows**](https://pythontest.com/python/installing-python-3-11/)

- pythontest.com
- I wrote this up because there are lots tutorials with weird instructions.
- For most people, I think the right answer is to use the python.org installer.
- It just works.
- One change, for Windows: Use “Advanced Options” and select “Add Python to environment variables”.
- The default process:
    - allows multiple versions, like 3.7, 3.10, 3.11, to all live side by side.
    - allows tox to use all of these
    - allows you to specify which one if you want
        - `python3.10`, for example, on mac
        - `py -3.10` on windows
    - allows you to update versions in place. Say 3.10.7 to 3.10.8, or 3.11.0 to 3.11.1 when it comes out.
- Please, blog writers, stop recommending `pyenv` to novices. It’s a cool project, but it is not a project for casual users.
- And homebrew lovers, go for it, you are not going to read my article anyway.


**Michael #4:**  [**Bossie 2022 Awards**](https://www.infoworld.com/article/3676829/the-best-open-source-software-of-2022.html)

- Notable winners
    - **Wasmtime**: Similar to what Node.js does for the JavaScript runtime, Wasmtime allows developers to leverage all of the advantages that WebAssembly provides inside the browser-including safe sandboxed execution, near-native performance, and support across multiple programming languages and platforms -outside the browser. ([**Python’s integration**](https://pypi.org/project/wasmtime/))
    - [**PyScript**](https://pyscript.net): One of the long-gestating promises of WebAssembly is enabling the use of languages other than JavaScript in the web browser. PyScript delivers a full Python runtime in the browser, allowing you to use Python in webpages as a full-blown scripting language.
    - [**Sentry**](https://talkpython.fm/sentry): Alongside security, error and performance tracing are among the most frustratingly inevitable requirements for many apps. Cue a sigh of relief. Sentry offers an entire ecosystem of open source tools for monitoring the health of applications, services, and APIs, from the server-side API for collecting data, to a dashboard for making it manageable, to a comprehensive slew of application-side integrations.
    - [**nbdev**](https://nbdev.fast.ai/): One of the dirty secrets of notebook programming, using environments like Jupyter or Google Colab, is that it produces some of the worst spaghetti code you've ever seen, with data scientists hopping from cell to cell and creating an unmaintainable mess. Some even go so far as to say that notebook programming might be as harmful as GOTO was back in the day.

**Brian #5:** [**Textual 0.2.0**](https://www.textualize.io/blog/posts/textual-0-point-2-point-0?utm_source=pocket_mylist)

- All the cool things Will has been showing off on Twitter recently are part of the css branch.
- This has been merged, and released as 0.2.0
- They also held off this release until they were happy with the documentation, which includes:
    - A new [tutorial](https://textual.textualize.io/tutorial/?utm_source=pocket_mylist) that walks through a stopwatch application and everything that goes into it.
    - An in depth [reference guide](https://textual.textualize.io/guide/?utm_source=pocket_mylist) with fully working examples, all of which are also in github, so you can play with it directly without retyping everything.

**Extras** 

Michael:

- Video I created: [**17x Faster Page Load in 30 minutes using Python, PyCharm, and MongoDB**](https://www.youtube.com/watch?v=mg8N62Xt204)
- [**Pandas Markets Calendar**](https://github.com/rsheftel/pandas_market_calendars) (by Ryan Sheftel)
- [**Beanie adds a sync API**](https://beanie-odm.dev/tutorial/sync/migrate-from-async/)
- [**DuckDuckGo browser**](https://techcrunch.com/2022/10/18/duckduckgos-beta-mac-app-is-open-to-public-with-new-features/), exciting and disappointing
- **int()** [**isn’t done yet**](https://github.com/conda-forge/python-feedstock/pull/579)
    - via Will Shanks
    - Ubuntu has decided to patch out the int limit and preserve the previous behavior on the basis that the risk factor is low and not worth breaking compatibility for.

**Joke:** [**i heard you like getters**](https://devhumor.com/media/developing-with-java-be-like)

