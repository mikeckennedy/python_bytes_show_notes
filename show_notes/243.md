# Python Bytes 243

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**Simon Willison**](https://twitter.com/simonw)

**Michael #1:** [**MongoDB 5**](https://www.mongodb.com/blog/post/launched-today-mongodb-5-0-serverless-atlas-evolution-application-data-platform)

- **Native Time Series**: Designed for IoT and financial analytics, our new time series collections, clustered indexing, and window functions make it easier, faster, and lower cost to build and run time series applications
- MongoDB automatically optimizes your schema for high storage efficiency, low latency queries, and real-time analytics against temporal data.
- **The Versioned API** future-proofs your applications. You can fearlessly upgrade to the latest MongoDB releases without the risk of introducing backward-breaking changes that require application-side rework
- **New MongoDB Shell** we have introduced syntax highlighting, intelligent auto-complete, contextual help and useful error messages creating an intuitive, interactive experience for MongoDB users (use `mongosh` rather than `mongo` on the CLI).
- Also launched preview release of serverless instances on MongoDB Atlas
- You can [**watch the MongoDB keynote here**](https://www.youtube.com/watch?v=OQJHf8xdDRM).

**Brian #2:** [**Python 3.11 : Enhanced error locations in tracebacks**](https://docs.python.org/3.11/whatsnew/3.11.html#enhanced-error-locations-in-tracebacks)

- Yes, 3.11. Even though 3.10 is still in Beta, we’re already excited about 3.11
- tracebacks now point to the exact expression that caused the error within the line:

```
    Traceback (most recent call last):
      File "distance.py", line 11, in <module>
        print(manhattan_distance(p1, p2))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "distance.py", line 6, in manhattan_distance
        return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)
                               ^^^^^^^^^
    AttributeError: 'NoneType' object has no attribute 'x'
```

- even deeply nested calls

```
    Traceback (most recent call last):
    File "query.py", line 37, in <module>
        magic_arithmetic('foo')
        ^^^^^^^^^^^^^^^^^^^^^^^
      File "query.py", line 18, in magic_arithmetic
        return add_counts(x) / 25
               ^^^^^^^^^^^^^
      File "query.py", line 24, in add_counts
        return 25 + query_user(user1) + query_user(user2)
                    ^^^^^^^^^^^^^^^^^
      File "query.py", line 32, in query_user
        return 1 + query_count(db, response\['a'\]['b']\['c'\]['user'], retry=True)
                                   ~~~~~~~~~~~~~~~~~~^^^^^
    TypeError: 'NoneType' object is not subscriptable
```

- and math expressions:

```
    Traceback (most recent call last):
      File "calculation.py", line 54, in <module>
        result = (x / y / z) * (a / b / c)
                  ~~~~~~^~~
    ZeroDivisionError: division by zero
```

**Simon #3:** **fly.io** [**multi-region PostgreSQL**](https://fly.io/docs/getting-started/multi-region-databases/) and [**last mile Redis**](https://fly.io/blog/last-mile-redis/)

- fly.io are a hosting provider that specialize in running your code in containers that are geographically close to your users
- What I find interesting about them is that they are taking something that used to be INCREDIBLY hard - like geographically sharding your database - and describing patterns for doing that which make it easy-enough that I might actually do it
- Their writing is really good. I’m learning a ton from them about designing code to run globally that applies even if I don’t end up using their service

**Michael #4:** [**django-unicorn**](https://www.django-unicorn.com/)

- A magical full-stack framework for Django
- Quickly add in simple interactions to regular Django templates without learning a new templating language. 
- Building a feature-rich API is complicated. Skip creating a bunch of serializers and just use Django. 
- Early days if you want to contribute

**Brian #5:** [**Blue : The somewhat less uncompromising code formatter than**](https://blue.readthedocs.io/en/latest/) `[**black**](https://blue.readthedocs.io/en/latest/)`

- Suggested by Chris May
- Code from Black, mods by Grant Jenks and Barry Warsaw
- It’s not a fork, it’s a patched version of black. Kind of a “containment over inheritance” thing.
- Deltas:
	- blue defaults to single-quoted strings. 
		- except docstrings and triple quoted strings (TQS). Those are still double quotes.
	- blue defaults to line lengths of 79 characters. black is 88.
    - line lengths are customizable with all related tools.
	- blue preserves the whitespace before the hash mark for right hanging comments.
		- making comment blocks off to the side possible
	- blue supports multiple config files: pyproject.toml, setup.cfg, tox.ini, and .blue.
- Interesting quote from the docs: “We’d prefer not to fork or monkeypatch. Instead, our hope is that eventually we’ll be able to work with the `black` maintainers to add just a little bit of configuration and merge back into the `black` project. “
- My take
	- Probably stick with black most of the time. 
	- For some large exiting projects with lots of strings that have standardized to single quote strings already, black is jarring. 
	- Also, strings with double quotes in them are untouched by black, so if you have lots of those, strings will be inconsistent, making the code harder to read and confusing to maintain.
	- And the choice isn’t really black or blue. It’s often nothing due to the non-starter of switching to double quote strings by default. blue is better than nothing.
- [See also](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) `[# fmt: off](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)`[,](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) `[# fmt: on](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)` [for both blue and black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)

```
    # tell black/blue to not reformat this table
    # fmt: off
    some_table = [
        1,     2,   3,
        100, 200, 300
    ]
    # fmt: on
```

**Simon #6:** [**Organize and Index Your Screenshots (OCR) on macOS**](https://alexn.org/blog/2020/11/11/organize-index-screenshots-ocr-macos.html)

- I’ve been wanting to figure out how to use Tesseract OCR for years, and this post finally unlocked it for me
- brew install tesseract
- tesseract image.png output-file -l eng pdf
- (use txt instead of pdf to get plain text)
- I wrote a TIL about this at https://til.simonwillison.net/tesseract/tesseract-cli
- It’s really good! Even works against photos I’ve taken. And the PDFs it produces have copy-and-paste text in them (despite looking visually identical to the image) and can be searched using Spotlight.
- There’s a pytesseract library but it actually just works by running that Tesseract CLI tool [in a subprocess](https://github.com/madmaze/pytesseract/blob/31973a4c58ad7d871f6b6b4cae1aa3f2f29d6b43/pytesseract/pytesseract.py#L252)
- Extra: [Using SQL to find my best photo of a pelican according to Apple Photos](https://simonwillison.net/2020/May/21/dogsheep-photos/)

**Extras**

Michael:

- Strong Typing follow up
	- typed nametuple: [strongtyping.readthedocs.io/en/latest/namedtuple/](https://strongtyping.readthedocs.io/en/latest/namedtuple/)
	- now classes: [github.com/FelixTheC/strongtyping/issues/65](https://github.com/FelixTheC/strongtyping/issues/65)
- We are *finally* rid of tracking on the podcast sites. But it took some neat tech work

**Simon**

- [https://pythonbytes.fm/episodes/show/237/separate-your-sql-and-python-asynchronously-with-aiosql](https://pythonbytes.fm/episodes/show/237/separate-your-sql-and-python-asynchronously-with-aiosql) talked about Textual but it’s worth marveling at how far along it has already come, one of the fastest pieces of development-in-the-open I’ve ever seen - follow along on Will’s Twitter account, he posts a lot of videos and screenshots e.g. https://twitter.com/willmcgugan/media and the videos in his README at https://github.com/willmcgugan/textual/blob/main/README.md

**Joke** 

[**A “Query tale”?**](https://twitter.com/Spirix3/status/1410564231897006082)

Song from Brett Cannon (take on [**Pinky and the Brain theme song**](https://www.youtube.com/watch?v=qzZmU0aGmcc))

*What do you want to do today, Brian?*
*Same thing we do every Wednesday, Michael. Help Python take over the world.*
*It's Michael and the Brain!*
*Yes, Michael and the Brain!*
*One's into testing, the other GUIs!*
*They're both into making Python seem sane!*
*They're Michael,*
*they're Michael and the Brain, Brain, Brain, Brain, Brain!*

