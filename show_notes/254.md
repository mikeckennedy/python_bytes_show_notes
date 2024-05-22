# Python Bytes 254


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Muhammad Raza**

**Brian #1:** **yaml, GH Actions, and Python 3.10**

- [Anthony Shaw (and others)](http://- https://twitter.com/anthonypjshaw/status/1445590908943044615?s=20)
![](https://paper-attachments.dropbox.com/s_475B9A46558034EA481F43B1DA42F12E48F56E121073AC5CB2D603642EFFC71F_1634145599744_ant.png)

- Old: `python: [3.7, 3.8, 3.9, 3.10-dev]`
- New: `python: ["3.7", "3.8", "3.9", "3.10"]`
- Reasons:
	- Github Actions use yaml. 
	- yaml treats 3.10-dev as a string, since it’s got non-numbers in it.
	- yaml treats 3.10 as a number, and is the same as 3.1
	- hence, we have to use quotes for “3.10”
	- using them on “3.7”, etc is not necessary, but is a nice consistency 

**Michael #****2****:** [**Beating C and Java, Python Becomes the #1 Most Popular Programming Language, Says TIOBE**](https://developers.slashdot.org/story/21/10/09/0029238/beating-c-and-java-python-becomes-the-1-most-popular-programming-language-says-tiobe)

-  via Brain Skin
- "For the first time in more than 20 years [we have a new leader of the pack](https://www.tiobe.com/tiobe-index/)..." the TIOBE Index announced this month. "The long-standing hegemony of Java and C is over.”
- For Tiobe, its enterprise focus, has seen Java and C dominate in recent years, but Python has been snapping at the heels of Java, and has now overtaken it...
- "Its ease of learning, its huge amount of libraries, and its widespread use in all kinds of domains, has made it the most popular programming language of today. Congratulations Guido van Rossum!"

**Muhammad #3:** \[Newspaper3k: Article scraping & curation](https://github.com/codelucas/newspaper)

- News, full-text, and article metadata extraction
- This allows you extract useful information from news articles, similar to Pocket or InstaPaper.

**Brian #4:** **PEP 660, pip 21.3, flit 3.4 -> easy editable installs**

- `pip install -e /local/dir` is a great way to have a project installed while you are developing it.
- It used to not work with `pyproject.toml` based projects. 
- Flit worked around this with `flit install` `--``pth-file` (or `--symlink`)
- [PEP660](https://www.python.org/dev/peps/pep-0660/) - Editable installs for pyproject.toml based builds (wheel based)
	- Plus tons of work by Stéphane Bidoul and others, see [Test & Code, episode 163](https://testandcode.com/163)
- pip 21.3 (Oct 11), flit 3.4 (Oct 10) now support PEP660
- And now with pip 21.3 and flit 3.4, `pip install -e` works for flit projects
- If you are using optional dependencies, for example:
```
    [project.optional-dependencies]
    test = [ "pytest", "tox", ]
```
- Then you need to use a quotes: `pip install -e ".[test]"`

**Michael #5:** [**Mito - a JupterLab Extension - generates Python code while you work on your analysis**](https://www.trymito.io/)

- via [Tomas Rollo](https://twitter.com/tomasrollo)
- Mito is a spreadsheet that helps you complete your Python analyses 10x faster. 
- You edit the Mitosheet, and it generates Python code for you. 
- Best way to experience it is to [**watch the video**](https://www.youtube.com/watch?v=VobWi0af-Tc)

**Muhammad #6:** [**troposphere**](https://github.com/cloudtools/troposphere) 
- [Python library to create AWS CloudFormation descriptions](https://github.com/cloudtools/troposphere)
- The troposphere library allows easier creation of CloudFormation templates by writing Python code to describe AWS resources.


**Extras**


Muhammad

- [How to learn Unix Tools](https://blog.nindalf.com/posts/how-to-learn-unix-tools/)

Brian

- PyCon 2022 site is live, [https://us.pycon.org/2022/](https://us.pycon.org/2022/)

**Joke:** [**Alphabet cancels Loon**](https://classicprogrammerpaintings.com/post/650892924479029248/alphabet-cancels-loon-zdzislaw-beksinski-1979)
