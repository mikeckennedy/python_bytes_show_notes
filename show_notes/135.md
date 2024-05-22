# Python Bytes 135
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest [**Max**](https://twitter.com/maxsklar) [**Sklar**](https://twitter.com/maxsklar) 

**Brian #1:** [**Why do Python lists let you += a tuple, when you can’t + a tuple?**](https://lerner.co.il/2019/06/06/why-do-python-lists-let-you-a-tuple-when-you-cant-a-tuple/)

- Reuven Lerner

```
    >>> x = [1, 2, 3]
    >>> b = (4, 5, 6)
    >>> x + b
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate list (not "tuple") to list
    >>> x += b
    >>> x
    [1, 2, 3, 4, 5, 6]
```

- Huh??
- “It turns out that the implementation of `list.__iadd__` (in place add) takes the second (right-hand side) argument and adds it, one element at a time, to the list. It does this internally, so that you don’t need to execute any assignment after. The second argument to “+=” must be iterable.”

**Max #2**: [**R vs Python, R is out of top 20 languages despite statistical boom**](https://www.zdnet.com/article/r-vs-python-rs-out-of-top-20-programming-languages-despite-boom-in-statistical-jobs/)

- Subtitle: is R declining because of Python?
- First of all, this article is about an index on the popularity of programming languages from an organization TIOBE. They have an index on the popularity of programming languages. Obviously it’s a combination of many different scores, and that could be controversial, but I’m going to assume that they put some thought into how the rankings are calculated, and that it’s as good as any.
- A few stories here: first Python hit at all time high in their ranking at number 3, beating out c++ I believe for the first time, and only Java and C are above it.
- The other story is that the statistical language R dipped below 20 to number 21, and the speculation is that Python has sort of taken over as the preferred statistical language to R.
- Personally, I got into Python much sooner, because I started as a software engineer, and moved into data science and machine learning. So after taking CS, and programming in Java and C for a few years, python came much more naturally.
- But still - a lot of people who are data-science first (and they have an additional skills to the kind of hybrid that I am) like and prefer R, and they can use it in a specialized way and get good results.
- Personally, I’m going to stick with python, because there’s so many statistical libraries yet to learn, and it’s served me well thus far.
- The language I’ve used most in recent years, Scala, is surprisingly down at 31 - not even close!
- related: **[https://www.zdnet.com/article/programming-languages-python-predicted-to-overtake-c-and-java-in-next-4-years/](https://www.zdnet.com/article/programming-languages-python-predicted-to-overtake-c-and-java-in-next-4-years/)**

**Michael #3:** [**macOS deprecates Python 2, will stop shipping it (eventually)**](https://developer.apple.com/documentation/macos_release_notes/macos_10_15_beta_release_notes#3318257)

- via Dan Bader, on the heels of WWDC 2019
- “Future versions of macOS won’t include scripting language runtimes by default”
- Contrast this with Windows just now starting to ship with Python 3
- In the same announcement: 
- “Use of Python 2.7 isn’t recommended as this version is included in macOS for compatibility with legacy software. Future versions of macOS won’t include Python 2.7. Instead, it’s recommended that you run `python3` from within Terminal. (51097165)”
- Also has impact wider than “us”. E.g. No Ruby or Perl, means home brew doesn’t install easily which is how we get Python 3!

**Brian #4:** [**Pythonic Ways to Use Dictionaries**](http://inventwithpython.com/blog/2019/06/05/pythonic-ways-to-use-dictionaries/)

- Al Sweigart
- A few pythonic uses of dictionaries that are not obvious to new people.
- Use `get()` and `setdefault()` with Dictionaries
	- `get(key, default=<something>)` allows you to read a key without checking for it’s existence beforehand.
	- `setdefault(key, default=<something>)` is a bit of a strange duck but still useful. Set the value of something if it doesn’t exist yet.
- Python Uses Dictionaries Instead of a Switch Statement
	- Just do it a few times to get the hang of it. Then it becomes natural.
- Michael's switch addition for Python: [**https://github.com/mikeckennedy/python-switch**](https://github.com/mikeckennedy/python-switch) 

**Max #5:** [**Things you are probably not using in Python 3 But Should**](https://datawhatnow.com/things-you-are-probably-not-using-in-python-3-but-should/)

- This is from Datawhatnow.com
- This is particularly relevant for me, since I used python legacy at Foursquare for many years, and now coming back to it taking another look at python v3.
- One that looks very useful is f-Strings where you can put the variable name in braces in a string and just have it replaced. I’ve seen things like this in other languages - notably PHP and most front-end scripts. Makes the code very readable.
	- Except I know I’m going to screw up by leaving out that stray “f” in front of the string. It should almost be automatic, because how often are you putting these variable names in braces?
- Another thing I didn’t know python 3 had - again I’m kind of just get started with python 3 is enumerations.
- I’ve been using Enums for years in scala (really case classes) to make my code WAY more readable. Will keep that in mind when developing in python 3.

**Michael #6:** **Have a time machine? C++ would get the Python 2 → 3 treatment too**

- via James Small
- In [**a recent CppCast interview**](http://cppcast.com/2019/05/herb-sutter/), Herb Sutter describes how he would change C/C++ types if he could go back in time.
- This is almost exactly how things were changed from Python 2 to Python 3 (str split into Unicode strings and byte arrays)
- So my question to you two is: Why was the transition so hard? Was it just habit and stubbornness? What could the PSF have done?


**Extras**

Michael:

- [**pip install mystery**](https://github.com/DivoK/mystery)
	- by Divo Kaplan
	- A random Python package every time.
	- Mystery is a Python package that is instantiated as a *different* package every time you install it!
	- Inspired by one of our episodes
- Get our effective pycharm book bundle with the courses over at [**effectivepycharm.com**](https://effectivepycharm.com/)

Brian:

- [**Python 3.8.0b1**](https://www.python.org/downloads/release/python-380b1/)
	- If you support a package, please test.

Max: 

- [**The Local Maximum**](https://www.localmaxradio.com/)
	- Weekly Podcast that covers both the theoretical issues in probability theory, philosophy, and machine learning, but then applies it in a practical way to things like current events and product development.
	- For example, a few weeks ago I did a show on how to estimate the probably of an event that has never occurred
	- We also cover things like Apple’s decision to breakup iTunes, how the internet is shaping up in places like Cuba, and the controversy around YouTube’s recommendation algorithm.

**Jokes** 

MK: There are only two hard problems in Computer Science: cache invalidation, naming things and off-by-one-errors.
