# Python Bytes 334

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**rye - Python workflow tool**](https://github.com/mitsuhiko/rye)

- Armin Ronacher
- Rust built tool, currently only for Linux and MacOS
- Project workflow commands, like
    - init - new project
    - add - add a dependency (including optional)
    - remove - remove a dependency
    - build - build wheel
    - lock - update lock file
- virtualenv commands
    - add —dev - install in environment
    - sync - install/update dependencies in env based on pyprojec.toml
    - run - run command within environment
- Install Python
    - fetch -  Fetches a Python interpreter for the local machine
- Register existing Python
    -   toolchain  Helper utility to manage Python toolchains
- Kinda like pipx
    - install  -  Installs a package as global tool
    - uninstall - Uninstalls a global tool
    - I  didn’t see that it added anything to my PATH, so this addition made it work: 
- Bonus
    - Everything lives under ~/.rye
    - So it’s easy to stop using, and doesn’t muck up 
- see also 
    - Simon Willison’s [A few notes on Rye](https://til.simonwillison.net/python/rye)
    - [Python Bytes #332, where we talked about huak](https://pythonbytes.fm/episodes/show/332/a-python-a-slurpee-and-some-chaos)

**Michael #2:** [**PyPI Organizations**](https://developers.slashdot.org/story/23/04/24/0040250/pythons-pypi-will-sell-organization-accounts-to-corporate-projects-to-fund-staff)

- The first step in our plan to build financial support and long-term sustainability of the Python Packaging Index (PyPI)
- Small fee for organizations rather than individual users
- Like Github orgs

**Brian #3:** [**5 tips to learn any new Python library faster**](https://pybit.es/articles/5-tips-to-learn-any-new-python-library-faster/)

- Bob Belderbos
- The tiips
    - RTFM - at lest the getting started docs
    - Install it
    - Explore the library - play. Bob recommends Jupyter notebook for this.
    - Apply it to a real world problem - deliberate practice
    - Build something with it
    - (bonus) Teach it - blog, TIL, video tutorial, etc.

**Michael #4:** [**Python gets down to (the) Metal**](https://thndl.com/python-metal.html)


**Extras** 

Brian:

-  [frogmouth](https://github.com/Textualize/frogmouth) -  Markdown viewer / browser for your terminal, built with [Textual](https://github.com/Textualize/textual).

Michael:

- Was going to talk about [Serenade](https://serenade.ai/download/), but seems to have gone silent.
- [Packaging follow up discussion](https://fosstodon.org/@btskinn/110294565751856796).

**Joke:** [It’s the progress that counts](https://www.reddit.com/r/programminghumor/comments/12xe5ov/wow_a_different_error_message_finally_some/)

