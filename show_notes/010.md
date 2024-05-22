This is Python Bytes, Python headlines and news deliver directly to your earbuds: episode 10, recorded on **Monday, January 23rd, 2016**. [more] 

**#1 (Brian): [Advanced Time Series Plots in Python](http://www.blackarbs.com/blog/advanced-time-series-plots-in-python/1/6/2017) from blackarbs.com**

- matplotlib 2.0 official release on Jan 17
  - [mentioned it was coming in episode 7](https://pythonbytes.fm/7)
  - [matplotlib.org](http://matplotlib.org/)
- A tutorial for using pandas, numpy, matplotlib, and seaborn for collecting, analyzing, and plotting time series plots.
  - start with an empty xy chart
  - grab some yahoo finance data, do some manipulation, and plot it.
  - add shaded areas, in the example, recession times
  - chart titles
  - axis labels
  - legend styling
  - horizontal line, at the 0 value, in this example
  - formatting x and y tick labels
  - controlling the font
  - turning on data points by specifying a marker shape
  - add some chart annotations with arrows pointing to specific data points
  - add a logo and watermark over the top of everything
- [seaborn](http://seaborn.pydata.org/) is a statistical data visualization tool for use with matplotlib
- See the seaborn site has tutorials for:
  - Style functions, Color palettes, Distribution plots, Regression plots, Categorical plots, and Axis grid objects. 

**#2 (Michael):** [**Dismissing Python Garbage Collection at Instagram**](https://engineering.instagram.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172#.q23x90dch)

- By dismissing the Python garbage collection (GC) mechanism, which reclaims memory by collecting and freeing unused data, Instagram can run 10% more efficiently.
- How We Run Our Web Server: Instagram’s web server runs on Django in a multi-process mode with a master process that forks itself to create dozens of worker processes that take incoming user requests. For the application server, we use uWSGI with pre-fork mode to leverage memory sharing between master and worker processes. 
- Attempt 1: Disable reference count on code objects (no effect)
- Attempt 2: Let’s try disabling GC
  -  With that, we successfully raised the shared memory of each worker process from 140MB to 225MB, and the total memory usage on the host dropped by 8GB per machine. This saved 25% RAM for the whole Django fleet. With such big head room, we're capable of running a lot more processes or running with a much higher RSS memory threshold. In effect, this improves the throughput of Django tier by more than 10%.
- Attempt 3: Completely shutdown GC takes churns (bad)
- Attempt 4: Final step for shutting down GC: No cleanup (success)

**#3 (Brian): [My experience with type hints and mypy](https://snarky.ca/my-experience-with-type-hints-and-mypy/)**

Brett Cannon on his blog [snarky.ca](https://snarky.ca/my-experience-with-type-hints-and-mypy/)

- Here's an example including the pull request of changes, of a project adding static types and static analysis of those types.
- Trying to use type hints to increase code quality and readability for a project.
- The project is CLA enforcement bot for the PSF, to make sure that all pull requests contributions to a python project is done by someone who has signed a PSF Contributor Licence Agreement.
- Process
  - Run mypy against your code with no types, then slowly add types, one object at a time.
  - [mypy](http://mypy-lang.org/) is a static analysis tool to make sure your typehints are correct. 
- Issues:
  - supports Python 3.5, but not new types in Python 3.6, specifically typying. Collection. Workaround was to use typing.AbstractSet
  - f-strings not supported yet, but coming
  - Skipped type hinting for test suite. 
    - It wouldn't occur to me to even try to add static types to tests.
  - Most linters would have caught the problems as well as mypy.
- Benefit
  - The act of adding static types increased the readability of the code. Did not detract from readability.
  - “What mypy really got me was better documentation. While I was adding the type hints there were a couple of times where I had to examine the code to realize what the appropriate type was. Now that I have the functions and methods all hinted I don't have to guess anymore. That should make long-term maintenance a bit easier”
- Conclusion
  "…would I bother typing new Python 3 code? … yes once mypy supports f-strings. 
  “When I design an API I already have to think about what type of objects would be acceptable, so quickly writing down my assumptions doesn't hurt anything, it's relatively quick, and it benefits anyone having to work with my code. But I also wouldn't contort my code to fit within the confines of type hints (i.e. if type hints forces me to write cleaner code then that's great, but if something is so dynamic that it can't have type hints then that's fine and I'll happily use typing.Any as an escape hatch). “
  “In the end I view type hints as enhanced documentation that has tooling to help verify that the documentation about types is accurate. And for that use-case I see type hints worth doing and not at all a burden.”

**#4 (Michael):** [**Understanding the underscore( _ ) of Python**](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc#.imwnkwoux)

- The *underscore* (_) is special in Python.
-  If you are python programmer, for _ in range(10) , __init__(self) like syntax may be familiar.
- There are 5 cases for using the underscore in Python.
  - For storing the value of last expression in interpreter.
  - For ignoring the specific values. (so-called “I don’t care”)
  - To give special meanings and functions to name of vartiables or functions.
    - _protected-ish, __*private-ish, conflicting: in_*, __magic__
  - To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
  - To separate the digits of number literal value.

**#5: (Brian): [PEP 541 -- Package Index Name Retention](https://www.python.org/dev/peps/pep-0541/)**
Draft status currently; was just submitted on the 12th by Donald Stufft.
“ Abstract:
This PEP proposes an extension to the Terms of Use of the Package Index, clarifying expectations of package owners regarding ownership of a package name on the Package Index, specifically with regards to conflict resolution.

Existing package repositories such as CPAN , NPM , and GitHub will be investigated as prior art in this field.

Rationale
Given that package names on the Index are sharing a single flat namespace, a unique name is a finite resource. The growing age of the Package Index causes a constant rise of situations of conflict between the current use of the name and a different suggested use of the same name.

This document aims to provide general guidelines for solving the most typical cases of such conflicts.”

**#6 (Michael):** [**Hackers downloaded US government climate data and stored it on European servers as Trump was being inaugurated**](https://flipboard.com/@flipboard/flip.it%2FIRwdse-hackers-downloaded-us-government-climat/f-1d75a23f08%2Fqz.com)

- As Donald Trump was sworn into office as the new president of the US on Jan. 20, a group of around 60 programmers and scientists were gathered in the Department of Information Studies building at the University of California-Los Angeles, harvesting government data.
- A spreadsheet detailed their targets: 
  - Webpages dedicated to the Department of Energy’s solar power initiative
  - Energy Information Administration data sets that compared fossil fuels to renewable energy sources
  - fuel cell research from the National Renewable Energy Laboratory, to name a few out of hundreds.
- Volunteer “data rescue” events in Toronto, Philadelphia, Chicago, Indianapolis, and Michigan over the last few weeks have managed to scrape hundreds of thousands of pages off of EPA.gov, NASA.gov, DOE.gov, and whitehouse.gov, uploading them to the Internet Archive. Another is planned for early February at New York University.
- Suddenly, at exactly noon on Friday as Trump was sworn in, and just as the UCLA event kicked off, some of their fears began to come true: The climate change-related pages on whitehouse.gov disappeared.
- There will, thanks to Michael Riedyk, CEO of the Canadian data-archiving company Page Freezer, also be a copy stored outside the US.