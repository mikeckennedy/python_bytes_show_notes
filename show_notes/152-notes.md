# Python Bytes 152
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Michael #1:** [**JPMorgan’s Athena Has 35 Million Lines of Python 2 Code, and Won’t Be Updated to Python 3 in Time**](https://www.techrepublic.com/article/jpmorgans-athena-has-35-million-lines-of-python-code-and-wont-be-updated-to-python-3-in-time/)

- With 35 million lines of Python code, the Athena trading platform is at the core of JPMorgan's business operations. A late start to migrating to Python 3 could create a security risk.
- Athena platform is used internally at JPMorgan for pricing, trading, risk management, and analytics, with tools for data science and machine learning. 
- This extensive feature set utilizes over 150,000 Python modules, over 500 open source packages, and 35 million lines of Python code contributed by over 1,500 developers, according to data presented by Misha Tselman, executive director at J.P. Morgan Chase in a talk at PyData 2017.
- And JPMorgan is going to miss the deadline
- Roadmap puts "most strategic components" compatible with Python 3 by the end of Q1 2020
- JPMorgan uses Continuous Delivery, with 10,000 to 15,000 production changes per week
- "If you maintain a library that other developers depend on," the post states, "you may be preventing them from updating to 3. By holding other developers back, you are indirectly and likely unintentionally increasing the security risks of others," adding that developers who do not publish code publicly should "consider your colleagues who may also be using your code internally."

**Brian #2:** [**organize**](https://github.com/tfeldmann/organize)

- suggested by [Ariel Barkan](https://twitter.com/ariel_blognot)
- a Python based file management automation tool
- configuration is via a yml file
- command line tool to organize your file system
- examples:
	- move all of your screenshots off of your desktop into a screenshots folder
	- move old incomplete downloads into trash
	- remove empty files from certain folders
	- organize receipts and invoices into date based folders

**Michael #3:** [**PEP 589 – TypedDict: Type Hints for Dictionaries With a Fixed Set of Keys**](https://www.python.org/dev/peps/pep-0589/)

- Author: Jukka Lehtosalo
- Sponsor: Guido van Rossum
- Status: Accepted
- Version: 3.8
- PEP 484 defines the type Dict[K, V] for uniform dictionaries, where each value has the same type, and arbitrary key values are supported. 
- It doesn't properly support the common pattern where the type of a dictionary value depends on the string value of the key.
- Core idea: Consider creating a type to validate an arbitrary JSON document with a fixed schema
- Proposed syntax:

```
    from typing import TypedDict
    
    class Movie(TypedDict):
        name: str
        year: int
    
    movie: Movie = {'name': 'Blade Runner',
                    'year': 1982}
```

- Operations on movie can be checked by a static type checker

```
    movie['director'] = 'Ridley Scott'  # Error: invalid key 'director'
    movie['year'] = '1982'  # Error: invalid value type ("int" expected)
```

**Brian #4:** [**gazpacho**](https://github.com/maxhumber/gazpacho)

- gazpacho is a web scraping library
- “It replaces requests and BeautifulSoup for most projects. “
- “gazpacho is small, simple, fast, and consistent.”
- [example of using gazpacho](https://maxhumber.com/scraping_fantasy_hockey) to scrape hockey data for fantasy sports.
- simple interface, short scripts, really beginner friendly
- retrieve with `get`, parse with `Soup`.
- I don’t think it will completely replace the other tools, but for simple get/parse/find operations, it may make for slimmer code.
- Note, I needed to update certificates to get this to work. see [this](https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/).

**Michael #5:** [**How pip install Works**](https://pydist.com/blog/pip-install)

- via PyDist
- What happens when you run pip install [somepackage]?
- First pip needs to decide which distribution of the package to install.
	- This is more complex for Python than many other languages
- There are 7 different kinds of distributions, but the most common these days are source distributions and binary wheels. 
- A binary wheel is a more complex archive format, which can contain compiled C extension code. 
- Compiling, say, numpy from source takes a long time (~4 minutes on my desktop), and it is hard for package authors to ensure that their source code will compile on other people's machines.
- Most packages with C extensions will build multiple wheel distributions, and pip needs to decide which if any are suitable for your computer.
- To find the distributions available, pip requests https://pypi.org/simple/[somepackage], which is a simple HTML page full of links, where the text of the link is the filename of the distribution.
- To select a distribution, pip first determines which distributions are compatible with your system and implementation of python.
	- binary wheels, it parses the filenames according to PEP 425, extracting the python implementation, application binary interface, and platform.
	- All source distributions are assumed to be compatible, at least at this step in the process
- Once pip has a list of compatible distributions, it sorts them by version, chooses the most recent version, and then chooses the "best" distribution for that version
- It prefers binary wheels if there are any
- Determining the dependencies for this distribution is not simple either. 
- For binary wheels, the dependencies are listed in a file called METADATA. But for source distributions the dependencies are effectively whatever gets installed when you execute their setup.py script with the install command. 
- What happens though if one of the distributions pip finds violates the requirements of another? It ignores the requirement and installs idna anyway!
- Next pip has to actually build and install the package.
- it needs to determine which library directory to install the package in—the system's, the user's, or a virtualenvs? 
- Controlled by sys.prefix, which in turn is controlled by pip's executable path and the PYTHONPATH and PYTHONHOME environment variables. 
- Finally, it moves the wheel files into the appropriate library directory, and compiles the python source files into bytecode for faster execution.
- Now your package is installed!

**Brian #6:** [**daily pandas tricks**](https://www.dataschool.io/python-pandas-tips-and-tricks/)

- Kevin Markham is sending out one pandas tip or trick per day via twitter.
- It’s been fun to watch and learn new bits.
- The link is a sampling of a bunch of them.
- Here’s just one example:

```
    Need to rename all of your columns in the same way? Use a string method:
    
    Replace spaces with _:
    df.columns = df.columns.str.replace(' ', '_')
    
    Make lowercase & remove trailing whitespace:
    df.columns = df.columns.str.lower().str.rstrip()
```

Extras

Michael:

- Switched to [Adobe Audition](https://www.adobe.com/products/audition.html)
- [Azure Databricks drops Python 2](https://docs.azuredatabricks.net/release-notes/product/2019/july.html)
- [Better Jupyter in VS Code](https://twitter.com/davorabbit/status/1176314998806630400) 
- macOS Catalina (so far so good)

Jokes:

- via [Sarcastic Pharmacist](https://twitter.com/Sarcastic_Pharm)
- [Hard to distinguish hard from easy in programming](https://xkcd.com/1425/)
