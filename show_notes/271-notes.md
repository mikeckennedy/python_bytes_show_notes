# Python Bytes 271


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: Steve Dower

**Michael #1:** [**fastapi-events**](https://github.com/melvinkcx/fastapi-events)

- Asynchronous event dispatching/handling library for FastAPI and Starlette
- Features:
    - straightforward API to emit events anywhere in your code
    - events are handled after responses are returned (doesn't affect response time)
    - support event piping to remote queues
    - powerful built-in handlers to handle events locally and remotely
    - coroutine functions (`async def`) are the first-class citizen
    - write your handlers, never be limited to just what `fastapi_events` provides

**Brian #2:** [**Ways I Use Testing as a Data Scientist**](https://www.peterbaumgartner.com/blog/testing-for-data-science/)

- Peter Baumgartner
- “In my work, writing tests serves three purposes: *making sure things work*, *documenting my understanding*, *preventing future errors*.”
- Test
    - The results of some analysis process (using assert)
    - Code that operates on data (using hypothesis)
    - Aspects of the data (using pandera or Great Expectations)
    - Code for others (using pytest)
- Use asserts liberally even within the code
    - use on as many intermediate calculations and processes as you can
    - embed expressions in f-strings as the last argument to `assert` to help debug failures
    - check calculations and arithmetic
    - check the obvious
- Notebooks: “One practice I’ve started is that whenever I *visually* investigate some aspect of my data by writing some disposable code in a notebook, I convert that validation into an assert statement.”
- utilize numpy and pandas checks, especially for arrays and floating point values
- `hypothesis` can help you think of edge cases that should work, but don’t, like empty `Series`, and `NaN` values.
- Write tests on the data itself
    - `pandera` useful for lightweight cases, checking schema on datasets.
    - Great Expectations if we’re epecting to repeatedly read new data with the same structure.
- Use `pytest`, especially for code you are sharking with other people, like libraries.
- TDD works great for API development
- Arrange-Act-Assert is a great structure.
- “Even if we’re not sure what to assert, writing a test that executes the code is still valuable. “
    - At least you’ll catch when you’ve forgotten to implement something.

**Steve** **#3:** [**PEP 654 Exception groups and except***](https://www.python.org/dev/peps/pep-0654/)

- A necessary building block for more advanced asyncio helpers
- Mainly for use by scheduler libraries to handle raising multiple errors “simultaneously”
- [except*](https://www.python.org/dev/peps/pep-0654/#except): “a single exception group can cause several except* clauses to execute, but each such clause executes at most once (for all matching exceptions from the group)”
- Necessary for complex scheduling, such as task groups

**Michael #4:** [**py-overload**](https://github.com/FelixTheC/py-overload/)

- A Runtime method override decorator.
- Python lacks method overriding (`do_it(7)` vs. `do_it(``"``7``"``)`)
- Probably due to lack of typing in the early days

Go from this:

    def _func_str(a: str):
        ...
    
    def _func_int(a: int):
        ...
    
    def func(a: Union[str, int]):
        if isinstance(a, str):
            _func_str(a)
        else:
            _func_int(a)

To this:

    @overload
    def func(a: str):
        ...
    
    @overload
    def func(a: int):
        ...


**Brian #5:** [**Next-generation seaborn interface**](https://seaborn.pydata.org/nextgen/#)

- Love the background and goals section
    - “This work grew out of long-running efforts to refactor the seaborn internals so that its functions could rely on common code-paths. At a certain point, I decided that I was developing an API that would also be interesting for external users too.”
    - “seaborn was originally conceived as a toolbox of domain-specific statistical graphics to be used alongside matplotlib.” 
        - I’ve always wondered about this
    - Some people now reach for, or learn, seaborn first.
    - As seaborn has grown, reproducing with raw matplotlib to change something seaborn doesn’t expose is sometimes painful
    - goal : “expose seaborn’s core features — integration with pandas, automatic mapping between data and graphics, statistical transformations — within an interface that is more compositional, extensible, and comprehensive.”
- I also like interface discussions that have phrases like “This is a clean namespace, and I’m leaning towards recommending `from seaborn.objects import *` for interactive usecases. But let’s not go so far just yet.”
    - I like clean namespaces, and use some of my own libs like this, but `import *` always is a red flag for me.
-  The new interface exists as a set of classes that can be acessed through a single namespace import: `import seaborn.objects as so`
- Start with `so.Plot`, add layers, like `so.Scatter()`, even multiple layers.
- layers have a `Mark` object, which defines how to draw the plot, like `so.Line` or `so.Dot`
- There’s a lot more detail in there. 
- The discussion is great. Also a neat understanding that established libraries can change their mind on APIs. This is a good way to discuss it, in the open.
- Note included at the top:
    - “This is very much a work in progress. It is almost certain that code patterns demonstrated here will change before an official release.
    - I do plan to issue a series of alpha/beta releases so that people can play around with it and give feedback, but it’s not at that point yet.”

**Steve #6:** [Compile CPython to Web Assembly](https://pythondev.readthedocs.io/wasm.html)

- Allows fully in-browser use of CPython (demo at https://repl.ethanhs.me/)
- Currently uses [Emscriptem](https://emscripten.org/docs/porting/emscripten-runtime-environment.html) as its runtime environment, to fill in gaps that browsers don’t normally offer (like an in-memory file system), or [WASI](https://github.com/bytecodealliance/wasmtime/blob/main/docs/WASI-intro.md) to more carefully add system functionality
- Still the CPython runtime, and a lot of work to do before you’ll see it as part of client-side web apps, but the possibility is now there.

**Extras** 

Michael:

- [**Get minutes, hours, and days from Python timedelta - A Python Short**](https://www.youtube.com/watch?v=xPXi3p8BvmU)
- Did you know ohmyzsh is [**kind of local**](https://www.planetargon.com/about)?  
- [**Django reformatted code with Black**](https://github.com/django/django/pull/15387) (via PyCoders)


Steve: 

- Python 3.11’s latest alpha now has Windows ARM64 installers. These aren’t the dominant devices yet, but they’re out there, and if you’ve got one the CPython team would love to hear about your experience.
- Steve just released a new version of [Deck](https://pypi.org/project/deck), which started as a way to help people who misspelled collections.deque, but has grown into a useful building block for traditional 52-card games (or 54 including jokers).

**Joke:**  [**Help is coming**](https://twitter.com/PR0GRAMMERHUM0R/status/1491336088190963713?cxt=HHwWgsC-laqRpbIpAAAA)

