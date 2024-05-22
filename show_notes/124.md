# Python Bytes 124
Sponsored by DigitalOcean: **[pythonbytes.fm/digitalocean](https://pythonbytes.fm/digitalocean)**

**Brian #1:** [**pytest 4.4.0**](https://docs.pytest.org/en/latest/changelog.html#pytest-4-4-0-2019-03-29) 

- Lots of amazing new features here (at least for testing nerds)
- `[testpaths](https://docs.pytest.org/en/latest/reference.html#confval-testpaths)` displayed in output, if used.
	- `pytest.ini` setting that allows you to specify a list of directories or tests (relative to test rootdir) to test. (can speed up test collection).
- Lots of goodies for plugin writers.
- Internal changes to allow subtests to work with a new plugin, [pytest-subtests](https://github.com/pytest-dev/pytest-subtests).
- Just started playing with it, but I’m excited already. Planning on a full [Test & Code](https://testandcode.com/) episode after I play with it a bit more.

```
    # unittest example:
    class T(unittest.TestCase):
        def test_foo(self):
            for i in range(5):
                with self.subTest("custom message", i=i):
                    self.assertEqual(i % 2, 0)
    # pytest example:
    def test(subtests):
        for i in range(5):
            with subtests.test(msg="custom message", i=i):
                assert i % 2 == 0
```

**Michael #2:** [**requests-async**](https://github.com/encode/requests-async)

- async-await support for requests
- Just finished talking with Kenneth Reitz, native async coming to requests, but awhile off
- Nice interm solution
- Requires modern Python (3.6)
- Interesting Flask, Quart, Starlette, etc. framework wrapper for testing

**Brian #3:** **Reasons why PyPI should not be a service**

- Dustin Ingram’s article: [**PyPI as a Service**](https://dustingram.com/articles/2019/04/02/pypi-as-a-service/)
- “Layoffs at JavaScript package registry raise questions about fate of community resource” - [The Register article](https://www.theregister.co.uk/2019/04/01/npm_layoff_staff/)
- Apparently PyPI gets requests for a private form of their service regularly, but there are problems with that.
- Currently a non-profit project under the PSF. That may be hard to maintain if they have a for-profit part.
- Donated services and infrastructure of more than $1M/year would be hard to replace.
- There are already other package repository options. Although there is probably room for others to compete.
- Currently run by volunteers for the most part. (<1 employee). Don’t think they would stick around to volunteer for a for-profit enterprise.
- conclusion: not impossible, but probably not worth it.

**Michael #4: [Jupyter in the cloud**](https://www.dataschool.io/cloud-services-for-jupyter-notebook/)

- Six easy ways to run your Jupyter Notebook in the cloud by Kevin Markham
- six services you can use to easily run your Jupyter notebook in the cloud. All of them have the following characteristics:
	- They don't require you to install anything on your local machine.
	- They are completely free (or they have a free plan).
	- They give you access to the Jupyter Notebook environment (or a Jupyter-like environment).
	- They allow you to import and export notebooks using the standard .ipynb file format.
	- They support the Python language (and most support other languages as well).
- [Binder](https://mybinder.org/) is a service provided by the Binder Project, which is a member of the Project Jupyter open source ecosystem. It allows you to input the URL of any public Git repository, and it will open that repository within the native Jupyter Notebook interface.
- [Kaggle](https://www.kaggle.com/) is best known as a platform for data science competitions. However, they also provide a free service called [Kernels](https://www.kaggle.com/kernels) that can be used independently of their competitions.
- [Google Colaboratory](https://colab.research.google.com/), usually referred to as "Google Colab," is available to anyone with a Google account. As long as you are signed into Google, you can quickly get started by creating an empty notebook, uploading an existing notebook, or importing a notebook from any public GitHub repository.
- To get started with [Azure Notebooks](https://notebooks.azure.com/), you first sign in with a Microsoft or Outlook account (or create one). The next step is to create a "project", which is structured identically to a GitHub repository: it can contain one or more notebooks, Markdown files, datasets, and any other file you want to create or upload, and all of these can be organized into folders.
- [CoCalc](https://cocalc.com/), short for "collaborative calculation", is an online workspace for computation in Python, R, Julia, and many other languages. It allows you to create and edit Jupyter Notebooks, Sage worksheets, and LaTeX documents.
- [Datalore](https://datalore.io/) was created by JetBrains, the same company who makes PyCharm (a popular Python IDE). Getting started is as easy as creating an account, or logging in with a Google or JetBrains account. You can either create a new Datalore "workbook" or upload an existing Jupyter Notebook.

**Brian #5:** **Jupyter Notebook tutorials**

- These are from Dataquest
- [**Jupyter Notebook for Beginners: A Tutorial**](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
	- Incredibly gentle, concise, useful tutorial to get started quickly.
	- Installation, creating, and running with server and browser.
	- Discussion of .ipynb files
	- Overview of interface, cells, shortcuts, markdown.
	- Kernels
	- Starting with data. Importing appropriate libraries, loading data.
	- Save and checkpoint
	- looking at data, graphing/plotting data
	- Sharing notebooks: exporting, using github and gists, nbviewer, 
- [**Tutorial: Advanced Jupyter Notebooks**](https://www.dataquest.io/blog/advanced-jupyter-notebooks-tutorial/)
	- shell commands
	- basic magics
	- autosaving
	- matplotlib inline
	- debugging in Jupyter 
	- (Brian: Gak! Maybe switch to PyCharm for debugging)
	- using timeit
	- rendering theml, latex, other languages in cells.
	- logging, extensions
	- charts with seaborn
	- macros
	- loading, importing and running external code and snippets.
	- scripted execution, even on the command line
	- parametrization with env variables
	- styling, hiding cells, working with databases


**Michael #6: [Unique sentinel values, identity checks, and when to use object() instead of None**](https://treyhunner.com/2019/03/unique-and-sentinel-values-in-python/)

- By Trey Hunner
- In Python (and in programming in general), you’ll need an object which can be uniquely identified. Sometimes this unique object represents a **stop value** or a **skip value** and sometimes it’s an **initial value**.
- Often this is None, but there are plenty of gotchas packed in there.
- Nice example of re-implementing min.
- Make sure to leverage `is` rather than `==`

```
    initial = object()
    # ...
    if minimum is not initial:
       return minimum
    # ...
```

**Extras**

**Brian**

- [pytest-neo](https://pypi.org/project/pytest-neo/)

**Michael**

- [Responder course](https://training.talkpython.fm/courses/explore_responder/responder-web-framework-mini-course)
- [AceJump](https://github.com/acejump/AceJump) for IntelliJ platforms (including PyCharm)

**Jokes**

