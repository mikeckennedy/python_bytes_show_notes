# Python Bytes 317

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).


**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

**Michael #1:** [**StackOverflow 2022 Developer Survey**](https://survey.stackoverflow.co/2022)

- Last year we saw Git as a fundamental tool to being a developer. This year it appears that **Docker is becoming a similar fundamental tool for Professional Developers**, increasing from 55% to 69%.
- Language: **Rust** is […] **the most loved language** with 87% of developers saying they want to continue using it.
- JS Frameworks: **Angular.js is in its third year as the most dreaded**.
- Let me Google that for you: 62% of all respondents **spend more than 30 minutes a day searching for answers** or solutions to problems. 25% spending more than an hour each day. 
- The demise of the full-stack developer [is overrated](https://survey.stackoverflow.co/2022/#section-developer-roles-developer-type).
- I do wish [there were more women](https://survey.stackoverflow.co/2022/#section-demographics-gender) in the field.
- **Databases**: Postgres is #1 and MongoDB is still going strong.
- The “[which web framework do you use](https://survey.stackoverflow.co/2022/#section-most-popular-technologies-web-frameworks-and-technologies)?” question is a full on train wreck. Why is this so hard for people to write the question? Node.js or Express (built on Node) vs. FastAPI or Flask (but no Python?)
- Most wanted / loved language is Rust (wanted) and **Python/Rust tied for most wanted**.
- [Worked with vs. want to work with](https://survey.stackoverflow.co/2022/#section-worked-with-vs-want-to-work-with-programming-scripting-and-markup-languages) has some interesting graphics.

**Brian #2:** [**PePy.tech - PyPI download stats with package version breakdown**](https://pepy.tech)

- Petru Rares Sincraian
- We’ve discussed pypistats.org before, which highlights
    - daily downloads
    - downloads per major/minor Python version
    - downloads per OS
- PyPy is a bit more useful for me
    - default shows last few versions and total for this major version
    - “select versions” box is editable.
        - clicking in it shows dropdown with downloads per version already there
        - you can add `*` for graph of total
        - or other major versions if you want to compare
    - daily/weekly/monthly is nice, to round out some noise and see larger trends
    - Oddity I noticed - daily graph isn’t the same dates as the table. 
        - off by a day on both sides
        - not a big deal, but I notice these kinds of things.

**Michael #3:**  [**Codon Python Compiler**](https://github.com/exaloop/codon)

- via Jeff Hutchins and Abdulaziz Alqasem
- A high-performance, zero-overhead, extensible Python compiler using LLVM 
- You can scale performance and produce executables, even when using third party libraries such as matplotlib. 
- It also supports writing and executing GPU kernels, which is an interesting feature.
- See how it works at [exaloop.io](https://exaloop.io)
- BTW, **really terrible licensing**. 
    - Free for non-commercial (great)
    - “Contact us” for commercial use (it’s fine to charge, but give us a price)

**Brian #4:**  [**8 Levels of Using Type Hints in Python**](https://medium.com/techtofreedom/8-levels-of-using-type-hints-in-python-a6717e28f8fd)

- [Yang Zhou](https://medium.com/@yangzhou1993?source=post_page-----a6717e28f8fd--------------------------------) (yahng cho)
- A progression of using type hints that seems to track how I’ve picked them up
1. Type Hints for Basic Data Types. 
    - `x: int`
2. Define a Constant Using Final Type 
    - `DB: Final =` `'``PostgreSQL'`
    - (ok. I haven’t used this one at all yet) 
3. Adding multipe type hints to one variable. 
    - `int | None`
4. Using general type hints. 
    - `def func(nums: Iterable)` 
    - Also using `Optional`
5. Type hints for functions 
    -  `def func(name: str) → str:` 
    - (I probably would put this at #2)
6. Alias of type hints (not used this yet, but looks cool)
    PostsType = dict[int, str]
    
    new_posts: PostsType = {1: 'Python Type Hints', 2: 'Python Tricks'}
1. Type hints for a class itself, i.e. `Self` type
    from typing import Self
    
    class ListNode:
        def __init__(self, prev_node: Self) -> None:
            pass
1. Provide literals for a variable.  (not used this yet, but looks cool)
    from typing import Literal
    weekend_day: Literal['Saturday', 'Sunday']
    weekend_day = 'Saturday'
    weekend_day = 'Monday' # will by a type error
    

**Extras** 

Brian:

- I hear a heartbeat for Test & Code, so it must not be dead yet.
        

Michael:

- New article: [Welcome Back RSS](https://mkennedy.codes/posts/welcome-back-rss/)
    - From this I learned about [Readwise](https://readwise.io/read), [Kustosz](https://www.kustosz.org), and Python’s [reader](https://reader.readthedocs.io/en/latest/). 
- [Year progress == 100%](https://techhub.social/@year_progress/109611005011655695)
- [PyTorch discloses malicious dependency chain compromise over holidays](https://www.bleepingcomputer.com/news/security/pytorch-discloses-malicious-dependency-chain-compromise-over-holidays/) (of course found over RSS and reeder — see article above)

**Joke:**  [vim switch](https://www.reddit.com/r/programminghumor/comments/z6uga8/finally_they_made_a_switch_to_exit_vim/)

