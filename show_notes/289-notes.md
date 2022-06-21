# Python Bytes 289

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: [**Gina Häußge**](https://twitter.com/foosel), creator & maintainer of [**OctoPrint**](https://octoprint.org)

**Michael #1:** [**beanita**](https://github.com/roman-right/beanita)

- Local MongoDB-like database prepared to work with Beanie ODM
- So, you know [**Beanie**](https://github.com/roman-right/beanie) - Pydantic + async + MongoDB
- And you know [**Mongita**](https://github.com/scottrogowski/mongita) - Mongita is to MongoDB as SQLite is to SQL 
- Beanita lets you use Beanie, but against Mongita rather than a server-based MongoDB server

**Brian #2:** [**The Good Research Code Handbook**](https://goodresearch.dev/index.html)

- Patrick J Mineault
- “for grad students, postdocs and PIs (principle investigator) who do a lot of programming as part of their research.”
- lessons
    - setup
        - git, virtual environments, project layout, packaging, cookie cutter
    - style
        - style guides, keeping things clean
    - coding
        - separating concerns, separating pure functions and those with side effects, pythonic-ness
    - testing
        - unit testing, testing with side effects, …
        - (incorrect definition of end-to-end tests, but a good job at covering the other bits)
    - documentation 
        - comments, tests, docstrings, README.md, usage docs, tutorials, websites
        - documenting pipelines and projects
    - social aspects
        - various reviews, pairing, open source, community 
    - sample project
    - extras
        - testing example
        - good tools to use

**Gina** **#3:** [**CadQuery**](https://cadquery.readthedocs.io/en/latest/)

- Python lib to do build parametric 3D CAD models
- Can output STL, STEP, AMF, SVG and some more
- Uses same geometry kernel as FreeCAD (OpenCascade)
- Also available: desktop editor, Jupyter extension, CLI
    - Would recommend the Jupyter extension, the app seems a bit behind latest development
- Jupyter extension is easy to set up on Docker and comes with a nice 3D preview pane
- Was able to create a basic parametric design of an insert for an assortment box easily
- Python 3.8+, not yet 3.11, OpenCascade related

**Michael #4:** [**Textinator**](https://twitter.com/RhetTurnbull/status/1535713115421089792)

- Like [**TextSniper**](https://www.textsniper.app), but in Python
- Simple MacOS StatusBar / Menu Bar app to automatically detect text in screenshots
- Built with [RUMPS](https://github.com/jaredks/rumps): Ridiculously Uncomplicated macOS Python Statusbar apps
- Take a screenshot of a region of the screen using ⌘ + ⇧ + 4 (`Cmd + Shift + 4`). 
- The app will automatically detect any text in the screenshot and copy it to your clipboard.
- How Textinator Works
    - At startup, Textinator starts a persistent [NSMetadataQuery Spotlight query](https://developer.apple.com/documentation/foundation/nsmetadataquery?language=objc) (using the [pyobjc](https://pyobjc.readthedocs.io/en/latest/) Python-to-Objective-C bridge) to detect when a new screenshot is created.
    - When the user creates screenshot, the `NSMetadataQuery` query is fired and Textinator performs text detection using a [Vision](https://developer.apple.com/documentation/vision?language=objc) [VNRecognizeTextRequest](https://developer.apple.com/documentation/vision/vnrecognizetextrequest?language=objc) call.

**Brian #5:** [**Handling Concurrency Without Locks**](https://hakibenita.com/django-concurrency)

- "How to not let concurrency cripple your system”
- Haki Benita
- “…common concurrency challenges and how to overcome them with minimal locking.”
- Starts with a Django web app
- A url shortener that generates a unique short url and stores the result in a database so it doesn’t get re-used.
- Discussions of 
    - collision with two users checking, then storing keys at the same time.
    - locking problems in general 
    - utilizing database ability to make sure some items are unique, in this case PostgreSQL
    - updating your code to take advantage of database constraints support to allow you to do less locking within your code

**Gina** **#6:** [**TatSu**](https://tatsu.readthedocs.io/en/stable/)

- Generates parsers from EBNF grammars (or ANTLR)
- Can compile the model (similar to regex) for quick reuse or generate python source
- Many examples provided
- Active development, Python 3.10+

**Extras** 

Michael:

- [**Back on 285**](https://pythonbytes.fm/episodes/show/285/where-we-talk-about-uis-and-python) we spoke about PEP 690. Now there is a [**proper blog post**](https://developers.facebook.com/blog/post/2022/06/15/python-lazy-imports-with-cinder) about it.
- [**Expedited release of Python3.11.0b3**](https://pythonweekly.us2.list-manage.com/track/click?u=e2e180baf855ac797ef407fc7&id=34c7bf229c&e=e4bde12891) - Due to a known incompatibility with pytest and the previous beta release ([**Python 3.11.0b2**](https://pythonweekly.us2.list-manage.com/track/click?u=e2e180baf855ac797ef407fc7&id=254cb29852&e=e4bde12891)) and after some deliberation, Python release team have decided to do an expedited release of Python 3.11.0b3 so the community can continue testing their packages with pytest and therefore testing the betas as expected. (via Python Weekly)
- [**Kagi search**](https://kagi.com)
    - via Daniel Hjertholm
    - Not really python related, but if I know Michael right, he'll love the new completely ad free and privacy-respecting search engine kagi.com.  I've used kagi.com since their public beta launched, mainly to search for solutions to Python issues at work. The results are way better than DuckDuckGo's results, and even better than Googles! Love the Programming-lens and the ability to up/down prioritize domains in the results.
    - Their FAQ explains everything you need to know: **[https://kagi.com/faq](https://kagi.com/faq)**
    - Looks great but not sure about the pricing justification (32 sec of compute = $1), that’s either 837x more than all of Talk Python + Python Bytes or more than 6,700x more than just one of our sites/services. (We spend about $100/mo on 8 servers.) But they *may* be buying results from Google and Bing, and that could be the cost.
    - Here's **[a short interview](https://twitter.com/vladquant/status/1538559700593156102?s=21&t=YSBQS2lP3oWVA9YDlZt1OA)** with the man who started kagi.

Gina: 

- [**rdserialtool**](https://github.com/rfinnie/rdserialtool): Reads out low-cost USB power monitors (UM24C, UM25C, UM34C) via BLE/pybluez. Amazing if you need to monitor the power consumption/voltage/current of some embedded electronics on a budget. Helped me solve a very much OctoPrint development specific problem. Python 3.4+
- [**nodejs-bin**](https://pypi.org/project/nodejs-bin/): 
    - by Sam Willis: [https://twitter.com/samwillis/status/1537787836119793667](https://twitter.com/samwillis/status/1537787836119793667)
    - Install nodejs via pypi/as dependency, still very much an Alpha but looks promising
    - Makes it easier to obtain a full stack environment
    - Very interesting for end to end testing with JS based tooling, or packaging a frontend with your Python app
    - See also nodeenv, which does a similar thing, but with additional steps

**Joke:** [**Rejected Github Badges**](https://twitter.com/btskinn/status/1535605341446098946)
