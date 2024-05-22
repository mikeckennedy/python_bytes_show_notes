# Python Bytes 12
This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 12, recorded on February 6th, 2017. In this episode we discuss expanding your Python mental model and serving millions of requests per second with Python. [more]

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

**BO 1:  A couple of mental model articles**

- **Python Functions aren’t what you think.**
  - http://powerfulpython.com/blog/python-functions-arent-what-you-think/
  - Functions are objects. The name of a function is just a variable name referring to the object.
- **The Tao of Python**
  - http://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/tao_mro/tao_of_python.ipynb
  - Jupiter notebook discussion of the relationship between objects, classes, and metaclasses.

**Michael #2:** [**Why Learn Python? Here Are 8 Data-Driven Reasons**](https://dbader.org/blog/why-learn-python) **by Dan Bader**

- Is Python worth learning? We’ve interviewed experts and surveyed the job market to identify the key reasons why you should learn Python today.
- Python is also one of the hottest skills to have according to [research by Dice](http://insights.dice.com/2016/02/01/whats-hot-and-not-in-tech-skills/)
- The 2nd most popular programming language in the world based on the [PYPL Popularity of Programming Language Index](http://pypl.github.io/PYPL.html).
  - 1. You Can Use Python for Pretty Much Anything
  - 2. Python Is Widely Used in Data Science
  - 3. Python Pays Well: Indeed’s salary calculator gives an even larger figure—a whopping $116,000 per year. (second only to ruby according to gooroo but has 3 times the job openings)
  - 4. Demand for Python Developers Is High (And Growing)
  - 5. Python Saves Time
  - 6. Python Is Beginner Friendly
  - 7. All the Big Names Use Python
    - Python could be your way into major tech companies: YouTube, IBM, Yahoo, Dropbox, Quora, Mozilla, Instagram, and many others 
  - 8. Python Has an Amazing Ecosystem
  - Segments from: Michael Kennedy, Ankur Gupta (Curator at ImportPython), and Sebastian Vetter (Python Engineer at Eventbase)

**B****rian #****3:** [**Testing Python Applications with Pytest - Kevin Ndung’u**](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)
How could I resist? Do a decent job explaining something about pytest, and I’m happy. 
What I liked:

- good really fast intro to pytest extreme basics
- Refactoring test code with fixtures. Pulling out common starting state into a fixture.
- Paramterizing tests to send multiple data sets into the same test function
- Using both fixtures and paratmerization in the same test function

There’s so much power and functionality in pytest. But just starting to use it as a better test framework for Python is a good thing. This article is a good kick in the pants for someone new to pytest. Easy intro, plus a couple of cool goodies.


**Michael #4:** [**A million requests per second with Python**](https://medium.freecodecamp.com/million-requests-per-second-with-python-95c137af319#.ju1j76oli)

- Screaming-fast Python 3.5+ web micro-framework integrated with pipelining HTTP server based on uvloop and picohttpparser.
- We spoke about sanic recently. Apparently this is much faster.
- https://github.com/squeaky-pl/japronto 2.6k stars
- Is it possible to hit a million requests per second with Python? Probably not until recently.
- Covers perf improvements found in 3.6 and coming in 3.7.
- It lets you do both synchronous and asynchronous programming thanks to asyncio. And it’s shamelessly fast. Even faster than NodeJS and Go.
- Japronto tries hard to delay creation of Python counterparts of its internal structures until asked explicitly. For example, a headers dictionary won’t be created until it’s requested in a view.

**Brian#5:** [**RethinkDB is alive and well**](https://rethinkdb.com/blog/rethinkdb-joins-linux-foundation/)

- RethinkDB joins The Linux Foundation
  - https://rethinkdb.com/blog/rethinkdb-joins-linux-foundation/
- The liberation of RethinkDB
  - https://www.joyent.com/blog/the-liberation-of-rethinkdb
- Company behind RethinkDB shut down Sept 2016
- Announced today that Cloud Native Computing Foundation purchased the rights to source code and contributed it to the Linux Foundation under Apache license ASLv2.
- Website, GitHub org, social media accounts will continue to operate.
- They can take donations, and stripe has ponied up 25k in donation matching.



**Michael #6:** [**Python Top 10 Articles for the Past Year (v.2017)**](https://medium.mybridge.co/python-top-10-articles-for-the-past-year-v-2017-6033ae8c65c9#.mhn051vv5)

1. The Hitchhiker’s Guide to Python: Best practices guidebook written for Humans.
2. Scipy Lecture Notes — Learn numerics, science, and data with Python.
3. 30 Essential Python Tips and Tricks for Programmers.
4. Computational and Inferential Thinking for Data Science. Courtesy of UC Berkeley
5. Welcome to Python cheatsheet.
6. Data Mining in Python: A Guide.
7. Python FAQ: Why should I use Python 3? (by eevee)
8. An Introduction to Stock Market Data Analysis with Python
9. NumPy Tutorial: Data analysis with Python.
10. Build Your First Python and Django Application

**Michael: Follow up on RHL:** [**Red Hat Software Collections**](https://developers.redhat.com/products/softwarecollections/hello-world/)
Thank you [Chip Warden](http://disq.us/p/1fua8rv)

- The latest, stable updates of development technologies for Red Hat Enterprise Linux
- Add latest for:
  - Node 
  - Perl 
  - PHP 
  - Python [YES! Python 3]
  - Ruby


