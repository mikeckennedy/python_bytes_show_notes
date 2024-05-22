# Python Bytes 332

Sponsored by [**InfluxDB**](https://pythonbytes.fm/influxdata) from Influxdata.

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**huak**](https://github.com/cnpryer/huak) - A Python package manager written in Rust. Inspired by Cargo

- Suggested by [Owen](https://fosstodon.org/@owenrlamont/110186104540920622)
- Tons of workflows
    - `activate` - activate a virtual environment
    - `add` add a dependency to a project
        - pip install it into your virtual environment, and add it to the dependency list in `pyproject.toml`
    - `test` - run pytest
    - `update` update dependencies
    - `lint` - run `ruff`, installing it first if necessary
    - `fix` - autofix fixable lint conflicts
    - `build` - build wheel in isolated virtual environment using `hatchling`
- Honestly
    - I was considering building my own workflow tool, but this is darned close to what I want.
    - Even though it’s still “in an experimental state”.
    - There are rough edges (ruff edges, get it), but still, way cool.
    - I just don’t know how to pronounce it. Is it like “walk”, or more like “whack”?


**Michael #2:** [**PSF expresses concerns about a proposed EU law that may make it impossible to continue providing Python and PyPI to the European public**](https://pyfound.blogspot.com/2023/04/the-eus-proposed-cra-law-may-have.html)

- After reviewing the proposed [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act) and [Product Liability Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0495), the PSF has found issues that put the mission of our organization and the health of the open-source software community at risk.
- As currently written, the authors of open-source components might bear legal and financial responsibility for the way their components are applied in someone else’s commercial product.
- The risk of huge potential costs would make it impossible in practice for us to continue to provide Python and PyPI to the European public.

**Brian #3:** [**ChaosToolkit**](https://chaostoolkit.org)

- Suggested by the maintainer, Sylvain Hellegouarch
- Declare and store your Chaos Engineering experiments as JSON/YAML files so you can collaborate and orchestrate them as any other piece of code.
- Extensible through an Open API
- Can be automated in CI/CD pipeline

**Michael #4:** [**PEP 711 – PyBI: a standard format for distributing Python Binaries**](https://peps.python.org/pep-0711/)
[](https://peps.python.org/pep-0711/)
- “Like wheels, but instead of a pre-built python package, it’s a pre-built python interpreter”

**Joke:** [**It’s the effort that counts**](https://www.reddit.com/r/ProgrammerHumor/comments/1033r4v/its_the_effort_that_counts/)

