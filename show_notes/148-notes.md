# Python Bytes 148

Sponsored by **DigitalOcean:** [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Brian #1:** [**Annual Release Cycle for Python**](https://www.python.org/dev/peps/pep-0602/) **- PEP 602**

- [Under discussion](https://discuss.python.org/t/pep-602-annual-release-cycle-for-python/2296)
- Annual release cadence
- Seventeen months to develop a major version
	- 5 months unversioned, 7 months alpha releases when new features and fixes come in, 4 months of betas with no new features, 1 month final RCs.
- One year of full support, four more years of security fixes.
- Rationale/Goals
	- smaller releases
	- features and fixes to users sooner
	- more gradual upgrade path
	- predictable  calendar releases that line up will with sprints and PyConUS
	- explicit alpha phase
	- decrease pressure and rush to get features into beta 1
- Risks
	- Increase concurrent supported versions from 4 to 5.
	- Test matrix increase for integrators and distributions.
- PEP includes rejected ideas like:
	- 9 month cadence
	- keep 18 month cadence

**Michael #2:** [**awesome-asgi**](https://github.com/florimondmanca/awesome-asgi)

- A curated list of awesome ASGI servers, frameworks, apps, libraries, and other resources  
- [ASGI](https://asgi.readthedocs.io) is a standard interface positioned as a spiritual successor to WSGI. It enables communication and interoperability across the whole Python async web stack: servers, applications, middleware, and individual components.
- Born in 2016 to power the Django Channels project, ASGI and its ecosystem have been expanding ever since, boosted by the arrival of projects such as Starlette and Uvicorn in 2018.
- *Frameworks for building ASGI web applications.*
	- [Bocadillo](https://bocadilloproject.github.io) - Fast, scalable and real-time capable web APIs for everyone. Powered by Starlette. Supports HTTP (incl. SSE) and WebSockets.
	- [Channels](https://channels.readthedocs.io/en/latest/) - Asynchronous support for Django, and the original driving force behind the ASGI project. Supports HTTP and WebSockets with Django integration, and any protocol with ASGI-native code.
	- [FastAPI](https://github.com/tiangolo/fastapi) - A modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. Powered by Starlette and Pydantic. Supports HTTP and WebSockets.
	- [Quart](https://github.com/pgjones/quart) - A Python ASGI web microframework whose API is a superset of the Flask API. Supports HTTP (incl. SSE and HTTP/2 server push) and WebSockets.
	- [Responder](https://python-responder.org/en/latest/) - A familiar HTTP Service Framework for Python, powered by Starlette. (ASGI 2.0 only, ed.)
	- [Starlette](https://www.starlette.io/) - Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. Supports HTTP and WebSockets.

**Brian #3**: [**Jupyter meets the Earth**](https://blog.jupyter.org/jupyter-meets-the-earth-1b0eb33c83f)

- Lindsey Heagy & Fernando Pérez
- “We are thrilled to announce that the NSF is funding our EarthCube proposal *“Jupyter meets the Earth: Enabling discovery in geoscience through interactive computing at scale”* “
- “This project provides our team with $2 Million in funding over 3 years as a part of the NSF [EarthCube](https://earthcube.org/) program. It also represents the first time federal funding is being allocated for the development of core Jupyter infrastructure.”
- “Our project team includes members from the [Jupyter](https://jupyter.org/) and [Pangeo](http://pangeo.io/) communities, with representation across the geosciences including climate modeling, water resource applications, and geophysics. Three active research projects, one in each domain, will motivate developments in the Jupyter and Pangeo ecosystems. Each of these research applications demonstrates aspects of a research workflow which requires scalable, interactive computational tools.”
- “The adoption of open languages such as Python and the coalescence of communities of practice around open-source tools, is visible in nearly every domain of science. This is a fundamental shift in how science is conducted and shared.”
- Geoscience use cases
	- climate data analysis
	- hydrologic modeling
	- geophysical inversions
- User-Centered Development
	- data discovery
	- scientific discovery through interactive computing
	- established tools and data visualization
	- using and managing shared computational infrastructure

**Michael #4:** [**Asynchronous Django**](https://docs.djangoproject.com/en/dev/releases/3.0/)

- via Jose Nario
- Python compatibility
	- Django 3.0 supports Python 3.6, 3.7, and 3.8. We highly recommend and only officially support the latest release of each series
	- The Django 2.2.x series is the last to support Python 3.5.
- Other items but
- Big news: **ASGI support**
- Django 3.0 begins our journey to making Django fully async-capable by providing support for running as an ASGI application.
- This is in addition to our existing WSGI support. Django intends to support both for the foreseeable future.
- Note that as a side-effect of this change, Django is now aware of asynchronous event loops and will block you calling code marked as “async unsafe” - such as ORM operations - from an asynchronous context.

**Brian #5**: [**The 1x Engineer**](https://1x.engineer/)

- *Fun take on 10x. List actually looks like probably a 3-4x to me, maybe even 8x or more. How high does this scale go anyway?*
- non-exhaustive list qualities, here’s a few.
	- Has a life outside engineering.
	- Writes code that others can read.
	- Doesn't act surprised when someone doesn’t know something.
	- Asks for help when they need it.
	- Is able to say "I don't know."
	- Asks questions.
	- Constructively participates in code reviews.
	- Can collaborate with others.
	- Supports code, even if they did not write it.
	- Can feel like an impostor at times.
	- Shares knowledge.
	- Never stops learning. 
		- *[obviously listens to Python Bytes, Talk Python, and Test & Code]*
	- Is willing to leave their comfort zone.
	- Contributes to the community.
	- Has productive and unproductive days.
	- Doesn't take themselves too seriously.
	- Fails from time to time.
	- Has a favorite editor, browser, and operating system, but realizes others do too.

**Michael #6:**  [**Sunsetting Python 2**](https://www.python.org/doc/sunset-python-2/)

- January 1, 2020, will be the day that we sunset Python 2
- Why are you doing this? We need to sunset Python 2 so we can help Python users.
- **How long is it till the sunset date?** [pythonclock.org](https://pythonclock.org/) will tell you.
- **What will happen if I do not upgrade by January 1st, 2020?** If people find catastrophic security problems in Python 2, or in software written in Python 2, then most volunteers will not help fix them.
- **I wrote code in Python 2. How should I port it to Python 3?** Please read [the official "Porting Python 2 Code to Python 3" guide](https://docs.python.org/3/howto/pyporting.html).
- **I didn't hear anything about this till just now. Where did you announce it?** We talked about it at software conferences, on the Python announcement mailing list, on official Python blogs, in textbooks and technical articles, on social media, and to companies that sell Python support.

**Extras**

Brian:

- working on a Portland Westside Python Meetup, info will be at [pythonpdx.com](http://pythonpdx.com)
	- Hoping to get something ready for Oct. But… if not, hopefully by Nov.

Michael:

- [**Humble Level Up Your Python Bundle**](https://talkpython.fm/hb2019)
