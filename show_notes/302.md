# Python Bytes 302


Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Brian #1:** [**Can Amazon’s CodeWhisperer write better Python than you?**](https://blog.symops.com/2022/08/31/amazon-codewhisperer/)

- Brian Tarbox
- “Despite the clickbait-y title, whether CW’s code is better or worse than mine is at the margins and not really important. What is significant is that it has the potential to save me a ton of time and mental space to focus on improving, refactoring and testing. It’s making me a better programmer by taking on some of the undifferentiated heavy lifting.”
- Some decent code generation, starting with Amazon API examples.
- The generated dataclass method was neat, but really, the comment “prompt” probably took as much time to write as the code would have.
- The generated test case is workable, but I would not consider that a good test. 
    - Perhaps don’t lump together construction, attribute access, and tests for all methods in one test function.
    - That said, I’ve seen way worse test methods in my career. So, decent starting point.
- Related and worth listening to: [**Changelog #506: Stable Diffusion breaks the internet w/ Simon Willison**](https://changelog.com/podcast/506)
    - Mostly an episode about AI generated art.
    - There is a bit of a tie in to AI code generation, the ethics around it, and making sure you walk up the value chain.
- I’m planning on playing with GitHub CoPilot. 
    - I’ve been reluctant in the past, but Simon’s interview is compelling to combine experienced engineering skill with AI code generation to possibly improve productivity. Simon does warn against possible abuse by Junior devs and the  “just believe the code” problem that we also see with “copy from StackOverflow” situations.
    

**Michael #2:** [Apache Superset](https://superset.apache.org)

- Apache Superset is a modern data exploration and visualization platform
- An intuitive interface for visualizing datasets and crafting interactive dashboards
- A wide array of beautiful visualizations to showcase your data
- Code-free visualization builder to extract and present datasets
- A world-class SQL IDE for preparing data for visualization, including a rich metadata browser
- A lightweight semantic layer which empowers data analysts to quickly define custom dimensions and metrics
- Out-of-the-box support for most SQL-speaking databases
- Seamless, in-memory asynchronous caching and queries
- An extensible security model that allows configuration of very intricate rules on who can access which product features and datasets.
- Integration with major authentication backends (database, OpenID, LDAP, OAuth, REMOTE_USER, etc)
- The ability to add custom visualization plugins
- An API for programmatic customization

**Brian #3:** [**Recipes from Python SQLite docs**](https://rednafi.github.io/reflections/recipes-from-python-sqlite-docs.html)

- Redowan Delowar
- Expanding on [**sqlite3 Python docs**](https://docs.python.org/3/library/sqlite3.html) with more examples, including
    - Executing individual and batch statements
    - Applying user-defined callbacks: scalar and aggregate
        - scalar example shows using a  sha256 function to hash passwords as their inserted into the database
    - Enabling tracebacks when callbacks raise an error
    - Transforming types between SQLite and Python
    - Implementing authorization control
    - … much more …
- This is great for not only learning SQLite, but also, since these kinds of topics exist in other databases, learning about databases.
- AND a great example of learning a subsystem by creating little code snippets to check your understanding of something.
    - One mod I would do in practice is to write these examples as pytest functions, because I can then run them individually while keeping a bunch in the same file. 🙂 

**Michael #4:**  [**-ffast-math and indirect changes**](https://twitter.com/moyix/status/1567167774039973888)

- Brendan Dolan-Gavitt downloaded 4 TB of Python packages containing native x86-64 libraries and see how many of them use -ffast-math, potentially altering floating point behavior in any program unlucky enough to load them! 
- Python packages built with an appealing-sounding but dangerous compiler option, -ffast-math, could end up causing any program that uses them to compute incorrect numerical results.
- When -ffast-math is enabled, the compiler will link in a constructor that sets the FTZ/DAZ flags whenever the library is loaded — even on shared libraries, which means that any application that loads that library will have its floating point behavior changed *for the whole process*.
- A total of **2,514** packages eventually depend on a package that uses -ffast-math.
- Because of [**highly connected nature of the modern software supply chain**](https://en.wikipedia.org/wiki/Software_supply_chain), even though a mere 49 packages were actually built with -ffast-math, thousands of other packages, with a total of at least **9.7** ***million*** downloads over the past 30 days, are affected.

**Extras** 

Brian:

- Thinking about changelogs
- [**Focusing on helping teams with specific goals**](https://pythontest.com/training/)
    - Working on an experiment in consulting with some lead engineers before the training to altering the content of a pytest course so the examples better match what the team will need.
        - Sharing packages through internal system, as that’s usually different than the PyPI process.
        - Altering the database and API example of the TalkPython pytest course content to match a teams external resources and responsibility scope.
    - It takes extra time and thought, but in the end might increase engagement and excitement about testing and keeping up on Python’s evolving common practices.

Michael:

- New course: [**Python Data Visualization**](https://training.talkpython.fm/courses/python-data-visualization)
- [**pytest course**](https://training.talkpython.fm/courses/getting-started-with-testing-in-python-using-pytest) going strong

**Joke:** 

- [**They all use it**](https://twitter.com/PR0GRAMMERHUM0R/status/1571333223443038209)
- [**State of emergency**](https://twitter.com/kyleecodes/status/1568351571427082246)

