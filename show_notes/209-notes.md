# Python Bytes 209
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Michael #1:** [**Running Python on .NET 5**](https://tonybaloney.github.io/posts/running-python-on-dotnet-5-with-pyjion.html)

- by Anthony Shaw
- Talked about [pyjion way back when on episode 49 with Brett Cannon](https://talkpython.fm/episodes/show/49/microsofts-jit-based-python-project-pyjion).
- .NET 5 was released on November 10, 2020. It is the cross-platform and open-source replacement of the [**.NET Core**](https://github.com/dotnet/core) project and the **.NET** project that ran exclusively on Windows since the late 90’s. See [the conference about it](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oVWop1HEOml2OdqbDs6IlcI) if you want to go deeper.
- Performance: I just saw a SO post about someone [complaining their Python was 31x slower than C#](https://stackoverflow.com/questions/29903320/why-is-my-computation-so-much-faster-in-c-sharp-than-python).
- The most common way around this performance barrier is to compile Python extensions from C or using something like Cython.
- .NET 5 CLR comes bundled with a performant JIT compiler (codenamed RyuJIT) that will compile .NETs IL into native machine instructions on Intel x86, x86-64, and ARM CPU architectures.
- Pyjion is a project to replace the core execution loop of CPython by transpiling CPython bytecode to ECMA CIL and then using the .NET 5 CLR to compile that into machine code.
- It then executes the machine-code compiled JIT frames at runtime instead of using the native execution loop of CPython.
- A few releases of Python ago (CPython specifically, the most commonly used version of Python) in 3.7 a new API was added to be able to swap out “frame execution” with a replacement implementation. This is otherwise known as [PEP 523](https://www.python.org/dev/peps/pep-0523/).
- This extension uses the same standard library as Python 3.9.
- Will this be compatible with my existing Python code? What about C Extensions?
	- The short answer is- if your existing Python code runs on CPython 3.9 – **yes** it will be compatible.
	- Tested against the full CPython “test suite” on all platforms. In fact, it was the first JIT ever to pass the test suite.
- Is this faster? The short answer a little, but not by much (yet).
- see also: https://twitter.com/anthonypjshaw/status/1328457723608928256?s=20 


**Brian #2:**  [**PEP 621 -- Storing project metadata in pyproject.toml**](https://www.python.org/dev/peps/pep-0621/)

- Progress on standardizing what goes into pyproject.toml
- Authors Brett Cannon, Paul Ganssle, Pradyun Gedam, Sébastien Eustace (of poetry), Thomas Kluyver (of flit), Tzu-Ping Chung
- Motivators of this PEP are:
	- Encourage users to specify core metadata statically for speed, ease of specification, unambiguity, and deterministic consumption by build back-ends
	- Provide a tool-agnostic way of specifying metadata for ease of learning and transitioning between build back-ends
	- Allow for more code sharing between build back-ends for the "boring parts" of a project's metadata
- Doesn’t change any existing core metadata
- Doesn’t attempt to standardize all possible metadata
- Included in table named `[project]`:
	- name
	- version
	- description
	- readme
	- requires-python
	- license
	- authors/maintainers
	- keywords
	- classifiers
	- urls
	- entry points
	- dependencies/optional-dependencies
	- dynamic 
- There’s an example in the PEP that helps clear things up
- Many items have synonyms specified for flit/poetry/setuptools (presumably for backward compatibility)

**Michael #3:** [**GitHub revamps copyright takedown policy after restoring YouTube-dl**](https://www.engadget.com/github-youtube-dl-aftermath-222301386.html)

- In October following a DMCA complaint from the Recording Industry Association of America (RIAA) it was taken down at GitHub. 
- Citing a [letter](https://github.com/github/dmca/blob/master/2020/11/2020-11-16-RIAA-reversal-effletter.pdf) from the Electronic Frontier Foundation (the EFF), GitHub says it ultimately found that the RIAA’s complaint didn’t have any merit. 
- The RIAA argued the tool ran afoul of section 1201 of the US copyright law by giving people the means to circumvent YouTube’s DRM. 
- the EFF dissects the RIAA’s claims, highlighting where the organization had either misinterpreted the law or how the code of YouTube-dl works. “Importantly, YouTube-dl does not decrypt video streams that are encrypted with commercial DRM technologies, such as Widevine, that are used by subscription videos sites, such as Netflix,” the organization points out when it comes to the RIAA’s primary claim.
- GitHub is implementing new policies to avoid a repeat of a repeat situation moving forward. First, it says a team of both technical and legal experts will manually evaluate every single section 1201 claim.
- If the company’s technical and legal teams ultimately find any issues with a project, GitHub will give its owners the chance to address those problems before it takes down their work.
- GitHub is establishing a $1 million legal defense fund for developers.
- Sidebar: EFF has just launched [*How to Fix the Internet*](https://www.eff.org/deeplinks/2020/11/introducing-how-fix-internet-new-podcast-eff), a new podcast mini-series that examines potential solutions to six ills facing the modern digital landscape.

**Brian #4:**  [**Install & Configure MongoDB on the Raspberry Pi**](https://developer.mongodb.com/how-to/mongodb-on-raspberry-pi)

- Mark Smith
- Definitely a “wow, I didn’t know you could do that” article.
- Tutorial walks through
	- Installing 64 bit Ubuntu Server on a Raspberry Pi
	- Configure wifi
	- Install MongoDB on Pi
	- Set up a user account, to safely expose MongoDB on a home network.
	- Now you’ve got a MongoDB server in your house. So cool

**Michael #5: Extra! extra! extra!, hear all about it!**

- [Follow up](https://twitter.com/jmnickerson/status/1327640465102016515) on my critique of things like SQL & CSS put next to Python and Java. Maybe best to grab the conversation from [here](https://twitter.com/mkennedy/status/1328029407752065025).
- Guido joins Microsoft, [why](https://twitter.com/gvanrossum/status/1326932991566700549)? People seem to see this as a positive for sure. But they [checked him out](https://twitter.com/edxplore/status/1327420845031972866)!
- New code editor roaming the streets: [Nova](https://www.nova.app/) from Panic.
- Two thumbs up on Big Sur and now waiting on the Mac Mini M1.

**Brian #6:**  [**A Python driven AI Stylist Inspired by Social Media**](https://daleonai.com/social-media-fashion-ai)

- Dale Markowitz
- A bunch of Google tools (cloud storage, firebase, cloud vision api, product search api)
- Some React for front end
- Python to batch script
- General oversimplified process:
	- photos from social media for inspiration
	- photos of everything in your closet, multiple of each item
	- use AI suggest outfits from your closet that match inspiration photos
- Ok. The process is really more of a promo for Google AI products, and not so much about Python, but it’s a cool “look what you can do with software” kinda thing.
- Also, many of the tools used by online retail, like “similar products” and such, are available to lots of people now, and that’s cool.

Joke:

[Back to the [dev] future!](https://devhumor.com/media/commitstrip-never-lose-hope)

![[commitstrip] Never lose hope](https://devhumor.com/content/uploads/images/November2020/ie-linux.jpg)
