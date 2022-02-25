# Python Bytes 272

**Sponsor**: Brought to you by [**FusionAuth**](http://pythonbytes.fm/fusionauth) - check them out at [**pythonbytes.fm/fusionauth**](https://pythonbytes.fm/fusionauth)

Special guest: **[Calvin Hendryx-Parker](https://twitter.com/calvinhp)**

**Brian #1:** [**Why your mock still doesn’t work**](https://nedbatchelder.com/blog/202202/why_your_mock_still_doesnt_work.html)

- Ned Batchelder
- Some back story: [Why your mock doesn’t work](https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html)
    - a quick tour of Python name assignment
        - The short version of [Python Names and Values](https://nedbatchelder.com/text/names1.html) talk
    - importing
    - difference between `from foo import bar` and `import foo` w.r.t mocking
    - punchline: “Mock it where it’s used”
- Now, [Why your mock still doesn’t work](https://nedbatchelder.com/blog/202202/why_your_mock_still_doesnt_work.html) talks about
    - using `@patch` decorator (also applies to `@patch.object` decorator)
    - and utilizing `mock_thing1, mock_thing2` parameters to test
    - you can change the return value or an attribute or whatever. normal mock stuff.
    - But…. the punchline…. be careful about the order of patches.
- It needs to be
```
    @patch("foo.thing2")
    @patch("foo.thing1")
    def test_(mock_thing1, mock_thing2):
      ...
```
- Further reading:
    - https://docs.python.org/3/library/unittest.mock.html#patch
    - https://docs.python.org/3/library/unittest.mock.html#patch-object

**Michael #2:** [**pls**](https://twitter.com/mkennedy/status/1494107080726396928)

- via Chris May
- Are you a developer who uses the terminal? (likely!)
- ls/l are not super helpful. There are replacements and alternatives
- But if you’re a dev, you might want the most relevant info for you, so enter pls
- See images in Michael’s tweets [[1](https://twitter.com/mkennedy/status/1494107080726396928), [2](https://twitter.com/mkennedy/status/1494115221727846400)].
- You must install [nerdfonts](https://www.nerdfonts.com/) and set your terminal’s font to them

**Calvin #3:** [**Kitty**](https://sw.kovidgoyal.net/kitty/)

- Cross platform GPU accelerated terminal (written in Python
- Extended with Kittens written in Python
- Super fast rendering
- Has a rich set of plugins available for things like searching the buffer with fzf

**Brian #4:** [**Futures and easy parallelisation**](https://wrongsideofmemphis.com/2022/02/17/futures-and-easy-parallelisation/)

- Jaime Buelta
- Code example for quick scripts to perform slow tasks in parallel.
- Uses `concurrent.futures` and `ThreadPoolExecutor`.
- Starts with a small toy example, then goes on to a requests example to grab a bunch of pages in parallel.
    - The call to `executor.submit()` sets up the job.
        - This is done in a list comprehension, generating a list of futures.
    - The call to `futures.result()`  on each future within the list is where the blocking happens. Since we want to wait for all results, it’s ok to block on the first, second, etc.
- Nice small snippet for easy parallel work.
- Example:
  
```    
    from concurrent.futures import ThreadPoolExecutor
    import time
    import requests
    from urllib.parse import urljoin
    
    NUM_WORKERS = 2
    executor = ThreadPoolExecutor(NUM_WORKERS)
    
    def retrieve(root_url, path):
        url = urljoin(root_url, path)
        print(f'{time.time()} Retrieving {url}')
        result = requests.get(url)
        return result
    
    arguments = [('https://google.com/', 'search'),
                 ('https://www.facebook.com/', 'login'),
                 ('https://nyt.com/', 'international')]
    futures_array = [executor.submit(retrieve, *arg) for arg in arguments]
    result = [future.result() for future in futures_array]
    print(result)
```

**Michael #5:** [**pgMustard**](https://www.pgmustard.com/)

- So you have a crappy web app that is slow but don’t know why.
- Is it an N+1 problem with an ORM?
- Is it a lack of indexes?
- If you’re using postgres, check out pgMustard: A simple yet powerful tool to help you speed up queries
- This is a paid product but might be worthwhile if you live deeply in postgres.

Calvin #6: [**bpytop**](https://github.com/aristocratos/bpytop)

- Great way to see what is going on in your system/server
- Shows nice graphs in the terminal for system performance such as CPU and Network traffic
- Support themes and is fast and easy to install with `pipx`
- Michael uses [Glances](https://nicolargo.github.io/glances/) which is fun too. Calvin used to be a heavy Glances user until he saw the light 🙂 

Extras 

Brian: 

- [pytest book](https://pythontest.com/pytest-book/) is officially no longer Beta, next is printing, expected paper copy ship date at March 22, although I’m hoping earlier.
    - For a limited time, to celebrate, [40% off the eBook](https://media.pragprog.com/newsletters/2022-02-22.html)
- [PyCamp Spain](https://pycamp.es/) is April 15-18: a weekend that includes 4 days and 3 nights with full board (breakfast, lunch and dinner) in Girona, Spain

Calvin:

- Python Web Conference 2022 ← bigger and better than ever!
  

Michael:

- [witch macOS switcher](https://manytricks.com/witch/)
- list comprehensions vs. loops [[video](https://www.youtube.com/watch?v=uVQVn8z8kxo), [code](https://gist.github.com/mikeckennedy/2ddb5ad84d6e116e6d14b5c2eef4245a)]
- [syncify.run](https://twitter.com/mkennedy/status/1495863810409865220) and [nesting asyncio](https://twitter.com/pdgjones/status/1495867430010339339)

Joke: [Killer robots](https://twitter.com/pr0grammerhum0r/status/1489282557074190340?s=12)

