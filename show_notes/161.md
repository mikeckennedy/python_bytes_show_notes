# Python Bytes 161
Sponsored by **DigitalOcean**: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

Special guest: [**Anthony Herbert**](https://twitter.com/pretty_printed)

**Anthony #1:** [**Larry Hastings - Solve Your Problem With Sloppy Python - PyCon 2018**](https://www.youtube.com/watch?v=Jd8ulMb6_ls)

- Michael’s personal automation things that I do all the time
	- stripe to sheets automation
	- [urlify](https://gist.github.com/mikeckennedy/3358f0908a39ae4872e9985b4f582aed)
	- tons of reporting
	- [wakeup](https://github.com/mikeckennedy/wakeup) - to get 100 on Lighthouse
	- deploy (on my servers)
	- creating import data for video courses
	- measuring duration of audio files

**Michael #2:** [**Introduction to ASGI: Emergence of an Async Python Web Ecosystem**](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/)

- by Florimond Manca 
- Python growth is not just data science
- Python web development is back with an async spin, and it's exciting. 
- One of the main drivers of this endeavour is [ASGI](https://asgi.readthedocs.io/en/latest/) , the Asynchronous Standard Gateway Interface.
- A guided tour about **what ASGI is** and **what it means for modern Python web development**.
- Since 3.5 was released, the community has been literally **async-ifying all the things**. If you're curious, a lot of the resulting projects are now listed in [aio-libs](https://github.com/aio-libs) and [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) .
- An overview of ASGI
- Why should I care? Interoperability is a strong selling point, there are many more advantages to using ASGI-based components for building Python web apps.
	- **Speed**: the async nature of ASGI apps and servers make them really fast (for Python, at least) — we're talking about 60k-70k req/s (consider that Flask and Django only achieve 10-20k in a similar situation).
	- **Features**: ASGI servers and frameworks gives you access to inherently concurrent features (WebSocket, Server-Sent Events, HTTP/2) that are impossible to implement using sync/WSGI.
	- **Stability**: ASGI as a spec has been around for about 3 years now, and version 3.0 is considered very stable. Foundational parts of the ecosystem are stabilizing as a result.
- To get your hands dirty, try out any of the following projects:
	- [uvicorn](https://www.uvicorn.org/): ASGI server.
	- [Starlette](https://www.starlette.io/): ASGI framework.
	- [TypeSystem](https://www.encode.io/typesystem/): data validation and form rendering
	- [Databases](https://www.encode.io/databases/): async database library.
	- [orm](https://github.com/encode/orm): asynchronous ORM.
	- [HTTPX](https://www.encode.io/httpx/): async HTTP client w/ support for calling ASGI apps (useful as a test client).

**Anthony #3:** ****[**Python Insights**](https://www.pythoninsight.com/)

**Michael #4:** [**Assembly**](https://github.com/mardix/assembly)

- via Luiz Honda
- Assembly is a Pythonic Object-Oriented Web Framework built on Flask, that groups your routes by class
- Assembly is a pythonic object-oriented, mid stack, batteries included framework built on Flask, that **adds structure to your Flask application, and group your routes by class**.
- Assembly **allows you to build web applications in much the same way you would build any other object-oriented Python program**.
- Assembly **helps you create small to enterprise level applications easily**.
- Decisions made for you + features: [**github.com/mardix/assembly#decisions-made-for-you--features**](https://github.com/mardix/assembly#decisions-made-for-you--features)

Examples, root URLs:

```
    # Extends to Assembly makes it a route automatically
    # By default, Index will be the root url
    class Index(Assembly):
    
        # index is the entry route
        # -> /
        def index(self):
            return "welcome to my site"
    
        # method name becomes the route
        # -> /hello/
        def hello(self):
            return "I am a string"
    
        # undescore method name will be dasherize
        # -> /about-us/
        def about_us(self):
            return "I am a string"
```

Example of **/blog**.

```
    # The class name is part of the url prefix
    # This will become -> /blog
    class Blog(Assembly):
        
        # index will be the root 
        # -> /blog/
        def index(self):
            return [
                {
                    "title": "title 1",
                    "content": "content"
                },
                ...
            ]
    
        # with params. The order will be respected
        # -> /comments/1234/
        # 1234 will be passed to the id
        def comments(self, id):
            return [
                {
                    comments...
                }
            ]
```

**Anthony #5:** [**Building a Standalone GPS Logger with CircuitPython using @Adafruit and particle hardware**](http://www.movingelectrons.net/blog/2019/04/03/Building-a-GPS-Logger-with-CircuitPython.html)

**Michael #6:** [**10 reasons python is good to learn**](https://dev.to/duomly/10-reasons-why-learning-python-is-still-a-great-idea-5abh)

- Python is popular and good to learn because, in Michael’s words, it’s a full spectrum language.
- And the reasons are:
1. Python Is Free and Open-Source
2. Python Is Popular, Loved, and Wanted
3. Python Has a Friendly and Devoted Community
4. Python Has Elegant and Concise Syntax
5. Python Is Multi-Platform
6. Python Supports Multiple Programming Paradigms
7. Python Offers Useful Built-In Libraries
8. Python Has Many Third-Party Packages
9. Python Is a General-Purpose Programming Language
10. Python Plays Nice with Others

Extras:

Michael:

- I was just on [**.NET Rocks podcast**](https://dotnetrocks.com/?show=1665) talking about Python for the .NET Developer
- New [**Python for the .NET Developer**](https://training.talkpython.fm/courses/explore_dotnet/python-for-dotnet-developers) 9-hour course
- New [**Python for Decision Makers course**](https://training.talkpython.fm/courses/explore_decision/python-for-decision-makers-and-business-leaders), 2.5 hours of exploring Python for your org.
- Hidden files in Finder: use shortcut `cmd+shift+.`

Anthony:

- [**Pretty Printed**](https://prettyprinted.com/)
- [**YouTube channel**](https://www.youtube.com/c/prettyprintedtutorials)

Joke: **The failed pickup line**

- A girl is hanging out at a bar with her friends. 
- Some guy comes up to her an says: “You are the ; to my line of code.”
- She responds, “Get outta here creep, I code in Python.”
