# Python Bytes 241

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pytestbook.com)!

Special guest: [**Jay Miller**](https://twitter.com/kjaymiller)

**Michael #1:** [**Autosync all branches of a fork**](https://twitter.com/ywalia01/status/1390629366527234051)

- Use GitHub actions to keep your fork in sync
- Step 1: make changes in a separate branch (a branch other than main) to keep the working tree clean and avoiding conflicts with upstream
- Step 2: Add a new workflow under the “actions” section. We are going to follow the Fork-Sync-With-Upstream-action from the Actions Marketplace. Copy the YAML in the article being careful to use the right repo/branch names
- Step 3: click on Start Commit and Commit new file and that's it!
- See your running workflow in the actions tab

**Brain #2:** [**Measuring memory usage in Python: it’s tricky!**](https://pythonspeed.com/articles/measuring-memory-python/)

- Itamar Turner-Trauring
- Nice, easy to follow discussion of memory
- Cool example to allocate 3 GB 
	- `arr = np.ones((1024, 1024, 1024, 3), dtype=np.uint8)`
	- that’s a 4 dimensional array of bytes, 1k x 1k x 1k x 3
- “Resident Memory” measured with `psutil.Process().memory_info().rss` 
	- rss = “Resident Set Size”, or “non-swapped physical memory”
	- returns bytes, so `/ (1024 * 1024)` gives MB
- Shows a little more than 3 GB
- Doing nothing to process, but opening a few tabs in a browser and re-running `rss` shows a reduction due to some memory being saved to disk.
- Fil profiler can show peak allocated memory.
- Memory
	- Resident Memory : RAM usage
	- Allocated Memory : what we asked for, not really measurable
	- Peak Allocated Memory : kinda the same, but not, and it’s measurable
- Tradeoffs between measuring the two

**Jay #3:** [**Python f-strings can do more than you thought. f'{val=}', f'{val!r}', f'{dt:%Y-%m-%d}'**](https://www.youtube.com/watch?v=BxUxX1Ku1EQ)

- Caution! Just because you can doesn’t mean you should but sometimes you will be looking for a way to do something

**Michael #4:** [**10 Tips and Tools You Can Adopt in 15 minutes or Less To Level Up Your Dev Productivity**](https://www.youtube.com/watch?v=EsWTf5LOp3E)

1. Upgrade your shell (ohmyzsh or ohmyposh) + Windows Terminal with PS 7
2. [Secure.py](https://secure.readthedocs.io/en/latest/index.html) (or NWebSec for ASP.NET or …)
3. Use a UI for git (SourceTree, GitHub Desktop, PyCharm, VS Code, etc)
4. Sync your github forks
5. Use a good logging framework: Logbook, Loguru, even Sentry
6. SSL/TLS with Let’s Encrypt
7. 80/20 testing with sitemaps
8. PageSpeed insights (e.g for [Python Bytes](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fpythonbytes.fm%2F&tab=desktop))
9. Use an OS package manager: [Homebrew](https://brew.sh/), [Chocolaty](https://chocolatey.org/), or Linux’s built in)
10. Manage your dependencies with dependabot or even `pip-compile requirements.in --upgrade`
- [Full conference](https://www.youtube.com/watch?v=aGPYQ8LgtF8) video

**Brian #5:** [**How to Start a Production-Ready Django Project**](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html)

- Vitor Freitas
- Some great points for really any project, not just Django projects
- Make sure different environments work with the project, in this priority:
	- local, so clone and run is easy and new people can onboard fast
	- test, also local, so devs actually test with no issues
	- production, can be more complicated since only experienced people will need it, or it will get run by your CI/CD chain
	- production is also used in staging
- Configure git and venv from the beginning.
- Cool requirements files example with a `requirements` directory containing
	- `base.txt`
	- `test.txt` : `base.txt` + test stuff
	- `local.txt` : `test.txt` + dev stuff
	- `production.txt` : `base.txt` + any production only stuff
- Settings setup, also with switched implementation for local, test, prod
- Shared editor configuration, interesting addition
- Shared linting and styling tools, isort, black, flake8, …
- There are some Django specifics also, like app structure.


**Jay #6:** [**Bunch**](https://bunchapp.co)

- macOS application that allows you to create starting and finishing workflows
- **[How Jay sets up and tears down the newsletter video](https://youtu.be/zDsyw5uU0wA)**

**Extras**


**Jay**

- [Monodraw - Make diagrams or outlines using ascii art](http://monodraw.helftone.com/)

**Joke** 

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/6025c6be09aa4603ccbbd487/8de8bd2a05ce79c62668723263a3126b/joke.png)



