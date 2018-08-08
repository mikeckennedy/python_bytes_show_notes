# Python Bytes 86

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest Bob Belderbos: [@bbelderbos](https://twitter.com/bbelderbos)

**Brian #1:** [**responses**](https://github.com/getsentry/responses)

- “A utility for mocking out the Python Requests library.”
- From Sentry

Example:

    import responses
    import requests
    
    @responses.activate
    def test_simple():
        responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
                      json={'error': 'not found'}, status=404)
        resp = requests.get('http://twitter.com/api/1/foobar')
        assert resp.json() == {"error": "not found"}
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'http://twitter.com/api/1/foobar'
        assert responses.calls[0].response.text == '{"error": "not found"}'

**Bob #2:** [**29 common beginner Python errors on one page**](https://pythonforbiologists.com/29-common-beginner-errors-on-one-page/)

- Decision trees / graphics are nice to digest and concise, it wraps a lot of experience on one slide
- Knowing about common errors can safe you a lot of time (the guide I wish I had when I started coding in Python)
- Reminded me of struggles I had when I started in Python, for example TypeErrors when converting suspected ints to strings, regexes before discovering raw strings
- It made me think of related issues newer Pythonistas face, for example “I am reading a file but getting no input” can be translated to “I am looping over a generator for the second time and don’t get any output”
- Made me realize that some things are subtle, like comparing 3 == “3” or require good knowledge of stdlib (sorted returning new sequence vs inplace sort() for example)
- Made me reflect on how much hand holding you would give your students when teaching. Part of the learning is in the struggle. 
- About the source, I like seeing Python being taught in all different kind of domains, in this case biology.

**Michael #3:** [**μMongo**](https://github.com/Scille/umongo) ****

- μMongo is a Python MongoDB ODM. 
- It inception comes from two needs: 
	- the lack of async ODM
	- the difficulty to do document (un)serialization with existing ODMs.
- a few design choices:
	- Stay close to the standards MongoDB driver to keep the same API when possible: use `find({"field": "value"})` like usual but retrieve your data nicely OO wrapped !
	- Work with multiple drivers (PyMongo, TxMongo, motor_asyncio and mongomock for the moment)
	- Tight integration with Marshmallow serialization library to easily dump and load your data with the outside world
	- i18n integration to localize validation error messages
	- Free software: MIT license
	- Test with 90%+ coverage ;-)
- async / await support through Motor

**Brian #4:** [**Basic Statistics in Python: Descriptive Statistics**](https://www.dataquest.io/blog/basic-statistics-with-python-descriptive-statistics/)

- Cool use of Python to teach basic statistics topics. 
- Includes code snippets to explain different concepts like min, max, mean, median, mode, …
- However, after you understand the math, DON’T write your own functions.
	- use built in Python functions and  t[he statistics library built in to Python](https://docs.python.org/3/library/statistics.html) (or numpy if you are on older Python versions).
  

Example from article:

    sum_score = sum(scores)
    num_score = len(scores)
    avg_score = sum_score/num_score
    avg_score
    >>> 87.8884184721394

Using built in:

    >>> x = (2, 2, 3, 100)
    >>> min(x), max(x)
    (2, 100)
    >>> import statistics as s
    >>> s.mean(x), s.median(x), s.mode(x)
    (26.75, 2.5, 2)
    >>> s.pstdev(x), s.pvariance(x)
    (42.29287765097097, 1788.6875)
    >>> s.stdev(x), s.variance(x)
    (48.835608593184, 2384.9166666666665)

**Bob #5:** [**Strings and Character Data in Python**](https://realpython.com/python-strings/#.W0P9uWMUJ7U.twitter) 

- Everything you need to know to work with strings and more …
- Similar to [that great itertools article](https://realpython.com/python-itertools/) you shared some weeks ago: exhaustive overview
- Nice re-usable code snippets and explanation of basic concepts, ideal for beginners but you likely will get something out of it, few useful bites:
	- Instead of `try int(…) except`, you can use `isdigit()` on a string
	- You can use `isspace()` to see if all characters of a nonempty string are whitespace characters ( `' '`, tab `'\t'`, and newline `'\n'`)
	- It’s easy to make a header in your Python scripts: 
```
>>>> 'bar'.center(10, '-')
		'---bar----'
```
	- Replace up till n occurrences:
```
>>>> 'foo bar foo baz foo qux'.replace('foo', 'grault', 2)
		'grault bar grault baz foo qux'
```
	- Strip multiple characters from both ends of a string:
```
>>>> 'www.realpython.com'.strip('w.moc')
		'realpython'
```
	- Add leading padding to a string with `zfill`: 
```
>>>> '42'.zfill(5)
		'00042'
```

- This also reminded me of Python’s polymorphism, for example str.find and str.index work on both strings as well as lists

```
    >>> 'foo bar foo baz foo qux'.index('baz')
      12
    >>> 'foo bar foo baz foo qux'.split().index('baz')
      3
    >>> 'foo bar foo baz foo qux'.count('foo')
      3
    >>> 'foo bar foo baz foo qux'.split().count('foo')
      3
```

**Michael #6:** **PEP 572**: [**Assignment expressions accepted**](https://twitter.com/raymondh/status/1014210487112818689)

- Whoa, check out that twitter conversation
- Splits 2 statements into an expressions (so they can be part of list comprehensions, etc).
- Not sure I like it but here you go:

Example:

    # Handle a matched regex
    if (match := pattern.search(data)) is not None:
        ...

Contrast old and new:

    # old
    if self._is_special:
        ans = self._check_nans(context=context)
        if ans:
            return ans


    # new
    if self._is_special and (ans := self._check_nans(context=context)):
        return ans

**Our news:**

* Michael: New course coming! Data-driven web apps in Pyramid
* Bob: Be sure to visit [PyBites Code Challenges](https://codechalleng.es/)
* Brian: More [Test and Code](http://testandcode.com/) episodes coming!

