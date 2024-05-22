# Python Bytes 211 - Will a black hole devour this episode?

Sponsored by Techmeme Ride Home podcast: [**pythonbytes.fm/ride**](http://pythonbytes.fm/ride)

Special guest: [**Matthew Feickert**](https://twitter.com/HEPfeickert)

Live streamed on Youtube: **[youtube.com/watch?v=ug3OR-BQ7Hw](https://www.youtube.com/watch?v=ug3OR-BQ7Hw)**

**Brian #1:**  [**Introducing FARM Stack - FastAPI, React, and MongoDB**](https://developer.mongodb.com/how-to/FARM-Stack-FastAPI-React-MongoDB)

- Aaron Basset
- Describes a todo CRUD application, available on github, to show the concepts in action.
- Animated gif showing how to use the FastAPI interactive documentation to understand the API in a browser.
- Shows
	- How app connects to routes and endpoints.
	- The run call with uvicorn to get an async even loop going
	- Connecting to a MongoDB database
	- Defining models and how easy it is to set up a schema.
	- Discusses routes and endpoints and how to hook up all the CRUD endpoints.
	- The React bit is an application that changes as you modify the elements through the endpoint interactive session.
- Very cool way to work and get something running fast.

**Michael #2:** [**py-applescript**](https://github.com/rdhyee/py-applescript)

- How would you like to automate your mac with Python rather than the dreadful AppleScript?
- [**py-applescript**](https://github.com/rdhyee/py-applescript) is an easy-to-use Python wrapper for NSAppleScript, allowing Python scripts to communicate with AppleScripts and AppleScriptable applications.
- Features:
- Scripts may be compiled from source or loaded from disk
- Standard 'run' handler and user-defined handlers can be invoked with or without arguments
- Argument and result values are automatically converted between common Python types and their AppleScript equivalents
- Compiled scripts are persistent: handlers can be called multiple times and top-level properties retain their state
- Avoids any dependency on the legacy appscript library, flawed Scripting Bridge framework, or limited osascript executable
- The applescript package exports four classes - AppleScript, ScriptError, AEType and AEEnum - plus one constant, kMissingValue.

**Matthew #3:** [airspeed velocity](https://asv.readthedocs.io/en/stable/)

- Are you developing a tool where performance is of individual functions is key? Do you want to be able to benchmark those metrics over every commit in your project with beautiful interactive visualizations?
- From the docs:
    > **airspeed velocity** (asv) is a tool for benchmarking Python packages over their lifetime. Runtime, memory consumption and even custom-computed values may be tracked. The results are displayed in an interactive web frontend that requires only a basic static webserver to host
- Developed by a community of people that you’ll probably recognize if you hang around the SciPy and Jupyter ecosystem lead by Michael Droettboom and Pauli Virtanen
- The docs include examples for benchmarks of NumPy, SciPy, and Astropy ([example: SciPy](https://pv.github.io/scipy-bench/))
	- Example: SciPy’s [interpolate.Interpolate1d.time_interpolate](https://pv.github.io/scipy-bench/#interpolate.Interpolate1d.time_interpolate) test
    - Produces plot of timing performance across multiple parameterizations of the test
    - Click on any node in the plot and get taken directly to the commit on GitHub! 🤯 
- [Developed openly on GitHub](https://github.com/airspeed-velocity/asv)
- Up on [PyPI as asv](https://pypi.org/project/asv/)
    python -m pip install asv
- Very cute and very Pythonic joke in the test dashboards: Report title for library X is “airspeed velocity of an unladen X” 😛 

**Brian** **#4:** [**Parsecs experience with Hypothesis testing**](https://parsec.cloud/en/blog/our_experience_with_hypothesis_testing/index.html)

- Parsec blog, Parsec is a client side encrypted file sharing service .
- Discussion of their experience with Hypothesis to test a 4 year old, large, asynchronous Python project.
- In particular, an algorithm around RAID5 redundancy.
- The test needs to check that:
	- blocks can be split into chunks
	- blocks can be rebuilt from chunks
	- blocks can be rebuilt with one missing storage chunk
- Goes on to describe how they use a stateful mode of hypothesis.
- It’s a rather complex description. But very welcome.
- I’ve been waiting to hear how people are using Hypothesis for real world problems.
- Their recommendations for when to use Hypothesis:
	- If you are writing a kind of encoder/decoder. Hypothesis is simply the perfect solution for you ;-)
	- If you can write a simple oracle (or even better: you already have one available given you are reimplementing a protocol !)
	- If the work is of type "hard to compute, simple to check" 

**Michael** **#5:** [**Amazon Web Services now offers Mac instances based on Mac mini; M1 coming later**](https://arstechnica.com/gadgets/2020/12/amazon-web-services-adds-macos-on-bare-metal-to-ec2/)

- [Amazon](https://9to5mac.com/guides/amazon/) Web Services ([AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services)) is now offering [Mac](https://9to5mac.com/guides/mac/) instances to developers who want to speed up building and testing of Mac, iOS, iPadOS, watchOS and tvOS apps.
- You no longer need a Mac and macOS to build iOS apps.
- The instances are based on physical [Mac minis](https://9to5mac.com/guides/mac-mini/), and you get exclusive access to a machine while you are using it.
- Right now, Amazon is using Intel-based Mac minis, but the company says that it will have [M1 Mac minis](https://9to5mac.com/guides/m1/) available in the first half of next year. 
- Check out the [blog post](https://aws.amazon.com/blogs/aws/new-use-mac-instances-to-build-test-macos-ios-ipados-tvos-and-watchos-apps/) and the video below for more details.
- Good as a backstop until we get the newer faster M1 chips if you/your company is holding off.
- Although there's no virtualization in play here, the mac1.metal instances can be spun up and down nearly as rapidly, thanks to the AWS Nitro hardware management—which is invisible, from the customer's perspective.
- To someone who spins up a mac1.metal instance, the instance is for all intents and purposes a perfectly vanilla, brand-new Intel Mac mini.
- But there is also [macstadium](https://www.macstadium.com/pricing) at 1/10th the price.

**Matthew #6:** [visidata](https://www.visidata.org/)

- Are you doing some data analysis and get given a new CSV file? Your first instinct is to load it up into pandas, right? Wouldn’t it be nice to drop in and explore at the command line though a bit to get the lay of the land and even do some preliminary analysis?
- From the docs:
    > Data science without the drudgery!
    > 
    > VisiData is an interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease
- Supports [large number of file formats](https://www.visidata.org/formats/): 42
	- Everything from CSV and JSON through JIRA, MySQL, and PNG
- [Developed openly on GitHub](https://github.com/saulpw/visidata) by [Saul Pwanson](https://github.com/saulpw)
- On [PyPI as visidata](https://pypi.org/project/visidata/)
```
python -m pip install visidata
```
- Though as this is a Python application you probably going to want this installed regardless of the virtual environment you’re working in. Distributions of visidata are available through [the package managers you’d expect](https://www.visidata.org/install/): apt, (also nix, Guix but not yum?), Homebrew, and Conda-forge so can easily get to work on most Unix-based machines.
- Tested it with our trusty beloved tool [pipx](https://github.com/pipxproject/pipx) and that works too (thanks again Chad Smith!)
```
python -m pip install pipx
pipx ensurepath
pipx install visidata
```
- Some pretty impressive [live demo videos on the website](https://www.visidata.org/)
- visidata has come in quite handy for me on a frequent basis as I deal with JSON serializations of statistical models with hundreds of parameters. Having a way to explore those JSON files without getting visually overwhelmed is *super* nice! 

**Extras**

**Brian:**
- [PyCon US 2021](https://us.pycon.org/2021/)

**Michael:**

- [PSF Fund Raiser](https://training.talkpython.fm/python-software-foundation-fund-raiser-2020)
- [Tickets for PyCascades 2021 are now available on pretix](https://pycascades.us15.list-manage.com/track/click?u=910a586d174a45ddb1125ad4e&id=404a5a3491&e=6829c54590). Our ticket prices are $10 for students, $20 for individuals, and $50 for professional attendees.
- [Live streaming on YouTube](https://www.youtube.com/watch?v=ug3OR-BQ7Hw)!

**Matthew**:

- [Advent of Code 2020](https://adventofcode.com/) has started. Happy coding! ❄️ 
- If time (don’t want to hog or go over):
	- Follow up from [Episode 205](https://pythonbytes.fm/episodes/show/205/this-is-going-to-be-a-little-bit-awkward):
		- [awk](https://pypi.org/project/awkward/#history)[w](https://pypi.org/project/awkward/#history)[ard v1.0.0rc1 is on PyPI](https://pypi.org/project/awkward/#history)
		- pip install awkward should get what you ant by the time this show goes live (no more need for awkard0)
- Kudos to Python Bytes for making full transcripts of all the shows available for view on [pythonbytes.fm](https://pythonbytes.fm/) — this helps be more inclusive of the deaf Python community (including Matthew’s good friend and coauthor)

**Joke:**

[**How to fix any computer - via theoatmean.com**](https://theoatmeal.com/blog/fix_computer)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5fc3434c4b9b5562499664f1/f674ed39e92a13bb66d82ec5cf364e06/how-to-fix.jpg)
