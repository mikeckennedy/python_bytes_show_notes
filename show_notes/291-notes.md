# Python Bytes 291

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Michael #1:** [**Python License tracker**](https://wagenrace.github.io/python_dep_frontend/)

- by Tom Nijhof/Nyhof
- Every package depends on other package with sometimes different licenses.
- Tom made a tool to find out what licenses you all need for a project:
- PyTest alone needs 4 different licenses for itself and its dependencies.
- Tensorflow is even worst

**Brian #2:** [**undataclass**](https://www.pythonmorsels.com/undataclass/)

- Trey Hunner
- As a teaching aid, and to show how much dataclasses do for you, this is a module and an application that converts dataclasses to normal classes, and fills in all of the dunder methods you need.
- Example in app:

```
from dataclasses import dataclass
    
    @dataclass()
    class Point:
        x: float
        y: float
        z: float
```

- Converts to

```
class Point:
        __match_args__ = ('x', 'y', 'z')
    
        def __init__(self, x: float, y: float, z: float) -> None:
            self.x = x
            self.y = y
            self.z = z
        
        def __repr__(self):
            cls = type(self).__name__
            return f'{cls}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
        
        def __eq__(self, other):
            if not isinstance(other, Point):
                return NotImplemented
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
```

- Note on `NotImplemented`:
    - It just means, “I don’t know how to compare this”, and Python will try `__eq__` on the `other` object. If that also raises `NotImplemented`, a `False` is returned. 
- The default is the above with `@dataclass(frozen=True, slots=True)` and adds the methods:
    - `fronzen=True` gives you implementations of `__hash__`, `__setattr__`, `__delattr__`, `__getstate__`, `__setstate__`, 
        - Essentially raises exception if you try to change the contents, and makes your objects hashable. 
    - `slots=True` adds the line: `__slots__ = (``'``x',` `'``y``'``,` `'``z``'``)`.
        - This disallows adding new attributes to objects at runtime. See [Python docs](https://docs.python.org/3.10/reference/datamodel.html#slots)
- Trey wrote two posts about it:
    - [Appreciating Python's match-case by parsing Python code](https://www.pythonmorsels.com/match-case-parsing-python/)
    - [How I made a dataclass remover](https://www.pythonmorsels.com/making-a-dataclass-remover/)
- Turns out, this is a cool example for AST and structural pattern matching.
- Notes from the “how I made..” article:
- "I used some tricks I don't usually get to use in Python. I used:
1. Many **very hairy** `**match**`**-**`**case**` **blocks** which replaced even hairier `if`-`elif` blocks
2. A **sentinel object** to keep track of a location that needed replacing
3. Python's `**textwrap.dedent**` **utility**, which I feel should be more widely known & used
4. **slice assignment** to inject one list into another
5. The `ast` module's `unparse` function to convert an abstract syntax tree into Python code”

**Michael #3:** [**Qutebrowser**](https://qutebrowser.org)

- via Martin Borus
- Qutebrowser is a keyboard-focused browser with a minimal GUI." 
- It's Python powered 
- Whats more important - doesn't force you to use it's Vim-based shortcuts, the mouse
- still works. But you usually don't need it: Because on any page, a keypress on the "f" key will show, you every clickable think and a letter combination to enter to click this.

**Brian #4:** **asyncio and web applications**

- A collection of articles
- [Quart is now a Pallets project](https://palletsprojects.com/blog/quart-pallets/)
    - P G Jones, maintainer of Quart and Hypercorn
    - “Quart, an ASGI re-implementation of the Flask API has joined the Pallets organization. This means that future development will be under the Pallets governance by the Pallets maintainers.
    - Our long term aim is to merge Quart and Flask to bring ASGI support directly to Flask. 
    - “When to use Quart?”
        - “Quart is an ASGI framework utilising async IO throughout, whereas Flask is a WSGI framework utilising sync IO. It is therefore best to use Quart if you intend to use async IO (i.e. async/await libraries) and Flask if not. Don't worry if you choose the 'wrong' framework though, as Quart supports sync IO and Flask supports async IO, although less efficiently.”
- [Using async and await](https://flask.palletsprojects.com/en/2.1.x/async-await/), from Flask docs
    - Flask has some support of async/await since Flask 2.0
    - But it’s still a WSGI application.
    - “Deciding whether you should use Flask, Quart, or something else is ultimately up to understanding the specific needs of your project.”
- [Should You Use AsyncIO for Your Next Python Web Application?](https://www.laac.dev/blog/should-you-use-asyncio-next-python-web-application/)
    - Steven Pate
    - A cool “brief history of Python web server interfaces”
    - Discussion of the Python servers and frameworks for both WSGI and ASGI
    - Recommendation: Do you need async? “… most people don’t. WSGI servers and frameworks are usually performant enough.”

**Extras** 

Michael:

- Python Web Conf Talk: [**HTMX + Flask: Modern Python Web Apps, Hold the JavaScript**](https://www.youtube.com/watch?v=-qU3cfU35OE)
- [browserosaurus](https://github.com/will-stone/browserosaurus)

**Joke:**  [**Understanding JavaScript**](https://twitter.com/PR0GRAMMERHUM0R/status/1542855590753583104)

**Joke:** [**Where do you see yourself in 5 years? (2022-04-21)**](https://www.neta.mk/archive)

![](https://paper-attachments.dropbox.com/s_2B2DA5ABAB520A067C7A455F46C098AF9EB6B5C867D3A5122B548BFAFDACC225_1657115556852_image.png)

