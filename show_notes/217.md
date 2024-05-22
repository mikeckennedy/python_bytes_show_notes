# Python Bytes 217

Sponsored by **Linode!** [**pythonbytes.fm/linode**](https://pythonbytes.fm/linode)

Special guest: [**Ogi Moore**](https://twitter.com/ogimoore)

**Michael #1:** [**diskcache**](https://github.com/grantjenks/python-diskcache)

-  via Ian Maurer
- Python disk-backed cache (Django-compatible). Faster than Redis and Memcached. Pure-Python.
- The cloud-based computing of 2020 puts a premium on memory. Gigabytes of empty space is left on disks as processes vie for memory. 
- Among these processes is Memcached (and sometimes Redis) which is used as a cache. 
- Wouldn't it be nice to leverage empty disk space for caching?
- **Features:**
- Pure-Python
- Fully Documented
- Benchmark comparisons (alternatives, Django cache backends)
- 100% test coverage
- Hours of stress testing
- Performance matters
- Django compatible API
- Thread-safe and process-safe
- Supports multiple eviction policies (LRU and LFU included)
- Keys support "tag" metadata and eviction
- Developed on Python 3.8
- Tested on CPython 3.5, 3.6, 3.7, 3.8
- Tested on Linux, Mac OS X, and Windows
- Tested using Travis CI and AppVeyor CI

**Brian #2:** [**TOML is 1.0.0 now.**](https://toml.io/en/) 

- What does that mean for Python?
	- Hopefully, some kind of toml parser will make it into Python core. 
- Any Python access to 1.0.0? Mixed
	- [Implementations and TOML version support page](https://github.com/toml-lang/toml/wiki) lists:
    - pytomlpp supports 1.0.0-rc.3, which is a wrapper around C++ tomlplusplus, which does support 1.0.0. Confusing
    - tomlkit supports 1.0.0-rc.1, so that’s promising
    - toml supports 0.5.0, great name. It’d be cool if it would support 1.0.0
- What’s different between 0.5.0 and 1.0.0?
	- Unless I’m mistaken, not much: [CHANGELOG](https://github.com/toml-lang/toml/blob/master/CHANGELOG.md)
	- 1.0.0-rc1
    - Leading zeroes in exponent parts of floats are permitted.
    - Allow raw tab characters in basic strings and multi-line basic strings.
    - Allow heterogenous values in arrays.
	- Other than that, lots of “Clarify …”, which I’m not sure how those all affect implementation.
- I’d love to hear more from people who know more about this

**Ogi #3: [pyqtgraph](http://www.pyqtgraph.org/)**

- pyqtgraph - plotting library, for when you need fast/interactive plots
- Uses qt5 (and soon qt6) bindings to generate plots within Qt applications
- Fills a niche role, want easy mouse interactivity, running locally on a machine
- Often used in engineering/scientific applications when looking at a lot of data, and wanting interactivity 


**Michael #4:** [**Parler + Python = Insurrection in public**](https://twitter.com/shaunking/status/1349495948972593154)

- via [Jim Kring](https://twitter.com/jimkring) and Mark Little
- [According to Wikipedia](https://en.wikipedia.org/wiki/Parler): Parler (/ˈpɑːrlər/) is an American alt-tech microblogging and social networking service. Parler has a significant user base of Donald Trump supporters, conservatives, conspiracy theorists, and right-wing extremists.
- ArsTechnica article send in by Mark Little
- Ars: [Parler’s amateur coding could come back to haunt Capitol Hill rioters](https://arstechnica.com/information-technology/2021/01/parlers-amateur-coding-could-come-back-to-haunt-capitol-hill-rioters/)
- Coding mess
	- A key reason for her success: Parler’s site was a mess. Its public API used no authentication. 
	- When users deleted their posts, the site failed to remove the content and instead only added a delete flag to it. 
	- Oh, and each post carried a numerical ID that was incremented from the ID of the most recently published one.
	- Another amateur mistake was Parler’s failure to scrub geolocations from images and videos posted online.
- Some 80 terabytes of posts, 1M videos, many already deleted, preserved for posterity.
- Catalog and Python pointed out by [Shaun King](https://twitter.com/shaunking).
- See [the catalog](https://www.tommycarstensen.com/terrorism/index.html) (maybe, it’s the ugly side of people).
- The gist: [https://gist.github.com/kylemcdonald/d8884da1a82ef50754ee49e0b6561071](https://gist.github.com/kylemcdonald/d8884da1a82ef50754ee49e0b6561071)
- Partially back online with Russian hosting service?

**Brian #5:** [**Best-of Web Development with Python**](https://github.com/ml-tooling/best-of-web-python)

- Suggested by Douglas Nichols
- Cool list with nice icons
- Covers
	- Frameworks, HTTP Clients, Servers
	- Auth tools, HTML Processing, URL utilities
	- OpenAPI, GraphQL, Websocket
	- RPC, Serverless, Content Management
	- Web Testing, Web Forms, Markdown
	- Third-party APIs
	- Email, Web Scraping & Crawling, Monitoring
	- Admin UI
	- API Proxies
	- Flask/FastAPI/Pyramid/Django  Utilities
- Nice to see lots of FastAPI projects:
	- fastapi-sqlalchemy - Adds simple SQLAlchemy support to FastAPI. 
	- fastapi-plugins - FastAPI framework plugins. 
	- fastapi_contrib - Opinionated set of utilities on top of FastAPI. 
	- starlette_exporter - Prometheus exporter for Starlette and FastAPI. 
	- fastapi-utils - Reusable utilities for FastAPI. 
	- fastapi-code-generator - This code generator creates FastAPI app from an.. 
	- slowapi - A rate limiter for Starlette and FastAPI. 
	- fastapi-versioning - api versioning for fastapi web applications. 
	- fastapi-react - Cookiecutter Template for FastAPI + React Projects. Using.. 
	- fastapi_cache - FastAPI simple cache. 

**Ogi #6: Assorted** 
- Pyjion - [https://github.com/tonybaloney/Pyjion](https://github.com/tonybaloney/Pyjion) a JIT extension for CPython that compiles python code using .NET 5 CLR 
- CuPy - NumPy compatible multi-dimensional array on CUDA, uses  `_``*array_function_*` (enabled with numpy 1.17) code using numpy to operate directly on CuPy arrays
	- [see NEP-18](https://numpy.org/neps/nep-0018-array-function-protocol.html) and [CuPy docs](https://docs.cupy.dev/en/stable/reference/interoperability.html)
	- compatible with other libraries as well

Extras:

Michael:

- Trying Firefox + Brave + VPN
- [Python Web Conf 2021](https://www.papercall.io/pwc-2021) call for talks, due Jan 29, I’ll be speaking!
- [PyCon US 2021](https://us.pycon.org/2021/speaking/) launched call for proposals:
	- December 22, 2020 — Call for proposals opened
	- February 12, 2021 — Proposals are due
	- March 16, 2021 — Notifications will be sent to presenters
	- March 23, 2021 — Deadline for speakers to confirm participation
	- March 30, 2021 — Schedule is publicly released
	- April 28, 2021 — Deadline to submit pre-recorded presentation (tutorials will be live)
	- May 12-13, 2021 — Tutorial days
	- May 15-16, 2021 — Conference days
- [Apple launching Racial Equity and Justice Initiatives](https://www.youtube.com/watch?v=tlWPdAWEjys) with partners across a broad range of industries and backgrounds — from students to teachers, developers to entrepreneurs, and community organizers to justice advocates

**Brian:**

- PyCascades 2021 schedule [https://2021.pycascades.com/program/schedule/](https://2021.pycascades.com/program/schedule/)

Ogi: 

- [Anthony Explains Video Series](https://www.youtube.com/playlist?list=PLWBKAf81pmOaP9naRiNAqug6EBnkPakvY)
- [Learn X in Y minutes](https://learnxinyminutes.com/)
- Reading [Working in Public](https://www.amazon.com/Working-Public-Making-Maintenance-Software/dp/0578675862) by Nadia Eghbal - provides some sanity checks for existing maintainers, might be a fantastic perspective for new contributors to open source

Joke

**Tech Support, 2x**

Working at the help desk? Get the theme song:

[Here to help song](https://youtu.be/_GTnJDvWpt0)

And help by chat:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5fdd9751558ca32ee444023f/2e82ec305e266150baa3a4dca1717111/Screen_Shot_2020-12-18_at_10.01.17_PM.png)


- "Running a successful open source project is just Good Will Hunting in reverse, where you start out as a respected genius and end up being a janitor who gets into fights." - Byrne Hobart

