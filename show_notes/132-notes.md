# Python Bytes 132
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**History of CircuitPython**](http://pyfound.blogspot.com/2019/05/scott-shawcroft-history-of-circuitpython.html)

- PSF blog, A. Jesse Jiryu Davis
- Adafruit hired Scott Shawcroft to port MicroPython to their SAMD21 chip they use on many of their boards.
- CircuitPython is a friendly fork of MicroPython. Same licensing, and they share improvements back and forth.
- “MicroPython customizes its hardware APIs for each chip family to provide speed and flexibility for hardware experts. Adafruit’s audience, however, is first-time coders. Shawcroft said, “Our goal is to focus on the first five minutes someone has ever coded.” “
- “Shawcroft aims to remove all roadblocks for beginners to be productive with CircuitPython. As he demonstrated, CircuitPython auto-reloads and runs code when the user saves it; there are two more user experience improvements in the latest release. First, serial output is shown on a connected display, so a program like `print("hello world")` will have visible output even before the coder learns how to control LEDs or other observable effects.”
- Related: [CircuitPython 4.0.0 released](https://blog.adafruit.com/2019/05/20/circuitpython-4-0-0-released/) 

**Michael** **#2**: [**R Risks Python Swallowing It Whole: TIOBE**](https://insights.dice.com/2019/05/09/r-risks-python-swallowing-whole-tiobe/)

-  Is the R programming language in serious trouble? According to the latest update of the TIOBE Index, the answer seems to be “yes.”
- R has finally tumbled out of the top 20 languages
- “It seems that there is a consolidation going on in the statistical programming market. Python has become the big winner.”
- Briefly speculates why is Python (which ranked fourth on this month’s list) winning big in data science? My thought: Python is a *full spectrum language* with solid numerical support.

**Brian#3:** [**The Missing Introduction To Containerization**](https://medium.com/faun/the-missing-introduction-to-containerization-de1fbb73efc5)

-  Aymen El Amri
- Understanding containerization through history
	- chroot jail, 1979, allowed isolation of a root process and it’s children from the rest of the OS, but with no security restrictions.
	- FreeBSD Jail, 2000, more secure, also isolating the file system.
	- Linux VServer, 2001, added “security contextes” and used new OS system-level virtualization. Allows you to run multiple Linux distros on a single VPS.
	- Oracle Solaris Containers, 2004, system resource controls and boundary separation provided by “zone”.
	- OpenVZ, 2005, OS-level virtualization. Used by many hosting companies to isolate and sell VPSs.
	- Google’s CGroups, 2007, a mechanizm to limit and isolate resource usage. Was mainlained into Linux kernel the same year.
	- LXC, Linux Containers, 2008, Similar to OpenVX, but uses CGroups.
	- CloudFoundry’s Warden, 2013, an API to manage environments.
	- Docker, 2013, os-level virtualization
	- Google’s LMCTFY (Let me contain that for you), 2014, an OSS version of Google’s container stack, providing Linux application containers. Most of this tech is being incorporated into libcontainer.
	- “Everything at Google runs on containers. There are [more than 2 billion containers](https://speakerdeck.com/jbeda/containers-at-scale) running on Google infrastructure every week.”
	- CoreOS’s rkt, 2014, an alternative to Docker.
- Lots of terms defined
    - VPS, Virtual Machine, System VM, Process VM, …
- OS Containers vs App Containers
- Docker is both a Container and a Platform


- This is halfway through the article, and where I got lost in an example on creating a container sort of from scratch. I think I’ll skip to a Docker tutorial now, but really appreciate the back story and mental model of containers.


**Michael #4:** [**Algorithms as objects**](https://gieseanw.wordpress.com/2019/05/10/algorithms-as-objects/)

- We usually think of an algorithm as a single function with inputs and outputs. 
- Our algorithms textbooks reinforce this notion. 
- They present very concise descriptions that neatly fit in half of a page. 
- Little details add up until you’re left with a gigantic, monolithic function
- monolithic function lacks **readability**
- the function also lacks **maintainability**
- *Nobody* wants to touch this code because it’s such a pain to get any context
- Complex code requires **abstractions**
- How to tell if your algorithm is an object
- **Code smell #1. It’s too long or too deeply nested**
- **Code smell #2. Banner comments**
- **Code smell #3. Helper functions as nested closures, but it’s still too long**
- **Code smell #4. There are actual helper functions, but they shouldn’t be called by anyone else**
- **Code smell #5. You’re passing state between your helper functions**
- Write your algorithm as an object
- Refactoring a monolithic algorithm into a class improves **readability**, which is is our #1 goal.
- Lots of concrete examples in the article

**Brian #5:** [**pico-pytest**](https://gitlab.com/obestwalter/pico-pytest)

- Oliver Bestwalter
- Super tiny implementation of pytest core. [25 lines](https://gitlab.com/obestwalter/pico-pytest/blob/master/src/pico_pytest/pytest.py)
- My original hand crafted test framework was way more code than that, and not as readable.
- This is good to look at to understand the heart of what test frameworks do
	- find test code
	- run it
	- mark any exceptions as failures
- Of course, the bells and whistles added in the full implementation are super important, but this is the heart of what is happening.

**Michael #6:** [**An Introduction to Cython, the Secret Python Extension with Superpowers**](http://okigiveup.net/an-introduction-to-cython/)

- Cython is one of the best kept secrets of Python. 
- It extends Python in a direction that addresses many of the shortcomings of the language and the platform, such as execution speed, GIL-free concurrency, absence of type checking and not creating an executable.
- Number of widely used packages that are written in it, such as [spaCy](https://github.com/explosion/spaCy), [uvloop](https://github.com/MagicStack/uvloop), and significant parts of [scikit-learn](https://github.com/scikit-learn/scikit-learn), [Numpy](http://www.numpy.org/) and [Pandas](https://pandas.pydata.org/).
- Cython makes use of the architectural organization of Python by translating (or 'transpiling', as it is now called) a Python file into the C equivalent of what the Python runtime would be doing, and compiling this into machine code.
- Can sometimes avoid Python types altogether (e.g. `sqrt` function)
- C arrays versus lists:  Python collection types (list, dict, tuple and set) can be used as a type in `cdef` functions. The problem with the list structure, however, is that it leads to Python runtime interaction, and is accordingly slow
- Nice article for getting started and motivation. But I didn’t see Python type annotations in play (they are now supported)

**Extras**

Brian: 

-  [**The Price of the Hallway Track**](https://hynek.me/articles/hallway-track/) **- Hynek**
	- It’s lame to speak to an empty room, so go to some talks, and lean toward less known speakers. Definitely on my todo list for next year.
- [**Who put Python in the Windows 10 May 2019 Update?**](https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/) **- Steve Dower**
    - more back story

Michael: 

- Little development board to production via Crowd Supply: [**The TinyPICO**](https://www.crowdsupply.com/unexpected-maker/tinypico) is an ESP32-based board that's, well, tiny ;) but packs a pretty significant punch...and it's been designed from day 1 to have first-class MicroPython support!  via [matt_trentini](https://twitter.com/matt_trentini)
- [**PyCon 2019 Reflections**](https://automationpanda.com/2019/05/20/pycon-2019-reflections/) by Automation Panda
- Python Bytes (yeah, us!) has a [**Patreon page**](https://www.patreon.com/pythonbytes).
- Upcoming webcast: [**10 Tools and Techniques Python Web Developers Should Explore**](https://www.wintellect.com/webinar/10-tools-and-techniques-python-web-developers-should-explore/)

**Jokes** 

- What do you call eight hobbits? A hobbyte.
- Two bytes meet. The first byte asks, 'Are you ill?' The second byte replies, 'No, just feeling a bit off.’
- OR: What is Benoit B. Mandelbrot's middle name? Benoit B. Mandelbrot.
