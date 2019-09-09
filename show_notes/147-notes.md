# Python Bytes 147
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/datadog)

**Brian #1:** [**rapidtables**](https://github.com/alttch/rapidtables)

- “**rapidtables …** converts lists of dictionaries to pre-formatted tables. And it does the job as fast as possible.”
- Also can do color formatting if used in conjunction with `termcolor.colored`, but I’m mostly excited about really easily generating tabular data with `print`.
- Can also format to markdown or reStructured text, and can do alignment, … 

**Michael #2**: [**httpx**](https://github.com/encode/httpx)

- A next generation HTTP client for Python. 🦋
- HTTPX builds on the well-established usability of `requests`, and gives you:
	- A requests-compatible API.
	- HTTP/2 and HTTP/1.1 support.
	- Support for [issuing HTTP requests in parallel](https://www.encode.io/httpx/parallel/). *(Coming soon)*
	- Standard synchronous interface, but [with](https://www.encode.io/httpx/async/) `[async](https://www.encode.io/httpx/async/)`[/](https://www.encode.io/httpx/async/)`[await](https://www.encode.io/httpx/async/)` [support if you need it](https://www.encode.io/httpx/async/).
	- Ability to [make requests directly to WSGI or ASGI applications](https://www.encode.io/httpx/advanced/#calling-into-python-web-apps).
		- This is particularly useful for two main use-cases:
			- Using `httpx` as a client, inside test cases.
			- Mocking out external services, during tests or in dev/staging environments.
	- Strict timeouts everywhere.
	- Fully type annotated.
	- 100% test coverage.
- Lovely support for “[parallel requests](https://www.encode.io/httpx/parallel/)” without full `asyncio` (at the API level).
	- Also pairs with async / await with async client.
- Plus all the requests features

**Brian #3:** [**Quick and dirty mock service with Starlette**](https://www.mattlayman.com/blog/2019/starlette-mock-service/)

- Matt Layman
- Mock out / fake a third party service in a testing environment.
- Starlette looks fun, but the process can be used with other API producing server packages.
- We tell people to do things like this all the time, but there are few examples showing how to.
- This example also introduces a delay because the service used in production takes over a minute and part of the testing is to make sure the system under test handles that delay gracefully.
- Very cool, easy to follow write up. (Should probably have Matt on a [Test & Code](https://testandcode.com) episode to talk about this strategy.)

**Michael #4:** [**Mocking out AWS APIs**](https://github.com/spulec/moto)

- via Giuseppe Cunsolo
- A library that allows you to easily mock out tests based on AWS infrastructure.
- Lovely use of a decorator to mock out S3
- Moto isn't just for Python code and it isn't just for S3. Look at the [standalone server mode](https://github.com/spulec/moto#stand-alone-server-mode) for more information about running Moto with other languages.
- Be sure to check out [very important note](https://github.com/spulec/moto#very-important----recommended-usage).

**Brian #5**: [**μMongo: sync/async ODM**](https://github.com/Scille/uMongo)

- “μMongo is a Python MongoDB ODM. It inception comes from two needs: the lack of async ODM and the difficulty to do document (un)serialization with existing ODMs.”
- works with common mongo drivers such as PyMongo, TxMongo, motor_asyncio, and mongomock. (Hadn’t heard of [mongomock](https://github.com/vmalloc/mongomock) before, I’ll have to try that out.)
- Note: We’ve discussed [MongoEngine](https://github.com/MongoEngine/mongoengine) before. (I’m curious what Michael has to say about uMongo.)
    

**Michael #6:** [**Single Responsibility Principle**](https://sobolevn.me/2019/03/enforcing-srp) [**in Python**](https://sobolevn.me/2019/03/enforcing-srp)

- via Tyler Matteson
- I’m a big fan of the [SOLID principles](https://itnext.io/solid-principles-explanation-and-examples-715b975dcad4)
- They even come in demotivator style posters
	- [DI](https://www.google.com/imgres?imgurl=http%3A%2F%2Fbrendan.enrick.com%2Fimage.axd%3Fpicture%3DNP-Dependency-Inversion_thumb.jpg&imgrefurl=http%3A%2F%2Fbrendan.enrick.com%2Fpost%2FSOLID-Principles-Software-Craftsmanship-Calendar-Topics&docid=No884kr6Vq4XOM&tbnid=fO846X2JegtChM%3A&vet=10ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhDKAAwAA..i&w=484&h=484&client=firefox-b-1-d&bih=901&biw=1677&q=SOLID%20principles%20calendar&ved=0ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhDKAAwAA&iact=mrc&uact=8)
	- [Liskov Substitution Principle](https://www.google.com/imgres?imgurl=http%3A%2F%2Fbrendan.enrick.com%2Fimage.axd%3Fpicture%3DLiskovSubstitutionPrinciple_thumb.jpg&imgrefurl=http%3A%2F%2Fbrendan.enrick.com%2Fpost%2FSOLID-Principles-Software-Craftsmanship-Calendar-Topics&docid=No884kr6Vq4XOM&tbnid=US_KS_hI72yNQM%3A&vet=10ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhEKAEwAQ..i&w=485&h=484&client=firefox-b-1-d&bih=901&biw=1677&q=SOLID%20principles%20calendar&ved=0ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhEKAEwAQ&iact=mrc&uact=8)
	- [Open/Closed Principle](https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.somkiat.cc%2Fwp-content%2Fuploads%2F2015%2F06%2Focp.jpeg&imgrefurl=http%3A%2F%2Fwww.somkiat.cc%2Fsolid-principle-calendar%2F&docid=k7BTk5K9fRkuhM&tbnid=zBs-qf2LFzsZAM%3A&vet=10ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhFKAIwAg..i&w=485&h=484&client=firefox-b-1-d&bih=901&biw=1677&q=SOLID%20principles%20calendar&ved=0ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhFKAIwAg&iact=mrc&uact=8)
	- [**Single Responsibility Principle**](https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.slidesharecdn.com%2Frefactoringwithsoliddevreach2012-121007122059-phpapp01%2F95%2Frefactoring-applications-using-solid-principles-15-728.jpg%3Fcb%3D1349617964&imgrefurl=https%3A%2F%2Fwww.slideshare.net%2Fardalis%2Frefactoring-applications-using-solid-principles&docid=zOwSzU4-EL6BoM&tbnid=iIl4YkbBFDejHM%3A&vet=10ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhGKAMwAw..i&w=728&h=546&client=firefox-b-1-d&bih=901&biw=1677&q=SOLID%20principles%20calendar&ved=0ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhGKAMwAw&iact=mrc&uact=8)
	- [Interface Segregation Principle](https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.slidesharecdn.com%2Frefactoringwithsoliddevreach2012-121007122059-phpapp01%2F95%2Frefactoring-applications-using-solid-principles-34-728.jpg%3Fcb%3D1349617964&imgrefurl=https%3A%2F%2Fwww.slideshare.net%2Fardalis%2Frefactoring-applications-using-solid-principles&docid=zOwSzU4-EL6BoM&tbnid=NvBTSxYKM_5BTM%3A&vet=10ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhHKAQwBA..i&w=728&h=546&client=firefox-b-1-d&bih=901&biw=1677&q=SOLID%20principles%20calendar&ved=0ahUKEwjx_rWazLXkAhWEop4KHYLSADIQMwhHKAQwBA&iact=mrc&uact=8)
- This article will guide you through a **complex process of writing simple code**.

**Extras**

Michael:

- [Code Challenge Bite 220. Analyzing @pythonbytes RSS feed](https://codechalleng.es/bites/220/)

**Jokes** 

- Q: What do you get when you cross a computer and a life guard?
- A: A screensaver!

- Q: What do you get when you cross a computer with an elephant?
- A: Lots of memory!

via [https://github.com/wesbos/dad-jokes](https://github.com/wesbos/dad-jokes) 

Anti-joke (we ready for those yet?): A Python developer, a PHP developer, a C# developer, and a Go developer went to lunch together.  They had a nice lunch and got along fine.

