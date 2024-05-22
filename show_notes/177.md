# Python Bytes 177

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

We’re launching a YouTube Project: [**pythonbytes.fm/youtube**](http://pythonbytes.fm/youtube)

**Brian #1:** [**Announcing a new Sponsorship Program for Python Packaging**](http://pyfound.blogspot.com/2020/04/sponsoring-python-packaging.html)

- “The Packaging Working Group of the Python Software Foundation is launching an all-new sponsorship program to sustain and improve Python's packaging ecosystem. Funds raised through this program will go directly towards improving the tools that your company uses every day and sustaining the continued operation of the Python Package Index.”
- Improvements since 2017, as a result of one time grants, a contract, and a gift:
	- relaunch PyPI in 2018
	- added security features in 2019
	- improve support for users with disabilities and multiple locales in 2019
	- security features in 2019, 2020
	- pip & dependency resolver in 2020
- Let’s keep it going
	- We use PyPI every day
	- We need packaging to keep getting better
- You, and your company, can sponsor. View the [prospectus](https://pypi.org/sponsor), [apply to sponsor](https://docs.google.com/forms/d/e/1FAIpQLSe3pvmpCYLTPB-V_9hpT6vrarm9GE6Wko_fy_KhJKm7NFqF_Q/viewform), or [ask questions](mailto:sponsorship@pypi.org).
- Individuals can also [donate](https://donate.pypi.org/).

**Michael #2:** [**energy-usage**](https://github.com/responsibleproblemsolving/energy-usage)

- A Python package that measures the environmental impact of computation. 
- Provides a function to evaluate the energy usage and related carbon emissions of another function. 
- Emissions are calculated based on the user's location via the GeoJS API and that location's energy mix data (sources: US E.I.A and eGRID for the year 2016).
- Can save report to PDF, run silently, etc.
- Only runs on Linux

**Brian #3:** [**Coding is 90% Google Searching — A Brief Note for Beginners**](https://medium.com/@DJVeaux/coding-is-90-google-searching-a-brief-note-for-beginners-f2f1161876b1)

- Colin Warn
- Short article, mostly chosen to discuss the topic.
- Michael & Brian disagree, so, what’s wrong with this statement?

**Michael #4:** [**Using WSL to Build a Python Development Environment on Windows**](https://pbpython.com/wsl-python.html)

- Article by Chris Moffet 
- VMs aren’t fair to Windows (or macOS or …)
- But you need to test on linux-y systems! Enter WSL.
- In 2016, Microsoft launched Windows Subsystem for Linux (WSL) which brought robust unix functionality to Windows.
- May 2019, Microsoft announced the release of WSL 2 which includes an updated architecture that improved many aspects of WSL - especially file system performance.
- Check out Chris’ article for
	- What is WSL and why you may want to install and use it on your system?
	- Instructions for installing WSL 2 and some helper apps to make development more streamlined.
	- How to use this new capability to work effectively with python in a combined Windows and Linux environment.
- The main advantage of WSL 2 is the efficient use of system resources. 
- Running a very minimal subset of Hyper-V features and only using minimal resources when not running.
- Takes about 1 second to start.
- The other benefit of this arrangement is that you can easily copy files between the virtual environment and your base Windows system.
- Get the most out of this with VS Code + 
	- [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
	- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
	- [Anaconda Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack)

**Brian #5:** [**A Pythonic Guide to SOLID Design Principles**](https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i)

- Derek D
- Again, mostly including this as a discussion point
- But for reference, here’s the decoder
	- Single Responsibility Principle 
		- Every module/class should only have one responsibility and therefore only one reason to change.
	- Open Closed Principle 
		- Software Entities (classes, functions, modules) should be open for extension but closed to change.
	- Liskov's Substitutability Principle
		- If S is a subtype of T, then objects of type T may be replaced with objects of Type S.
	- Interface Segregation Principle
		- A client should not depend on methods it does not use.
	- Dependency Inversion Principle
		- High-level modules should not depend on low-level modules. They should depend on abstractions and abstractions should not depend on details, rather details should depend on abstractions.

**Michael #6:** [**Types for Python HTTP APIs: An Instagram Story**](https://instagram-engineering.com/types-for-python-http-apis-an-instagram-story-d3c3a207fdb7)

- Let’s talk about Typed HTTP endpoints
- Instagram has a few (thousand!) on a single Django app
- We can have data access layers with type annotations, but how do these manifest in HTTP endpoints?
- Instagram has a cool `api_view` decorator to “upgrade” regular typed methods to HTTP endpoints.
- For data exchange, dataclasses are nice, they have types, they have type validation, they are immutable via `frozen`.
- But some code is old and crusty, so `TypedDict` out of `mypy` allows raw `dict` usage with validation still.
- [OpenAPI](https://github.com/OAI/OpenAPI-Specification) can be used for very nice documentation generation.
- Comments are super interesting. Suggesting `pydantic`, `fastapi`, and more. But that all ignores the massive legacy code story.
- But one is helpful and suggests `Schemathesis`: A tool for testing your web applications built with Open API / Swagger specifications.

**Extras:**

Michael:

- [superstring follow up](https://twitter.com/thisfred/status/1245836318027812864)

**Joke:**

> "How many programmers does it take to kill a cockroach? Two: one holds, the other installs Windows on it."
