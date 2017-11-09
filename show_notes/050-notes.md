# Python Bytes 50
Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1:** [**Think Like a Pythonista**](https://www.youtube.com/watch?v=HmT6d-ho5J8&list=PL85KuAjbN_gtuA4pNPftJWaui-8ARervQ&index=2)

- 2017, by [@standupdev](https://twitter.com/standupdev) Luciano Ramalho
- [The PyBay2017 playlist](https://www.youtube.com/playlist?list=PL85KuAjbN_gtuA4pNPftJWaui-8ARervQ)
- Covered in “Think Lika a Pythonista”
  - Creating a container type, a Deck of Cards.
  - Luciano shows how to utilize duck typing, builtin types, and operator overloading while creating a type without inheritance.
  - Uses a [Jupyter notebook](http://jupyter.org/) to work with the code.
  - Describes and shows monkeypatching to implement shuffle.
  - Watch until the end, he takes feedback from the audience to optimize some code.

**Michael #2:** [**Serpent.AI - Game Agent Framework**](https://www.reddit.com/r/Python/comments/71uwob/serpentai_game_agent_framework_turn_any_video/)

- Turn ANY video game in a sandbox environment for AI & Bot programming with Python.
- goal with Serpent.AI is to lower the barriers to entry when it comes to using games as sandboxes for code experiments. 
- It unlocks your entire existing game library (Steam, DRM-Free etc.) to be used as potential game agent environments and it does so natively
- It also doesn't try to dictate how you solve your problems. Your game agent is your canvas!
- Even a twitch channel with live PyCharm + Jupyter + Game. Here’s a cool example: [https://go.twitch.tv/videos/173580782](https://go.twitch.tv/videos/173580782)
- Provides some useful conventions but is absolutely NOT opinionated about what you put in your agents: 
	- Want to use the latest, cutting-edge deep reinforcement learning algorithm? ALLOWED. 
	- Want to use computer vision techniques, image processing and trigonometry? ALLOWED. 
	- Want to randomly press the Left or Right buttons? *sigh* ALLOWED. 

**Brian #3:** [**MkDocs**](http://www.mkdocs.org/)

- I’ve been creating pytest plugins using the [pytest-plugin cookiecutter](https://github.com/pytest-dev/cookiecutter-pytest-plugin).
- One option is to start the documentation using mkdocs, so I thought I’d try it out.
- For the most part, you have a yaml file to configure things, and a directory with markdown files in it. Then you call `mkdocs build` and blammo, your documentation is built. I like markdown, so I’m going to try working with mkdocs more.
- Also want to try:
  - Generating documentation from source code using [Christian Medina](https://twitter.com/tryexceptpass)’s [How to write your own Python documentation generator](https://medium.com/python-pandemonium/python-introspection-with-the-inspect-module-2c85d5aa5a48) article and the code in a snippet, [gendocs.py](https://gist.github.com/dvirsky/30ffbd3c7d8f37d4831b30671b681c24#file-gendocs-py).
  - I know about [Sphinx](http://www.sphinx-doc.org/en/stable/), but I’m not a fan of reStructured text.
  
  
**Michael #4:**  [**PyInstaller 3.3 released**](https://github.com/pyinstaller/pyinstaller/releases/tag/v3.3)

-  PyInstaller is a program that freezes (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, FreeBSD, Solaris and AIX.
- The main goal of PyInstaller is to be **compatible with 3rd-party packages out-of-the-box**.
- **Libraries like PyQt, Django or matplotlib are fully supported**, without having to handle plugins or external data files manually. 
- The #1 thing that stands out to me in this release: Python 3.6 support!
- PyInstaller can produce single immutable self contained dependency free portable exe files using the --one-file option.
- Consider the --noconsole option too
- cx_freeze vs pyinstaller? I can tell you that pyinstaller does a much better job of actually detecting and including dependencies. I recently tried both for freezing a multi-threaded, scipy based application and cx_freeze was a real hassle to get functional. Pyinstaller more or less just magically worked in my case whereas cx_freeze took hours of debugging.

**Brian #5:** [**PEX:**](https://github.com/pantsbuild/pex) [**A library and tool for generating .pex (Python EXecutable) files**](https://github.com/pantsbuild/pex)

- Developed by twitter. Originally part of the twitter.commons package.
- `pex` is a tool to create PEX files, which are “files are self-contained executable Python virtual environments.”, from [pex.readthedocs.io](https://pex.readthedocs.io/en/stable/whatispex.html#whatispex).
- Python can import from zip files. You can add instructions at the beginning of a zip file to make it look like a python script. `pex` allows you to do that.
- Watch [WTF is PEX?](https://www.youtube.com/watch?v=NmpnGhRwsu0), a 16 min video describing how it works. Brian Wickman

**Michael #6:** [**Using Cython to protect a Python codebase**](https://bucharjan.cz/blog/using-cython-to-protect-a-python-codebase.html)

- A Python project that required the whole codebase to be protected
- They used Cython
- By following this guide, you should be able to cythonize a Python codebase with non-trivial package/module structure, thus making it difficult for evil hackers to reverse engineer it and steal your programming know-how.
- Although protecting Python sources from reverse engineering seems like a futile task at first, cythonizing all the code leads to a reasonable amount of security
- This was a Flask project!
- The current standard for Python archives is the wheel format (.whl), which aims to replace the .egg format. So, let's try to create a wheel with `python setup.py bdist_wheel`!
- Apparently, the archive contains not only compiled code, but also the sources.
- There is a way to fix this, however it is counter-intuitive.


## Our news
- Python for Windows developers: A survey → [https://docs.google.com/forms/d/e/1FAIpQLSdygLS0G91t5E8LCGtZvdfzeqdePr2jFqoiR30HZjmGbaJjNQ/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdygLS0G91t5E8LCGtZvdfzeqdePr2jFqoiR30HZjmGbaJjNQ/viewform)- 

