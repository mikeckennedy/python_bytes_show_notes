# Python Bytes 45
This episode is brought to you by Rollbar: [pythonbytes.fm/rollbar](http://pythonbytes.fm/rollbar)

**Brian #1:** [**pico**](http://pico.readthedocs.io/) 

- "a very small web application framework for Python" 
- Recommended by Ivan Pejić
- [lightning talk from EuroPython 2017](https://www.youtube.com/watch?v=wyhAzM6TIrw&feature=youtu.be&t=5h54m44s)
- This would be a good web framework for building internal services and tools that non-web developers need to interact with and modify.
- Very simple.
- Not REST, but not confusing either.

**Michael #2:** [**High Sierra ships, first major OS with machine learning built in?**](https://arstechnica.com/gadgets/2017/09/macos-10-13-high-sierra-the-ars-technica-review/8/#h5)

- September 26th [**macOS High Sierra**](https://www.apple.com/macos/high-sierra/) was released (yay)
- Mostly a foundational release with barely visible changes but awesome things like APFS replacing HFS+, etc.
- Comes with **CoreML**
  - Apple’s intent with the new CoreML framework is to package up prebuilt ML models and execution engines and make them possible for third-party apps to use. 
  - Developers can take a trained machine learning algorithm, package it up as an MLModel, and integrate it into their apps. 
  - Apple offers a few default machine learning models that developers can download and use too
- Rather than sharing your data with a central server, grouping it together with a lot of other people's data, and improving machine learning models that way, Apple stresses that everything CoreML does is happening on the device.
- On Macs that support Metal—generally, Macs from 2012 and later—CoreML uses a mix of CPU processing and GPGPU processing, depending on the task.
- Add on the fact that High Sierra has [**external GPU support**](https://arstechnica.com/gadgets/2017/09/macos-10-13-high-sierra-the-ars-technica-review/7/#h2) now and you have a sweet combo.

**Brian #3:** [**A guide to logging in Python**](https://opensource.com/article/17/9/python-logging)

- Simply put, the best logging introduction I've read so far.

**Michael #4:** [**Let me introduce: slots**](https://www.chrisbarra.xyz/posts/let-me-introduce-slots/)

- So what are slots? __slots__ are a different way to define the attributes storage for classes in Python.
- for normal Python classes, a dict is used to store the instance's attributes.
- With `__slots__` we don't have an attribute called `__dict__` inside our instance. But we have a new attribute called `__slots__`.
- But why would you need to use slots when you have a dict? Well the answer is that __slots__ are a lot lighter and slightly faster.
- Outcome:
  - ~57% less memory usage thanks to just one line of code.
  - __slots__ are also slightly faster.
- Covered in depth in my [Write Pythonic Code Like a Seasoned Developer](https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer) course.

**Brian #5:** [**pipenv revisited**](https://docs.pipenv.org/)

- Covered in [episode 11](https://pythonbytes.fm/). However, there are some notable changes since then.
- Reminder:
  - `pepenv` handles virtualenv and pip interaction for you
  - `pipenv install` creates a virtualenv (if one doesn't exist) and installs stuff into a virtualenv.
  - `pipenv shell` uses the virtualenv
  - `exit` allows you to get out of the virtualenv
  - `pipenv lock -r` will generate a requirements.txt file for you, so you can use it even if you need a requirements.txt file.
- Notable changes:
    - New [4 minute screencast](https://vimeo.com/233134524) with Kenneth demonstrating how to use it. Watching him use it makes it very simple to understand. 
    - Specify multiple package indexes, and even specify a particular index for particular packages. So you can combine both pypi with a company index and a group index and maybe one for your project.
    - pipenv check will tell you about any known security vulnerabilities in your installed packages
    - 9 months old with 192 releases, so keep an eye on it for new features all the time.

**Michael #6:** [**Stack Overflow gives an even closer look at developer salaries**](https://arstechnica.com/gadgets/2017/09/devops-and-data-science-are-the-big-software-dev-money-makers/)

-  Tabs and spaces aren't the only things that influence developer pay…
- Some of the broad trends are no big surprise; for example, the chosen cities tend to pay more than their respective nations do, for example.
- DevOps specialists and data scientists both earn well. 
- Other aspects of the data are a little more surprising. Graphics programmers, for example, aren't particularly well paid, in spite of having a relatively specialized, complex niche.
- And while earnings in four of the countries are surprisingly similar, those in America are substantially higher, regardless of experience; in fact, the median salary of a developer in the US is comparable to that of someone with 20 years of experience in Canada or Germany and markedly higher than 20-year veterans in France and the UK. Even after taking into account the US' higher healthcare costs, America is the place to be if you're a programmer.
- Comments
  - I do have to wonder how much Silicon Valley skews that salary chart, as the Web 2.0 companies pay HUGE comparatively [[ref](https://arstechnica.com/gadgets/2017/09/devops-and-data-science-are-the-big-software-dev-money-makers/?comments=1&post=34009615)]
  - I asked Stack Overflow's data scientist that question, and she said not much; even without its outlier cities, the US pays much more than the rest of the world. [[ref](https://arstechnica.com/gadgets/2017/09/devops-and-data-science-are-the-big-software-dev-money-makers/?comments=1&post=34009667)]
  - Healthcare cost are only part of it. I got paid about $600/month 9 months a year by my government to study in university. [[ref](https://arstechnica.com/gadgets/2017/09/devops-and-data-science-are-the-big-software-dev-money-makers/?comments=1&post=34009803)]
  - I feel like a lot of IT people lack soft skills, and it caps their salary at a lower end. [[ref](https://arstechnica.com/gadgets/2017/09/devops-and-data-science-are-the-big-software-dev-money-makers/?comments=1&post=34009925)]

Our news:

- Hardcopies of [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) now [shipping on Amazon](http://amzn.to/2fUZJxi), as well as [Pragmatic](https://pragprog.com/book/bopytest/python-testing-with-pytest).
  - When you get your copy, let me know. Send a pic to [@brianokken](https://twitter.com/brianokken)

