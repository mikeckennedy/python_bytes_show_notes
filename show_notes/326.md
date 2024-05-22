# Python Bytes 326

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Data Classification : Does Python still have a need for class without @dataclass?**](https://blog.glyph.im/2023/02/data-classification.html)

- Glyph
- dataclasses have been in the the language since 3.7
    - That’s pretty much all modern Python, right?
- “…, is there *any* point to having non-`@dataclass` classes any more? Is there any remaining justification for writing them in new code?”
- Options:
    - `class` just becomes a dataclass if you have typehinted members in it.
    - `data` instead of `class`, to avoid decorators

**Michael #2:** [**PyGWalker**](https://github.com/Kanaries/pygwalker)

- Turn your pandas dataframe into a Tableau-style User Interface for visual analysis.
- Works with pandas and polars
- Open-source alternative to Tableau
- It allows data scientists to analyze data and visualize patterns with simple drag-and-drop operations.

**Brian #4:** [**An opinionated Python boilerplate**](https://duarteocarmo.com/blog/opinionated-python-boilerplate)

- Duarte O.Carmo
- Tools and processes for new projects
- pip-tools - Pip-tools strikes the right balance between simplicity, effectiveness, and speed.
    - especially for generating pinned requirements.txt files, if necessary
- pyproject.toml - for configuration. packaging, but also any tool that supports it.
- ruff
- black, isort
- no pre-commit hooks, just run it in CI

**Michael #5:** [**Front Matter VS Code**](https://frontmatter.codes)

- via Mark Little
- If you have content that supports frontmatter and is markdown-based, check this out.
- Stay in your editor and easily create, manage, and publish content.
- Don’t make front matter mistakes
    - When was it published? What is the timezone text formatting again?
- Learn new features of your existing static site (e.g. article image)
- Manage images and more.

**Extras** 

Brian:

- **[VSCode improves IntelliSense support for pytest in Feb release](https://code.visualstudio.com/updates/v1_76#_python)**

Michael:

- [**AI search wars get weird**](https://simonwillison.net/2023/Feb/15/bing/)
- [**Proton Drive is Out of Beta, Available for Everyone**](https://news.itsfoss.com/proton-drive-available/)

**Joke:** 

- **[Is your computer on? Is it on fire?](http://aicoder.blogspot.com/2011/03/hilarious-system-calls-in-beos.html?utm_source=pocket_saves)**

