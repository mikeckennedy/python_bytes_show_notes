# Python Bytes 318

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with us**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/stream/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**PEP 703 - Making the GIL Optional in CPython**](https://peps.python.org/pep-0703/)

- Author: Sam Gross
- Sponsor: Łukasz Langa
- Draft status, but on Standards Track, targeting Python 3.12
- Suggested by: Will Shanks
- “The GIL is a major obstacle to concurrency.” Especially for scientific computing.
- PEP 703 proposes adding a `--without-gil` build configuration to CPython to let it run code without the global interpreter lock and with the necessary changes needed to make the interpreter thread-safe.
- PEP includes several issues with GIL and sckikit-learn, PyTorch, Numpy, Pillow, and other numerically intensive libraries.
- Python’s GIL makes it difficult to use modern multi-core CPUs efficiently for many scientific and numeric computing applications.
- There’s also a section on how the GIL makes many types of parallelism difficult to express.
- Changes primarily in internals, and not much exposed to public Python and C APIs:
    - Reference counting
    - Memory management
    - Container thread-safety
    - Locking and atomic APIs
- Includes information on all of these challenges.
- Distribution
    - C-API extension authors will need access to a `--without-gil` Python to modify their projects and supply `--without-gil` versions.
    - Sam is proposing “To mitigate this, the author will work with Anaconda to distribute a `--without-gil` version of Python together with compatible packages from conda channels. This centralizes the challenges of building extensions, and the author believes this will enable more people to use Python without the GIL sooner than they would otherwise be able to.”


**Michael #2:** [FerretDB](https://www.ferretdb.io)

- Via Jon Bultmeyer
- A truly Open Source MongoDB alternative
- MongoDB abandoned its Open-Source roots, changing the license to SSPL making it unusable for many Open Source and Commercial Projects.
-  The core of our solution is a stateless proxy, which converts MongoDB protocol queries to SQL, and uses PostgreSQL as a database engine. 
- FerretDB will be compatible with MongoDB drivers and will strive to serve as a drop-in replacement for MongoDB 6.0+.
- [First release](https://www.ferretdb.io/new-release-ferretdb-0_6_1/) back in Nov 2022
- I still love you MongoDB ;)


**Brian #3:** [**Four tips for structuring your research group’s Python packages**](https://blog.nicholdav.info//four-tips-structuring-research-python/?utm_source=pocket_reader)

- David Aaron Nicholson
- Not PyPI packages, but, you know, directories with `__init__.py` in them.
- Corrections for mistakes I see frequently
    - Give your packages and modules terse, single-word names whenever possible.
    - Import modules internally, instead of importing everything *from* modules.
    - Make use of sub-packages.
    - Prefer modules with very specific names containing single functions over modules with very general names like `utils`, `helpers`, or `support` that contain many functions.

**Michael #4:** [**Quibbler**](https://github.com/Technion-Kishony-lab/quibbler)

- *Quibbler* is a toolset for building highly interactive, yet reproducible, transparent and efficient data analysis pipelines.
- One import statement and matplotlib becomes interactive.
- Check out [the video](https://github.com/Technion-Kishony-lab/quibbler) on the repo page.

**Extras** 

Brian:

- And now for something completely different: [turtles talk](https://www.washingtonpost.com/climate-environment/2023/01/06/turtles-eat-south-america/?utm_source=pocket_saves)

Michael:

- More RSS recommendations
    - [FreshRSS](https://www.freshrss.org) a self-hosted RSS and Atom feed aggregator.
    - [Feedly (for AI)](https://feedly.com)
    - [Flym for Android](https://play.google.com/store/apps/details?id=net.frju.flym&hl=en_US&gl=US)
    - [Readwise](https://readwise.io/read) is very interesting
    - [RSS for courses at Talk Python](https://training.talkpython.fm/courses/rss)
- New article: [Dev on the Road](https://mkennedy.codes/posts/dev-on-the-road-leaving-your-laptop-at-home/)

**Joke:** [Testing the program](https://www.reddit.com/r/programminghumor/comments/zaolsk/what_is_the_hack/)
**Joke:** [Every Cloud Architecture](https://www.goodtechthings.com/every-cloud-architecture/)

