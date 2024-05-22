# Python Bytes 115
Sponsored by [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

Special guest: [Nina Z](https://twitter.com/nnja)[akharenko](https://twitter.com/nnja)

**Brian #1:** [**Great Expectations**](https://great-expectations.readthedocs.io/en/latest/)

- A set of tools intended for batch time testing of data pipeline data.
- Introduction to the problem doc: [Down with Pipeline debt / Introducing Great Expectations](https://medium.com/@expectgreatdata/down-with-pipeline-debt-introducing-great-expectations-862ddc46782a)
- `expect_<something>()` methods that return json formatted descriptions of whether or not the passed in data matches your expectations.
- Can be used programmatically or interactively in a notebook. ([video demo](https://www.youtube.com/watch?v=-_0tG7ACNU4)).
- For programmatic use, I’m assuming you have to put code in place to stop a pipeline stage if expectations aren’t met, and write failing json result to a log or something.
- Examples, just a few, full list is big:
	- Table shape: 
		- expect_column_to_exist, expect_table_row_count_to_equal
- Missing values, unique values, and types: 
		- expect_column_values_to_be_unique, expect_column_values_to_not_be_null
	- Sets and ranges
		- expect_column_values_to_be_in_set
	- String matching
		- expect_column_values_to_match_regex
	- Datetime and JSON parsing
	- Aggregate functions
		- expect_column_stdev_to_be_between
	- Column pairs
	- Distributional functions
		- expect_column_chisquare_test_p_value_to_be_greater_than

**Nina #2:** **Using CircuitPython and MicroPython to write Python for wearable electronics and embedded platforms**

- I’ve been playing with electronics projects as a hobby for the past two years, and a few months ago turned my attention to Python on microcontrollers
- [MicroPython](http://micropython.org/) is a lean and efficient implementation of Python3 that can run on microcontrollers with just 256k of code space, and 16k of RAM. [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) is a port of MicroPython, optimized for Adafruit devices. 
- Some of the devices that run Python are as [small as a quarter](https://www.adafruit.com/product/3500).
- My favorite Python hardware platform for beginners is [Adafruit’s Circuit PlayGround Express](https://www.adafruit.com/product/3333). It has everything you need to get started with programming hardware without soldering. All you’ll need is alligator clips for the conductive pads.
	- The board features NeoPixel LEDs, buttons, switches, temperature, motion, and sound sensors, a tiny speaker, and lots more. You can even use it to control servos, tiny motor arms.
  - Best of all, it only costs $25.
- If you want to program the Circuit PlayGround Express with a drag-n-drop style scratch-like interface, you can use [Microsoft’s MakeCode](https://makecode.adafruit.com/). It’s perfect for kids and you’ll find lots of examples on their site.
- Best of all, there are tons of [guides for Python projects](https://learn.adafruit.com/category/circuitpython) to build on their website, from making your own synthesizers, to jewelry, to silly little robots. 
- Check out the [repo](https://github.com/nnja/pyearrings) for my Python-powered earrings, see a [photo](https://twitter.com/nnja/status/1074771014838448128), or a [demo](https://twitter.com/nnja/status/1054728692067393536). 
- Sign up for the Adafruit Python for Microcontrollers mailing list [here](https://www.adafruitdaily.com/), or see the archives [here](https://www.adafruitdaily.com/category/circuitpython/). 

**Michael #3**: [**Dataclass CSV reader**](https://github.com/dfurtado/dataclass-csv)

- Map CSV to Data Classes 
- You probably know about reading CSV files
	- Maybe as tuples
	- Better with csv.DictReader
- This library is similar but maps Python 3.7’s data classes to rows of CSV files
- Includes type conversions (say string to int)
- Automatic type conversion. `DataclassReader` supports `str`, `int`, `float`, `complex` and `datetime`
- `DataclassReader` use the type annotation to perform validation of the data of the CSV file.
- Helps you troubleshoot issues with the data in the CSV file. `DataclassReader` will show exactly in which line of the CSV file contain errors.
- Extract only the data you need. It will only parse the properties defined in the `dataclass`
- It uses `dataclass` features that let you define metadata properties so the data can be parsed exactly the way you want.
- Make the code cleaner. No more extra loops to convert data to the correct type, perform validation, set default values, the `DataclassReader` will do all this for you
- Default fallback values, more.

**Brian #4:** [**How to Rock Python Packaging with Poetry and Briefcase**](https://dan.yeaw.me/posts/python-packaging-with-poetry-and-briefcase/)

- Starts with a discussion of the packaging (for those readers that don’t listen to Python Bytes, I guess.) However, it also puts flit, pipenv, and poetry in context with each other, which is nice.
- Runs through a tutorial of how to build a pyproject.toml based project using poetry and briefcase.
- We’ve talked about Poetry before, on [episode 100](https://pythonbytes.fm/100).
- pyproject.toml is discussed extensively on [Test & Code 52](https://testandcode.com/52).
- [briefcase](https://github.com/pybee/briefcase) is new, though, it’s a project for creating standalone native applications for Mac, Windows, Linux, iOS, Android, and more.
- The tutorial also discusses using poetry directly to publish to the test-pypi server. This is a nice touch. Use the test-pypi before pushing to the real pypi. Very cool.


**Nina #5:** [**awesome-python-security**](https://github.com/guardrailsio/awesome-python-security) ****🕶🐍🔐**, a collection of tools, techniques, and resources to make your Python more secure**

- All of your production and client-facing code should be written with security in mind
- This list features a few resources I’ve heard of such as [Anthony Shaw’s excellent 10 common security gotchas article](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03) which highlights problems like input injection and depending on assert statements in production, and a few that are new to me:
- [OWASP (Open Web Application Security Project) Python Resources](http://www.pythonsecurity.org/) at pythonsecurity.org
- [bandit](https://github.com/PyCQA/bandit) a tool to find common security issues in Python
	- bandit features a lot of useful plugins, that test for issues like:
		- hardcoded password strings
		- leaving flask debug on in production
		- using exec() in your code
		- [& more](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing)
- [detect-secrets](https://libraries.io/pypi/detect-secrets), a tool to detect secrets left accidentally in a Python codebase
- & lots more like resources for learning about security concepts like cryptography
- See the [full list](https://github.com/guardrailsio/awesome-python-security) for more

**Michael #6: [pydbg**](https://github.com/tylerwince/pydbg)

- Python implementation of the Rust `dbg` macro
- Best seen with an example. Rather than printing things you want to inspect, you:

```
    a = 2
    b = 3
    
    dbg(a+b)
    
    def square(x: int) -> int:
        return x * x
    
    dbg(square(a))
```

outputs:

```
    [testfile.py:4] a+b = 5
    [testfile.py:9] square(a) = 4
```

**Extras:**

**Brian:**

- pathlib + pytest tmpdir → tmp_path & tmp_path_factory
  - [https://docs.pytest.org/en/latest/tmpdir.html](https://docs.pytest.org/en/latest/tmpdir.html)
  - These two new fixtures (as of pytest 3.9) act like the good old tmpdir and tmpdir_factory, but return pathlib Path objects. Awesome.

**Michael:** 

- [*The Art of Python*](https://www.papercall.io/art-of-python) is a miniature arts festival at [PyCon North America 2019](https://us.pycon.org/), focusing on narrative, performance, and visual art. We intend to encourage and showcase novel art that helps us share our emotionally charged experiences of programming (particularly in Python). We hope that by attending, our audience will discover new aspects of empathy and rapport, and find a different kind of delight and perspective than might otherwise be expected at a large conference.
- StackOverflow Survey is Open! [https://stackoverflow.az1.qualtrics.com/jfe/form/SV_1RGiufc1FCJcL6B](https://stackoverflow.az1.qualtrics.com/jfe/form/SV_1RGiufc1FCJcL6B) 
- [NumPy Is Awaiting Fix for Critical Remote Code Execution Bug](https://www.bleepingcomputer.com/news/security/numpy-is-awaiting-fix-for-critical-remote-code-execution-bug/)
	- via Doug Sheehan
	- The issue was raised on January 16 and affects [NumPy](https://pypi.org/project/numpy/) versions 1.10 (released in 2015) through 1.16, which is the latest release at the moment, released on January 14
	- The problem is with the '[pickle](https://pythontips.com/2013/08/02/what-is-pickle-in-python/)' module, which is used for transforming Python object structures into a format that can be stored on disk or in databases, or that allows delivery across a network.
	- The issue was [reported](https://github.com/numpy/numpy/issues/12759) by security researcher [Sherwel Nan](https://github.com/nanshihui), who says that if a Python application loads malicious data via the `numpy.load` function  an attacker  can obtain remote code execution on the machine.
- Get your google data
	- All google docs in MS Office format via [https://takeout.google.com/settings/takeout](https://takeout.google.com/settings/takeout)
	- All Gmail in MBOX format from there as well
	- Hint: Start with nothing selected ;)

**Nina**:

- I’m teaching a two day [Intro](https://frontendmasters.com/workshops/intro-to-python/) and [Intermediate](https://frontendmasters.com/workshops/intermediate-python/) Python course on March 19th and 20th. The class will live-stream for **free** [here](https://frontendmasters.com/) on each day of or join in-person from downtown Minneapolis. All of the course materials will be released for free as well.
- I recently recorded a series of videos with Carlton Gibson (Django maintainer) on developing Django Web Apps with VS Code, deploying them to Azure with a few clicks, setting up a Continuous Integration / Continuous Delivery pipeline, and creating serverless apps. Watch the series here: [https://aka.ms/python-videos](https://aka.ms/python-videos)
- I’ll be a mentor at a brand new hatchery event at PyCon US 2019, mentored sprints for diverse beginners organized by Tania Allard. The goal is to help underrepresented folks at PyCon contribute to open source in a supportive environment. The details will be located [here](https://us.pycon.org/2019/hatchery/mentoredsprints/) (currently a placeholder) when they’re finalized.
- Catch my talk about [electronics projects in Python with LEDs at PyCascades](https://2019.pycascades.com/talks/light-up-your-life-with-python-and-leds/) in Seattle on February 24th. Currently tickets are still for sale. 
- If you haven’t tried the [Python extension for VS Code](https://code.visualstudio.com/docs/languages/python?WT.mc_id=pythonbytes-podcast-ninaz), now is a great time. The [December release](https://blogs.msdn.microsoft.com/pythonengineering/2018/12/13/python-in-visual-studio-code-december-2018-release/?WT.mc_id=pythonbytes-podcast-ninaz) included some killer features, such as remote Jupyter support, and exporting Python files as Jupyter notebooks. Keep up with future releases at the [Python at Microsoft blog](https://blogs.msdn.microsoft.com/pythonengineering/?WT.mc_id=pythonbytes-podcast-ninaz). 

Jokes:

- Q: What do you call a snake that only eats desert? A: A pie-thon. (might not make sense read out loud)
- Q: How do you measure a python? A: In inches. They don't have any feet! 
- Q: What is a python’s favorite subject? Hiss-tory! 
