# Python Bytes 64
Sponsored by DigitalOcean: **[http://do.co/python](http://do.co/python)**

**Brian #1: wxPython 4,** **Pheonix is now live and supports Python 3**

- [wxPython on PyPI](https://pypi.python.org/pypi/wxPython/4.0.0)
- [4.0.0](https://www.wxpython.org/news/wxpython-4.0.0-release/index.html), [4.0.1 release notes](https://www.wxpython.org/news/wxpython-4.0.1-release/index.html)
- If you haven’t played with wxPython for a while, now might be a good time.

**Michael #2:** [**typeshed**](https://github.com/python/typeshed)

- Typeshed contains external type annotations for the Python standard library and Python builtins, as well as third party packages.
- This data can e.g. be used for static analysis, type checking or type inference. 
- Used as the basis of mypy and PyCharm’s magic
- Each Python module is represented by a .pyi "stub". This is a normal Python file (i.e., it can be interpreted by Python 3), except all the methods are empty. Python function annotations (PEP 3107) are used to describe the types the function has.
- Here’s what one of these exeternal definitions looks like:

```
     class NodeVisitor():
        def visit(self, node: AST) -> Any: ...
        def generic_visit(self, node: AST) -> None: ...
```

**Brian #3:** [**Coverage 4.5 adds configurator plug-ins**](https://nedbatchelder.com/blog/201802/coverage_45.html)

- “There’s one new feature: [configurator plug-ins](http://coverage.readthedocs.io/en/latest/api_plugin.html#configurers), that let you run Python code at startup to set the configuration for coverage. This side-steps a requested feature to have different exclusion pragmas for different versions of Python.”


**Michael #4:** [**Python integrated into Unreal Engine**](https://www.unrealengine.com/en-US/blog/technology-sneak-peek-python-in-unreal-engine)

- via  Pirogov Alexander‏ ( [@Pie_Daddy](https://twitter.com/Pie_Daddy/status/948934041985781760) )
- tl;dr: Autodesk university plans to integrate Python into Unreal Engine for the data integration pipeline and ease the process of bringing assets into the game.
- Autodesk is working on that will solve complicated problems with bringing CAD data into the Unreal Engine.
- Where they are today: 
	- The Datasmith workflow toolkit, currently in beta, makes moving data into Unreal Engine as frictionless as possible. 
	- Datasmith provides high-fidelity translation of common scene assets such as geometry, textures, materials, lights and cameras from popular DCC and CAD applications into Unreal Engine.


**Brian #5:** [**Python 3.7.0b1**](https://www.python.org/downloads/release/python-370b1/) **: Beta means we should be testing it!!!**

- If not people like us and our listeners, then who? Seems like we’re a good set of beta testers.
- What are you going to test?
- I'm going to look at breakpoint() and data classes.

**Michael #6: Releases abound!**

- Django security releases issued: 2.0.2 and 1.11.10
  [https://www.djangoproject.com/weblog/2018/feb/01/security-releases/](https://www.djangoproject.com/weblog/2018/feb/01/security-releases/)
- Python 3.4.8 (security)
  [https://www.python.org/downloads/release/python-348/](https://www.python.org/downloads/release/python-348/)
- Python 3.5.5 (security)
  [https://www.python.org/downloads/release/python-355/](https://www.python.org/downloads/release/python-355/)
	 - libexpat XML lib had a security issue
- Channels 2.0 is a major rewrite of Channels
  https://channels.readthedocs.io/en/latest/releases/2.0.0.html
	- See [Talk Python’s interview](https://talkpython.fm/episodes/show/98/adding-concurrency-to-django-with-django-channels) for more details
	- Notably: Python 2.7 and 3.4 are no longer supported.

**Our news**

Brian:

- Speaking at PyCon 2018. “PyCharm and pytest”. Speaking with Paul Everitt
- Upcoming webinar: [Productive pytest with Pycharm](https://blog.jetbrains.com/pycharm/2018/02/webinar-productive-pytest-with-pycharm-with-brian-okken/)
  - Feb 22, registration open

Michael:

- [**Webinar Recording:**](https://blog.jetbrains.com/pycharm/2018/02/webinar-recording-mongodb-quickstart-with-python-and-pycharm-with-michael-kennedy/) “MongoDB Quickstart with Python and PyCharm” with Michael Kennedy
