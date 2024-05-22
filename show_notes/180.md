# Python Bytes 180

Sponsored by **DigitalOcean**: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean) - $100 credit for new users to build something awesome.

**Michael #1:** [**Ubuntu 20.04 is out**](https://lists.ubuntu.com/archives/ubuntu-announce/2020-April/000256.html)!

- Next LTS support version since 26th April 2018 (18.04).
- Comes with Python 3.8 included!
- Already upgraded all our servers, super smooth.
- Kernel has been updated to the 5.4 based Linux kernel, with additional support for Wireguard VPN, AUFS5, and improved support for IBM, Intel, Raspberry Pi and AMD hardware.
- Features the latest version of the GNOME desktop environment.
- Brings support for installing an Ubuntu desktop system on top of ZFS.
- 20.04 already an option on DigitalOcean ;)

**Brian #2:** [**Working with warnings in Python**](https://lerner.co.il/2020/04/27/working-with-warnings-in-python/)

- (Or: When is an exception not an exception?)
- Reuven Lerner
- Exceptions, the class hierarchy of exceptions, and warnings.
- “… most of the time, warnings are aimed at developers rather than users. Warnings in Python are sort of like the “service needed” light on a car; the user might know that something is wrong, but only a qualified repairperson will know what to do. Developers should avoid showing warnings to end users.”
- Python’s warning system …:
	- It treats the warnings as a separate type of output, so that we cannot confuse it with either exceptions or the program’s printed text,
	- It lets us indicate what kind of warning we’re sending the user,
	- It lets the user indicate what should happen with different types of warnings, with some causing fatal errors, others displaying their messages on the screen, and still others being ignored,
	- It lets programmers develop their own, new kinds of warnings.
- Reuven goes on to show how to use warnings in your code.
	- using them
	- creating custom warnings
	- filtering

**Michael #3:** [**Safer file writer**](https://medium.com/@TomSwirly/%EF%B8%8F-safer-a-safer-file-writer-%EF%B8%8F-5fe267dbe3f5)

- pip installable, see [the article](https://medium.com/@TomSwirly/%EF%B8%8F-safer-a-safer-file-writer-%EF%B8%8F-5fe267dbe3f5) and the [repo too](https://github.com/rec/safer).
- Consider this code:

```
    with open(filename, 'w') as fp:
        json.dump(data, fp)
```

- It’s using with, so it’s good right? 
- Well the file itself may be overwritten and maybe corrupted
- With `safer`, you write almost identical code:
 
 ```   
    with safer.open(filename, 'w') as fp:
        json.dump(data, fp)
```

- Now if `json.dump()` throws an exception, the original file is unchanged, so your important data file lives to see another day.
- The actual 28 lines of code is pretty interesting: [https://github.com/rec/safer/blob/v1.0.0/safer.py#L70-L97](https://github.com/rec/safer/blob/v1.0.0/safer.py#L70-L97)


**Brian #4:** [**codespell**](https://github.com/codespell-project/codespell)

- codespell : Fix common misspellings in text files. It's designed primarily for checking misspelled words in source code, but it can be used with other files as well.
- I got a cool [pull request against the cards project](https://github.com/okken/cards/pull/43) to add a pre-commit hook to run codespell. (Thanks Christian Clauss)
- codespell caught a documentation spelling error in cards, where I had spelled “arguments” as “arguements”. Oops.
- Spelling errors are annoying and embarrassing in code and comments, and distracting. Also hard to deal with using traditional spell checkers. So super glad this is a thing. 

**Michael #5:** [**Austin profiler**](https://github.com/P403n1x87/austin)

- via [Anthony Shaw](http://twitter.com/anthonypjshaw/)
- Python frame stack sampler for CPython
- Profiles CPU and Memory!
- Why Austin?
	- **Written in pure C** Austin is written in pure C code. There are no dependencies on third-party libraries.
	- **Just a sampler** - fast: Austin is just a frame stack sampler. It looks into a running Python application at regular intervals of time and dumps whatever frame stack it finds.
	- **Simple output, powerful tools** Austin uses the collapsed stack format of FlameGraph that is easy to parse. You can then go and build your own tool to analyse Austin's output.
	- You could even make a *player* that replays the application execution in slow motion, so that you can see what has happened in temporal order.
	- **Small size** Austin compiles to a single binary executable of just a bunch of KB.
	- **Easy to maintain** Occasionally, the Python C API changes and Austin will need to be adjusted to new releases. However, given that Austin, like CPython, is written in C, implementing the new changes is rather straight-forward.
- Creates nice flame graphs
- The Austin TUI is nice!
![Austin TUI](https://raw.githubusercontent.com/P403n1x87/austin/master/art/austin-tui_threads_nav.gif)

- Web Austin is yet another example of how to use Austin to make a profiling tool. It makes use of [d3-flame-graph](https://github.com/spiermar/d3-flame-graph) to display a *live* flame graph in the web browser that refreshes every 3 seconds with newly collected samples.
![](https://raw.githubusercontent.com/P403n1x87/austin/master/art/web-austin.gif)

- Austin output format can be converted easily into the [Speedscope](https://github.com/P403n1x87/austin/blob/master/speedscope.app) JSON format. You can find a sample utility along with the TUI and Austin Web.

**Brian #6:** [**Numbers in Python**](https://orbifold.xyz/numbers.html)

- Moshe Zadka
- A great article on integers, floats, fractions, & decimals 
- Integers
	- They turn into floats very easily, `(4/3)*3` → `4.0`, int → float
- Floats
	- don’t behave like the floating point numbers in theory
	- don’t obey mathematical properties
		- subtraction and addition are not inverses 
		    - `0.1 + 0.2 - 0.2 - 0.1` != `0.0`
		- addition is not associative
	- My added comment: Don’t compare floats with ==, use pytest.approx or other approximation techniques.
- Fractions
	- Kinda cool that they are there but be very careful about your input
	- Algorithms on fractions can explode in time and to some extent memory.
	- Generally better to use floats
- Decimals
	- Good for financial transactions.
	- Weird dependence on a global state variable, the context precision.
	- Safer to use a local context to set the precision locally

```
    >>> with localcontext() as ctx:
    ...     ctx.prec = 10
    ...     Decimal(1) / Decimal(7)
    ...
    Decimal('0.1428571429')
```

- See also
	- [fractions in std lib](https://docs.python.org/3/library/fractions.html)
	- [decimals in std lib](https://docs.python.org/3/library/decimal.html)
	- [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)
    

Extras:

Brian:

- [python 3.9.0a6](https://mail.python.org/archives/list/python-committers@python.org/message/JJWIXYICQHCEFCJCCXVSWTP5O67UVCQC/), now with the new PEG parser for CPython

Michael:

- Keep subscribing over at youtube: [pythonbytes.fm/youtube](http://pythonbytes.fm/youtube)

Joke:

***Unix is user friendly. It's just very particular about who its friends are. (via*** [***PyJoke***](https://pypi.org/project/PyJoke/)***)***

***If you put 1000 monkeys at 1000 computers eventually one will write a Python program.  The rest will write PERL.*** (via [@JamesAbel](https://twitter.com/JamesAbel))



