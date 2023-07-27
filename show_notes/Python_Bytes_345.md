# Python Bytes 345

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- The [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Cython 3.0**](https://www.infoworld.com/article/3702888/cython-30-the-next-generation-of-python-at-the-speed-of-c.html)

- Long in development, the new major release of the Python-to-C compiler sheds legacy Python support and readies Cython developers for big changes in Python.
- Cython 3 cleans up and modernizes Cython.
- Pure Python mode allows Python developers to use their existing Python linting and code analysis tools on Cython.

**Brian #2:** [**Reading code**](https://mostlypython.substack.com/p/reading-code) [:](https://mostlypython.substack.com/p/reading-code) [**An important but seldom-discussed skill**](https://mostlypython.substack.com/p/reading-code)

- Eric Matthes
- A cool walk through of several techniques to read code
- Strategies
    - Ignore function definitions
        - And in the example, also ignore comments
    - Simplify repetitive blocks
        - Examples shows mentally lumping a bunch of print statements into “print message”
    - Utilize IDE tools, like folding to hide functions your not looking at
- Also includes a note about writing readable code.
- Notes: 
    - People believe your function and variable names, they should be descriptive, and they should not be deceptive.

**Michael #3:** [**Major new version of MicroPython: v1.20.0**](https://github.com/micropython/micropython/releases/tag/v1.20.0)
[](https://github.com/micropython/micropython/releases/tag/v1.20.0)
- [via Matt Trentini](https://twitter.com/matt_trentini/status/1651425308502032385)
- >10 months, >1000 mainline commits from >100 contributors
- This release of MicroPython introduces a new lightweight package manager called mip.
- In the MicroPython runtime, core/built-in types have been compressed by only including in the C-level type struct as many slots for C function pointers as is needed for a given type → 
    - Any third-party C extensions will need to be updated to work with this change.
- Massive list of detailed changes.

**Brian #4:** [**Advanced Python Tips for Development**](https://dev.to/scofieldidehen/advanced-python-tips-for-development-olo)

- Scofield Idehen
- There’s 15 in the article, here’s a few
    - 1 & 2. Use List Comprehensions and Generator Expressions.
        - It’s cool to see them side by side
    - 3. `enumerate()` is fun
    - 5. Embrace `zip()`. It’s weird, but very useful.
    - 12. Utilize slots to Reduce Memory Usage 
    

**Extras** 

Brian:

- Hear the story behind the quote “I came for the language, but I stayed for the community.” and learn about fountain pens, tea, and a Murderbot, on this week‘s [**Python People**](https://pythonpeople.fm/episodes/brett-cannon).


Michael:

- Search (LLM like) Talk Python: [**explore-talk-python-to-me.streamlit.app**](https://explore-talk-python-to-me.streamlit.app) by [Aguss](https://github.com/plaguss)

**Joke:** 

- [**You’re full stack now**](https://twitter.com/htmx_org/status/1681322091650629632)
- Seriously, take [the HTMX course](https://training.talkpython.fm/courses/htmx-flask-modern-python-web-apps-hold-the-javascript) :)

