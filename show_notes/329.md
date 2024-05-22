# Python Bytes 329

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael #1:** [**Prefix-cache**](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)

- via Brendan Hannigan
- You can set an environment variable or use it as a command line argument and then instead of creating tons of `__pycache__` folders to store your `*.pyc` files right next to the source code, it puts them in some specified folder. 
- Introduced in python 3.8.

**Brian #2:**  [**NiceGUI**](https://github.com/zauberzeug/nicegui)

- Suggested by several listeners
- Browser based GUI
- “NiceGUI is an easy-to-use, Python-based UI framework, which shows up in your web browser. You can create buttons, dialogs, Markdown, 3D scenes, plots and much more.
    It is great for micro web apps, dashboards, robotics projects, smart home solutions and similar use cases. You can also use it in development, for example when tweaking/configuring a machine learning algorithm or tuning motor controllers.” - from the README


**Michael #3:** [**flask-ngrok**](https://pypi.org/project/flask-ngrok/)

- A simple way to demo Flask apps from your machine. 
- Makes your [Flask](http://flask.pocoo.org/) apps running on localhost available over the internet via [ngrok](https://ngrok.com/).
- Great for testing API consumers too.
```python
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

# Endpoints ...

if __name__ == '__main__':
  app.run()
```

**Brian #4:**  [**No-async async with Python**](https://textual.textualize.io/blog/2023/03/15/no-async-async-with-python)

- Will McGugan
- Allowing async while not requiring async
- Await me (maybe)
    - borrowed from Simon Willison’s [The “await me maybe” pattern for Python asyncio](https://simonwillison.net/2020/Sep/2/await-me-maybe/)
- Optionally awaitable
    - Providing API methods that can be called by both async and non-async code.
    - The called method really is async, but if a caller doesn’t want to know when the code is done, it can ignore the return value and not await.
- MK: I had to solve a similar problem in [**fastapi-chameleon**](https://github.com/mikeckennedy/fastapi-chameleon/blob/7ef7627de5b508a009e2350bc7d5548a710b800b/fastapi_chameleon/engine.py#L53)
- MK: [**Syncify async functions**](https://gist.github.com/mikeckennedy/c76739766ce072f980aa4df1a6dc9516).

Extras:

Brian: 

- [**PyPI has a blog**](https://blog.pypi.org/posts/2023-03-21-welcome-to-the-pypi-blog/)
- [**Docker no longer sunsetting free team plan**](https://www.docker.com/blog/no-longer-sunsetting-the-free-team-plan/)

Jokes: 

- [**Long-lived software**](https://xkcd.com/2730/)
- [**Mysteries make life more interesting**](https://pytest-cov.readthedocs.io/en/latest/markers-fixtures.html)
    - last paragraph, discussing the `cov` fixture of `pytest-cov`

