# Python Bytes 255

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Will McGugan**

**Michael #****1****:** [**Wrapping C++ with Cython**](https://azhpushkin.me/posts/cython-cpp-intro)

- By [Anton Zhdan-Pushkin](https://azhpushkin.me/)
- A small series showcasing the implementation of a Cython wrapper over a C++ library.
- C library: **yaacrl - Y**et **A**nother **A**udio **R**ecognition **L**ibrary is a small Shazam-like library, which can recognize songs using a small recorded fragment.
- For Cython to consume yaacrl correctly, we need to “teach” it about the API using `cdef extern 
- It is convenient to put such declarations in `*.pxd` files.
- One of the first features of Cython that I find extremely useful — aliasing. With aliasing, we can use names like `Storage` or `Fingerprint` for Python classes without shadowing original C++ classes.
- **Implementing a wrapper: pyaacrl** - The most common way to wrap a C++ class is to use [Extension types](https://docs.python.org/3/extending/newtypes_tutorial.html). As an extension type a just a C struct, it can have an underlying C++ class as a field and act as a proxy to it.
- Cython documentation has a whole page dedicated to the pitfalls of [“Using C++ in Cython](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html).”
- Distribution is hard, but there is a tool that is designed specifically for such needs: scikit-build.
- [**PyBind11 too**](https://pybind11.readthedocs.io/en/stable/)

**Brian #****2****:** **** ****[**tbump**](https://github.com/dmerejkowsky/tbump) [](https://github.com/dmerejkowsky/tbump)[**: bump software releases**](https://github.com/dmerejkowsky/tbump)

- [suggested by Sephi Berry](https://twitter.com/geosephi/status/1437697175987920896)
- limits the manual process of updating a project version
- `tbump init 1.2.2` initializes a `tbump.toml` file with customizable settings
    - `--pyproject` will append to `pyproject.toml` instead
- `tbump 1.2.3` will 
    - patch files: wherever the version listed
    - (optional) run configured commands before commit
        - failing commands stop the bump.
    - commit the changes with a configurable message
    - add a version tag
    - push code
    - push tag
    - (optional) run post publish command
    - Tell you what it’s going to do before it does it. (can opt out of this check)
- pretty much everything is customizable and configurable.
- I tried this on a flit based project. Only required one change
    # For each file to patch, add a [[file]] config
    # section containing the path of the file, relative to the
    # tbump.toml location.
    [[file]]
    src = "pytest_srcpaths.py"
    search = '__version__ = "{current_version}"'
- cool example of a pre-commit check:
    #  [[before_commit]]
    #  name = "check changelog"
    #  cmd = "grep -q {new_version} Changelog.rst"

**Will #3:** ****https://closember.org/ by **Matthias Bussonnier**


**Michael #****4****:**  [**scikit learn goes 1.0**](https://twitter.com/btskinn/status/1441597030934011909?s=12)

- via Brian Skinn
- The library has been stable for quite some time, releasing version 1.0 is recognizing that and signalling it to our users.
- Features:
- Keyword and positional arguments - To improve the readability of code written based on scikit-learn, now users have to provide most parameters with their names, as keyword arguments, instead of positional arguments.
- Spline Transformers - One way to add nonlinear terms to a dataset’s feature set is to generate spline basis functions for continuous/numerical features with the new `[SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer)`.
- Quantile Regressor - Quantile regression estimates the median or other quantiles of Y conditional on X
- Feature Names Support - When an estimator is passed a [pandas’ dataframe](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe) during [fit](https://scikit-learn.org/stable/glossary.html#term-fit), the estimator will set a `feature_names_in_` attribute containing the feature names.
- A more flexible plotting API
- Online One-Class SVM
- Histogram-based Gradient Boosting Models are now stable
- Better docs


**Brian #****5****:**  ****[**Using devpi as an offline PyPI cache**](https://blog.jaraco.com/devpi-as-offline-pypi-cache/)

- Jason R. Coombs
- This is the devpi tutorial I’ve been waiting for.
- Single machine local server mirror of PyPI (mirroring needs primed), usable in offline mode.
    $ pipx install devpi-server
    $ devpi-init
    $ devpi-server
- now in another window, prime the cache by grabbing whatever you need, with the index redirected
    (venv) $ export PIP_INDEX_URL=http://localhost:3141/root/pypi/
    (venv) $ pip install pytest, ...
- then you can restart the server anytime, or even offline
     $ devpi-server --ofline
- tutorial includes examples, proving how simple this is.


**Will #6:** ****https://github.com/wasi-master/pypi-command-line PyPi command line 


**Extras**

Brian:

- I’ve started using pyenv on my Mac just for downloading Python versions. Verdict still out if I like it better than just downloading from pytest.org. 
- Also started using [Starship](https://starship.rs/) with no customizations so far. I’d like to hear from people if they have nice Starship customizations I should try.
- [vscode.dev](https://vscode.dev/) is a thing, [announcement](https://code.visualstudio.com/blogs/2021/10/20/vscode-dev) just today 

Michael:

- PyCascades [**Call for Proposals**](https://bit.ly/pycascades2022cfp) is currently open 
- Got your [**M1 Max**](https://www.apple.com/macbook-pro-14-and-16/)?
- Prediction: Tools like [**Crossover for Windows apps**](https://www.codeweavers.com/crossover) will become more of a thing.

Will: 

- GIL removal 
    - https://docs.google.com/document/u/0/d/18CXhDb1ygxg-YXNBJNzfzZsDFosB5e6BfnXLlejd9l0/mobilebasic?urp=gmail_link
    - https://lwn.net/SubscriberLink/872869/0e62bba2db51ec7a/
- [vscode.dev](https:///vscode.dev)

**Joke:** 

- [**The torture never stops**](https://devops.com/the-torture-never-stops/)
- [**IE (“Safari”) Eating Glue**](http://www.zaphinath.com/wp-content/uploads/2015/11/ie-eats-glue.jpg)

