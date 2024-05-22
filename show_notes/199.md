# Python Bytes 199
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python Testing with pytest**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)

**Michael #1:** [**micropython updated**](https://twitter.com/matt_trentini/status/1302980818877390849)

- via Matt Trentini
- v1.13 is packed with features and bugfixes including solid asyncio support and tasty BLE improvements. Heck, we've even got the walrus operator.
- a new implementation of the uasyncio module which aims to be more compatible with CPython's asyncio module.
- The main change is to use a Task object for each coroutine, allowing more flexibility to queue tasks in various places, eg the main run loop, tasks waiting on events, locks or other tasks.
- It no longer requires pre-allocating a fixed queue size for the main run loop.
- Most code in this repository is now auto-formatted using uncrustify for C code and Black for Python code.
- BlueKitchen BTstack bindings have been added for the ubluetooth module, as an optional alternative to the NimBLE stack. The unix port can now be built with BLE support using these bindings
- Other Bluetooth additions include: new events for service/characteristic/ descriptor discovery complete; new events for read done and indicate acknowledgement; and support for active scanning in BLE.gap_scan().
- PEP 526 has been (Walrus)
- There has been an important bug fix when importing ARM machine code from an .mpy file: the system now correctly tracks the executable memory allocated to the machine code so this memory is not reclaimed by the garbage collector.
- For testing, a multi-instance test runner has been added (see tests/run-multitests.py) which allows running a synchronised test across two or more MicroPython targets.
- There are breaking changes
- First release since Dec 19, 2019

**Brian #2:** [**respx: A utility for mocking out the Python HTTPX library**](https://lundberg.github.io/respx/)

- When using [requests](https://requests.readthedocs.io/en/master/), you can mock it with [responses](https://github.com/getsentry/responses).
- When using [httpx](https://github.com/encode/httpx), mock with [respx](https://lundberg.github.io/respx/).
- Quick start:
```
    import httpx
    import respx
    
    @respx.mock
    def test_something():
        request = respx.post("https://foo.bar/baz/", status_code=201)
        response = httpx.post("https://foo.bar/baz/")
        assert request.called
        assert response.status_code == 201
```

- Documentation includes examples of using respx with both pytest and unittest, including how to set up mocked_api fixtures for pytest.
- There’s call statistics you can assert on.
- Ability to raise exceptions, return non-200 status codes, set custom return content.
- Content can be generated in a callback method.
- JSON content can be returned
- Tons of nice options to help test your httpx based application.

**Michael #3:** [**GetPy - A Vectorized Python Dict/Set**](https://github.com/atom-moyer/getpy)

- The goal of GetPy is to provide the highest performance python dict/set that integrates into the python scientific ecosystem.
- GetPy is a thin binding to the Parallel Hashmap (https://github.com/greg7mdp/parallel-hashmap.git) which is the current state of the art unordered map/set with minimal memory overhead and fast runtime speed.
- The binding layer is supported by PyBind11 (https://github.com/pybind/pybind11.git)
- The gp.Dict and gp.Set objects are designed to maintain a similar interface to the corresponding standard python objects.
- Simple example:
- 
```
    import getpy as gp
    
    key_type = np.dtype('u8')
    value_type = np.dtype('u8')
    
    keys = np.random.randint(1, 1000, size=10**2, dtype=key_type)
    values = np.random.randint(1, 1000, size=10**2, dtype=value_type)
    
    gp_dict = gp.Dict(key_type, value_type)
    gp_dict[keys] = values
```

**Brian #4:** **isort and black now play nice together easily**

- Contributed by John Hagen
- `isort` “sorts your imports, so you don’t have to”
- `black` reformats all of your code to a consistent code style, including import statements
- There is a [config page on black documentation that shows how to set isort to be compatible with black](https://black.readthedocs.io/en/stable/compatible_configs.html#isort). It also shows how to make flake8 and pylint play nice with black, but they are less complicated.
- Now, however, with [isort 5 introduction of built in profiles](https://pycqa.github.io/isort/docs/major_releases/introducing_isort_5/), you can just use `isort` `--``profile black .` and the profile sets everything for you.
- There’s a [profile page for isort](https://pycqa.github.io/isort/docs/configuration/profiles/) that describes all that it does. 
- Other profiles include: django, pycharm, google, open_stack, plone, attrs, hug
- And as always, you can configure your own with config files.

**Michael #5:** [**Scientists rename human genes to stop Microsoft Excel from misreading them as dates**](https://www.theverge.com/2020/8/6/21355674/human-genes-rename-microsoft-excel-misreading-dates)

- Via Chris Moffitt
- There are tens of thousands of genes in the human genome
- Each gene is given a name and alphanumeric code, known as a symbol, which scientists use to coordinate research.
- Over the past year or so, some 27 human genes have been renamed, all because Microsoft Excel kept misreading their symbols as dates.
- Excel is regularly used by scientists to track their work and even conduct clinical trials.
- But its default settings were designed with more mundane applications in mind, so when a user inputs a gene’s alphanumeric symbol into a spreadsheet, like MARCH1 — short for “Membrane Associated Ring-CH-Type Finger 1” — Excel converts that into a date: 1-Mar.
- One study from 2016 examined genetic data shared alongside 3,597 published papers and found that roughly one-fifth had been affected by Excel errors.
- See 12 of the Biggest Spreadsheet Fails in History for more examples: https://blogs.oracle.com/smb/10-of-the-costliest-spreadsheet-boo-boos-in-history
- The scientific body in charge of standardizing the names of genes, the HUGO Gene Nomenclature Committee, published new guidelines for gene naming. From now on human genes and the proteins they expressed will be named with one eye on Excel’s auto-formatting.
- Check out the [**Excel to Python course**](https://talkpython.fm/excel) and [**webcast**](https://talkpython.fm/excel-webcast) to escape this.

**Brian #6:** [**Never Run ‘python’ In Your Downloads Folder**](https://glyph.twistedmatrix.com/2020/08/never-run-python-in-your-downloads-folder.html)

- by Glyph
- This is really a nice, short tutorial on how `sys.path` is populated, why you should care, and why you need to make sure it’s only trusted locations.
- “downloads” is definitely not trusted.
- So never, ever, ever run `python` from the downloads directory, even with `python -m something`, as that adds the download dir to the include path.
- Example includes a demonstration of malicious js code that downloads a fake `pip.py` to your downloads folder, so when you call `python -m pip install ./legit_package.whl` you get the fake pip.
- Further examples show how you need to be vigilant to check your dot files for weird PYTHONPATH extensions and additions. 

Extras:


Michael:

- We recently passed 5,000,000 downloads of the audio files over at Python Bytes and are the 130th most popular tech podcast in the world. Thank you everyone!
- Got a new [**LinkSys WiFi 6 mesh router**](https://www.bestbuy.com/site/linksys-mx10-velop-ax5300-mesh-wi-fi-6-system-2-pack-white/6373231.p?skuId=6373231), and wow, highly recommended.

Joke

Are you a real programmer? [**Check with XKCD**](https://xkcd.com/378/) to find out.