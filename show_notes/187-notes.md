# Python Bytes 187
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

Brian #1: [**LEGO Mindstorms Robot Inventor  supports Python**](https://www.lego.com/en-gb/aboutus/news/2020/june/lego-mindstorms-robot-inventor)

- Past
	- NXT 2006
	- NXT 2.0 2009
	- EV3 2013 (plus, weird post apocalypse thing going on)
- Robot Inventor will be available Autumn 2020 (not sure what that means).
	- Controllable with both Scratch and Python
	- Great updates to help with STEM education
	- Instructions for 5 different robots
	- interesting:
		- 5x5 LED matrix
		- 6 input/output ports for connecting a variety of sensors and motors.
		- 6 axis gyro/accelerometer
		- color sensor
		- distance sensor
		- and Python!
		- Can be programmed with Windows & Mac, of course. But also iOS & Android tablets and phones and even some FireOS devices.
- Related: [MicroscoPy](https://github.com/IBM/MicroscoPy) - IBM open source, motorized, modular microscope built using LEGO bricks, Arduino, Raspberry Pi and 3D printing.

Michael #2: [**Step-by-step guide to contributing on GitHub**](https://www.dataschool.io/how-to-contribute-on-github/)

- by Kevin Markham
- Want to contribute to an open source project? Follow this detailed visual guide to make your first contribution TODAY
- Although there are other guides like it out there, mine is (1) up-to-date with the latest GitHub interface, (2) much more detailed, and (3) highly visual. Includes 16 annotated screenshots + 2 workflow diagrams.
- The only prerequisite is that the reader has a tiny bit of Git knowledge. They don't even have to be a great coder, because what I suggest is that they start by fixing a typo or broken link in the documentation. That way they can focus on learning the contribution workflow!
- Steps:
- **choose a project to contribute to**
- **fork the project**
- **clone your fork locally**
- **load your local copy in an editor**
- **make sure you have an "origin" remote**
- **add the project repository as the "upstream" remote**
- **pull the latest changes from upstream into your local repository**
- **create a new branch**
- **make changes in your local repository**
- **commit your changes**
- **push your changes to your fork**
- **create the pull request**
- **review the pull request**
- **add more commits to your pull request**
- **discuss the pull request**
- **delete your branch from your fork**
- **synchronize your fork with the project repository**
- Nice Tips for contributing code section too.

Brian #3: [**sneklang**](https://sneklang.org/)

- Snek: A Python-inspired Language for Embedded Devices
- An even smaller footprint than MicroPython or CircuitPython
- Can’t wait for Robot Inventor? Snek supports Lego EV3.
- “Snek is a tiny embeddable language targeting processors with only a few kB of flash and ram. … These processors are too small to run [MicroPython](https://micropython.org/).”
- Can develop using Mu editor
- Custom Snekboard runs either Snek or CircuitPython.
- Or run Snek on Lego EV3.
- Smaller language than Python, but intended to have all learning of Snek transferable to later development with Python.
- “The goals of the Snek language are:
	- **Text-based.** A text-based language offers a richer environment for people comfortable with using a keyboard. It is more representative of real-world programming than building software using icons and a mouse.
	- **Forward-looking.** Skills developed while learning Snek should be transferable to other development environments.
	- **Small.** This is not just to fit in smaller devices: the Snek language should be small enough to teach in a few hours to people with limited exposure to software.
- Snek is Python-inspired, but it is not Python. It is possible to write Snek programs that run under a full Python system, but most Python programs will not run under Snek.”

Michael #4: [**Oh sh*t git**](https://wizardzines.com/zines/oh-shit-git/)

- via Andrew Simon, by Julia Evans
- Does cost $10, no affiliations
- This zine explains git fundamentals (what’s a SHA?)
- How to fix a lot of common git mistakes (I committed to the wrong branch!!).
- Fundamentals
- Mistakes and how to fix them
- Merge conflicts
- Committed the wrong file
- Going back in time

Brian #5: [**Why I don't like SemVer anymore**](https://snarky.ca/why-i-dont-like-semver/)

- Brett Cannon
- Interesting thoughts on SemVer
	- SemVer isn't as straightforward as it sounds; we don't all agree on what a major, minor, or micro change really is.
		- Is adding a depreciation warning a bug fix? or a major interface break?
		- What if projects depending on your project have CI with warnings as errors? 
	- Your version number represents your branching strategy, so you choose a versioning scheme that's appropriate your branching and release strategy.
	    - While maintaining multiple branches, x.y.z might make sense:
		    - x - current release
		    - x.y - current development
		    - x.y.z - bug fixes
		    - x+1 - crazy new stuff
    - If you aren’t maintaining 3+ branches at all times, that might be overkill
    - Maybe x.y is enough
    - Maybe just x is enough
	- Rely on CI, potentially on a cron job, to detect when a project breaks for you instead of leaving it up to the project to try and make that call based on their interpretation of SemVer; will inevitably disagree
	- Remember to pin your dependencies in your apps if you really don't want to have to worry about a dependency breaking you unexpectedly
	- Libraries/packages should be setting a floor, and if necessary excluding known buggy versions, but otherwise don't cap the maximum version as you can't predict future compatibility

Michael #6: [**git fame**](https://github.com/casperdcl/git-fame)

- via Björn Olsson
- Pretty-print `git` repository collaborators sorted by contributions.
- Install via pip: `pip install --user git-fame`
- Register with git: `git config --global alias.fame "!python -m gitfame``"`
- Run in a repo directory: `git fame`
- Get a table of contributors including: Author, Lines of Code, Files, Distribution (stats), sorted by most contributions.

Extras:

Patreon Shoutout:

- We have 26 supporters at https://www.patreon.com/pythonbytes
- Many donate $1 a month, and that’s awesome.
- A few go above and beyond with more than that:
- Special shout out to those above a buck:
	- Brent Kincer
	- Brian Cochrane
	- Bert Raeymaekers
	- Richard Stonehouse
	- Jeff Keifer 
- Thank you

Michael: 

- `__pypackages__` [**follow up**](https://twitter.com/kushaldas/status/1261307240255913985) from Kushal Das

Joke:

[https://www.commitstrip.com/en/2017/02/28/definitely-not-lazy/](https://www.commitstrip.com/en/2017/02/28/definitely-not-lazy/)