# Python Bytes 356

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Psycopg 3**](https://www.psycopg.org/psycopg3/)

- Psycopg folks recommend starting with 3 for new projects
- 2 is still actively maintained, but no new features are planned
    - recommend staying with 2 for legacy projects
- [Psycopg 3 project](https://www.psycopg.org/psycopg3/)
- [2 vs 3 feature comparison](https://www.psycopg.org/features/)
- A few Psycopg 3 highlights
    - native asyncio support
    - native support for more Python types (such as Enums) and PostgreSQL types (such as multirange)
    - Default server-side parameters binding
    - Allows binary parameters and query results (and text, of course)
    - Pipeline/batch mode support
    - Static typing support

**Michael #2:** [**dacite**](https://github.com/konradhalas/dacite)

- via Raymond Peck
- Simple creation of data classes from dictionaries
- Dacite supports following features:
    - nested structures
    - (basic) types checking
    - optional fields (i.e. `typing.Optional`)
    - unions
    - forward references
    - collections
    - custom type hooks
- It's important to mention that `dacite` is not a data validation library.
- [Type hooks](https://github.com/konradhalas/dacite#type-hooks) are interesting too.


**Brian #3:** [**RIP: Fast, barebones pip implementation in Rust**](https://github.com/prefix-dev/rip)

- list of current and planned features of `RIP`, the biggest are listed below:
    - Downloading and aggressive caching of PyPI metadata. (done)
    - Resolving of PyPI packages using [Resolvo](https://github.com/mamba-org/resolvo). (done)
    - Installation of wheel files (planned)
    - Support sdist files (planned)
- new project, just a couple weeks old. … “We would love to have you contribute!”

**Michael #4:** [**Flaky Tests follow up**](https://www.marwansarieddine.com/posts/flaky_tests)

- by Marwan Sarieddine
- I was inspired by the Talk Python podcast on "Taming flaky tests" with Gregory Kapfhammer and Owain Parry so I wrote up an article on my blog titled "How not to footgun yourself when writing tests - a showcase of flaky tests”


**Extras** 

Brian:

- Just wrapping up some personal projects, which means…
    - Python People episodes soon
    - Python Test episodes soon (but later)
    - More course chapters coming

Michael:

- [**PyBay 2023**](https://pybay.com) was fun
- Switched to [**Spark Mail**](https://sparkmailapp.com), recommended
- Dust (what science fiction story telling should be), try:
    - [**FTL**](https://www.youtube.com/watch?v=t8LD0iUYv80)
    - [**Oceanus**](https://www.youtube.com/watch?v=V6_9YnTDR-s)

**Joke:**

- There are more hydrogen atoms in a single molecule of water than there are stars in the entire Solar System. - [mas.to/@SmudgeTheInsultCat/111174610011921264](https://mas.to/@SmudgeTheInsultCat/111174610011921264)
- [**The Big Rewrite**](https://www.youtube.com/watch?v=xCGu5Z_vaps)

