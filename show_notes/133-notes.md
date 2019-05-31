# Python Bytes 133
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Python built-ins worth learning**](https://treyhunner.com/2019/05/python-builtins-worth-learning/#Learn_it_later)

- Trey Hunner
- “I estimate **most Python developers will only ever need about 30 built-in functions**, but which 30 depends on what you’re actually doing with Python.” 
- “I recommend triaging your knowledge:
	- Things I should memorize such that I know them well
	- Things I should know *about* so I can look them up more effectively later
	- Things I shouldn’t bother with at all until/unless I need them one day”
- all 69 built-in functions, split into
	- commonly known
	- overlooked by beginners
	- learn it later
	- maybe learn it eventually
	- you likely don’t need these
- Highlighting some:
	- overlooked by beginners
		- sum, enumerate, zip, bool, reversed, sorted, min, max, any, all
	- know it’s there, but learn it later:
		- open, input, repr, super, property, issubclass, isinstance, hasattr, getattr, setattr, delattr, classmethod, staticmethod, next
- my notes
	- I think getattr should be learned early on, because it’s default behavior is so useful. But can’t use it for dicts. Use `mydict.get(key, default)` for dictionaries.

**Michael #2:** [**Github sponsors and match**](https://github.com/sponsors)

- Like Patreon but for GitHub projects
- 2x your sponsorship: Github matches! To boost community funding, we'll match contributions up to $5,000 during a developer’s first year in GitHub Sponsors with the GitHub Sponsors Matching Fund.
- 100% to developers, Zero fees: GitHub will not charge fees for GitHub Sponsors.
- Anyone who contributes to open source—whether through code, documentation, leadership, mentorship, design, or beyond—is eligible for sponsorship.


**Brian #3:** [**Build a REST API in 30 minutes with Django REST Framework**](https://medium.com/@BennettGarner/build-your-first-rest-api-with-django-rest-framework-e394e39a482c)

- Bennett Garner
- Very fast intro including:
	- Set up Django
	- Create a model in the database that the Django ORM will manage
	- Set up the Django REST Framework
	- Serialize the model from step 2
	- Create the URI endpoints to view the serialized data
- Example is a simple hero db with hero name and alias.

**Michael #4:** [**Dependabot has been acquired by GitHub**](https://dependabot.com/blog/hello-github/)

- Automated dependency updates: Dependabot creates pull requests to keep your dependencies secure and up-to-date.
- I personally use and recommend PyUP: [**https://pyup.io/**](https://pyup.io/)
- How it works: 
	- Dependabot checks for updates: Dependabot pulls down your dependency files and looks for any outdated or insecure requirements.
	- Dependabot opens pull requests: If any of your dependencies are out-of-date, Dependabot opens individual pull requests to update each one.
	- You review and merge: You check that your tests pass, scan the included changelog and release notes, then hit merge with confidence.
- Here's what you need to know:
	- We're integrating Dependabot directly into GitHub, starting with security fix PRs 👮‍♂️
	- You can still install Dependabot from the GitHub Marketplace whilst we integrate it into GitHub, but it's now free of charge 🎁
	- We've doubled the size of Dependabot's team; expect lots of great improvements over the coming months 👩‍💻👨‍💻👩‍💻👨‍💻👩‍💻👨‍💻
- Paid accounts are now free, automatically.

**Brian #5:** [**spoof “**](http://charlesleifer.com/blog/new-features-planned-for-python-4-0/)[**New features planned for Python 4.0**](http://charlesleifer.com/blog/new-features-planned-for-python-4-0/)[**”**](http://charlesleifer.com/blog/new-features-planned-for-python-4-0/)

- Charles Leifer - also known for Peewee ORM
- This is funny, but painful. Is it too soon to joke about the pain of 2 to 3?
- A few of my favorites
	- PEP8 will be updated. Line lengths will be increased to 89.5 characters. (compromise between 79 and 100)
	- All new libraries and standard lib modules must include the phrase "for humans" somewhere in their title.
	- Type-hinting has been extended to provide even fewer tangible benefits and will be called *type whispering*.
	- You can make stuff go faster by adding async before every other keyword.
	- Notable items left out of 4.0
		- Still no `switch` statement.
		- No improvements to packaging.

**Michael #6:** [**BlackSheep web framework**](https://github.com/RobertoPrevato/BlackSheep)

- Fast HTTP Server/Client microframework for Python asyncio, using Cython, uvloop, and httptools.
- Very Flask-like API. Interesting to consider the “popularity” of Flask vs Django in this context.
- Objectives
	- Clean architecture and source code, following [SOLID principles](https://en.wikipedia.org/wiki/SOLID)
	- Intelligible and easy to learn API, similar to those of many Python web frameworks
	- Keep the core package minimal and focused, as much as possible, on features defined in HTTP and HTML standards
	- Targeting stateless applications to be deployed in the cloud
	- [High performance, see results from TechEmpower benchmarks (links in Wiki page)](https://github.com/RobertoPrevato/BlackSheep/wiki/Server-performance)
- Also has an async client much like **aiohttp**.

**Extras**

Michael: 

- Free courses in the [**Training mobile apps**](https://training.talkpython.fm/apps)
- Upcoming webcast: [**10 Tools and Techniques Python Web Developers Should Explore**](https://www.wintellect.com/webinar/10-tools-and-techniques-python-web-developers-should-explore/)
- 2019 [**PSF Board Elections**](https://www.python.org/nominations/elections/)
-  Get [**PyCharm, Support Python**](https://www.jetbrains.com/pycharm/promo/support-python/)
	- Until June 1st, get PyCharm at 30% OFF All the money raised will go toward the Python Software Foundation 

**Jokes** 

- How do you generate a random string? Put a first year Computer Science student in Vim and ask them to save and exit.
- Waiter: He's choking! Is anyone a doctor? Programmer: I'm a Vim user.
