# Python Bytes 68
Sponsored by DigitalOcean! **http://do.co/python**

**Brian #1:** [**dumb-pypi**](https://github.com/chriskuehl/dumb-pypi)

- This takes some fiddling with and trial and error. I definitely need to write up my experiences with this as a blog post.
- Combine with `pip download` (covered in [episode 24](https://pythonbytes.fm/episodes/show/24/i-have-a-local-pypi-server-and-so-do-you)), this makes it super easy to create a static locally hosted pypi server, either for all of your packages, or for your proprietary packages.
- Roughly:
```
    pip download -d my-packages-dir <package name>
    ls my-packages-dir > package-list.txt
    dumb-pypi --package-list my-packages-dir \
              --packages-url <url of my server> \
              --output-dir my-pypi
```

- Now add something like this to requirements.txt or pip commands:
- `--trusted-host <my server name> -i http://<my server>/my-pypi/simple`

**Michael #2:** [**Requests-HTML: HTML Parsing for Humans**](https://github.com/kennethreitz/requests-html)

- This library intends to make parsing HTML (e.g. scraping the web) as simple and intuitive as possible.
- When using this library you automatically get:
	-     Full JavaScript support!
	-     CSS Selectors (a.k.a jQuery-style, thanks to PyQuery).
	-     XPath Selectors, for the faint at heart.
	-     Mocked user-agent (like a real web browser).
	-     Automatic following of redirects.
	-     Connection–pooling and cookie persistence.
	-     The Requests experience you know and love, with magical parsing abilities

**Brian #3:**  [**A phone number proxy**](https://www.twilio.com/blog/2018/02/phone-number-forward-mask-python-flask.html)

-  Naomi Pentrel, [@naomi_pen](http://twitter.com/naomi_pen) on twilio blog
- Set up a phone number that you can share for temporary events to send and receive texts that get forwarded to your actual number.

**Michael #4: Notebooks galore part 1:** [**Datalore**](https://datalore.io/)

- In cloud and ready to go
- Intelligent code editor
- Out-of-the-box Python tools
- Collaboration
- Integrated version control
- Incremental calculations: Improve and adjust models without hustling with additional recalculations. Datalore follows dependencies between multiple computations and automatically applies relevant recalculations.

**Brian #5:** [**bellybutton**](https://github.com/hchasestevens/bellybutton)

- by Chase Stevens, [@hchasestevens](https://twitter.com/hchasestevens)
- Tool for creating personal static analysis/style tools like `pycodestyle`, `pylint`, and `flake8`
- Teams often have some of their own style requirements that can’t be expressed as `flake8` flags and exceptions.
- Example: deprecating internal library functions and catching that by the linter. 

**Michael #6:Notebooks galore part 2**

- [Python 3.6 Jupyter Notebook on Azure](https://www.reddit.com/r/Python/comments/7xwotz/python_36_jupyter_notebook_on_azure/?st=JDT0O9LI&sh=0c41688d)
- [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb)
- [JupyterLab is Ready for Users](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906)
	- JupyterLab is an interactive development environment for working with notebooks, code and data. Most importantly, JupyterLab has full support for Jupyter notebooks. Additionally, JupyterLab enables you to use text editors, terminals, data file viewers, and other custom components side by side with notebooks in a tabbed work area.
- you can pip install python packages within python code itself. 
	- Super useful in situation #1 when you need a package that's not included but you don't have access to the shell. 
	- If you need to upgrade a package. For example the Pandas version is a little old on Azure, so you can upgrade by simply running:

```
    import pip
    pip.main(['install', 'pandas', '--upgrade'])
```
