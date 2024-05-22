# Python Bytes 268


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!


**Brian #1:** [**(draft) PEP 679 -- Allow parentheses in assert statements**](https://www.python.org/dev/peps/pep-0679/)

- Pablo Galindo Salgado
- This is in draft, not approved, and not scheduled for any release
- But it seems like a really good idea to me.
- `assert(1 == 2, "seems like it should fail")` will always pass currently
- since the tuple `(False,"seems like it should fail")` is a non-empty tuple.
- Current Python will emit a warning

```
    >>> assert(1 == 2, "seems like it should fail")
    <stdin>:1: SyntaxWarning: assertion is always true, perhaps remove parentheses?
```

- - But really, why not just change the language to allow `assert` with or without parens.
- Also would allow multi-line assert statements more easily:

```
    assert (
        very very long
        expression,
    
        "very very long "
        "message",
    )
```

- - I hope this is a slam dunk and gets in ASAP. 


**Michael #2:** [**Everything I googled as a dev**](https://localghost.dev/blog/everything-i-googled-in-a-week-as-a-professional-software-engineer/)

- by Sophie Koonin
- In an attempt to dispel the idea that if you have to google stuff you’re not a proper engineer, this is a list of nearly everything I googled in a week at work
- Rather than my posting a huge list, check out the day logs on her post
- Worth calling out a few:
    - `Expecting a parsed GraphQL document. Perhaps you need to wrap the query string in a "gql" tag?` - said React upgrade then started causing some super fun errors.
    - `semantic HTML contact details` - wanted to check if the `<address>` tag was relevant here
    - `editing host file` - desperate times (and it didn’t even work)


**Madison #3:** [**PyCascades 2022!**](https://2022.pycascades.com/)

- Another year of excellent and diverse talks across an array of subjects.
- Talks from some well known folks ([Thursday Bram](https://2022.pycascades.com/program/talks/supporting-the-george-floyd-protests-in-portland-demonstrations-legal-support-and-django-apps/), [Jay Miller](https://2022.pycascades.com/program/talks/diversity-in-neurodiversity-help-for-underrepresented-folks-in-tech-and-allies-with-new-mental-health-diagnoses/)) as well as first time speakers ([Joseph Riddle](https://2022.pycascades.com/program/talks/how-not-to-start-a-python-user-group/), [Isaac Na](https://2022.pycascades.com/program/talks/council-data-project-infrastructure-as-code-for-civic-transparency-and-accessibility/))
- PSF’s DE&I Panel is doing a meet & greet, and they have [a survey they’d like Python community members to fill out](https://docs.google.com/forms/d/e/1FAIpQLSc8957QqYuPDF2qL8Q2ctFzBH_mPMi0yxSQ2oqOACTU9jIVDg/viewform).
- Socials Friday & Saturday night, sprints on Sunday.
- [Tickets are still available!](https://pretix.eu/pycascades/remote-2022/)


**Brian #4:**  [**Strict Python function parameters**](https://sethmlarson.dev/blog/strict-python-function-parameters)

- Seth Michael Larson
- We have keyword only parameters
    -  `def process_data(data, *, encoding="ascii"): ...`
    - notice the `*`
    - `encoding` has to be a keyword argument, cannot be positional.
- We have position only parameters:
    - `def process_data(data, /, encoding="ascii"): ...` 
    - notice the `/`
    - `data` has to be positional, cannot be passed in as a keyword argument
- Combine the two:
    - `def process_data(data, /, *, encoding="ascii"): ...`
    - Now `data` has to be positional, and `encoding` has to be a keyword, if present.
- This way a function really can only be called as intended and all uses of the function will be consistent. This is a good thing.
- There are many benefits, including [empowering library authors](https://www.python.org/dev/peps/pep-0570/#empowering-library-authors) to make changes without weird behaviors cropping up in user code.
- Commentary:
    - extra syntax may be confusing for some new users. 
    - For a lot of library API entry points, I think this makes a lot of sense.


**Michael #5:** [**mureq**](https://github.com/slingamn/mureq) **- vendored requests**

- `mureq` is a single-file, zero-dependency alternative to [python-requests](https://github.com/psf/requests)
- Intended to be vendored in-tree by Linux systems software and other lightweight applications.
- Doesn’t support connection pooling (but neither does `requests.get()`).
- Uses much less memory
- Avoids supply chain attack vulnerabilities 
- Consider [**my prod branch**](https://github.com/mikeckennedy/mureq/tree/prod) until PRs [**#2**](https://github.com/slingamn/mureq/pull/2) and [**#3**](https://github.com/slingamn/mureq/pull/3) are merged.

**Madison #6**: [**Openverse**](https://make.wordpress.org/openverse/2022/01/25/everything-you-need-to-know-about-openverse-and-the-wordpress-photo-directory/)

- No, not Metaverse!
- Previously [“CC Search”](https://creativecommons.org/2021/12/13/dear-users-of-cc-search-welcome-to-openverse/)
- Search engine for openly licensed media, for [free and public](https://creativecommons.org/use-remix/) use/remix of content.
- Currently images & audio, hope to include video, text, 3D models down the line.
- [Start your search here](http://wp.org/openverse)


**Extras** 

Michael:

- We now have playable times in the transcript section ([**example**](https://pythonbytes.fm/episodes/transcript/267/python-on-the-beach)).
- Very cool tool for building regex-es I used for the above: [**regex101.com**](https://regex101.com/r/BRaEMy/1)
- Next video is out: [**Do you even need loops in Python? A Python short by Michael Kennedy**](https://www.youtube.com/watch?v=uVQVn8z8kxo)
- Remember, we have full-text search

Brian:

- [pip-secure-install](https://github.com/marketplace/actions/pip-secure-install) - from Brett Cannon
- [Python Testing with pytest](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) is, when I last checked, the [#2 bestseller at Pragmatic](https://pragprog.com/best_sellers/)
    - so cool
    - My Maui trip was also a work trip. Gave me time to completely re-read the book, make notes, and make last minute changes. Changes went in this week and tonight is my “pencils down” date. This is getting real, folks. 
    - Thanks to everyone for buying beta copies and supporting the re-write. 

Madison:

- [spd.watch](https://spd.watch) - new police accountability/information tool for the Seattle area
- Shoutout to `[just](https://github.com/casey/just)` (mentioned in [Ep 242](https://pythonbytes.fm/episodes/show/242/from-lib-import-but-less))
- [ghcr.io](https://ghcr.io) - free docker image hosting for open source projects, easy integration with GitHub Actions

**Joke:** 

via Josh Thurston

- How did the hacker get away from the police? He just ransomware.
- That joke makes me WannaCry…
- Where do you find a hacker? In decrypt.
