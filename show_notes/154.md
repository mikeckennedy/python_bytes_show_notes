# Python Bytes 154

Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog) 

**Brian #1:** [**Lesser Known Coding Fonts**](https://vfoley.xyz/lesser-known-coding-fonts/)

- Interesting examination of some coding fonts.
- Link to a great talk called [Cracking the Code](https://www.youtube.com/watch?v=SzC3qTo0p1k), by Jonathan David Ross, about coding fonts and Input.

I’m trying out Input Mono right now, and quite like it.

- Fira code: [https://github.com/tonsky/FiraCode](https://github.com/tonsky/FiraCode) 

**Bob #2:** [**Django Admin Handbook**](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)

- As a Django developer knowing the admin is pretty important.
- Free ebook of 40 or so pages, you can consume it in one evening.
- There are a lot of good tricks, 3 I liked:
	- [How to optimize queries in Django admin](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/optimize_queries.html) (override *get_queryset*)
	- [How to export CSV from Django admin](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html) (useful for data analysis in Jupyter for example) 
	- [How to override save behaviour for Django admin](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/override_save.html) (used this to notify users upon publishing a new exercise on our platform)
- Some more cool ebooks on that site, e.g. [Tweetable #Python](https://books.agiliq.com/projects/tweetable-python/en/latest/).

**Michael #3:** [**Your Guide to the CPython Source Code**](https://realpython.com/cpython-source-code-guide/)

- Let’s talk about exploring the CPython code
- You’ll want to get the code: `git clone https://github.com/python/cpython`
- Compile the code (Anthony gives lots of steps for macOS, Windows, and Linux)
- Structure:

```
    cpython/
    │
    ├── Doc      ← Source for the documentation
    ├── Grammar  ← The computer-readable language definition
    ├── Include  ← The C header files
    ├── Lib      ← Standard library modules written in Python
    ├── Mac      ← macOS support files
    ├── Misc     ← Miscellaneous files
    ├── Modules  ← Standard Library Modules written in C
    ├── Objects  ← Core types and the object model
    ├── Parser   ← The Python parser source code
    ├── PC       ← Windows build support files
    ├── PCbuild  ← Windows build support files for older Windows versions
    ├── Programs ← Source code for the python executable and other binaries
    ├── Python   ← The CPython interpreter source code
    └── Tools    ← Standalone tools useful for building or extending Python
```

- Some cool “hidden” goodies. For example, check out `Lib/concurrent/futures/process.py`, it comes with a cool ascii diagram of the process.
- Lots more covered, that we don’t have time for
    - The Python Interpreter Process
    - The CPython Compiler and Execution Loop
    - Objects in CPython
    - The CPython Standard Library
    - Installing a custom version

**Brian #4:** [**Six Django template tags not often used in tutorials**](https://medium.com/@highcenburg/django-template-tags-not-often-used-in-tutorials-78d6c5f29b26)

- Here’s a few:
	- `{% empty %}`, for use in `for` loops when the array is empty
	- `{% lorem \[count\] [method] [random] %}` for automatically filling with Lorem Ipsum text.
	- `{% verbatim %} … {% endverbatim %}`, stop the rendering engine from trying to parse it and replace stuff.
	- [https://hipsum.co/](https://hipsum.co/)

**Bob #5:** **[Beautiful code snippets with Carbon](https://carbon.now.sh)**

- Beautiful images, great for teaching Python / programming.
- Used by a lot of developer, [nice example I spotted today](https://twitter.com/somacdivad/status/1186455654480957440).
- Supports typing and drag and drop, just generated [this link](https://carbon.now.sh/?bg=rgba(171%252C%2520184%252C%2520195%252C%25201)&t=seti&wt=none&l=auto&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%2525&si=false&es=2x&wm=false&code=import%252520pytest%25250A%25250Afrom%252520scores%252520import%252520Player%25252C%252520calculate_score%25252C%252520get_winner%25250A%25250A%25250A%252540pytest.mark.parametrize(%252522arg%25252C%252520expected%252522%25252C%252520%25255B%25250A%252520%252520%252520%252520(%25255B1%25252C%2525203%25252C%2525202%25252C%2525205%25255D%25252C%2525205)%25252C%25250A%252520%252520%252520%252520(%25255B1%25252C%2525204%25252C%2525202%25252C%2525205%25255D%25252C%2525209)%25252C%25250A%252520%252520%252520%252520(%25255B1%25252C%2525201%25252C%2525201%25252C%2525201%25255D%25252C%2525200)%25252C%25250A%252520%252520%252520%252520(%25255B4%25252C%2525205%25252C%2525201%25252C%2525202%25255D%25252C%2525209)%25252C%25250A%252520%252520%252520%252520(%25255B6%25252C%2525206%25252C%2525205%25252C%2525205%25255D%25252C%25252022)%25252C%25250A%25255D)%25250Adef%252520test_calculate_score(arg%25252C%252520expected)%25253A%25250A%252520%252520%252520%252520assert%252520calculate_score(arg)%252520%25253D%25253D%252520expected%25250A%25250A%25250A%252540pytest.mark.parametrize(%252522arg%252522%25252C%252520%25255B%25250A%252520%252520%252520%252520%25255B4%25252C%2525205%25252C%2525206%25252C%252520%2527a%2527%25255D%25252C%25250A%252520%252520%252520%252520%25255B4%25252C%252520-5%25252C%252520-1%25252C%2525202%25255D%25252C%25250A%252520%252520%252520%252520%25255B4%25252C%2525207%25252C%2525206%25252C%2525202%25255D%25252C%25250A%25255D)%25250Adef%252520test_wrong_inputs(arg)%25253A%25250A%252520%252520%252520%252520with%252520pytest.raises(ValueError)%25253A%25250A%252520%252520%252520%252520%252520%252520%252520%252520calculate_score(arg)%25250A%25250A%25250Adef%252520test_winner_3_players()%25253A%25250A%252520%252520%252520%252520players%252520%25253D%252520%25255B%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525201%2527%25252C%252520scores%25253D%25255B1%25252C%2525203%25252C%2525202%25252C%2525205%25255D)%25252C%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525202%2527%25252C%252520scores%25253D%25255B1%25252C%2525201%25252C%2525201%25252C%2525201%25255D)%25252C%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525203%2527%25252C%252520scores%25253D%25255B4%25252C%2525205%25252C%2525201%25252C%2525202%25255D)%25252C%252520%252520%252523%252520max%2525209%25250A%252520%252520%252520%252520%25255D%25250A%252520%252520%252520%252520assert%252520get_winner(players)%252520%25253D%25253D%252520players%25255B-1%25255D%25250A%25250A%25250Adef%252520test_winner_shorter_score_len_raises_exception()%25253A%25250A%252520%252520%252520%252520players%252520%25253D%252520%25255B%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525201%2527%25252C%252520scores%25253D%25255B4%25252C%2525203%25252C%2525205%25252C%2525205%25255D)%25252C%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525202%2527%25252C%252520scores%25253D%25255B4%25252C%2525204%25252C%2525206%25255D)%25252C%252520%252520%252523%252520lacks%252520one%252520score%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525203%2527%25252C%252520scores%25253D%25255B4%25252C%2525205%25252C%2525206%25252C%2525206%25255D)%25252C%25250A%252520%252520%252520%252520%25255D%25250A%252520%252520%252520%252520with%252520pytest.raises(ValueError)%25253A%25250A%252520%252520%252520%252520%252520%252520%252520%252520get_winner(players)%25250A%25250A%25250Adef%252520test_winner_longer_score_len_raises_exception()%25253A%25250A%252520%252520%252520%252520players%252520%25253D%252520%25255B%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525201%2527%25252C%252520scores%25253D%25255B4%25252C%2525203%25252C%2525205%25252C%2525205%25252C%2525204%25255D)%25252C%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525202%2527%25252C%252520scores%25253D%25255B4%25252C%2525204%25252C%2525206%25252C%2525206%25252C%2525203%25252C%2525202%25255D)%25252C%252520%252520%252523%2525201%252520more%25250A%252520%252520%252520%252520%252520%252520Player(name%25253D%2527player%2525203%2527%25252C%252520scores%25253D%25255B4%25252C%2525205%25252C%2525206%25252C%2525206%25252C%2525205%25255D)%25252C%25250A%252520%252520%252520%252520%25255D%25250A%252520%252520%252520%252520with%252520pytest.raises(ValueError)%25253A%25250A%252520%252520%252520%252520%252520%252520%252520%252520get_winner(players)%25250A) by dropping a test module onto the canvas!
- Great to expand Twitter char limit (we use it to [generate Python Tip images](https://pybit.es/python-tips-carbon-selenium.html)).
- Follow the project [here](https://twitter.com/carbon_app), seems they now integrate with Github.

**Michael #6:** [**Researchers find bug in Python script may have affected hundreds of studies**](http://Researchers find bug in Python script may have affected hundreds of studies)

- More info via Mike Driscoll at [**Thousands of Scientific Papers May be Invalid Due to Misunderstanding Python**](http://www.blog.pythonlibrary.org/2019/10/13/thousands-of-scientific-papers-may-be-invalid-due-to-misunderstanding-python/)
- In a paper published October 8, researchers at the University of Hawaii found that a programming error in a set of Python scripts commonly used for computational analysis of chemistry data returned varying results based on which operating system they were run on.
- Scientists did not understand that Python’s glob.glob() does not return sorted results
- Throwing doubt on the results of more than 150 published chemistry studies.
- the researcher were trying to analyze results from an experiment involving cyanobacteria discovered significant variations in results run against the same nuclear magnetic resonance spectroscopy (NMR) data.
- The scripts, called the "Willoughby-Hoye" scripts after their creators, were found to return correct results on macOS Mavericks and Windows 10. But on macOS Mojave and Ubuntu, the results were off by nearly a full percent.
- The module depends on the operating system for the order in which the files are returned. And the results of the scripts' calculations are affected by the order in which the files are processed.
- The fix: A simple `list.sort()`!
- Williams said he hopes the paper will get scientists to pay more attention to the computational side of experiments in the future.

Extras:

- Nov 5 is the next [Python PDX West](https://www.meetup.com/Python-PDX-West/)
- [Using Big Tech Tools](https://vicki.substack.com/p/open-thread-using-big-tech-tools/comments)

Working on: [PyBites platform](https://codechalleng.es): added flake8/ black code formatting,  UI enhancements. 


Michael:

- [Bezos DDoS'd: Amazon Web Services' DNS systems knackered by hours-long cyber-attack](https://www.theregister.co.uk/2019/10/22/aws_dns_ddos/)
- PyPI Just Crossed the 200,000 Packages Threshold! (via RP)
- XKCD Date — via André Jaenisch, Enter [https://explainxkcd.com/wiki/index.php/1425:_Tasks](https://explainxkcd.com/wiki/index.php/1425:_Tasks) and learn, that it was published on 24th Sep 2014.

Joke:

- **Q:** What did the Network Administrator say when they caught a nasty virus?
- **A:** It hurts when IP

