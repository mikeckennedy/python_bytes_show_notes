# Python Bytes 336

Sponsored by [**InfluxDB**](https://pythonbytes.fm/influxdata) from Influxdata.

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Python's Missing Batteries: Essential Libraries You're Missing Out On**](https://martinheinz.dev/blog/96)
[](https://martinheinz.dev/blog/96)
- Martin Heinz
- Fun collection of a bunch of libraries you may not know about (or forgot about), with code examples.
- Utilities
    - boltons : iterate through json and dates, quickly grab data out of nested structures, and convert nested data with `jsonutils`, `timeutils`, and `iterutils`
    - sh : conveniently call shell funcitons
- Data Validation
    - validators : validate email addresses, credit cars, IP addresses, and more.
    - the fuzz : fuzzy string comparisons
- Debugging
    - stackprinter : nice stack traces with exception messages higlighted
- Testing
    - freezegun : stop time, change dates, …
    - dirty_equals : comparing things that are kinda equal
- CLI
    - tqdm : add a progress bar to command line apps

**Michael #2:** [**awesome-polars**](https://github.com/ddotta/awesome-polars)

- A curated list of Polars talks, tools, examples & articles.
- Mostly articles and tutorials however.  

**Brian #3:**  [**Running Headless Selenium in Python (2023)**](https://coderslegacy.com/running-headless-selenium-in-python-2023)

- Siddiqi
- First off, if you are doing automated testing with Selenium, I hope you already know about headless. It’s awesome and speeds up testing.
- Next, there’s changes to how you code headless, as of Selenium 4.8.0 (Jan. 2023).
- Old:
    - ``options.headless` `**=**` `True``
- New:
    - ``options.add_argument('--headless=new')`` for Chrome
    - ``options.add_argument('--headless')`` for Firefox
- Reasons: [Read Headless is Going Away!](https://www.selenium.dev/blog/2023/headless-is-going-away/) post on Selenium blog.
    - Subtitle: “Now that we got your attention, headless is not actually going away, just the convenience method to set it in Selenium”

**Michael #4:** [**Gracy**](https://github.com/guilatrova/gracy)

- Gracy helps you handle failures, logging, retries, throttling, and tracking for all your HTTP interactions. 
- Has support for
  - Parsing per status code
  - Throttling
  - Retries
  - Custom validation
  - Record/replay for testing

- A bit non-pythonic but perhaps inspriation for some out there

**Extras** 

Michael:

- [**Mobile apps are finally out**](https://mkennedy.codes/posts/mobile-apps-at-talk-python-python-flutter/)
    - Take the [**git course**](https://training.talkpython.fm/courses/up-and-running-with-git-a-pragmatic-ui-based-introduction) for free for a limited time.
    - [**Michael's blog post**](https://mkennedy.codes/posts/mobile-apps-at-talk-python-python-flutter/) announcing the apps

**Joke:** [**It’s practice**](https://www.reddit.com/r/programminghumor/comments/13clz5m/its_practice/)

