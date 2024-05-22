# Python Bytes 360
Sponsored by [**Scout APM**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Note: **No episode next week**. Michael will be at Microsoft Ignite in Seattle. 

**Happy Birthday**  to us (7 years old today)!

**Brian #1:** [**exclude_also with coverage.py**](https://dev.to/hugovk/til-excludealso-with-coveragepy-2hkm)

- Interesting exchange between [Pamela Fox, Hugo van Kemenade, and myself](https://mastodon.social/@hugovk/111364089644762276) where we all discover `exclude_also`, even though it’s been there since February
- This is cool because you can exclude common “should I cover this? It’s just for debugging.” kinda stuff, and other “I don’t wanna test that” places.
- To exclude code blocks, we can use `*# pragma: no cover*` in the code.
- Or we can list lines in coverage setting with `exclude_lines`, but you have to also list `# pragma: no cover`, which is weird.
- `exclude_also` just just right. It leaves all the inline excludes alone, and adds some regexes, and you can even just have one if that’s all you need, like `if __name__ == .__main__.:`
- See [coverage docs](https://coverage.readthedocs.io/en/7.3.2/excluding.html#advanced-exclusion)

**Michael #2:** [**Writeside**](https://www.jetbrains.com/writerside/?utm_source=pythonbytes)

- An IDE for writing the docs
- Write, test, build, and publish docs
- Docs-as-code out of the box
- Doc quality automation: Ensure documentation quality and integrity with 100+ on-the-fly inspections in the editor as well as tests in Live Preview and during build.
- Comes as a separate IDE as well as a plugin for PyCharm, etc.
- Pricing will be free + paid premium version (like PyCharm), fully free for now



**Brian #3:** **Extra, extra, extra**

- [Welcome Marie Nordin as the new PSF Community Communications Manager](https://pyfound.blogspot.com/2023/10/announcing-community-communications-mgr.html)
    - Woohoo! 
- [Pablo Galindo and Łukasz Langa started a podcast, called core.py](https://podcasters.spotify.com/pod/show/corepy)
    - Inside look into Python 3.13
    - Two episodes so far
        - The first core sprint for 3.13
        - Details on removing the GIL
    - [regexcrossword](https://regexcrossword.com)
        - Suggested by Kim van Wyk
        - actually really great for practicing regex rules
        [](https://podcasters.spotify.com/pod/show/corepy)
        **Michael #4:** [Chrome](https://9to5google.com/2023/11/02/google-chrome-web-integrity-api/) [not](https://9to5google.com/2023/11/02/google-chrome-web-integrity-api/) [proceeding with Web Integrity API deemed by many to be DRM](https://9to5google.com/2023/11/02/google-chrome-web-integrity-api/)

- Google’s premise for the internet:
    - ***The Internet should be constructed so that users can be identified, tracked, retargeted (and hence resold).*** — Google
- And privacy is important.
- So how do we make both of these work.
    - FLOCs?
    - Privacy Sandboxes?
    - Web Integrity?
- No, just no.
- How about you sell us ads the same way you surface search results (by what is on the page, not who is visiting it)
- Good riddance to this idea you corrupted organization. 
- [What was wrong with Web Integrity](https://arstechnica.com/gadgets/2023/07/googles-web-integrity-api-sounds-like-drm-for-the-web/)? Some comments
    - Issue #134 calls the idea "absolutely unethical and against the open web." 
    - Issue #113 say they "can't believe this is even proposed." 
    - Issue #127 adds: "Have you ever stopped to consider that **you're the bad guys**?”

**Extras** 

Brian:

- Mock chapter of [pytest: working with projects](https://courses.pythontest.com/p/pytest-working-with-projects), the 2nd course in [The Complete pytest Course](https://courses.pythontest.com/) series, is recorded and hopefully releasing today. At the very least some time this week.
- PyCharm has sent me a bunch of coupon codes for students of [The Complete pytest Course](http://ttps://courses.pythontest.com/). 
    - Sign up for the course and ask me for the code, and I’ll send it to you. 
- Nov 21 webinar with yours truly: [**Do You Do Enough Testing? pytest to the Rescue!**](https://info.jetbrains.com/pycharm-webinar-november21-2023.html)

Michael:

- [We Just Gave $500,000 to Open Source Maintainers](https://blog.sentry.io/we-just-gave-500-000-dollars-to-open-source-maintainers/?utm_medium=organic-social&utm_source=mastodon&utm_campaign=oss-fy24q3-brand&utm_content=blog-fundfest23-learnmore) - Sentry (thank you)
- `ruff format` + pycharm [follow up](https://python-bytes-static.nyc3.digitaloceanspaces.com/ruff-pycharm-nov-2023.png)
- JetBrains AI is getting very good a commit messages
    - **Add exception handling in background_service.py**:
    - *Introduced try-except blocks to handle potential exceptions in the 'pending_jobs', 'start_job_processing', and 'run_pending_job' methods in background_service.py. This change enhances error handling and makes the service more robust by preventing crashes if a job or episode cannot be fetched or if an unknown job action is encountered.*
    - **Add assemblyai to requirements and update ruff version**:
    - This commit includes the addition of assemblyai package as part of the requirements.txt file, required to introduce new speech-to-text feature in our application.  Ruff version is also updated from 0.1.3 to 0.1.4 due to bug fixes and stability improvements in the new version. Assemblyai also includes dependencies like pydantic and websockets.
- [GPT4All](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-api/README.md) follow up
- Got some nice feedback on my statement on [PyCon 2024’s health and safety policy](https://us.pycon.org/2024/about/health-safety-guidelines/)
    - More I think about it, the more out of touch it seems
    - Comparisons, no mask requirements for any of:
        - GitHub Universe - N,NNN? attendees
        - CES - 180,000 attendees
        - SXSW - 152,000 attendees
        - KubeCon - 12,000 attendees
        - Adobe Summit - 10,000 attendees
        - Mobile World Conference - 109,500 attendees
        - DeveloperWeek - 2,000 attendees
        - Microsoft Ignite - 4,000 attendees
        - WWDC - unkown

**Joke:** 

- **The plural of regex is *regrets*.**

