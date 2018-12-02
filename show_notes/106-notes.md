# Python Bytes 106
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** **Dependency Management through a DevOps Lens**

- [Python Application Dependency Management in 2018](https://hynek.me/articles/python-app-deps-2018) - Hynek
- An opinionated comparison of one use case and [pipenv](https://pypi.org/project/pipenv/), [poetry](https://github.com/sdispater/poetry), [pip-tools](https://pypi.org/project/pip-tools/)
- “We have more ways to manage dependencies in Python applications than ever. But how do they fare in production? Unfortunately this topic turned out to be quite polarizing and was at the center of a lot of heated debates. This is my attempt at an opinionated review through a DevOps lens.”
- Best disclaimer in a blog article ever:
	- “**DISCLAIMER:** The following technical opinions are mine alone and if you use them as a weapon to attack *people* who try to improve the packaging situation you’re objectively a bad person. Please be nice.”
- **Requirements:**  Solution needs to meet the following features:
	1. Allow me specify my immediate dependencies (e.g. Django),
	2. resolve the dependency tree and lock all of them with their versions and ideally [hashes](https://pip.pypa.io/en/stable/reference/pip_install/#hash-checking-mode)[**2**](https://hynek.me/articles/python-app-deps-2018/#fn:ideally-hashes),
	3. integrate somehow with `[tox](https://tox.readthedocs.io/en/latest/)` so I can run my tests,
	4. and finally allow me to install a project with all its locked dependencies into a virtual environment of my choosing.
- Seem like reasonable wishes. So far, none of the solutions work perfectly.
- A good example of pointing out tooling issues with his use case while being respectful of the people involved in creating other tools.

**Michael #2:** [**Plugins made simple with**](https://github.com/Rockhopper-Technologies/pluginlib) `[**pluginlib**](https://github.com/Rockhopper-Technologies/pluginlib)`

- makes creating plugins for Python very simple
- it relies on metaclasses, but the average programmer can easily get lost dealing with metaclasses
- Main Features:
	- Plugins are validated when they are loaded (instead of when they are used)
	- Plugins can be loaded through different mechanisms (modules, filesystem paths, entry points)
	- Multiple versions of the same plugin are supported (The newest one is used by default)
	- Plugins can be blacklisted by type, name, or version
	- Multiple plugin groups are supported so one program can use multiple sets of plugins that won't conflict
	- Plugins support conditional loading (examples: os, version, installed software, etc)
	- Once loaded, plugins can be accessed through dictionary or dot notation

**Brian #3:** [**How to Test Your Django App with Selenium and pytest**](https://pybit.es/selenium-pytest-and-django.html)

- Bob Belderbos
- “In this article I will show you how to test a Django app with pytest and Selenium. We will test our [CodeChalleng.es platform](https://codechalleng.es/) comparing the logged out homepage vs the logged in dashboard. We will navigate the DOM matching elements and more.”

**Michael #4: [Fluent collection APIs](https://github.com/olirice/flupy) (`flupy` and `asq`)**

- flupy implements a fluent interface for chaining multiple method calls as a single python expression. 
- All flupy methods return generators and are evaluated lazily in depth-first order. 
- This allows flupy expressions to transform arbitrary size data in extremely limited memory.
- Example:

```
    pipeline = flu(count()).map(lambda x: x**2) \
                           .filter(lambda x: x % 517 == 0) \
                           .chunk(5) \
                           .take(3)
    
    for item in pipeline:
      print(item)
```


- The CLI in particular has been great for our data science team. Not everyone is super comfortable with linux-fu so having a cross-platform way to leverage python knowledge on the shell has been an easy win.
- Also if you are LINQ inclined: **[https://github.com/sixty-north/asq](https://github.com/sixty-north/asq)**
- `asq` is simple implementation of a LINQ-inspired API for Python which operates over Python iterables, including a parallel version implemented in terms of the Python standard library multiprocessing module.

 
```
    # ASQ
    >>> from asq import query
    >>> words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    >>> query(words).order_by(len).then_by().take(5).select(str.upper).to_list()
    ['ONE', 'SIX', 'TEN', 'TWO', 'FIVE']
```

**Brian #5:** **Guido blogging again**

- [What to do with your computer science career](https://neopythonic.blogspot.com/2018/11/what-do-do-with-your-computer-science.html)
- Answering “A question about whether to choose a 9-5 job or be an entrepreneur”
	- entrepreneurship isn’t for everyone
	- working for someone else can be very rewarding 
	- shoot for “better than an entry-level web development job”
- And “A question about whether AI would make human software developers redundant (not about what I think of the field of AI as a career choice)”
	- AI is about automating tasks that can be boring
	- Software Engineering is never boring.

**Michael #6: [Web apps in pure Python apps with Anvil](https://anvil.works/)**

- Design with our visual designer
- Build with nothing but Python
- Publish Instant hosting in the cloud or on-site
- Paid product but has a free version
- Covered on [Talk Python 138](https://talkpython.fm/episodes/show/138/anvil-all-web-all-python)

Extras:

- Second Printing (P2) of “[Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)”



