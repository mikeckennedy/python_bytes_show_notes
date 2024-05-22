# Python Bytes 357

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**QuickMacHotKey**](https://github.com/glyph/QuickMacHotKey)

- This is a set of minimal Python bindings for the undocumented macOS framework APIs that even [the most modern, sandboxing-friendly shortcut-binding frameworks](https://github.com/cocoabits/MASShortcut/blob/6f2603c6b6cc18f64a799e5d2c9d3bbc467c413a/Framework/Monitoring/MASHotKey.m#L21-L22) use under the hood for actually binding global hotkeys.
- Thinking of updating my [urlify menubar app](https://github.com/mikeckennedy/urlify).

**Brian #2:** [**Things I’ve learned about building CLI tools in Python**](https://simonwillison.net/2023/Sep/30/cli-tools-python/)

- Simon Willison
- [A cool Cookiecutter starter project](https://github.com/simonw/click-app), if you like Click. 
- Conventions and consistency in commands, arguments, options, and flags.
- The importance of versioning. Your CLI is an API.
- Include examples in `--help`
- Include `--help` in documentation.
- Aside, [Typer](https://pypi.org/project/typer/) is also cool, and is built on Click.


**Michael #3:**  [**Warp Terminal**](https://www.warp.dev) **(**[**referral code**](https://app.warp.dev/referral/96PYZY)**)**

-  Really nice reimagining of the terminal 
    - Currently macOS only but will be Linux, then Windows
- New command section & output section mode
- Blocks can be navigated and searched as a single thing (even if it’s 1,000 lines of output)
- CTRL+R gives a nice history like McFly I’ve discussed before
- Completions into popular CLIs (i.e. git)
- Edit like an editor (even you VIM people 🙂 )
- Has AI built in too
- Free for individuals
- If you’re going to give it a try, use [**my referral**](https://app.warp.dev/referral/96PYZY) I guess?

**Brian #4:** [**Python 3.7 EOLed, but I hadn’t noticed**](https://devguide.python.org/versions/)

- EOL was June 27
- I’m still supporting 3.7, as are most projects I work with. But I’m not sure when that will change.
- [VS Code is deprecating 3.7 support](https://devblogs.microsoft.com/python/python-in-visual-studio-code-october-2023-release/#deprecation-of-python-3-7-support)
- Why I’m ok with supporting 3.7 for some projects
    - dataclasses came in with 3.7
    - `from __ future__ import annotations` allows the use of union types with `X|Y`.
    - [example](https://github.com/okken/pytest-param-scope/blob/main/src/pytest_param_scope/plugin.py)
- I’ll probably drop 3.7 as my dependent projects drop it.

**Extras** 

Brian:

- [**pytest-param-scope**](https://github.com/okken/pytest-param-scope) is an in progress hack to workaround this missing scope. 
    - Runs setup before any param test cases, and teardown after the last one.
- [**Stop defining people by what they’re not: on “non-code contributors”**](https://blog.josh.tel/2023/09/29/stop-defining-people-by-what-theyre-not-on-non-code-contributors/) - Josh Simmons

Michael:

- [**OpenAI has unveiled the Beta version of its Python SDK**](https://developers.slashdot.org/story/23/10/08/0414238/openai-to-release-its-python-sdk) (via Mark Little)
- StackOverflow [**lays off 28% of its staff**](https://techcrunch.com/2023/10/17/stack-overflow-cuts-28-of-its-staff/?guccounter=1)
    - Weird follow up of their [“what to do if you’re laid off” post](https://stackoverflow.blog/2023/03/19/whats-different-about-these-layoffs/) from 6 months ago?
    - Is AI eating into their traffic?
    - ArsTechnica [**has thoughts**](https://arstechnica.com/?p=1976310) too

**Joke:** 

- [**Define**](https://tech.lgbt/@nliz/111193884424695678?kjy=spring) [***hot***](https://tech.lgbt/@nliz/111193884424695678?kjy=spring)
- New Zoo exhibit

