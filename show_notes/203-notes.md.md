# Python Bytes 203
Sponsored by DataDog: [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Michael #1:** [**Introducing DigitalOcean App Platform**](https://www.digitalocean.com/blog/introducing-digitalocean-app-platform-reimagining-paas-to-make-it-simpler-for-you-to-build-deploy-and-scale-apps)

- Reimagining PaaS to make it simpler for you to build, deploy, and scale apps.
- Many of our customers have come to DigitalOcean after their PaaS became too expensive, or after hitting various limitations.
- You can build, deploy, and scale apps and static sites by simply pointing to your GitHub repository. 
- Built on [DigitalOcean Kubernetes](https://www.digitalocean.com/products/kubernetes/), the App Platform brings the power, scale, and flexibility of Kubernetes without exposing you to any of its complexity.
- App Platform is built on open standards providing more visibility into the underlying infrastructure than in a typical closed PaaS environment.
- You can also enable ‘Autodeploy on Push,’ which automatically re-deploys the app each time you push to the branch containing the source code.
- To efficiently handle traffic spikes (planned or unplanned), the App Platform lets you scale apps horizontally (i.e., add more instances that serve your app) and vertically (beef up the instances with more CPU and memory resources). (with zero downtime)
- What can you build with the App Platform?  Web apps, Static sites, APIs, Background workers

**Brian #2:** ****[**Announcing Playwright for Python**](https://devblogs.microsoft.com/python/announcing-playwright-for-python-reliable-end-to-end-testing-for-the-web/)

- [playwright-python](https://github.com/microsoft/playwright-python)
- [playwrignt-pytest](https://github.com/microsoft/playwright-pytest)
- it’s a Microsoft thing
- the pitch: “With the Playwright API, you can author end-to-end tests that run on all modern web browsers. Playwright delivers automation that is faster, more reliable and more capable than existing testing tools.”
- timeout-free automation
	- automatically waits for the UI to be ready
- Intended to stay modern
	- emulation of mobile viewports
	- geolocation
	- web permissions
	- can automate scenarios across multiple pages
- cross browser
	- Chromium (Chrome and Edge), WebKit (Safari), and Firefox
	- Safari rendering even works on Windows and Linux
- pytest compatible
- Django compatible
- Can work within CI/CD, even GH actions.

**Michael #3:** [**Asynchronously Opening and Closing Files in asyncio**](https://nullprogram.com/blog/2020/09/04/)

- Article by Chris Wellons
- asyncio has support for asynchronous networking, subprocesses, and interprocess communication. However, it has nothing for asynchronous file operations — opening, reading, writing, or closing.
- If a file operation takes a long time, perhaps because the file is on a network mount, then the entire Python process will hang.
- Let’s build it!
- The usual way to work around the lack of operating system support for a particular asynchronous operation is to [dedicate threads to waiting on those operations](http://docs.libuv.org/en/v1.x/design.html#file-i-o). By using a thread pool, we can even avoid the overhead of spawning threads when we need them. Plus asyncio is designed to play nicely with thread pools anyway.
- `open()` uses with so build an `aopen()` to have `async with`. Here’s the tasty bit:
```
        def __aenter__(self):
            def thread_open():
                return open(*self._args, **self._kwargs)
            loop = asyncio.get_event_loop()
            self._future = loop.run_in_executor(None, thread_open)
            return self._future
```
- [aiofile](https://pypi.org/project/aiofile/) package 

**Brian #4:** [**Excel: Why using Microsoft's tool caused Covid-19 results to be lost**](https://www.bbc.com/news/technology-54423988)

- this article was on bbc.com, but it was in several places
- Nearly 16,000 coronavirus cases went unreported in England.
- Logs pulled together from data from commercial testing firms (filed as csv files) was combined in a Excel xls template so that it could then be uploaded to a central system and made available to the NHS Test and Trace team, as well as other government computer dashboards.
- XLS was one problem. Limit is about 65k rows.
- XLSX increases that limit by about 16 times.
- But still, …. Excel for this?
- Comment from Prof Jon Crowcroft from the University of Cambridge:
	- "Excel was always meant for people mucking around with a bunch of data for their small company to see what it looked like.”
	- “And then when you need to do something more serious, you build something bespoke that works - there's dozens of other things you could do.”
	- "But you wouldn't use XLS. Nobody would start with that."
- In short: Best practices in computing don’t always make it into the rest of the world. Much of the world still runs on Excel.
- What does this have to do with Python? Well.. Big datasets should use databases and Python. 
- Check out the Talk Python free webcast on moving from Excel to Python: [talkpython.fm/excel-webcast](http://talkpython.fm/excel-webcast)

**Michael #5:** [**locust.io**](https://locust.io/)

- via Prayson Daniel
- locust.io is awesome tool to simulate users hammering your endpoint. Quite handy.
- An open source load testing tool: Define user behavior with Python code, and swarm your system with millions of simultaneous users. 
- Usage: after installing it via pip, you can map your local endpoint `locust --host=http://localhost:5000` and open http://localhost:8089 to access the locust web ui to simulate usage
- Features:
	- **Define user behavior in code**: No need for clunky UIs or bloated XML. Just plain code.
	- **Distributed & scalable:** Locust supports running load tests distributed over multiple machines, and can therefore be used to simulate millions of simultaneous users
	- **Proven & battle tested:** Locust has been used to simulate millions of simultaneous users. Battlelog, the web app for the [Battlefield games](https://www.ea.com/games/battlefield/all-battlefield), is load tested using Locust, so one can really say Locust is Battletested ;).
- Example:
```
    from locust import HttpUser, between, task
    
    class WebsiteUser(HttpUser):
        wait_time = between(5, 15) 
      
        def on_start(self):
            self.client.post("/login", {
                "username": "test_user",
                "password": ""
            })
        
        @task
        def index(self):
            self.client.get("/")
            self.client.get("/static/assets.js")
            
        @task
        def about(self):
            self.client.get("/about/")
```

**Brian #6:** **Fixing Hacktoberfest**

- various sources
- [Hacktoberfest](https://hacktoberfest.digitalocean.com/) is an interesting idea sponsored by Digital Ocean, and other sponsors.
	- Overall, it’s a good idea. Encourage people to contribute by bribing them with a t-shirt and other swag.
- Problem and some solutions outlined well by Anthony Sottile in [what’s (wrong with) hacktoberfest?](https://youtu.be/dzRTR63Lzx8)
	- There’s always been some spam associated with hacktoberfest. 
		- Tiny bizarre PRs, PRs to unmaintained repos, etc.
	- This year has been worse
	- A fairly popular YouTuber posted a video showing people how to get a free t-shirt by doing things like adding “- an awesome project” or expanding “It’s” to “It is” to the readme, then submitting it as “improved docs”.
- Changes:
	- On 10/3, rules changed: [An update on efforts to reduce spam with Hacktoberfest: introducing maintainer opt-in and more](https://hacktoberfest.digitalocean.com/hacktoberfest-update)
	- maintainers can opt-in by adding `hacktoberfest` topic to their repo.
	- No longer have to opt out
	- Should discourage spamming of inactive repos
	- Summary:
```
	PRs count if:
    > Submitted during the month of October AND (
    >   The PR is labelled as hacktoberfest-accepted by a maintainer OR
    >   Submitted in a repo with the hacktoberfest topic AND (
    >     The PR is merged OR
    >     The PR has been approved
    >   )
    > )
```
	
	- The deadline for completions, merging, labeling, and approving is November 1.
	- I applaud DO and whoever else is working on hacktoberfest for reacting quickly to this.

Extras:

Michael:

- PyCascades 2021 will take place on Saturday, February 20th from many locations across the Pacific Northwest and beyond. 
- Call for Proposals 📣 PyCascades has been lucky to give our stage to incredible speakers with wonderful talks over the last three years. We are really looking forward to showcasing our community again next year. Our Call for Proposals (CFP) opens today and closes at the end of the day on Tuesday, November 10th, 2020 Anywhere on Earth.
- Patricio Reyes, a researcher at Barcelona Supercomputing Center ([virtual tour](https://my.matterport.com/show/?m=oj5FSKsTt7o)): 
	- You could also consider talking about [nb_black](https://github.com/dnanhkhoa/nb_black): a simple black formatter for Jupyter and JupyterLab too.
	- There is another project (only for JupyterLab): JupyterLab Code Formatter: [jupyterlab-code-formatter.readthedocs.io](https://jupyterlab-code-formatter.readthedocs.io)

Joke: More Classical Programmer Paintings

- [“Delivering a feature in the time of a codefreeze”](https://classicprogrammerpaintings.com/post/186838680505/delivering-a-feature-in-the-time-of-a)
- [“RHEL sysadmins entering the Docker convention floor”](https://classicprogrammerpaintings.com/post/190532155430/rhel-sysadmins-entering-the-docker-convention)
