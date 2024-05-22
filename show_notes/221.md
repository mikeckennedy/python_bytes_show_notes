# Python Bytes 221

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: [**Brett Cannon**](https://twitter.com/brettsky)

**Brian #1:** **Keeping up with Rich**

- Will McGugan has been building [Rich](https://github.com/willmcgugan/rich)
- It looks like it’s on its way to becoming a full fledged TUI (text user interface)
- December: [Live view](https://rich.readthedocs.io/en/latest/live.html): no blog post on that, I don’t think.
- January:  [Tree view](https://rich.readthedocs.io/en/latest/tree.html): [Rendering a tree view in the terminal with Python and Rich](https://www.willmcgugan.com/blog/tech/post/rich-tree/)
- February: [Layouts](https://rich.readthedocs.io/en/latest/layout.html):  [Building Rich terminal dashboards](https://www.willmcgugan.com/blog/tech/post/building-rich-terminal-dashboards/)
	- fun [fullscreen.py](https://github.com/willmcgugan/rich/blob/master/examples/fullscreen.py) example, uses Live view
- Also, `python -m rich` will display a demo screen that shows tons of the stuff that Rich can do
- Many of the features also have a stand alone demo built in, like:
```
    $ python -m rich.layout
    $ python -m rich.tree
    $ python -m rich.live
```
- Although I haven’t figured out how to kill the live demo. it doesn’t seem to time out, and it eats Ctrl-C in my terminal.
- I’d really like to use Rich for interactive stuff, like keyboard interrupts and arrow keys and tab and such. It’d be fun.
- Which brings me to the bottom right corner of the `python -m rich` output. It includes a [GitHub Sponsor link for Will](https://github.com/sponsors/willmcgugan).  
- Also, Will, unless it’s a contradiction to RTD TOS, I think you should include a Sponsor link in the [Rich documentation](https://rich.readthedocs.io/en/latest/). 
- Let’s convince Will to make Rich a full TUI.

**Michael #2:** [**12 requests per second**](https://suade.org/dev/12-requests-per-second-with-python/)

- If you take a look around the blogosphere at various benchmarks for Python web frameworks, you might start to feel pretty bad about your own setup.
- The incredible work of the guys at [magic stack](https://magic.io/blog/uvloop-blazing-fast-python-networking/), getting **100,000 requests per second** from [uvloop](https://github.com/MagicStack/uvloop) in a single thread.
- There’s the FastAPI benchmarks
- Even more mind-blowing is [Japronto](https://github.com/squeaky-pl/japronto) which claims an insane **1.2 million requests per-second** in a single thread
- But what about your “boring” Flask or Django app? And how realistic are these benchmarks? Usually, not very.
- Here’s an article diving into this for a “proper” ORM style app.
- 12 - 80 requests per sec: Both our sync workers are now hitting a blazing **12** **requests per second** 😅 Using async workers seems to help a lot, but oddly Sanic struggles here.
- Be sure to run in prod on a “real” server setup (nginx + gunicorn or whatever)
- Compare this to Talk Python Training - Python 3, uWSGI, Pyramid, MongoDB, $20/mo server
- Get around 125 requests/sec @ 100ms response time on a single server.
- More realistically, we can handle about 10,000-20,000 concurrent “realistic” users before performance suffers.

**Brett #3:** [**Python Launcher for Unix**](https://crates.io/crates/python-launcher) **reaches RC (probably 😉)**

- Exclusive! 😁
- Started right after PyCon US 2018
- Implemented in Rust (it’s my “good size” Rust learning project)
- The Python Launcher for Windows works by:
	- Checking the shebang line
	- If `VIRTUAL_ENV` is set
	- Find the newest `pythonX.Y` version/command on `$PATH`
	- Can specify specific versions via e.g. `-3` or `-3.9`
	- `PY_PYTHON` and `PY_PYTHON3` environment variables supported
	- `--list` also works
	- Can use `PYLAUNCH_DEBUG` to see what the tool is doing
	- `--help` covers all of this
- Unix version differs in the preference of shebang versus `VIRTUAL_ENV` over shebang
	- Figure on Unix you will `chmod` the executable bit if you truly care about the shebang
	- I also assume at this point people will use entry points if they really want to tie something to an interpreter version
	- How often do people peg their scripts to a specific Python version instead of `python2` or `python3`?
	- What do people think of this logic swap (hence the “probably”)?
- Unix bonus feature: will automatically use any virtual environment found in `.venv` in the working directory (and no, what directory is considered is not configurable 😁)
- All of this has made it `py` my preferred way of running Python on my machine
- Really useful with [Starship](https://starship.rs/) and its [Python support](https://starship.rs/config/#python) (does away with the big “Tip” box they have for the `python_binary` setting)


**Michael #4:** [**Build a text editor with Python and curses**](https://wasimlorgat.com/editor)

- `[curses](https://docs.python.org/3/library/curses.html)` is a library to avoid having to deal with low level issues like efficiently painting to the terminal screen and receiving user input.
- a barebones `curses` application
```
    import curses
    
    def main(stdscr):
        while True:
            k = stdscr.getkey()
            if k == "q":
                sys.exit(0)
    
    if __name__ == "__main__":
        curses.wrapper(main)
```
- Clear the screen with `stdscr.erase()`
- Adding text (a line of text) to the screen: `stdscr.addstr(row, 0, line)`
- The article covers interesting topics like a “view” into the file that fits the screen and a cursor you move around with arrow keys

**Brett #5:** [**Pattern matching**](https://mail.python.org/archives/list/python-committers@python.org/message/SQC2FTLFV5A7DV7RCEAR2I2IKJKGK7W3/) **and accepting change in Python**

- The “5-barrel foot-gun” in the room (to use Brian’s words from the last episode 😉)
- Usual places have people commenting from “I like this” to screaming bloody murder
- I think there are many “new” people to the language who don’t know Python prior to Python 3, so they don’t realize how much things used to regularly change in the language
- Pattern matching was **very** much debated publicly, so this wasn’t a secret (and I’m sorry if you didn’t have the time to participate, but Python development doesn’t even always wait for me and I’m on the SC, so …)
	- The 2020 SC also announced publicly the possibility of this back in December with their recommendation to accept the PEP(s)
- Also usual comments of “why did they waste their time on *that*?!? Go fix packaging!” (and it’s almost always packaging 🙄)
	- This is open source: some people wanted to put their personal time and effort into trying to get pattern matching into Python, so that’s what they did
	- If you want to help with Python’s packaging ecosystem, you can do so but trying to tell people what they “need” or “should” do with their time is simply rude
- History repeats itself: every change is unwelcome unless it solves *your* problem
	- Pattern matching very much opens up opportunities for certain problems that were not easily possible before, e.g. parsers and compilers are classics (and hence why they are so often implemented in functional languages)
	- I don’t think you will see this in nearly every code base like you do e.g. list comprehensions
	- E.g. I’m sure data scientists aren’t saying any of this since they got `@`, right? 😉
- People also claiming it isn’t Pythonic need to note that Guido helped drive this
	- Do *you* know what is Pythonic better than Guido? 😉
	- He might not be BDFL anymore, but that doesn’t mean he still doesn’t have good design sense, i.e. if you like Python up to this point then trust Guido’s gut that this is a good thing
	- “In Guido We Trust” (you can even [get it on a mug](https://nerdlettering.com/collections/mugs-for-python-developers/products/in-guido-we-trust-python-mug-black) 😉)
- **If** you use pattern matching in **real-world code** and have feedback to provide with enough time to consider it **before b1**, then please let python-dev know
	- E.g. there is a chance to change the meaning of `_` if that is truly your biggest hang-up
- This will all probably become a blog post
	- Running title is “The Social Contract of Open Source”
	- These kinds of attitudes against people trying their best to make things better for folks is what led to Guido retiring from being the BDFL in the first place, me having to take a month off from open source every year, etc.
- Aside: more influenced by Scala than by Haskell (not sure where Michael and some other people I’ve seen online got the idea Haskell played into this)
	- Did you know we got list comprehensions from Haskell?

**Brian #6:** [**A Quick Intro to Structural Pattern Matching in Python**](https://www.python.org/dev/peps/pep-0636/#appendix-a-quick-intro)

- aka the “switch” statement. I mean, the “match” statement.
- Also known as PEP 636, [Appendix A — Quick Intro](https://www.python.org/dev/peps/pep-0636/#appendix-a-quick-intro)
	- [courtesy Guido van Rossum](https://github.com/gvanrossum/patma/blob/master/README.md)
- This finally helps me to get my head around simple uses of the new syntax for 3.10
- simple form:
```
    def http_error(status):
        match status:
            case 400:
                return "Bad request"
            case 401:
                return "Unauthorized"
            case 403:
                return "Forbidden"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case _: # _ acts as a wildcard and never fails to match
                return "Something else"
```
- you can combine several matches using `|`
```
    case 401|403|404:
                return "Not allowed"
```
- Patterns can look like unpacking assignments, and can be used to bind variables:

```
    # The subject is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
```

- This is actually the tricky one. x and/or y can change values after this statement if their case is hit.
- More details in the article, er, appendix.
- It’s still going to take a while to get used to this, but this appendix is a good start.

**Joke**

## [true happiness](https://devhumor.com/media/true-happiness)




