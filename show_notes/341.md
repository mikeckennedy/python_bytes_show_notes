# Python Bytes 341

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Pydantic roadmap**](https://pydantic.dev/roadmap/)

- via Mario Munoz
- Back in February [Samuel] [announced](https://pydantic.dev/announcement/) Pydantic Inc., but I didn't explain what services we were building.
- The problem is that even with Pydantic in your corner, working with data when it leaves Python often still sucks.
- We want to build a data platform to make working with data quick, easy, and enjoyable — where developer experience is our north star.
- There are five key components to the Pydantic Data Platform that we're thinking of building.
    1. **Python Analytics/Observability** — a logging and metrics platform with tight Python and Pydantic integration, designed to make the data flowing through your application more readily usable for both engineering and business analytics. [More info...](https://pydantic.dev/roadmap/#3-1-analyticsobservability-for-python)
    2. **Data Gateway for object stores** — Add validation, transformation and cataloguing in front of object stores like S3, with a schema defined in Pydantic models then validated by our Rust service. [More info...](https://pydantic.dev/roadmap/#3-2-data-gateway-for-object-stores)
    3. **Data Gateway for data warehouses** — the same service as above, but integrated with your existing data warehouse. [More info...](https://pydantic.dev/roadmap/#3-3-data-gateway-for-data-warehouses)
    4. **Schema Catalog** — for many, Pydantic already holds the highest fidelity representation of their data schemas. Our Schema Catalog will take this to the next level, serving as an organization-wide single source of truth for those schemas, tracking their changes, and integrating with our other tools and your wider platform. [More info...](https://pydantic.dev/roadmap/#3-4-schema-catalog)
    5. **Dashboards and UI powered by Pydantic models** — a managed platform to deploy and control dashboards, auxiliary apps and internal tools where everything from UI components (like forms and tables) to database schema would be defined in Python using Pydantic models. [More info...](https://pydantic.dev/roadmap/#3-5-dashboards-and-ui-powered-by-pydantic-models)
1. [**Tell them what you think**](https://forms.gle/cMbLXNUxdgG2DeSv6) with their survey

**Brian #2:** [**The Right Way to Run Shell Commands From Python**](https://martinheinz.dev/blog/98)

- Martin Heinz
- Should have a tagline of “especially if you’re on Mac or Linux”.
- Includes discussion of
    - Python native tools - recommended
    - a few os module functions - but otherwise avoid relying too much on os.
    - subprocess.run() - stick with run() if you can.
    - [sh third party package](https://amoffat.github.io/sh/) - should be second choice if on Linux or Mac

**Michael #3:** [**US: Yep, We're Buying Your Data, Including Your Embarrassing Secrets**](https://www.pcmag.com/news/us-yes-were-buying-data-on-us-citizens-including-their-embarrassing-secrets)

- Digital information can be purchased from commercial data brokers and 'deanonymized' to ID the person it's tied to, including US citizens, the Office of the Director of National Intelligence says.
- The Office of the Director of National Intelligence (ODNI) on Friday declassified(Opens in a new window) a report from January 2022 that outlines the US government’s approach to using Commercially Available Information (CAI), which can come from data brokers working in the internet ad and analytics industries. 
- The purchased information includes details from users' smartphones and social media accounts.
- To all the “please disable your ad blockers” companies out there
    - 1) It’s not just about supporting your website
    - 2) Ad blockers are not just avoiding ads.
    - 3) It’s not even necessary (our ads are not blocked on the podcast or the website)
- Consider **browser != Chrome** and/or [**nextdns.io**](https://nextdns.io/?from=a743zhpr) for your whole network

**Brian #4:** [**Pro-Tip – pytest fixtures are magic!**](https://www.revsys.com/tidbits/pytest-fixtures-are-magic)

- Frank Wiles
- “The magic of pytest fixtures is how they are injected into your tests for you to use and their composability. When done well, writing tests is considerably easier and actually fun.”
- Setup code is often the biggest headache of test writing. pytest fixtures help solve the setup problem.
- Fixtures 
    - are used by just including them in a tests parameter list
    - can build on top of each other
    - can be used in any test in the project, if you put it in a central conftest.py
    - can return all kinds of things: static data, instantiated objects, callables to make other things, 
- Frank includes an interesting way to organize fixtures such that they are defined in local test directories but usable across a project, under “Organizing Your Fixtures”.
- Plugins with fixtures: A shoutout to [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and a Revsys plugin called [django-test-plus](https://github.com/revsys/django-test-plus).
- Built-in fixtures. See also `tmp_path`.
- autouse
    - One bit of incorrect info: `autouse` doesn’t work like that. The value of `global_thing` cannot be grabbed unless you list it in the parameter list. It will run before every function (since it’s `scope=``"``function``"`  by default), but you gotta list it to get the value.
    - To be fair, it’s really hard to come up with good `autouse` examples. Partly because there are so few good reasons to use `autouse`.

**Extras** 

Brian:

- [**Porting Python projects to Rust**](https://www.jelmer.uk/port-py-to-rust.html)
- [**International Obfuscated Python Code Competition**](https://pyobfusc.com/)

Michael:

- Remember the AMA ([**submit your question**](https://pythonbytes.fm/ama2023)). “Scheduled” on July 11th at 11am.

**Joke:** [**Marked as duplicate**](https://www.reddit.com/r/programminghumor/comments/13nls2h/every_time/)

