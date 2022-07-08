# Python Bytes 290

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

Special guest: [**Nick Muoh**](https://twitter.com/Spirix3)

**Brian #1:** [**picologging**](https://github.com/microsoft/picologging)

- From a [tweet by Anthony Shaw](https://twitter.com/anthonypjshaw/status/1539735691890163714?s=20&t=AofRg_xUHlAmMMhG4uMHlA)
- From README.md
- “early-alpha” stage project with some incomplete features. (cool to be so up front about that)
    - “Picologging is a high-performance logging library for Python. picologging is 4-10x faster than the `logging` module in the standard library.”
    - “Picologging is designed to be used as a *drop-in* replacement for applications which already use logging, and supports the same API as the `logging` module.”
- Now you’ve definitely got my attention.
- For many common use cases, it’s just way faster. 
- Sounds great, why not use it? A few limitations listed:
    - process and thread name not captured. 
    - Some logging globals not observed: `logging.logThreads`, `logging.logMultiprocessing`,  `logging.logProcesses`
    - Logger will always default to the Sys.stderr and not observe (emittedNoHandlerWarning).

**Michael #2:** [**CheekyKeys**](https://github.com/everythingishacked/CheekyKeys)

- via Prayson Daniel
- What if you could silently talk to your computer?
- CheekyKeys uses OpenCV and MediaPipe's Face Mesh to perform real-time detection of facial landmarks from video input.
- The primary input is to "type" letters, digits, and symbols via Morse code by opening and closing your mouth quickly for `.` and slightly longer for `-`.
- Most of the rest of the keyboard and other helpful actions are included as modifier gestures, such as:
    - `shift`: close right eye
    - `command`: close left eye
    - `arrow up/down`: raise left/right eyebrow
    - …
- Watch [the video](https://www.youtube.com/watch?v=rZ0DBi1avMM) where he does a coding interview for a big tech company using no keyboard.

**Nick** **#3:**  [**Is Google’s**](https://www.theguardian.com/technology/2022/jun/12/google-engineer-ai-bot-sentient-blake-lemoine) [LaMDA Model Sentient?](https://www.theguardian.com/technology/2022/jun/12/google-engineer-ai-bot-sentient-blake-lemoine)

- authored by [**Richard Luscombe**](https://www.theguardian.com/profile/richardluscombe) (The Guardian)
- The Google engineer who thinks the company’s AI has come to life
- [Transcript of conversation](https://cajundiscordian.medium.com/is-lamda-sentient-an-interview-ea64d916d917)

**Brian #4:** [**richbench**](https://github.com/tonybaloney/rich-bench)

- Also from Anthony
- “A little Python benchmarking tool.”
- Give it a list of (first_func, second_func, “label”), and it times them and prints out a comparison.
- Simple and awesome. 

```
    def sort_seven():
        """Sort a list of seven items"""
        for _ in range(10_000):
            sorted([3,2,4,5,1,5,3])
    
    def sort_three():
        """Sort a list of three items"""
        for _ in range(10_000):
            sorted([3,2,4])
    
    __benchmarks__ = [
        (sort_seven, sort_three, "Sorting 3 items instead of 7")
    ]
```

**Michael #5:** [**typeguard**](https://github.com/agronholm/typeguard)

- A run-time type checker for Python
- Three principal ways to do type checking are provided, each with its pros and cons:
    - Manually with function calls
    - `@typechecked` decorator
    - import hook (`typeguard.importhook.install_import_hook()`)
- Example:

```
    @typechecked
    def some_function(a: int, b: float, c: str, *args: str) -> bool:
        ...
        return retval
```

**Nick** **#6:** [**CustomTkinter**](https://github.com/TomSchimansky/CustomTkinter)

- A modern and customizable python UI-library based on Tkinter. 

**Extras** 


Michael:

- [**OpenSSF Funds Python and Eclipse Foundations**](https://openssf.org/blog/2022/06/20/openssf-funds-python-and-eclipse-foundations-and-acquires-sos-dev-through-alpha-omega-project/) - OpenSSF’s Alpha-Omega Project has committed $400K to the Python Software Foundation (PSF), in order to create a new role which will provide security expertise for Python, the Python Package Index (PyPI), and the rest of the Python ecosystem, as well as funding a security audit. (via Python Weekly)

Nick: 

- [Terms of Service Didn’t Read](https://tosdr.org/) -  Terms of Service; Didn't Read” (short: ToS;DR) is a young project started in June 2012 to help fix the “biggest lie on the web”: almost no one really reads the terms of service we agree to all the time.

**Joke:** 

- [**Serverless**](https://twitter.com/pr0grammerhum0r/status/1536362784144908288?s=21&t=XQLdkT0BwFv4s15eHbBmPQ)
- [A DevOps approach to COVID-19](https://twitter.com/the_unix_guru/status/1541084815927164933)
