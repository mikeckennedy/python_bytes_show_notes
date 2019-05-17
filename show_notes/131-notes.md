# Python Bytes 131
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1: PEP 581 (Using GitHub issues for CPython) is accepted**

- [PEP 581](https://www.python.org/dev/peps/pep-0581/)
- [The email announcing the acceptance.](https://mail.python.org/pipermail/python-dev/2019-May/157399.html)
- “The migration will be a large effort, with much planning, development, and testing, and we welcome volunteers who wish to help make it a reality.  I look forward to your contributions on [PEP 588](https://www.python.org/dev/peps/pep-0588/) and the actual work of migrating issues to GitHub.” — Barry Warsaw

**Michael** **#2**: [**Replace Nested Conditional with Guard Clauses**](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html)

- Deeply nested code is problematic (does it have deodorant — err comments?)
- But what can you do? Guard clauses!
- See [Martin Fowler’s article](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html) and [this one.](https://medium.com/@matryer/line-of-sight-in-code-186dd7cdea88)

```
    # BAD! 
    def checkout(user):
        shipping, express = [], []
        if user is not None:
            for item in user.cart:
                if item.is_available:
                    shipping.append(item)
                    if item.express_selected:
                        express.append(item)
    
        return shipping, express
```

```
    # BETTER! 
    def checkout(user):
        shipping, express = [], []
        if user is None:
            return shipping, express
    
        for item in user.cart:
            if not item.is_available:
                continue
    
            shipping.append(item)
            if item.express_selected:
                express.append(item)
    
        return shipping, express
```

**Brian #3:** [**Things you’re probably not using in Python 3 – but should**](https://datawhatnow.com/things-you-are-probably-not-using-in-python-3-but-should/)

- Vinko Kodžoman
- Some of course items:
	- f-strings
	- Pathlib (side note. [pytest](https://docs.pytest.org/en/latest/tmpdir.html) `[tmp_path](https://docs.pytest.org/en/latest/tmpdir.html)` [fixture](https://docs.pytest.org/en/latest/tmpdir.html) creates temporary directories and files with PathLib)
	- data classes
- Some I’m warming to:
	- type hinting
- And those I’m really glad for the reminder of:
- enumerations

```
    from enum import Enum, auto
    class Monster(Enum):
        ZOMBIE = auto()
        WARRIOR = auto()
        BEAR = auto()
        
    print(Monster.ZOMBIE)
    # Monster.ZOMBIE
```

- built in lru_cache: easy memoization with the `functools.lru_cache` decorator.

```
    @lru_cache(maxsize=512)
    def fib_memoization(number: int) -> int:
        ...
```

- extended iterable unpacking

```
    >>> head, *body, tail = range(5)
    >>> print(head, body, tail)
    0 [1, 2, 3] 4
    >>> py, filename, *cmds = "python3.7 script.py -n 5 -l 15".split()
    >>> cmds
    ['-n', '5', '-l', '15']
    >>> first, _, third, *_ = range(10)
    >>> first, third
    (0, 2)
``` 

**Michael #4:** [**The Python Arcade Library**](http://arcade.academy/)

- Arcade is an easy-to-learn Python library for creating 2D video games. It is ideal for people learning to program, or developers that want to code a 2D game without learning a complex framework.
- Minesweeper games, hangman, [**platformer games**](http://arcade.academy/examples/platform_tutorial/index.html) in general.
- Check out [Sample Games Made With The Arcade Library](http://arcade.academy/sample_games.html) too
- Includes physics and other goodies
- Based on OpenGL

**Brian #5:** [**Teaching a kid to code with Pygame Zero**](https://www.mattlayman.com/blog/2019/teach-kid-code-pygame-zero/)

- Matt Layman
- Scratch too far removed from coding.
- Using Mu to simplify coding interface.
	- comes with a built in Python.
	- Pygame Zero preinstalled
- “*[Pygame Zero] is intended for use in education, so that teachers can teach basic programming without needing to explain the Pygame API or write an event loop.”*
- Initial 29 line game taught:
	- naming things and variables
	- mutability and fiddling with “constants” to see the effect
	- functions and side effects
	- state and time
	- interactions and mouse events
- Article also includes some tips on how to behave as the adult when working with kids and coding.

**Michael #6:** **Follow up on GIL / PEP 554**

- [Has the Python GIL been slain?](https://hackernoon.com/has-the-python-gil-been-slain-9440d28fa93d) by Anthony Shaw
- multithreading in CPython is easy, but it’s not truly concurrent, and multiprocessing is concurrent but has a significant overhead.
- Because Interpreter state contains the memory allocation arena, a collection of all pointers to Python objects (local and global), sub-interpreters in PEP 554 cannot access the global variables of other interpreters.
- the way to share objects between interpreters would be to serialize them and use a form of IPC (network, disk or shared memory). All options are fairly inefficient
- But: [PEP 574 proposes a new pickle](https://www.python.org/dev/peps/pep-0574/) protocol (v5) which has support for allowing memory buffers to be handled separately from the rest of the pickle stream.
- When? Pickle v5 and shared memory for multiprocessing will likely be Python 3.8 (October 2019) and sub-interpreters will be between 3.8 and 3.9.

**Extras**

Brian: 

-  [PyCon 2019 videos are available](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ/videos)
    - So grateful for this. Already watched a couple, including Ant’s awesome talk about [complexity and wily](https://www.youtube.com/watch?v=dqdsNoApJ80).
- pytest and hypothesis show up in the new [Pragmatic Programmer](https://pragprog.com/book/tpp20/the-pragmatic-programmer-20th-anniversary-edition) book.

Michael:

- [**100 Days of Web**](https://training.talkpython.fm/courses/explore_100days_web/100-days-of-web-in-python) course is out!
- [**Effective PyCharm book**](https://effectivepycharm.com/)
- New release of our [**Android and iOS apps**](https://training.talkpython.fm/apps).

**Jokes**

- MK → Waiter: **Would you like coffee or tea?** Programmer: **Yes**.
