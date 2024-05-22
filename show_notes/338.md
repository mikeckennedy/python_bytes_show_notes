# Python Bytes 338

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)
- Special guest: GUEST_PROFILE

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** The Basics of Python Packaging in Early 2023 

- Jay Qi
- Good description of a minimal-ish `pyproject.toml` file, which includes a build backend and project metadata.
- That’s all you need for a Python-only project.
- Discussion of how to choose a build backend. Mostly it’s baed on extra features you might want, like hatchling’s include/exclude features for source distributions.
- Some discussion of frontend choices.
- Nice discussion of non-Python-only builds. Specifically, if you need to compile C or C++ extensions, you can use `scikit-build-core`, or `meson-python`, or `setuptools`. 
- Related: ["Sharing is Caring - Sharing pytest Fixtures" by Brian Okken (PyCascades 2023)](https://www.youtube.com/watch?v=kevcz8NRcQU)
    - My PyCascades 2023 on packaging pytest plugins is up on YouTube

**Michael #2:** [**vecs**](https://github.com/supabase/vecs)

- via Oli
- Python collection-like interface to storing and searching vectors in postgres.
- Vector search is a key component in building AI chatbots, and semantic document search.
- If you're familiar with the space, it's effectively Pinecone built on free OSS
- It's under the Supabase github org but it's fully open source, and compatible with any pgvector vendor, e.g. RDS, or locally in docker
- If you’re on macOS and need Postgres, [Postgres App](https://postgresapp.com) is a good option.

**Brian #3:** [**Introducing Grasshopper - An Open Source Python Library for Load Testing**](https://innovation.alteryx.com/introducing-grasshopper-an-open-source-python-library-for-load-testing/)

- Jacob Fiola
- “Grasshopper is a library for automated load testing, written in Python.”
- Open source project from Alteryx, 
- On GitHub and PyPI under the name [locust-grasshopper](https://github.com/alteryx/locust-grasshopper)
- Built on Locust.
- Adds
    - Tag-based suites for trend analysis and evaluating changes.
    - Custom trends. Useful for actions that span multiple http calls, and you want to see timing trends for the whole action.
    - Checks. Checks validate boolean conditions in the test.
    - Custom tagging for all metrics
    - Send data to time series db & dashboards.
    - Thresholds. 
    - Reporting results to other locations.
    - Some reusable base classes that take care of the majority of the boilerplate that tests often contain
- Readme has a very thorough introduction including configuration and samples.

**Michael #4:** [**memocast**](https://github.com/engdan77/memocast)

- by Daniel Engvall
- A small [iOS](https://en.wikipedia.org/wiki/IOS) app for e.g. iPhone that allow you to add links heard in podcasts into [reminders](https://en.wikipedia.org/wiki/Reminders_(Apple)).
- Good example of how to use Pythonista to build python scripts for iOS
- Pythonista just made an update (2 weeks ago) so that'd use Python 3.10 on the iOS which makes it even more interesting.

**Extras** 

Brian:

- [Help test Python 3.12 beta!](https://dev.to/hugovk/help-test-python-312-beta-1508)
- [Python Language Summit write-ups available](https://pyfound.blogspot.com)
- [PyPI was subpoenaed](https://blog.pypi.org/posts/2023-05-24-pypi-was-subpoenaed)
[](https://pyfound.blogspot.com)
Michael:

- [**You Can Ignore This Post**](https://mkennedy.codes/posts/github-gitignore-repo-is-open-to-all/)

**Joke:**  [**Careful or you might end up summoning a demon**](https://devhumor.com/media/careful-or-you-might-end-up-summoning-a-demon)[.](https://devhumor.com/media/careful-or-you-might-end-up-summoning-a-demon)

