# Python Bytes 367
Sponsored by **Bright Data** : [**pythonbytes.fm/brightdata**](https://pythonbytes.fm/brightdata)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Leaving the cloud**](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb)

- Also see [Five values guiding our cloud exit](https://world.hey.com/dhh/five-values-guiding-our-cloud-exit-638add47)
    - We value independence above all else.
    - We serve the internet. 
    - We spend our money wisely. 
    - We lead the way. 
    - We seek adventure.
- And [We stand to save $7m over five years from our cloud exit](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa)
- Slice our new monster 192-thread Dell R7625s into isolated VMs
- Which added a combined [4,000 vCPUs with 7,680 GB of RAM and 384TB of NVMe storage](https://world.hey.com/dhh/the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966) to our server capacity
- They [created Kamal](https://kamal-deploy.org) — Deploy web apps anywhere
- A lot of these ideas have changed how I run the infrastructure at Talk Python and for Python Bytes. 

**Brian #2:** [**PEP 723 - Inline script metadata**](https://peps.python.org/pep-0723/)

- Author: Ofek Lev
- This PEP specifies a metadata format that can be embedded in single-file Python scripts to assist launchers, IDEs and other external tools which may need to interact with such scripts.
- Example:

```
    # /// script
    # requires-python = ">=3.11"
    # dependencies = [
    #   "requests<3",
    #   "rich",
    # ]
    # ///
    
    import requests
    from rich.pretty import pprint
    
    resp = requests.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    pprint([(k, v["title"]) for k, v in data.items()][:10])

```


**Michael #3:** [**Flet for Android**](https://flet.dev/blog/flet-for-android)

- via Balázs
- [Remember Flet](https://talkpython.fm/episodes/show/378/flet-flutter-apps-in-python)?
- Here’s a [code sample](https://flet.dev/docs/guides/python/drag-and-drop) (scroll down a bit).
- It’s amazing but has been basically impossible to deploy. 
- Now we have Android.
- Here’s a good [YouTube video](https://www.youtube.com/watch?v=Hj09tFCdjSw) showing the build process for APKs.

**Brian #4:** [**harlequin: The SQL IDE for Your Terminal.**](https://github.com/tconbeer/harlequin)

- Ted Conbeer & other contributors
- Works with DuckDB and SQLite
- Speaking of SQLite
    - [Jeff Triplett and warnings of using Docker and SQLite in production](https://mastodon.social/@webology/111766195410833730)
    - [Anže’s post](https://blog.pecar.me/)
    - and and article: [Django, SQLite, and the Database is Locked Error](https://blog.pecar.me/django-sqlite-dblock)

**Extras** 

**Brian**:

- Recent [Python People](https://pythonpeople.fm) episodes
    -  Will Vincent
    - Julian Sequeira
    - Pamela Fox

**Michael**:

- PageFind and [how I’m using it](https://fosstodon.org/@mkennedy/111637520985150159)
- When "[Everything" Becomes Too Much](https://socket.dev/blog/when-everything-becomes-too-much?utm_source=tldrnewsletter): The npm Package Chaos of 2024
- Essay: [Unsolicited Advice for Mozilla and Firefox](https://mkennedy.codes/posts/michael-kennedys-unsolicited-advice-for-mozilla-and-firefox/)
- [SciPy 2024 is coming to Washington](https://fosstodon.org/@matthewfeickert/111763520503201675) 

**Joke:** Careful with that [bike lock combination code](https://trello.com/1/cards/655ef44fcc1657159ad4102c/attachments/655ef452b9b27b86253285c2/download/1700711828998blob.jpg)

