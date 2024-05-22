# Python Bytes 215
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: [**Jason McDonald**](https://twitter.com/codemouse92)

**Michael #1:** [**5 ways I use code as an astrophysicist**](https://www.youtube.com/watch?v=bxWrXhLFN2s)

- Video by [**Dr. Becky**](https://twitter.com/drbecky_) (i.e. Dr Becky Smethurst, an astrophysicist at the University of Oxford)
- She has a [great YouTube channel](https://www.youtube.com/channel/UCYNbYGl89UUowy8oXkipC-Q) to check out.
- #1: Image Processing (of galaxies from telescopes)
	- Noise removal
- #2: Data analysis
	- Image features (brightness, etc)
	- One example: 600k “rows” of galaxy properties
- #3: Model fitting
	- e.g. linear fit (visually as well through jupyter)
	- e.g. Galaxies and their black holes grow in mass together
	- Color of galaxies & relative star formation
- #4: Data visualization
- #5: Simulations
	- Beautiful example of galaxies colliding
	- Star meets black hole

**Brian #2:** [**A Visual Intro to NumPy and Data Representation**](http://jalammar.github.io/visual-numpy/)

- [Jay Alammar](https://twitter.com/JayAlammar)
- I’ve started using numpy more frequently in my own work.
- Problem: I think of np.array like a Python list. But that’s not right.
- This visualization guide helped me think of them differently.
- Covers:
	- arrays
		- creating arrays (I didn’t know about np.ones(), np.zeros(), or np.random.random(), so cool)
		- array arithmetic
		- indexing and slicing
		- aggregation with min, max, sum, mean, prod, etc.
	- matrices : 2D arrays
		- matrix arithmetic
		- dot product (with visuals, it takes seconds to understand)
		- matrix indexing and slicing
		- matrix aggregation (both all entries and column or row with axis parameter)
		- transposing and reshaping
	- ndarray: n-dimensional arrays
	- transforming mathematical formulas to numpy syntax
	- data representation
- All with excellent drawings to help visualize the concept.

**Jason #3:** **Qt 6 release (including PySide2)**

- Qt 6.0 released on December 8: [https://www.qt.io/blog/qt-6.0-released](https://www.qt.io/blog/qt-6.0-released)
	- 3D Graphics abstraction layer called RHI (Rendering Hardware Interface), eliminating hard dependency on OpenGL, and adding support for DirectX, Vulkan, and Metal. Uses native 3D graphics on each device by default.
	- Property bindings: [https://www.qt.io/blog/property-bindings-in-qt-6](https://www.qt.io/blog/property-bindings-in-qt-6)
	- A bunch of refactoring to improve performance.
	- QtQuick styling
	- CAUTION: Many Qt 5 add-ons not yet supported!! They plan to support by 6.2 (end of September 2021).
	- Pay attention to your 5.15 deprecation warnings; those things have now been removed in 6.0.
- PySide6/Shiboken6 released December 10: [https://www.qt.io/blog/qt-for-python-6-released](https://www.qt.io/blog/qt-for-python-6-released)
	- New minimum version is Python 3.6, supported up to 3.9.
	- Uses properties instead of (icky) getters/setters now. (Combine with snake_case support from 5.15.2)

```
    from __feature__ import snake_case, true_property
```

- PyQt6 also just released, if you prefer Riverbank’s flavor. (I prefer official.)

**Michael #4:** [**Is your GC hyper active? Tame it!**](https://twitter.com/mkennedy/status/1339657542591336448)

- Let’s think about `gc.get_threshold()`.
- Returns `(700, 10, 10)` by default. That’s read roughly as:
	- For every net 700 allocations of a collection type, a gen 0 collection runs
	- For every gen 0 collection run, 1/10 times it’ll be upgraded to gen 1.
	- For every gen 1 collection run, 1/10 times it’ll be upgraded to gen 2. Aka for every 100 gen 0 it’s upgraded to gen 2.
- Now consider this:

```
    query = PageView.objects(created__gte=yesterday).all()
    data = list(query)  # len(data) = 1,500
```

- That’s multiple GC runs. We’ve allocated at least 1,500 custom objects. Yet never ever will any be garbage.
- But we can adjust this. Observe with `gc.set_debug(gc.DEBUG_STATS)` and consider this ONCE at startup:

```
    # Clean up what might be garbage
    gc.collect(2)
    # Exclude current items from future GC.
    gc.freeze()
    
    allocs, gen1, gen2 = gc.get_threshold()
    allocs = 50_000  # Start the GC sequence every 10K not 700 class allocations.
    gc.set_threshold(allocs, gen1, gen2)
    print(f"GC threshold set to: {allocs:,}, {gen1}, {gen2}.")
```

- May be better, may be worse. But our pytest integration tests over [at Talk Python Training](https://training.talkpython.fm/) run 10-12% faster and are a decent stand in for overall speed perf.
- Our sitemap was doing 77 GCs for a single page view (77!), now it’s 1-2.

**Brian #5:** [**Top 10 Python libraries of 2020**](https://tryolabs.com/blog/2020/12/21/top-10-python-libraries-of-2020/)

- tryolabs
- criteria
	- They were launched or popularized in 2020.
	- They are well maintained and have been since their launch date.
	- They are outright cool, and you should check them out.

General interest:

1. [Typer](https://github.com/tiangolo/typer) : FastAPI for CLI applications
	- I can’t believe first commit was right before 2020. 
	- Just about a year after the introduction of FastAPI, if you can believe it.
	- [Sebastián Ramírez](https://github.com/tiangolo) is on 🔥 
2. [Rich](https://github.com/willmcgugan/rich) : rich text and beautiful formatting in the terminal.
	- [Will McGugan](https://github.com/willmcgugan)
	- yep. showed up in 2020, amazing.
3. [Dear PyGui](https://github.com/hoffstadt/DearPyGui) : Python port of the popular [**Dear ImGui**](https://github.com/ocornut/imgui) C++ project.
4. [PrettyErrors](https://github.com/onelivesleft/PrettyErrors) : transforms stack traces into color coded, well spaced, easier to read stack traces.
5. [Diagrams](https://github.com/mingrammer/diagrams) : lets you draw the cloud system architecture without any design tools, directly in Python code.

Machine Learning:

6. [Hydra](https://hydra.cc/) and [OmegaConf](https://github.com/omry/omegaconf)
7. [PyTorch Lightning](https://github.com/PyTorchLightning/PyTorch-lightning)
8. [Hummingbird](https://github.com/microsoft/hummingbird)
9. [HiPlot](https://github.com/facebookresearch/hiplot) : plotting high dimensional data

Also general

10. [Scalene](https://github.com/emeryberger/scalene) : CPU and memory profiler for Python scripts capable of correctly handling multi-threaded code and distinguishing between time spent running Python vs. native code, without having to modify your code to use it.

**Jason #6:** **[Adoption of pyproject.toml — why is this so darned controversial?](https://github.com/carlosperate/awesome-pyproject/)**

The goal of this file is to have a single standard place for all Python tool configurations. It was introduced in PEP 518, but the community seems divided over standardizing.

A bunch of tools are lagging behind others in implementing. Tracked in this repo

A few of the bigger “sticking points”:

- setuptools is working on it: [https://github.com/pypa/setuptools/issues/1688](https://github.com/pypa/setuptools/issues/1688)
- MyPy: GVR says it “doesn’t solve anything” and closed the PR. [https://github.com/python/mypy/issues/5205](https://github.com/python/mypy/issues/5205)
- Flake8 objections: [https://gitlab.com/pycqa/flake8/-/issues/428#note_251982786](https://gitlab.com/pycqa/flake8/-/issues/428#note_251982786)
	- Lack of standard TOML parser.
	- “pip to change its behavior so mere presence of the file does not change functionality”
	- Flake9 already implemented what Flake8 wouldn’t. Is this political?
- Bandit is sitting on a PR since 2019: [https://github.com/PyCQA/bandit/issues/550](https://github.com/PyCQA/bandit/issues/550)
- ReadTheDocs: It’s too much work? — [https://github.com/readthedocs/readthedocs.org/issues/7065](https://github.com/readthedocs/readthedocs.org/issues/7065)
- PyOxidizer (shockingly), silent on the topic since 2019: [https://github.com/indygreg/PyOxidizer/issues/93](https://github.com/indygreg/PyOxidizer/issues/93)

Extras:

Michael:

- [PyXLL for Excel people,](https://www.pyxll.com/) including [Python Jupyter Notebooks in Excel](https://www.pyxll.com/blog/python-jupyter-notebooks-in-excel).
- Django 3.1.5 Released
- Python 3.10.0a4 Is Now Available for Testing
- SciPy 1.6.0 Released
- M1 + PyCharm fast? [Example](https://www.dropbox.com/s/25ibecobry82imm/load-pycharm-project-speed.mp4?dl=0).
- Flying solo with the M1 too - apparently 75% is shutdown time for my MBP!

Joke

“Why did the programmer always refuse to check his code into the repository? He was afraid to commit.”
