# Python Bytes 281

Sponsored: [**RedHat: Compiler Podcast**](https://pythonbytes.fm/compiler)

Special guest: [**Anna Astori**](https://twitter.com/AmaMidzu)

**Michael #1:** [**Take Your Github Repository To The Next Level 🚀️**](https://dev.to/eludadev/take-your-github-repository-to-the-next-level-17ge)

- Step 0. Make Your Project More Discoverable
- Step 1. Choose A Name That Sticks
- Step 2. Display A Beautiful Cover Image
- Step 3. Add Badges To Convey More Information
- Step 4. Write A Convincing Description
- Step 5. Record Visuals To Attract Users 👀
- Step 6. Create A Detailed Installation Guide (if needed)
- Step 7. Create A Practical Usage Guide 🏁
- Step 8. Answer Common Questions
- Step 9. Build A Supportive Community
- Step 10. Create Contribution Guidelines
- Step 11. Choose The Right License
- Step 12. Plan Your Future Roadmap
- Step 13. Create Github Releases (know [release drafter](https://github.com/release-drafter/release-drafter))
- Step 14. Customize Your Social Media Preview
- Step 15. Launch A Website

**Brian #2:** [**Fastero**](https://fastero.readthedocs.io/en/latest/index.html)

- “Python timeit CLI for the 21st century.”
- Arian Mollik Wasi, [@wasi_master](https://twitter.com/wasi_master)
- Colorful and very usable benchmarking/comparison tool
- Time or Compare one ore more
    - code snippet
    - python file
    - mix and match, even
- Allows setup code before snippets run
- Multiple output export formats: markdown, html, csv, json, images, …
- Lots of customization possible
- Takeaway
    - especially for comparing two+ options, this is super handy

**Anna** **#3:** 

- langid vs langdetect

langdetect

- This library is a direct port of Google's language-detection library from Java to Python
- langdetect supports 55 languages out of the box (ISO 639-1 codes):
- Basic usage: detect() and detect_langs()
- great to work with noisy data like social media and web blogs
- being statistical, works better on larger pieces of text vs short posts

langid

- hasn't been updated for a few years
- 97 languages
- can use Python's built-in wsgiref.simple_server (or fapws3 if available) to provide language identification as a web service. To do this, launch python langid.py -s, and access http://localhost:9008/detect . The web service supports GET, POST and PUT.
- the actual calculations are implemented in the log-probability space but can also have a "confidence" score for the probability prediction between 0 and 1:
    > from langid.langid import LanguageIdentifier, model
    > identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
    > identifier.classify("This is a test")
    > ('en', 0.9999999909903544)
        - minimal dependencies
        - relatively fast
        - NB algo, can train on user data.



**Michael #4:** [**Watchfiles**](https://watchfiles.helpmanual.io)

- by Samual Colvin (of Pydantic fame)
- Simple, modern and high performance file watching and code reload in python.
- Underlying file system notifications are handled by the [Notify](https://github.com/notify-rs/notify) rust library.
- Supports sync watching but also async watching
- CLI example
- Running and restarting a command¶
    - Let's say you want to re-run failing tests whenever files change. You could do this with watchfiles using
    - Running a command:  `watchfiles 'pytest --lf``'` 

**Brian #5:** [**Slipcover: Near Zero-Overhead Python Code Coverage**](https://github.com/plasma-umass/slipcover)

- From coverage.py twitter account, which I’m pretty sure is Ned Bachelder
- coverage numbers with “3% or less overhead”
- Early stages of the project.
- It does seem pretty zippy though. 
- Mixed results when trying it out with a couple different projects
    - flask:
        - just pytest:  2.70s
        - with slipcover: 2.88s
        - with coverage.py:  4.36s
    - flask with xdist n=4
        - pytest:   2.11 s
        - coverage: 2.60s
        - slipcover: doesn’t run (seems to load pytest plugins)
- Again, still worth looking at and watching. It’s good to see some innovation in the coverage space aside from Ned’s work.

**Anna #6:** 

- scrapy vs robox

scra-py

- shell to try out things: fetch url, view response object, response.text
- extract using css selectors or xpath
- lets you navigate between levels e.g. the parent of an element with id X
- crawler to crawl websites and spider to extract data
- startproject for project structure and templates like settings and pipelines
- some advanced features like specifying user-agents etc for large scale scraping.
- various options to export and store the data
- nice features like LinkExtractor to determine specific links to extract, already deduped.
- FormRequest class

robox

- layer on top of httpx and beautifulsoup4
- allows to interact with forms on pages: check, choose, submit

**Extras** 

Michael:

- [**ohmyzsh**](https://ohmyz.sh) + [**ohmyposh**](https://ohmyposh.dev) + [**mcfly**](https://github.com/cantino/mcfly) + [**iterm2**](https://iterm2.com) + [**pls**](https://dhruvkb.github.io/pls/) + [**nerdfonts**](https://www.nerdfonts.com/font-downloads) = wow

**Joke:** 

- [**Out for a byte**](https://www.reddit.com/r/ProgrammerHumor/comments/u72sli/hello_i_am_your_server_for_today/)

