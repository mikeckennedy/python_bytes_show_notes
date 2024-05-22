# Python Bytes 160

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Brian #1:** [**Type Hints for Busy Python Programmers**](https://inventwithpython.com/blog/2019/11/24/type-hints-for-busy-python-programmers/)

- Al Sweigart, [@AlSweigart](https://twitter.com/AlSweigart)
- We’ve (Michael and myself, of course) convinced you that type hints might be a good thing to help reduce bugs or confusion or whatever. Now what? 
- Al’s got your back with this no nonsense guide to get you going very quickly.
- Written as a conversation between a programmer and an type hint expert. Super short. Super helpful.
- `typing` and `mypy` are the modules you need.
- There are other tools, but let’s start there.
- Doesn’t affect run time, so you gotta run the tool. 
- Gradually add, don’t have to do everything in one go.
- Covers the basics
- And then the “just after basics” stuff you’ll run into right away when you start, like:
	- Allowing a type and None: `Union[int, NoneType]`
	- `Optional` parameters
	- Shout out to `Callable`, `Sequence`, `Mapping`, `Iterable`, available in the documentation when you are ready for them later
- Just really a great get started today guide.

**Michael #2:** [**auto-py-to-exe**](https://pypi.org/project/auto-py-to-exe/)

- A `.py` to `.exe` converter using a simple graphical interface built using [Eel](https://github.com/ChrisKnott/Eel) and [PyInstaller](http://www.pyinstaller.org/) in Python.
- Using the Application
	1. Select your script location (paste in or use a file explorer)
		- Outline will become blue when file exists
	1. Select other options and add things like an icon or other files
	2. Click the big blue button at the bottom to convert
	3. Find your converted files in /output when complete
- Short [3 min video](https://www.youtube.com/watch?v=OZSZHmWSOeM&feature=youtu.be).

**Brian #3:** [**How to document Python code with Sphinx**](https://opensource.com/article/19/11/document-python-sphinx)

- Moshe Zadka, [@moshezadka](https://twitter.com/moshezadka)
- I’m intimidated by sphinx. Not sure why. But what I’ve really just wanted to do is to use it for this use of generating documentation of code based on the code and the docstrings. Many of the tutorials I’ve looked at before got me stuck somewhere along the way and I’ve given up. But this looks promising.
- Example module with docstring shown.
- Simple `docs/index.rst`, no previous knowledge of restructured text necessary.
- Specifically what extensions do I need: autodoc, napolean, and viewcode
- example `docs/conf.py` that’s really short
- setting up `tox` to generate the docs and the magic command like incantation necessary:
	-  `sphinx-build -W -b html -d {envtmpdir}/doctrees . {envtmpdir}/html`
- That’s it. (well, you may want to host the output somewhere, but I can figure that out. )
- Super simple. Awesome

**Michael #4:** [**Snek is a cross-platform PowerShell module for integrating with Python**](https://ironmansoftware.com/snek-integrating-python-in-powershell/)

- via Chad Miars
- [Snek](https://github.com/adamdriscoll/snek) is a cross-platform PowerShell module for integrating with Python. 
- It uses the [Python for .NET](https://github.com/pythonnet/pythonnet) library to load the Python runtime directly into PowerShell. 
- Using the [dynamic language runtime](https://docs.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/dynamic-language-runtime-overview), it can then invoke Python scripts and modules and return the result directly to PowerShell as managed .NET objects.
- Kind of funky syntax, but that’s PowerShell for you ;)
- Even allows for external packages installed via pip

**Brian #5:**[**How to use Pandas to access databases**](https://medium.com/jbennetcodes/how-to-use-pandas-to-access-databases-e4e74e6a329e)

- Irina Truong, [@irinatruong](https://twitter.com/irinatruong)
- You can use pandas and sqlalchemy to easily slurp tables right out of your db into memory.
- But don’t. pandas isn’t lazy and reads everything, even the stuff you don’t need.
- This article has tips on how to do it right.
- Recommendation to use the CLI for exploring, then shift to pandas and sqlalchemy.
- Tips (with examples, not shown here):
	- limit the fields to just those you care about
	- limit the number of records with `limit` or by selecting only rows where a particular field is a specific value, or something.
	- Let the database do joins, even though you can do it in pandas
	- Estimate memory usage with small queries and `.memory_usage().sum()`.
	- Tips on reading chunks and converting small int types into small pandas types instead of 64 bit types.

**Michael #6:** [**ijson — Iterative JSON parser with a standard Python iterator interface**](https://pypi.org/project/ijson/)

- Iterative JSON parser with a standard Python iterator interface
- Most common usage is having ijson yield native Python objects out of a JSON stream located under a prefix. Here’s how to process all European cities:

```
    // from:
    {
      "earth": {
        "europe": [ ... ]
      }
    }
```

stream each entry in europe as item:

```
    objects = ijson.items(f, 'earth.europe.item')
    cities = (o for o in objects if o['type'] == 'city')
    for city in cities:
        do_something_with(city)
```

Extras:

Michael:

- [Python decision makers webcast](https://www.crowdcast.io/e/python-for-decision) on January 14th, 9:30am US Pacific
- Guido steps down from Steering Council via Vincent POULAILLEAU
- [GitHub Archive Program](https://archiveprogram.github.com/), Preserving open source software for future generations, [video](https://www.youtube.com/watch?v=fzI9FNjXQ0o)
- Python 2.7 will be [removed from Homebrew](https://brew.sh/2019/11/27/homebrew-2.2.0/), via Allan Hansen
- [Django 3.0 released](https://docs.djangoproject.com/en/3.0/releases/3.0/)

Joke:

- Question: "What is the best prefix for global variables?"
- Answer: `#` 
- via shinjitsu

- A web developer walks into a restaurant. He immediately leaves in disgust as the restaurant was laid out in tables.
- via shinjitsu

