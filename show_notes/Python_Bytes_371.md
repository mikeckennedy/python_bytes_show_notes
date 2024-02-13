# Python Bytes 371

Sponsored by ScoutAPM: [pythonbytes.fm/scout](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**AppleCrate**](https://fosstodon.org/@RhetTbull/111876913345192826)

- By [Rhet Turnbull](https://fosstodon.org/@RhetTbull/111876913345192826) (from [Building macOS Apps episode](https://talkpython.fm/episodes/show/383/textinator-and-building-macos-apps-with-python))
- AppleCrate is a tool for creating native macOS installers for your command line tools. 
- It's useful for creating installers for command line tools written in any language. 
- Tools written in interpreted languages like Python will need to be first processed with a tool like pyinstaller to create a standalone executable.
- AppleCrate uses [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) templates to generate the files required for the installer. This allows you to use template variables in your files or command line parameters to customize the installer. 

**Brian #2:** [**One way to package Python code right now**](https://nedbatchelder.com/blog/202402/one_way_to_package_python_code_right_now.html?utm_source=pocket_reader)

- Ned Batchelder
- An example repo with all the parts for package
- A lot of discussion and what to think about in the README (unfortunately rst and not md, but we can’t have everything)
- Includes
    - pyproject.toml
    - dev-requirements.txt
    - README.rst
    - Makefile
    - LICENSE.txt
    - .bitignore
    - .editorconfig
        - see https://editorconfig.org
- Shout out to to [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) on python.org, which is pretty good

**Michael #3:** [**Flask8 but why?**](https://fosstodon.org/@ihor/111456123685623940)

- Ihor Kalnytskyi: Something I really like about [#ruff](https://fosstodon.org/tags/ruff), a new tool for both linting and formatting in the [#python](https://fosstodon.org/tags/python) ecosystem. You can literally pick any lint rule it supports and see both reasoning and examples.
- Ruff supports over 700 lint rules, many of which are inspired by popular tools like Flake8, isort, pyupgrade, and others. 

**Brian #4:** **Extra, Extra, Extra**

- [Flat.app](https://flat.app/) 
    - kinda like trello, etc. but a very simple interface that makes it pretty easy to use
- [tosdr.org](https://tosdr.org/en/frontpage)
    - Terms of Service; Didn’t Read
    - Kind of a wikipeda way to summarize the terms of service of different web services, and give them ratings/grades
- [Why I write](https://www.sheenaoc.com/articles/2024-02-06-why-i-write)
    - I talked about blogging more last episode. Here’s a cool write-up by Sheena O'Connell
    - reasons
        - to remember
        - to refine my thinking
        - to impact
        - to get through hard times
        - to connect
- [Three pytest Features You Will Love](https://blog.jetbrains.com/pycharm/2024/02/pytest-features/)
    - Helen Scott at JetBrains/PyCharm
    - Fixtures, Markers, Parametrize
    - Plus shoutouts to my [course](https://courses.pythontest.com/p/complete-pytest-course) and [book](https://pythontest.com/pytest-book/)

**Extras** 

Brian:

- [Wikipedia List of common misconceptions](https://en.wikipedia.org/wiki/List_of_common_misconceptions) - just for fun
- [Ear Trumpet Labs (a Potland Company) Edwina mic](https://www.eartrumpetlabs.com/products/microphones/edwina) - just something on my wish list

Michael

- [Mozilla Monitor](https://monitor.mozilla.org/)
- [Python 3.12.2](https://docs.python.org/release/3.12.2/whatsnew/changelog.html#python-3-12-2)
    - Upgraded all the Python apps (11 of them) in about 2 minutes and one command
- Got a Vision Pro? Try the [Talk Python Courses app](https://training.talkpython.fm/apps)
- Great video event: [Data Doodling with Martina Pugliese](https://www.youtube.com/watch?v=KeegA_uzzSo)

**Joke:** [Free Tier](https://ifunny.co/picture/why-would-a-fly-land-on-something-like-this-rats-7NlBlVArA?s=cl)

