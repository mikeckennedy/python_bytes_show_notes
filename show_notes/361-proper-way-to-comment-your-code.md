# Python Bytes 361
Sponsored by [**Scout APM**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [The many shapes and sizes of keyboards](https://snarky.ca/the-many-shapes-and-sizes-of-keyboards/)

- Many keyboards discussed 
- Focus on health and safety (as it should!)
- I swear by [Microsoft Sculpt Ergonomic](https://www.microsoft.com/en/accessories/products/keyboards/sculpt-ergonomic-desktop?activetab=pivot:overviewtab) (which wasn’t mentioned)
- More options still [over at Wire Cutter](https://www.nytimes.com/wirecutter/reviews/comfortable-ergo-keyboard/)

**Brian #2:** [**appeal - a CLI framework from Larry Hastings**](https://github.com/larryhastings/appeal)

- “Give your program APPEAL!”
- Appeal is a command-line argument processing library for Python, like `argparse`, `optparse`, `getopt`, `docopt`, `Typer`, and `click`. But Appeal takes a refreshing new approach.
- Hello World example:
```
import appeal
    
    app = appeal.Appeal()
    
    @app.command()
    def hello(name):
        print(f"Hello, {name}!")
    
    app.main()
```

- looks fun, no idea how to test with it “yet”. 
    - But I plan on looking into that.

**Michael #3:** [Graphinate: Data to Graphs](https://erivlis.github.io/graphinate/)

- via Eran Rivlis
- Graphinate is a python library that aims to simplify the generation of Graph Data Structures from Data Sources.
- Write a function to definite the edges as a generator, call materialize
- Based on [NetworkX](https://networkx.org)
- See the github page for visual examples

**Brian #4:** [**A Disorganized List of Maintainer Tasks**](https://davidism.com/maintainer-notes/)

- David Lord
    - Plus, David Lord, lead maintainer of Flask, Jinja, Click, … on Pallets, also PSF Fellow, has a blog. Neat.
- TLDR; Next time you want to ask "When's the next release?", instead look at the project and see where you can start getting involved. The more help maintainers have, the more they can get done.
- Long list of stuff David thinks about when maintaining a project.
    - My list is shorter, but it’s still long, and my projects are tiny in comparison to his
    

**Extras** 

Brian:

- [Do you do enough testing? pytest to the Rescue!](https://www.youtube.com/watch?v=i-7EMhvxYKs) webinar from this morning
- [The Complete pytest Course](https://courses.pythontest.com/p/the-complete-pytest-course) will be 16 chapters, 11 are released, the 12th is recorded and almost released, and the 13th should be next week, … I should be done with all 16 by the end of the year. 
- Testing argparse Applications
    - [Python Test Podcast episode 109: Testing argparse Applications](https://testandcode.com/episodes/209-testing-argparse-applications)
    - [Blog post on pythontest.com: Testing argparse Applications](https://pythontest.com/testing-argparse-apps/)
- Black Friday sale on [The Complete pytest Course](https://courses.pythontest.com/p/the-complete-pytest-course)
    - Use code BLACKFRIDAY for 50% off of
    - [The Complete pytest Course, Full Course + Full Access](https://courses.pythontest.com/p/the-complete-pytest-course)

Michael:

- It’s [Black Friday at Talk Python](https://talkpython.fm/black-friday)
- [Python 3.13.0 alpha 1](https://pythoninsider.blogspot.com/2023/10/python-3130-alpha-1-is-now-available.html) is now available
- [Python Developers Survey 2023](https://survey.alchemer.com/s3/7554174/python-developers-survey-2023)

**Joke:** [The proper way to comment your code!](https://www.reddit.com/r/programminghumor/comments/1798vi7/the_proper_way_to_comment_your_code/)

