# Python Bytes 286

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:** [**The Python GIL: Past, Present, and Future**](https://www.backblaze.com/blog/the-python-gil-past-present-and-future/)
- Bary Warsaw and Paweł Polewicz

**Michael #2:** [**Announcing the PyOxy Python Runner**](https://gregoryszorc.com/blog/2022/05/10/announcing-the-pyoxy-python-runner/)

- PyOxy is all of the following:
    - An executable program used for running Python interpreters.
    - A single file and highly portable (C)Python distribution.
    - An alternative `python` driver providing more control over the interpreter than what `python` itself provides.
    - A way to make some of PyOxidizer's technology more broadly available without using PyOxidizer.
- PyOxidizer is often used to generate binaries embedding a Python interpreter and a custom Python application. However, its configuration files support additional functionality, such as the ability to produce Windows MSI installers, macOS application bundles, and more.
- The `pyoxy` executable also embeds a copy of the Python standard library and imports it from memory using the [oxidized_importer](https://pyoxidizer.readthedocs.io/en/latest/oxidized_importer.html) Python extension module.

**Brian #4:** [**The unreasonable effectiveness of f‍-‍strings and re.VERBOSE**](https://death.andgravity.com/f-re)

**Michael #5:** [**PyCharm PR Management**](https://twitter.com/mkennedy/status/1471606340619419652)

- Really nice but not very discoverable
- Not covered in [the docs](https://www.jetbrains.com/pycharm/features/tools.html), but super useful.
- Available in pro and free community edition
- Steps
    - Open a project that has an associated github git repo
    - If the GitHub repo has a PR, you’ll see it in the Pull Requests tab.
    - Browse the PRs, and open them for details
    - There you can see the comments, close or merge it, and more
    - Most importantly, check it out to see how it works

 
**Extras** 

Brian:

- [**Pandas Tutor: Using Pyodide to Teach Data Science at Scale**](https://blog.pyodide.org/posts/pandastutor/)

Michael:

- [**Python + pyscript + WebAssembly: Python Web Apps, Running Locally with pyscript video**](https://www.youtube.com/watch?v=lC2jUeDKv-s) is out
- And an [**iOS Python Apps video**](https://youtu.be/Nct0usblj64) too

**Joke:** 

[**Losing an orm**](https://twitter.com/btskinn/status/1526583946372317184?s=12&t=tc8OsqCRA9o-20wgFMqXHA)!

![](https://paper-attachments.dropbox.com/s_8D63881203B6B9B83341B9CED474611E85FBFC726008DD91E14C0FB9110B49B3_1653978086388_joke_1.jpeg)
