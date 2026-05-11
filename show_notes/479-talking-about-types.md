# #479: Talking About Types

Show Intro

Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 11am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1: [httpxyz one month in](https://tildeweb.nl/~michiel/httpxyz-one-month-in.html)**

- First version of httpxyz contained just the fixes to get zstd working, and the fixes to get the test suite running on python 3.14, some ‘housekeeping’ changes related to the renaming
- End of March: a compatibility shim that allows you to use httpxyz even with third-party packages that import httpx themselves, as long as you import httpxyz first.
  - Importing `httpxyz` automatically registers it under the `httpx` name in `sys.modules` , see https://httpxyz.org/httpx-compatibility/
- Fixed a WHOLE bunch of performance related issues by forking httpcore

**Brian #2: [Learn concurrency - a deep dive into multithreading with Python](https://blog.geekuni.com/2026/04/python-concurrency.html)**

- Nikos Vaggalis
- “Whenever you are trying to speed up code using multiple cores, always ask yourself: “Do these threads need to talk to each other right now?” If the answer is yes, it will be slow. The best parallel code splits a big job into completely isolated chunks, processes them separately, and merges the results at the finish line.”
- Good overview of thread concurrency with Python and how that’s been improved dramatically with free-threaded Python
- Defines lots of terms you come across, including “embarrassingly parallel multithreading”
- There’s a counter example that’s nice
  - Start with a shared resource, a counter, and multiple threads updating it
  - Attempt to fix with `threading.Lock()`, which fixes it, but slows things down
  - Good explanation of why
  - Proper fix with `concurrent.futures` and separating the work of different threads so that they can be independent and their results can be combined when they’re all finished.

**Michael #3: [pip 26.1 - lockfiles and dependency cooldowns](https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/)**

- Python 3.9 is no longer supported
- Experimental: installing from pylock files
- Dependency cooldowns (see [my post about this](https://mkennedy.codes/posts/python-supply-chain-security-made-easy/))
- Lifting several 2020 resolver limitations

**Brian #4: [Python 3.15 `sentinal` values from PEP 661](https://peps.python.org/pep-0661/)**

```python
MISSING = sentinel("MISSING")
def next_value(default: int | MISSING = MISSING):
    ...
    if default is MISSING:
       ...
```
- Take a name str as a constructor parameter
- Intended to be compared with `is` operator, similar to `None`
- Sentinal objects can be used as a type, also similar to `None`
  - and can be combined with other types with `|`.
- Unlike `None`, sentinal values are truthy. (Elipses `...` are also truthy)
  - This seems like a strange choice. but I guess it must have made sense to someone.
  - It does force you to use `is` instead of depending on False-ness, so I guess it’ll make code using sentinels more readable.
- Interesting that the PEP was started in 2021, and we’re finally getting it this year.

**Extras**

Brian:
- [Before GitHub](https://lucumr.pocoo.org/2026/4/28/before-github/) - Armin Ronacher
- [tenacity](https://tenacityaudio.org) - cross-platform multi-track audio editor/recorder
  - learned about it from Armin’s article

**Joke:**

- Joke option [Make it myself](https://xkcd.com/3233/)
  - Seems similar to what people think about software now

Links

- [httpxyz one month in](https://tildeweb.nl/~michiel/httpxyz-one-month-in.html)
- [httpxyz.org/httpx-compatibility](https://httpxyz.org/httpx-compatibility/)
- [Learn concurrency - a deep dive into multithreading with Python](https://blog.geekuni.com/2026/04/python-concurrency.html)
- [pip 26.1 - lockfiles and dependency cooldowns](https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/)
- [my post about this](https://mkennedy.codes/posts/python-supply-chain-security-made-easy/)
- [Python 3.15 `sentinal` values from PEP 661](https://peps.python.org/pep-0661/)
- [Before GitHub](https://lucumr.pocoo.org/2026/4/28/before-github/)
- [tenacity](https://tenacityaudio.org)
- [Make it myself](https://xkcd.com/3233/)
