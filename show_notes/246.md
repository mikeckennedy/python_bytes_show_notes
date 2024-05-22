# Python Bytes 246

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**David Smit**](https://twitter.com/davidouglasmit)

**Brain #1:** [**mktestdocs**](https://github.com/koaning/mktestdocs)

- [Vincent D. Warmerdam](https://twitter.com/fishnets88)
- [Tutorial with videos](https://calmcode.io/labs/mktestdocs.html)
- Utilities to check for valid Python code within markdown files and markdown formatted docstrings.
- Example:

```
    import pathlib
    import pytest
    
    from mktestdocs import check_md_file
    
    @pytest.mark.parametrize('fpath', pathlib.Path("docs").glob("**/*.md"), ids=str)
    def test_files_good(fpath):
        check_md_file(fpath=fpath)
```

- This will take any codeblock that starts with *```python* and run it, checking for any errors that might happen. 
- Putting `assert` statements in the code block will actually check things.
- Other examples in README.md for markdown formatted docstrings from functions and classes.
- Suggested usage is for code in mkdocs documentation.
- I’m planning on trying it with blog posts.

**Michael #2:** [Redis powered queues](https://twitter.com/shacker/status/1242509337517580288) (QR3)

- [via Scot Hacker](https://twitter.com/shacker/status/1242509337517580288)
- QR queues store serialized Python objects (using [cPickle](http://docs.python.org/library/pickle.html) by default), but that can be changed by setting the serializer on a per-queue basis.
- There are a few constraints on what can be pickled, and thus put into queues
- Create a queue:
-  `bqueue = Queue('brand_new_queue_name', host='localhost', port=9000)`
- Add items to the queue

```
    >> bqueue.push('Pete')
    >> bqueue.push('John')
    >> bqueue.push('Paul')
    >> bqueue.push('George')
```

- Getting items out

```
    >> bqueue.pop()
    'Pete'
```

- Also supports **deque**, or double-ended queue, capped collections/queues, and **priority queues**.

**David #3:**  **[25 Pandas Functions You Didn’t Know Existed](https://towardsdatascience.com/25-pandas-functions-you-didnt-know-existed-p-guarantee-0-8-1a05dcaad5d0)**

- Bex T
- So often, I come across a pandas method or function that makes me go “AH!” because it saves me so much time and simplifies my code
	- Example: Transform
- Don’t normally like these articles, but this one had several “AH” moments
	- between
	- styler
	- options
	- convert dtypes
	- mask
	- nasmallest, nalargest
	- clip
	- attime

**Brian #4:** [**FastAPI and Rich Tracebacks in Development**](https://blog.hay-kot.dev/fastapi-and-rich-tracebacks-in-development/)

- [Hayden Kotelman](https://twitter.com/kot_hay)
- Rich has, among other cool features, beautiful tracebacks and logging.
- FastAPI makes it easy to create web API’s
- This post shows how to integrate the two for API’s that are easy to debug.
- It’s really only a few simple steps
	- Create a dataclass for the logger config.
	- Create a function that will either install rich as the handler (while not in production) or use the production log configuration.
	- Call `logging.basicConfig()` with the new settings.
	- And possibly override the logger for Uvicorn.
- Article contains all code necessary, including examples of the resulting logging and tracebacks.

**Michael #5:** [**Dev in Residence**](https://lukasz.langa.pl/1c78554f-f81d-43d0-9c89-a602cafc4c5a/)

- [I am the new CPython Developer in Residence](https://lukasz.langa.pl/a072a74b-19d7-41ff-a294-e6b1319fdb6e/)
- [Report on first week](https://lukasz.langa.pl/1c78554f-f81d-43d0-9c89-a602cafc4c5a/)
- Łukasz Langa: “*When the PSF first announced the Developer in Residence position, I was immediately incredibly hopeful for Python. I think it’s a role with transformational potential for the project. In short, I believe the mission of the Developer in Residence (DIR) is to accelerate the developer experience of everybody else.*”
- The DIR can:
	- providing a steady review stream which helps dealing with PR backlog;
	- triaging issues on the tracker dealing with issue backlog;
	- being present in official communication channels to unblock people with questions;
	- keeping CI and the test suite in usable state which further helps contributors focus on their changes at hand;
	- keeping tabs on where the most work is needed and what parts of the project are most important.

**David #6:** [**Dagster**](https://dagster.io/)

- Dagster is a data orchestrator for machine learning, analytics, and ETL
- Great for local development that can be deployed on Kubernetes, etc
- Dagit provides a rich UI to monitor the execution, view detailed logs, etc
- Can deploy to Airflow, Dask, etc 
- Quick demo?
- References
    - [https://www.dataengineeringpodcast.com/dagster-data-applications-episode-104/](https://www.dataengineeringpodcast.com/dagster-data-applications-episode-104/)
    - [https://softwareengineeringdaily.com/2019/11/15/dagster-with-nick-schrock/](https://softwareengineeringdaily.com/2019/11/15/dagster-with-nick-schrock/)

**Extras**

Michael: 

- Get a vaccine, please.
- Python 3.10 Type info ---- er [Make the 3.9](https://www.python.org/dev/peps/pep-0585/), thanks John Hagen. Here is a quick example. All of these are functionally equivalent to PyCharm/mypy:

```
    # Python 3.5-3.8
    from typing import List, Optional
    def fun(l: Optional[List[str]]) -> None:


    # Python 3.9+
    from typing import Optional
    def fun(l: Optional[list[str]]) -> None:


    # Python 3.10+
    def fun(l: list[str] | None) -> None:
```

Note how with 3.10 we no longer need any imports to represent this type.

David:
- [Great SQL resource](https://winand.at/sql-slides-for-developers)


**Joke:** Pray

[![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/611186c6ed3008129dd6585b/4bac458e34ac9d8cf4da63252367a846/Screen_Shot_2021-08-09_at_12.38.36_PM.png)](https://geek-and-poke.com)




