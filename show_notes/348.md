# Python Bytes 348
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Differentiating between writing down dependencies to use packages and for packages themselves**](https://snarky.ca/differentiating-between-writing-down-dependencies-to-use-packages-and-for-packages-themselves/)

- Brett Cannon
- Why can’t we just use pyproject.toml and stop using requirements.txt?
- Nope. At least not yet. They’re currently for different things.
- pyproject.toml
    - There’s  `project.dependencies` and `project.optional-dependencies.tests` that kinda would work for listing dependencies for an app.
    - But you can’t say `pip install -r pyproject.toml`. It doesn’t work. And that’s weird.
    - `project` is intended for packaged projects.
- requirements.txt
    - for applications and other non-packaged projects
    - It has specific versions
    - works great with pip
- What then?
    - Either we stick with requirements.txt
    - Or we invent some other file, maybe requirements.toml?
    - Or maybe (Brian’s comment), add something like `[application]` and `application.dependencies` and `application.optional-dependencies.tests` to pyproject.toml

**Michael #2:** [**PythonMonkey**](https://github.com/Distributive-Network/PythonMonkey)

- [PythonMonkey](https://pythonmonkey.io/) is a Mozilla [SpiderMonkey](https://firefox-source-docs.mozilla.org/js/index.html) JavaScript engine embedded into the Python VM, using the Python engine to provide the JS host environment.
- This product is in an early stage, approximately 80% to MVP as of July 2023. It is under active development by [Distributive](https://distributive.network/). External contributions and feedback are welcome and encouraged.
- It will enable JavaScript libraries to be used seamlessly in Python code and vice versa — without any significant performance penalties. 
- Call Python packages like NumPy from within a JavaScript library, or use NPM packages like `[crypto-js](https://www.npmjs.com/package/crypto-js)` directly from Python.
- Executing WebAssembly modules in Python becomes trivial using the WebAssembly API and engine from SpiderMonkey.
- More details in [Will Pringle’s article](https://medium.com/@willkantorpringle/pythonmonkey-javascript-wasm-interop-in-python-using-spidermonkey-bindings-4a8efce2e598).

**Brian #3:** [**Quirks of Python package versioning**](https://sethmlarson.dev/pep-440)

- Seth Larson
- Yes, we have SemVer, 1.2.3, and CalVer, 2023.6.1, and suffixes for pre-release, 1.2.3pre1.
- But it gets way more fun than that, if you get creative
- Here’s a few
    - `v` is an optional prefix, like `v.1.0`
    - You can include an “Epoch” and separate it from the version with a `!`, like `20!1.2.3`
    - Local versions with alphanumerics, periods, dashes, underscores, like `1.0.0+ubuntu-1`. PyPI rejects those. That’s probably good.
    - Long versions. There’s no max length for a version number. How about `1.2.3.4000000000000000001`?
    - Pre, post, dev aren’t mutually exclusive: `1.0.0-pre0-post0-dev0`
    - More craziness in article
- 

**Michael #4:** [**bear-type**](https://beartype.readthedocs.io/en/latest/)

- **Beartype** is an [open-source](https://github.com/beartype/beartype/blob/main/LICENSE) [PEP-compliant](https://beartype.readthedocs.io/en/latest/pep/#pep-pep) [near-real-time](https://beartype.readthedocs.io/en/latest/faq/#faq-realtime) [pure-Python runtime type-checker](https://beartype.readthedocs.io/en/latest/eli5/#eli5-eli5) emphasizing efficiency, usability, and thrilling puns.
- Annotate @beartype-decorated classes and callables with type hints.
    - Call those callables with valid parameters: Transparent
    - Call those callables with invalid parameters: Boom


    Traceback:
        raise exception_cls(
    beartype.roar.BeartypeCallHintParamViolation: @beartyped
    quote_wiggum() parameter lines=[b'Oh, my God! A horrible plane
    crash!', b'Hey, everybody! Get a load of thi...'] violates type hint
    list[str], as list item 0 value b'Oh, my God! A horrible plane crash!'
    not str.


**Extras** 

Brian:

- [**Python Testing with Pytest Course Bundle: Limited Pre-Release Beta**](https://testandcode.teachable.com/p/full-pytest-course-bundle-limited-pre-release-beta)
    - Use code PYTHONBYTES now through Aug 17 for 20% discount
    - What’s a pre-release beta? There’s a video. Check out the link.
- [**Error-tolerant pytest discovery in VSCode**](https://devblogs.microsoft.com/python/python-in-visual-studio-code-august-2023-release/#error-tolerant-pytest-discovery) 
    - Finally! But you gotta turn it on. Also, I gotta talk to them about the proper non-capitalization of `pytest`.
- [**We’re at RC1 for Python 3.12.0**](https://pythoninsider.blogspot.com/2023/08/python-3120-release-candidate-1-released.html)
    - Hard to believe it’s that time of year again

Michael:

- [**PyPI hires a Safety & Security Engineer**](https://blog.pypi.org/posts/2023-08-04-pypi-hires-safety-engineer/), welcome Mike Fiedler
- [**PackagingCon**](https://packaging-con.org) October 26-28 
- [**Cloud Builders: Python Conf**](https://www.cloud-builders.tech/en/python-conf) (born in Ukraine): September 6, 2023 | online

**Joke:** [**Learning JavaScript**](https://www.reddit.com/r/programminghumor/comments/14dh6lk/sad/)

