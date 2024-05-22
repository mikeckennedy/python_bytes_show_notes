# Python Bytes 90
Sponsored by Digital Ocean: [pythonbytes.fm/digitalocean](https://pythonbytes.fm/digitalocean)

Brian #1: [Reproducible Data Analysis in Jupyter](https://www.youtube.com/playlist?list=PLYCpMb24GpOC704uO9svUrihl-HY1tTJJ)

- Amazing series of videos by Jake Vanderplas
- Exploring a data set through visualization in a Jupyter notebook
- There’s a lot of dense material there, from saving datasets to files, plotting in the notebook as opposed to outside in a separate window, using resampling, … 

Michael #2: [PySimpleGUI - For simple Python GUIs](https://github.com/MikeTheWatchGuy/PySimpleGUI)

- Via Mike Barnett
- Looking to take your Python code from the world of command lines and into the convenience of a GUI? 
- Have a Raspberry Pi with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK? 
- Look no further, you've found your GUI package.
- Based on tkinter
-  No dependencies (outside of Python itself): `pip install PySimpleGUI`
- Python3 is required to run PySimpleGUI. It takes advantage of some Python3 features that do not translate well into Python2.
- Looking to help? → Port to other graphic engines. Hook up the front-end interface to a backend other than tkinter. Qt, WxPython, etc.

Brian #3: [**Useful tricks you might not know about Git stash**](https://dev.to/srebalaji/useful-tricks-you-might-not-know-about-git-stash-117e)

- `git stash save`  - Stash the changes in a dirty working directory away
- `git stash apply` - re-applies your changes after you do whatever you need to to your directory, like perhaps pull.
- Lots of neat things to do with stash
	- you can add a message so the stashed content has a nice label
	- `-u` will include untracked files when saving.
	- `git stash branch <name> stash@{1}` will create a new branch with the latest stash, and then deletes the latest stash
	- Lots of other nice tricks in the article
- See also: [git-stash in git-scm book](https://git-scm.com/docs/git-stash)

Michael #4: [A Django Async Roadmap](https://www.aeracode.org/2018/06/04/django-async-roadmap/)

- via Andrew Godwin, from Django Channels
- Thinks that the time has come to start talking seriously about bringing async functionality into Django itself
- Open for public feedback
- The goal is to make Django a world-class example of what async can enable for HTTP requests, such as:
	- Doing ORM queries in parallel
	- Allowing views to query external APIs without blocking threads
	- Running slow-response/long-poll endpoints alongside each other efficiently
	- Bringing easy performance improvements to any project that spends a majority of time blocking on databases or sockets (which is most projects!)
- Imperative that we keep Django backwards-compatible with existing code
- Why now?  Django 2.1 will be the first release that only supports Python 3.5 and up, and so this provides us the perfect place to start working on async-native code

Brian #5: [**pydub**](https://github.com/jiaaro/pydub)

- “Manipulate audio with a simple and easy high level interface”
- Really clean use of operators.

```
    from pydub import AudioSegment 
     
    # also handles lots of other formats 
    song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3") 
     
    # pydub does things in milliseconds 
    ten_seconds = 10 * 1000 
    first_10_seconds = song[:ten_seconds] 
    last_5_seconds = song[-5000:] 
     
    # boost volume by 6dB 
    beginning = first_10_seconds + 6 
     
    # reduce volume by 3dB 
    end = last_5_seconds - 3 
     
    # Concatenate audio (add one file to the end of another) 
    without_the_middle = beginning + end
```

- also:
	- crossfade
	- repeat
	- fade
	- switch formats
	- add metadata tags
	- save with a specific bitrate

Michael #6: [Molten: Modern API framework](https://moltenframework.com/v0.4.1/index.html)

- molten is a minimal, extensible, fast and productive framework for building HTTP APIs with Python.
- Heavy use of type annotations
- Officially supports Python 3.6 and later
- Request Validation: molten can automatically validate requests according to predefined schemas, ensuring that your handlers only ever run if given valid input
- Dependency Injection: Write clean, decoupled code by leveraging DI.
- Still experimental at this stage.

