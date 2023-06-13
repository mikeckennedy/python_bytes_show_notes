# Python Bytes 340

Sponsored by [**InfluxDB**](https://pythonbytes.fm/influxdata) from Influxdata.

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

[**Ask me anything episode**](https://pythonbytes.fm/ama2023): Submit your question(s) for our upcoming AMA episode: [**form here**](https://pythonbytes.fm/ama2023). Thank you!

**Brian #1:** [**PythonGUIS**](https://www.pythonguis.com)

- Martin Fitzpatrick
- A site with a collection of resources, guides, books, comparisons, etc, around GUIs in Python.
- Martin recommends starting with PyQT6
- However, there are tutorials covering
    - PyQT6
    - PySide6
    - PyQT5
    - TkInter
    - PySide
    - even Kivy

**Michael #2:** [**JupyterLab 4.0 is Here**](https://blog.jupyter.org/jupyterlab-4-0-is-here-388d05e03442)

- The next major release of our full-featured development environment
- You can upgrade by running `pip install --upgrade jupyterlab` or `conda install -c conda-forge jupyterlab`. 
- **JupyterLab is now faster**, thanks to improvements such as CSS rules optimization, CodeMirror 6, MathJax 3, and notebook windowing. JupyterLab 3 was when working with large notebooks.
- There are additional performance improvements available via opt-in settings:
    - Faster tab-switching on Chromium browsers:
    - “Settings” → “JupyterLab Shell” → switch “Hidden mode” to “contentVisibility”
    - Better performance with long notebooks:
    - “Settings” → “Notebook” → switch “Windowing mode” to “full”
- An upgraded text editor. 
- Better real time collaboration.
- **Bug fixes.** More than 100 bugs have been addressed and resolved, enhancing JupyterLab’s stability and performance. 

**Brian #3:** [**Proposing a struct syntax for Python**](https://snarky.ca/proposing-a-struct-syntax/)

- Brett Cannon
- This would be a cool syntax for a data only type: `struct Point(x: int, y: int)`
- No positional only parameters
- No inheritance
- No methods
- Instances would be immutable, so `p = Point(1, 2)` would create an object that could be used as a key.
- A data only focused set of types. 

**Michael #4:** [**Python 3.13 Removes 20 Stdlib Modules**](https://discuss.python.org/t/pep-594-has-been-implemented-python-3-13-removes-20-stdlib-modules/27124)

- via PyCoders
- From [PEP 594 – Removing dead batteries from the standard library](https://peps.python.org/pep-0594/) we’re saying goodbye to
    - `aifc`, `audioop`, `cgi`, `cgitb`, `chunk`, `crypt`, `imghdr`, `mailcap`, `msilib`, `nis`, `nntplib`, `ossaudiodev`, `pipes`, `sndhdr`, `spwd`, `sunau`, `telnetlib`, `uu`, `xdrlib`
- As well as the 2to3 program and lib2to3 module in Python.
- Python 3.12 final release is scheduled in 4 months (October 2023) and Python 3.13 final release is scheduled in 1 year and 4 months (October **2024**).

**Extras** 

Brian:

- [**Affirming your PSF Membership voting status**](https://pyfound.blogspot.com/2023/06/affirming-your-psf-membership-voting.html)
    - You have until June 15 to affirm your voting rights in the upcoming Board Election, if you care about such things.

Michael:

- [**5 Career Tips for Budding Python Developers**](https://www.youtube.com/watch?v=8DgvzwqEHUs) video
- [**PyCon US 2023 videos**](https://www.youtube.com/playlist?list=PL2Uw4_HvXqvY2zhJ9AMUa_Z6dtMGF3gtb) are up
- [**Python 3.11.4, 3.10.12, 3.9.17, 3.8.17, 3.7.17, and 3.12.0 beta 2 are now available**](https://pythoninsider.blogspot.com/2023/06/python-3114-31012-3917-3817-3717-and.html)

**Joke:** [**Snorkel not included**](https://fosstodon.org/@kimvanwyk/110501443665450503)

