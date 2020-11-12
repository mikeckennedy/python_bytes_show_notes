# Python Bytes 208

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:** [**pip-chill - Make requirements with only the packages you need**](https://github.com/rbanffy/pip-chill)

- Ricardo Bánffy
- Like `pip freeze` but lists only the packages that are not dependencies of installed packages.
- Will be great for creating requirements.txt files that look like the ones you would write by hand.
- I wish it had an option to not list itself, but `pip-chill | grep -v pip-chill` works.

- What do I have installed?
```
    (foo) $ pip freeze
    appdirs==1.4.4
    black==20.8b1
    click==7.1.2
    mypy-extensions==0.4.3
    ...
```

- No really, what did I myself install?
```
    (foo) $ pip-chill 
    black==20.8b1
    pip-chill==1.0.0
```

- Without versions?
```
    (foo) $ pip-chill --no-version
    black
    pip-chill
```

- What did those things install as dependencies?
```
    (foo) $ pip-chill -v --no-version
    black
    pip-chill
    # appdirs # Installed as dependency for black
    # click # Installed as dependency for black
    ...
```

**Michael #2:** [**Windows update broke NumPy**](https://developercommunity2.visualstudio.com/t/fmod-after-an-update-to-windows-2004-is-causing-a/1207405)

- Sent in by Daniel Mulkey
- A recent Windows update broke some behavior that I think OpenBLAS (used by NumPy) relied on. 
- There's a [Developer Community thread here](https://developercommunity2.visualstudio.com/t/fmod-after-an-update-to-windows-2004-is-causing-a/1207405). 
- *I am a NumPy developer. We have been trying to track down a strange issue where after updating to windows 10 2004, suddenly code that worked no longer works. Here is* [*the NumPy issue*](https://github.com/numpy/numpy/issues/16744) *and here is the corresponding* [*issue in OpenBLAS*](https://github.com/xianyi/OpenBLAS/issues/2709)*. The problem can be summarized: when calling fmod, something is changed so that much later calling an OpenBLAS assembly routine fails. The only difference I can see in the registers that visual studio exposes is that after the call to fmod, register ST(0) is set to NAN.*
- Steve Dower and other Microsoft people have commented. 
- The fix is slated to take until January 2021 to be released, though there are workarounds for some scenarios.
- Matt P. posted a workaround:
	- For all those at home following along and looking for a quick fix, NumPy has released a bugfix 1.19.3 to work around this issue. The bugfix broke something else on Linux, so we had to revert the fix in release 1.19.4, but you can still install the 1.19.3 via
	- `pip install numpy==1.19.3`.
	- Note this is only works around the way this bug crashes NumPy (technically, in OpenBLAS which is shipped with NumPy), and may not fix all your problems related to this bug, Microsoft’s help is needed to do that.

**Brian #3:**  [**Build Plugins with Pluggy**](https://kracekumar.com/post/build_plugins_with_pluggy/)

- kracekumar
- Blog post related to talks given at PyGotham and PyCon India
- Pluggy is the plugin library used by pytest
- Article 
	- starts with a CLI application that has one output format.
	- Need is for more formats, implemented as plugins.
	- Quick look at pluggy architecture of **host/caller/core system** and **plugin/hook**.
	- Also plugin manager, hook specs, and hook implementations.
	- Walks through the changes to the application needed to support plugins.
- I’ve been waiting for an article on pluggy, and this is nice. 
- But I admit I’m still a little lost. I guess I need to watch one of the presentations and try to build something with pluggy.

**Michael #4:** [**LINQ in Python**](https://github.com/avilum/linqit)

- via Adam: I seem to recall that Michael had a C# background, so this might be of interest:
- Bringing LINQ-like expressions to Python with `linqit`
- Example:
```
    last_hot_pizza_slice = programmers.where(lambda e:e.experience > 15)
                          .except_for(elon_musk)
                          .of_type(Avi)
                          .take(3) # [<Avi>, <Avi>, <Avi>]
                          .select(lambda avi:avi.lunch) # [<Pizza>, <Pizza>, <Pizza>]
                          .where(lambda p:p.is_hot() and p.origin != 'Pizza Hut').
                          .last() # <Pizza>
                          .slices.last() # <PizzaSlice>
```
- Also interesting asq: [https://github.com/sixty-north/asq](https://github.com/sixty-north/asq)

**Brian #5:** [**Klio : a framework for processing audio files or any binary files, at large scale**](https://docs.klio.io/en/latest/index.html)

- [Recently open sourced by Spotify](https://engineering.atspotify.com/2020/11/04/its-all-just-wiggly-air-building-infrastructure-to-support-audio-research/)
- [An article about it](https://venturebeat.com/2020/10/13/spotify-open-sources-klio-a-framework-for-ai-audio-research/)
- Klio is based on Apache Beam and allows
	- integration with cloud processing engines
	- open graph of job dependencies
	- batch and streaming pipelines
- goals:
	- large-file input/output
	- scalability, reproducibility, efficiency
	- closer collaboration between researchers and engineers
- uses Python
- Obviously useful for Spotify, but they are hoping it will help with other audio research and applications.

**Michael #6:** [**Collapsing code cells in Jupyter Notebooks**](https://towardsdatascience.com/self-contained-reports-from-jupyter-notebooks-219a3887979d)

- via [Marco Gorelli](https://github.com/MarcoGorelli)
- You mentioned in that episode that you'd like to have a way of collapsing code cells in Jupyter Notebooks so you can export them as reports - incidentally, I wrote a little blog post about how to do that - in case it's useful/of interest to you, here it is! 
- Basically get a static HTML file that is the static notebook output but can start with the code cells collapsed and can toggle their visibility.

**Extras**

**Michael:**

- New Apple Silicon macs?
- Bot tweets: [**twitter.com/MichelARenard/status/1324269474544029696**](https://twitter.com/MichelARenard/status/1324269474544029696)

**Joke:**

By Richard Cairns

Q: Why did the data scientist get in trouble with Animal Welfare?
A: She was caught trying to import pandas.

“10e engineeeeeeeeers are the future.” - detahq
