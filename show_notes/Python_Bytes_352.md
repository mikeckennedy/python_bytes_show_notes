# Python Bytes 352

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Heliclockter**](https://pypi.org/project/heliclockter/) - Like datetime, but more timezone-aware

- Suggested by Peter Nilsson
- The library exposes 3 classes:
    - `datetime_tz`, a datetime ensured to be timezone-aware.
    - `datetime_local`, a datetime ensured to be timezone-aware in the local timezone.
    - `datetime_utc`, a datetime ensured to be timezone-aware in the UTC+0 timezone.

**Michael #2:** [**Wagtail 5**](https://wagtail.org/blog/come-over-to-the-dark-side-with-wagtail-50/)

- Wagtail is the leading open-source Python CMS, based on Django.
- Anything you can do in Python or Django, you can do in Wagtail.
- Wagtail 5.0 provides even more options for your content creation experience
    - Dark mode has arrived
    - SVG support
    - Enhanced accessibility checker
    - Delete more safely
    - Some breaking changes in it because this release removes some of the old code paths that were maintained to give people more time to adapt their code to the new upgrades
    - Add custom validation logic to your Wagtail projects. You can now attach errors to specific child blocks in StreamField.

**Brian #3:** [**Git log customization**](https://www.justinjoyce.dev/customizing-git-log-format/)

- Justin Joyce
- Just a simple `git log --oneline` makes the log so much more readable, but don’t stop there.
- `--graph` helps to show different branches
- `-10` shows the last 10 commits.
- And this beauty in `.gitconfig` makes `git lg` mostly do what you want most of the time:

```
[alias]
  lg = log --graph -10 --format='%C(yellow)%h%Creset  %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' 
```

**Michael #4:** [**MiniJinja template engine**](https://github.com/mitsuhiko/minijinja)

- MiniJinja is a powerful but minimal dependency template engine **for Rust** compatible with Jinja/Jinja2
- Comes with integration back into Python via [minijinja-py](https://github.com/mitsuhiko/minijinja/tree/main/minijinja-py) package.
- MiniJinja has a stronger sandbox than Jinja2 and *might perform ever so slightly better* in some situations. 
- However you should be aware that due to the marshalling that needs to happen in either direction there is a certain amount of loss of information.
- [Compiles to WebAssembly](https://github.com/mitsuhiko/minijinja-playground/blob/main/src/lib.rs)

**Extras** 

Brian:

- The [**pytest Primary Power**](https://testandcode.teachable.com/p/pytest-primary-power) course is ready.
    - To celebrate wrapping up the first course, [**pytest Primary Power**](https://testandcode.teachable.com/p/pytest-primary-power) is $49, the bundle is $99.
    - Bundle: This + next 2 courses + access to repo, discussion forum, Slack, and Discord

Michael:

- New HTMX, language course, and data science course coming at Talk Python. [**Add your name here to get notified**](https://training.talkpython.fm/getnotified).
- I’ll be [**at PyBay 2023**](https://pybay.com) on Oct 8, 2023
    - Use "**friendofspeaker**" with for a 20% discount on the regular tickets.
- Follow up from docstrings:
    - [From Rhet](https://fosstodon.org/@RhetTbull/111030986252105257)
    - John Hagen:
        - You can certainly omit the type information from the docstring when you are using typehints. This is the way I've seen almost all modern usages of Google style docstrings nowadays. They still have some examples that include the type information because the original standard pre-dated Python 3 type annotations. Here is a simple example:
        - [https://github.com/johnthagen/python-blueprint/blob/main/src/fact/lib.py#L5](https://github.com/johnthagen/python-blueprint/blob/main/src/fact/lib.py#L5)
        - This also shows off the next point that you brought up: can I document all of the exceptions that a function could raise. Google docstrings have the "Raises:" block for this, and I find it pretty nice and concise for when this is needed.
        - Also, PyCharm can be configured to autocomplete and render Google style docstrings
        - [https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html](https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html)
        - Tools | Python Integrated Tools | Docstrings | Docstring Format: Google
        - What's nice about this, is that then PyCharm will render the google style docstrings in the Quick Doc function (Ctrl+Q), making the headers bold and larger and lists look nice so it's easy to read.

**Joke:**  [**Fully optimized my algorithm**](https://devhumor.com/media/fully-optimized-my-algorithm)

