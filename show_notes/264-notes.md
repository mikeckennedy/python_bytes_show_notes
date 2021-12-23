# Python Bytes 264

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**Kim van Wyk**](https://twitter.com/kim_vanwyk)


Michael #0: 

- **Take our survey**: Should we try to shorten the episodes? Please fill out [**the 3 question Google Form here**](https://forms.gle/LJ9uKkArwALDi9oX6)
- We’ll be taking a break so see you in two weeks.
- Also feedback / rate us in your podcast player app

**Brian #1:** [**Jupyter Games**](https://blog.jupyter.org/jupyter-games-cda20dc15a21)

- Thorsten Beier
- “Making their own tiny video games can be a great way for kids to learn programming in a playful matter.”
- For 2D physics-based games, Box2D, (written in C++), is a 2D rigid body simulation library
- One Python binding, pyb2d, is from Thorsten
- Game examples use Ipycanvas, Ipywidgets, and Ipyevents for a place to draw and input events.
- There are Box2D examples for physics simulations, like internal combustion and a wind tunnel.
- Game examples, with code, and not that much code
    - billiards
    - Angry Shapes (like Angry birds)
    - World of Goo homage
    - Rocket
    - Color Mixing (it’s oddly satisfying to play with, and it’s like 73 lines of code, including blank lines and docstring)
    - several more examples
- Demo games/examples in binder
- Being able to play with a game engine through Jupyter is kind of amazing. Cool teaching/learning tool.


**Michael #2:** [**Canary Tokens**](https://canarytokens.org/generate)

-  First, what are canaries (from Thinkst)?
- These tokens might be useful for finding fallout of Log4Shell
- But also generally useful

**Kim #3:** 

- [**pywinauto**](https://pywinauto.readthedocs.io/en/latest/) and [**PyAutoGUI**](https://pyautogui.readthedocs.io/en/latest/) - libraries for programmatically controlling a GUI-based tool. These can be very handy for simplifying the use of complex GUIs with dozens of options you need to set every time you run them and also for automating GUI tooling as part of a pipeline. 

**Brian #4:** [**A reverse chronology of some Python features**](https://snarky.ca/a-reverse-chronology-of-some-python-features/)

- Brett Cannon
- Partly for people wishing for the “good old days” of some old version of Python
- Brett recommends going down the list and stopping at the first feature you can’t live without. If you can’t go very far, better not complain about language bloat.
- I had to stop at 3.10, since I really like the new error messages.
- Here’s an abbreviated list of new features in different Python versions. (And I’m abbreviating it even more for the podcast)
    - Python 3.10
        - Better error messages, Union operator for types, paraenthesized context managers, match statement (pattern matching)
            - Brett notes that 
                - the match statement required a new parser for Python
                - the new parser made better error messages possible
                - so, you can’t toss pattern matching without being willing to give up better error messages
    - Python 3.9
        - dict support for `|` and `|=`, type hinting generics for built-in collections
    - Python 3.8
        - f-string support for `=`, `f``"``{val=}``"`, `:=` walrus operator (assignment expressions)
    - Python 3.7
        - dictionaries preserve insertion order, `breakpoint()`
    - Python 3.6
        - f-strings, (need we say more)
        - also underscores in numeric literals, async generators and comprehensions, preserving keyword argument order
    - … goes back to 3.1


**Michael #5:** [**Hyperactive GCs and ORMs/ODMs**](https://github.com/mikeckennedy/pythons-gc-and-orms)

- Does Python do extremely too many GCs for ORMs? Hint: yes
- During the execution of that single query against SQLAlchemy, without adjusting Python's GC settings, we get an extreme number of GC collections (1,859 GCs for a single SQLAlchemy query of 20k records).
- Our fix at [Talk Python](https://talkpython.fm) has been to increase the number of surviving allocations required to *force* a GC from 700 to 50,000.
- What can be done to improve this? Maybe someday Python will have an adaptive GC where if it runs a collection and finds zero cycles it backs off and if it starts finding more cycles it ramps up or something like that. 
- For now, test adjusting the thresholds
- Here are a few presentations / resources:
    - Michael’s [**presentation at Python Web Conf**](https://www.youtube.com/watch?v=A-3_Iw6KNCw) 2021
    - Talk Python [**Memory Deep Dive course**](https://talkpython.fm/memory)


    allocations, gen1, gen2 = gc.get_threshold()
    allocations = 50_000 # Start the GC every 50K not 700 surviving container allocations.
    gc.set_threshold(allocations, gen1, gen2)


**Kim #6:**

- **[DockerSlim](https://github.com/docker-slim/docker-slim)**- A tool to reduce the size and improve the security of Docker images. I’ve used it a little and got some 1Gb Ubuntu-based images down to 50Mb and that was barely scratching the surface.

**Extras** 


Michael:

- Emojis for comments
![](https://paper-attachments.dropbox.com/s_17160480C0A88546D554F06AFA46303E561FC99B09E5DA89035E29522B6126C1_1640119124175_Screen+Shot+2021-12-21+at+12.38.35+PM.png)


Kim: 

- `python -m http.server` - a small reminder to people that this is a quick way to get files off a Python-equipped system by standing up a simple web server.
- **[Mess with DNS](http://messwithdns.net/)** - [Julia Evans](https://jvns.ca/) released this really impressive learning tool last week to let people explore DNS settings without breaking real sites.
- **[Magit](https://magit.vc/)** - a slightly tongue-in-cheek addition to last week’s discussion on git via both CLI and by mashing buttons in VS Code. Anyone using emacs should strongly consider magit for git - I’ve kept emacs open even while trying to use other editors because I find magit so indispensable.

I’ve included these just as small items off the top of my head that may or may not be worth a mention.

**Joke:** 

- We use cookies candle (and [**I don’t care about cookies extension**](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/))
![](https://paper-attachments.dropbox.com/s_17160480C0A88546D554F06AFA46303E561FC99B09E5DA89035E29522B6126C1_1640195194820_candle.jpg)

- [**Little Bobby Jindi**](https://twitter.com/btskinn/status/1473308223319023625)
- And more [**Log4Shell memes**](https://log4jmemes.com/)

![https://dl.airtable.com/.attachments/2cbdda337b90bcff7d5b966390dc24de/97435cba/FHDe6KdXwAUgK8t](https://dl.airtable.com/.attachments/2cbdda337b90bcff7d5b966390dc24de/97435cba/FHDe6KdXwAUgK8t)

