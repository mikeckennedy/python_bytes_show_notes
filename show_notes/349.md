# Python Bytes 349
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Omnivore app**](https://omnivore.app)

- Omnivore is the free, open source, read-it-later app for serious readers.
- Distraction free. Privacy focused. Open source. Designed for knowledge workers and lifelong learners.
- Save articles, newsletters, and documents and read them later — focused and distraction free. 
- Add notes and highlights. 
- Organize your reading list the way you want and sync it across all your devices.
- Syncs with popular Personal Knowledge Management systems including Logseq and Obsidian
- Wait, what’s [**Logseq**](https://logseq.com)? :)
    - A privacy-first, open-source platform for knowledge management and collaboration.
    - Kinda like Notion?

**Brian #2:** [**Djangonaut.space**](https://djangonaut.space)

- “Where contributors launch”
- This is a group mentoring program where individuals will work self-paced in a semi-structured learning environment over the course of three months.
- Djangonauts are members of the community who wish to level up their current Django code contributions and potentially take on leadership roles in Django in the future.

**Michael #3:** [**Server-side hot reload**](https://github.com/mikeckennedy/server-hot-reload)

- Thanks to [**Alex Riviere**](https://fosstodon.org/@fimion@notacult.social) for some improvements
- Bill Mill suggests websockets and Adam Johnson points he built something like this for Django  (sorta) with [**django-browser-reload**](https://github.com/adamchainz/django-browser-reload)
- To make it work just:
- Include this script in your web projects for dev-time auto reloading of web browser when any change is detected in content. 
- Works across all web technologies, built out on a FastAPI / Tailwind project.
- General workflow looks like:
    1. Edit the source CSS file
    2. Tailwind watcher generates a built CSS file
    3. Built CSS file is included the Python web HTML template
    4. Template appends a hash ID for the state of the CSS file
    5. Changes to the source CSS thus trigger a change in the final ID
    6. New ID means the page contents change and the script does a reload
- Even works for static resources if you put a “version” indicator on them:
    <link href="/static/site.css?v=670022" rel="stylesheet">
    <img src="/static/img/logo.webp?v=a4c931" />

**Brian #4:** [**Python in Excel**](https://www.anaconda.com/blog/announcing-python-in-excel-next-level-data-analysis-for-all)

- Anaconda working with Microsoft to have Python built in to Excel.
- “*Python in Excel is currently in preview and is subject to change based on feedback. To use this feature, join the* [*M*](https://insider.microsoft365.com/en-us/join/windows)*icrosoft 365 Insider Program and choose the* ***Beta Channel*** *Insider level.”* 
    - from Microsoft Support article: Getting started with Python in Excel


**Extras** 

Brian:

- Working on videos for “Ch3 : pytest Fixtures” for the [Python Testing with pytest Course Bundle](https://testandcode.teachable.com)
    - Adding some drawings and some more bonus videos.
    - Thanks to everyone who’s signed up already. 
    - I’ve pushed the 20% discount out till the end of August.
- I also finally listed it on [pythontest.com/courses](https://pythontest.com/courses/)
- Also lots of new interviews for [pythonpeople.fm](https://pythonpeople.fm/), and I’m expecting at least one new episode of [testandcode.com](https://testandcode.com) this week.
    - It’s going to be a busy week.

Michael:

- PyCon Sweden [**CFP is open**](https://www.pycon.se)
- [**Be on Talk Python around Mobile Apps**](https://forms.gle/7bgENZXmsvzJXyVEA)?

**Joke:** 

- [**The Password Game**](https://neal.fun/password-game/)
- [**KennyLog-in.com**](https://www.kennylog-in.com/) - secure password generator

