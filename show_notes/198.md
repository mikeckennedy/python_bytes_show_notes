# Python Bytes 198
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [Test & Code](https://testandcode.com/) Podcast

Special guest: [Anna-Lena Popkes](http://alpopkes.com/)

**Brian #1:** **Easily create Python scripts using argparse** 

- Back in the day, when I was writing most of my utility scripts in bash, I’d keep around an `example.bash` file with different types of arguments and flags and control structures, etc to use as a template for new scripts.
- Python has the same problem, or worse, if you use the built in argparse instead of something like click or typer. However, there are many times where you don’t want to have any external dependencies on a script, so built in argparse it is.
- But I definitely relate to this tweet: 
	- “Every time I write a python script, I have to go back to an old script of mine to remember how to set up argparse. For some reason it just does not stick in my mind AT ALL.” - [Joshua Schraiber](https://twitter.com/jgschraiber/status/1255199030738513920?s=20) 
- Well, then steps in [Ken Youens-Clark](https://twitter.com/kycl4rk) with a little utility called [new.py](https://github.com/kyclark/new.py). It’s not `pip install`-able, so you gotta clone it or fork it or copy it or whatever. But it’s cool and fairly simple to hack on yourself, and you’re going to want to make it your own anyway, so that’s fine.
- You do something like `python new.py foo.py` and it creates an example starter `foo.py` for you with:
	- a positional argument
	- a string argument
	- an integer argument
	- a file argument (which also checks to make sure the file is readable)
	- a boolean flag
- Modify, copy, paste, delete, whatever you want to it now to make it the script you need super fast.
- Also, add a `-t`  flag to it, like this `python new.py -t foo.py`, and it generates a test stub to test your new script.

**Michael #2:** [**DBeaver Database UI Tool**](https://dbeaver.io/)

- via exhuma 
- Remember I mentioned [BeeKeeper](https://www.beekeeperstudio.io/)
- Free multi-platform database tool for developers, database administrators, analysts and all people who need to work with databases. 
- Supports all popular databases: MySQL, PostgreSQL, SQLite, Oracle, DB2, SQL Server, Sybase, MS Access, Teradata, Firebird, Apache Hive, Phoenix, Presto, etc.
- Out-of-the box DBeaver supports more than 80 databases.
- Having usability as its main goal, DBeaver offers:
	- Carefully designed and implemented User Interface
	- Support of Cloud datasources
	- Support for Enterprise security standard
	- Capability to work with various extensions for integration with Excel, Git and others.
	- Multiplatform support
	- Nice UML table/entity diagrams
- Open source: [github.com/dbeaver/dbeaver](https://github.com/dbeaver/dbeaver)
- Based on Eclipse

**Anna-Lena #3:** [**pdp++ debugger**](https://github.com/pdbpp/pdbpp)

- I recently switched from using ipdb to pdb++
- Extension of the [pdb](http://docs.python.org/library/pdb.html) module of the standard library
- Fully compatible with pdb but introduces some new features to improve debugging experience
- Can easily be installed with pip install pdbpp (`pdb++` is not a valid package name)
- Favorites: 1) sticky mode, 2) smart command parsing
1. Sticky mode: “When in this mode, every time the current position changes, the screen is repainted and the whole function shown. Thus, when doing step-by-step execution you can easily follow the flow of the execution.”
2. Smart command parsing:
	- pdb tries to interpret entered commands as one of its builtin commands
	- Inconvenient in some situations
	- Example: printing value of a local variable which happens to have the same name as one of the commands (e.g. c could refer to a local variable but is interpreted as the command ‘continue’)
	- pdb++ solution: in case of ambiguity / if a variable with the same name exists in the scope, it’s preferred
	- To execute the corresponding command, you can prefix it with `!!`

**Brian #4:** **Markdown toys**

1. [HackMD.io](https://hackmd.io/)
    - I just found out about [HackMD](https://hackmd.io/) at [hackmd.io](https://hackmd.io/) and I’m quite impressed.
    - “**HackMD** is a realtime, multi-platform collaborative markdown knowledge base. You can write notes with other people on your **desktop**, **tablet** or even on the **phone**.”
    - Two panel markdown editor with some nice menus to help you remember how to do all the fancy stuff like 
	    - inserting pictures
	    - tables, with all the table options
	    - quotes, references, TOC blocks, links, etc.
    - Great for people learning Markdown and for collaborating.
    - Even has fancy addons like 
	    - math expressions
	    - UML Diagrams
	    - todo lists
    - And now, sync with github works, so you can edit files that are saved on github.
2. [Markdown Guide](https://www.markdownguide.org/)
    - Just a really good, clean, “… free and open-source reference guide that explains how to use Markdown, the simple and easy-to-use markup language you can use to format virtually any document.”
    - Includes
        - Getting started page
        - Cheat Sheet for super common elements
        - Basic Syntax for more of the details
        - Extended Syntax page
        - Tools with links to lots of tools, including HackMD

**Michael #5:** [**Python Malware and obfuscation**](https://www.cyborgsecurity.com/python-malware-on-the-rise/)

- via Connor Ferster
- Malware is starting to appear that has been written using the Python programming language. Traditionally, most malware has been written in compiled languages, such as C or C++.
- Uses all the tools we promote for distributing apps: py2exe and py2app (which I used for [urlify](https://github.com/mikeckennedy/urlify/))
- Specific examples of Python malware include [SeaDuke](https://unit42.paloaltonetworks.com/unit-42-technical-analysis-seaduke/) that was used against the Democratic National Committee back in 2015 and 2016.
- Lots of interesting tools
	- **uncompyle6:** The successor to decompyle, uncompyle, and uncompyle2- [uncompyle6](https://github.com/rocky/python-uncompyle6/) is a native Python cross-version decompiler and fragment decompiler. It can be used to translate Python bytecode back into Python source code.
	- **pyinstxtractor.py:** The [PyInstaller Extractor](https://github.com/extremecoders-re/pyinstxtractor) can extract Python data from PyInstaller compiled executables.
- Detecting Python Compiled Executables: Both PyInstaller and py2exe when compiled on Windows place unique strings within their binary executable.

**Anna-Lena #6:** [**attrs package**](https://www.attrs.org/en/stable/)

- What is `attrs`? → Python package that simplifies writing classes (dunder methods are created automatically)
- How is this related to [dataclasses](https://docs.python.org/3/library/dataclasses.html)?
	- [**PEP 557**](https://www.python.org/dev/peps/pep-0557) added Data Classes to [Python 3.7](https://docs.python.org/3.7/whatsnew/3.7.html#dataclasses) that resemble `attrs` in many ways.
	- The PEP was inspired by `attrs` and is the result of the wish to simplify writing classes without having to deal with the problems of  `namedtuple`s
	- Main difference: data classes are less powerful than attrs (certain features were sacrificed for the sake of simplicity)
	- Example: with attrs you can use [validators](https://www.attrs.org/en/stable/examples.html) in your initializer that perform some kind of validation of the input arguments (e.g. checking that they have the correct type)

Extras:

Michael:

- Was a guest on the [Technado show last week](https://www.youtube.com/watch?v=K85MLlncH2w&feature=youtu.be).
- Our Move from [Excel to Python and Pandas course](https://training.talkpython.fm/courses/move-from-excel-to-python-and-pandas) is out!

Joke:

**New code quality metric:** [**WTFs/minute**](https://www.osnews.com/story/19266/wtfsm/)
