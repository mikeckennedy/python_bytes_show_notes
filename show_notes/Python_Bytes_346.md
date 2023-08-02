# Python Bytes 346
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**A Steering Council notice about PEP 703 (Making the Global Interpreter Lock Optional in CPython)**](https://discuss.python.org/t/a-steering-council-notice-about-pep-703-making-the-global-interpreter-lock-optional-in-cpython/30474)

- Thomas Wouters
- Suggested by John Hagen
- “We intend to accept PEP 703, although we’re still working on the acceptance details.”
- Moving forward in 3 stages
    - short-term, no-GIL experimental build in 3.13 or 3.14
    - mid-term, declare support for no-GIL version
    - long-term, no-GIL becomes default and remove any vestiges of the GIL
- No commitment and timeframe is nebuous
- long-term means 5+ years
- Need community support
- “We want to be able to change our mind if it turns out, any time before we make no-GIL the default, that it’s just going to be too disruptive for too little gain.”

**Michael #2:** [**Google's post-cookie world could turn into DRM for the internet**](https://www.techspot.com/news/99540-google-post-cookie-world-could-turn-drm-internet.html#commentsOffset)

- A new authentication system could let websites block extensions or jailbroken devices.
- Google has been trying to implement plans to move beyond cookies for years without denying its partners the means to sell targeted ads.
- One recent proposal to guarantee user privacy and security could come at the cost of freedom of functionality.
- Comments are somewhat interesting.
- More info in [**a second article**](https://www.bleepingcomputer.com/news/google/browser-developers-push-back-on-googles-web-drm-wei-api/).
- [**Vivaldi has a response here**](https://vivaldi.com/blog/googles-new-dangerous-web-environment-integrity-spec/).
- Brave won’t ship with it.

**Brian #3:** [**How ruff changed my Python programming habits**](https://406.ch/writing/how-ruff-changed-my-python-programming-habits)

- Matthias Kestenholz
- “…there’s always a trade off between development speed (waiting on `git commit` is very boring) and strictness. “
- “ruff is so fast that enabling additional rules is practically free in terms of speed...”
- `ruff` has way more rules since last I checked. They are just mostly turned off by default.
- The article suggests a bunch to try turning on.
- See also
    - [ruff config settings](https://beta.ruff.rs/docs/configuration/)
        - turn on flake8-bugbear while leaving on defaults with `select = ["E", "F", "B"]`
    - [lots of rules to choose from](https://beta.ruff.rs/docs/rules/)
    - [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit) to run these with pre-commit

**Michael #4:** [**pathlib api extended to use fsspec backends**](https://github.com/fsspec/universal_pathlib)

- via Justin Flannery
- Expanding on the capabilities of **fsspec**, the same GitHub organization also supports another powerful library called [**universal_pathlib**](https://github.com/fsspec/universal_pathlib). 
- **universal_pathlib** is a python library that aims to extend Python's built-in **pathlib.Path** api to use a variety of backend filesystems using **fsspec**. 
- This seamless replacement allows developers to leverage the familiar and powerful **pathlib** API on any type of filesystem. **upath.Path** is a drop-in replacement for **pathlib.Path** and is an excellent addition to your toolkit.

**Joke:** [**Understanding pointers**](https://twitter.com/theprimeagen/status/1683671315377541121?s=12&t=RL7Nk7OAFSptvENxe1zIqA)

