# Python Bytes 159

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

Michael #1: [**Final type**](https://www.python.org/dev/peps/pep-0591/)

- PEP 591 -- Adding a final qualifier to typing
- This PEP proposes a "final" qualifier to be added to the typing module---in the form of a final decorator and a Final type annotation---to serve three related purposes:
	- Declaring that a method should not be overridden
	- Declaring that a class should not be subclassed
	- Declaring that a variable or attribute should not be reassigned
- Some situations where a final class or method may be useful include:
	- A class wasn’t designed to be subclassed or a method wasn't designed to be overridden. Perhaps it would not work as expected, or be error-prone.
	- Subclassing or overriding would make code harder to understand or maintain. For example, you may want to prevent unnecessarily tight coupling between base classes and subclasses.
	- You want to retain the freedom to arbitrarily change the class implementation in the future, and these changes might break subclasses.

```
    # Example for a class:
    from typing import final
    
    @final
    class Base:
        ...
    
    class Derived(Base):  # Error: Cannot inherit from final class "Base"
        ...
```

And for a method:

```
    class Base:
        @final
        def foo(self) -> None:
            ...
    
    class Derived(Base):
        def foo(self) -> None:  # Error: Cannot override final attribute "foo"
                                # (previously declared in base class "Base")
            ...
```

- It seems to also mean `const`

```
    RATE: Final = 3000

class Base:

        DEFAULT_ID: Final = 0
    
    RATE = 300  # Error: can't assign to final attribute
    Base.DEFAULT_ID = 1  # Error: can't override a final attribute
```

**Brian #2:** [**flit 2**](https://flit.readthedocs.io/en/latest/history.html)

Michael #3: [**Pint**](https://pint.readthedocs.io/en/0.9/)

- via Andrew Simon
- Physical units and builtin unit conversion to everyday python numbers like floats. 
- Receive inputs in different unit systems it can make life difficult to account for that in software. 
- Pint handles the unit conversion automatically in a wide array of contexts – Can add 2 meters and 5 inches and get the correct result without any additional work. 
- The integration with numpy and pandas are seamless, and it’s made my life so much simpler overall. 
- [Units and types of measurements](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt)
- Think you need this? How about the Mars Climate Orbiter 
	- *The MCO MIB has determined that the root cause for the loss of the MCO spacecraft was the failure to use metric units in the coding of a ground software file, “Small Forces,” used in trajectory models. Specifically, thruster performance data in English units instead of metric units was used in the software application code titled SM_FORCES (small forces).*

**Brian #4:** [**8 great pytest plugins**](https://opensource.com/article/18/6/pytest-plugins)
- Jeff Triplett

Michael #5: [11 new web frameworks](https://deepsource.io/blog/new-python-web-frameworks/)

- via [LuisCarlos Contreras](https://twitter.com/chui_k)

1. **Sanic** [flask like] - a web server and web framework that’s written to go fast. It allows the usage of the async / await syntax added in Python 3.5
2. **Starlette** [flask like] - A lightweight [ASGI](https://asgi.readthedocs.io/en/latest/) framework which is ideal for building high performance `asyncio` services, designed to be used either as a complete framework, or as an ASGI toolkit.
3. **Masonite** - A developer centric Python web framework that strives for an actual batteries included developer tool with a lot of out of the box functionality. Craft CLI is the edge here.
4. **FastAPI** - A modern, high-performance, web framework for building APIs with Python 3.6+ based on standard Python type hints.
5. **Responder** - Based on Starlette, Responder’s primary concept is to bring the niceties that are brought forth from both Flask and Falcon and unify them into a single framework.
6. **Molten** - A minimal, extensible, fast and productive framework for building HTTP APIs with Python. Molten can automatically validate requests according to predefined schemas.
7. **Japronto** - A screaming-fast, scalable, asynchronous Python 3.5+ HTTP toolkit integrated with pipelining HTTP server based on `uvloop` and `picohttpparser`.
8. **Klein** [flask like] - A micro-framework for developing production-ready web services with Python. It is ‘micro’ in that it has an incredibly small API similar to Bottle and Flask.
9. **Quart** [flask like]- A Python ASGI web microframework. It is intended to provide the easiest way to use asyncio functionality in a web context, especially with existing Flask apps.
10. **BlackSheep** - An asynchronous web framework to build event based, non-blocking Python web applications. It is inspired by Flask and ASP.NET Core. BlackSheep supports automatic binding of values for request handlers, by type annotation or by conventions.
11. **Cyclone** - A web server framework that implements the Tornado API as a Twisted protocol. The idea is to bridge Tornado’s elegant and straightforward API to Twisted’s Event-Loop, enabling a vast number of supported protocols.

**Brian #6:** [**Raise Better Exceptions in Python**](https://orbifold.xyz/raising-exceptions.html)

Extras

Michael: 

- [Naming venvs](https://twitter.com/brettsky/status/1197943833813635072) `--prompt` 
- Another new course coming soon: **Python for decision makers and business leaders**
- Some random interview over at Real Python: [Python Community Interview With Brian Okken](https://pycoders.com/link/2966/yrq2q8ogch)

Joke

- via Daniel Pope 
- What's a tractor's *least* favorite programming language? **Rust**.
