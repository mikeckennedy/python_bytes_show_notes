# Python Bytes 323
Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken) - may be a minute or two late. 
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)
- Special guest: [**Pamela Fox**](https://fosstodon.org/@pamelafox) - @pamelafox@fosstodon.org

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** ƒ[**camply**](https://github.com/juftin/camply)

- A tool to find campsites at sold out campgrounds through sites like recreation.gov and Yellowstone
-  Finding reservations at sold out campgrounds can be tough.
- Searches the APIs of booking services like [**recreation.gov**](https://recreation.gov) (which indexes thousands of campgrounds across the USA) to continuously check for cancellations and availabilities to pop up.
- Once a campsite becomes available, camply sends you a notification to book your spot!
- Want to camp in a tower in California?
  
    camply campgrounds --search "Fire Lookout Towers" --state CA

**Brian #2:** [**hatch-fancy-pypi-readme**](https://github.com/hynek/hatch-fancy-pypi-readme)

- Your ✨Fancy✨ Project Deserves a ✨Fancy✨ PyPI Readme! 🧐
- Hynek Schlawack
- Include lots of extras in a README.md
    - text fragments
    - files, like AUTHORS.md or Changelog.md, with custom start, stop, pattern includes, etc.
    - regular expression substitutions
- Several projects with examples, including [black](https://github.com/psf/black/blob/main/pyproject.toml).

**Pamela** **#3:** [**Pyodide dev branch now supports 3.11**](https://github.com/pyodide/pyodide/pull/3252)

- [Python 3.11 PR](https://github.com/pyodide/pyodide/pull/3252)
- [Benchmark Py3.11 and Py3.10](https://github.com/pyodide/pyodide/issues/3503) 
- [pyodide console](https://pyodide.org/en/latest/console.html)
- [TODO list for 0.23.0 alpha release](https://github.com/pyodide/pyodide/issues/3410) 
- [Dis-this: specializing adaptive interpreter](http://www.dis-this.com) 
- [Recursion visualizer](https://www.recursionvisualizer.com/)

**Michael #4:** [**EU hates open source?**](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13410-Cyber-resilience-act-new-cybersecurity-rules-for-digital-products-and-ancillary-services/F3376611_en)

- via **Pamphile Roy**
- The Cyber Resilience Act (CRA) is an interesting and important proposal for a European law that aims to drive the safety and integrity of software
- The proposal includes a requirement for self-certification by suppliers of software to attest conformity with the requirements of the CRA including security, privacy and the absence of Critical Vulnerability Events (CVEs).
- We recognize that the European Commission has framed an exception in recital 10 attempting to ensure these provisions do not accidentally impact Open Source software. 
- However, drawing on more than two decades of experience, we at the Open Source Initiative can clearly see that the current text will cause extensive problems for Open Source software.
- Since the goal is to avoid harming Open Source software this goal should be stated at the start of the paragraph as the rationale, replacing the introductory wording about avoiding harm to "research and innovation" to avoid over-narrowing the exception.
- The reference to "non-commercial" as a qualifier should be substituted. The term “commercial” has always led to legal uncertainty for software and is a term which should not be applied in the context of open source
- OSI recommends further work on the Open Source exception to the requirements within the body of the Act to *exclude all activities prior to commercial deployment of the software* and to clearly ensure that *responsibility for CE marks does not rest with any actor who is not a direct commercial beneficiary of deployment*.

**Brian #5:** [**So, Single (‘) or Double (“) Quotes in Python?**](https://medium.com/pythoniq/so-single-or-double-quotes-in-python-47c2e7425f32)

- Marcin Kozak
- PEP8 doesn’t recommend anything.
- REPL uses single quotes.
    >>> x = "one"
    >>> x
    'one'
- Black sides with “double quotes”, due to the apostrophe in the string problem.
    - 'Don\'t be so sad.' vs “Don’t be sad.”
- You get to pick, and don’t be bullied by black-fanatics.
- There’s always [blue](https://pypi.org/project/blue/), which is just like black, but
    - defaults to single-quotes
    - line length defaults to 79, not black’s 88.
    - preserves whitespace before hash marks for right hanging comments (so multiple lines can line up).

**Pamela** **#6:** [**Frozen-Flask**](https://pythonhosted.org/Frozen-Flask) 

- [Pamela’s PR for moving to Frozen Flask](https://github.com/pamelafox/pamelafox-site/pull/10/files) 
- [Stepping down as a maintainer](https://github.com/Frozen-Flask/Frozen-Flask/pull/128)

**Extras** 

Brian:

- What does everyone think of [GitHub pricing](https://github.com/pricing)?

Michael:

- Much much better transcripts, for example, [**last episode 322**](https://pythonbytes.fm/episodes/transcript/322/python-packages-let-me-count-the-ways).
    - Means [our search](https://pythonbytes.fm/search) works way better too
- The AI search wars have begun
    - [Microsoft Bing rockets to the top of the App Store after announcing ChatGPT integration](https://9to5mac.com/2023/02/08/microsoft-bing-rockets-to-top-of-app-store/)
    - [Google shares lose $100 billion after company's AI chatbot makes an error during demo](https://www.news8000.com/lifestyle/technology/google-shares-lose-100-billion-after-companys-ai-chatbot-makes-an-error-during-demo/article_aab57c1e-28b8-59b9-8f68-a99ab001a6c6.html)
- [Free PyCharm](https://talkpython.fm/pycharm-free) for all the Talk Python customers
- Thanks for the help with finding a good Flutter dev.
- Important Talk Python episode: [Fusion Ignition Breakthrough and Python](https://talkpython.fm/episodes/show/403/fusion-ignition-breakthrough-and-python)

Pamela:

- [Github pyproject.toml support](https://github.blog/changelog/2023-02-13-dependency-graph-supports-the-python-pep-621-standard/).
- [Python Package Template](https://github.com/microsoft/python-package-template)

**Jokes:** 

- [**$McTitle**](https://www.reddit.com/r/softwaregore/comments/zzuyhx/shouldnt_it_be_the_mctitle/)
- [**Worst input fields**](https://www.boredpanda.com/funny-worst-input-fields/)

