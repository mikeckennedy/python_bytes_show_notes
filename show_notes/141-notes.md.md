# Python Bytes 141
Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Debugging with f-strings in Python 3.8**](https://docs.python.org/3.8/whatsnew/3.8.html#f-strings-now-support-for-quick-and-easy-debugging)

- We’ve talked about the walrus operator, `:=`, but not yet “debug support for f-strings”
- this: `print(f'foo={foo} bar={bar}')`
- can change to this: `print(f'{foo=} {bar=}')`
- and if you don’t want to print with `repr()` you can have `str()` be used with `!s`.
	- `print(f'{foo=!s} {bar=!s}')`
- also `!f` can be used for float modifiers:
```
        >>> import math
        >>> print(f'{math.pi=!f:.2f}')
        math.pi=3.14
```

- one more feature, space preservation in the f-string expressions:

```
        >>> a = 37
        >>> print(f'{a = }, {a  =  }')
        a = 37, a  =  37
```

**Michael #2:** [**Am I "real" software developer yet?**](https://medium.com/free-code-camp/am-i-a-real-software-engineer-yet-a0f38a2248c0)

- by [Sun-Li Beatteay](https://medium.com/@SunnyB?source=post_page---------------------------)
- To new programmers joining the field, especially those without CS degrees, it can feel like the title is safe-guarded. Only bestowed on the select that have proven themselves.
- Sometimes manifests itself as Impostor Syndrome
- Focused on front-end development as I had heard that HTML, CSS and JavaScript were easy to pick up
- That was when I decided to [create a portfolio site for my wife](https://medium.freecodecamp.org/a-tale-of-two-websites-the-importance-of-slow-progress-and-self-reflection-4a09ffcbd059), who was a product designer.
- Did my best to surround myself with tech culture. 
	- Watched YouTube videos
	- listened to podcasts
	- read blog posts from experienced engineers to keep myself motivated. 
	- Daydreamed what it would be like to stand in their shoes.
- My wife’s website went live in July of that year. I had done it.
- Could I finally start calling myself something of a *Software Engineer*?
	- “Web development isn’t real programming”
- Spent the next 18 months studying software development full time. I quit my job and moved in with my in-laws — which was a journey in-and-of itself.
	- Software engineer after 1-2 years? No so fast (says the internet)
- The solution that I found for myself was simple yet terrifying: talking to people
- MK: BTW, I don’t really like the term “engineer”

**Brian #3:** [**De**](https://github.com/alexmojaki/snoop)[**bugging with local variables and snoop**](https://github.com/alexmojaki/snoop)

- debugging tools
- ex: “You want to know which lines are running and which aren't, and what the values of the local variables are.”
	- Throw a `@snoop` decorator on a function and the function lines and local variable values will be dumped to stderr during run. Even showing loops a bunch of times.
- It’s tools to almost debug as if you had a debugger, without a debugger, and without having to add a bunch of logging or print statements.
- Lots of other use models to allow more focus.
	- wrap just part of your function with a `with snoop` block
	- only watch certain local variables.
	- turn off reporting for deep function/block levels.

**Michael #4:** [**New home for Humans**](https://github.com/not-kennethreitz/team/issues/21)

- This came out of the blue with some trepidation:
-  kennethreitz commented 6 days ago:

In the spirit of transparency, I'd like to (publicly) find a new home for my repositories. I want to be able to still make contributions to them, but no longer be considered the "owner" or "arbiter" or "BDFL" of these repositories.

Some notable repos:
    
- [https://github.com/kennethreitz/requests](https://github.com/kennethreitz/requests)
- [https://github.com/kennethreitz/records](https://github.com/kennethreitz/records)
- [https://github.com/kennethreitz/requests-html](https://github.com/kennethreitz/requests-html)
- [https://github.com/kennethreitz/setup.py](https://github.com/kennethreitz/setup.py)
- [https://github.com/kennethreitz/legit](https://github.com/kennethreitz/legit)
- [https://github.com/kennethreitz/responder](https://github.com/kennethreitz/responder)
        
- Lots of back and forth until [**Ernest jumped in**](https://github.com/not-kennethreitz/team/issues/21#issuecomment-512535398).
- The Python Software Foundation would like to offer to accept transfers of these repositories into the [@psf](https://github.com/psf) GitHub organization. This organization was recently acquired by the Python Software Foundation and intended to provide administrative backstopping for projects in the ecosystem; existing maintainers of various projects will remain and the PSF staff will be available to manage repositories and teams as necessary.

**Brian #5:** [**The Backwards Commercial License**](https://hueniverse.com/the-backwards-commercial-license-647290f7e38b)

- Eran Hammer - open source dev, including hapi.js
- Interesting idea to make open source projects maintainable
- Three phases of software lifecycle for some projects:
	- first: project created to fill a need in one project/team/company, a single use case
	- second: used by many, active community, growing audience
	- three: work feels finished. bug fixes, security issues, minor features continue, but most people can stay on old stable versions
- During the “done” phase, companies would like to have bug fixes but don’t want to have to keep changing their code to keep up.
- Idea: commercial license to support old stable versions. 
	- “If you keep up with the latest version, you do not require a license (unless you want the additional benefits it will provide).”
	- “However, very few companies can quickly migrate every time there is a new major release of a core component. Engineering resources are limited and in most cases, are better directed at building great products than upgrading supporting infrastructure. The backwards license provides this exact assurance. You can stay on any version you would like knowing that you are still running supported, well-maintained, and secure code.”
	- “The new commercial license will include additional benefits focused on providing enterprise customers the assurances needed to rely on these critical components for many years to come. “

**Michael #6:** [**Switching Python Parsers?**](https://medium.com/@gvanrossum_83706/peg-parsers-7ed72462f97c)

- via [Gi Bi](https://twitter.com/_gbon/status/1153269201097936898), article by Guido van Rossum
- Alternative to the home-grown parser generator that I developed 30 years ago when I started working on Python. (That parser generator, dubbed “pgen”, was just about the first piece of code I wrote for Python.)
- Here are some of the issues with pgen that annoy me. 
	- The “1” in the LL(1) moniker implies that it uses only a single token lookahead, and this limits our ability of writing nice grammar rules.
	- Because of the single-token lookahead, the parser cannot determine whether it is looking at the start of an expression or an assignment.
- So how does a PEG parser solve these annoyances? By using an infinite lookahead buffer! 
- The typical implementation of a PEG parser uses something called “packrat parsing”, which not only loads the entire program in memory before parsing it, but also allows the parser to backtrack arbitrarily.
- Why not sooner? Memory! But that is much less of an issue now.
- My idea now, putting these things together, is to see if we can create a new parser for CPython that uses PEG and packrat parsing to construct the AST directly during parsing, thereby skipping the intermediate parse tree construction, possibly *saving* memory despite using an infinite lookahead buffer

**Extras**

Brian: 

- Plone 5.2 [https://plone.org/news/2019/plone-5-2-the-future-proofing-release](https://plone.org/news/2019/plone-5-2-the-future-proofing-release)
	- Plone is a content management system built on top of Zope, a web application server framework.
	- Plone 5.2 
		- supports Python 3.6, 3.7, 3.8
		- uses Zope 4, which also support Python 3
	- Multi-year effort
		- [Interview with Philip Bauer, organizer of 5.2.](https://plone.org/news/2019/q-a-with-philip-bauer)

Michael:

- [Building Dab and T-Pose Controlled Lights - Make Art with Python](https://www.makeartwithpython.com/blog/dab-and-tpose-controlled-lights/)    

**Jokes** 

A couple of quick ones:

- “What is a whale’s favorite language?” “C” — via Eric Nelson
- Why does Pythons live on land? Because it is above C-level! — via Jesper Kjær Sørensen @JKSlonester

