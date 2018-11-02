# Python Bytes 102
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**QuantEcon**](https://quantecon.org/)

- “Open source code for economic modeling”
- “QuantEcon is a [NumFOCUS](http://www.numfocus.org/) fiscally sponsored project dedicated to development and documentation of modern open source computational tools for economics, econometrics, and decision making.”
- Educational resource that includes:
  - Lectures, workshops, and seminars
  - Cheatsheets for scientific programming in Python and Julia
  - Notebooks
  - QuantEcon.py : open source Python code library for economics

**Michael** **#****2****:** ****[**Structure of a Flask Project**](https://lepture.com/en/2018/structure-of-a-flask-project)

- Flask is very flexible, it has no certain pattern of a project folder structure. Here are some suggestions.
- I always keep this one certain rule when writing modules and packages:
  - “Don't backward import from root __init__.py.”
- Candidate structure:


    project/
      __init__.py
      models/
        __init__.py
        users.py
        posts.py
        ...
      routes/
        __init__.py
        home.py
        account.py
        dashboard.py
        ...
      templates/
        base.html
        post.html
        ...
      services/
        __init__.py
        google.py
        mail.py


- Love it! To this, I would rename `routes` to `views` or `controllers` and add a `viewmodels` folder and viewmodels themselves.
- Brian, see anything missing? 
  - ya. tests. :)
- Another famous folder structure is app based structure, which means things are grouped bp application
- I (Michael) STRONGLY recommend [**Flask blueprints**](http://flask.pocoo.org/docs/1.0/blueprints/)

**Brian** **#****3****:** [**Overusing lambda expressions in Python**](https://treyhunner.com/2018/09/stop-writing-lambda-expressions/)
[](https://treyhunner.com/2018/09/stop-writing-lambda-expressions/)
- lambda expressions vs defined functions
  1. They can be immediately passed around (no variable needed)
  2. They can only have a single line of code within them
  3. They return automatically
  4. They can’t have a docstring and they don’t have a name
  5. They use a different and unfamiliar syntax
- misuses: 
  - naming them. Just write a function instead
  - calling a single function with a single argument : just use that func instead
- overuse:
  - if they get complex, even a little bit, they are hard to read
  - has to be all on one line, which reduces readibility
  - map and filter : use comprehensions instead
  - using custom lambdas instead of using operators from the [operator module](https://docs.python.org/3/library/operator.html). 

**SPONSOR -** **DO**
**Bring Your Custom Image to DigitalOcean** 
With their new Custom Image feature, you can benefit from the scale of DigitalOcean while using your own custom environment. 
Pricing: Importing custom images is free, as you are only charged for the storage of your image at $0.05/GB per month.
After logging into cloud.digitalocean.com, you can click on Images on the left of the screen and then click on “Custom Images” 
Shortly after You can start a Droplet directly from the Custom Images
Visit https://pythonbytes.fm/digitalocean to get started.

**Michael #****4****:** ****[**Asyncio in Python 3.7**](https://tryexceptpass.org/article/asyncio-in-37/)

- by Cris Medina
- The release of Python 3.7 introduced a number of changes into the async world. 
  - Some may even affect you even if you don’t use asyncio.
- New Reserved Keywords: The async and await keywords are now reserved.
  - There’s already quite a few modules broken because of this. However, the fix is easy: rename any variables and parameters.
- Context Variables: Version 3.7 now allows the use of context variables within async tasks. If this is a new concept to you, it might be easier to picture it as global variables whose values are local to the currently running coroutines.
- Python has similar constructs for doing this very thing across threads. However, those were not sufficient in async-world
- New `asyncio.run()` function
  - With a call to `asyncio.run()`, we can now automatically create a loop, run a task on it, and close it when complete.
- Simpler Task Management: Along the same lines, there’s a new asyncio.create_task() function that helps make tasks that inside the current loop, instead of having to get the loop first and calling create task on top of it.
- Simpler Event Loop Management: The addition of asyncio.get_running_loop() will help determine the active event loop, and catch a RuntimeError if there’s no loop running. 
- Async Context Managers: Another quality-of-life improvement. We now have the asynccontextmanager() decorator for producing async context managers without the need for a class that implements __aenter__() or __aexit__(). 
- Performance Improvements: Several functions are now optimized for speed, some were even reimplemented in C. Here’s the list:
  -     asyncio.get_event_loop() is now 15 times faster.
  -     asyncio.gather() is 15% faster.
  -     asyncio.sleep() is two times faster when the delay is zero or negative.
  -     asyncio.Future callback management is optimized.
  -     Reduced overhead for asyncio debug mode.
- Lots lots more

**Brian** **#5****: Giving thanks with** `**pip thank**`

- proposal: https://github.com/pypa/pip/issues/5970

**Michael #6:** [**Getting Started With Testing in Python**](https://realpython.com/python-testing/)

- by Anthony Shaw, 33 minutes reading time according to Instapaper
- Automated vs. Manual Testing
- Unit Tests vs. Integration Tests: A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.
- Compares unittest,  nose or nose2, pytest
- Covers things like:
  - Writing Your First Test
  - Where to Write the Test
  - How to Structure a Simple Test
  - How to Write Assertions
  - Dangers of Side Effects
- Testing in PyCharm and VS Code
- Testing for Web Frameworks Like Django and Flask
- Advanced Testing Scenarios
- Even: Testing for Security Flaws in Your Application

**Extra****s****:** 

- Brian: 
- M**K:** [**Hack ur name**](http://hackurname.com/) — aka Pivot me bro (done in Python: https://github.com/veekaybee/hustlr ) by Vicki Boykis
- MK: [Python 3.7.1 and 3.6.7 Are Now Available](https://blog.python.org/2018/10/python-371-and-367-are-now-available.html)
- MK: Click-Driven Development (CDD) - via @[tombaker](https://twitter.com/tombaker)
  - Use Python Click package to mock up suite of commands w/options/args. 
  - Decorated functions print description of intended results. 
  - Replace placeholders with code.


