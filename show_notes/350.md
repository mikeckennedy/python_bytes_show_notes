# Python Bytes 350
Sponsored by Sentry: [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Make Each Line Count, Keeping Things Simple in Python**](https://pybit.es/articles/make-each-line-count-keeping-things-simple-in-python)

- Bob Belderbos
- Some great tips to help you simplify your Python code to make it more understandable and maintainable.

**Michael #2:** [**Parsel**](https://github.com/scrapy/parsel)

- Parsel is a BSD-licensed [Python](https://www.python.org/) library to extract data from [HTML](https://en.wikipedia.org/wiki/HTML), [JSON](https://en.wikipedia.org/wiki/JSON), and [XML](https://en.wikipedia.org/wiki/XML) documents.
- Parsel lets you extract data from XML/HTML documents using XPath or CSS selectors.
- It supports:
    - [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and [XPath](https://en.wikipedia.org/wiki/XPath) expressions for HTML and XML documents
    - [JMESPath](https://jmespath.org/) expressions for JSON documents
    - [Regular expressions](https://docs.python.org/library/re.html)


    # Want a RSS feed detail from a website standard HTML?
    selector = parsel.Selector(text=html_text)
    for link in selector.css('head > link'):
        rel = link.xpath('.//@rel').get()
        rel_type = link.xpath('.//@type').get()
        href = link.xpath('.//@href').get()

**Brian #3:** [**A Comprehensive Guide to Python Logging with Structlog**](https://betterstack.com/community/guides/logging/structlog/)

- Stanley Ulili
- [structlog](https://github.com/hynek/structlog) is an awesome logging tool, and already has [great documentation](https://www.structlog.org/en/stable/).
- However, [this article](https://betterstack.com/community/guides/logging/structlog/) is a great starting point, highlighting 
    - how easy it is to get started using structlog
    - configuring the default log level
    - changing the formatting
    - customizing the time stamp
    - adding custom fields
    - adding contextual data
    - filtering
    - async
    - …

**Michael #4:** [**Stamina**](https://stamina.hynek.me/en/stable/)

- via [**Matthias Bach**](https://chaos.social/@marix), by Hynek
- Production-grade Retries Made Easy
- *stamina* is an opinionated wrapper around the *great-but-unopinionated* [Tenacity](https://tenacity.readthedocs.io/) package. Its goal is to be as ergonomic as possible, while doing the right thing by default, while minimizing potential for misuse.
- General additions on top of Tenacity
    - Retry only on certain exceptions.
    - Exponential backoff with *jitter* between retries.
    - Limit the number of retries **and** total time.
    - Automatic **async** support.
    - Preserve **type hints** of the decorated callable.
    - Count ([Prometheus](https://github.com/prometheus/client_python)) and log ([*structlog*](https://www.structlog.org/)) retries with basic metadata, if they’re installed.
    - Easy *global* deactivation for testing.

**Extras** 

Brian:

- The [**“pytest fixtures” chapter of the pytest course**](https://testandcode.teachable.com/p/pytest-primary-power) is available now. 
    - Also, the PYTHONBYTES 20% discount still active for bundle through the end of August.

Michael:

- Python 3.12.0 release candidate 1 [**released**](https://docs.python.org/3.12/whatsnew/3.12.html)
- PyCon UK: The conference takes place from the 22nd to the 25th of September in Cardiff, Wales. The schedule is available at [**2023.pyconuk.org/schedule/**](https://2023.pyconuk.org/schedule/) and tickets are available at [**2023.pyconuk.org/tickets/**](https://2023.pyconuk.org/tickets/).
- [**PyData Eindhoven 2023**](https://pydata.org/eindhoven2023/), Nov 30 CFP open
- [**PyData Seattle Language Creators Charity Fundraiser**](https://pydata.org/language-creator-fundraiser/): Adele Goldberg - Smalltalk, Guido Van Rossum, Anders Hejlsberg, C#, and James Gosling - Java. September 19, 2023: 12:00 - 4:00 PM, in person only. 

**Joke:** 

- [**Librarian**](https://mastodon.neilzone.co.uk/@neil/110922305790818460)
- [**chatgpt-failures**](https://github.com/giuven95/chatgpt-failures) [](https://github.com/giuven95/chatgpt-failures)
