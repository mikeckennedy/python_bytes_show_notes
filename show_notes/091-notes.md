# Python Bytes 91
Sponsored by Datadog [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:**  [**What makes the Python Cool**](https://hackernoon.com/what-makes-the-python-cool-426e4c576685)

- Shankar Jha
- “some of the cool feature provided by Python”
- The Zen of Python: `import this`
- XKCD: `import antigravity`
- Swapping of two variable in one line: `a, b = b, a`
- Create a web server using one line: `python -m http.server 8000`
- `collections`
- `itertools`
- Looping with index: `enumerate`
- reverse a list: `list(reversed(a_list))`
- `zip` tricks
- list/set/dict comprehensions
- Modern dictionary
- `pprint`
- `_` when in interactive REPL
- Lots of great external libraries

**Michael #2:** [**Django 2.1 released**](https://www.djangoproject.com/weblog/2018/aug/01/django-21-released/)

- [The release notes](https://docs.djangoproject.com/en/stable/releases/2.1/) cover the smorgasbord of new features in detail, the [model “view” permission](https://docs.djangoproject.com/en/stable/releases/2.1/#model-view-permission) is a highlight that many will appreciate.
- Django 2.0 has reached the end of mainstream support. The final minor bug fix release (which is also a security release), [2.0.8](https://docs.djangoproject.com/en/stable/releases/2.0.8/), was issued today.
- Features
	- model  “view” feature: This allows giving users read-only access to models in the admin.
	- The new `[ModelAdmin.delete_queryset()](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.delete_queryset)` method allows customizing the deletion process of the “delete selected objects” action.
	- You can now [override the default admin site](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#overriding-default-admin-site).
	- Lots of ORM features
	- Cache: The [local-memory cache backend](https://docs.djangoproject.com/en/2.1/topics/cache/#local-memory-caching) now uses a least-recently-used (LRU) culling strategy rather than a pseudo-random one.
	- Migrations: To support frozen environments, migrations may be loaded from `.pyc` files.
	- Lots more

**Brian #3:** ****[**Awesome Python Features Explained Using Harry Potter**](https://github.com/zotroneneis/harry_potter_universe)

- Anna-Lena Popkes
- [Initial blog post](http://alpopkes.com/posts/2018/07/blog-post-1/)
- 100 Days of code, with a Harry Potter universe bent.
- Up to day 18 so far.

**Michael #4:** [**Executing Encrypted Python with no Performance Penalty**](https://blog.soroco.com/articles/pyce/)

- Deploying Python in production presents a large attack surface that allows a malicious user to modify or reverse engineer potentially sensitive business logic. 
- This is worse in cases of distributed apps.
- Common techniques to protect code in production are [binary signing](https://en.wikipedia.org/wiki/Code_signing), [obfuscation](https://en.wikipedia.org/wiki/Obfuscation_(software)), or [encryption](http://phrack.org/issues/58/5.html#article). But, these techniques typically assume that we are protecting either a single file (EXE), or a small set of files (EXE and DLLs).
- In Python signing is not an option and source code is wide open.
- requirements were threefold:
	1. Work with the reference implementation of Python,
	2. Provide strong protection of code against malicious and natural threats,
	3. Be performant both in execution time and in stored space
- This led to a pure Python solution using authenticated cryptography.
- Created a `.pyce` file that is encrypted and signed
- Customized import statement to load and decrypt them
- Implementation has no overhead in production. This is due to Python's [in-memory bytecode cache](https://docs.python.org/3/reference/import.html#the-module-cache).

**Brian 5 : icdiff and pytest-icdiff**

- [icdiff](https://github.com/jeffkaufman/icdiff): “Improved colored diff”
  - Jeff Kaufman
- [pytest-icdiff](https://github.com/hjwp/pytest-icdiff): “better error messages for assert equals in pytest”
  - Harry Percival

**Michael #6: Will there be a PyBlazor?**

- The .NET guys, and Steve Sanderson in particular, are undertaking [**an interesting project**](http://blog.stevensanderson.com/2018/02/06/blazor-intro/) with WebAssembly.
- **WebAssembly** (abbreviated Wasm) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.
- Works in Firefox, Edge, Safari, and Chrome
- Their project, [**Blazor**](http://blog.stevensanderson.com/2018/02/06/blazor-intro/), has nearly the entire .NET runtime (AKA the CLR) running natively in the browser via WebAssembly.
- This is notable because the CLR is basically pure C code. What else is C code? Well, CPython!
- Includes Interpreted and AOT mode:
	- **Ahead-of-time (AOT) compiled mode:** In AOT mode, your application’s .NET assemblies are transformed to pure WebAssembly binaries at build time.
- Being able to run .NET in the browser is a good start, but it’s not enough. To be a productive app builder, you’ll need a coherent set of standard solutions to standard problems such as UI composition/reuse, state management, routing, unit testing, build optimization, and much more.
- Mozilla called for this to exist for Python, but sadly didn’t contribute or kick anything off at PyCon 2018: https://www.youtube.com/watch?v=ITksU31c1WY&t=7s
- Gary Bernhardt’s [Birth and Death of JavaScript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) video is required pre-reqs as well (asm.js).

Extras and personal info:

Michael:

- [**Building data-driven web apps**](https://training.talkpython.fm/courses/explore_pyramid/building-data-driven-web-applications-in-python-with-pyramid-sqlalchemy-and-bootstrap) course is being well received
- [**Guido van Rossum: Python 3 retrospective**](https://www.youtube.com/watch?v=Oiw23yfqQy8&feature=youtu.be) — Guido’s final presentation as BDFL
