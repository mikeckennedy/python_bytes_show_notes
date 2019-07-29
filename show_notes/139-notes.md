# Python Bytes 139
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest: [**Ines Montani**](https://twitter.com/_inesmontani)

**Brian #1:** [**Simplify Your Python Developer Environment**](https://medium.com/expedia-group-tech/simplify-your-python-developer-environment-aba90f32dddb)

- Contributed by Nils de Bruin
- “Three tools (pyenv, pipx, pipenv) make for smooth, isolated, reproducible Python developer and production environments.”
- The tools:
	- pyenv - install and manage multiple Python versions and flavors
	- pipx - install a Python application with it’s own virtual environment for use globally
	- pipenv - managing virtual environments, dependencies, on a per project basis
- Brian note: I’m not sold on any of these yet, but honestly haven’t given them a fair shake either, but also didn’t really know how to try them all out. This is a really good write up to get started. 


**Ines #2:** [**New fast.ai course: A Code-First Introduction to Natural Language Processing**](https://www.fast.ai/2019/07/08/fastai-nlp/)

- [fast.ai](http://fast.ai) is a really popular, free course for deep learning by Rachel Thomas and Jeremy Howard
- Also comes with a Python library and lots of notebooks
- Some influential research developed alongside the course, e.g. [ULMFiT](https://arxiv.org/abs/1801.06146) (popular algorithm for NLP tasks like text classification)
- New course on Natural Language Processing:
	- Practical introduction to NLP covering both modern neural network approaches *and* traditional techniques
	- Highlights:
		- NLP background: topic modeling and linear models
		- Rule-based approaches and real-world problem solving
		- Focus on ethics – videos on bias and disinformation

**Michael #3:** [**Cloning the human voice**](https://github.com/CorentinJ/Real-Time-Voice-Cloning)

- In 5 minutes, with Python
- via Brenden
- Clone a voice in 5 seconds to generate arbitrary speech in real-time
- An implementation of [Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf) (SV2TTS) with a vocoder that works in real-time.
- Watch the video: **[https://www.youtube.com/watch?v=-O_hYhToKoA](https://www.youtube.com/watch?v=-O_hYhToKoA)** 
- Also: [Fake voices 'help cyber-crooks steal cash](https://www.bbc.com/news/technology-48908736)’

**Brian #4:** [**Ab(using) pyproject.toml and stuffing pytest.ini and mypy.ini content into it**](https://www.reddit.com/r/Python/comments/c5jn39/til_you_can_specify_your_mypy_pytest/)

- Contributed by Andrew Spittlemeister 
- My first reaction is horror, but this is kinda my thought process with this one
	- toml is not ini (but they look close)
	- neither pytest nor mypy support storing configuration in pyproject.toml
	- they both do support using setup.cfg (but flit and poetry projects don’t use that file, or try not to)
	- they both support passing in the config file as a command line argument
	- you can be careful and write a pyproject.toml file that is both toml and ini compliant
	- drat, this is a reasonable idea, if not a little wacky
	- no **guarantee** that it will keep working
- one thing to note: use quotes for stuff you normally wouldn’t need to in ini file.

Example ini: 

```
    [pytest]
    addopts = -ra -v
```

if stuffed in pyproject.toml

```
    [pytest]
    addopts = "-ra -v"
```

to run:

```
    > mypy --config-file pyproject.toml module_name
    > pytest -c pyproject.toml
```

**Ines #5:** ****[**Polyaxon**](https://polyaxon.com/)
- *A platform for reproducing and managing the whole life cycle of machine learning and deep learning applications.*
- We talked to lots of research groups and everyone works with just their GPU on desktop. Super slow – you need to wait for results, schedule next job etc.
- Polyaxon is a free open source library built on Kubernetes. Really easy to set up, especially on Google Kubernetes Engine.
- Especially good for hyper-parameter search, where you might not need GPU experiments if you can run lots of experiments in parallel
- [Release v0.5](https://medium.com/polyaxon/polyaxon-v0-5-released-a275a322088b) just came today. Big improvements:
	- Plugins system
	- Local runs, for much easier debugging
	- New workflow engine for chaining things together and run experiments with lots of steps

**Michael #6:** [**Flynt for f-strings**](https://github.com/ikamensh/flynt)

- A tool to automatically convert old string literal formatting to f-strings
- F-Strings: Not only are they more readable, more concise, and less prone to error than other ways of formatting, but they are also faster!
- Converted over 500 lines / expressions in Talk Python Training and Python Bytes.
- Get started with a [**pipx**](https://github.com/pipxproject/pipx) install: `pipx install flynt`
- Then point it at
	- A file: `flynt somefile.py`
	- A directory (recursively): `flynt ./`
- Converts code like this: `print(``"``Greetings {}, you have found {:,} items!``"``.format(name, count))`
- To code like this: `print(f"Greetings {name}, you have found {count:,} items!")`
- Beware of the digit grouping bug.
- Good project to jumping in and contributing to open source

Extras:

- Thanks to André Jaenisch for pointing the existence of [ReDoS attacks and a good video explaining them](https://snyk.io/blog/snyking-in-regular-expression-denial-of-service-vulnerability-exploit-in-the-ms-package/).

Michael:

- [Python httptoolkit](https://httptoolkit.tech/view/python/)
- [Python Magic’s name](https://en.wikipedia.org/wiki/List_of_file_signatures) via David Martínez
- Flying Fractals ([video](https://www.reddit.com/r/Python/comments/c3zifq/raymarching_fractal_video_made_with_python_glsl/) and [code](https://github.com/neozhaoliang/pywonderland))
- Python 3.7.4 is out

Ines:

- [Explosion](https://explosion.ai/) [(?)](https://explosion.ai/)
- [spaCy IRL 2019](https://irl.spacy.io/2019)
	- our very first conference held on July 6 in Berlin
	- many amazing speakers from research, applied NLP and the community
	- all talks were recorded and will be up on [our YouTube channel](http://www.youtube.com/c/ExplosionAI) very soon
- [FastAPI](https://github.com/tiangolo/fastapi) core developer Sebastián Ramírez is joining our team
	- FastAPI was [presented by Brian](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) in episode 123 of this podcast
	- we’re big fans and have been switching all our APIs over to FastAPI
	- we’ll keep supporting the project and will definitely give Sebastián enough time to keep working on it

Joke:

- A programmer walks into a bar and orders 1.38 root beers. The bartender informs her it's a root beer float. She says 'Make it a double!’
- What do you call a developer without a side project?
	- Well rested.
