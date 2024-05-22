# Python Bytes 354
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** Ï[**logmerger**](https://github.com/ptmcg/logmerger) 

- Paul McGuire
- `logmerger` is a TUI for viewing a merged display of multiple log files, merged by timestamp.
- Built on textual
- Awesome flags:
    -  `--output -`  
        - to send the merged logs to stdout
    -   `--start START` and `--end END` 
        - start and end time to select time window for merging logs
- Caveats: 
    - new. no pip install yet. so clone the code or download
    - perhaps I jumped the gun on covering this, but it’s cool

**Michael #2:** [**The third and final Python 3.12 RC is out now**](https://mastodon.social/@hugovk/111091573987175428)

- Get your final bugs fixed before the full release
- **Call to action**: We strongly encourage maintainers of third-party Python projects to prepare their projects for 3.12 compatibilities during this phase
- [How to test](https://dev.to/hugovk/help-test-python-312-beta-1508).
- [Discussion on the issue](https://discuss.python.org/t/python-3-12-0rc3-released-honestly-the-final-release-candidate-i-swear/34093?u=hugovk).
- Count down until October 2nd, 2023.

**Brian #3:** [**The Python dictionary dispatch pattern**](https://jamesg.blog/2023/08/26/python-dictionary-dispatch/)

- I kinda love (and hate) jump tables in C
- We don’t talk about dictionary dispatch much in Python, so this is nice, if not dangerous.
- Short story: you can store lambdas or functions in dictionaries, then look them up and call them at the same time.
- Also, I gotta shout out to the first blogroll I’ve seen in a very long time. 
    - Should we bring back blogrolls?

**Michael #4:** [**Visualizing the CPython Release Process**](https://sethmlarson.dev/security-developer-in-residence-weekly-report-9)

- by Seth Larson
- Here’s the deal (you should [see the image in the article](https://sethmlarson.dev/security-developer-in-residence-weekly-report-9) 😉 )
    1. Freeze the [python/cpython](https://github.com/python/cpython) release branch. This is done using GitHub Branch Protections.
    2. Update the Release Manager's fork of [python/cpython](https://github.com/python/cpython).
    3. Run Python release tools (release-tool, blurb, sphinx, etc).
    4. Push diffs and signed tag to Release Manager's fork.
    5. Git tag is made available to experts for Windows and macOS binary installers.
    6. Source tarballs, Windows, and macOS binary installers built and tested concurrently.
        - 6a: Release manager builds the `tgz` and `tar.xz` source files for the Python release. This includes building the updates documentation.
        - 6b: Windows expert starts the [Azure Pipelines](https://github.com/python/release-tools/tree/master/windows-release) configured to build Python.
        - 6c: macOS Expert builds the macOS installers.
    7. All artifacts (source and binary) are tested on their platforms.
    8. Release manager signs all artifacts using Sigstore and GPG.
    9. All artifacts are made available on python.org.
    10. After artifacts are published to python.org, the git commit and tag from the Release Manager's fork is pushed to the release branch.


**Extras** 

Brian:

- [**The Complete pytest Course**](https://testandcode.teachable.com/p/the-complete-pytest-course), [**part 2, Ch 7 Testing Strategy**](https://testandcode.teachable.com/p/pytest-working-with-projectshttps://testandcode.teachable.com/p/pytest-working-with-projects) went up this weekend.
    - Only 9 more chapters to go
- [**“Test & Code” → “Python Test”**](https://testandcode.com/207)
    - Full version: “The Python Test Podcast” → “Test & Code” → “Python Test”
    - Also: “Python (Bytes | People | Test)” 

Michael:

- If you’re at [PyBay](https://pybay.com), come say “hi”
- [EuroPython 2023 Videos up](https://www.youtube.com/playlist?list=PL8uoeex94UhFcwvAfWHybD7SfNgIUBRo-)
- [Django + HTMX](https://training.talkpython.fm/courses/htmx-django-modern-python-web-apps-hold-the-javascript) has a few days of early-bird discount left

**Joke:** [**Are you sleeping?**](https://www.reddit.com/r/programminghumor/comments/15tnhhs/so_true/) 

