# Python Bytes 136
Brought to you by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:**  [**Voilà!**](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93)

- “from Jupyter notebooks to standalone applications and dashboards”
- Turn a notebook into a web app with:
	- custom widgets
	- runnable code (but not editable)
	- interactive plots
	- different custom grid layouts
	- templates

**Michael #2:** [**Toward a “Kernel Python”**](https://glyph.twistedmatrix.com/2019/06/kernel-python.html)

- By Glyph
- Glyph wants to Marie Kondō the standard library (and I think I agree with him)
- We have [**PEP 594**](https://www.python.org/dev/peps/pep-0594/) for removing obviously obsolete and unmaintained detritus from the standard library.
- PEP 594 is great news for Python, and in particular for the maintainers of its standard library, who can now address a reduced surface area.
- Believes the PEP may be approaching the problem from the wrong direction.
- One “dead” battery is the `colorsys` module: why not remove it? “The module is useful to convert CSS colors between coordinate systems. Today, however, the modules you need to convert colors between coordinate systems are only a `pip install` away.
- Every little bit is overhead for the core devs, consider the state of PRs
- Looking at [CPython’s keyword-based review queue](https://github.com/python/cpython/pulls?q=is%3Apr+is%3Aopen+label%3A%22awaiting+review%22+sort%3Aupdated-asc), we can see that there are *429* tickets currently awaiting review. The oldest PR awaiting review hasn’t been touched since February 2, 2018, which is almost 500 days old.
- By Glyph’s subjective assessment, on this page of 25 PRs, 14 were about the standard library, 10 were about the core language or interpreter code
- We need a “kernel” version of Python that contains only the most absolutely minimal library, so that all implementations can agree on a core baseline that gives you a “python”
- Michael: There will be a cost to beginners. But there is already.

**Brian #3:**  [**Use __main__.py**](https://shaneoneill.io/2019/06/12/use-__main__-py/)

- I didn’t know it was that easy to get `python -m <mymodule>`  to work.

**Michael #44:**  [**The CPython Bytecode Compiler is Dumb**](https://nullprogram.com/blog/2019/02/24/)

- by Chris Wellons
- Given multiple ways to express the same algorithm or idea, Chris tends to prefer the one that compiles to the more efficient bytecode.
- Fortunately CPython, the main and most widely used implementation of Python, is very transparent about its bytecode. It’s easy to inspect and reason about its bytecode. The disassembly listing is easy to read and understand.
- One fact has become quite apparent: **the CPython bytecode compiler is pretty dumb**. With a few exceptions, it’s a very literal translation of a Python program, and there is almost [no optimization](https://legacy.python.org/workshops/1998-11/proceedings/papers/montanaro/montanaro.html).
- [Darius Bacon points out](https://codewords.recurse.com/issues/seven/dragon-taming-with-tailbiter-a-bytecode-compiler) that Guido van Rossum himself said, “[Python is about having the simplest, dumbest compiler imaginable.](https://books.google.com/books?id=bIxWAgAAQBAJ&pg=PA26&lpg=PA26&dq=%22Python+is+about+having+the+simplest,+dumbest+compiler+imaginable.%22&source=bl&ots=2OfDoWX321&sig=ACfU3U32jKZBE3VkJ0gvkKbxRRgD0bnoRg&hl=en&sa=X&ved=2ahUKEwjZ1quO89bgAhWpm-AKHfckAxUQ6AEwAHoECAkQAQ#v=onepage&q=%22Python%20is%20about%20having%20the%20simplest%2C%20dumbest%20compiler%20imaginable.%22&f=false)” So this is all very much by design.
- The consensus seems to be that if you want or need better performance, use something other than Python. (And if you can’t do that, at least use PyPy.) ← Cython people, Cython.
- Example

```
    def foo():
        x = 0
        y = 1
        return x
```

Could easily be:

```
    def foo():
        return 0
```

Yet, CPython completely misses this optimization for both x and y:

```
      2           0 LOAD_CONST               1 (0)
                  2 STORE_FAST               0 (x)
      3           4 LOAD_CONST               2 (1)
                  6 STORE_FAST               1 (y)
      4           8 LOAD_FAST                0 (x)
                 10 RETURN_VALUE
```

And so on.

- Brett Cannot has expressed performance as a major focus for CPython, maybe there is something here?

**Brian #5:** **You can play with EdgeDB now, maybe**

- [A Path to a 10x Database](https://edgedb.com/blog/a-path-to-a-10x-database/)
- [EdgeDB roadmap](https://edgedb.com/roadmap/)
- Alpha 1 is available. 
- “EdgeDB is the next generation relational database based on PostgreSQL. It features a novel data model and an advanced query language.”
- I’m excited about what their doing. Looking forward to 1.0.
- Lots of great features listed in the 10x post, but what I’m most intrigued by is their [replacement of SQL with a different query language](https://edgedb.com/blog/we-can-do-better-than-sql/).

**Michael #6:** [**16 Python libraries that helped a healthcare startup grow**](https://www.pythontraininghq.com/2019/05/16-python-libraries-that-helped-a-healthcare-startup-grow/)

- via [Waqas Younas](https://www.pythontraininghq.com/author/waqas/)
- Worked with a U.S.-based healthcare startup for 7 years. This startup developed a software product that sent appointment reminders to the patients of healthcare facilities; the reminders were sent via email, text, and IVR.
    
1. Paramiko - A Python implementation of SSHv2.
2. built-in CSV module
3. SQLAlchemy - The Python SQL Toolkit and Object Relational Mapper
4. Requests - HTTP for Humans™
5. BeautifulSoup - Python library for pulling data out of HTML and XML files.
6. testscenarios - a pyunit extension for dependency injection
7. HL7 - a simple library for parsing messages of Health Level 7 (HL7) version 2.x into Python objects. 
8. Python-Phonenumbers - Library for parsing, formatting, and validating international phone numbers
9. gevent - a coroutine -based Python networking library that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop.
10. dateutil - powerful extensions to datetime (pip install python-dateutil)
11. Matplotlib - a Python 2D plotting library which produces publication quality figures
12. python-magic - a python interface to the libmagic file type identification library. libmagic identifies file types by checking their headers according to a predefined list of file types.
13. Django - a high-level Python Web framework that encourages rapid development and clean, pragmatic design
14. Boto - a Python package that provides interfaces to Amazon Web Services.
15. Mailgun Python bindings - helped us send appointment reminders seamlessly
16. Twilio’s Python bindings - helped us send appointment reminders seamlessly

**Extras**

Michael:

[United States Digital Service](https://www.usds.gov/)

**Jokes** 

Difference between ML & AI? [**Ans**](https://twitter.com/iliandili/status/1135079242130214912).
