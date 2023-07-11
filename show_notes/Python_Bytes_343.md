# Python Bytes 343

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Pydantic v2 released**](https://docs.pydantic.dev/2.0/blog/pydantic-v2-final/)

- Pydantic V2 is compatible with Python 3.7 and above.
- There is a [migration guide](https://docs.pydantic.dev/2.0/migration/).
- Check out the [**bump-pydantic**](https://github.com/pydantic/bump-pydantic) tool to auto upgrade your classes

**Brian #2:** [**Two Ways to Turbo-Charge tox**](https://hynek.me/articles/turbo-charge-tox/)

- Hynek
- Not just `tox run-parallel` or `tox -p` or `tox` `--``parallel` , but you should know about that also. 
- The 2 ways
    - Build one wheel instead of N sdists
    - Run pytest in parallel
- `tox` builds source distributions, sdists, for each environment before running tests.
    - that’s not really what we want, especially if we have a test matrix.
    - It’d be better to build a wheel once, and use that for all the environments.
    - Add this to your tox.ini and now we get one wheel build
    [testenv]
    package = wheel
    wheel_build_env = .pkg
    - It will save time. And a lot if you have a lengthy build.
- Run `pytest` in parallel, instead of `tox` in parallel, with `pytest -n auto` 
    - Requires the `pytest-xdist` plugin.
    - Can slow down tests if your tests are pretty fast anyway.
    - If you’re using hypothesis, you probably want to try this.
- There are some gotchas and workarounds (like getting coverage to work) in the article.

**Michael #3:** [**Awesome Pydantic**](https://github.com/Kludex/awesome-pydantic)

- A curated list of awesome things related to Pydantic! 🌪️
- Notable items for me:
    - ML:
        - [spaCy](https://github.com/explosion/spaCy) 🌟(26575) - spaCy is a free open-source library for Natural Language Processing in Python. It features NER, POS tagging, dependency parsing, word vectors and more.
        - [ray](https://github.com/ray-project/ray) 🌟(26496) - Ray provides a simple, universal API for building distributed applications.
        - [jina](https://github.com/jina-ai/jina) 🌟(18734) - Jina is geared towards building search systems for any kind of data, including text, images, audio, video and many more. With the modular design & multi-layer abstraction, you can leverage the efficient patterns to build the system by parts, or chaining them into a Flow for an end-to-end experience.
    - Data
        - [Beanie](https://github.com/roman-right/beanie) 🌟(1287) - Beanie - is an Asynchronous Python object-document mapper (ODM) for MongoDB, based on Motor and Pydantic.
    - Utilities
        - [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) 🌟(1694) - Pydantic model generator for easy conversion of JSON, OpenAPI, JSON Schema, and YAML data sources.
        - [Goodconf](https://github.com/lincolnloop/goodconf) 🌟(99) - A thin wrapper over Pydantic's settings management. Allows you to define configuration variables and load them from environment or JSON/YAML file. Also generates initial configuration files and documentation for your defined configuration.

**Brian #4:** [**CLI tools hidden in the Python standard library**](https://til.simonwillison.net/python/stdlib-cli-tools)

- Simon Willison (and hat tip to Seth Larson)
- Simon looked for all of the command line goodies in the standard library. 
- I knew about `python -m http.server` to run a server at port 8000 from the local directory, but there’s so much more.
- Here are a few
    - `python -m gzip --decompress pypi.db.gz` as a gzip utility.
        - Especially handy on Windows as it doesn’t come with gzip by default
    - `python -m base64` with `-d` decode, `-e` encode, and `-t` encode and decode
    - `python -m asyncio` for an asyncio REPL
    - Tokenize a Python file with `python -m tokenize somefile.py`
    - View the AST with `python -m ast somefile.py`
    - Pretty print JSON with `python -m json.tool`


**Extras** 

Brian:

- Congrats to Seth Larson, PSFs first Security Developer-in-Residence
    - [Announcing Our New Security Developer in Residence!](https://pyfound.blogspot.com/2023/06/announcing-our-new-security-developer.html) - PSF announcement
    - [I am the first PSF Security Developer-in-Residence](https://sethmlarson.dev/security-developer-in-residence) - Seth’s announcement
- [PythonPeople.fm](https://pythonpeople.fm/) is live
    - "The NEW podcast about the people who make the Python community awesome.”
    - I’m focusing more on the people, and less on the tech.
    - First episode is with Michael Kennedy
    - Upcoming episodes in the works with Paul Everitt, Paul McGuire, and Steve Holden.
    - More people scheduled, many asked, and many more to be asked.

Michael:

- [**MongoDB with Async Python course**](https://talkpython.fm/async-mongodb) is out! ([talkpython.fm/async-mongodb](https://talkpython.fm/async-mongodb))
- [**Meta commits to dedicate three engineer-years to implement the removal of the GIL from Python**](https://twitter.com/llanga/status/1677648534563086338) 
- [**PyPI has a blog**](https://blog.pypi.org/posts/2023-03-21-welcome-to-the-pypi-blog/)

**Joke:** 

- [**C**](https://devhumor.com/media/linux-containers-and-kubernetes-for-beginners)[**ontainers, that’ll fix it**](https://devhumor.com/media/linux-containers-and-kubernetes-for-beginners)
- Bonus dad joke: *5 ants rent an apartment. Invite 5 other ants to share the rent. Now there are tenants.*

