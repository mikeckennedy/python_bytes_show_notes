# Python Bytes 191
Live from Manning Python Conf.

Quick intro and welcome everyone. What is Python Bytes?

**Michael #1:** [**VS Code Device Simulator**](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress)

- Want to experiment with MicroPython? 
- Teaching a course with little IoT devices? 
    - Circuit Playground Express
    - BBC micro:bit
    - Adafruit CLUE with a screen
- Get a free VS code extension that adds a high fidelity simulator
- Easily create the starter code (**main.py**)
- Interact with all the sensors (buttons, motion sensors, acceleration detection, device shake detection, etc.)
- Deploy and debug on a real device when ready
![Example of it running on a CLUE](https://www.microsoft.com/en-us/garage/wp-content/uploads/sites/5/2020/04/DeviceSimulatorExpress_ScreenShot4-1.png)

- [Had the team over on Talk Python](https://talkpython.fm/episodes/show/272/no-iot-things-in-hand-simulate-them-with-device-simulator-express).

Brian #2: [**pytest 6.0.0rc1**](https://docs.pytest.org/en/latest/changelog.html) 

- New features
    - You can put configuration in pyproject.toml
    - Inline type annotations. Most user facing API and internal code.
    - New flags
        - --no-header
        - --no-summary
        - --strict-config : error on unknown config key
        - --code-highlight : turn on/off code highlighting in terminal
    - Recursive comparison for dataclass and attrs
- Tons of fixes
- Improved documentation
- There’s a list of breaking changes and deprications. But really, nothing in the list seems like a big deal to me.
- Plugin authors, including myself, should go test this.
    - Already found one problem. `pytest-check`: stop on fail works fine, but failing tests marked with xfail show up as xpass. Gonna have to look into that. And might have to recruit Anthony to help out again.
- To try it: `pip install pytest==6.0.0rc1`
- I’m currently running through the pytest book to make sure it all still works with pytest 6. So far, so good. 
    - The one hiccup I’ve found so far, TinyDB had a breaking change with 4.0, so you need to `pip install tinydb==3.15.2` to get the tasks project to run right. I should have pinned that in the original setup.py.
    - However, all of the pytest stuff is still valid.
- [Guido just tweeted](https://twitter.com/gvanrossum/status/1282175743493935104): “Yay type annotations in pytest!”

Ines #3: [**TextAttack**](https://github.com/QData/TextAttack)

- Python framework for adversarial attacks and data augmentation for natural language processing
- What are adversarial attacks? You might have seen examples like these:
    - image classifier predicting a cat even if the image is complete noise
    - people at protests wearing shirts and masks with certain patterns to trick facial recognition
    - Google Translate [hallucinating bible texts](https://deliprao.com/archives/301) if you feed it nonsense or repetitive syllables
- What does it mean to "understand" a model?
    - How does it behave in different situations, with unexpected data?
    - We can't just inspect the weights – that's not how neural networks work
    - To understand a model, we need to run it and find behaviours we don't like
- TextAttack lets you run various different “attacks” from the current academic literature
- It also lets you create more robust training data using data augmentation, for example, replacing words with synonyms, swapping characters, etc.

**Sponsor**

Us!

Check out Talk Python Training and Brian’s pytest book. Oh, and explosion.ai ;)

**Michael #4:** [**What is the core of the Python programming language?**](https://snarky.ca/what-is-the-core-of-the-python-programming-language/) ****

- By Brett Cannon, core developer
- Brett and I discussed Python implementation for [WebAssembly before](https://webassembly.org/)
- Get Python into the browser, but with the fact that both [iOS](https://developer.apple.com/documentation/javascriptcore) and [Android](https://developer.android.com/guide/webapps) support running JavaScript as part of an app it would also get Python on to mobile.
- We have  lived with [CPython](https://github.com/python/cpython) for so long that I suspect most of us simply think that "Python == CPython".
- [PyPy](https://www.pypy.org/) tries to be so [compatible](https://www.pypy.org/compat.html) that they will implement implementation details of CPython.
-  Basically most implementations of Python strive to pass CPython's test suite and to be as compatible with CPython as possible.
- Python’s dynamic nature makes it hard to do outside of an interpreter
- That has led Brett to contemplate the question of what exactly is Python?
- How much would one have to implement to compile Python directly to WebAssembly and still be considered a Python implementation?
- Does Python need a REPL?
- Could you live without `[locals()](https://docs.python.org/3/library/functions.html?highlight=locals#locals)`?
- How much compatibility is necessary to be useful? The answer dictates how hard it is to implement Python and how compatible it would be with preexisting software.
- [Brett] has no answers
    - It might make sense to develop a compiler that translates Python code directly to WebAssembly and sacrifice some compatibility for performance. 
    - It might make sense to develop an interpreter that targets WebAssembly's design but maintains a lot of compatibility with preexisting code. 
    - It might make sense to simply support RustPython in their WebAssembly endeavours. 
    - Maybe Pyodide will get us there.
- Michael’s thoughts: 
- How about a Python standard language spec? A standard-library “standard???!?” spec. It’s possible - .[NET did it](https://docs.microsoft.com/en-us/dotnet/standard/net-standard).
- What would be build if we could build it with web assembly?
- Interesting options open up, say with NodeJS like capabilities, front-end frameworks
- This could be MUCH bigger if we got browser makes to support alternative runtimes through WebAssembly

Brian #5: **Getting started with Pathlib**

- Chris May
- Blog post: [Stop working so hard on paths. Get started with pathlib!](https://everydaysuperpowers.dev/articles/stop-working-so-hard-paths-get-started-pathlib/)
- PDF “field guide”: [Getting started with Pathlib](https://everydaysuperpowers.dev/documents/3/ES-Getting_Started_with_Pathlib.pdf)
- Really great introduction to Pathlib
- Some of the info
    - This file as a path object: `Path(__file__)`
    - Parent directory: `Path(__file__).parent`
    - Absolute path:  `Path(__file__).parent.resolve()`
    - Two levels up:  `Path(__file__).resolve(strict=True).parents[1]` See pdf for explanation.
    - Current working dir: `Path.cwd()`
    - Path building with `/`
    - Working with files and folders
    - Using glob
    - Finding parts of paths and file names.
- Any time spent learning Pathlib is worth it. 
- If I can do it in Pathlib, I do. It makes my code more readable.

Ines #6: [**Data Version Control (DVC)**](https://dvc.org/)

![](https://paper-attachments.dropbox.com/s_3C80362588E556A2A94CFCC192BC01E3A9CD56E45FE09AB3F372C35AC24DB158_1594739271850_Screenshot+2020-07-14+at+17.01.25.png)

- We're currently working on v3.0 of [spaCy](https://spacy.io) and one of the big features is going to be a completely new way to train your custom models, manage end-to-end training workflows and make your experiments reproducible
- It will also integrate with a tool called DVC (short for Data Version Control), which we've started using internally
- DVC is an open-source tool for version control, specifically for machine learning and data
- Machine learning = code + data. You can check your code into a Git repo, but you can't really check in your datasets and model weights. So it's very difficult to keep track of changes.
- You can think of DVC as “Git for data” and the command line usage is actually pretty similar – for example, you run `dvc init` to initialize a repo and `dvc add` to start tracking assets
- DVC lets you track any assets by adding meta files to your repository. So everything, including your data, is versioned, and you can always go back to the commit with the best accuracy
- It also builds a dependency graph based on the inputs and outputs of each step, so you only have to re-run a step if things changed
    - for example, you might have a preprocessing step that converts your data and then a step that trains your model. If the data hasn't changed, you don't have to re-run the preprocessing step.
- They recently released a new tool called [CML](https://cml.dev/) (short for Continuous Machine Learning), which we haven't tried yet.
    - CI for Machine Learning
    - Previews look pretty cool: you can submit a PR with some changes and a GitHub action will run your experiment and auto-comment on the PR with the results, changes in accuracy and some graphs (similar to tools like Code Coverage etc.)

**Extra**

Michael: 

- [Podcast Python Search API package,](https://github.com/nalgeon/podsearch-py) by Anton Zhiyanov
- [Mid-string f-string upgrades coming to PyCharm](https://twitter.com/NotGbo/status/1275265091139756032). And [Flynt](https://github.com/ikamensh/flynt)! via [Colin Martin](https://twitter.com/NotGbo)

Ines:

- [Built-in generic types in 3.9 (PEP 585)](https://docs.python.org/3.9/whatsnew/3.9.html#pep-585-builtin-generic-types):  you can now write `list[str]` !

Brian:

- https://testandcode.com/120: FastAPI & Typer - Sebastián Ramírez

**Jokes**

Fast API Job Experience:

[Sebastián Ramírez - @tiangolo](https://twitter.com/tiangolo)
I saw a job post the other day.
It required 4+ years of experience in FastAPI.
I couldn't apply as I only have 1.5+ years of experience since I created that thing.
Maybe it's time to re-evaluate that "years of experience = skill level".

Defragged Zebra:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5ef8cf8dd4e6c71b093aa4a9/8c2413e40dbe64b2a80a6f460db7b1da/Screen_Shot_2020-06-28_at_10.08.19_AM.png)


Final call to action: subscribe to the podcast!

