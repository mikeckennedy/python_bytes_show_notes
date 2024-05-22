# Python Bytes 216
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: [Jousef Murad](https://twitter.com/Jousefm2), Engineered Mind podcast ([audio](https://overcast.fm/itunes1510183304/engineered-mind-podcast-engineering-ai-neuroscience), [video](https://www.youtube.com/watch?v=l_h-wkpNoW4))

YOUTUBE: id=*Jc_VSHpBM7Y* 

**Brian #1:** **pip search. Just don’t.**

- `pip search <query>` is supposed to “Search for PyPI packages whose name or summary contains <query>”
- The search feature looks like it’s going to be removed and the PyPI api for it removed.
- **Alternative, and better approach, just manually look at pypi.org and search for stuff.** 
- Right now it does this:
```
    $ pip search pytest
    ERROR: Exception:
    Traceback (most recent call last):
    ... <longish traceback ommited> ---
    xmlrpc.client.Fault: <Fault -32500: "RuntimeError: PyPI's XMLRPC API has been temporarily disabled due to unmanageable load and will be deprecated in the near future. See https://status.python.org/ for more information.">
```
- The [Python Infrastructure status page](https://status.python.org/) says, as of Jan 12: “**Update** - The XMLRPC Search endpoint remains disabled due to ongoing request volume. As of this update, there has been no reduction in inbound traffic to the endpoint from abusive IPs and we are unable to re-enable the endpoint, as it would immediately cause PyPI service to degrade again.”
- This started becoming a problem in mid December.
- The endpoint was just never architected to handle the scale it’s getting now. 
- There’s a current issue [“Remove the pip search command”](https://github.com/pypa/pip/issues/5216), open on pip.
	- The commend thread is locked now, but you can read some of the history.
- I personally don’t understand the need to hammer search with a CI system or other. 
	- Probably should be using a local cache or local pypi mirror for an active/aggressive CI system.
- If you have scripts or jobs that run `pip search` , it ain’t gonna work, so probably best to remove that.

**Michael #2:** [**QPython - Scripting for Android with Python**](http://qpython.com/)

- Python REPL on Android - interesting
- Scripting Android tasks with Python - more interesting
- Free, open source app that is ad supported.
- Some people have commented that their phone is their only “computer”
- With SL4A features, you can use Python programming to control Android work:
	- Android Apps API, such as: Application, Activity, Intent & startActivity, SendBroadcast, PackageVersion, System, Toast, Notify, Settings, Preferences, GUI
	- Android Resources Manager, such as: Contact, Location, Phone, Sms, ToneGenerator, WakeLock, WifiLock, Clipboard, NetworkStatus, MediaPlayer
	- Third App Integrations, such as: Barcode, Browser, SpeechRecongition, SendEmail, TextToSpeech
	- Hardwared Manager: Carmer, Sensor, Ringer & Media Volume, Screen Brightness, Battery, Bluetooth, SignalStrength, WebCam, Vibrate, NFC, USB

**Jousef #3:** **Thesis: Deep Learning assistant for designers/engineers** 

- [PyTorch (3D)](https://pytorch3d.org/) / TensorFlow
- The thesis: what is it actually about & goal of the thesis
- Libraries mainly used: numpy, pandas
- (Reinforcement Learning & GANs)

**Brian #4:** [**sortedcontainers**](http://www.grantjenks.com/docs/sortedcontainers/index.html)

- Thanks to Fanchen Bao for the topic suggestion.
- Pure-Python, as fast as C-extensions, sorted collections library.
```
    >>> from sortedcontainers import SortedList
    >>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
    >>> sl
    SortedList(['a', 'b', 'c', 'd', 'e'])
    >>> sl *= 10_000_000
    >>> sl.count('c')
    10000000
    >>> sl[-3:]
    ['e', 'e', 'e']
    >>> from sortedcontainers import SortedDict
    >>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
    >>> sd
    SortedDict({'a': 1, 'b': 2, 'c': 3})
    >>> sd.popitem(index=-1)
    ('c', 3)
    >>> from sortedcontainers import SortedSet
    >>> ss = SortedSet('abracadabra')
    >>> ss
    SortedSet(['a', 'b', 'c', 'd', 'r'])
    >>> ss.bisect_left('c')
    2
```

- “All of the operations shown above run in faster than linear time.”
- Types:
	- SortedList
	- SortedKeyList (like SortedList, but you pass in a key function, similar to key in Pythons `sorted` function.)
	- SortedDict
	- SortedSet
- [Great documentation](http://www.grantjenks.com/docs/sortedcontainers/index.html) and tons of performance metrics in the docs.

**Michael #5:** [**Łukasz Langa Typed Twitter Thread**](https://twitter.com/brianokken/status/1345438719721918464?cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email)

- Let’s riff on typing for a bit. 
- Here is my philosophy: If I have to type more than three characters to complete a symbol in my editor, something is wrong. 
- e.g. to go from `email_service.` → `email_service.send_account_email()` I should only need to type `.sae` then tab/enter. These types of things are vastly better because of type hints.
- Python type hints are more malleable than even TypeScript.
- Lukasz is addressing this comment: *Controversial take: Types in a Python code-base are a net negative*.
- Points
	- put enough annotations and tooling connects the dots, making plenty of errors evident.
	- The most common to me at least is when a None creeps in. 
	- The second bug often caught by type checkers is on the "return" boundary: one of your code paths forgets a return.
	- squiggly lines in your editor
	- Microsoft is now developing powerful type checking and code completion for Python in VSCode. This effort employs a member of the Python Steering Council, and possibly also the creator of Python himself soon. You think they would settle for "illusion of productivity"?

**Jousef #6:** 

- Point Cloud operations → [open3d](http://www.open3d.org/)

Extras:

Michael:

- via Francisco Giordano Silva: On Brian's ref to using numpy all for array element-wise comparison, also please check out `numpy.allclose` method. Allows you to compare two arrays based on a given tolerance.

Brian: 

- Just this: 2021 is exhausting so far.
- [Test & Code](https://testandcode.com/) has shifted to every other week to allow time for other projects I’m working on.
	- This is probably a short term change. But I don’t know for how long. It’s definitely not going away though. Just slowing down a bit.

Jousef: [Engineered Mind podcast](https://overcast.fm/itunes1510183304/engineered-mind-podcast-engineering-ai-neuroscience)


