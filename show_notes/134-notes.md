# Python Bytes 134
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Three scientists publish a paper proving that Mercury, not Venus, is the closest planet to Earth.**](https://bigthink.com/strange-maps/mercury) **using Python**

- contributed by, and explained by, listener Andrew Diederich.

    “This is from the March 19th, 2019 Strange Maps article. Which planet is, on average, closest to the Earth? Answer: Mercury. Actually, Mercury is, on average, the closest to all other planets, because it’s closest to the sun.”
    
- article, including video, uses [PyEphem](https://rhodesmill.org/pyephem/), which apparently is now deprecated and largely replaced with [skyfield](https://rhodesmill.org/skyfield/). 

**Michael #2:** [**Github semantics**](https://github.com/github/semantic)

- Parsing, analyzing, and comparing source code across many languages
- Written in a Haskell, it’s a library and command line tool for parsing, analyzing, and comparing source code.
- It’s still early days yet, but semantic can do a lot of cool things, and is powering public-facing GitHub features. I’m tremendously excited as to see how it’ll evolve now that it’s a community-facing project.
- Understands: Python, TypeScript, JavaScript, Ruby, Go, …
- here are some cool things inside it:
	- A flow-sensitive, caching, generalized interpreter for imperative languages
	- An abstract interpreter that generates scope graphs for a given program text
	- A strategic rewriting system based on recursion schemes for open syntax terms

**Brian #3:** [**flake8-black**](https://pypi.org/project/flake8-black/)

- Contributed by Nathan Clayton
- “The point of this plugin is to be able to run `black --check ...` from within the flake8 plugin ecosystem.”
- I like to run flake8 during development both to keep things neat, and to train myself to just write code in a more standard way. This is a way to run `black` with no surprises.

**Michael #4:** [**Python Preview**](https://marketplace.visualstudio.com/items?itemName=dongli.python-preview) [**for VS Code**](https://marketplace.visualstudio.com/items?itemName=dongli.python-preview)

- You write Python code (script style mostly), it creates an object-visualization
- Think of a picture your first year C++ CS prof might draw. This extension does that automatically as you write Python code
- Looks to be based (conceptually) on [Philip Guo](https://twitter.com/pgbovine)’s  [Python Tutor](http://www.pythontutor.com/) site.

**Brian #5:** [**Create and Publish a Python Package with Poetry**](https://johnfraney.ca/posts/2019/05/28/create-publish-python-package-poetry/)

- John Franey
- Walks through creating a package, customizing the `pyproject.toml`, and talks about the different settings in the toml and what it means.
- Then using the testpypi, and finally publish.

**Michael #6:** [**Pointers in Python: What's the Point?**](https://realpython.com/pointers-in-python/)

- by Logan Jones
- Quick question: Does Python have pointers (outside of C-extensions, etc of course)?
- Yet Python is more pointer heavy than most languages (more so than C# more so than even C++)!
- In Python, everything is an object, even numbers and booleans.
- Each object contains at least three pieces of data:
	- Reference count
	- Type
	- Value
- Check that you have the same object `is` instead of `==`
- Python variables are pointers, just safe ones.
- Interesting little tidbit from the article:
	- Interning strings is useful to gain a little performance on dictionary lookup—if the keys in a dictionary are interned, and the lookup key is interned, the **key comparisons** (after hashing) **can be done by a pointer compare** instead of a string compare. (Source)
- But like we have inline-assembly in C++ and unsafe mode in C#, we [can use pointers in Cython](https://medium.com/@yusuken/calling-c-functions-from-cython-references-pointers-and-arrays-e1ccb461b6d8) or more fine-grained with [ctypes](https://dbader.org/blog/python-ctypes-tutorial).

**Extras**

Michael:

- PSF needs your help. Spread the word about the fundraiser and please, ask your company to contribute: [Building the PSF: the Q2 2019 Fundraiser](https://www.python.org/psf/donations/2019-q2-drive/) (Donations are tax-deductible for individuals and organizations that pay taxes in the United States)
	- “Contributions help fund workshops, conferences, pay meetup fees, support fiscal sponsorships, PyCon financial aid, and development sprints. ”
    

**Jokes** 

via Jay Miller

What did the developer name his newborn boy? **JSON**

