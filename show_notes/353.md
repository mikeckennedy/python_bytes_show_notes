# Python Bytes 353
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python Testing with pytest, full course**](https://testandcode.teachable.com/p/pytest-primary-power)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**OverflowAI**](https://stackoverflow.blog/2023/07/27/announcing-overflowai/)

- Integration of generative AI into our public platform, Stack Overflow for Teams, and brand new product areas, like an IDE integration.
- Have a conversation about the search results and proposed answer with GenAI
- Coming with IDE integration too.
- Check out the video on their page for some more detail than the article.

**Brian #2:** [**Switching to Hatch**](https://andrich.me/2023/08/switching-to-hatch/)

- Oliver Andrich
- Hatch has some interesting features
    - Template built from `hatch new myproject` includes isolating dev, test, lint virtual environments.
    - Each env can have scripts
    - Test matrix ala tox, but possibly easier to express complex matrices. 
    - May not even need tox then, but then now you have hatch.
    - A way to specify which optional dependencies needed for default environment.
- Notes from Brian
    - One premise is that lots of projects are now using hatch.
    - I don’t know if that’s true. A quick spot check of a few projects include projects that use `hatchling`. While `hatchling` is the back end to `hatch`, they are not the same. I use `hatchling` a lot now, but haven’t picked up using `hatch`. But I do want to try it more after reading this article.

**Michael #3:** [**Alpha release of the Ruff formatter**](https://github.com/astral-sh/ruff/blob/main/crates/ruff_python_formatter/README.md)

- vis Sky Kasko
- Charlie Marsh [announced](https://github.com/astral-sh/ruff/issues/1904#issuecomment-1716130700) that an alpha version of a Ruff formatter has been released in Ruff v0.0.289. 
- The formatter is designed to be a drop-in replacement for [Black](https://github.com/psf/black), but with an excessive focus on performance and direct integration with Ruff.
- Sky says: I can't find any benchmarks that have been released yet, but I did some extremely unscientific testing and found the Ruff formatter to be around 5 to 10 times faster than Black when running on already-formatted code or in a small codebase, and 75 times faster when running on a large codebase of unformatted code. (The second outcome probably isn't very important since most people would not often be formatting thousands of lines of completely unformatted code.)
- For more info, see the README: [https://github.com/astral-sh/ruff/blob/main/crates/ruff_python_formatter/README.md](https://github.com/astral-sh/ruff/blob/main/crates/ruff_python_formatter/README.md)

**Brian #4:** [**What is wrong with TOML?**](https://hitchdev.com/strictyaml/why-not/toml/)
****
- Colm O'Connor
- Suggested by Will McGugan
- This is a comparison of TOML vs StrictYAML under the use case of “readable story tests”.
- TLDR; For smallish things like pyproject.toml, toml is fine. For huge files, something like StrictYAML may be less horrible.
- from Brian: 
    - Short answer: Nothing, unless you’re doing crazy things with it.
    - Re “readable story tests”: WTF? Neither of these are something I’d like to maintain.

**Extras** 

Brian:

- [**Python Testing with pytest, the course**](https://testandcode.teachable.com/p/pytest-primary-power)
    - New intro video to explain what the course is about
    - Using Teachable video
        - like notes, mini-viewer, and speed controls
    - Chapter on “Testing Strategy” is next

Michael:

- [**HTMX + Django: Modern Python Web Apps, Hold the JavaScript Course**](https://training.talkpython.fm/courses/htmx-django-modern-python-web-apps-hold-the-javascript)
- [**Coding in Rust? Here's a New IDE by JetBrains**](https://news.itsfoss.com/rust-ide-jetbreains/)
- [**Delightful Machine Learning Apps with Gradio**](https://talkpython.fm/episodes/show/430/delightful-machine-learning-apps-with-gradio) out on Talk Python

**Joke:** [**The 5 stages of debugging**](https://www.reddit.com/r/programminghumor/comments/16651p4/the_5_stages_of_debugging/)

