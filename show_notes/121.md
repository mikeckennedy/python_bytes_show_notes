# Python Bytes 121
Sponsored by Datadog: [*pythonbytes.fm/datadog*](http://pythonbytes.fm/datadog)

**Brian #1:** [**Futurize**](https://python-future.org/automatic_conversion.html) **and** [**Auto-Futurize**](https://github.com/tdhopper/auto-futurize)

- Staged automatic conversion from Python2 to Python3 with [futurize](https://python-future.org/automatic_conversion.html) from python-future.org
  - `pip install future`
- Stages:
	- 1: safe fixes: 
		- exception syntax, print function, object base class, iterator syntax, key checking in dictionaries, and more
	- 2: Python 3 style code with wrappers for Python 2
		- more risky items to change
		- separating text from bytes, quite a few more
	- very modular and you can be more aggressive and more conservative with flags.
- Do that, but between each step, run tests, and only continue if they pass, with [auto-futurize](https://github.com/tdhopper/auto-futurize) from Timothy Hopper.
	- a shell script that uses `git` to save staged changes and `tox` to test the code.

**Michael #2:** [**Tech blog writing live stream**](https://www.youtube.com/watch?v=vtlaNShM_s0&feature=youtu.be)

- via [Anthony Shaw](https://twitter.com/anthonypjshaw/status/1101264901232779264)
- Live stream on "technical blog writing"
- Talking about how I put articles together, research, timing and other things about layouts and narratives.
- Covers “Modifying the Python language in 6 minutes”, deep article
- Listicals, “5 Easy Coding Projects to Do with Kids”
- A little insight into what is popular.
- Question article: Why is Python Slow?
- Tourists guide to the CPython source code

**Brian #3**: [**Try out walrus operator in Python 3.8**](https://medium.com/hultner/try-out-walrus-operator-in-python-3-8-d030ce0ce601)

- Alexander Hultnér
- The walrus operator is the assignment expression that is coming in thanks to PEP 572.

```
    # From: https://www.python.org/dev/peps/pep-0572/#syntax-and-semantics
    # Handle a matched regex
    if (match := pattern.search(data)) is not None:
        # Do something with match
    
    # A loop that can't be trivially rewritten using 2-arg iter()
    while chunk := file.read(8192):
       process(chunk)
    
    # Reuse a value that's expensive to compute
    [y := f(x), y**2, y**3]
    
    # Share a subexpression between a comprehension filter clause and its output
    filtered_data = [y for x in data if (y := f(x)) is not None]
```

- This article walks through trying this out with the 3.8 alpha’s now available.
- Using pyenv and brew to install 3.8, but you can also just download it and try it out.
	- 3.8.0a1: [https://www.python.org/downloads/release/python-380a1/](https://www.python.org/downloads/release/python-380a1/)
	- 3.8.0a2: [https://www.python.org/downloads/release/python-380a2/](https://www.python.org/downloads/release/python-380a2/)
- Ends with a demonstration of the walrus operator working in a (I think) very likely use case, grabbing a value from a dict if the key exists

```
    for entry in sample_data: 
        if title := entry.get("title"):
            print(f'Found title: "{title}"')
```

- That code won’t fail if the `title` key doesn’t exist.

**Michael #4:** [**bullet : Beautiful Python Prompts Made Simple**](https://github.com/Mckinsey666/bullet)

- Have you ever wanted a dropdown select box for your CLI? Bullet!
- Lots of design options
- Also
	- Password “boxes”
	- Yes/No
	- Numbers
- Looking for contributors, especially Windows support.

**Brian #5:** [**Hosting private pip packages using Azure Artifacts**](https://zerowithdot.com/private-pip-azure/)

- Interesting idea to utilize artifacts as a private place to store built packages to pip install elsewhere.
- Walkthrough is assuming you are working with a data pipeline.
- You can package some of the work in earlier stages for use in later stages by packaging them and making them available as artifacts.
- Includes a basic tutorial on setuptools packaging and building an sdist and a wheel.
- Need to use CI in the Azure DevOps tool and use that to build the package and save the artifact
- Now in a later stage where you want to install the package, there are some configs needed to get the pip credentials right, included in the article.
- Very fun article/hack to beat Azure into a use model that maybe it wasn’t designed for.
- Could be useful for non data pipeline usage, I’m sure.


- Speaking of Azure, we brought up Anthony Shaw’s [**pytest-azurepipelines**](https://github.com/tonybaloney/pytest-azurepipelines) pytest plugin last week. Well, it is now part of the recommended [Python template from Azure](https://github.com/Microsoft/azure-pipelines-yaml/blob/master/templates/python-package.yml). Very cool.

 

**Michael #6:** [**Async/await for wxPython**](https://medium.com/@abulka/async-await-for-wxpython-c78c667e0872)

- via Andy Bulka
- Remember asyncio and PyQt from last week?
- Similar project called wxasync which does the same thing for wxPython!
- He’s written a medium article about it https://medium.com/@abulka/async-await-for-wxpython-c78c667e0872 with links to that project, and share some real life usage scenarios and fun demo apps.
- wxPython is important because it's free, even for commercial purposes (unlike PyQt).
- His article even contains a slightly controversial section entitled "Is async/await an anti-pattern?" which refers to the phenomenon of the async keyword potentially spreading through one's codebase, and some thoughts on how to mitigate that.

**Extras**

**Michael: Mongo license followup**

- Will S. told me I was wrong! [And I was](https://www.mongodb.com/press/mongodb-issues-new-server-side-public-license-for-mongodb-community-server). :)
- The main clarification I wanted to make above was that the AGPL has been around for a while, and it is the new SSPL from MongoDB that targets cloud providers.
- Also, one other point I didn't mention -- the reason the SSPL isn't considered open source is that it places additional conditions on providing the software as a service and the OSI's open source definition requires no discrimination based on field of endeavor.

**Michael:** `python2` **becomes self-aware, enters fifth stage of grief**

- Funny [thread I started](https://twitter.com/mkennedy/status/1104210397517631488)

> "python2 -m pip list
    DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7."

Michael: [PyDist — Simple Python Packaging](https://pydist.com/)

- Your private and public dependencies, all in one place.
- Looks to be paid, but with free beta?
- It mirrors the public PyPI index, and keeps packages and releases that have been deleted from PyPI. It allows organizations to upload their own private dependencies, and seamlessly create private forks of public packages. And it integrates with standard Python tools almost as well as PyPI does.


**Joke**

A metajoke: `pip install` `--``user pyjokes` or even better `pipx install pyjokes`. Then:

`$ pyjoke`

[hilarity ensues! …]

