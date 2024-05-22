# Python Bytes 247

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**Dan Taylor**](https://twitter.com/qubitron)


**Michael #1:** [**Keep your computer awake during long processing**](https://github.com/np-8/wakepy)

- For now, use [**Michael’s fork**](https://github.com/mikeckennedy/wakepy) when on macOS. Until [**this PR is merged**](https://github.com/np-8/wakepy/pull/12).
- Do you have work that will take a long time?
- Keeping your OS working away is just a context block

```
    from wakepy import keepawake
    
    with keepawake(keep_screen_awake=False):
      ... # do stuff that takes long time
```

**Brian #2:**  [**How to write a great Stack Overflow question**](https://www.dataschool.io/how-to-ask-for-coding-help-online/)

- via Kevin Markham
- The punchline (but it’s not enough)
	- Write a brief introduction
	- Provide a self-contained code example
	- Detail the expected results and why I expect those results
	- Add any important notes
	- Link to any relevant questions
	- Write a title that summarizes the question
- Kevin starts with a question about pandas dataframes and filling in missing values.
	- The question is really application specific
- The rewrite of the question is awesome
	- Simplifies the problem into a toy example, literally, and out of the domain specific context.
	- Includes example code that can copied, pasted, and run that sets up the problem
	- Uses short and simple variable names
	- Talks about expected results. And why he expects those results.
	- Includes a dataset in the sample code that covers cases the solution needs to provide
	- Includes non-obvious requirements or non-requirements
	- Links to related questions and why they don’t solve your problem.
- I don’t think I’ve ever seen this, but I think it’d be cool to add test code that will pass when the problem is solved. But that might make the question unnecessarily long.


**Dan #3:** [**Github.dev - press ‘.’ to edit code in any GitHub repo**](https://www.tiktok.com/@vscode/video/6995256325295082757) 

- Fun bonus feature released at the same time as [GitHub Codespaces](https://github.com/features/codespaces) 
- Runs VS Code entirely in your browser - supercharged “edit button”
	- Nothing to install
	- There’s no server to pay for, though functionality is limited
	- The file system is your browser’s local storage and GitHub repo
	- You can add files and commit changes directly to your repo
- You can install extensions that support running in “VS Code Web”
- Added basic web support to the Python Extension just yesterday 
	- Syntax checking, auto-complete, go-to-definition
	- Uses type hints for packages (no python interpreter in the browser)
- You can also install [vscode-pyiodide](https://marketplace.visualstudio.com/items?itemName=joyceerhl.vscode-pyodide) to run Python code using Jupyter+Pyiodide
- Overall means you can do more powerful code editing quickly in GitHub.com, I’m looking forward to seeing how this evolves

**Michael #4:** [**Log analyzer (minus google analytics)**](https://twitter.com/junctionapps/status/1425530639621754882)

- **GoAccess** is an open source **real-time web log analyzer** and interactive viewer that runs in a **terminal** in *nix systems or through your **browser**.
- Features
	- **Fast**, **real-time**, millisecond/second updates, written in C
	- **Only** ncurses as a **dependency**
	- **Nearly all** web log **formats** (Apache, Nginx, Amazon S3, Elastic Load Balancing, CloudFront, Caddy, etc)
	- Simply set the log format and run it against your log
	- Beautiful terminal and bootstrap dashboards (Tailor GoAccess to suit your own color taste/schemes)

**Brian #5:**  [**KMK: Clackety Keyboards Powered by Python**](https://github.com/KMKfw/kmk_firmware)

- recommended by [Blaise](https://twitter.com/controlpl4n3/status/1429915992650665986?s=20)
- “firmware for computer keyboards written and configured in CircuitPython.”
- Cool list of features
	- Fully configured through a single, easy to understand Python file.
	- Single-piece or two-piece split keyboards are supported
	- Chainable keys such as KC.LWIN(KC.L) to lock the screen on a Windows PC
	- Built-in unicode macros, including emojis
	- RGB underglow and LED backlights
	- One key can turn into many more based on how many times you tap it
- One writeup I found of someone using it for a 10-key 
	- [KMK: run Python on your keyboard](https://epxx.co/artigos/kmk.html)
    - includes a video
- Seems like limited hardware so far, and although the coding might not be too difficult, you still gotta swap out of the circuitboard.
- I’m bringing this topic up because I’m hoping some keyboard kit people will put together something that just starts with the ability to run CircuitPython so I can just skip to the coding part. 

**Dan #6:** [**SQLModel - use the same models for SQL and FastAPI**](https://github.com/tiangolo/sqlmodel) 

- via [Sebastián Ramírez](https://twitter.com/tiangolo/status/1430252646968004612) (creator of SQLModel and FastAPI)
- Write a schema once and use everywhere, reduces a lot of repetitive code
	- Traditionally have to manage several layers of code to pass your data from database queries, to the backend code, expose to your API and consume from the client
	- Code-first ORMs (SQLAlchemy, Django ORM) make it easy to write code that generates SQL
	- FastAPI makes it easy to expose objects to your API using Pydantic models
	- Before you would need to create both models and convert from ORM to Pydantic using .from_orm
- SQLModel unifies those: a SQLModel is both a SQLAlchemy model and a Pydantic model
	- You can use SQLModel to interact with the database (via wrapping SQLAlchemy)
	- You can use that same model as a Pydantic model in FastAPI [requests](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/#create-heroes-path-operation) and [responses](https://sqlmodel.tiangolo.com/tutorial/fastapi/response-model/#use-response_model)
	- FastAPI also uses the Pydantic models to generate an openapi.json, meaning you could generate a client library in any language using [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator)
- Some other cool things:
	- Designed using type annotations so that editors like VS Code, PyCharm give great auto-complete out of the box, uses the proposed [dataclass_transforms](https://github.com/microsoft/pyright/blob/main/specs/dataclass_transforms.md) spec for dynamic typing
	- Supports async database sessions, alembic migrations because it’s based on SQLAlchemy (not yet documented)
	- Should be possible to integrate with postgis, ts_vectors


**Extras**

 

Brian 
-  [pip install ./local_directory](https://testandcode.com/163) is pretty interesting. Test & Code 163
    - The way pip installs from a local directory is about to change. Stéphane Bidoul joins the show to talk about it.

Dan
- [type4py](https://mirblog.net/index.php/2021/07/31/development-and-release-of-type4py-machine-learning-based-type-auto-completion-for-python/) - using ML to add type annotations to your codebase
	- retrofitting codebases with types is a pain — static type checkers can only infer so much
	- type4py [research paper](http://research paper) outlines a state of the art ML model for inferring types, adopting some techniques used in computer vision 
	- Open sourced [training code](https://github.com/saltudelft/type4py), [data set](https://zenodo.org/record/4719447), [VS Code extension](https://github.com/saltudelft/type4py-vscode-ext), and [inferencing server](https://github.com/saltudelft/type4py/tree/server/type4py/server)
	- If you have a need to add type annotations to a large code base, worth giving this a try!
	- **WARNING** the VS Code extension sends code tokens to their API on type4py.com (they do have a [privacy policy](https://github.com/saltudelft/type4py-vscode-ext/blob/master/PRIVACY.md)) — if this is a concern be sure to host the inferencing server yourself!
    

**Joke:** [**Continuous Deployment**](https://geek-and-poke.com/geekandpoke/2017/11/27/simply-explained)

Also:

“If a programmer gets an interview because of a recommendation from a friend, are they being passed by reference?” From [@CarlaNotarobot](https://twitter.com/CarlaNotarobot), via [@bluefiddleguy](https://twitter.com/bluefiddleguy/status/1430194434713522182)


