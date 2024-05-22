# Python Bytes 261

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**Dr. Chelle Gentemann**](https://twitter.com/ChelleGentemann)



**Michael #1:** [**rClone**](https://rclone.org/)

- via Mark Pender
- Not much Python but useful for Python people :)
- Rclone is a command line program to manage files on cloud storage.
- [Over 40 cloud storage products](https://rclone.org/#providers) support rclone including S3 object stores
- Rclone has powerful cloud equivalents to the unix commands rsync, cp, mv, mount, ls, ncdu, tree, rm, and cat.

**Brian #2:**  [**check-wheel-contents**](https://pypi.org/project/check-wheel-contents/)

- Suggested by several listeners, thank you.
- “Getting the right files into your wheel is tricky, and sometimes we mess up and publish a wheel containing __pycache__ directories or tests/”
- usage: `check-wheel-contents [<options>] <wheel or dir>`
- ex:
```
    (venv) $ pwd
    /Users/okken/projects/cards
    (venv) $ check-wheel-contents dist
    dist/cards-1.0.0-py3-none-any.whl: OK
```
- Checks
```
    - W001 - Wheel contains .pyc/.pyo files
    - W002 - Wheel contains duplicate files
    - W003 - Wheel contains non-module at library toplevel
    - W004 - Module is not located at importable path
    - W005 - Wheel contains common toplevel name in library
    - W006 - __init__.py at top level of library
    - W007 - Wheel library is empty
    - W008 - Wheel is empty
    - W009 - Wheel contains multiple toplevel library entries
    - W010 - Toplevel library directory contains no Python modules
    - W101 - Wheel library is missing files in package tree
    - W102 - Wheel library contains files not in package tree
    - W201 - Wheel library is missing specified toplevel entry
    - W202 - Wheel library has undeclared toplevel entry
```

- Readme has good description of each check, including common causes and solutions.


**Chelle #3:** [**xarray**](http://xarray.pydata.org/en/stable/)

- Where can I find climate and weather data?
- Binary to netCDF to Zarr… data is all its gory-ness
- Data formats are critical for data providers but should be invisible to users
- What is Xarray
- An example reading climate data and making some maps

**Michael #4:** [**JetBrains Remote Development**](https://www.jetbrains.com/remote-development/)

- If you can SSH to it, that can be your dev machine
- Keep sensitive code and connections on a dedicated machine
- Reproducible environments for the team
- Spin up per-configured environments (venvs, services, etc)
- Treat your dev machine like a temp git branch checkout for testing PRs, etc
- They did bury the lead [with Fleet in here too](https://www.jetbrains.com/fleet/)

**Brian #5:**  **The XY Problem**

- This topic is important because many of us, including listeners, are 
    - novices in some topics and ask questions, sometimes without giving enough context.
    - experts in some topics and answer questions of others.
- The XY Problem
    - “… You are trying to solve problem *X*, and you think solution *Y* would work, but instead of asking about *X* when you run into trouble, you ask about *Y.”  -* [*From a Stack Exchange Answer*](https://meta.stackexchange.com/a/66378) 
- Example from [xyproblem.info](https://xyproblem.info/)
    <n00b> How can I echo the last three characters in a filename?
    <feline> If they're in a variable: echo ${foo: -3}
    <feline> Why 3 characters? What do you REALLY want?
    <feline> Do you want the extension?
    <n00b> Yes.
    <feline> There's no guarantee that every filename will have a three-letter extension,
    <feline> so blindly grabbing three characters does not solve the problem.
    <feline> echo ${foo##*.}
- Reason why it’s common and almost unavoidable:
    - Almost all design processes for software
        - I can achieve A if I do B and C.
        - I can achieve B if I do D and E.
        - And I can achieve C if I do F and G. 
        - … I can achieve X if I do Y.
- More important questions than “What is the XY Problem?”:
    - Is it possible to avoid? - not really
    - Is it possible to mitigate when asking questions? - yes
    - When answering questions where you expect XY might be an issue, how do you pull out information while providing information and be respectful to the asker? 
- [One great response included](https://meta.stackexchange.com/a/269222)
    - **Asking Questions where you risk falling into XY**
        - State your problem
        - State what you are trying to achieve
        - State how it fits into your wider design
    - **Giving Answers to XY problems**
        1. Answer the question (answer Y)
        2. Discuss the attempted solution (ask questions about context)
            - “Just curious. Are you trying to do (possible X)? If so, Y might not be appropriate because …”
            - “What is the answer to Y going to be used for?”
        3. Solve X
- Also interesting reading
    - [Einstellung effect](https://en.wikipedia.org/wiki/Einstellung_effect) - The Einstellung effect is the negative effect of previous experience when solving new problems.

**Chelle #6:** [**kerchunk**](https://github.com/fsspec/kerchunk) - Making data access fast and invisible

- S3 is pretty slow, especially when you have LOTS of files
- We can speed it up by creating json files that just collect info from files and act as a reference
- Then we can collate the references into MEGAJSON and just access lots of data at once
- Make it easy to get data!


**Extras** 


Michael:

- [**Xojo**](https://twitter.com/_rlivingston/status/1463277526210416644) - like modern VB6?
- [**10 Reasons You'll Love PyCharm Even More in 2021 webcast**](https://www.youtube.com/watch?v=sJriZQsMHrw)
- [**Users revolt as Microsoft bolts a short-term financing app onto Edge**](https://arstechnica.com/information-technology/2021/11/microsoft-plans-to-integrate-a-buy-now-pay-later-app-into-edge/)

**Chelle**: 

- Why we need python & FOSS to solve the climate crisis


**Joke:** [**Spacebar Heating**](https://xkcd.com/1172/)

