# Python Bytes 368

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Syntax Error #11: Debugging Python**](https://www.syntaxerror.tech/syntax-error-11-debugging-python/)

- Juhis
- Issue 11 of a fun debugging newsletter from Juhis
- Debugging advice
    - mindeset
        - take a break
        - adopt a process
        - talk to a duck
    - tools & techniques
        - print
        - snoop
        - debuggers
        - Django debug toolbar & Kolo for VS Code

**Michael #2:**  [umami](https://umami.is) and [umami-analytics](https://pypi.org/project/umami-analytics/)

-  Umami makes it easy to collect, analyze, and understand your web data — while maintaining **visitor privacy** and **data ownership**.
-  [umami-analytics](https://pypi.org/project/umami-analytics/) is a client for privacy-preserving, open source [Umami analytics platform](https://umami.is/) based on `httpx` and `pydantic`.
-  Core features
-  ➕ **Add a custom event** to your Umami analytics dashboard.
-  🌐 List all websites with details that you have registered at Umami.
-  🔀 Both **sync** and **async** programming models.
-  ⚒️ **Structured data with Pydantic** models for API responses.
-  👩‍💻 **Login / authenticate** for either a self-hosted or SaaS hosted instance of Umami.
-  🥇Set a **default website** for a **simplified API** going forward.


**Brian #3:** [**pytest-suite-timeout**](https://github.com/okken/pytest-suite-timeout)

- While recording [Python Test 213 : Repeating Tests](https://podcast.pythontest.com/episodes/213-repeating-tests)
    - I noted that pytest-repeat doesn’t have a timeout, but pytest-flakefinder does.
    - And perhaps I should add a timeout to pytest-repeat
- But also, maybe there’s other places I’d like a timeout, not just with repeat, but often with other parametrizations and even parametrize matrices. 
- So, [**pytest-suite-timeout**](https://github.com/okken/pytest-suite-timeout) is born
- But [Why not pytest-timeout? asks Mike Felder](https://hachyderm.io/@miketheman/111799555975904630)
    - timeout is only timeouts per test, and it isn’t always graceful
    - suite-timeout is for the full suite, and only times out between tests.
    - so, you could use both

**Michael #4:** [Listmonk](https://listmonk.app) and [(py) listmonk](https://pypi.org/project/listmonk/)

- [Listmonk](https://listmonk.app)
    - Self-hosted newsletter and mailing list manager (think mailchimp)
    -  Built on Go and Vue
    - Backed by a company charing for this service as SaaS
    - Still requires a mail infrastructure backend (I’m using [Sendgrid](https://sendgrid.com))
-  [listmonk](https://pypi.org/project/listmonk/) (on PyPI)
    - API Client for Python
    - Created by Yours Truly
    - I tried 4 other options first, they were all bad in their own way.
    - Features:
    - ➕**Add a subscriber** to your subscribed users.
    - 🙎 Get **subscriber details** by email, ID, UUID, and more.
    - 📝 **Modify subscriber details** (including custom attribute collection).
    - 🔍 **Search** your users based on app and custom attributes.
    - 🏥 Check the **health and connectivity** of your instance.
    - 👥 Retrieve your **segmentation lists**, list details, and subscribers.
    - 🙅 Unsubscribe and block users who don't want to be contacted further.
    - 💥 Completely delete a subscriber from your instance.
    - 📧 Send transactional email with template data (e.g. password reset emails).
- These pair well in my new [docker](https://www.docker.com) cluster infrastructure
    - Calls to the API from a client app (e.g. [Talk Python Training](https://training.talkpython.fm)) are basically loopback on the local docker bridge network.

**Extras** 


Michael:

- Every github repo that has “releases” has a releases RSS feed, e.g. [Umami](https://github.com/umami-software/umami/releases.atom)
- [Kolo Django + VS Code](https://kolo.app)
- [Warp Terminal](https://www.warp.dev/linux-terminal) on linux
- [bpytop and btop](https://fosstodon.org/@mkennedy/111787125592445700) - live server monitoring

**Joke:** [The cloud, visualized](https://infosec.exchange/@jbhall56/111178034352233910)

