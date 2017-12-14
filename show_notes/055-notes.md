# Python Bytes 55
Sponsored by DigitalOcean: [http://digitalocean.com](http://digitalocean.com)

**Brian #1** [**The Flask Mega-Tutorial**](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)**, reborn**

- This very popular tutorial, written in 2012, has been rewritten.
- [Miguel Grinberg](https://twitter.com/miguelgrinberg) has rewritten it with the help of a kickstarter campaign.
- [Part 1 of the tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is up, and he’s releasing 1 part per week.
- Want it faster, you can get it all in an [eBook](https://learn.miguelgrinberg.com/) right now.
- A video version is coming in January.

**Michael #2:** [**Django 2.0 Released**](https://www.djangoproject.com/weblog/2017/dec/02/django-20-released/)

-  This release starts Django’s use of a [loose form of semantic versioning](https://docs.djangoproject.com/en/stable/internals/release-process/#internal-release-cadence)
- Features
	- A [simplified URL routing syntax](https://docs.djangoproject.com/en/stable/releases/2.0/#simplified-url-routing-syntax) that allows writing routes without regular expressions.
	- A responsive, [mobile-friendly contrib.admin](https://docs.djangoproject.com/en/stable/releases/2.0/#mobile-friendly-contrib-admin).
	- [Window expressions](https://docs.djangoproject.com/en/stable/releases/2.0/#window-expressions) to allow adding an OVER clause to querysets.
- Python 3 only
- django.contrib.auth
  - The default iteration count for the PBKDF2 password hasher is increased from 36,000 to 100,000.
- Lots more changes

**Brian #3:** [**The Big Ol' List of Rules**](https://lintlyci.github.io/Flake8Rules/)

- [Flake8](http://flake8.pycqa.org/en/latest/index.html) is a popular code linter that combines pyflakes, pycodestyle, and mccabe.
	- [pycodestyle](https://pypi.python.org/pypi/pycodestyle) is the new pep8 to enforce [PEP8](https://www.python.org/dev/peps/pep-0008/) suggestions. These are mostly style guide items, and not actual bugs.
	- [pyflakes](https://pypi.python.org/pypi/pyflakes) is more like a traditional linter in that it catches things that are probably oversight or bugs.
	- [mccabe](https://pypi.python.org/pypi/mccabe) is harder to explain, but it generally tells you if your code might be too complicated, using [Cyclomatic Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity).
- Flake8 produces error codes if your code has problems
	- Ennn and Wnnn for pycodestyle errors and warnings
	- Fnnn for pyflakes errors
	- Cnnn for mccabe errors
- The [The Big Ol' List of Rules](https://lintlyci.github.io/Flake8Rules/) is a very nice breakdown of every error, what it means, and has links to other documents where they are defined.
- Very nice work from [Grant McConnaughey](https://twitter.com/gmcconnaughey)

**Michael #4:** [**requests-staticmock**](https://github.com/tonybaloney/requests-staticmock)

- via [Anthony Shaw](https://twitter.com/anthonypjshaw)
- The Session object allows you to persist certain parameters across requests. It also persists cookies across all requests made from the Session instance, and will use `urllib3`'s [connection pooling](http://urllib3.readthedocs.io/en/latest/reference/index.html#module-urllib3.connectionpool). So if you're making several requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase
- A Session object has all the methods of the main Requests API.
- [**requests-staticmock**](https://github.com/tonybaloney/requests-staticmock) is a static HTTP mock interface for testing classes that leverage Python requests with **no** monkey patching!

**Brian #5:** [**PEP 557 -- Data Classes**](https://www.python.org/dev/peps/pep-0557/) **have been approved**

- You can play with them now if you want, with the [3.7.0a3 developer build](https://www.python.org/downloads/release/python-370a3/).
- However, [3.7 isn’t scheduled for release until June 2018](https://www.python.org/dev/peps/pep-0537/).

Very short Example lifted directly from PEP 557 doc.

    @dataclass
    class C:
        a: int       # 'a' has no default value
        b: int = 0   # assign a default value for 'b'

In this example, both a and b will be included in the added __init__ method, which will be defined as:

    def __init__(self, a: int, b: int = 0):
        pass


- Why not just use [attrs](http://www.attrs.org/en/stable/)? (Also lifted from the pep doc)
  - attrs moves faster than could be accommodated if it were moved in to the standard library.
  - attrs supports additional features not being proposed here: validators, converters, metadata, etc. Data Classes makes a tradeoff to achieve simplicity by not implementing these features.

**Michael #6:** [**Quart: 3x faster Flask**](https://hackernoon.com/3x-faster-than-flask-8e89bfbe8e4f)

- Python has evolved since [Flask](https://github.com/pallets/flask) was first released around 8 years ago, particularly with the introduction of asyncio. 
- Asyncio has allowed for the development of libraries such as [uvloop](https://github.com/MagicStack/uvloop) and [asyncpg](https://github.com/magicstack/asyncpg) that are reported ([here](https://magic.io/blog/uvloop-blazing-fast-python-networking/), and [here](https://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/)) to improve performance far beyond what was previously possible. 
- Quart provides the easiest transition for Flask apps to use asyncio as it shares the Flask-API.
- **tl;dr:** Upgrading [this](https://github.com/pgjones/faster_than_flask_article/commit/253538aa8cd65a3ed48563c2ea4594d998286293) Flask-pyscopg2 app to a Quart-asyncpg app gives a performance speedup of 3x without requiring a major rewrite or adjustment of the code
- View methods become async / await methods

**Our news**

Michael:

- Pythonic staff of enlightnement
	- I have already encountered the Pythonic Staff of Enlightenment, see [the photo that Anthony tweeted of you guys brandishing it at PyCon US](https://twitter.com/anthonypjshaw/status/866430414537216000).
	- Now so can you: [https://www.enstaved.com/pythonic-staff-of-enlightenment-now-on-sale/](https://www.enstaved.com/pythonic-staff-of-enlightenment-now-on-sale/)

