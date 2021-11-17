# Python Bytes 258
Sponsored by **Shortcut - Get started at** [**shortcut.com/pythonbytes**](http://shortcut.com/pythonbytes)

Special guest: **Karen Dalton**

I
**Brian #1:** [**stale : github bot to “Close Stale Issues and PRs”**](https://github.com/actions/stale)

- Was one response to a question by Will McGugan 
- Something like “An issue filed on an open source project, I’ve asked a followup question about the issue, and filer doesn’t respond. Is there an easy way to close the issue after a set time period of inactivity.”
    - Just trying to get a reference to Will out of the way early in the episode.
- stale does this:
    - Warns and then closes issues and PRs that have had no activity for a specified amount of time.
    - The configuration must be on the default branch and the default values will:
        - Add a label "Stale" on issues and pull requests after 60 days of inactivity and comment on them
        - Close the stale issues and pull requests after 7 days of inactivity
        - If an update/comment occur on stale issues or pull requests, the stale label will be removed and the timer will restart
- If defaults seem too short or harsh, everything is configurable

**Michael #2:** [**jut - JUpyter notebook Terminal viewer**](https://github.com/kracekumar/jut)

- via [kidpixo](https://twitter.com/kidpixo)
- The command line tool view the IPython/Jupyter notebook in the terminal.
- Even works against remote ipynb files (via http)

**Karen #3:** **[JupyterLyte](https://github.com/jupyterlite/jupyterlite)**

- via [**Marcel Milcent**](https://twitter.com/MarcelMilcent) ****[@MarcelMilcent](https://twitter.com/MarcelMilcent)
- JupyterLite is a JupyterLab distribution that **runs entirely in the browser and is interactive**
- Built from using JupyterLab components and extensions
- Being **developed by core Jupyter developers**, but the project is still **unofficial**
- Example: [https://jupyterlite.readthedocs.io/en/latest/_static/lab/index.html](https://jupyterlite.readthedocs.io/en/latest/_static/lab/index.html)
- Offers JupyterLab or RetroLab (a.k.a JupyterLab Classic) look
- No application server required, cacheable
- Try "import this"! 


**Brian #4:** [**Feature comparison of ack, ag, git-grep, GNU grep and ripgrep**](https://beyondgrep.com/feature-comparison/)

- ack now, supplies are limited!
- Tangent for those unfamiliar with grep
    - grep is an essential tool for many developers that prints lines that match a pattern
    - `grep foo *.py` - list all lines containing “foo” in this directory
    - `grep -l foo **/*.py | grep -v venv` 
        - `**``*/**``.py` Recursively find all Python files this directory and all subdirectories
        - `-l` Print just the name of the file if it contains a “foo” in it.
        - `| grep -v venv` Exclude virtual environments, because there’s a lot of “foo” in there. (There’s gotta be a better way to do this, someone suggest a better way, please).
- Article compares ack, ag “The silver Searcher”, git-grep, grep, and rg “ripgrep”
    - Language, Licence, and regex versions
    - Features like parallelism, config, etc.
    - Fine grain feature comparisons
        - searching capability
        - regular expression style
        - search output 
        - file presentation
        - file finding
        - inclusion, exclusion
        - file type specification
        - random other features
- This is on the ack website, and kinda makes my want to try ripgrep.

**Michael #5:** [**Python Client for Airtable: pyairtable**](https://pyairtable.readthedocs.io/en/latest/)

- by [**Gui Talarico**](https://twitter.com/gtalarico/status/1432780116006891525)
- What is Airtable? Hmm kind of like:
    - Excel
    - Trello boards
    - CI Pipelines
- A big player on nocode/lowcode community 
- Check out the [**quickstart**](https://pyairtable.readthedocs.io/en/latest/getting-started.html#quickstart) to see how it works.

**Karen #6:** **Black can now format notebooks**

- via Marco Gorelli gh: [MarcoGorelli](https://github.com/MarcoGorelli) (creator of nbQA  [isort, pyupgrade, mypy, pylint, flake8, and more on Jupyter Notebooks])
- `pip install black[jupyter]`
- `black mynotebook.ipynb`
- “…it should be significantly more robust than the current third-party tools”


**Extras**

Michael

- Trying a new password manager (sorta): [**Bitwarden**](https://bitwarden.com/)
- The PSF is [**looking for an Executive Director**](https://twitter.com/PSF/status/1456035112206815237)
- [**Want a person in anime form**](https://huggingface.co/spaces/akhaliq/AnimeGANv2)? 
- [**Python 3.11.0a2 is out**](https://pythoninsider.blogspot.com/2021/11/python-398-and-3110a2-are-now-available.html) (via PyCoders)

Karen

- Volunteer in your local Python community (or volunteer to speak)

**Joke:**


![](https://paper-attachments.dropbox.com/s_C74D95C712E13FD161AAF3E98A5938D9477EE3EC2F65839F041F2ABA70F4978E_1636136051509_Screenshot_2021-10-05_at_18.51.24.png)
