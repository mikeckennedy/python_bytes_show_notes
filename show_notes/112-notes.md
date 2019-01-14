# Python Bytes 112
Sponsored by [https://pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Brian #1:** [**nbgrader**](https://github.com/jupyter/nbgrader)

- [**nbgrader: A Tool for Creating and Grading Assignments in the Jupyter Notebook**](https://jose.theoj.org/papers/10.21105/jose.00032)
	- The Journal of Open Source Education, paper accepted 6-Jan-2019
- [nbgrader documentation, including a intro video](https://nbgrader.readthedocs.io/en/stable/)
- From the JOSE article:
	- “nbgrader is a flexible tool for creating and grading assignments in the Jupyter Notebook (Kluyver et al., 2016). nbgrader allows instructors to create a single, master copy of an assignment, including tests and canonical solutions. From the master copy, a student version is generated without the solutions, thus obviating the need to maintain two separate versions. nbgrader also automatically grades submitted assignments by executing the notebooks and storing the results of the tests in a database. After auto-grading, instructors can manually grade free responses and provide partial credit using the formgrader Jupyter Notebook extension. Finally, instructors can use nbgrader to leave personalized feedback for each student’s submission, including comments as well as detailed error information.”
- CS teaching methods have come a long ways since I was turning in floppies and code printouts.


Michael #2: [profanity-check](https://github.com/vzhou842/profanity-check)

- A fast, robust Python library to check for offensive language in strings.
- `profanity-check` uses a linear SVM model trained on 200k human-labeled samples of clean and profane text strings.
- Making `profanity-check` both robust and extremely performant
- Other libraries like [profanity-filter](https://github.com/rominf/profanity-filter) use more sophisticated methods that are much more accurate but at the cost of performance.
	- profanity-filter runs in 13,000ms vs 24ms for profanity-check in a benchmark
- Two ways to use:
	- `predict(text)` → 0 or 1 (1 = bad)
	- `predict_prob(text)` → [0, 1] confidence interval (1 = bad)

**Brian #3**: [**An Introduction to Python Packages for Absolute Beginners**](https://hackernoon.com/pip-install-abra-cadabra-or-python-packages-for-beginners-33a989834975)

- Ever tried to explain the difference between module and package? Between package-in-the-directory-with-init sense and package-you-can-distribute-and-install-with-pip sense? Here’s the article to read beforehand.
- Modules, packages, using packages, installing, importing, and more.
- And that’s not even getting into flit and poetry, etc. But it’s a good place to start for people new to Python.


**Michael #4: Python Dependencies  and IoC**

- via Joscha Götzer
- **Open-closed principle** is at work with these and is super valuable to testing (one of the SOLID principles): *Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification*.
- There is a huge debate around why Python doesn’t need DI or Inversion of Control (IoC), and a quick stackoverflow search yields multiple results along the lines of “python is a scripting language and dynamic enough so that DI/IoC makes no sense”. However, especially in large projects it might reduce the cognitive load and decoupling of individual components
- [**Dependency Injector**](https://github.com/ets-labs/python-dependency-injector)**:** I couldn’t get this one to work on windows, as it needs to compile some C libraries and some Visual Studio tooling was missing that I couldn’t really install properly. The library looks quite promising though, but sort of static with heavy usage of containers and not necessarily pythonic.
- [**Injector**](https://pythonhosted.org/injector/): The library that above mentioned article talks about, a little Java-esque
- [**pinject**](https://github.com/google/pinject): Has been unmaintained for about 5 years, and only recently got new attention from some open source people who try to port it to python3. A product under Google copyright, and looks quite nice despite the lack of python3 bindings. Probably the most feature-rich of the listed libraries.
- [**python-inject**](https://github.com/ivankorobkov/python-inject)**:** I discovered that one while writing this email, not really sure if it’s any good. Nice use of type annotations and testing features
- [**di-py**](https://github.com/telefonicaid/di-py): Only works up to python 3.4, so I’ve also never tried it (I’m one of those legacy python haters, I’m sure you can relate 😄).
- [**Serum**](https://github.com/suned/serum): This one is a little too explicit to my mind. It makes heavy use of context managers (literally with Context(...): everywhere 😉) and I’m not immediately sure how to work with it. In this way, it is quite powerful though. Interesting use of class decorators.
- And now on to my favorite and a repeated recommendation of mine around the internet→  [**Haps**](https://github.com/ekiro/haps): This lesser-known, lightweight library is sort of the new kid on the block, and really simple to use. As some of the other libraries, it uses type annotations to determine the kind of object it is supposed to instantiate, and automatically discovers the required files in your project folder. Haps is very pythonic and fits into apps of any size, helping to ensure modularization as the only dependency of your modules will be one of the types provided by the library. [Pretty good example here](https://github.com/ekiro/haps/blob/master/samples/simple.py).

**Brian #5:** [**A Gentle Introduction to Pandas**](https://medium.com/@wbusaka/a-gentle-introduction-to-pandas-5ed17421a59d)

- Really a gentle introduction to the Pandas data structures `Series` and `DataFrame`.
- Very gentle, with console examples.
- Create series objects:
	- from an array
	- from an array, and change the indexing
	- from a dictionaries
	- from a scalar, cool. didn’t know you could do that
- Accessing elements in a series
- DataFrames
	- sorting, slicing
	- selecting by label, position
	- statistics on columns
	- importing and exporting data

 
**Michael #6:** [**Don't use the greater than sign in programming**](http://llewellynfalco.blogspot.com/2016/02/dont-use-greater-than-sign-in.html)

- One simple thing that comes up time and time again is the use of the greater than sign as part of a conditional while programming. Removing it cleans up code.
- Let's say that I want to check that something is between 5 and 10. 
- There are many ways I can do this

```
    x > 5 and 10 > x
    5 < x and 10 > x
    x > 5 and x < 10
    10 < x and x < 5
    x < 10 and x > 5
    x < 10 and 5 < x
```

- Sorry, one of those is incorrect. Go ahead and find out which one
- If you remove the use of the greater than sign then only 2 options remain
	- `x < 10 and 5 < x`
	- `5 < x and x < 10`
	- The last is nice because x is **literally between** 5 and 10
- There is also a nice way of expressing that *"x is outside the limits of 5 and 10”*
	- `x < 5 or 10 < x`
	- Again, this expresses it nicely because x is **literally outside** of 5 to 10.
- Interesting comment: What is cleaner or easier to read comes down to personal taste. But how to express "all numbers greater than 1" without '>'? 
	- ans:  `1 < allNumbers`

Extras:

Michael

- [Teaching Python podcast](https://www.teachingpython.fm/) by Kelly Paredes & Sean Tibor
- [Github private repos (now free)](https://blog.github.com/changelog/2019-01-08-pricing-changes/)
- [EuroPython 2019 announced](https://ep2019.europython.eu/)
- [South African AWS Data Center coming](https://www.allthingsdistributed.com/2018/10/an-aws-region-is-coming-to-south-africa.html) (via William H.)
- [Pandas is dropping legacy Python support](https://twitter.com/jakevdp/status/1080583192803823616) any day now

Joke: [Harry Potter Parser Tongue](https://twitter.com/Spirix3/status/1080205170183716865) via Nick Spirit
