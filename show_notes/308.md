# Python Bytes 308

Sponsored by ****[**Complier Podcast from RedHat**](https://pythonbytes.fm/compiler)

**Michael #0**: New livestream time - **11am PT on Tuesdays**. Also, subscribe to [**the youtube channel**](https://pythonbytes.fm/youtube) and “hit the bell” to get notified of all the live streams.

**Brian #1:** **It’s PyCon US 2023 CFP time**

- Will be held in Salt Lake City, Salt Palace Convention Center
- Talks are Friday - Sunday, April 19-23
- [PyCon US 2023 launch announcement](https://pycon.blogspot.com/2022/10/pycon-us-2023-launches.html)
- [PyCon 2023](https://us.pycon.org/2023/) site features images taken from past PyCon artwork
- [Call for proposals](https://us.pycon.org/2023/speaking/guidelines/) open until Dec 9, but please don’t wait that long.


**Michael #2:** [**Any.io**](https://anyio.readthedocs.io/en/stable/index.html)

- AnyIO is an asynchronous networking and concurrency library that works on top of either [asyncio](https://docs.python.org/3/library/asyncio.html) or [trio](https://github.com/python-trio/trio). It implements trio-like [structured concurrency](https://en.wikipedia.org/wiki/Structured_concurrency) (SC) on top of asyncio.
- Cool [**interpretability**](https://anyio.readthedocs.io/en/stable/threads.html#working-with-threads) between native threads and asyncio
- [**Using subprocesses**](https://anyio.readthedocs.io/en/stable/subprocesses.html): AnyIO allows you to run arbitrary executables in subprocesses, either as a one-shot call or by opening a process handle for you that gives you more control over the subprocess.
- [**Async file I/O**](https://anyio.readthedocs.io/en/stable/fileio.html#asynchronous-file-i-o-support): AnyIO provides asynchronous wrappers for blocking file operations. These wrappers run blocking operations in worker threads.
- [**Cool synchronization primitives**](https://anyio.readthedocs.io/en/stable/synchronization.html) too.
- Catch the Talk Python episode with Alex: [**talkpython.fm/385**](https://talkpython.fm/episodes/show/385/higher-level-python-asyncio-with-anyio)

**Brian #4:** [**How to propose a winning conference talk**](https://lerner.co.il/2022/10/19/how-to-propose-a-winning-conference-talk/) ****

- Reuven Lerner
- Some nice tips and advice
- Build a list of topics 
    - If you train, teach, mentor, lead, or coach already:
        - what questions to people always ask you?
        - what knowledge would help people to have?
        - where do people seem to just “not get it”?
    - If you don’t train or teach, then maybe hit up Stack Overflow…
    - From Brian: I think you can imagine yourself a year or two ago and think about stuff you know now you wish you knew then and could learn faster.
- Build an outline with times 
    - This part often seems scary, but Reuven’s example is 10 bullets with (x min) notes. 
- Write up a summary. One short, one longer.
    - Indicate who will benefit, what they will come out knowing, and how it will help them.
- Propose to multiple conferences. Why not?
- Practice
- (from Brian: Even if you get rejected, you’ve gained. Turn it into a youTube video or blog post or both.)
- 

**Michael #5:** [**Sanic release adds background workers**](https://sanic.dev/en/)

- via Felix
- In v22.9 (go cal-ver!), the main new feature is the [worker process management](https://sanic.dev/en/guide/release-notes/v22.9.html#important-new-worker-manager) - the main Sanic process handles a pool of workers. 
- They are normally used for handling requests but you can also use them to handle background jobs and similar things. You could probably use it for a lot of the reasons people turn to something like Celery.
- The lead developer (Adam Hopkins) [**has written a blog post**](https://amhopkins.com/posts/background-job-worker.html) about this feature.
- MK: Sanic has been flying a bit under my radar. Maybe time to dive into it a bit more.


**Extras** 

Brian: 

- [**Create Presentation from Jupyter Note**](https://mljar.com/blog/jupyter-notebook-presentation/)[**book**](https://mljar.com/blog/jupyter-notebook-presentation/)
    - Cool walkthrough of how to use the built in slideshow features of Jupyter Notebooks.
- [pytest 7.2.0 is out](https://docs.pytest.org/en/7.2.x/changelog.html)
    - No longer depends on the `py` library. So if you do, you need to add it to your dependencies. 
    - `nose` officially deprecated, which includes `setup()` and `teardown()`. Really glad I dropped the “x unit” section on the [2nd edition of the pytest book](https://pythontest.com/pytest-book/). 
    - `testpaths` now supports shell-style wildcards
    - Lots of other improvements. check out the change log

Michael:

- [**Rich on pyscript**](https://jeff.glass/project/richdemo/) (via Matt Kramer)
- [**Python 3.11 in 100 seconds video**](https://youtu.be/8NQGZA1wWiQ) from Michael

**Joke:** [**Deep questions**](https://twitter.com/PR0GRAMMERHUM0R/status/1585285144407162880) & [**Relationship advice from geeks**](https://twitter.com/i/topics/848921413196984320?pt=1586795095147565056)

