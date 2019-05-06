# Python Bytes 128
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Solving Algorithmic Problems in Python with pytest**](https://adamj.eu/tech/2019/04/21/solving-algorithmic-problems-in-python-with-pytest/)

- Adam Johnson
- How to utilize pytest to set up quick test cases for coding challenges, like [Project Euler](https://projecteuler.net/) or [Advent of Code](https://adventofcode.com/).
- Moving the specification and examples in the challenge description into test cases.
- Running the tests with a stub implementation and understanding the failure output.
- Gradually building up a working solution.
- Nice demo of how little code it takes to write quick test cases.
- Also a cool idea to use challenge sites and platforms as TDD/test first practice, as well as practice converting specifications into test cases.

**Michael #2: [DepHell -- project management for Python](https://github.com/dephell/dephell)**

- via [**@dreigelb**](https://twitter.com/dreigelb/status/1121119117296177154)
- Why it is better than all other tools:
	1. **Format agnostic**. You can use DepHell with your favorite format: setup.py, requirements.txt, Pipfile, poetry. DepHell supports them all and much more.
	2. **Use your favorite tool on any project**. Want to install a poetry based project, but don't like poetry? Just say DepHell to convert project meta information into setup.py and install it with pip. Or directly work with the project from DepHell, because DepHell can do everything what you usually want to do with packages.
	3. **DepHell doesn't try to replace your favorite tools**. If you use poetry, you have to use poetry's file formats and commands. However, DepHell can be combined with any other tool or even combine all these tools together through formats converting. You can use DepHell, poetry and pip at the same time.
	4. **Easily extendable**. Pipfile should be just another one supported format for pip. However, pip is really old and big project with many bad decisions, so, PyPA team can't just add new features in pip without fear to broke everything. This is how pipenv has been created, but pipenv has inherited almost all problems of pip and isn't extendable too. DepHell has strong modularity and can be easily extended by new formats and commands.
	5. **Developers friendly**. We aren't going to place all our modules into `[_internal](https://github.com/pypa/pip/tree/master/src/pip/_internal)`. Also, DepHell has [big ecosystem](https://github.com/dephell) with separated libraries to help you use some DepHell's parts without pain and big dependencies for your project.
	6. **All-in-one-solution**. DepHell can manage dependencies, virtual environments, tests, CLI tools, packages, generate configs, show licenses for dependencies, make security audit, get downloads statistic from pypi, search packages and much more. None of your tools can do it all.
	7. **Smart dependency resolution**. Sometimes pip and pipenv can't lock your dependencies. Try to execute `pipenv install oslo.utils==1.4.0`. Pipenv can't handle it, but DepHell can: `dephell deps add --from=Pipfile oslo.utils==1.4.0` to add new dependency and `dephell deps convert --from=Pipfile --to=Pipfile.lock` to lock it.
	8. **Asyncio based**. DepHell doesn't support Python 2.7, and that allows us to use modern features to make network and filesystem requests as fast as possible.
	9. **Multiple environments**. You can have as many environments for project as you want. Separate sphinx dependencies from your main and dev environment. Other tools like pipenv and poetry don't support it.

**Brian #3 [Python rant: from foo import  is bad](http://www.walkingrandomly.com/?p=6209)**

- Mike Croucher
- I’m glad to see this post because I’m still seeing this practice a lot, even in tutorial blog posts!
- This is meaningless: `result = sqrt(-1)`
- Is it:  `math.sqrt(-1)`? or `numpy.sqrt(-1)` or `cmath.sqrt(-1)`? 
	- or `scipy`? or `sympy`?
- Recommendation:
	- Never do `from x import *`
	- Use `import math` 
		- or `import numpy as np`
		- or even `from scipy import sqrt` 

**Michael #4:** [**Dask**](https://dask.org/)

- Dask natively scales Python 
- Have numpy, pandas, and scikit-learn code that needs to go faster?
- Run these on smart clusters of servers
- Or just on your laptop
- Process more data than will fit into RAM
- Supported by… interesting to see proper support there.
- Matthew Rocklin was on [**Talk Python 207 to discuss**](http://talkpython.fm/207)

**Brian #5:** [**Animations with Matplotlib**](https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c)

- Parul Pandey
- The raindrop simulation is mesmerizing. 
- Tutorial on using `FuncAnimation` to animate a sine wave
	- although, I’m not sure what the x axis means during an animation
- Also:
	- live updates based on changing data
	- animate turning a 3D plot
	- using `celluloid` package to animate
		- simple example
		- animating subplots
		- changing legend during animation

**Michael #6:** [**PEP 554 -- Multiple Interpreters in the Stdlib**](https://www.python.org/dev/peps/pep-0554/)

- This proposal introduces the stdlib interpreters module. The module will be [provisional](https://www.python.org/dev/peps/pep-0554/#provisional-status). It exposes the basic functionality of subinterpreters already provided by the C-API, along with new (basic) functionality for sharing data between interpreters.
- Sharing data centers around "channels", which are similar to queues and pipes.
- Examples and use-cases:
	- Running isolated code
	- In process, true parallelism 
	- Versioning of modules (?)
	- Plugin systems

**Extras**

Michael:

- iOS Talk Python Training app is out: [**training.talkpython.fm/apps**](http://training.talkpython.fm/apps)
- Find us at PyCon!
- [**Blessings terminal API**](https://github.com/erikrose/blessings) (from Erik Rose, via Prayson Daniel)

**Jokes**

via Topher Chung

- Knock knock.
- Race condition.
- Who's there?


