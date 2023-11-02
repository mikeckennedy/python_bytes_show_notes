# Python Bytes 359
Sponsored by [**Scout APM**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** ****[**PyCon 2024 is up**](https://us.pycon.org/2024/)**?**

- May 15 - May 23, 2024 - Pittsburgh, Pennsylvania
- Conference breakdown:
    - Tutorials: May 15 - 16, 2024
    - Main Conference and Online: May 17 - 19, 2024
    - Job Fair: May 19, 2024
    - Sprints: May 20 - May 23, 2024
- Tickets aren’t on sale yet
- Unfortunately, I’m not going (see [**health and safety guidelines**](https://us.pycon.org/2024/about/health-safety-guidelines/))
- See the attendance numbers of time [**on Wikipedia**](https://en.wikipedia.org/wiki/Python_Conference)

**Brian #2:** [**Ruff formatter is production ready**](https://astral.sh/blog/the-ruff-formatter)

- [We reported the alpha release in September](https://pythonbytes.fm/episodes/show/353/hatching-another-episode)
- It’s fast, 30x faster than Black
- Provides >99.9% compatibility with Black, with a [list of known deviations](https://github.com/astral-sh/ruff/blob/main/docs/formatter/black.md)
- More configurable
- Bundled with ruff, `ruff format`
- Still in Beta, but considered production-ready
- Integration extensions for VSCode and PyCharm


**Michael #3:** [**gil--;**](https://mastodon.social/@hugovk/111293506058914553)

- The Python Steering Council has now formally accepted [PEP 703](https://peps.python.org/pep-0703/) ("Making the Global Interpreter Lock Optional in CPython")
- The **global interpreter lock will remain the default for CPython** builds and python.org downloads.
-  A new **build** configuration flag, --disable-gil will be added to the configure script that will build CPython with support for running without the global interpreter lock.
- "In short, the SC accepts PEP 703, but with clear provisio: 
    - that the rollout be gradual and break as little as possible,
    - that we can roll back any changes that turn out to be too disruptive – which includes potentially rolling back all of PEP 703 entirely if necessary (however unlikely or undesirable we expect that to be)."
- Removing the global interpreter lock requires substantial changes to CPython internals, but relatively few changes to the public Python and C APIs.
- The implementation changes can be grouped into the following four categories:
    - Reference counting
    - Memory management
    - Container thread-safety
    - Locking and atomic APIs

**Brian #4:** [**Why is the Django Admin “Ugly”?**](https://www.coderedcorp.com/blog/why-is-the-django-admin-ugly/)

- Vince Salvino
- Some great quotes from the article:
    - "The Django admin is not ugly, rather, no effort was made to make it a beautiful end-user tool.” - Ken Whitesell
    - “The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.” - Django docs
    - “The Django admin was built for Phil.” - Jacob Kaplan-Moss
    - “Even in the 0.9x days we used to have a image that said “Admin: it’s not your app”.” - Curtis Maloney
- As Curtis put it, “encouraging people to build their own management interface, and treat admin as a DB admin tool, has saved a lot of people pain... the effort to customise it grows far faster than the payoffs.”

**Extras** 

Brian:

- [**Local Conferences: Big Potential**](https://overtag.dk/v2/blog/local-conferences-big-potential/)

Michael:

- [**Data Science Jumpstart with 10 Projects course**](https://training.talkpython.fm/courses/data-science-jumpstart-with-10-projects) is out!
- [**PSF is X-ed out**](https://mastodon.social/@andymckay/111293685334582922) (or are they?)
- [**GPT4All**](https://gpt4all.io/index.html) is pretty excellent
- [**Fosstodon invites**](https://fosstodon.org/invite/fmM5PebT) from us (expires Nov 7 2023)

**Joke:** [Searching YouTube for bug fixes](https://www.reddit.com/r/programminghumor/comments/16065hs/this_is_me_right_now/)

