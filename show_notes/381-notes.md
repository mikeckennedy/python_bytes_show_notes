# Python Bytes 381

Sponsored by ScoutAPM: [pythonbytes.fm/scout](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of 

the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1:** [**Announcing py2wasm: A Python to Wasm compiler**](https://wasmer.io/posts/py2wasm-a-python-to-wasm-compiler)

- py2wasm converts your Python programs to WebAssembly, running them at 3x faster speeds
- thanks to [Nuitka](https://nuitka.net/)

**Brian #2:** **Exploring Python packages with** [**Oven**](https://oven.fming.dev) **and** [**PyPI Browser**](https://pypi-browser.org)

- [pypi.org](https://pypi.org) is great, but there are some handy alternatives
- [**Oven**](https://oven.fming.dev) 
  - Shows how to install stuff with pip, pdm, rye, and poetry
  - Similar meta and description as PyPI
  - Includes README.md view (no tables yet, though)
  - Nice listing of versions
  - Ability to look at what files are in wheels and tarballs (very cool) 
  - Can deploy yourself. Node/Remix app.
  - Really slick.
- [PyPI Browser](https://pypi-browser.org)
  - View versions
  - View wheel and tarball contents.
  - Metadata and contents.
  - No README view
  - Is a Starlette app that you can deploy on your on with a private registry. So that’s cool.

SPONSOR DETAILS: SCOUT APM

**Michael #3:** [PyCharm Local LLM](https://www.youtube.com/watch?v=DLBiJ5kYUFg)

- Pretty awesome full line completer based on a local LLM for PyCharm
- Requires PyCharm Professional
- An example, given this partial function in Flask:

```
@blueprint.get('/listing')
def listing():
  videos = video_service.all_videos()
```

Typing ret →

![img](https://python-bytes-static.nyc3.digitaloceanspaces.com/llm-complete.png)

That is, typing ret autocompletes to:

```
return flask.render_template('home/listing.html', videos=videos)
```

Which is pretty miraculous, and correct.

**Brian #4:** **Google shedding Python devs** **(at** **least in the US).**

- [Google lays off staff from Flutter, Dart and Python teams weeks before its developer conference](https://techcrunch.com/2024/04/29/google-lays-off-staff-from-flutter-dart-python-weeks-before-its-developer-conference/) - techcrunch
- [Python, Flutter teams latest on the Google chopping block](https://www.theregister.com/2024/04/29/google_python_flutter_layoffs/) - The Register
  - “Despite Alphabet last week [reporting](https://www.theregister.com/2024/04/26/register_kettle_ai/) a 57 percent year-on-year jump in net profit to $23.66 billion for calendar Q1, more roles are being expunged as the mega-corp cracks down on costs.”
  - “As for the Python team, the current positions have [reportedly](https://social.coop/@Yhg1s/112332127058328855) been "reduced" in favor of a new team based in Munich.”
- MK: Related and timely: [How one power-hungry leader destroyed Google search](https://www.wheresyoured.at/the-men-who-killed-google/)

**Extras** 

Brian:

- [Python Gotcha: strip, lstrip, rstrip can remove more than expected](https://andrewwegner.com/python-gotcha-strip-functions-unexpected-behavior.html)
  - Reminder: You probably want .removesuffix() and .removeprefix() 

Michael:

- [Using Llama3](https://lmstudio.ai/blog/llama-3) in [LMStudio](https://lmstudio.ai)

**Joke:**  [Broken System](https://devhumor.com/media/broken-system)