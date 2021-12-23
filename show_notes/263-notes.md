# Python Bytes 263

Sponsored by **us:**

- Check out the **courses over at Talk Python**
- And **Brian’s book too**!

Special guest: [**Laís Carvalho**](https://twitter.com/lais_bsc)

**Michael #1:** [**Django 4.0 released**](https://www.djangoproject.com/weblog/2021/dec/07/django-40-released/)

- Django is picking up speed:
- 4.0 Dec 2021 (+1)
- 3.0 Dec 2020 (+3)
- 2.0 Dec 2017 (+7)
- 1.0.1 May 2010
- Feature highlights:
    - The new [RedisCache backend](https://docs.djangoproject.com/en/4.0/releases/4.0/#redis-cache-backend) provides built-in support for caching with Redis.
    - To ease customization of Forms, Formsets, and ErrorList they are now [rendered using the template engine](https://docs.djangoproject.com/en/4.0/releases/4.0/#template-based-form-rendering).
    - The Python standard library’s zoneinfo is now the [default timezone implementation in Django](https://docs.djangoproject.com/en/4.0/releases/4.0/#zoneinfo-default-timezone-implementation).
    - **scrypt password hasher**: The new scrypt password hasher is more secure and recommended over PBKDF2. However, it’s not the default as it requires OpenSSL 1.1+ and more memory.
- Django 3.2 has reached the end of mainstream support. The final minor bug fix release, [3.2.10](https://docs.djangoproject.com/en/stable/releases/3.2.10/), was issued today. Django 3.2 is an LTS release and will receive security and data loss fixes until April 2024.
- Some [backwards incompatible changes](https://docs.djangoproject.com/en/4.0/releases/4.0/#backwards-incompatible-4-0) you’ll want to be aware of when upgrading from Django 3.2 or earlier. 
- They’ve [begun the deprecation process for some features](https://docs.djangoproject.com/en/4.0/releases/4.0/#deprecated-features-4-0).
- Django 4.0 supports Python 3.8, 3.9, and 3.10.

**Brian #2:** [**python-minifier**](https://github.com/dflook/python-minifier)

- Suggested by Lance Reinsmith
- My first thought was “we don’t need a minifier for Python”
- The docs give one reason:
    - “AWS Cloudformation templates may have AWS lambda function source code embedded in them, but only if the function is less than 4KiB. I wrote this package so I could write python normally and still embed the module in a template.”
- Lance has another reason:
    - “I needed it because the RAM on Adafruit boards using the common M0 chip is around 192KB to 256KB total--not all of which is available to your program.  To get around this, you can either 1) compile your code to an .mpy file or 2) minify it.  The second worked for me and allowed me to alter it without constantly re-compiling.”
- Fair enough, what does it do?
- All of these features are options you can turn off, and are documented well:
    -  Combine Import statements
    -  Remove Pass statements
    -  Remove literal statements (docstrings)
    -  Remove Annotations
    -  Hoist Literals
    -  Rename Locals, with preserved Locals list 
    -  Rename Globals, with preserved Globals list
    -  Convert Positional-Only Arguments to Normal Arguments
- Also looks like it replaces spaces with tabs
    - Begrudgingly, that makes sense in this context.
- You can try it at [python-minifier.com](https://python-minifier.com/)

 **Laís #3:** [**It’s time to stop using Python 3.6**](https://pythonspeed.com/articles/stop-using-python-3.6/)

- Python 3.6 is reaching the [end of it’s life](https://pythonspeed.com/articles/stop-using-python-3.6/https://endoflife.date/python) in 1 week and 1 day (Dec 23rd), i.e. no more releases after it.
- You should care because the Python dev team will no longer release security updates for 3.6 ⚠️
- if you use Linux, you have a bit more time BUT security updates will be released and bug fixes will not.
- also, Python 3rd party libraries and frameworks will drop support for 3.6 soon enough. *See the* [*log4j issue and Java*](https://twitter.com/WeldPond/status/1469313738029289476?ref_src=twsrc%5Etfw)*.*
- [Brian might like this one] [**Grype: a vulnerability scanner for container images and filesystems**](https://twitter.com/anthonypjshaw/status/1469952485687107584)

**Michael #4:** [**How to Visualize the Formula 1 Championship in Python**](https://medium.com/towards-formula-1-analysis/how-to-visualize-the-formula-1-championship-in-python-using-the-ergast-api-and-seaborn-ac2f88ae7248)

- [**Race Highlights | 2021 Abu Dhabi Grand Prix**](https://www.youtube.com/watch?v=7QJ-N-AQJYc)
- [**Formula 1: Drive to Survive (Season 3) | Official Trailer**](https://www.youtube.com/watch?v=aViLtXEtgqs)
- Wanting to get into Formula 1 data analysis, the [**Ergast API**](https://ergast.com/mrd/) is a very good starting point.
- This tutorial will show you how to use data from the Ergast API to visualize the changes in the 2021 championship standings over the rounds.
- Introduces [**fastf1**](https://pypi.org/project/fastf1/): Wrapper library for F1 data and telemetry API with additional data processing capabilities.

**Brian #5:**  [**nbdime**](https://github.com/jupyter/nbdime)[**:**](https://github.com/jupyter/nbdime) [**Jupyter Notebook Diff and Merge tools**](https://github.com/jupyter/nbdime)

- Suggestion from Henrik Finsberg
- “you recently covered ‘jut’ for viewing Jupyter notebooks from the terminal. Check out ‘mbdime’.” (that was [episode 258](https://pythonbytes.fm/episodes/show/258/python-built-us-an-anime-dog))
- So I did. And it looks cool.
- `nbdime` provides tools for diffing and merging of Jupyter Notebooks.
    - `nbdiff` compare notebooks in a terminal-friendly way
    - `nbmerge` three-way merge of notebooks with automatic conflict resolution
    - `nbdiff-web` shows you a rich rendered diff of notebooks
    - `nbmerge-web` gives you a web-based three-way merge tool for notebooks
    - `nbshow` present a single notebook in a terminal-friendly way

**Laís #6:** [**Using AI to analyse and recommend software stacks for Python apps**](https://developers.redhat.com/articles/2021/11/17/customize-python-dependency-resolution-machine-learning#python_interface_and_prescriptionshttps://developers.redhat.com/articles/2021/11/17/customize-python-dependency-resolution-machine-learning#python_interface_and_prescriptions)

- thanks Fridolin!
- Project Thoth: an open source cloud-based Python dependency resolver
    - ML (reinforcement learning) that solves dependency issues taking into consideration runtime envs, hardware and other inputs. Using Markov’s decision process.
    - “a smarter pip” that instead of using backtracking, precomputes the dependency information and stores it in a database that can be queried for future resolutions. Using pre-specified criteria by the developer.
- In summary:
    - Thot’s resolver uses automated bots that guarantee dependencies are locked down to specific versions, making builds and deployments reproducible;
    - the aggregated knowledge (reinforcement learning from installed logs) helps the bots to lock the dependencies to the best libraries, instead of the latest.
    - They are in beta phase but welcoming feedback and suggestions from the community.


**Extras** 

Brian:

- [Pragmatic Bookshelf 12 days of Christmas](https://pragprog.com/twelve-days-of-pragprog/)
    - Today, pytest book is part of the deal, nice timing, right?

Michael:

- [**My talk**](https://www.youtube.com/watch?v=kNXVFB5eQfo) at FlaskCon is out
- Firefox [**releases RLBox**](https://hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/)
- We’re all [**getting identity theft monitoring**](https://arstechnica.com/information-technology/2021/12/the-critical-log4shell-zero-day-affects-a-whos-who-of-big-cloud-services/) for 1 year for free :-/

**Laís**: 

- Python Ireland’s [speaker’s coaching session](https://www.meetup.com/pythonireland/events/281468322/) is on Jan 22nd
- [Learning git](https://learngitbranching.js.org/) the visual way - cool for beginners, thorough explanations
- [Good read](https://realpython.com/java-vs-python/) for Java devs who want to start with Python (by Real Python)


**Joke:** 

- [**Janga**](https://twitter.com/GGreg/status/1469442136961695752)
- [**Python (hellish) virtual envs**](https://twitter.com/OfficialLoganK/status/1454130937730535424)

