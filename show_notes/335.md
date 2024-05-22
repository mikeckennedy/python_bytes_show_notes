# Python Bytes 335

Sponsored by [**InfluxDB**](https://pythonbytes.fm/influxdata) from Influxdata.

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Introducing 'Trusted Publishers’**](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/)

- PyPI package maintainers can adopt a new, more secure publishing method that does not require long-lived passwords or API tokens to be shared with external systems.
- Our term for using the [OpenID Connect (OIDC)](https://openid.net/connect/) standard to exchange short-lived identity tokens between a trusted third-party service and PyPI.
- Instead, PyPI maintainers can configure PyPI to trust an identity provided by a given OpenID Connect Identity Provider (IdP).
- These API tokens 
    - never need to be stored or shared
    - rotate automatically by expiring quickly
    - provide a verifiable link between a published package and its source
- Additional security hardening is available

**Brian #2:** [**Mojo : a new programming language for all AI developers.**](https://www.modular.com/mojo)

- [Mojo may be the biggest programming language advance in decades](https://www.fast.ai/posts/2023-05-03-mojo-launch.html) - fast.ai blog
- Suggested by many listeners
- “Mojo combines the usability of Python with the performance of C, unlocking unparalleled programmability of AI hardware and extensibility of AI models.”
- A programming language compatible with Python, with performance similar to C++/Rust.
- “Mojo is designed **to become** a superset of Python over time by preserving Python’s dynamic features while adding new primitives for systems programming.” - emphasis from Brian
    - It’s not there yet, but still super cool
- Built on a MLIR, not LLVM
- “**How compatible is Mojo with Python really?**
    - Mojo already supports many core features of Python including async/await, error handling, variadics, etc, but… it is still very early and missing many features - so today it isn’t very compatible. Mojo doesn’t even support classes yet!”


**Michael #3:** django-prose

- Wonderful rich-text editing for your Django project.
- [Rendering rich-text in templates](https://github.com/withlogicco/django-prose#rendering-rich-text-in-templates)
- [Small rich-text content](https://github.com/withlogicco/django-prose#small-rich-text-content) (as model fields)
- Django Prose is using [Bleach](https://bleach.readthedocs.io/en/latest/) to only allow certain tags and attributes
- See the website for a screenshot of it in action

**Brian #4:** `[**pylyzer**](https://github.com/mtshiba/pylyzer)` [**is a static code analyzer / language server for Python, written in Rust.**](https://github.com/mtshiba/pylyzer)

- Shunsuke Shibayama
- Suggested by [Owen](https://fosstodon.org/@owenrlamont)
- Features
    - fast 
    - detailed analysis 
        - type checking
        - plus things like out-of-bounds accesses to lists, and non-existent key references to dicts
    - more readable reports
    - and a VS Code extension
- pylyzer vs ruff 
    - “[Ruff](https://github.com/charliermarsh/ruff), like pylyzer, is a static code analysis tool for Python written in Rust, but Ruff is a linter and pylyzer is a type checker & language server. pylyzer does not perform linting, and Ruff does not perform type checking.”
- Some limitations and incomplete “todo list”. See README for more details.

**Extras** 

Brian:

Michael: App update, [we were so close](https://talk-python-static.nyc3.digitaloceanspaces.com/appstore-20.png)!

**Joke:** [Escape Room](https://twitter.com/arthur_rio/status/1651272804460032000)

