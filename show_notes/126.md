# Python Bytes 126
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest: **[Cecil Philip](https://twitter.com/cecilphillip/)**

**Brian #1:**  [**Python Used to Take Photo of Black Hole**](http://www.blog.pythonlibrary.org/2019/04/11/python-used-to-take-photo-of-black-hole/)

- Lots of people talking about this. The link I’m including is a quick write up by Mike Driscoll.
-  From now on these conversations can happen:
	- “So, what can you do with Python?”
	- “Well, it was used to help produce the worlds first image of a black hole. Your particular problem probably isn’t as complicated as that, so Python should work fine.”
- Projects listed in the paper: “[First M87 Event Horizon Telescope Results. III. Data Processing and Calibration](https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57/meta)”:
	- [Numpy](http://www.numpy.org/) (van der Walt et al. 2011)
	- [Scipy](https://www.scipy.org/) (Jones et al. 2001)
	- [Pandas](https://pandas.pydata.org/) (McKinney 2010)
	- [Jupyter](https://jupyter.org/) (Kluyver et al. 2016)
	- [Matplotlib](https://matplotlib.org/) (Hunter 2007).
	- [Astropy](http://www.astropy.org/) (The Astropy Collaboration et al. 2013, 2018)

**Cecil #2:** [**Wasmer - Python Library for executing WebAssembly binaries**](https://github.com/wasmerio/python-ext-wasm)

- [WebAssembly](https://webassembly.org) (Wasm) enables high level languages to target a portable format that runs in the web
- Tons of languages compile down to Wasm but Wasmer enables the consumption of Wasm in python
- This enables an interesting use case for using Wasm as a way to leverage code between languages

**Michael #3:** [**Cooked Input**](https://cooked-input.readthedocs.io/en/latest/quick_start.html)

- cooked_input is a Python package for getting, cleaning, converting, and validating command line input.
- Name comes from `input` / `raw_input` (unvalidated) and cooked input (validated)
- Beginner’s can use the provided convenience classes to get simple inputs from the user.
- More complicated command line application (CLI) input can take advantage of `cooked_input`’s ability to create commands, menus and data tables.
- All sorts of cool validates and cleaners
- Examples

```
    cap_cleaner = ci.CapitalizationCleaner(style=ci.ALL_WORDS_CAP_STYLE)
    ci.get_string(prompt="What is your name?", cleaners=[cap_cleaner])
```

```
    >>>  ci.get_int(prompt="How old are you?", minimum=1)
    
    How old are you?: abc
    "abc" cannot be converted to an integer number
    How old are you?: 0
    "0" too low (min_val=1)
    How old are you?: 67
    67
```

**Brian #4:** [**JetBrains and PyCharm officially collaborating with Anaconda**](https://blog.jetbrains.com/pycharm/2019/04/collaboration-with-anaconda-inc/)

- PyCharm 2019.1.1 has some improvements for using Conda environments.
	- Fixed various bugs related to creating Conda envs and installing packages into them.
- Special distribution of PyCharm: [PyCharm for Anaconda](https://www.jetbrains.com/pycharm/promo/anaconda/) with enhanced Anaconda support.
- I’m using PyCharm Pro with vim emulation this week to edit a notebook based presentation. I might run them in Jupyter, or just run it in PyCharm, but editing with all my normal keyboard shortcuts is awesome.

**Cecil #5:** [Building a Serverless IoT Solution with Python Azure Functions and SignalR](https://dev.to/azure/building-a-serverless-iot-solution-with-python-azure-functions-and-signalr-4ljp)

- Interesting blog post on using serverless, IoT, real-time messaging to create a live dashboard
- Shows how to create a serverless function in Python to process IoT data
- There’s tons of DIY applications for using this technique at home 
- The Dashboard is a static website using D3 for charting.

**Michael #6:** [**multiprocessing.shared_memory — Provides shared memory for direct access across processes**](https://docs.python.org/3.8/library/multiprocessing.shared_memory.html)

- New in Python 3.8
- This module provides a class, `[SharedMemory](https://docs.python.org/3.8/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory)`, for the allocation and management of shared memory to be accessed by one or more processes on a multicore or symmetric multiprocessor (SMP) machine.
- The `ShareableList` looks nice to use.

**Extras**

Brian:

- Getting ready for PyCon with STICKERS. Yeah, baby. Come see us at PyCon. I’ll also be bringing some copies of [Python Testing with pytest](https://amzn.to/2IqvjCG), if anyone doesn’t already have a copy.
- Lots of interviews going on for [Test & Code](https://testandcode.com), and some will happen at PyCon.

Cecil:  

- [Attendee Detector Workshop](https://github.com/jimbobbennett/AttendeeDetectorWorkshop) 
- [Talk Python training app on Android](https://play.google.com/store/apps/details?id=fm.talkpython.training.player)

Michael:

- Course player app update: iOS app may be ready, but not published.
- Guido van Rossum [**interviewed on MIT’s AI podcast**](https://lexfridman.com/guido-van-rossum/) via Tony Cappellini 
- [**Visual Studio IntelliCode for VS & VS Code**](https://marketplace.visualstudio.com/itemdetails?itemName=VisualStudioExptTeam.vscodeintellicode)
- [**Showing a Craigslist scammer who's boss using Python**](https://www.youtube.com/watch?v=GVQoAlQrnSg) via Dan Koster

**Jokes**

Brian:  To understand recursion you must first understand recursion.

Michael: A programmer was found dead in the shower. Next to their body was a bottle of shampoo with the instructions 'Lather, Rinse and **Repeat**'.
