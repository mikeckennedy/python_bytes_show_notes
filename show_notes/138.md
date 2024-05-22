# Python Bytes 138
Sponsored by **DigitalOcean:** [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Brian #1:**  [**flake8-comprehensions**](https://github.com/adamchainz/flake8-comprehensions)

- submitted by Florian Dahlitz
- I’m already using flake8, so adding this plugin is a nice idea.
- checks your code for some generator and comprehension questionable code.
	- C400        Unnecessary generator - rewrite as a list comprehension.
	- C401        Unnecessary generator - rewrite as a set comprehension.
	- C402        Unnecessary generator - rewrite as a dict comprehension.
	- C403        Unnecessary list comprehension - rewrite as a set comprehension.
	- C404        Unnecessary list comprehension - rewrite as a dict comprehension.
	- C405        Unnecessary (list/tuple) literal - rewrite as a set literal.
	- C406        Unnecessary (list/tuple) literal - rewrite as a dict literal.
	- C407        Unnecessary list comprehension - '<builtin>' can take a generator.
	- C408        Unnecessary (dict/list/tuple) call - rewrite as a literal.
	- C409        Unnecessary (list/tuple) passed to tuple() - (remove the outer call to tuple()/rewrite as a tuple literal).
	- C410        Unnecessary (list/tuple) passed to list() - (remove the outer call to list()/rewrite as a list literal).
	- C411        Unnecessary list call - remove the outer call to list().
- Example:
	- Rewrite `list(f(x) for x in foo)` as `[f(x) for x in foo]`
	- Rewrite `set(f(x) for x in foo)` as `{f(x) for x in foo}`
	- Rewrite `dict((x, f(x)) for x in foo)` as `{x: f(x) for x in foo}`

**Michael #2:**  [**PyOxidizer (again)**](https://gregoryszorc.com/blog/2019/06/24/building-standalone-python-applications-with-pyoxidizer/)

- Michael’s assessment - There are three large and looming threats to Python. Lack of
	- A real mobile development story
	- GUI applications on desktop operating systems
	- Sharing your application with users (this is VERY far from deployment to servers)
- Cover PyOxidizer before but seems to have just rocketed off last couple of weeks.
- At their PyCon 2019 keynote talk, Russel Keith-Magee [identified code distribution](https://youtu.be/ftP5BQh1-YM?t=2033) as a potential *black swan* - an existential threat for longevity - for Python.
	- “*Python hasn't ever had a consistent story for how I give my code to someone else, especially if that someone else isn't a developer and just wants to use my application.*”
- They announced the first release of PyOxidizer ([project](https://github.com/indygreg/PyOxidizer), [documentation](https://pyoxidizer.readthedocs.io/en/latest/)), an open source utility that aims to solve the Python application distribution problem!
- **PyOxidizer's marquee feature is that it can produce a single file executable containing a fully-featured Python interpreter, its extensions, standard library, and your application's modules and resources.** 
- You can have a single `.exe` providing your application. 
- Unlike other tools in this space which tend to be operating system specific, PyOxidizer works across platforms (currently Windows, macOS, and Linux - the most popular platforms for Python today).
- **PyOxidizer loads everything from memory and there is no explicit I/O being performed. When you** `**import**` **a Python module, the bytecode for that module is being loaded from a memory address in the executable using zero-copy.**
- This makes PyOxidizer executables [faster](https://pyoxidizer.readthedocs.io/en/latest/overview.html#faster-python-programs) to start and `import` - faster than a `python` executable itself!

**Brian #3:**  **Using** `changedir` **to avoid the need for** `src`

- I’ve been experimenting with combining flit, pytest, tox, and coverage for new projects.
- And in doing so, ran across a cool feature of tox that I didn’t know about before, `changedir`.
- It’s a feature of tox to allow you to run tests in a different directory than the top level project directory.
	- [tox changedir docs](https://tox.readthedocs.io/en/latest/config.html?highlight=changedir#conf-changedir)
	- [tox and pytest and changedir](https://tox.readthedocs.io/en/latest/example/pytest.html?highlight=changedir)
- I talk about this more in [episode 80 of Test & Code](https://testandcode.com/80).
	- As an example project I build yet another markdown converter using regular expressions.
	- This is funny to me, considering the recent cloudflare outage due to a single regular expression. https://blog.cloudflare.com/cloudflare-outage/
	- “Tragedy is what happens to me, comedy is what happens to you” - Mel Brooks approximate quote.

**Michael #4:** [**WebRTC and ORTC implementation for Python using asyncio**](https://github.com/aiortc/aiortc)

- [Web Real-Time Communication (WebRTC)](https://webrtc.org/) - WebRTC is a free, open project that provides browsers and mobile applications with Real-Time Communications (RTC) capabilities via simple APIs.
- [Object Real-Time Communication (ORTC)](https://ortc.org/) - ORTC (Object Real-Time Communications) is an API allowing developers to build next generation real-time communication applications for web, mobile, or server environments.
- The API closely follows its Javascript counterpart while using pythonic constructs:
	- promises are replaced by coroutines
	- events are emitted using `pyee.EventEmitter`
- The main WebRTC and ORTC implementations are either built into web browsers, or come in the form of native code.
- In contrast, the `aiortc` implementation is fairly simple and readable. 
	- Good starting point for programmers wishing to understand how WebRTC works or tinker with its internals. 
	- Easy to create innovative products by leveraging the extensive modules available in the Python ecosystem. 
	- For instance you can build a full server handling both signaling and data channels or apply computer vision algorithms to video frames using OpenCV.

**Brian #5:** [**Apprise - Push Notifications that work with just about every platform!**](https://github.com/caronc/apprise)

- listener suggestion
- cool shim project to allow multiple notification services in one app
- “*Apprise* allows you to send a notification to *almost* all of the most popular *notification* services available to us today such as: Telegram, Pushbullet, Slack, Twitter, etc.
	- One notification library to rule them all.
	- A common and intuitive notification syntax.
	- Supports the handling of images (to the notification services that will accept them).”
- supports
	- notification services such as discord, gitter, ifttt, mailgun, mattermost, MS teams, twitter, …
	- SMS notification through Twilio, Nexmo, AWS, D7
	- email notifications

**Michael #6:**  [**Websauna**](https://websauna.org) [**web framework**](https://websauna.org)

- Websauna is a full stack Python web framework for building web services and back offices with admin interface and sign up process https://websauna.org
- "*We have web applications 80% figured out. Websauna takes it up to 95%.*”
- Built upon Python 3, Pyramid, and SQLAlchemy.
- When to use it?
	- Websauna is focused on Internet facing sites where you have a public or private sign up process and an administrative interface. Its sweet spots include custom business portals and software-as-a-service products which are too specialized for off-the-shelf solutions.
- Benefits
	- Focus on core business logic as Websauna provides basic website building blocks like sign up and sign in. 
	- Low learning curve and friendly comprehensive documentation help novice developers
	- Emphasis is on meeting business requirements with reliable delivery times, responsiveness, consistency
	- Site operations is half the story. Websauna provides an automated deployment process and integrates with monitoring, security and other DevOps solutions.

**Extras**

Michael:

- [**Data driven Flask course**](https://training.talkpython.fm/courses/explore_flask/building-data-driven-web-applications-in-python-with-flask-sqlalchemy-and-bootstrap) is out!

Brian:

- Recent [Test & Code episodes](https://testandcode.com) were solo because I’m in the middle of a work move and didn’t want to schedule interviews around a crazy work schedule. However, that should settle down in July and I can get back to getting great guests on the show. But I’m also having fun with solo topics, so I’ll keep that in the mix.
	- upshot: if I’ve contacted you or you me about being on the show and you haven’t heard from me lately, give me a nudge with a DM or email or something.

**Jokes** 

- An SQL query goes into a bar, walks up to two tables and asks, 'Can I join you?'
- Not a joke, really, but along the lines of “comedy when it happens to you”.
	- Reset procedure for GE lightbulbs [theregister.co.uk/2019/06/20/ge_lightblulb_reset](https://www.theregister.co.uk/2019/06/20/ge_lightblulb_reset/)

