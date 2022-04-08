# Python Bytes 278

Sponsored by: [**Microsoft for Startups Founders Hub**](https://pythonbytes.fm/foundershub).

Special guest: [Vuyisile Ndlovu](https://twitter.com/TerraMeijar)

**Brian #1:** [**dunk - a prettier git diff**](https://github.com/darrenburns/dunk)

- Darren Burns 
- Uses Rich
- “⚠️ This project is *very* early stages” - whatever, I like it.
- Recommendation is to use less as a pager for it
    - `git diff | dunk | less -R`

**Michael #2:** [**Is your Python code vulnerable to log injection?**](https://dev.arie.bovenberg.net/blog/is-your-python-code-vulnerable-to-log-injection/)

- via Adam Parkin
- Let’s just appreciate [log4jmemes.com](https://log4jmemes.com) for a moment
- Ok, now we can talk about Python
- We can freak our the logging with line injection

```
    "hello'.\nINFO:__main__:user 'alice' commented: 'I like pineapple pizza"
```

Results in two lines for one statement

```
    INFO:__main__:user 'bob' commented: 'hello'.
    INFO:__main__:user 'alice' commented: 'I like pineapple pizza'.
```

- The safest solution is to simply not log untrusted text. If you need to store it for an audit trail, use a database. 
- Alternatively, [structured logging](https://www.structlog.org/en/stable/) can prevent newline-based attacks.
- Padding a ton? One such case is abusing [padding syntax](https://pyformat.info/#string_pad_align). Consider this message: 
- `*"%(user)999999999s"*`
- This will pad the `user` with almost a gigabyte of whitespace.
- Mitigation: To eliminate these risks, you should always let logging handle string formatting.
- See this discussion: [Safer logging methods for f-strings and new-style formatting](https://discuss.python.org/t/safer-logging-methods-for-f-strings-and-new-style-formatting/13802)

**Vuyisile #3:** [**Building multi tenant applications with Django**](https://books.agiliq.com/projects/django-multi-tenant/en/latest/index.html)

- Free book by Agiliq, covers different approaches to building Software as a service applications in Python/Django.
- Covers four approaches to multi tenancy, namely:
    1. Shared database with shared schema
    2. Shared database with isolated schema
    3. Isolated database with a shared app server
    4. Completely isolated tenants using Docker

**Brian #4:** [**Should you pre-allocate lists in Python?**](https://rednafi.github.io/reflections/pre-allocated-lists-in-python.html)

- Redowan Delowar
- Discussion of 3 ways to build up a list
    - Start empty and append: `l=[]; l.append(1); …`
    - Pre-allocate: `l = [None] * 10_000; …`
    - List comprehension: `l = [i for i in range(10_000)]`
- Interesting discussion and results
    - The times (filling the list with the index):
        - append: 499 µs ± 1.23 µs
        - pre-allocate: 321 µs ± 71.1
        - comprehension: 225 µs ± 711
    - Python lists dynamically allocate extra memory when they run out, and it’s pretty fast at doing this.
    - Pre-allocation can save a little time.
    - Conclusion: use comprehensions when you can, otherwise, don’t sweat it unless you really need to shave off as much time as possible
- Of note: this was just measuring time, no discussion of memory usage.

**Michael #5:** [**mockaroo**](https://mockaroo.com) and [**tonic**](http://talkpython.fm/tonic)

- Do you need to generate fake data?
- Mockaroo let’s you generate realistic data based data types (car registrations, credit cards, dates, etc)
- Tonic takes your actual production data and reworks it into test data (possibly striping out PII)

**Vuyisile #6:**

- [Brachiograph](https://www.brachiograph.art/) —the cheapest, simplest possible Python powered pen plotter by Daniele Procida
- Low tech Raspberry Pi project that can be built for < $50 using common household objects like a clothes peg ice cream stick

**Extras** 

Brian:

- [April 8 new date for Python Issues migrating to GH](https://discuss.python.org/t/github-issues-migration-status-update/14573)

Michael:

- [ngrok](https://ngrok.com) has a [detailed web explorer](https://ngrok.com/docs#getting-started-inspect)

Vuyisile: 

- [Thunder Client](https://www.thunderclient.com/)  : VS Code extension, Lightweight client for testing REST APIs
    Postman alternative

**Joke:** [**Linux world in tatters**](https://www.reddit.com/r/ProgrammerHumor/comments/tqtuys/the_linux_world_is_in_tatters_now/)

Related: Origin of the joke - [**Lapsus$ claims to leak 90% of Microsoft Bing's source code**](https://www.windowscentral.com/lapsus-claims-leak-90-microsoft-bings-source-code)

