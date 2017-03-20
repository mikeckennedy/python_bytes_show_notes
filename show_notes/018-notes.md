# Python Bytes 18
(comment: I’d like to try on this episode something like Michael:”… I’m Michael Kennedy”, then I’ll say “and I’m Brian Okken”, and then we both try not to say “and we’re Wyld Stallyns”. I hope you get the reference. But seriously, I think I can introduce myself.)


**#1 Brian: [pdir2](https://github.com/laike9m/pdir2)**

- Nice use of animated gif to showcase what it does.
- It’s a replacement for `dir()` to use interactively.
- `pip install pdir2` , but `import pdir` .
- `pdir(something)` gives you all that `dir()` does, but splits things into categories like exceptions, functions, attributes, … 
- each item on one line, and includes the first line of the docstring for the item.
- Also, uses colors nicely. (Except I need to run it in a shell with non-black background on my mac or I can’t see the docstring output. )
- Hugely useful if you use `dir()` interactively. 
- 😞 Readme is in markdown, pypi still can’t handle that well. Maybe a listener can do a pull request on it to spiff up the pypi page: [https://pypi.python.org/pypi/pdir2](https://pypi.python.org/pypi/pdir2)
- Consider pairing this with [**ptpython**](https://github.com/jonathanslenders/ptpython)

**#2 Michael:** [**How to recover lost Python source code if it's still resident in-memory**](https://gist.github.com/simonw/8aa492e59265c1a021f5c5618f9e6b12)

- Ooops: I screwed up using git ("git checkout --" on the wrong file) and managed to delete the code I had just written, but it was still running in memory.
- Uses
  - [http://pyrasite.com/](http://pyrasite.com/) Tools for injecting code into running Python processes
  - [https://github.com/rocky/python-uncompyle6/](https://github.com/rocky/python-uncompyle6/) A Python cross-version decompiler
- Main take-away: Really cool to attach **pyrasite** and explore a running Python process for many reasons.

**#3 Brian:** [**New Interesting Data Types in Python 3**](https://github.com/topper-123/Articles/blob/master/New-interesting-data-types-in-Python3.rst)

- `types.MappingProxyType` - acts like a dictionary, but it’s read only. Convenient for exposing a mutable data structure through an API and making it less convenient for the client code to modify things they aren’t supposed to.
- `types.SimpleNamespace`- kind of a general purpose class with attributes defined by the constructor parameters you pass in. May be useful in places where you would use `collections.namedtuple` . 
- `typ``ing.NamedTuple` - You define a class derived from `NamedTuple`, and define attributes with types and optionally a default value. Constructor automatically assigns the attributes in order.
- These types help you to create quick small classes/types allow concise and readable code.

**#4 Michael:** [**howdoi**](https://github.com/gleitz/howdoi)

- Instant coding and shell answers via the command line 
- Examples
  - howdoi print stack trace python
  - howdoi connect sqlalchemy
  - howdoi python save dict
  - howdoi debug python
  - howdoi install ohmyzsh
  - howdoi change path macos
- Notable related 
  - [https://github.com/nvbn/thefuck](https://github.com/nvbn/thefuck)

**#5 Brian: A python project from a listener of the show converts to asyncio and speeds up by 150x**

- Project is a Python interface to a commercial cloud based CRM called Emarsys. But the specifics are kinda beside the point.
- Comment from episode 17: [http://disq.us/p/1h43lc0](http://disq.us/p/1h43lc0) From Diego Mora Cespedes
  
_Another awesome episode, thanks Michael and Brian!_

_About asyncio being awesome, I had my own experience. I had to send information about hundreds of thousands of users to a CRM through their public API daily. Without asyncio, it would have taken 50 hours daily, which we all know is just not possible! After developing a sync (using requests) and async (using aiohttp) client for their API, I managed to send the information about the users to the CRM asynchronously, and it takes... ... ... wait for it... ... ... 20 minutes!_

_So that's 150 times faster than without asyncio!_

_Anyway, if you wanna take a look at the client I open sourced, here is the link: [https://github.com/transcovo/pymarsys](https://github.com/transcovo/pymarsys)_

_Oh yeah, fun fact: the first time I implemented the async functionality, I made too many API calls at the same time, my mac crashed and I think I DDoSed the CRM. Now I use semaphores, which allow you to limit the number of tasks you launch at the same time. So much Python awesomeness!_
    
- However, I can’t find where in this code he uses semaphores, so here’s an example that does use semaphores to limit how many connections to make at a time.
  - [Making 1 million requests with python-aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html)
  

**#6 Michael:** [**cookiecutter-pyramid-talk-python-starter**](https://github.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter)

An opinionated Cookiecutter template for creating Pyramid web applications starting way further down the development chain. This cookiecutter template will create a new Pyramid web application with email, sqlalchemy, rollbar, and way more integrated.

- **Factored and organized**: This code was generalized out of a large, professional web application
- **Master layout template**: Comes pre-configured with a master layout template. Navigation, CSS, JS, etc is factored into a single template file and is reused across all views
- **Chameleon language**: This template uses the chameleon template language (the cleanest template language for Python - we did say opinionated right?)
- **Pyramid Handlers**: Code is factored into handler / controller classes. You have the full power of object-oriented programming immediately available
- **Secure user management**: The app comes with full user management. Users can register, log in and out, and reset passwords. We use the passlib package for secure user storage using best practices SQLAlchemy data access: Comes with SQLAlchemy ORM preconfigured using sqlite
- **Bootstrap and modern design**: As you can see from the screenshot below, the app comes with bootstrap and fontawesome. It uses a free, open-source theme and images used under CC-Attribution.
- **Logging with LogBook**: A logging system for Python that replaces the standard library’s logging module. It was designed with both complex and simple applications in mind and the idea to make logging fun
- **Runtime error monitoring with Rollbar**: Rollbar adds runtime notifications and detailed error tracking and it comes pre-configured in this template
- **Mailing list integration**: Comes with Mailchimp integration. Just enter your API key and list ID to start collecting and managing users for your mailing list
- **Outbound email with templates**: The app has a set of static HTML files with placeholders that are loaded by the outbound email system and populated with user data
- **Bower static resource management**: Most templates are based on out-of-date files (css templates, js, etc.). This template is uses bower for it's static files. This means a single CLI command will get you the latest everything.
- **Fast pages that are never stale**: Every static resource is referenced with our own cache busting system. This means you can use extremely aggressive caching for performance on static files yet they immediately invalidate upon changes
- **Comes with an entire online course**: This template is built from the final project in Python for Entrepreneurs, a 20 hour course on building professional web apps in Python and Pyramid from Talk Python Training


What are we up to?

Brian: 

- some gardening. planted 5 trees this weekend and pruned a cherry and a pear tree.
- some dining, it’s [Portland March dining month](http://www.oregonlive.com/dining/index.ssf/2017/02/27_portland_dining_month_resta.html). 
- [writing](http://pythontesting.net/books/pytest/). nothing to announce yet. But I’m super grateful to the early tech editors for comments on the first 4 chapters. Lots of edits in store as I chug through all of the incredible feedback. I’m hugely humbled by having incredible programmers and great writers read my writing and provide feedback. They are helping to make the book way more valuable than I could have done by myself.


