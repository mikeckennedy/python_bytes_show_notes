# Python Bytes 14

**Brian #1:** [**Tiny Python 3.6 Notebook - Matt Harrison**](https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/README.md)

- README : [https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/README.md](https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/README.md)
- Full Book on GitHub : [https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/python.rst](https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/python.rst)
- “This is not so much an instructional manual, but rather notes, tables, and examples for Python syntax.”
- Physical book is 134 pages, but looks like about 90 pages of content. 

**Michael #2:** [**Oh no! This package is Python 2 only - Anthony Shaw**](https://medium.com/@anthonypjshaw/oh-no-this-package-is-python-2-only-8e6316f9a02#.xrquwdh51)

- You’re head down, working on a new project and one of your dependencies still doesn’t support Python 3 - argh! Here’s a quick guide on how to solve that problem, step by step.
- Step 0: Check that nobody else has solved this
- Step 1: Fork it
- Step 2: Print statements
- Step 3: Tests
  - Static Analysis: modernize
- Step 4: Update setup.py
- Step 5: Install it into your original project
- Step 6: Raise a pull request
- Step 7: 3 months later?

**Brian #3:** [**Elements of Python Style**](https://github.com/amontalenti/elements-of-python-style) **- Andrew Montalenti**

- More than PEP8, and opinionated. 
- I admire the effort, and I may at some point fork it to remove/fix the few things I disagree with and to be able to use it as a style guide for my team.
- Great: most of it. 
  - Use parens for continuation
  - Use with for files and locks
- May need tweaking
  - Avoid custom exceptions
    - I’d prefer, “Add one custom base exception, and build specific exceptions off of that”. 
    - This may be a controversial point, or I may be just confused about conventional practice here
  - As with any style guide, more detail brings more controversy. 
- Michael: I like this guidance: You can also choose to use CamelCase for things that are class-like but not quite classes -- the main benefit of CamelCase is calling attention to something as a "global noun", rather than a local label or a verb. Notice that Python names True, False, and None use CamelCase even though they are not classes.
    

**Michael #4:** [**Python 3 was exactly 3000 days old this past Sunday**](https://www.reddit.com/r/Python/comments/5v0tt6/python_3_created_via_pep_3000_is_exactly_3000/)

- Reddit post about my tweet (wow)
  - 537 upvotes, 71 comments
- Test it yourself:
  background = 
      “Python 3 was released December 3, 2008 ” + \
      “Its original working name was Python 3000”
  release = datetime.date(year=2008, month=12, day=3)
  today = datetime.date(year=2017, month=2, day=19)
  (today - release).days # → 3000
- Via @cclauss Christian Clauss

Brian #5:
**From beginner to pro:** [**Python books, videos and resources**](http://pybit.es/python-resources.html)
[](http://pybit.es/python-resources.html)
- Bob Belderbos and Julian Sequeira
- Reddit thread: [https://redd.it/5sjt3l](https://redd.it/5sjt3l)
- Post: [http://pybit.es/python-resources.html](http://pybit.es/python-resources.html)
- “a list of useful Python resources to boost up your skills”
- Some very nice podcasts listed in “other resources”

**Michael #6:** [**mongoaudit**](https://github.com/stampery/mongoaudit)

- mongoaudit is a CLI tool for auditing MongoDB servers, detecting poor security settings and performing automated penetration testing.
- pip install mongoaudit
- Tests things like:
  - MongoDB listens on a port different to default one
  - Server only accepts connections from whitelisted hosts / networks
  - MongoDB HTTP status interface is not accessible on port 28017
  - MongoDB is not exposing its version number
  - MongoDB version is newer than 2.4
  - TLS/SSL encryption is enabled
  - Authentication is enabled
  - SCRAM-SHA-1 authentication method is enabled
  - Server-side Javascript is forbidden
  - Roles granted to the user only permit CRUD operations
  - The user has permissions over a single database
  - Various security vulnerabilities 
- From Michael: MongoDB is awesome. But please make sure at least one of the following is true.
  - You only listen on local loopback (127.0.0.1) and run mongo on the web server
  - You run mongodb with authentication enabled (it’s off by default)
  - You run mongodb with SSL enabled (may be off by default too)
  
What else? Launched my course at [https://bit.ly/python-rest-course](https://bit.ly/python-rest-course)