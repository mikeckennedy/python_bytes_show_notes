# Python Bytes 298

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Brian #1:** [**Uncommon Uses of Python in Commonly Used Libraries**](https://eugeneyan.com/writing/uncommon-python/)
[](https://eugeneyan.com/writing/uncommon-python/)
- by Eugene Yan
- Specifically, [Using relative imports](https://eugeneyan.com/writing/uncommon-python/#using-relative-imports-almost-all-the-time)
- Example from sklearn’s `base.py`
    from .utils.validation import check_X_y
    from .utils.validation import check_array
- “Relative imports ensure we search the *current* package (and import from it) before searching the rest of the `PYTHONPATH`. “
- For relative imports, we have to use the `from .something import thing` form. 
- We cannot use `import .something` since later on in the code `.something` isn’t valid.
- There’s a [good discussion of relative imports in pep 328](https://peps.python.org/pep-0328/#guido-s-decision)

**Michael #2:** [**Skyplane Cloud Transfers**](https://twitter.com/aikidouke/status/1549687841265008642?s=12&t=LyRHbdObe2ee-wWTwuLslA)

- Skyplane is a tool for blazingly fast bulk data transfers in the cloud. 
- Skyplane manages parallelism, data partitioning, and network paths to optimize data transfers, and can also spin up VM instances to increase transfer throughput.
- You can use Skyplane to transfer data: 
    - Between buckets within a cloud provider 
    - Between object stores across multiple cloud providers 
    - (experimental) Between local storage and cloud object stores 
- Skyplane takes several steps to ensure the correctness of transfers: Checksums, verify files exist and match sizes.
- Data transfers in Skyplane are encrypted end-to-end.
- Security: Encrypted while in transit and over TLS + config options

**Brian #3:** [**7 things I've learned building a modern TUI framework**](https://www.textualize.io/blog/posts/7-things-about-terminals)

- by Will McGugan
- Specifically, **DictViews are amazing.** They have set operations.
- Example of using `items()` to get views, then `^` for symmetric difference (done at the C level):

```
    # Get widgets which are new or changed
    print(render_map.items() ^ new_render_map.items())
```

- Lots of other great topics in the article
    - `lru_cache` is fast
    - Unicode art in addition to text in doc strings
    - The `fractions` module
    - and a cool embedded video demo of some of the new css stuff in Textual
- [**Python’s object allocator ascii art**](https://github.com/python/cpython/blob/4b4439daed3992a5c5a83b86596d6e00ac3c1203/Objects/obmalloc.c#L778)

**Michael #4:** [‘Unstoppable’ Python](https://www.infoworld.com/article/3669232/python-popularity-still-soaring.html)

- Python popularity still soaring: ‘Unstoppable’ Python once again ranked No. 1 in the August updates of both the Tiobe and Pypl indexes of programming language popularity.
- [Python first took the top spot in the index last October](https://www.infoworld.com/article/3636789/python-tops-tiobe-language-index.html), becoming the only language besides Java and C to hold the No. 1 position.
- “Python seems to be unstoppable,” said the Tiobe commentary accompanying the August index.
- In the alternative [Pypl Popularity of Programming Language index](https://pypl.github.io/PYPL.html), which assesses language popularity based on Google searches of programming language tutorials, Python is way out front.

**Extras** 

Brian:

- Matplotlib stylesheets can make your chart look awesome with one line of code.
    - But it never occurred to me that I could write my own style sheet.
    - Here’s an article discussing creation of custom matplotlib stylesheets
        - [**The Magic of Matplotlib Stylesheets**](https://www.datafantic.com/the-magic-of-matplotlib-stylesheets/)
        - [**XKCD Plots**](https://jakevdp.github.io/blog/2013/07/10/XKCD-plots-in-matplotlib/)

Michael:

- Back [on 295](https://pythonbytes.fm/episodes/show/295/flutter-python-gui-apps) we talked about [Flet](https://flet.dev). We now have a Talk Python episode on it ([live](https://www.youtube.com/watch?v=kxsLRRY2xZA) and [polished](https://talkpython.fm/episodes/show/378/flet-flutter-apps-in-python) versions).

**Joke:** [Rakes and AWS](https://twitter.com/PR0GRAMMERHUM0R/status/1550254320637157379)

