# Python Bytes 292

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:** [**rich-codex**](https://ewels.github.io/rich-codex/)

- by Phil Ewels
- [suggested by Will McGugan](https://twitter.com/willmcgugan/status/1545052601649020928?s=20&t=AQxTIX8SCz95bN2_ZnWqDg)
- “A GitHub Action / command-line tool which generates screen grab images of a terminal window, containing *command outputs* or *code snippets*.”
- Generate images from commands embedded in markdown files, like README.md, for example.
    - Searches through markdown files for stuff like:
    !\[`cat cat.txt | lolcat -S 1`\](img/cat.svg)
    - then runs the command, and generates the image.
- Can be done within a GitHub action
- Can also send code snippets or json to rich-cli, then generate an image.
- You can also have commands in a config file, 
- Very easy to use, makes very professional looking images for documentation, that’s always up to date.

**Michael #2:** [**Pydastic**](https://twitter.com/iamramiawar/status/1523370586629877760)

- via Roman Right, by [Rami Awar](https://twitter.com/iamramiawar)
- Pydastic is an elasticsearch python ORM based on Pydantic.
- Core Features
    - Simple CRUD operations supported
    - Sessions for simplifying bulk operations (a la SQLAlchemy)
    - Dynamic index support when committing operations
- More on [**Elasticsearch here**](https://www.elastic.co/elasticsearch/)

**Brian #3:** [**3 Things to Know Before Building with PyScript**](https://towardsdatascience.com/3-things-you-must-know-before-building-with-pyscript-245a0a82f2c3)

- by Braden Riggs
- Package indentation matters
- Local file access is possible.
```
        <py-env>
    - numpy
    - pandas
    - paths:
        - /views.csv
        </py-env>
```

- - DOM manipulation has interesting conventions
    1. For buttons, you can include *pys-onClick=”your_function”* parameter to trigger python functions when clicked.
    2. For retrieving user input from within the *<py-script>* tag *document.getElementById(‘input_obj_id’).value* can retrieve the input value.
    3. And Finally *pyscript.write(“output_obj_id”, data)* can write output to a tag from within the *<py-script>* tag.

**Michael #4:** [**disnake**](https://twitter.com/datacascadia/status/1542043036586082304)

- via Sean Koenig
- disnake is a modern, easy to use, feature-rich, and async-ready API wrapper for Discord.
- **Features:**
    - Modern Pythonic API using `async`/`await` syntax
    - Sane rate limit handling that prevents 429 errors
    - Command extension to aid with bot creation
    - Easy to use with an object oriented design
    - Optimized for both speed and memory
    - [**Quickstart**](https://docs.disnake.dev/en/latest/quickstart.html)
    - [**Commands API**](https://docs.disnake.dev/en/latest/ext/commands/commands.html)

**Extras** 

Michael:

- [**Scholarships**](https://forms.gle/ZXHJCH1LuVdr6UUr8) for upcoming FastAPI + MongoDB live course
- [**Humble Bundle for Python 2022**](https://www.humblebundle.com/operation-python-2022-software)

**Joke:**  [**Better than a wage increase**](https://twitter.com/PR0GRAMMERHUM0R/status/1542976365485596672)
