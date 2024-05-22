# Python Bytes 98
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Making Etch-a-Sketch Art With Python**](http://sunnybala.com/2018/09/10/python-etch-a-sketch.html)

- Really nice write up of methodically solving problems with simplifying the problem space, figuring out what parts need solved, grabbing off the shelf bits that can help, and putting it all together. 
- Plus it would be a fun weekend (or several) project with kids helping.
- Controlling the Etch-a-Sketch
	- Raspberry Pi, motors, cables, wood fixture
	- Software to control the motors
- Picture simplification with edge detection with Canny edge detection.
- Lines to motor control with path finding with [networkx](https://networkx.github.io/) library.
- Example results included in article.
- Pentium song: https://www.youtube.com/watch?v=qpMvS1Q1sos

**Michael #2:** [**Dropbox moves to Python 3**](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/)

- They just rolled out one of the largest Python 3 migrations ever
- Dropbox is one of the most popular desktop applications in the world
- Much of the application is written using Python. In fact, Drew’s very first lines of code for Dropbox were written in Python for Windows using venerable libraries such as pywin32.
- Though we’ve relied on Python 2 for many years (most recently, we used Python 2.7), we began moving to Python 3 back in 2015.
- If you’re using Dropbox today, the application is powered by a Dropbox-customized variant of Python 3.5. 
- Why Python 3?
	- Exciting new features: Type annotations and async & await
	- Aging toolchains: As Python 2 has aged, the set of toolchains initially compatible for deploying it has largely become obsolete
- Embedding Python
	- To solve build and deploy problem, we decided on a new architecture to embed the Python runtime in our native application.
	- Deep integration with the OS (e.g. smart sync) means native apps are required
- In future posts, we’ll look at:
	- How we report crashes on Windows and macOS and use them to debug both native and Python code.
	- How we maintained a hybrid Python 2 and 3 syntax, and what tools helped.
	- Our very best bugs and stories from the Python 3 migration.

**Brian #3: Resources for PyCon that relate to really any talk venue**

- [Speaking page](https://us.pycon.org/2019/speaking/)
- [Talk proposal tips and resources](https://us.pycon.org/2019/speaking/talks/)
- And the [poster session](https://us.pycon.org/2019/speaking/posters/). Way cooler than I originally understood.
- [Mariatta recently published her set of proposals](https://talk-talk-talk.readthedocs.io/en/latest/)
	- Nice clean examples that don’t look overwhelming
	- There’s also some links to examples at the talk proposal page.
- Related, on attending PyCon (or other technical conferences):
	- [You don't need to be a Pro @ Python to crack the code of Pycon](https://pybit.es/howto-crack-pycon.html)
		- missing: hang out and talk with, ask questions, and possibly help out with communities as part of the Expo.

**Michael #4:** [**Electron as GUI of Python Applications**](https://github.com/fyears/electron-python-example)

- via [Andy Bulka](http://www.andypatterns.com/)
- [**Electron Python**](https://github.com/fyears/electron-python-example) is a template of code where you use [Electron](https://electronjs.org/) (nodejs + chromium) as a GUI talking to Python 3 as a backend via zerorpc. Similar to [Eel](https://github.com/ChrisKnott/Eel) but much more capable e.g. you get proper native operating system menus — and users don’t need to have Chrome already installed.
- Needs to run zerorpc server and then start electron separately — can be done via the node backend
- using Electron as a GUI toolkit gets you
	- native menus, notifications
	- installers, automatic updates to your app
	- debugging and profiling that you are used to, using the Chrome debugger
	- ES6 syntax (a cleaner Javascript with classes, module imports, no need for semicolons etc.). Squint, look sideways, and it kinda looks like Python… ;-)
	- the full power of nodejs and its huge npm package repository
	- the large community and ecosystem of Electron
- How to package this all?
- [**Building a deployable Python-Electron App**](https://medium.com/@abulka/electron-python-4e8c807bfa5e) post by Andy Bulka
	- One of the great things about using Electron as a GUI for Python is that you get to use cutting edge web technologies and you don’t have to learn some old, barely maintained GUI toolkit
	- How much momentum, money, time and how many developer minds are focused on advancing web technologies? Answer: it’s staggeringly huge. 
	- Compare this with the number of people maintaining old toolkits from the 90’s e.g. wxPython? Answer: perhaps one or two people in their spare time. 
	- Which would you rather use?
	- Final quote: And someone please wrap Electron-Python into an IDE so that in the future all we have to do is click a ‘build’ button — like we could 20 years ago. :-)

**Brian #5:** [**pluggy: A minimalist production ready plugin system**](https://github.com/pytest-dev/pluggy) 

- [docs](https://pluggy.readthedocs.io/en/latest/)
- plugin management and hook system used by pytest
- A separate package to allow other projects to include plugin capabilities without exposing unnecessary state or behavior of the host project.

**Michael #6:** [**How China Used a Tiny Chip to Infiltrate U.S. Companies**](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies)

- via [Eduardo Orochena](https://twitter.com/EduardoOrochena/status/1047785560004341760)
- The attack by Chinese spies reached almost 30 U.S. companies, including Amazon and Apple, by compromising America’s technology supply chain, according to extensive interviews with government and corporate sources.
- In 2015, Amazon.com Inc. began quietly evaluating a startup called Elemental Technologies, a potential acquisition to help with a major expansion of its streaming video service, known today as Amazon Prime Video. (from Portland!)
- To help with due diligence, AWS, which was overseeing the prospective acquisition, hired a third-party company to scrutinize Elemental’s security
- servers were assembled for Elemental by [Super Micro Computer Inc.](https://www.bloomberg.com/quote/SMCI:US), a San Jose-based company (commonly known as Supermicro) that’s also one of the world’s biggest suppliers of server motherboards
- Nested on the servers’ motherboards, the testers found a tiny microchip, not much bigger than a grain of rice, that wasn’t part of the boards’ original design.
- Amazon reported the discovery to U.S. authorities, sending a shudder through the intelligence community. Elemental’s servers could be found in Department of Defense data centers, the CIA’s drone operations, and the onboard networks of Navy warships. And Elemental was just one of hundreds of Supermicro customers.
- During the ensuing top-secret probe, which remains open more than three years later, investigators determined that the chips allowed the attackers to create a stealth doorway into any network that included the altered machines. Multiple people familiar with the matter say investigators found that the chips had been inserted at factories run by manufacturing subcontractors in China.
- One government official says China’s goal was long-term access to high-value corporate secrets and sensitive government networks. No consumer data is known to have been stolen.
- American investigators eventually figured out who else had been hit. Since the implanted chips were designed to ping anonymous computers on the internet for further instructions, operatives could hack those computers to identify others who’d been affected.

**Extra:** 

- Michael's Async course [**talkpython.fm/async**](https://talkpython.fm/async) 

