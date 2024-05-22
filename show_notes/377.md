Sponsored by ScoutAPM: [**pythonbytes.fm/scout**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of 

the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1:** [**justpath**](https://github.com/epogrebnyak/justpath)

- Inspect and refine PATH environment variable on both Windows and Linux.
- Raw, count, duplicates, invalids, corrections, excellent stuff.
- Check out [the video](https://asciinema.org/a/642726)

**Brian #2:** **xz back door**

- In case you kinda heard about this, but not really.
- Very short version: 
  - A Microsoft engineer noticed a performance problem with ssh and tracked it to a particular version update of xz.
  - Further investigations found a multi-year installation of a fairly complex back door into the xz by a new-ish contributor. But still contributing over several years. First commit in early 2022.
  - The problem is caught. But if it had succeeded, it would have been bad.
  - Part of the issue of how this happened is due to having one primary maintainer on a very widely used tool included in tons-o-Linux distributions.
- Some useful articles
  - [**Everything I Know About the XZ Backdoor**](https://boehs.org/node/everything-i-know-about-the-xz-backdoor) - Evan Boehs - recommended read
- Don’t think your affected? Think again if you use homebrew, for example:
  - [**Update and upgrade Homebrew and**](https://micro.webology.dev/2024/03/29/update-and-upgrade.html)[ ](https://micro.webology.dev/2024/03/29/update-and-upgrade.html)[**`xz`**](https://micro.webology.dev/2024/03/29/update-and-upgrade.html)[ **versions**](https://micro.webology.dev/2024/03/29/update-and-upgrade.html)
- Notes
  - Open source maintenance burnout is real
  - Lots of open source projects are maintained by unpaid individuals for long periods of time.
  - Multi-year sneakiness and social bullying is pretty hard to defend against.
  - Handing off projects to another primary maintainer has to be doable.
    - But now I think we need better tools to vet contributors. 
    - Maybe? Or would that just suppress contributions?
- One option to help with burnout: 
  - JGMM, Just Give Maintainers Money: [**Software Needs To Be More Expensive**](https://blog.glyph.im/2024/03/software-needs-to-be-more-expensive.html) - Glyph

**Michael #3:**  [LPython](https://lpython.org)

- LPython aggressively optimizes type-annotated Python code. It has several backends, including LLVM, C, C++, and WASM. 
- LPython’s primary tenet is speed.
- Play with the wasm version here: [dev.lpython.org](https://dev.lpython.org)
- Still in alpha, so keep that in mind.

**Brian #4:** [**dramatic**](https://github.com/treyhunner/dramatic)

- Trey Hunner
- More drama in the software world. This time in the Python. 
- Actually, this is just a fun utility to make your Python output more dramatic.
- More fun output with [terminaltexteffects](https://github.com/ChrisBuilds/terminaltexteffects)
  - suggested by Allan

**Extras** 

Brian:

- [Textual how has a new inline feature in the new release.](https://github.com/Textualize/textual/releases/tag/v0.55.0)

Michael:

- My keynote talk is out: [The State of Python in 2024](https://www.youtube.com/watch?v=coz1CGRxjQ0)
- Have you browsed your [github feed](https://github.com) lately?
- [3.10, 3.9, 3.8 security updates](https://pythoninsider.blogspot.com/2024/03/python-31014-3919-and-3819-is-now.html)

**Joke:** [Definition of terms](https://python-bytes-static.nyc3.digitaloceanspaces.com/definition-of-methodolgy-terms.jpg)