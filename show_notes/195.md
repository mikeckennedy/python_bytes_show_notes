# Python Bytes 195
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [Test & Code](https://testandcode.com/) Podcast

**Michael #1:** [**watchdog**](https://github.com/gorakhargosh/watchdog)

- via Prayson Daniel
- Python API and shell utilities to monitor file system events.
- Example:
```
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
```
- Watchdog comes with an *optional* utility script called `watchmedo`
- try `$ watchmedo log` and see what happens in that folder.
- Why Watchdog? Compared to other similar libs

**Brian #2:** **Status code 418**

- Thanks Andy Howe for the suggestion
- Python 3.9 rc1 is out.
- One nice enhancement that has made it into 3.9, a fix for http library missing HTTP status code 418 “I’m a teapot”.
- [https://bugs.python.org/issue39507](https://bugs.python.org/issue39507) 
	- Title:  http library missing HTTP status code 418 "I'm a teapot"
- See also status code 418 is also supported by HTCPCP, Hyper Text Coffee Pot Control Protocol, https://tools.ietf.org/html/rfc2324  
	- 418 I'm a teapot
```
           Any attempt to brew coffee with a teapot should result in the error
           code "418 I'm a teapot". The resulting entity body MAY be short and
           stout.
```
- The only other unique HTCPCP code is 406
	- 406 Not Acceptable
```
           … In HTCPCP, this response code MAY be
           returned if the operator of the coffee pot cannot comply with the
           Accept-Addition request. Unless the request was a HEAD request, the
           response SHOULD include an entity containing a list of available
           coffee additions.
```
- This has been going on since 1998 and I'm just now hearing about it.
- A nice reference site: [httpstatuses.com](https://httpstatuses.com/)
- References
	- [https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol](https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol) 
	- [https://cstrobbe.github.io/WC3/TR/2008/RFC-htcpcp-in-rdf-20080401/](https://cstrobbe.github.io/WC3/TR/2008/RFC-htcpcp-in-rdf-20080401/)  
	- [https://cstrobbe.github.io/WC3/TR/2008/RFC-htcpcp-in-rdf-20080401/](https://cstrobbe.github.io/WC3/TR/2008/RFC-htcpcp-in-rdf-20080401/)

**Michael #3:** [**pydantic’s new Validation decorator**](https://pydantic-docs.helpmanual.io/usage/validation_decorator/)

- via Andy Shapiro 
- Built-in type checking for any function via a decorator
- easy to add for any public methods in a package
- pydantic uses lots of cython under the hood so it should be fast....
- The validate_arguments decorator allows the arguments passed to a function to be parsed and validated using the function's annotations before the function is called. 
- Under the hood this uses the same approach of model creation and initialization; it provides an extremely easy way to apply validation to your code with minimal boilerplate.
- Example:
```
    from pydantic import validate_arguments, ValidationError
    
    @validate_arguments
    def repeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
        b = s.encode()
        return separator.join(b for _ in range(count))
    
    a = repeat('hello', 3)
    print(a)
    #> b'hellohellohello'
    
    b = repeat('x', '4', separator=' ')
    print(b)
    #> b'x x x x'
    
    try:
        c = repeat('hello', 'wrong')
    except ValidationError as exc:
        print(exc)
        """
        1 validation error for Repeat
        count
          value is not a valid integer (type=type_error.integer)
        """
```

**Brian #4:** [**Building Python Extension Modules in Assembly**](https://github.com/tonybaloney/python-assembly-poc)

- Anthony Shaw
- From twitter announcement:
	- “After a series of highly questionable life decisions, my Python extension written in pure assembly is now on PyPI. [https://pypi.org/project/pymult/](https://t.co/hzXKlA471L?amp=1) it required writing an Assembly extension for distutils, I also added GitHub Actions support so its running CI/CD and testing with pytest”.
- A proof-of-concept to demonstrate how you can create a Python Extension in 100% assembly.
- Demonstrates:
	- How to write a Python module in pure assembly
	- How to write a function in pure assembly and call it from Python with Python objects
	- How to call the C API to create a PyObject and parse PyTuple (arguments) into raw pointers
	- How to pass data back into Python
	- How to register a module from assembly
	- How to create a method definition in assembly
	- How to write back to the Python stack using the dynamic module loader
	- How to package a NASM/Assembly Python extension with distutils
- The simple proof-of-concept function takes 2 parameters,
```
    >>> import pymult
    >>> pymult.multiply(2, 4)
    8  
```
- May need a few more test cases:
```
    >>> pymult.multiply(2, 3)
    6
    >>> pymult.multiply(-2, -3)
    6
    >>> pymult.multiply(-2, 3)
    4294967290
```
- Also, clearly Anthony has too much time on his hands. Just saying.

**Michael #5:** [**easy property**](https://github.com/salabim/easy_property)

- via Ruud van der Ham
- The easy_property module, developed by me, offers a more intuitive way to define a Python property with getter, setter, deleter, getter_setter and documenter decorators.
- Normally when you want to define a property that has a getter and a setter, you have to do something like
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @property
        def a(self):
            return self._a
    
        @a.setter
        def a(self, val):
            self._a = val
```
- IMHO, the @a.setter is a rather ugly decorator, and hard to remember. And there's no way to not define the getter.
- With the easy_property module, one can use the decorators
	- getter
	- setter
	- deleted
- as in:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @setter
        def a(self, val):
            self._a = val
        @deleter
        def a(self):
            print('delete')
            del self._a
```
- In contrast with an ordinary property, the order of definition of getter, setter and deleter is not important. And it is even possible to define a setter only (without a getter), just in case.
- With easy_property, you can even create a **combined getter/setter decorator**:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter_setter
        def a(self, val=None):
            if val is None:
                return self._a
            self._a = val
```
- Finally, it is possible to add a docstring to the property, with the @documenter decorator:
```
    Class Demo:
        def __init__(self, val):
            self.a = val
        @getter
        def a(self):
            return self._a
        @documenter:
        def a(self):
            return "this is the docstring of Demo.a"
```

Although this might not be always a good solution, I think in many cases this will make it easier and more intuitive to define properties.

**Brian #6:** [**Non Blocking Assertion Failures with pytest-check**](https://blog.testproject.io/2020/08/11/non-blocking-assertion-failures-with-pytest-check/)

- Ryan Howard wrote an article about a project of mine on the TestProject blog.
- I think it’s a first that someone else wrote an article about something I made. So that’s cool.
- Most tests do the “check” part with assert statements.
- The problem is assert stops after the first failure and you often want to check lots of stuff, and you want to see all the failures.
- Ryan has a good example with checking web pages using selenium and a simple example of wanting to check both the content of an element on the page, and the url.
- Cool use of pytest-check
- See also: 
	- [pytest-check](https://pypi.org/project/pytest-check/)
	- This plugin started as a discussion I started online in 2015 with a blog post: [Delayed assert / multiple failures per test](https://pythontesting.net/strategy/delayed-assert/).

Extras:

Brian

- PSA: There are no capital letters in pytest, even if it begins a sentence.

Michael

- [PyMC](https://docs.pymc.io/) core devs, we are currently planning [the first ever PyMCon](https://pymc-devs.github.io/pymcon/) (pronounce "PyMC ON", because "it is oooon" ;))! This is an asynchronous-first conference for the Bayesian community, with three goals:
	- Create a space and time for community members to meet each other and interact
	- Record and organize the expertise and experience around PyMC
	- Help folks find ways to contribute to PyMC, authentic to themselves
- urlify! [https://twitter.com/mkennedy/status/1292955438552506370](https://twitter.com/mkennedy/status/1292955438552506370) get it on github at [https://github.com/mikeckennedy/urlify](https://github.com/mikeckennedy/urlify)
- Thumbnails in the video player at talk python training

Joke:

- XKCD git - [**xkcd.com/1597**](https://xkcd.com/1597/) 
- “I used to do low-level programming. Then a product I bought told me, "No assembly required." Since then, I've been coding in Python.” - From Rueven Lerner, Inspired by Anthony Shaw

