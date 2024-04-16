# Python Bytes 379

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of 

the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1:** [How to Set Up Pre-Commit Hooks A step-by-step guide to installing and configuring pre-commit hooks on your project](https://stefaniemolin.com/articles/devx/pre-commit/setup-guide/).

- by [**Stefanie Molin**](https://stefaniemolin.com/)
- Pre-commit hooks are code checks that run as part of the “pre-commit” stage of the git commit process. 
- If any of these checks fail, git aborts the commit
- Sometimes, we need to bypass the hooks temporarily. For these instances, we can pass the --no-verify option when we run git commit

**Brian #2:** [**difftastic**](https://difftastic.wilfred.me.uk)

- Found this a couple years ago, but really using it a lot now.
- Excellent structurally diff tool that compares code based on syntax, not line by line.

**Michael #3:**  [**Quarto**](https://quarto.org)

- via Mathias Johansson
- An open-source scientific and technical publishing system
- Transforming a notebook into a pdf / HTML / MS Word / ePub with minimal effort, or even all formats at once.
- Author using [Jupyter](https://jupyter.org/) notebooks or with plain text markdown in your favorite editor.
- Write using [Pandoc](https://pandoc.org/) markdown, including equations, citations, crossrefs, figure panels, callouts, advanced layout, and more.

**Brian #4:** [**constable**](https://github.com/saurabh0719/constable)

- “inserts print statements directly into the AST at runtime “
- “If you find yourself aimlessly adding ![sparkles](https://paper.dropboxstatic.com/static/img/ace/emoji/2728.png?version=8.0.0) print ![sparkles](https://paper.dropboxstatic.com/static/img/ace/emoji/2728.png?version=8.0.0) statements while debugging your code, this is for you. ![handshake](https://paper.dropboxstatic.com/static/img/ace/emoji/1f91d.png?version=8.0.0)”
- Add decorators like @constable.trace('a', 'b') to functions and you’ll get nice output showing when and how a and b changed.
- see also [icecream](https://github.com/gruns/icecream) for another fun debugging with print project.

**Extras** 

Brian:

- [**pointers being added to the standard library**](https://www.reddit.com/r/Python/comments/1bt7rnw/pointerspy_being_added_to_the_standard_library/)
  - A couple weeks old, but still worth covering
  - Guido’s take on adding this, "Why the hell not?"

Michael:

- [Python 3.12.3 is out](https://docs.python.org/release/3.12.3/whatsnew/changelog.html#python-3-12-2)

**Joke:** [Hugo SciFi Award](https://twitter.com/hynek/status/1777377316269883420)