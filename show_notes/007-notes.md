# Python Bytes Episode 7

This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 7, recorded on Wednesday, January 4th. 

In this episode we discuss Python 3.6 being release, a blazing Python web framework called Sanic, how we are failing our open source infrastructure, and more. [more]

This episode was brought to you by [Rollbar: they help you take the pain out of errors](http://rollbar.com/pythonbytes).

**#1 (Brian)**:  **Python 3.6 is officially released**

- Dec 23 Announcement on blog.python.org: [http://blog.python.org/2016/12/python-360-is-now-available.html](http://blog.python.org/2016/12/python-360-is-now-available.html)
- What’s new article on docs.python.org: [https://docs.python.org/3.6/whatsnew/3.6.html](https://docs.python.org/3.6/whatsnew/3.6.html)

Here’s a few more articles:

- Python 3.6 is packed with goodness - Serdar Yegulalp -  InfoWorld
  - [http://www.infoworld.com/article/3149782/application-development/python-36-is-packed-with-goodness.html](http://www.infoworld.com/article/3149782/application-development/python-36-is-packed-with-goodness.html)
  - A list of cool things in Python 3.6
    - async/await in more places
    - Improved memory usage and speed
    - frame evaluation API to provide better support for JITs, tracers, debuggers
    - secrets module for common security-related functions such as generating tokens
- One thing that could stop a team from switching to Python 3 would be that they looked into it once, and a package they needed was not ported yet. That’s different now, most are ported, or have been replaced with some other way.
- Adopt Python 3 - Dibya Chakravorty - on Medium
  - [https://medium.com/broken-window/python-3-support-for-third-party-libraries-dcd7a156e5bd](https://medium.com/broken-window/python-3-support-for-third-party-libraries-dcd7a156e5bd) 
  - A discussion of packages that support Python 2 and 3, those that are 2 only, those that are 3 only.
  - Two lists of most downloaded packages and their py3 readiness:
    - Wall of superpowers: [http://python3wos.appspot.com/](http://python3wos.appspot.com/), 187/200 = 93.5%
    - Python 3 readiness: [http://py3readiness.org/](http://py3readiness.org/), 341/360 = 94.7%
  - Go further:
    - all pypi packages that are stable and active (at least one release in 2016), about 6000 packages
    - total python 3 coverage is 72%
    - 14% are Python 3 only
    - 28% are Python 2 only
    - of the 28%, author estimates only 25% of the remaining packages would be difficult to port, based on their size, and included that list.
    - Also entire code for this article is in an iPython notebook:[https://github.com/gutfeeling/pypi_explorer/blob/master/pypi_database/analysis.ipynb](https://github.com/gutfeeling/pypi_explorer/blob/master/pypi_database/analysis.ipynb)

**#2 (Michael)**
**Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure by Nadia Eghbal**
[http://www.fordfoundation.org/library/reports-and-studies/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure](http://www.fordfoundation.org/library/reports-and-studies/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure)

- From The Ford Foundation, 14 JULY 2016
- Features Eric Holscher from Read the Docs & Donald Stufft from PyPI
- Discussed on Talk Python episode [#84: Are we failing to fund Python's core infrastructure?](https://talkpython.fm/episodes/show/84/are-we-failing-to-fund-python-s-core-infrastructure)
- Some highlights from the 149 page report:
  - Our modern society—everything  from hospitals to stock markets to  newspapers to social media—runs on  software. But take a closer look, and  you’ll find that the tools we use to build  software are buckling under demand. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.4)
  - No individual company or organization is incentivized to address the  problem alone, because open source code is a public good. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.9)
  - By 2014, two-thirds of all Web servers were using OpenSSL, enabling  websites to securely pass credit card and other sensitive information  over the Internet. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.11)
  - Institutional efforts to support digital  infrastructure: There are some institutional efforts to collectively organize and help  support open source projects. Some are independent software  foundations; other sources of support come from software companies themselves. Administrative support and fiscal sponsorship Several foundations provide organizational support, such as fiscal  sponsorship, to open source projects: in other words, taking care of  the non-coding tasks that many developers would prefer not to do (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.109)
  - Of Heartbleed, Marquess wrote, “The mystery is not that a few over-worked volunteers missed this bug; the mystery is why it hasn’t  happened more often.” (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.13)
  - Heartbleed, had been included in a 2011  update. It had gone unnoticed for years. Heartbleed could allow any  sophisticated hacker to capture secure information being passed to  vulnerable web servers, including passwords, credit card information,  and other sensitive data (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.13)
  - People expressed their support by sending donations to the foundation. Although Marquess was grateful for their enthusiasm, the first  round of donations came out to roughly $9,000: not nearly enough  to sustain a team. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.13)
  - After Heartbleed, OpenSSL finally got more of the funding it  needed—at least for now. They currently have enough money to pay  four full-time employees for three years. But a year and a half into  that funding, Marquess isn’t sure what will come next. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.14)
  - Free software makes it exponentially cheaper  and easier to build software (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.23)
  - Free software is directly responsible for  today’s current startup renaissance (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.24)
  - Software not getting the necessary  maintenance it needs Building digital infrastructure in a haphazard fashion means that all  software gets built more slowly and inefficiently. One example of  this can be found in the history of Python infrastructure. An important infrastructure project for Python developers is called setuptools. (roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure, p.80)

**#3 (Brian)**: **Matplotlib 2.0.0 rc2 was released by Thomas Caswell**
- install instructions: [http://matplotlib.org/style_changes.html](http://matplotlib.org/style_changes.html)
- List of top level changes in release history on github
-[https://github.com/matplotlib/matplotlib/releases](https://github.com/matplotlib/matplotlib/releases)
- Changes to the default style - matplotlib.org
- [http://matplotlib.org/2.0.0rc2/users/dflt_style_changes.html](http://matplotlib.org/2.0.0rc2/users/dflt_style_changes.html)
- Post visually shows all of the new changes. 
- What’s new in matplotlib 2.0 - also on [http://matplotlib.org](matplotlib.org)
- [http://matplotlib.org/2.0.0rc2/users/whats_new.html](http://matplotlib.org/2.0.0rc2/users/whats_new.html)

**#4 (Michael)**
**Introduction to MongoDB and Python**
[https://realpython.com/blog/python/introduction-to-mongodb-and-python/](https://realpython.com/blog/python/introduction-to-mongodb-and-python/)

- SQL vs NoSQL
- PyMongo
  - Inserting and querying data
- MongoEngine
  - Classes
  - Constraints 
  - OOP
- Michael’s 1.5 hour presentation at Software Architect conference in London: [Applied NoSQL with MongoDB and Python](https://www.youtube.com/watch?v=_r7ozqiTN2k)

**#5: (Brian)**: **Introducing Maya: Datetimes for Humans**
[https://www.kennethreitz.org/essays/introducing-maya-datetimes-for-humans](https://www.kennethreitz.org/essays/introducing-maya-datetimes-for-humans)
- Working with dates is harder than it should be. Kenneth has proven that he understands how to make reasonable interfaces to hide complicated things.

From "why is this useful?" section

- All timezone algebra will behave identically on all machines, *regardless of system locale*.
- Complete symmetric import and export of both **ISO 8601** and **RFC 2822** datetime stamps.
- Fantastic parsing of both dates written for/by humans and machines (**maya.when()** *vs.* **maya.parse()**).
- Support for human slang, both import and export (e.g. 'an hour ago').
- Datetimes can very easily be generated, with our without timezone information attached (naive).
- This library is based around epoch time, but dates before Jan 1 1970 are indeed supported, via negative integers.

**#6 (Michael)**: **Sanic: Python 3.5+ web server that's written to go fast**
[https://github.com/channelcat/sanic](https://github.com/channelcat/sanic)

- Sanic is a Flask-like Python 3.5+ web server that's written to go fast. It's based on the work done by the amazing folks at magicstack, and was inspired by this article: [https://magic.io/blog/uvloop-blazing-fast-python-networking/](https://magic.io/blog/uvloop-blazing-fast-python-networking/).
- On top of being Flask-like, Sanic supports async request handlers. This means you can use the new shiny async/await syntax from Python 3.5, making your code non-blocking and speedy.

A basic action method

    @app.route("/")
    async def test(request):  # async def !!!
        return json({ "hello": "world" })

- Performance numbers:
    - | Server  | Implementation      | Requests/sec | Avg Latency |
    - | Sanic   | Python 3.5 + uvloop |       33,342 |      2.96ms |
    - | Bottle  | gunicorn + meinheld |       13,596 |      7.36ms |
    - | Flask   | gunicorn + meinheld |        4,988 |     20.08ms |
    - | Aiohttp | Python 3.5 + uvloop |        2,979 |     33.42ms |
    - | Tornado | Python 3.5          |        2,138 |     46.66ms |