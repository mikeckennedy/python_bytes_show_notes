# Python Bytes 319

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/stream/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Secure maintainer workflow**](https://nedbatchelder.com/blog/202211/secure_maintainer_workflow.html)

- by [**Ned Batchelder**](https://nedbatchelder.com/)
- We are the magicians, but also the gatekeepers for our users
- Terminal sessions with implicit access to credentials
    - first is unlikely: a bad guy gets onto my computer and uses the credentials to cause havoc
    - second way is a more serious concern: I could unknowingly run evil or buggy code that uses my credentials in bad ways.
- Mitigations
    - **1Password:** where possible, I store credentials in [1Password](https://1password.com/), and use tooling to get them into environment variables.
        - Side bar: Do not use lastpass, see end segment
        - I can have the credentials in the environment for just long enough to use them. This works well for things like PyPI credentials, which are used rarely and could cause significant damage.
    - **Docker:** To really isolate unknown code, I use a Docker container.

**Brian #2:** **Tools for parsing HTML and JSON**

- Learned these from [A Year of Writing about Web Scraping in Review](https://scrapecrow.com/year-of-writing-in-review.html)
- [Parsel](https://parsel.readthedocs.io/en/latest/index.html) - extract and remove data from HTML using XPath and CSS selectors
- [jmespath](https://pypi.org/project/jmespath/) - “James Path” - declaratively specify how to extract elements from a JSON document


**Michael #3:** [**git-sizer**](https://github.com/github/git-sizer)

- Compute various size metrics for a Git repository, flagging those that might cause problems.
- Tip, partial clone: git clone **--filter=blob:none** URL
```
    # Stats for training.talkpython.fm
    # Full: git clone repo
    Receiving objects: 100% (118820/118820), 514.31 MiB | 28.83 MiB/s, done.
    Resolving deltas: 100% (71763/71763), done.
    Updating files: 100% (10792/10792), done.
    1.01 GB on disk
    
    # Partial: git clone --filter=blob:none repo
    Receiving objects: 100% (10120/10120), 220.25 MiB | 24.92 MiB/s, done.
    Resolving deltas: 100% (1454/1454), done.
    Updating files: 100% (10792/10792), done.
    694.4 MB on disk
```

- [Partial clone](https://github.com/git/git/blob/master/Documentation/technical/partial-clone.txt) is a performance optimization that “allows Git to function without having a complete copy of the repository. The goal of this work is to allow Git better handle extremely large repositories.” When changing branches, Git may download more missing files.
- Not the same as shallow clones or sparse checkouts
    - Consider shallow clones for CI/CD/deployment
    - Sparse checkouts for a slice of a monorepo

**Brian #4:** [**Dataclasses without type annotations**](https://death.andgravity.com/dataclasses)

- Probably file this under “don’t try this at home”. 
    - Or maybe “try this at home, but not at work”.
    - Or just “that Brian fella is a bad influence”.
        - What! It’s not me. It’s Adrian, the dude that wrote the article.
- Unless you’re using a type checker, for dataclasses, “… use any type you want. If you're not using a static type checker, no one is going to care what type you use.”


    @dataclass
    class Literally:
        anything: ("can go", "in here")
        as_long_as: lambda: "it can be evaluated"
        # Now, I've noticed a tendency for this program to get rather silly.
        hell: with_("from __future__ import annotations")
        it_s: not even.evaluated
        it: just.has(to=be) * syntactically[valid]
        # Right! Stop that! It's SILLY!

**Extras** 

Michael:

- [LastPass story](https://www.theverge.com/2022/12/22/23523322/lastpass-data-breach-cloud-encrypted-password-vault-hackers) just keeps getting worse
    - We will see problems in supply chains because of this too
    - A whole 2 hour discussion diving into what I touched on: [twit.tv/shows/security-now](https://twit.tv/shows/security-now/episodes/905?autostart=false)
- Got your [new mac mini](https://www.apple.com/mac-mini/) yet? Or [MacBook Pro](https://www.apple.com/macbook-pro-14-and-16/)?

**Joke:** [Developer/maker, what’s my purpose?](https://www.reddit.com/r/ProgrammerHumor/comments/107xuhu/no_better_place_to_put_it/)

