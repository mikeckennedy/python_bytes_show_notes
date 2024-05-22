# Python Bytes 249

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **[Erik Christiansen](https://twitter.com/Hellsen83)**

**Michael #1:** [**Fickling**](https://github.com/trailofbits/fickling)

- via Oli
- A Python pickling decompiler and static analyzer
- Pickled ML models are becoming the data exchange and workflow of ML
- Analyses pickle files for security risks - It can also remove or insert [malicious] code into pickle files...  
- Created by a security firm, it can be a useful defensive or offensive tool.
- Perhaps it is time to screen all pickles?
```
    >>> import ast
    >>> import pickle
    >>> from fickling.pickle import Pickled
    >>> print(ast.dump(Pickled.load(pickle.dumps([1, 2, 3, 4])).ast, indent=4))
    Module(
        body=[
            Assign(
                targets=[
                    Name(id='result', ctx=Store())],
                value=List(
                    elts=[
                        Constant(value=1),
                        Constant(value=2),
                        Constant(value=3),
                        Constant(value=4)],
                    ctx=Load()))])
```
- You can test for common patterns of malicious pickle files with the `--check-safety` option
- You can also safely trace the execution of the Pickle virtual machine without exercising any malicious code with the `--trace` option.
- Finally, you can inject arbitrary Python code that will be run on unpickling into an existing pickle file with the `--inject` option.
- See **[Risky Biz's episode for more details](https://risky.biz/RB635/)**.

**Brian #2:** [**Python Project-Local Virtualenv Management**](https://hynek.me/til/python-project-local-venvs/)

- **Hynek Schlawack**
- Only works on UNIX-like systems. MacOS, for example.
- Instructions
	- Install direnv. (ex: brew install direnv)
	- Put this into a `.envrc` file in your project root: 
    - `layout python python3.9`
- Now
	- when you `cd` into that directory or a subdirectory, your virtual environment is loaded.
	- when you cd out of it, the venv is unloaded
- Notes: 
	- Michael covered direnv on [Episode 185](https://pythonbytes.fm/episodes/show/185/this-code-is-snooping-on-you-a-good-thing). But it wasn’t until Hynek spelled it out for me how to use it with venv that I understood the simplicity and power. 
	- Not really faster than creating a venv, but when flipping between several projects, it’s way faster than deactivating/activating.
	- You can also set env variables per directory (kinda the point of direnv)

**Erik #3:** **[Testcontainers](https://github.com/testcontainers/testcontainers-python)**

“Python port for testcontainers-java that allows using docker containers for functional and integration testing. Testcontainers-python provides capabilities to spin up docker containers (such as a database, Selenium web browser, or any other container) for testing. “ (pypi description).

- Provides cloud native services, many databases and the like (e.g. Google Cloud Pub/Sub, Kafka..)
- Originally a java project, still a way to go for us python programmers to implement all services
- Provides an example for use in CI/CD by leveraging Docker in Docker
```
    import sqlalchemy
    from testcontainers.mysql import MySqlContainer
    
    with MySqlContainer('mysql:5.7.17') as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        version, = engine.execute("select version()").fetchone()
        print(version)  # 5.7.17
```

**Michael #4:** [**jc**](https://github.com/kellyjonbrazil/jc)

- via Garett
- CLI tool and python library that converts the output of popular command-line tools and file-types to JSON or Dictionaries. This allows piping of output to tools like jq and simplifying automation scripts.
- Run it as `COMMAND ARGS | jc --C`OMMAND
- Commands include: `systemctl`, `passwd`, `ls`, `jobs`, `hosts`, `du`, and `cksum`.

**Brian #5:**  [**What is Python's Ellipsis Object?**](https://florian-dahlitz.de/articles/what-is-pythons-ellipsis-object)

- Florian Dahlitz
- `Ellipsis` or `…`  is a constant [defined in Python](https://docs.python.org/3/library/constants.html#Ellipsis) 
	- “Ellipsis: The same as the ellipsis literal “...”. Special value used mostly in conjunction with extended slicing syntax for user-defined container data types.”
- Can be used in type hinting
	- Func returns two int tuple
```
	def return_tuple() -> tuple[int, int]:
    pass
```
- Func returns one or more integer:
```
    def return_tuple() -> tuple[int, ...]:
        pass
```
- Replacement for `pass`:
```
    def my_function():
        ...
```
- Ellipsis in the wild, “if you want to implement a certain feature where you need a non-used literal, you can use the ellipsis object.”
	- FastAPI : [Ellipsis used to make parameters required](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#make-it-required)
	- Typer: [Same](https://typer.tiangolo.com/tutorial/arguments/optional/)

**Erik #6:** **[PyTorch Forecasting](https://pytorch-forecasting.readthedocs.io/en/latest/)**
PyTorch Forecasting aims to ease state-of-the-art timeseries forecasting with neural networks for both real-world cases and research alike. The goal is to provide a high-level API with maximum flexibility for professionals and reasonable defaults for beginners. 

- basically tries to achieve for time series what fast.ai has achieved for computer vision and natural language processing
- The package is built on PyTorch Lightning to allow training on CPUs, single and multiple GPUs out-of-the-box.
- Implements of Temporal Fusion Transformers (https://arxiv.org/abs/1912.09363)
	- interpretable - can calculate feature importance
- Hyperparameter tuning with [optuna](https://optuna.readthedocs.io/)

**Extras**

Brian

- [Python 3.10rc2](https://blog.python.org/2021/09/python-3100rc2-is-available.html) available. 3.10 is about a month away

Michael

- **GoAccess** follow up
- **Caffinate more** - via Nathan Henrie: you mentioned the MacOS /usr/bin/caffeinate tool on "https://pythonbytes.fm/episodes/show/247/do-you-dare-to-press-.". Follow caffeinate with long-running command to keep awake until done (caffeinate python -c 'import time; time.sleep(10)'), or caffeinate -w "$PID" for an already running task. 
- [**Python Keyboard**](https://twitter.com/smtibor/status/1433870246276907009) (via Sean Tabor)
- [**Open source is booming**](https://www.cnbc.com/2021/09/03/mongodb-tops-30-billion-market-cap-in-banner-week-for-open-source.html) (via Mark Little)
- [**FFMPEG.WASM ffmpeg.wasm is a pure WebAssembly**](https://ffmpegwasm.netlify.app/) via Jim Anderson
- Everything is fine: [**PyPI packages**](https://www.theregister.com/2021/08/02/in_brief_security/)
- [**Python 3.10 RC 2 is out**](https://twitter.com/pyblogsal/status/1435611382976684039)

**Joke:** [**200 == 400**](https://www.reddit.com/r/ProgrammerHumor/comments/jnb9fa/when_you_only_validate_the_http_code_of_the/) 
