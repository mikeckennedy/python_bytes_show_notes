Welcome to Python bytes. Episode 24, recorded May 2, 2017. This episode is sponsored by rollbar: [https://rollbar.com/pythonbytes](https://rollbar.com/pythonbytes)

**Brian #1: [Learning Python Series by Doug Ferrell](https://dbader.org/blog/python-intro-statements-variables-and-loops), published on dbader.org**

- Doug Ferrell wrote for [Robotics and Beyond](https://roboticsandbeyond.org/) , a STEM educational space
- This is part 1: **Let’s Program with Python: Statements, Variables, and Loops**

**Michael #2:** [**Geeking out in your older years**](http://www.pgbovine.net/publications/older-adults-learning-programming_CHI-2017.pdf)

- Over 500 respondents on [http://pythontutor.com/](http://pythontutor.com/)
- Age group: 60-85
- Opportunities: Help older adults become software dev proficient to
  - Connect with their grand children
  - Fill the growing tech / teacher gap
  - Mentor others
  - Keep mentally active
  - Pursue their hobbies
- Used MOOCs, online courses, books, and more to learn
- Felt somewhat isolated and disconnected
  - How could we all help? Or help them help themselves as a group?

**Brian #3:** **Local package store**

- Not a story, just something I used for the plane trip that didn’t know worked before.
- Stops my quest for a easy to use local pypi server.
- Download without installing

  `$ cd /tmp/wheelhouse` 
  `$ python3.6 -m pip download <somePackage>` 

- Then, later, probably within a virtual env

  `$ python3.6 -m pip install --no-index --find-links=/tmp/wheelhouse somePackage`  

- **Does it work with requirements files? Yes!**

`pip3 download -r /full_path_to/requirements.txt`

**Sponsored by rollbar** [https://rollbar.com/pythonbytes](https://rollbar.com/pythonbytes)

- **Adding the Rollbar Python SDK is as easy as `pip install rollbar`.**
- **Make sure to check out Rollbar at Pycon. Grab swag and get a product demo.** 
- Visit [https://rollbar.com/pythonbytes](https://rollbar.com/pythonbytes) and get the get the Bootstrap Plan free for free
  - 100,000 rollbar events / mo, 180 days retention

**Michael #4:** [**Modifying the Python language in 6 minutes**](https://hackernoon.com/modifying-the-python-language-in-7-minutes-b94b0a99ce14)

- Anthony Shaw
- I’m writing my findings on how CPython works and show you how easy it is to modify the Python syntax.
- I’m going to show you how to add a new **feature** to the Python syntax.
- **Level 1: PEPs**
- **Level 2: Grammar**
- The [Grammar](https://github.com/python/cpython/blob/v3.6.1/Grammar/Grammar) file is simple text file describing all the elements of the Python language. This is used by not just CPython, but other implementations like PyPy to keep consistency and agree on the types of language semantics.
  - New statements
      - `incr_stmt: '++'`
      - `decr_stmt: '--'`
- **Level 3 : Lexer:** There are four steps that Python takes when you hit return: lexing, parsing, compiling, and interpreting. Lexing is breaking the line of code you just typed into tokens.
- **Level 4 : Parser**: The parser takes those tokens and generates a structure that shows their relationship to each other. For Python and many other languages, this is the Abstract Syntax Tree (or AST). 
- **Level 5: Compiler:**  The compiler then takes the syntax tree and ‘visits’ each branch, the CPython compiler has a method for visiting a statement, called `compile_visit_stmt` which is just a big switch statement looking at the statement kind.
- [https://github.com/tonybaloney/cpython/commit/fd7c20c3a3a02b4f2dae8ec7a90448627aa0d757](https://github.com/tonybaloney/cpython/commit/fd7c20c3a3a02b4f2dae8ec7a90448627aa0d757)


**Brian #5:** [**colorful**](https://github.com/timofurrer/colorful)

- “Terminal string styling done right, in Python”
- Add color to terminal applications with a pretty easy to read syntax

**Michael #6:** [**Five steps to add the _bling_ factor your Python package**](https://www.reddit.com/r/Python/comments/65v1kx/five_steps_to_add_the_bling_factor_your_python/) ****

- by Tjelvar Olsson
- Step 1: Host the documentation on readthedocs
- Step 2: Set up continuous integration testing on Travis Ci
- Step 3: Calculate your code coverage using Codecov
- Step 4: Upload your Package to PyPi
- Step 5: Add badges to your project’s README file
