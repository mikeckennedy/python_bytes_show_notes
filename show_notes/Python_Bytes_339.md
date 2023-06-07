# Python Bytes 339

Sponsored by [**InfluxDB**](https://pythonbytes.fm/influxdata) from Influxdata.

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**pystack**](https://github.com/bloomberg/pystack)

- PyStack is a tool that uses forbidden magic to let you inspect the stack frames of a running Python process or a Python core dump, helping you quickly and easily learn what it's doing.
- PyStack has the following amazing features:
    - 💻 Works with both running processes and core dump files.
    - 🧵 Shows if each thread currently holds the Python GIL, is waiting to acquire it, or is currently dropping it.
    - 🗑️ Shows if a thread is running a garbage collection cycle.
    - 🐍 Optionally shows native function calls, as well as Python ones. In this mode, PyStack prints the native stack trace (C/C++/Rust function calls), except that the calls to Python callables are replaced with frames showing the Python code being executed, instead of showing the internal C code the interpreter used to make the call.
    - 🔍 Automatically demangles symbols shown in the native stack.
    - 📈 Includes calls to inlined functions in the native stack whenever enough debug information is available.
    - 🔍 Optionally shows the values of local variables and function arguments in Python stack frames.
    - 🔒 Safe to use on running processes. PyStack does not modify any memory or execute any code in a process that is running. It simply attaches just long enough to read some of the process's memory.
    - ⚡ Optionally, it can perform a Python stack analysis without pausing the process at all. This minimizes impact to the debugged process, at the cost of potentially failing due to data races.
    - 🚀 Super fast! It can analyze core files 10x faster than general-purpose tools like GDB.
    - 🎯 Even works with aggressively optimized Python interpreter binaries.
    - 🔍 Even works with Python interpreters' binaries that do not have symbols or debug information (Python stack only).
    - 💥 Tolerates memory corruption well. Even if the process crashed due to memory corruption, PyStack can usually reconstruct the stack.
    - 💼 Self-contained: it does not depend on external tools or programs other than the Python interpreter used to run PyStack itself.

**Brian #2:** [**Securing PyPI accounts via Two-Factor Authentication**](https://blog.pypi.org/posts/2023-05-25-securing-pypi-with-2fa/)

- Donald Stufft
- “… *every* account that maintains any project or organization on PyPI will be required to enable 2FA on their account by the end of 2023.”
- “One of the key security promises that PyPI makes is that when you're downloading something, that only the people associated with that project are going to be able to upload, delete, or otherwise modify a project. That when you look at that project and see that it is owned by someone that you trust, that you can be assured that nobody else is making changes to that package on PyPI.”
- If you maintain a package on PyPI to a point where you are uploading to PyPI or plan to soon, enable 2FA on you account.
- May as well do it sooner than later. But officially, you have the rest of the year.
- This has already been a requirement for “critical projects” since last summer. (top 1% of downloads, about 3,500 projects.) See [episode 293](https://pythonbytes.fm/episodes/show/293/and-if-i-pull-this-open-source-jenga-block).
- Now it’s going to be for everyone.

**Michael #3:** [**Propan - a declarative Python MQ framework**](https://github.com/Lancetnik/Propan)

- Propan is a powerful and easy-to-use Python framework for building asynchronous web services that interact with any MQ Broker.
- It's following by [*fastapi*](https://fastapi.tiangolo.com/ru/), simplify Message Brokers around code writing and provides a helpful development toolkit, which existed only in HTTP-frameworks world until now.
- It is a modern, high-level framework on top of popular specific Python brokers libraries, based on [*pydantic*](https://docs.pydantic.dev/) and [*fastapi*](https://fastapi.tiangolo.com/ru/), [*pytest*](https://docs.pytest.org/en/latest/) concepts.
- **The key features are**
    - **Simple**: Designed to be easy to use and learn.
    - **Intuitive**: Great editor support. Autocompletion everywhere.
    - [**Dependencies management**](https://github.com/Lancetnik/Propan#dependencies): Minimization of code duplication. Access to dependencies at any level of the call stack.
    - [**Integrations**](https://github.com/Lancetnik/Propan#http-frameworks-integrations): **Propan** is fully compatible with [any HTTP framework](https://lancetnik.github.io/Propan/integrations/1_integrations-index/) you want
    - **MQ independent**: Single interface to popular MQ:
        - **Redis** (based on [redis-py](https://redis.readthedocs.io/en/stable/index.html))
        - **RabbitMQ** (based on [aio-pika](https://aio-pika.readthedocs.io/en/latest/))
        - **Kafka** (based on [aiokafka](https://aiokafka.readthedocs.io/en/stable/))
        - **SQS** (based on [aiobotocore](https://aiobotocore.readthedocs.io/en/latest/))
        - **Nats** (based on [nats-py](https://github.com/nats-io/nats.py))
    - [**RPC**](https://lancetnik.github.io/Propan/getting_started/4_broker/5_rpc/): The framework supports RPC requests over MQ, which will allow performing long operations on remote services asynchronously.
    - [**Great to develop**](https://github.com/Lancetnik/Propan#cli-power): CLI tool provides great development experience:
        - framework-independent way to manage the project environment
        - application code *hot reload*
        - robust application templates
    - [**Testability**](https://lancetnik.github.io/Propan/getting_started/7_testing): **Propan** allows you to test your app without external dependencies: you do not have to set up a Message Broker, you can use a virtual one!

**Brian #4:** [**Makefile tricks for Python projects**](https://ricardoanderegg.com/posts/makefile-python-project-tricks/)

- Ricardo Ander-Egg
- A pretty short basic starter template Makefile for Python projects with some cool snippets.
- Some default settings to have make behave sanely
    - exit on error, warn about undefined variables, disable built-in rules
    - set up working directory correctly if called from a different dir
- A `$(py)` definition that picks up the virtual environment if it’s there.
- Also `$(pip)` from the virtual env.
- Default goal and help message
    - cool trick so that `make` with no arguments just prints the help
    - And also picks up target comments as help text for the target. Neat.
- Injecting paths into PYTHONPATH, and an example on how that works if you need it.
- A `.venv` target
    - create a virtual environment, update setuptools, wheel, build, and install requirments


**Extras** 

Michael:

- [PyCon Portugal CFP](https://2023.pycon.pt/talks/cfp/)
- [DjangoCon 2024](https://2024.djangocon.eu)
- [Apple Vision Pro](https://www.apple.com/apple-vision-pro/)
- [Duet App](https://www.duetdisplay.com)

**Joke:** [Actual technical people](https://www.reddit.com/r/programminghumor/comments/1428piy/new_headsets_announced/)

