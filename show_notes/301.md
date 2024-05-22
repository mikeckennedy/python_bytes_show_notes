# Python Bytes 301


Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).


**Michael #1:** [**PythonAnywhere: Our Commitment to Providing Free Accounts**](https://blog.pythonanywhere.com/206/)

- via Matthew Kramer
- In light of Heroku’s cancelling their free tiers…
- They believe free tiers are important for beginners
- Two part solution:
    - Limit outbound internet access for free accounts
    - “Proof of life” to keep running - 3 months for apps, 1 yr for accounts
- BTW, they were acquired by Anaconda Inc.

**Brian #2:** [**ruff: An extremely fast Python linter, written in Rust.**](https://github.com/charliermarsh/ruff)

- Announcement article: [Python tooling could be much, much faster](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster)
- Charlie Marsh
- Quite the [star history](https://star-history.com/#charliermarsh/ruff&Date), as it’s a new repo as of Aug 30. Now at 1.8k.
- It is extremely fast.
- I installed it and tried it on a small project.
- It ran so fast I thought it didn’t do anything. I went and added some errors to convince myself it was running.
```
$ time flake8 src tests     
    ...
    flake8 src tests  0.29s user 0.02s system 98% cpu 0.311 total
    
    $ time ruff src/ tests/   
    ...  
    ruff src/ tests/  0.01s user 0.01s system 162% cpu 0.011 total
```

**Michael #3:**  [**Meta spins off PyTorch Foundation to make AI framework vendor neutral**](https://arstechnica.com/information-technology/2022/09/meta-spins-off-pytorch-foundation-to-make-ai-framework-vendor-neutral/)

- PyTorch, which powers Tesla Autopilot and 150K other projects, will join the Linux Foundation.
- Its governing board includes representatives from Nvidia, Meta, Google, Microsoft, Amazon, and AMD.
- The PyTorch Foundation will strive to adhere to four principles,
    - Remaining open
    - Maintaining neutral branding
    - Staying fair
    - Forging a strong technical identity
- According to Meta, the transition to the PyTorch Foundation will not affect any existing PyTorch code

**Brian #4:** **Two string resources**

- [Python String Methods to Know](https://www.pythonmorsels.com/string-methods/?utm_source=pocket_mylist)
    - Trey Hunner
- [F-Strings Number Formatting Cheat Sheet](https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/?utm_source=pocket_mylist)
    - Brian Allan

**Extras** 

Brian:

- In Feb, on [episode 271, we talked about Seaborn’s new object interface](https://pythonbytes.fm/episodes/show/271/cpython-async-task-groups-in-python-3.11)
    - Well, it’s [out now in seaborn 0.12](https://michaelwaskom.medium.com/announcing-the-release-of-seaborn-0-12-f26266ddbd8f)
- Interesting discussion about [lazy imports](https://lwn.net/SubscriberLink/907226/d9bd243556d15d8b/).
- Other than that, I’m good with your extra. 🙂 

Michael:

- [**pytest course is out**](https://training.talkpython.fm/courses/getting-started-with-testing-in-python-using-pytest)!

**Joke:** [**If a developer had to build a horse**](https://twitter.com/pr0grammerhum0r/status/1544093723541348353?s=12&t=9gGvVIDpqOfv22I40TQUzw)…
