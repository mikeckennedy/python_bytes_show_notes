# Python Bytes 83
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest: [Cristian Medina](https://tryexceptpass.org/), [@tryexceptpass](https://twitter.com/tryexceptpass)

**Brian #1:** [**Code with Mu: a simple Python editor for beginner programmers.**](https://codewith.mu/en/)

- Found out about this from Nicholas Tollervey ([@ntoll](https://twitter.com/ntoll))
- Built by an impressive list of people: [https://codewith.mu/en/](https://codewith.mu/en/) thanks
- Beginning code editor that also works with Adafruit and micro:bit boards.
- From about:
	- **Less is More.**
		- Mu has only the most essential features, so users are not intimidated by a baffling interface.
	- **Tread the Path of Least Resistance.**
		- Whatever the task, there is always only one obvious way to do it with Mu.
	- **Keep it Simple.**
		- It's quick and easy to learn Mu ~ complexity impedes a novice programmer's first steps.
	- **Have fun!**
		- Learning should inspire fun ~ Mu helps learners quickly create and test working code.

**Cris #2:** [**Python parenthesis primer**](http://blog.lerner.co.il/python-parentheses-primer/)

- Good for beginners. Covers the main uses of parenthesis, curly brackets and square brackets. Including code examples.
- Parenthesis
	- Callables.
	- Operation prioritization.
	- Tuples.
	- Generator expressions.
	- Skirting the indentation rules.
- Square brackets
	- Lists and their comprehensions.
	- Indexing.
	- Slices.
	- Comments also mention type hints.
- Curly braces
	- Dictionaries and comprehensions.
	- Sets and comprehensions.
	- F-strings.
	- str.format.
- Try to import braces from `__future__`:

```
    >>> from __future__ import braces
      File "<stdin>", line 1
    SyntaxError: not a chance
```

**Michael #3:** [**Python for Qt Released**](https://blog.qt.io/blog/2018/06/13/qt-python-5-11-released/)

- The Qt Company happy to announce the first official release of Qt for Python (Pyside2).
- v5.11
- We hope we can receive plenty of feedback on what works and what does not. We want to patch early and often.
- Eventually the aim is to release Qt for Python 5.12 without the Tech Preview flag.
- Started two years ago with this [announcement](https://groups.google.com/forum/#!topic/pyside-dev/pqwzngAGLWE) from [Lars](https://blog.qt.io/blog/author/lars/).
- Get Qt for Python: The release supports Python 2.7, 3.5 & 3.6 on the three main desktop platforms. The packages can be obtained from download.qt.io or using pip with
- `pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2`

**Brian #4:** [**Itertools in Python 3, By Example**](https://realpython.com/python-itertools/)
[](https://realpython.com/python-itertools/)
- by David Amos ([@somacdivad](https://twitter.com/somacdivad))
- Iterators and generators are awesome.
- Nice discussion of lazy evaluation and iterator algebra.
- Naive approach using list can blow up in memory and time if you use huge datasets.
- Examples:
	- combinations, combinations_with_replacement, permutations
	- count, repeat, cycle, accumulate
	- product, tee, islice, chain
	- filterfalse, takewhile, dropwhile

**Cris #5:** [**Python Sets and Set Theory**](https://towardsdatascience.com/python-sets-and-set-theory-2ace093d1607)

- Nice primer on sets in python and a little set theory.
- How to build them: `set()` vs `{``'``value1``'``,` `'``value2``'``}` vs `{name for name in name_list}`
- Membership tests (which are O(1))
- Set operations
	- Union
	- Intersection
	- Difference
	- Symmetric Difference
- Frozen sets

**Michael #6:** [**Python 3.7 is coming soon**](https://docs.python.org/3.7/whatsnew/3.7.html)**!**

- Schedule
	- 3.7.0 candidate 1: 2018-06-12
	- 3.7.0 final: 2018-06-27
- What’s new / changed?
	- New syntax features: PEP 563, postponed evaluation of type annotations.
	- New modules: dataclasses: PEP 557 – Data Classes
	- New built-in features: PEP 553, the new breakpoint() function.
	- Standard lib changes: 
		- The asyncio module has received new features, significant usability and performance improvements.
		- The time module gained support for functions with nanosecond resolution.
	- Speed: 
		- Method calls are 20% faster
		- 3.7 is THE fastest Python available, period.
- [**What’s new in Python 3.7 course**](https://app.pluralsight.com/library/courses/python-whats-new/) by Anthony Shaw

**Our news**

- ahem… **[https://www.mongodb.com/presentation/building-python-web-apps](https://www.mongodb.com/presentation/building-python-web-apps)**

