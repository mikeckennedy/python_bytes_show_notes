# Python Bytes 231


**Watch the live stream:**

YOUTUBE: id=rDYKZG6Fn8o

**About the show**

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guests: 

- [**Cecil Phillip**](https://twitter.com/cecilphillip)

**Brian #1:** [**For-Else: A Weird but Useful Feature in Python**](https://medium.com/techtofreedom/for-else-a-weird-but-useful-feature-in-python-2076d8dafad1)

- Yang Zhou
- After a `for` loop, you can put an `else` block.
- The `else` block only executes when there is no `break` in the loop. If the loop got all the way to the end, and off the end, the `else`  block will run.
- First, I’m not used to putting `break` or `else` anywhere in my Python code, so I’m also curious why you’d want to do this.
- Yang explains the feature, then talks about 3 scenarios for use:
	- Iterate and find items without needing a flag variable. 
    - `break` when you find what you are looking for, and the `else` only runs if you didn’t find it.
	- Help to break out of nested loops
		- I’m still confused by this one
	- Help to handle exceptions
		- Kind of a cool use. try/except in a `for` loop. Have a `break` in the `except` block. Then the `else` block will be fore code where you know no exceptions were caught.
- Take away: The first reason wins it for me. I hate it when I feel I need to add a “found” flag to some code. `else` seems cleaner.
- Also: Please add comments to `else` blocks. Many people won’t know how they work, so a short explanation can help tons.

**Michael #2:** [**Tortoise ORM**](https://github.com/tortoise/tortoise-orm)

- Familiar asyncio ORM for python, built with relations in mind
- I’ve seen this ORM popping up around the async web stories a lot these days
- Similar to Django’s ORM
- Tortoise ORM is supported on CPython >= 3.7 for SQLite, MySQL and PostgreSQL.
- They offer a nice, broad perf comparison on their github page
- Really nice and clean API for ORM things, again on the github page
- Tortoise ORM uses [Aerich](https://github.com/tortoise/aerich) as database migrations tool

**Cecil #3:** [**Faster Python with Go Shared objects**](https://blog.kchung.co/faster-python-with-go-shared-objects/)

- Leverage Go's standard library and ecosystem in Python
- Language interop is a good for productivity
- Passing data is limited to primitive types

**Brian #4:** [**Learn by reading code: Python standard library design decisions explained (for advanced beginners)**](https://death.andgravity.com/stdlib)

- Reading code is a great way to improve your own coding.
- What code should you read?
	- If it’s great code, you could improve.
	- If it’s scary code, it might not be so good, and might teach you bad practices
- Python stdlib is there and has some interesting features:
	- all of the code is available
	- PEPs are available so you can read the discussions that went into it while you are reading the code, or before
    - This is huge. Most code you’ll find, even within companies, doesn’t have “why we did this” explanations.
- However…
	- it is not uniform
	- different authors
	- some is old, and pythonic was different 10-20 years ago
	- lots of code around to preserve backwards compatibility
- So here’s some recommendations:
	- statistics : code is simple, well documented, PEP has design decisions and comparisons
	- pathlib: good object-oriented example, good comparative study, as you can also read os.path
	- dataclasses: extremely well documented, good example of dataclasses
	- graphlib: does one thing, an implementation of a topological sort algorithm. no PEP, but an issue with a discussion thread that discusses the API decisions

Related: https://devops.com/learning-curve-computer-programming-languages/

![](https://paper-attachments.dropbox.com/s_F9A2A0911FFE1F78C1A86C3DF0B67FFAAD84704801453ECE7274E60D39131BB8_1619632331818_image.png)


**Michael #5:** [**Gradio: Create UIs for prototyping your machine learning model in 3 minutes**](https://www.gradio.app/)

- via David Smit
- Quickly create customizable UI components around your models.
- Gradio makes it easy for you to "play around" with your model in your browser
- Drag-and-drop in your own images, pasting your own text, recording your own voice, etc. and seeing what the model outputs.
- Gradio is useful for:
- Creating demos of your machine learning code for clients / collaborators / users
- Getting feedback on model performance from users
- Debugging your model interactively during development
- Interfaces can be easily shared publicly by setting `share=True` in the `launch()` method.

**Cecil #6:** [Use basketball stats to optimize game play with Visual Studio Code](https://docs.microsoft.com/en-us/learn/paths/optimize-basketball-games-with-machine-learning/)

- Free MS Learn learning path
- Inspired by Space Jam: A New Legacy
- Use tools like Python, Pandas, and Visual Studio Code 
- [Space Jam: A New Legacy coding workshops](https://www.microsoft.com/whatsinstore/2020/12/14/space-jam-a-new-legacy-coding-workshops-let-kids-team-up-with-lebron-bugs-bunny)

**Extras**

**Michael**

- [**People are liking**](https://twitter.com/TalkPython/status/1384943094899122177) the zero analytics / perfect privacy score


**Joke:** [**They said containers would fix it**](https://devhumor.com/media/linux-containers-and-kubernetes-for-beginners)

![](https://trello-attachments.s3.amazonaws.com/60817ae1a522117c64d17c10/700x979/2fe03ead925aaab83ee0a49fe43d1cfd/kubernetes_begginers.jpg)
