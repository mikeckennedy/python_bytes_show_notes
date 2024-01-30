# Python Bytes 369



Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Granian**](https://github.com/emmett-framework/granian)

- via Andy Shapiro and Bill Crook
- A Rust HTTP server for Python applications.
- Granian design goals are:
    - Have a single, correct HTTP implementation, supporting versions 1, 2 (and eventually 3)
    - Provide a single package for several platforms
    - Avoid the usual Gunicorn + uvicorn + http-tools dependency composition on unix systems
    - Provide stable [performance](https://github.com/emmett-framework/granian/blob/master/benchmarks/README.md) when compared to existing alternatives
- Could use better logging
    - But [making my own](https://github.com/emmett-framework/granian/issues/152) taught me maybe I prefer that!
- Originates from the [Emmett framework](https://emmett.sh).

**Brian #2:** [**pytest 8 is here**](https://pythontest.com/pytest/pytest-8-is-here/)

- Improved diffs:
    - Very verbose `-vv` is a colored diff, instead of a big chunk of red.
    - Python code in error reports is now syntax-highlighted as Python.
    - The sections in the error reports are now better separated.
    - Diff for standard library container types are improved.
    - Added more comprehensive set assertion rewrites for comparisons other than equality ==, with the following operations now providing better failure messages: !=, <=, >=, <, and >.
- Improvements to -r for xfailures and xpasses
    - Report tracebacks for xfailures when -rx is set.
    - Report captured output for xpasses when -rX is set.
    - For xpasses, add - in summary between test name and reason, to match how xfail is displayed.
    - *This one was important to me. Massively helps when checking/debugging xfail/xpass outcomes in CI. Thanks to Fabian Sturm, Bruno Oliviera, and Ran Benita for help to get this release.*
- Lots of other improvements
- See full [changelog](https://docs.pytest.org/en/stable/changelog.html) for all the juicy details. And then upgrade and try it out! 
- `pip install -U pytest`

**Michael #3:** **Assorted Docker Goodies**

- [OrbStack](https://orbstack.dev)
    - Say goodbye to slow, clunky containers and VMs
    - OrbStack is the fast, light, and easy way to run Docker containers and Linux. Develop at lightspeed with our Docker Desktop alternative.
- [Podman](https://podman.io)
    - Podman is an open source container, pod, and container image management engine. Podman makes it easy to find, run, build, and share containers.
        - **Manage containers (not just Podman.)**
        - Podman Desktop allows you to list, view, and manage containers from multiple supported container engines* in a single unified view.
        - Gain easy access to a shell inside the container, logs, and basic controls.
        - Works on Podman, Docker, Lima, kind, Red Hat OpenShift, Red Hat OpenShift Developer Sandbox.
- [CasaOS](https://casaos.io)
    - Your Personal Cloud OS.
    - Community-based open source software focused on delivering simple personal cloud experience around Docker ecosystem.
    - Also have the [ZimaCube](https://www.kickstarter.com/projects/icewhaletech/zimacube-personal-cloud-re-invented) hardware (Personal cloud. Re-invented.)

**Brian #4:** [**New GitHub Copilot Research Finds 'Downward Pressure on Code Quality'**](https://visualstudiomagazine.com/articles/2024/01/25/copilot-research.aspx)

- David Ramel
- Regarding “…the quality and maintainability of AI-assisted code compared to what would have been written by a human.”
- Q: "Is it more similar to the careful, refined contributions of a Senior Developer, or more akin to the disjointed work of a short-term contractor?"
- A: *"We find disconcerting trends for maintainability. Code churn -- the percentage of lines that are reverted or updated less than two weeks after being authored -- is projected to double in 2024 compared to its 2021, pre-AI baseline. We further find that the percentage of 'added code' and 'copy/pasted code' is increasing in proportion to 'updated,' 'deleted,' and 'moved 'code. In this regard, AI-generated code resembles an itinerant contributor, prone to violate the DRY-ness [don't repeat yourself] of the repos visited."*

**Extras** 

Brian:

- Did I mention pytest 8? Just  `pip install -U pytest` today
- And if you want to learn pytest super fast, check out [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course) or grab a copy of the book, [Python Testing with pytest](https://pythontest.com/pytest-book/)

Michael:

- I’d like to encourage people to join our mailing list. We have some fun plans and some of them involve [our newsletter](https://pythonbytes.fm/friends-of-the-show). It’s super private, no third parties, no spam and is based on my recent Docker and [Listmonk work](https://github.com/mikeckennedy/listmonk).
- [Big release for Pydantic](https://github.com/pydantic/pydantic/releases/tag/v2.6.0), 2.6.
- New essay: [Use Custom Search Engines Way More](https://mkennedy.codes/posts/you-should-use-custom-search-engines-way-more/)

**Joke:**  

- [Pushing to main](https://devhumor.com/media/better-call-saul)
- [Junior vs Senior engineer](https://packmates.org/@draconigen/111805683031473439?utm_source=pocket_saves)

