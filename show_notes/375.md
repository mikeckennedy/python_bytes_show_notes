# Python Bytes 375

Sponsored by ScoutAPM: [**pythonbytes.fm/scout**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [pycountry](https://github.com/pycountry/pycountry)

- A Python library to access ISO country, subdivision, language, currency and script definitions and their translations.
- pycountry provides the ISO databases for the standards:
    - [639-3](https://en.wikipedia.org/wiki/ISO_639-3) Languages
    - [3166](https://en.wikipedia.org/wiki/ISO_3166) Codes for representation of names of countries and their subdivisions
    - [3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) Countries
    - [3166-3](https://en.wikipedia.org/wiki/ISO_3166-3) Deleted countries
    - [3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) Subdivisions of countries
    - [4217](https://en.wikipedia.org/wiki/ISO_4217) Currencies
    - [15924](https://en.wikipedia.org/wiki/ISO_15924) Scripts

**Brian #2:** [**Does Python have pointers?**](https://nedbatchelder.com/blog/202403/does_python_have_pointers.html)

- Ned Batchelder
- Turns out, this is really the description of “what’s a variable in Python?” that helps to make sense of the “variables as names” model in Python, especially for people coming from languages that use pointers a lot.
- You can use `id()` to find out what a variable points to
- You just can’t do the reverse of access it given an id.
- There’s no “dereference” operator.
- See also [Python Names and Values](https://nedbatchelder.com/text/names1.html), also by Ned
    - Should be required reading/viewing for all Python curriculum.

**Michael #3:** [ingestr](https://bruin-data.github.io/ingestr/)

- ingestr is a command-line application that allows ingesting or copying data from any source into any destination database.
- Works on both MongoDB and Postgres and [many more](https://bruin-data.github.io/ingestr/supported-sources/overview.html). 
- incremental loading: `append`, `merge` or `delete+insert`

**Brian #4:** [**Make your terminal nice**](https://davidism.com/starship-and-fish/)

- David Lord
- David’s switched to [Fish](https://fishshell.com) and [Starship](https://starship.rs)
- I tried switching to Fish several times, and I guess I’m good with zsh.
    - Although I admire the brave comic sans motto: “**Finally, a command line shell for the 90s”**
- But I’m finally ready for Starship, and it takes [almost no time to set up](https://starship.rs/guide/#%F0%9F%9A%80-installation)
- Plus it’s fast. (Has it always been Rust?)

**Extras** 

Brian:

- Doing some groundwork for a SaaS project, using SaaS Pegasus
    - I just talked with Cory from Pegasus for an upcoming PythonTest episode
    - I haven’t decided whether to save up SaaS episodes for one big series, or spread them out.
    - But mostly I’m excited to get my project started.

Michael:

- Excellent video about “[cloud exit](https://youtu.be/a30vFpSaoZg?si=sdsOspRZB6Kg3Tpo)”
- [uv - The Next Evolution in Python Packages](https://talkpython.fm/episodes/show/453/uv-the-next-evolution-in-python-packages)?
- [Python 3.13 a5](https://pythoninsider.blogspot.com/2024/03/python-3130-alpha-5-is-now-available.html)
- [Target’s Open Source Fund](https://tech.target.com/blog/open-source-fund) via Pat Decker

**Joke:** [Anti-social engineer](https://devhumor.com/media/anti-social-engineer)

