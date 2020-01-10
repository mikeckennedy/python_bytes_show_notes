# Python Bytes 163

Sponsored by us! Support us by visiting [**pythonbytes.fm/biz**](http://pythonbytes.fm/biz) [courses] and [**pythonbytes.fm/pytest**](https://pythonbytes.fm/pytest) [book], or becoming a patron at [patreon.com/pythonbytes](https://www.patreon.com/pythonbytes)

**Brian #1:** [**Meditations on the Zen of Python**](https://orbifold.xyz/zen-of-python.html)

- Moshe Zadka
- The Zen of Python is not "the rules of Python" or "guidelines of Python". It is full of contradiction and allusion. It is not intended to be *followed*: it is intended to be meditated upon.
- Moshe give some of his thoughts on the different lines of the Zen of Python.
- Full Zen of Python can be found [here](https://www.python.org/dev/peps/pep-0020/) or in a REPL with `import this`
- A few
	- Beautiful is better than ugly
		- Consistency helps. So black, flake8, pylint are useful.
		- “But even more important, only humans can judge what humans find beautiful. Code reviews and a collaborative approach to writing code are the only realistic way to build beautiful code. Listening to other people is an important skill in software development.”
	- Complex is better than complicated.
		- “When solving a hard problem, it is often the case that no simple solution will do. In that case, the most Pythonic strategy is to go "bottom-up." Build simple tools and combine them to solve the problem.”
	- Readability counts
		- “In the face of immense pressure to throw readability to the side and just "solve the problem," the Zen of Python reminds us: readability counts. Writing the code so it can be read is a form of compassion for yourself and others.”

**Michael #2: nginx raided by Russian police**

- [**Russian police have raided today the Moscow offices of NGINX, Inc**](https://www.zdnet.com/article/russian-police-raid-nginx-moscow-office/)., a subsidiary of F5 Networks and the company behind the internet's most popular web server technology.
- Russian search engine Rambler.ru claims full ownership of NGINX code.
- Rambler claims that Igor Sysoev developed NGINX while he was working as a system administrator for the company, hence they are the rightful owner of the project.
- Sysoev never denied creating NGINX while working at Rambler. In a 2012 interview, Sysoev claimed he developed NGINX in his free time and that Rambler wasn't even aware of it for years.
- **Update**
- Promptly following the event we took measures to ensure the security of our master software builds for NGINX, NGINX Plus, NGINX WAF and NGINX Unit—all of which are stored on servers outside of Russia. No other products are developed within Russia. F5 remains committed to innovating with NGINX, NGINX Plus, NGINX WAF and NGINX Unit, and we will continue to provide the best-in-class support you’ve come to expect.

**Brian #3:** [**I'm not feeling the async pressure**](https://lucumr.pocoo.org/2020/1/1/async-pressure/)

- Armin Ronacher
- “Async is all the rage.” But before you go there, make sure you understand flow control and back pressure.
- “…back pressure is resistance that opposes the flow of data through a system. Back pressure sounds quite negative … but it's here to save your day.”
- If parts of your system are async, you have to make sure the entire flow throw the system doesn’t have overflow points. 
- An example shown with reader/writer that is way hairier than you’d think it should be.
- “New Footguns: async/await is great but it encourages writing stuff that will behave catastrophically when overloaded.”
- “So for you developers of async libraries here is a new year's resolution for you: give back pressure and flow control the importance they deserve in documentation and API.”

**Michael #4:** [**codetiming from Real Python**](https://github.com/realpython/codetiming)

- via Doug Farrell 
- A flexible, customizable timer for your Python code
- For a complete tutorial on how `codetiming` works, see [Python Timer Functions: Three Ways to Monitor Your Code](https://realpython.com/python-timer) on [Real Python](https://realpython.com/).
- Time your code via
	- A timer class
	- A decorator
	- A context manager

**Brian #5:** [**Making Python Programs Blazingly Fast**](https://martinheinz.dev/blog/13)

- Martin Heinz
	- Seemed like a good followup to the last topic
- Profiling with
	- command line `time python something.py`
	- `python -m cProfile -s time something.py`
	- timing functions with wrapper
	- Misses `timeit`, but see that also, https://docs.python.org/3.8/library/timeit.html
- How to make things faster:
	- use built in types over custom types
	- caching/memoization with `lru_cache`
	- use local variables and local aliases when looping
	- use functions… (kinda duh, but sure).
	- don’t repeatedly access attributes in loops
	- use f-strings over other formatting
	- use generators. or at least experiment with them. 
		- the memory savings could result in speedup

**Michael #6:** [**LocalStack**](https://github.com/localstack/localstack)

- via Graham Williamson and Jan 'oglop' Gazda
- A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline!
- LocalStack spins up the following core Cloud APIs on your local machine:
	- S3, DynamoDB, Lambda, Elasticsearch
	- see [many more services](https://github.com/localstack/localstack#overview)
	- paid one has more
- LocalStack builds on existing best-of-breed mocking/testing tools, most notably [kinesalite](https://github.com/mhart/kinesalite)/[dynalite](https://github.com/mhart/dynalite) and [moto](https://github.com/spulec/moto). While these tools are *awesome* (!), they lack functionality for certain use cases. LocalStack combines the tools, makes them interoperable, and adds important missing functionality on top of them
- Has lots of config and knobs, but runs in docker so that helps

Extras:

- [Python Job Board](https://www.python.org/jobs/)

Michael:


- [Guido interviewed for JavaScript language](https://twitter.com/joostlubach/status/1203273058133454848)!
- [Microsoft: We're creating a new Rust-based programming language for secure coding](https://www.zdnet.com/article/microsoft-were-creating-a-new-rust-based-programming-language-for-secure-coding/)
- [New webcast: Python for the .NET developer](https://www.crowdcast.io/e/python-for-dotnet-devs-webcast)
- [Ace Python Interviews free course](https://store.lerner.co.il/ace-python-interviews)

Joke: [Types of software jobs](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5dea84098844ad200aac9a52/056c9e38545b0d04786a2f57aed18b80/065993072277cd63e10884ddbb606ed8.jpg).
