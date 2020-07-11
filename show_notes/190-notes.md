# Python Bytes 190
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

**Brian #1:** [**Python async frameworks - Beyond developer tribalism**](https://www.encode.io/articles/python-async-frameworks-beyond-developer-tribalism)

- Tom Christie 
	- Written on encode.io. encode also encompasses several awesome projects:
		- Django REST framework
		- HTTPX
		- async projects: starlette, uvicorn, orm, databases, broadcaster
- Partly a reaction to “[Async Python is not faster](http://calpaterson.com/async-python-is-not-faster.html)”
- Tom would like to see the Python community move beyond polarizing discussions.
- “… we could probably benefit from a bit more recognition of where there is shared ground. And in areas where there’s less clarity, to be able to have constructive conversations around the relative merits in differing approaches.”
- Some points about performance
	- You probably shouldn’t care about performance when you start a project. Success of a project is more related to development experience and strength of the surrounding  ecosystem.
	- We should care enough about performance that people don’t dismiss Python due to performance issues.
	- Be careful about the word “performance”. Single async function calls are slightly slower. But as concurrency increases on I/O bound systems, async Python will remain more efficient at interleaving the concurrent tasks.
	- There are no good benchmarks.
- There are valid unknowns. 
	- Should we have hybrid frameworks or have new async frameworks?
- There are different approaches
	- asyncio, trio, twisted, curio
- In general, Python async discussions continue to move toward positive discourse, even with this divisive topic and strong opinions.
- “In short this is a call for the benefits of adopting **a genuinely collaborative mindset rather than a competitive mindset**.
- We may all working on different little corners of the landscape, but we’re can still all appreciate that in the bigger view, we’re all working together.”


**Michael #2:** [**commitizen**](https://github.com/commitizen-tools/commitizen)

- Create committing rules for projects 🚀, auto bump versions ⬆️ and auto changelog generation 📂
- by Wei Lee
- For teams
- Main purpose is to define a standard way of committing rules and communicating it (using the cli provided by commitizen).
- **Commitizen features**
	- Command-line utility to create commits with your rules. Defaults: [Conventional commits](https://www.conventionalcommits.org)
	- Display information about your commit rules (commands: schema, example, info)
	- Bump version automatically using [semantic versioning](https://semver.org/) based on the commits. [Read More](https://github.com/commitizen-tools/commitizen/blob/master/docs/bump.md)
	- Generate a changelog using [Keep a changelog](https://keepachangelog.com/)

**Anthony #3:** **International PyCons go online (kind of)**
There are lots of regional PyCons across the world. Some of the larger ones are 

Cancelled:

- PyConWeb, PyCon Israel, PyCon Odessa (Ukraine), EuroSciPy (Spain), PyCon Brasil, [PyCon UK](https://2020.pyconuk.org/), PyCon Thailand, [PyCon ES (Spain)](https://2020.es.pycon.org/), [DragonPy](http://dragonpy.com/) (Slovenia), [PyLatam](https://www.pylatam.org/en/), [PyCon DE](https://de.pycon.org/), [PyCon CZ](https://cz.pycon.org/2020/)

Online:

- [PyCon US](https://us.pycon.org/2020/online/), [Python Web Conference](https://2020.pythonwebconf.com/), [FlaskCon](https://flaskcon.com/#), [SciPy, PyHEP](https://www.scipy2020.scipy.org/), [EuroPython](https://ep2020.europython.eu/), [PyCon JP (Japan)](https://pycon.jp/2020/), [PyCon AU](https://2020.pycon.org.au/) (Australia), PyCon Bolivia, [PyCon ZA (RSA)](https://za.pycon.org/), [PyCon APAC (Malaysia)](https://pycon.my/), [PyCon HK](https://pycon.hk/schedule-pycon-hk-2020-spring/), [PyBay](https://pybay.com/), [PyCon Africa](https://africa.pycon.org/)

In Person:

- [PyCon Taiwan](https://tw.pycon.org/2020/en-us/), [PyCon Italia](https://pycon.it/en/), [PyCon Russia](https://pycon.ru/)

Favourites:

- [Deceptive Security using Python](https://youtu.be/N1ZcjR6yMlM?t=103) - Gajendra Deshpande
- [If Statements are a Code Smell](https://www.youtube.com/watch?v=P0kfKqMHioQ) - Aly Sivji 
- [Stop Using Mocks.. For a while](https://www.youtube.com/watch?v=rk-f3B-eMkI) - Harry Percival
- [Network Analysis and Text PEP in Analysis](https://www.youtube.com/watch?v=o-UBokTvQjE&t=14970s) - Tomoko Furuki
- [Using Python to Detect Vulnerabilities in Binaries](https://www.youtube.com/watch?v=k3fM9KqKfTg) - Terri Oda
- [Optimize Python and Django apps with PostGres superpowers](https://www.youtube.com/watch?v=dyBLGjCQJHs) - Louise Grandjonc
[](https://www.youtube.com/watch?v=o-UBokTvQjE&t=14970s)


**Brian #4:** [**PEP 618 -- Add Optional Length-Checking To zip**](https://www.python.org/dev/peps/pep-0618/)

- This PEP proposes adding an optional strict boolean keyword parameter to the built-in zip. When enabled, a ValueError is raised if one of the arguments is exhausted before the others.
- Accepted for Python 3.10
- Awesome. I really dislike checking length of everything before using zip
- Without it, zip silently throws away any data past the point where there’s data in every iterable.

```
    >>> x = (1, 2, 3) # 3 will be lost
    >>> y = ('a', 'b')
    >>> list(zip(x,y))
    [(1, 'a'), (2, 'b')]
```

- with this change, `list(zip(x,y), strict=True)` would raise `ValueError`

**Michael #5: timedelta and division?**

- How do you find the difference between two times?
- `t0 = datetime.datetime.now()`
- `dt = datetime.datetime.now() - t0`
- Now what? We have `dt.total_seconds()` and things like `d.days`, `d.seconds`, `d.microseconds` but these combine in, … weird ways.
- What about `dt.total_hours()`? Oh, and why aren’t these properties?
- Well, I learned the right way from Paul Ganssle on TP 271: [**talkpython.fm/271**](https://talkpython.fm/271)
- `weeks = dt / timedelta(days=7)`
- `hours = dt / timedelta(hours=1)`
- And so on!
- Jeff commented on the episode page “Learning that you can divide a timedelta by a timedelta to come up with days, weeks, etc is like the Python tip of the year.” I agree.
- [https://docs.python.org/3/library/datetime.html#timedelta-objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)

**Anthony #6:** **Pylance released for Microsoft VS Code**
[New Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
Designed to be used *with* the Python extension, The Python Extension and the Python Language Server (using the LSP) were different projects. The Python LSP was written in .NET and the Python Extension is written in Typescript.

This extension is closed-source as Microsoft plan to use it for some proprietary technology.

- Features docstring automation, Signature help, parameter suggestions, code completion (better than existing)
- Supports auto-imports, if you start typing from a namespace, like a standard library module, it will add the import for you.
- Go to Reference, Go to Implementation shortcuts
- Uses the pyright type checker (an alternative to MyPy (Dropbox), Pyre (Facebook) and Pytype (Google))
- If you have pyright extension installed, remove it first!
- Extension is more useful with a couple of non-default settings
	- Change diagnostic mode to workspace so it inspects all files, not just open ones
	- Change type checking mode to basic (is off by default)
- In my testing had a few issues resolving super methods with mixin (multiple inheritance) in Django


Extras:

Anthony:

-  My book is out and Guido is reviewing it!

Michael: 

- Humble Bundle is going strong: [talkpython.fm/humble2020](http://talkpython.fm/humble2020)
- [Python 3.9.0b4 Is Now Ready for Testing](https://pycoders.com/link/4454/yrq2q8ogch)
- Excel to Python course is coming to Talk Python Training ([get notified](https://training.talkpython.fm/getnotified)).

Joke:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5ef8cfc9f79c8a05e915c894/9ff8c95da7da3bbf4351d0f1d566fa69/Screen_Shot_2020-06-28_at_10.10.07_AM.png)



