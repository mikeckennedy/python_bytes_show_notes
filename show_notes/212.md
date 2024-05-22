# Python Bytes 212

Catch the **video edition live stream** on YouTube: [**youtube.com/watch?v=oKgAsjiJqMs**](https://www.youtube.com/watch?v=oKgAsjiJqMs)

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: **Shari Eskenas**

Be part of the episode by subscribing and “smashing that bell” over at [**pythonbytes.fm/youtube**](http://pythonbytes.fm/youtube)

**Brian #1:**  [**pytest 6.2 is out**](https://docs.pytest.org/en/stable/changelog.html) 

- `pytester` fixture for plugin testing. Like `testdir`, but a better name, and uses `pathlib.Path` objects.
- verbose mode now shows the reason a test was skipped in the terminal line after the SKIPPED, XFAIL, or XPASS
- Can use monkeypatch as a context manager with `.context()` and it’s available both in test and fixture functions, but also in helper functions by using `pytest.Monkeypatch.context()`.

```  
    import os
    from contextlib import contextmanager
    import pytest
    
    def test_foo_1(monkeypatch):
        with monkeypatch.context() as mp:
            mp.setenv("foo", "bar")
            assert os.getenv("foo") == "bar"
    
    @contextmanager
    def some_func():
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("foo", "bar")
            yield
    
    def test_foo_2():
        with some_func():
            assert os.getenv("foo") == "bar"
```

- Lots of other goodies.
- related: [pytest-check](https://pypi.org/project/pytest-check/), my only released plugin for pytest, was updated to support pytest 6.x

**Michael #2:** [**SQLite as a file format (like docx)**](https://www.sqlite.org/appfileformat.html)

- via Jon Bultmeyer
- An SQLite database file with a defined schema often makes an excellent application file format. Here are a dozen reasons why this is so:
1. **Simplified Application Development.** No new code is needed for reading or writing the application file.
2. **Single-File Documents.** An SQLite database is contained in a single file, which is easily copied or moved or attached.
3. **High-Level Query Language.** SQLite is a complete relational database engine, which means that the application can access content using high-level queries.
4. **Accessible Content.** Information held in an SQLite database file is accessible using commonly available open-source command-line tools - tools that are installed by default on Mac and Linux systems and that are freely available as a self-contained EXE file on Windows.
5. **Cross-Platform.** SQLite database files are portable between 32-bit and 64-bit machines and between big-endian and little-endian architectures and between any of the various flavors of Windows and Unix-like operating systems.
6. **Atomic Transactions.** Writes to an SQLite database are [atomic](https://www.sqlite.org/atomiccommit.html). They either happen completely or not at all, even during system crashes or power failures.
7. **Incremental And Continuous Updates.** When writing to an SQLite database file, only those parts of the file that actually change are written out to disk. This makes the writing happen faster and saves wear on SSDs.
8. **Easily Extensible.** As an application grows, new features can be added to an SQLite application file format simply by adding new tables to the schema or by adding new columns to existing tables. Adding columns or tables does not change the meaning of prior queries.
9. **Performance.** In many cases, an SQLite application file format will be [faster than a pile-of-files format](https://www.sqlite.org/fasterthanfs.html) or a custom format.
10. **Concurrent Use By Multiple Processes.** SQLite automatically coordinates concurrent access to the same document from multiple threads and/or processes.
11. **Multiple Programming Languages.** Though SQLite is itself written in ANSI-C, interfaces exist for just about every other programming language you can think of.
12. **Better Applications.** If the application file format is an SQLite database, the complete documentation for that file format consists of the database schema, with perhaps a few extra words about what each table and column represents.

**Shari #3:** [**A Day in Code: Python – A picture book written in code**](https://www.kickstarter.com/projects/914595512/a-day-in-code-python)

**Brian #4:** [**PythonLabs is now hosted by Azure. and “Yes, Barry, there is a PythonLabs”**](https://azure.pythonlabs.com/)

- I can’t believe we haven’t covered this in the last 211 episodes.
- But it seems like good timing now.
- Now resides at azure.pythonlabs.com
- By Tim Peters (originally posted on January 6th, 2004 to the PSF members list)
- Barry (I’m assuming Barry Warsaw) asked the question: “… what /is/ Pythonlabs now?  Or /is/ there a Pythonlabs now?  I dunno -- Guido owns the domain name which is probably the biggest claim to Pythonlabhood there is.”
- Tim replies with a very “[Yes, Virginia, there is a Santa Clause”](https://en.wikipedia.org/wiki/Yes,_Virginia,_there_is_a_Santa_Claus)-esque answer:

Snippets include: 
- Barry, your little friends are wrong. They have been affected by the skepticism of a skeptical age. …
- Yes, Barry, there is a PythonLabs. 
- It exists as certainly as love and generosity and devotion exist, … Alas! how dreary would be the world if there were no PythonLabs! It would be as dreary as if there were no Barrys. …
- Not believe in PythonLabs! You might as well not believe in fairies. … 
- Nobody sees PythonLabs, but that is no sign that there is no PythonLabs. …
- A thousand years from now, Barry, nay 10 times 10,000 years from now, it will continue to make glad the heart of childhood.

**Michael #5: Extra, extra, extra, extra, extra, extra, hear all about it**

- #1 [**Numpy version pinning via Grice**](https://twitter.com/JustTurrble/status/1334336419205165058)
- Just catching up on Ep 208. Note in part 2 about the Numpy issue, folks can pin versions by platform with environment markers: 
```
    numpy==1.19.3; platform_system == 'Windows' 
    numpy==1.19.4; platform_system == 'Linux'
```
- #2 [**Stylesheet for PySide2 and PyQt5, this time looks like Material Design**](https://github.com/UN-GCPDS/qt-material) - via William Jamir Silva
- #3 [**Talk Python hits 20M downloads**](https://blog.michaelckennedy.net/2020/12/07/20_000_000-is-quite-a-milestone/). Python Bytes is almost 6M too.
- #4 [**Pyramid 2.0 is coming**](https://twitter.com/mkennedy/status/1336496326956077056).
- #5 [**Python 3.9.1**](https://www.python.org/downloads/release/python-391/) is out with 282 changes. Ships as a universal binary (Intel + M1) on macOS.
- #6 [**Python + Mac Mini + M1 video**](https://www.youtube.com/watch?v=PnxlHfGdihI)
- #7 [**Python Steering Council selected**](https://twitter.com/pyblogsal/status/1339260581367476224)

**Shari #6:** [**OpenMV**](https://openmv.io/)

Extras

Brian: 

- agrs, kwargs (quargs), and community
	- [a silly discussion on twitter](https://twitter.com/brianokken/status/1339027336134492160?s=20)
	- Nocole Carlson: “Huge debate … about whether you say “quargs” or “keyword arguments” for “kwargs”. Obviously “quargs” is correct.”
	- It never occurred to me to say “quargs”, but I like it.
	- Vicki Boykis replied that she’s “… never said anything but “quargs”. This is like a parallel universe.”
	- Some other amusing responses.
	- This reminded me of a conversation I might have over beer at PyCon. or at a booth, or just standing around in the hallway.
	- I miss so much the in person community. I’m grateful that little bits of it are intact on twitter.

Joke:

Pizza delivery fail

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5fc34445e547fe70d07d061f/a1b7e39f3f786d32bdd822e4f1ced1af/Screen_Shot_2020-11-28_at_9.59.04_PM.png)


Second joke:

- Why do you many developers use dark mode?
    - Because bugs are attracted to light.
