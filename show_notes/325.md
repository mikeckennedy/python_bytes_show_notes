# Python Bytes 325

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Python Parquet and Arrow: Using PyArrow With Pandas**](https://codesolid.com/python-pyarrow-and-parquet/)

- Parquet is an efficient, compressed, column-oriented storage format for arrays and tables of data.
- Less wrangle-able than Pandas, but way faster and lower memory
- Questions answered
    - Can we use Pandas DataFrames and Arrow tables together, and if so, how is this done? (It turns out the answer is yes, and it’s quite simple, as we’ll see).
    - In what ways are Arrow tables “better” than Pandas DataFrames? In other words, for which tasks are Arrow tables better suited? Conversely, what tasks are possible or easy in Pandas that are difficult or impossible in Arrow?
    - As an on-disk format, how does Parquet compare to popular alternatives such as feather, orc, CSV, etc.?

**Brian #2:** [**FastAPI-Filter**](https://pypi.org/project/fastapi-filter/)

- Arthur Rio
- Add query string filters to your api endpoints and show them in the swagger UI.
- The supported backends are SQLAlchemy and MongoEngine.
- [FastAPI-Filter documentation](https://fastapi-filter.netlify.app/)
- The philosophy of **fastapi_filter** is to be very declarative. You define the fields you want to be able to filter on as well as the type of operator, then tie your filter to a specific model.
- default filters: neq, gt, gte, in, isnull, lt, lte, not/ne, not_in, nin, like/ilike
- The swagger support is actually quite cool.

**Michael #3:** [**12 Python Decorators to Take Your Code to the Next Level**](https://towardsdatascience.com/12-python-decorators-to-take-your-code-to-the-next-level-a910a1ab3e99)

- Decorators are awesome
- This is mostly home-grown decorators, but some **standard ones** too
- Notable ones:
    - **@warps**
    - **@lru_cache**
    - @repeat
    - @timeit
    - @retry ← no please use [tenacity](https://tenacity.readthedocs.io/en/latest/)
    - @countcall
    - @rate_limited
    - **@dataclass**
    - **@register**
    - **@property**
    - **@singledispatch**

**Brian #4:** [**PyHamcrest**](https://pypi.org/project/PyHamcrest/)

- Contributed by [Txels](https://mastodont.cat/@txels/109932213451142531)
- PyHamcrest is a framework for writing matcher objects, allowing you to declaratively define “match” rules. 
- [PyHamcrest tutorial](https://pyhamcrest.readthedocs.io/en/latest/tutorial.html)
- Having a tool that allows you to pick out precisely the aspect under test and describe the values it should have, to a controlled level of precision, helps greatly in writing tests that are “just right.”
- From Brian: I’ve been reluctant to try matcher style assertion helper libraries, as, with pytest, assert works just fine. However, I can see cases where PyHamcrest assertions could help test readability, and that’s always a win.
- Examples:
    - equality: `assert_that(theBiscuit, equal_to(myBiscuit))`
    - exceptions: `assert_that(calling(parse, bad_data), raises(ValueError))`
    - async: `assert_that(``**await**` `resolved(future), future_raising(ValueError))`
    - boolean: `assert_that(theBiscuit.isCooked())`
- There’s predefined matchers for 
    - objects, numbers, text, logical checks, dequences, dictionaries


**Extras** 

Brian:

- [pytest tips and tricks](https://pythontest.com/pytest-tips-tricks/) - recent post, and discussion on upcoming Talk Python episode
- [sharing pytest fixtures](https://pythontest.com/pycascades-2023/) - placeholder page where I’ll share slides and code after my talk.

Michael:

- [Python runtime updates](https://pythoninsider.blogspot.com/2023/02/python-3112-python-31010-and-3120-alpha.html)
- [Django 4.2 beta 1 released](https://www.djangoproject.com/weblog/2023/feb/20/django-42-beta-1-released/)

**Joke:** [A group of developers is called …](https://twitter.com/nixcraft/status/1601960164848193536?lang=en)

