# Python Bytes 324

Sponsored by [**Compiler Podcast from Red Hat**](https://pythonbytes.fm/compiler).
[](https://pythonbytes.fm/compiler)
**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)
- Special guest, Erin Mullaney: [**@erinrachel@fosstodon.org**](https://fosstodon.org/@erinrachel) 

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Use TOML for `.env` files?**](https://snarky.ca/use-toml-for-env-files/)

- Brett Cannon
- .env files are used to store default settings that can be overridden by environmental variables.
- Possibly brought on by twelve-factor app design.
- Supported by  [python-dotenv](https://pypi.org/project/python-dotenv/), which is also used by pydantic, pipenv, and others.
- One issue is that it’s not a defined standard.
    - from python-dotenv docs “The format is not formally specified and still improves over time. That being said, `.env` files should mostly look like Bash files.”
- Adafruit decided that an upcoming CircuitPython will use TOML as the format for settings.toml files, which are to be used mostly how .env files are being used.
- Brett notices this may fix things for Python for VS Code, and other people as well.
- So… Is this a good idea? I think so.


**Michael #2:**  [**Pydantic gets serious funding**](https://techcrunch.com/2023/02/16/sequoia-backs-open-source-data-validation-framework-pydantic-to-commercialize-with-cloud-services/?guccounter=1)

- via Mark Little (was on [episode 285](https://pythonbytes.fm/episodes/show/285/where-we-talk-about-uis-and-python))
- Sequoia backs open source data-validation framework Pydantic to commercialize with cloud services.
- Pydantic Services Inc. emerges from stealth today with $4.7 million in seed funding.
- Pydantic’s new commercial entity will incorporate a swath of new tools and services that are both “powered-by and inspired-by the Pydantic library”
- Pydantic will start with an initial team of six, with the first three engineers based in Montana, Chicago and Berlin.
- “With $4.7 million in the bank, Colvin said that they’re continuing to rewrite parts of Pydantic in [Rust](https://techcrunch.com/2021/02/08/the-rust-programming-language-finds-a-new-home-in-a-non-profit-foundation/), with a view toward making it more efficient via a ten-fold performance improvement.”

**Erin** **#3:** [**JSON Fields for performance (Denormalization)**](https://www.youtube.com/watch?v=Y7Z1vwbG7rY)
[](https://www.youtube.com/watch?v=Y7Z1vwbG7rY)
- David Stokes
- Using JSON fields when you design your databases is a good way to improve database query performance.

**Brian #4:** [**f-strings with pandas**](https://www.dataschool.io/how-to-use-f-strings-with-pandas/) **and** [**Jupyter keyboard shortcuts**](https://www.dataschool.io/jupyter-notebook-keyboard-shortcuts/)

- Kevin Markham
- After a couple year break from blogging, friend of the show Kevin Markham has a couple great, short, useful posts.
- [How to use Python's f-strings with pandas](https://www.dataschool.io/how-to-use-f-strings-with-pandas/)
    - My favorite bit is the part about using f-strings for dictionary keys
- [Fly through Jupyter with keyboard shortcuts 🚀](https://www.dataschool.io/jupyter-notebook-keyboard-shortcuts/)
    - I’m a sucker for a rocket emoji
    - Not an overwhelming list. Just the essentials for even the casual Jupyter user.
    - Examples
        - `Esc` and `Enter` for command mode/edit mode
        - `a` and `b` for creating a new cell above or below current cell.
        - `m`  and `y` for changing the cell type to Markdown or code.
        - `Shift+m` to merge cells
        - so many more
- 

**Michael #5:** [**BioGPT**](https://github.com/microsoft/BioGPT)

- “GPT” for biomedical text generation and mining 
- As motivation, let’s see what [ChatGPT can do with arrow anti-patterns in Python](https://medium.com/lemon-code/guard-clauses-3bc0cd96a2d3).
- Smaller models and “Large” models
- Used [via an API rather than chat style](http://for biomedical text generation and mining).
- BioGPT has also been integrated into the Hugging Face `transformers` library too
- [Play with it here](https://huggingface.co/spaces/katielink/biogpt-large-demo).

**Erin** **#6:** **Code Mentorship and Communicating with Newer Devs** 

- Sheena O’Connell 
- Sheena O’Connell [gave a talk at DjangoCon](https://www.youtube.com/watch?v=5-gybkYB3lM) about her work at Umuzi, training unemployed young people in underserved communities in Africa and also was on [Django Chat Podcast](https://djangochat.com/episodes/django-lms-sheena-oconnell). 
- Dmitriy Chukhin
- Caktus Group is trying a [new mentorship program](https://www.caktusgroup.com/blog/2022/12/07/new-mentorship-program/) for folks who don’t have the necessary training. 

**Extras** 

Brian:

- 

Michael:

- News is, these are no loner news: [Security Researchers Uncover 700+ Malicious Open-Source Packages in npm and PyPI](https://news.itsfoss.com/malicious-packages-npm-and-pypi/)
- [Git security vulnerabilities announced, again](https://github.blog/2023-02-14-git-security-vulnerabilities-announced-3/)
- git ignores
    - https://github.com/github/gitignore
    - https://gitignore.io

Erin: 

- [DjangoCon is in October in Durham, NC](https://2023.djangocon.us/) this year (Oct 15-20)

**Joke:** 

- [Remember your pointers?](https://www.reddit.com/r/ProgrammerHumor/comments/110uh08/my_c_code_isnt_working_guys/)

