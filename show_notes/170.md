# Python Bytes 170

Sponsored by **DigitalOcean**: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean) - $100 credit for new users to build something awesome.

**Michael #1:** [**Python visualization graph**](https://pyviz.org/) **(**[**image**](https://rougier.github.io/python-visualization-landscape/landscape-colors.png)**)**

- via Prayson Daniel
- The PyViz.org website is an open platform for helping users decide on the best open-source (OSS) Python data visualization tools for their purposes, with links, overviews, comparisons, and examples.
- [Overviews](https://pyviz.org/overviews/index.html) of the OSS visualization packages
- [High-level tools](https://pyviz.org/high-level/index.html) for getting started
- A [live table](https://pyviz.org/tools.html) for comparing maturity, popularity, and support.
- [Dashboarding](https://pyviz.org/dashboarding/index.html) tools
- [SciVis](https://pyviz.org/scivis/index.html) tools for rendering data embedded in three-dimensional space.
- [Tutorials](https://pyviz.org/tutorials/index.html)
- [Topic examples](https://examples.pyviz.org) of using Python viz tools to analyze or describe specific datasets

**Brian #2:** ****[**Awesome Zen of Python**](https://github.com/Pilifer/awesome-zen-of-python)

- A Rabbit Hole lot of Zen
    - yes, I know, that’s a terrible mixed metaphor
- List of articles on “the Zen of Python”
- Well, articles, talks, tools, and “other?”
- [Al Sweigart: The Zen of Python, Explained](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/) is a nice quick reference.
- [Moshe Zadka: Meditations on the Zen of Python](https://orbifold.xyz/zen-of-python.html) is slightly longer, but good and still a quick read.
- One line (“There should be one-- and preferably only one --obvious way to do it.”) is a joke making fun of pre-decrement, post-decrement in C.
- [Abdur-Rahmaan Janhangeer: The Zen Of Python Is A Joke And Here Is Why](https://dev.to/abdurrahmaanj/the-zen-of-python-is-a-joke-and-here-is-why-you-should-not-take-it-too-seriously-508d) is a must read.

**Michael #3:** [**Jupytext**](https://github.com/mwouts/jupytext)

- via [**Matt Harrison**](https://twitter.com/__mharrison__/status/1229995792061976576)
- Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts 
- Wished Jupyter notebooks were plain text documents? 
- Wished you could edit them in your favorite IDE? 
- And get clear and meaningful diffs when doing version control? 
- Then... Jupytext may well be the tool you're looking for!
- Jupytext can save Jupyter notebooks as
    - Markdown and R Markdown documents
    - Scripts in many languages.
- The languages that are currently supported by Jupytext are: Julia, Python, R, Bash, Scheme, Clojure, Matlab, Octave, C++, q/kdb+, IDL, TypeScript, Javascript, Scala, Rust/Evxcr, PowerShell, C#, F#, and Robot Framework.

**Brian #4:** ****[**Tour of Python Itertools**](https://martinheinz.dev/blog/16)

- Martin Heinz
- Very cool quick look at some of the cool-ness to be found in itertools and more_itertools.
- itertools
    - compress - one iterator to another eliminating elements that fail a bool expression
    - accumulate - like functools.reduce but returns all intermediate values
    - cycle - so cool, create a never ending repeating iterable
    - tee - multiple references to one iterable
- more_itertools
    - divide - divides iterable into sub-iterables
    - partition - split into two based on a predicate bool expression
    - side_effect - attach a side effect function to an iterable that gets called with each element
    - collapse - like flatten
    - split_at - multiple iterables splitting at divider items, specified with predicate
    - bucket - multiple iterables based on multi-return-value expression
    - map_reduce - specify 3 functions: *key* function (for categorizing), *value* function (for transforming) and finally *reduce* function (for reducing).
    - sort_together
    - seekable
    - filter_except
    - unique_to_each

**Michael #5:** [**justpy.io**](https://justpy.io/#/)

- JustPy is an object-oriented, component based, high-level Python Web Framework that requires no front-end programming.
- JustPy has no front-end/back-end distinction. All programming is done on the back-end allowing a simpler, more productive, and more Pythonic web development experience.
- JustPy removes the front-end/back-end distinction by intercepting the relevant events on the front-end and sending them to the back-end to be processed.
- Elements on the web page are instances of component classes. A component in JustPy is a Python class that allows you to instantiate reusable custom elements whose functionality and design is encapsulated away from the rest of your code.
- Custom components can be created using other components as building blocks. Out of the box, JustPy comes with support for [HTML](https://justpy.io/#/tutorial/html_components) and [SVG](https://justpy.io/#/tutorial/svg_components) components as well as more complex components such as [charts](https://justpy.io/#/charts_tutorial/introduction) and [grids](https://justpy.io/#/grids_tutorial/introduction).
- Supports most of the components and the functionality of the [Quasar](https://quasar.dev/) library
- Based on solid libraries: Starlette, uvicorn, and Vue.js.

**Brian #6:** ****[**Modularity for Maintenance**](https://glyph.twistedmatrix.com/2020/02/modules-for-maintenance.html)

- Glyph
- A list of many automation tools you can use to help with the maintenance of open source projects.
    - CI, tox, linting, type checking, dependencies, security, coverage, formatting, releasing
    - with lots of options and links
- A request for some kind of tool to help automate all the automation when starting new projects. Maybe a cookie-cutter thing….
- That would be cool. But frankly, the list is super helpful also.

Extras:

Brian:

- [Sentry helping fund some OSS projects.](https://blog.sentry.io/2020/02/18/funding-open-source)
    - black, pypi, pytest, structlog, gimli (last one is a Rust thing).

Michael:


- Just launched a new 7.2 hour course: [**Python for absolute beginners**](https://training.talkpython.fm/courses/explore_beginners/python-for-absolute-beginners)
- Talk Python Training now streaming newest courses in **HiDPI** (nearly 4K) and it’s super crisp
- AWS Cloud has [**decided to no longer publish awscli**](https://twitter.com/codewithanthony/status/1228002256441597952) to #pypi pulling a 700M+ download package (via [Anthony Sottile](https://twitter.com/codewithanthony))
- The podcast RSS feed is a little smaller now.

Joke:

First law of software quality: `e = mc^2` → `errors = (more code)^2`.


