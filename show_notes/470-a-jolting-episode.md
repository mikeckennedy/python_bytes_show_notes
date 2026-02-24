Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 11am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Brian #1: [Better Python tests with inline-snapshot](https://pydantic.dev/articles/inline-snapshot)**

- Alex Hall, on Pydantic blog
- Great for testing complex data structures
- Allows you to write a test like this:
```toml
from inline_snapshot import snapshot
def test_user_creation():
    user = create_user(id=123, name="test_user")
    assert user.dict() == snapshot({})
```
- Then run `pytest --inline-snapshot=fix`
- And the library updates the test source code to look like this:
```toml
def test_user_creation():
    user = create_user(id=123, name="test_user")
    assert user.dict() == snapshot({
        "id": 123,
        "name": "test_user",
        "status": "active"
    })
```
- Now, when you run the code without “fix” the collected data is used for comparison
- Awesome to be able to visually inspect the test data right there in the test code.
- Projects mentioned
  - [inline-snapshot](https://15r10nk.github.io/inline-snapshot/latest/)
  - [pytest-examples](https://github.com/pydantic/pytest-examples)
  - [syrupy](https://github.com/syrupy-project/syrupy)
  - [dirty-equals](https://github.com/samuelcolvin/dirty-equals)
  - [executing](https://github.com/alexmojaki/executing)

**Michael #2: [jolt Battery intelligence for your laptop](https://getjolt.sh/)**

- Support for both macOS and Linux
- **Battery Status** — Charge percentage, time remaining, health, and cycle count
- **Power Monitoring** — System power draw with CPU/GPU breakdown
- **Process Tracking** — Processes sorted by energy impact with color-coded severity
- **Historical Graphs** — Track battery and power trends over time
- **Themes** — 10+ built-in themes with dark/light auto-detection
- **Background Daemon** — Collect historical data even when the TUI isn't running
- **Process Management** — Kill energy-hungry processes directly

**Brian #3: [Markdown code formatting with ruff](https://docs.astral.sh/ruff/formatter/#markdown-code-formatting)**

- Suggested by Matthias Schoettle
- `ruff` can now format code within markdown files
- Will format valid Python code in code blocks marked with `python`, `py`, `python3` or `py3`.
- Also recognizes `pyi` as Python type stub files.
- Includes the ability to turn off formatting with comment `<!-- fmt:off -->` , `<!-- fmt:on -->` blocks.
- Requires preview mode
```toml
[tool.ruff.lint]
preview = true
```

**Michael #4: [act - run your GitHub actions locally](https://github.com/nektos/act)**

- Run your [GitHub Actions](https://developer.github.com/actions/) locally! Why would you want to do this? Two reasons:
  - **Fast Feedback** - Rather than having to commit/push every time you want to test out the changes you are making to your `.github/workflows/` files (or for any changes to embedded GitHub actions), you can use `act` to run the actions locally. The [environment variables](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables#default-environment-variables) and [filesystem](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#filesystems-on-github-hosted-runners) are all configured to match what GitHub provides.
  - **Local Task Runner** - I love [make](https://en.wikipedia.org/wiki/Make_(software)). However, I also hate repeating myself. With `act`, you can use the GitHub Actions defined in your `.github/workflows/` to replace your `Makefile`!
- When you run `act` it reads in your GitHub Actions from `.github/workflows/` and determines the set of actions that need to be run.
  - Uses the Docker API to either pull or build the necessary images, as defined in your workflow files and finally determines the execution path based on the dependencies that were defined.
  - Once it has the execution path, it then uses the Docker API to run containers for each action based on the images prepared earlier.
  - The [environment variables](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables#default-environment-variables) and [filesystem](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#file-systems) are all configured to match what GitHub provides.

**Extras**

Michael:
- Winter is coming: [Frozendict accepted](https://www.linkedin.com/feed/update/urn:li:activity:7427589361048948736/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAABOjqABPkOWTTbZXV9tmnQohvpkplQOibU)
- [Django ORM stand-alone](https://mastodon.social/@webology/116103649163718377)
- Command Book app [announcement post](https://mkennedy.codes/posts/your-terminal-tabs-are-fragile-i-built-something-better/)

**Joke:** [Plug ‘n Paste](https://x.com/pr0grammerhum0r/status/2017704478267314514?s=12)

Links

- [Better Python tests with inline-snapshot](https://pydantic.dev/articles/inline-snapshot)
- [inline-snapshot](https://15r10nk.github.io/inline-snapshot/latest/)
- [pytest-examples](https://github.com/pydantic/pytest-examples)
- [syrupy](https://github.com/syrupy-project/syrupy)
- [dirty-equals](https://github.com/samuelcolvin/dirty-equals)
- [executing](https://github.com/alexmojaki/executing)
- [jolt Battery intelligence for your laptop](https://getjolt.sh/)
- [Markdown code formatting with ruff](https://docs.astral.sh/ruff/formatter/#markdown-code-formatting)
- [act - run your GitHub actions locally](https://github.com/nektos/act)
- [GitHub Actions](https://developer.github.com/actions/)
- [environment variables](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables#default-environment-variables)
- [filesystem](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#filesystems-on-github-hosted-runners)
- [make](https://en.wikipedia.org/wiki/Make_(software)
- [filesystem](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#file-systems)
- [Frozendict accepted](https://www.linkedin.com/feed/update/urn:li:activity:7427589361048948736/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAABOjqABPkOWTTbZXV9tmnQohvpkplQOibU)
- [Django ORM stand-alone](https://mastodon.social/@webology/116103649163718377)
- [announcement post](https://mkennedy.codes/posts/your-terminal-tabs-are-fragile-i-built-something-better/)
- [Plug ‘n Paste](https://x.com/pr0grammerhum0r/status/2017704478267314514?s=12)
