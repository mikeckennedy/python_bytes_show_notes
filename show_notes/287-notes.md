# Python Bytes 287

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Michael #1:** [**auto-py-to-exe**](https://github.com/brentvollebregt/auto-py-to-exe)

- Converts .py to .exe using a simple graphical interface
- A good candidate to install via pipx
- For me, just point it at the top level app.py file and click go
- Can add icons, etc. 
- Got a **.app** version and **CLI** version (I think 😉 ) 
- Required brew install python-tk to get tkinter on my mac
- I tested it against my [**URLify app**](https://github.com/mikeckennedy/urlify/).
- Oddly, only ran on Python 3.9 but not 3.10

**Brian #2:** [**8 surprising ways how to use Jupyter Notebook**](https://mljar.com/blog/how-to-use-jupyter-notebook/)

- by Aleksandra Płońska, Piotr Płoński
- Fun romp through ways you can use and abuse notebooks
    - package development
    - web app
    - slides
    - book
    - blog
    - report
    - dashboard
    - REST API

**Michael #3:** [**piptrends**](https://piptrends.com)

- by Tankala Ashok
- Made https://piptrends.com for comparing python packages downloads and GitHub Statistics.
- Built it because whenever I do research which python package I need to use for a project I need to check multiple places to finalize it so thought of putting all those things in a single place.
- Inspired by http://npmtends.com.


**Brian #4:** [**Is it a class or a function? It's a callable!**](https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable)

- by Trey Hunner
- It’s kinda hard to tell in Python. Actually, impossible to tell from staring at the calling code.
- “Of the 69 “built-in functions” listed in the Python Built-In Functions page, **only 42 are actually implemented as functions**: 26 are classes and 1 (`help`) is an instance of a callable class.
- Of the 26 classes among those built-in “functions”, four *were* actually functions in Python 2 (the now-lazy `map`, `filter`, `range`, and `zip`) but have since become classes.
- The Python built-ins and the standard library are both full of maybe-functions-maybe-classes.”
- `len` - yep, that’s a function
- `zip` - that’s a class
- `reversed`, `enumerate`, `range`, and `filter` “functions”  are all classes. But callable classes.
- Cool discussion of
    - callable objects
    - partials, itemgetters, iterators, generators, factory functions
    - …

**Extras** 

Brian:

- [**What’s in which Python**](https://nedbatchelder.com/text/which-py.html) - Ned Batchelder
    - brief bullet list of a few memorable changes in versions 2.1 through 3.11

Michael:

- [**Orion Browser**](https://browser.kagi.com) via Dan Bader
- PSF 2021 Survey Results [**are out**](https://pyfound.blogspot.com/2022/06/python-developers-survey-2021-python-is.html) (full analysis next week)

**Joke:**  [**async problems**](https://twitter.com/LukeBMorey/status/1527209064090181633)

