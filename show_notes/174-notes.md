# Python Bytes 174
Sponsored by us! [**Talk Python courses**](https://training.talkpython.fm/) & [**pytest book**](https://pragprog.com/book/bopytest/python-testing-with-pytest).

**Topic #0: Quick chat about COVID 19.**

**Brian #1:** [**Documentation as a way to build Community**](https://labs.quansight.org/blog/2020/03/documentation-as-a-way-to-build-community/)

- Melissa Mendonça
- “… educational materials can have a huge impact and effectively bring people into the community.”
- Quality documentation for OSS is often lacking due to:
	- decentralized development
	- documentation is not as glamorous or as praised as new features or major bug fixes
	- “Even when the community is welcoming, documentation is often seen as a "good first issue", meaning that the docs end up being written by the least experienced contributors in the community.”
- Possible solution: 
	- organize/re-organize docs into:
		- tutorials
		- how-tos
		- reference guide
		- explanations
	- consequences:
		- Improving on the quality and discoverability 
		- Clear difference between docs aimed at different users 
		- Give users more opportunities to contribute, generating content that can be shared directly on the official documentation
		- Building a documentation team as a first-class team in the project, which helps create an explicit role as *documentation creator*. This helps people better identify how they can contribute beyond code.
		- Diversifying our contributor base, allowing people from different levels of expertise and different life experiences to contribute. This is also extremely important so that we have a better understanding of our community and can be accessible, unbiased and welcoming to all people.
- Referenced in article: ["What nobody tells you about documentation"](https://www.divio.com/blog/documentation)

**Michael #2:** [**The Django Speed Handbook: making a Django app faster**](https://openfolder.sh/django-faster-speed-tutorial)

- By [Shibel Mansour](https://twitter.com/SHxKM)
- Speed of your app is very important: 100ms is an eternity. SEO, user conversions, bounce rates, etc.
- Use the tried-and-true `[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)`. 
	- Analyze your request/response cycles and see where most of the time is spent. 
	- Provides database query execution times and provides a nice SQL `EXPLAIN` in a separate pane that appears in the browser.
- **ORM/Database:** Two ORM functionalities I want to mention first: these are `select_related` and `prefetch_related`. Nice 24x perf improvement example  in the article. Basically, beware of the N+1 problem.
- **Indexes:** Be sure to add them but they *slow* writes.
- **Pagination:** Use it if you have lots of data
- **Async / background tasks**.
- **Content size:** Shrunk 9x by adding gzip middleware
- **Static files:** minify and bundle as you can, cache, serve through nginx, etc.
	- At Python Bytes, Talk Python, etc, we use `webassets`, `cssmin`, and `jsmin`.
- **PageSpeed** from Google, [**talk python’s ranking**](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Ftraining.talkpython.fm%2F&tab=desktop).
- **ImageOptim** (for [macOS](https://imageoptim.com/mac), [others](https://imageoptim.com/versions))
- **Lazy-loading images:** Lazily loading images means that we only request them when or a little before they enter the client’s (user’s) viewport. With excellent, dependency-free JavaScript libraries like [LazyLoad](https://github.com/verlok/lazyload), there really isn’t an excuse to not lazy-load images. Moreover, Google Chrome natively supports the `lazy` attribute.
- Remember: Test and measure everything, before and after.

**Brian #3:** ****[**dacite: simplifies creation of data classes from dictionaries**](https://github.com/konradhalas/dacite)

- Konrad Hałas
- dataclasses are awesome
	- quick and easy
	- fields can
		- have default values
		- be excluded from comparison and/or repr and more
- data often gets to us in dictionaries
- Converting from dict to dataclass is trivial for trivial cases: `x = MyClass(**data_as_dict)`
- For more complicated conversions, you need `dacite`
- `dacite.from_dict` supports:
	- nested structures
	- optional fields and unions
	- collections
	- type_hooks, which allow you to have custom converters for certain types
- strict mode. Normally allows extra input data that is just ignored if it doesn’t match up with fields. But you can use strict to not allow that.
- Raises exceptions when something weird happens, like the wrong type, missing values, etc.

**Michael #4:** [**How we retired Python 2 and improved developer happiness**](https://engineering.linkedin.com/blog/2020/how-we-retired-python-2-and-improved-developer-happiness)

- By [Barry Warsaw](https://engineering.linkedin.com/blog/authors/b/barry-warsaw)
- [The Python Clock](https://pythonclock.org/) is at 0:00.
- In 2018, LinkedIn embarked on a multi-quarter effort to fully transition to a Python 3 code base.
- In total, the effort entailed the migration of about 550 code repositories.
- They don't use Python in our product or as a monolithic web service, and instead have hundreds of independent microservices and tools, and dozens of supporting libraries, all owned by independent teams in separate repositories.
- In the early days, most of internal libraries were ported to be “[bilingual](https://docs.python.org/3/howto/pyporting.html),” meaning they could be used in either Python 2 or 3.
- Given that the migration affected all of LinkedIn engineering across so many disparate teams and thousands of engineers, the effort was overseen by our Horizontal Initiatives (HI) program.
- **Phase 1:** In the first quarter of 2019, we performed detailed dependency graphing, identifying a number of repositories that were more foundational, and thus needed to be fully ported first because they blocked the ports of everything that depended on them.
- **Phase 2:** In the second quarter of 2019, we identified the remainder of repositories that needed porting
- **Post-migration reflections**: Our primary indicator for completing the migration of a multiproduct was that it built successfully and passed its unit and integration tests.
- For other organizations planning or in the midst of their own migration paths, we offer the following guidelines:
	- Plan early, and engage your organization’s Python experts. Find and leverage champions in your affected teams, and promote the benefits of Python 3.
	- Adopt the bilingual approach to supporting libraries so that consumers of your libraries can port to Python 3 on their own schedules.
	- Invest in tests and code coverage—these will be your best success metrics.
	- Ensure that your data models are explicit and clear, especially in identifying which data are bytes and which are human-readable text.
- Benefits: 
	- No longer have to worry about supporting Python 2 and have seen our support loads decrease. 
	- Can now depend on the latest open source libraries and tools, and free from the constrictions of having to write bilingual Python. 
	- Opportunistically and enthusiastically adopting type hinting and the [mypy](https://mypy.readthedocs.io/en/latest/) type checker, improving the overall quality, craft, and readability of Python code bases. 

**Brian #5:** [**The Troublesome Active Record Pattern**](http://calpaterson.com/activerecord.html)

- Cal Paterson
- "Object relational mappers" (ORMs) exist to bridge the gap between the programmers' friend (the object), and the database's primitive (the relation). 
- Examples include Django ORM and SQLAlchemy
- The Active Record pattern of data access is marked by:
	1. A whole-object basis
	2. Access by key (mostly primary key)
- Problem: Queries that don’t need all information for objects retrieve it all anyway, and it’s easy to code for loops to select or collect info that are wildly inefficient.
	- how many books are there
	- how many books about software testing written by Oregon authors
- Problem: transactions. people can forget to use transactions, some ORMs don’t support them, they are not taught in beginner tutorials, etc.
	- SQLAlchemy has sessions
	- Django has `atomic()`
- REST APIs can suffer the same problems.
- Solutions:
	- just use SQL
	- first class queries
	- first class transactions
	- avoid Active Record style access patterns 
	- Be careful with REST APIs
		- Alternatives:
			- GraphQL
			- RPC-style APIs

**Michael #6:** [**Types at the edges in Python**](https://blog.meadsteve.dev/programming/2020/02/10/types-at-the-edges-in-python/)

- By Steve Brazier
- For a new web service in python there are 3 things to start with:
	- [Pydantic](https://pydantic-docs.helpmanual.io/)
	- [mypy](http://mypy-lang.org/)
	- Production error tracking of some kind
- Why: Because what is this about? `AttributeError: 'NoneType' object has no attribute 'strip'` It should be: `none is not an allowed value (type=type_error.none.not_allowed)`
- We then launch this code into production and our assumptions are tested against reality. If we’re lucky our assumptions turn out to be correct. If not we likely encounter some cryptic `NoneType` errors like the one at the start of this post.
- Pydantic can help by formalizing our assumptions.
- **mypy carries on helping**: Once you see the error at the start of this post (thanks error reporting) you know what is wrong about assumptions. Make the following change to your code: `field: typing.Optional[str]`
- BTW: FastAPI integrates with Pydantic out of the box.
- A mini-kata like exercise here that can be worked through: [meadsteve/types-at-the-edges-minikata](https://github.com/meadsteve/types-at-the-edges-minikata)

Extras:

Michael:

- [**Python Bytes Awesome Package List**](https://jackmckew.dev/python-bytes-awesome-package-list.html) by Jack Mckew
- [**Visual Basic Will Stall Out With .NET 5**](https://flip.it/dp9cxY)
- [**COVID 19 data sets**](https://twitter.com/b33k33p/status/1240022365125443584)
- New course in dev: **Adding a CMS to Your Data-Driven Web App** [in Pyramid|Flask]

Joke:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e5ff59ebac11305019c191c/73ba3e752f0d132242e626d8ffc53cf2/docs.jpg)

[https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e5ff59ebac11305019c191c/73ba3e752f0d132242e626d8ffc53cf2/docs.jpg](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e5ff59ebac11305019c191c/73ba3e752f0d132242e626d8ffc53cf2/docs.jpg)
