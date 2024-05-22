# python bytes 46
Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1:** [**Scipy lecture notes**](http://www.scipy-lectures.org/)

- “One document to learn numerics, science, and data with Python”
- Topics
  - Python language tutorial
  - NumPy, Matplotlib, scipy
  - Debugging, optimizing, image manipulation
  - Statistics, scikit-image, scikit learn
  - 3D plotting
- Nice table of contents layout that makes it easy to jump right to whatever you need to learn.
- Just in time learning for scientific Python.

**Michael #2:** [**Building a desktop notification tool for Linux using python**](https://www.codementor.io/dushyantbgs/building-a-desktop-notification-tool-using-python-bcpya9cwh)

- The term desktop notifications refer to a graphical control element that communicates certain events to the user without forcing them to react to this notification immediately.
- Example: we are going to build a notification tool which displays the current rate of bitcoins in INR.
- Based on [notify2](https://notify2.readthedocs.io/en/latest/) package

**Brian #3****:** [**pytest-benchmark**](https://pypi.python.org/pypi/pytest-benchmark)

- Easily wrap some time constraints around some code to make sure certain parts of your system don’t slow down.
- Good table or graph based preliminary times with statistics
- Can generate golden sets of numbers, then compare against those and fail based on changes in particular stats like min, mean, etc.
- Can have max and min times for benchmarks even without previous training.
- Lots of fun flags and utilities.
- good integration with pytest


**Michael #4:** [**Alice in Python projectland**](https://veekaybee.github.io/2017/09/26/python-packaging/)

- via Vicki Boykis
- Python project structure and packaging standardization is still not a solved problem
- In the JVM, as long as you have your path structured correctly, build tools will understand it and create a package for you into an executable JAR.
- But, when I started looking for the same standardization in Python, it wasn’t as straightforward. Some questions I had as I worked: 
	  - Should I be using virtualenvs? 
	  - Pipenvs? 
	  - Setuptools? 
	  - Should I have a setup.cfg? 
	  - What are wheels, or eggs, for that matter? 
	  - Does each folder need an __init__.py? 
	  - What does that file even do? 
	  - How do I reference modules along the same PYTHONPATH?
- Hat tip to [pipreqs](https://github.com/bndr/pipreqs)
- Conclusion: Python project structure and packaging can be intimidating, but, if you take it step by step, it doesn’t have to be.

**Brian #5:** [**How to teach technical concepts with cartoons**](https://jvns.ca/teach-tech-with-cartoons/)

- Just draw more pictures.
- You don’t have to be a good artist for drawings to help with retention when you are trying to teach technical concepts.

**Michael #6:** [**Halo: Beautiful terminal spinners in Python**](https://github.com/ManrajGrover/halo)

- We’ve talk about progressbars: tqdm: https://github.com/tqdm/tqdm
- doesn’t have to be.
- Cool methods like
- `spinner.start([text])`
- `spinner.succeed([text])`
- `spinner.fail([text])`
- Windows File Progress Dialog Author: https://xkcd.com/612/

## Extras

- releases: stay current. go upgrade
	  - [Python 3.6.3 released](https://www.python.org/downloads/release/python-363/)
	  - [pytest 3.2.3 released](https://docs.pytest.org/en/latest/changelog.html)
- New Test & Code episodes 
	  - [31: I'm so sick of the testing pyramid](http://testandcode.com/31)
	  - [32: David Hussman - Agile vs Agility, Dude's Law, and more](http://testandcode.com/32)
  

