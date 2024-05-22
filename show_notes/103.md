# Python Bytes 103
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**FEniCS**](https://fenicsproject.org/)

- “FEniCS is a popular open-source ([LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html)) computing platform for solving partial differential equations (PDEs). FEniCS enables users to quickly translate scientific models into efficient finite element code. With the high-level Python and C++ interfaces to FEniCS, it is easy to get started, but FEniCS offers also powerful capabilities for more experienced programmers. FEniCS runs on a multitude of platforms ranging from laptops to high-performance clusters.”
- Solves partial differential equations efficiently with a combination of C++ and Python.
- Can be run on a desktop/laptop or deployed to a supercomputer with thousands of parallel processes.
-  is a [NumFOCUS](http://www.numfocus.org/) fiscally supported project
- “makes the implementation of the mathematical formulation of a system of partial differential equations almost seamless.” - Sébastien Brisard
- “FEniCS is in fact a C++ project with a full-featured Python interface. The library itself generates C++ code on-the-fly, that can be called (on-the-fly) from python. It's almost magical... Under the hood, it used to use SWIG, and recently moved to pybind11. I guess the architecture that was set up to achieve this level of automation might be useful in other situations.” - Sébastien Brisard

**Michael #2:** [**cursive_re**](https://github.com/Bogdanp/cursive_re)

-  via [Christopher Patti](https://twitter.com/feoh), created by Bogdan Popa
- Readable regular expressions for Python 3.6 and up.
-  It’s a tiny Python library made up of combinators that help you write regular expressions you can read and modify six months down the line.
- Best understood via an example:

```
    >>> hash = text('#')
    >>> hexdigit = any_of(in_range('0', '9') + in_range('a', 'f') + in_range('A', 'F'))
    >>> hexcolor = (
    ...     beginning_of_line() + hash +
    ...     group(repeated(hexdigit, exactly=6) | repeated(hexdigit, exactly=3)) +
    ...     end_of_line()
    ... )
    >>> str(hexcolor)
    '^\\#([a-f0-9]{6}|[a-f0-9]{3})$'
```

- Has automatic escaping for `[` and `\` etc: `str(any_of(text("[]"))) → '[\\[\\]]'`
- Easily testable / inspectable. Just call `str` on any expression.

**Brian #3:**  [**pyimagesearch**](https://www.pyimagesearch.com/)

-  Adrian Rosebrock is focused on teaching OpenCV with Python
-  Just a really cool resource of integrating computer vision and Python. Both free and paid resources.
- He had one of the most successful tech learning kickstarters (ever?) on this topic: [https://www.kickstarter.com/projects/adrianrosebrock/deep-learning-for-computer-vision-with-python-eboo](https://www.kickstarter.com/projects/adrianrosebrock/deep-learning-for-computer-vision-with-python-eboo)

**Michael #4:** [**Visualization of Python development up till 2012**](https://www.youtube.com/watch?v=cNBtDstOTmA)

-  via [Ophion Group (on twitter)](https://twitter.com/OphionGroup)
- mercurial (hg) source code repository commit history 
- August 1990 - June 2012 (cpython 3.3.0 alpha)
- Watch the first minute, then click ahead minute at a time and watch for a few seconds to get the full feel 
- Really interesting to see a visual representation of the growth of an open source ecosystem
- Built with Gource: [https://gource.io/](https://gource.io/)
	- Amazing video of the history gource and its visualization of various projects: [https://vimeo.com/15943704](https://vimeo.com/15943704)
- Who wants to build this for 2012-present?
- Would make an amazing lightning talk!

**Brian #5:** [**Getting to 10x (Results): What Any Developer Can Learn from the Best**](https://medium.com/javascript-scene/getting-to-10x-results-what-any-developer-can-learn-from-the-best-54b6c296a5ef)

- Forget the “10x” bit if that term is fighting words.  - Brian’s advice
  - How about just “**ways to improve your effectiveness as a developer**”?
- “… there is a clear path to excellence. People aren’t born great developers. They get there through focused, deliberate practice.”
- traits of great developers
	- problem solver
	- skilled
	- mentor/teacher
	- excellent learner
	- passionate
- traits to avoid:
	- incompetent
	- arrogant
	- uncooperative
	- unmotivated
	- stubborn
- Focus on your strengths more than your weaknesses
- Pick 1 thing to improve on this week and focus on it relentlessly

**Michael #6:** [**Chaos Toolkit**](https://chaostoolkit.org)

- Chaos Engineering is the discipline of experimenting on a distributed system in order to build confidence in the system's capability to withstand turbulent conditions in production.
- Netflix uses the chaos monkey (et. al.) on their systems. Covered on [https://talkpython.fm/episodes/show/16/python-at-netflix](https://talkpython.fm/episodes/show/16/python-at-netflix) 
- The Chaos Toolkit aims to be the simplest and easiest way
- to explore building, and automating, your own Chaos Engineering Experiments.
- Integrates with Kubernetes, AWS, Google Cloud, Microsoft Azure, etc.
- To give you an idea, here are some things it can do to aws:
	- lambda: `delete_function_concurrency` Removes concurrency limit applied to the specified Lambda
	- `stop_instance` Stop a single EC2 instance. You may provide an instance id explicitly or, if you only specify the AZ, a random instance will be selected.

**Extras:** 

- MK: [Malicious Python Libraries Found & Removed From PyPI](https://www.zdnet.com/article/twelve-malicious-python-libraries-found-and-removed-from-pypi/)
- MK: [Some really long type names](https://twitter.com/tirkarthi/status/1058996814790111232)
- Brian: [Deep dive into pyproject.toml and the future of Python packaging with Brett Cannon](https://testandcode.com/52)
  - follow up from [episode 100 Python Bytes](http://pythonbytes.fm/100)

