# Python Bytes 99
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**parse**](https://pypi.org/project/parse/)

- “*parse() is the opposite of format()**”*
- `regex` not required for parsing strings.
- Provides these functionalities: export `parse()`, `search()`, `findall()`, and `with_pattern()`

```
    >>> parse("It's {}, I love it!", "It's spam, I love it!")
    <Result ('spam',) {}>
    >>> search('Age: {:d}\n', 'Name: Rufus\nAge: 42\nColor: red\n')
    <Result (42,) {}>
    >>> ''.join(r.fixed[0] for r in findall(">{}<", "<p>the <b>bold</b> text</p>"))
    'the bold text'
```
     
- Can also compile for repeated use.

**Michael #2:** [**fman Build System**](https://build-system.fman.io/#features)

- FBS lets you create GUI apps for Windows, Mac and Linux 
- via Michael Herrmann
- Build Python GUIs, with Qt – in minutes
- Write a desktop application with PyQt or Qt for Python. 
- Use fbs to package and deploy it on Windows, Mac and Linux. 
- Avoid months of painful work with the proven solutions provided by fbs.
- Easy Packaging: Unlike other solutions, fbs makes packaging easy. Create installers for your app in seconds and distribute them to your users – on Windows, Mac and Linux!
- Open Source: fbs's source code is available on GitHub. You can use it for free in open source projects licensed under the GPL. Commercial licenses are also offered.
	- Free under the GPL. If that's too restrictive, a commercial license is 250 Euros once.
	- PyQt's licensing is similar (GPL/Commercial). A license for it is € 450 ([source](https://www.riverbankcomputing.com/commercial/buy)).
- Came from fman, a dual-pane file manager for Mac, Windows and Linux

**Brian #3:** [**fastjsonschema**](https://horejsek.github.io/python-fastjsonschema/)

- Validate JSON against a schema, quickly.

[](https://blog.horejsek.com/fastjsonschema/)

**Michael #4:** [**IPython 7.0, Async REPL**](https://blog.jupyter.org/ipython-7-0-async-repl-a35ce050f7f7)

- via [Nick Spirit](https://twitter.com/Spirix3)
- Article by [Matthias Bussonnier](https://blog.jupyter.org/@mbussonn?source=post_header_lockup)
- We are pleased to announce the release of [IPython 7.0, the powerful Python interactive shell](https://ipython.readthedocs.io/) that goes above and beyond the default Python REPL with advanced tab completion, syntactic coloration, and more.
- Not having to support Python 2 allowed us to make full use of new Python 3 features and bring never before seen capability in a Python Console, see the [Python 3 Statement.](https://python3statement.org/)
- One of the core features we focused on for this release is the ability to (ab)use the *async* and *await* syntax available in Python 3.5+.
- TL;DR: You can now use *async*/*await* at the top level in the IPython terminal and in the notebook, it should — in most of the cases — “just work”.
- The only thing you need to remember is: If it is an async function you need to await it.

**Brian #5:** [**molten**](https://moltenframework.com)

**Michael #6:** [**A Python love letter**](https://www.reddit.com/r/Python/comments/8ndhel/dear_python_where_have_you_been_all_my_life/)

- Dear Python, where have you been all my life? (reddit thread)
- I am NOT a developer. But, I've tinkered with programming (in BASIC, Visual Basic, Perl, now Python) when needed over the years
- I decided that I needed to script something, and hoped that learning how to do it in Python was going to take me significantly less time than doing it manually - with the benefit of future timesavings. No, I didn't go from 0 to production in a day. But if my coworkers will leave me alone, I might be in production by the end of the day tomorrow.
- What I'm working on today isn't super complex —  But putting together what I've done so far has just been a complete joy.
- Overall it feels natural, intuitive, and relatively easy to understand and write the code for the basic things I'm doing - I haven't had this much fun doing stuff with code since the days fooling around with BASIC in my teens.
- Feedback / comments
	- Welcome to the club. I came up on c++; my job highly trained me in C and assembly but every project I touch I think, wait, "we can do 95% this in python". And we do.
	- I used to have a chip on my shoulder. I wanted to do things the hard way to truly understand them. I went with C++. … I learned that doing things the smart way was better than doing things the hard way and didn't interfere with learning.
	- I felt the exact same way I finally decided to learn it. It's like a breath of fresh air. Sadly there are few things in my life that made me feel like this, Python and Bitcoin both give me the same levels of enjoyment. … I've used Java, Groovy, Scala, Objective-C, C, C++, C#, Perl and Javascript in a professional capacity over the years and nothing feels as natural to me as Python does. The developers truly deserve any donations they get for making it. … Hell **my next two planned tattoos are bitcoin and python** logos on my wrists.
	- I taught myself Python a little over 3 years ago and I quickly went from not being programmer to being a programmer. … However the real popularity of Python comes from the depth and quality of 3rd party libraries and how easy they are to install. 

**Extra:** 

- [**Brian: Power Mode II**](https://plugins.jetbrains.com/plugin/8251-power-mode-ii)


