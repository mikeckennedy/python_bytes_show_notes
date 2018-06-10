# Python Bytes 81
Sponsored by digitalocean

**Brian #1: Learning about Machine Learning**

- [**hello tensorflow**](https://hello-tensorflow.glitch.me/)
	- one pager site with a demo of machine learning in action.
	- “**Machine Learning (ML)** is the dope new thing that everyone's talking about, because it's really good at learning from data so that it can predict similar things in the future.”
	- Includes a graphical demo of ML trying to learn the correct coefficients to a polynomial.
- [Google Provides Free Machine Learning Course For All](https://www.technotification.com/2018/04/google-free-machine-learning.html)
	- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/) (MLCC) is a free 15 hours course that is divided into 25 lessons. It provides exercises, interactive visualizations, and instructional videos. These can help in learning machine learning concepts.
	- 40 exercises, 25 lessons, 15 hours, case studies, interactive visualizations

**Michael #2:** [**Making your C library callable from Python by wrapping it with Cython**](https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3)

- Article by Stav Shamir
- Cython is known for its ability to increase the performance of Python code. Another useful feature of Cython is making existing C functions callable from within (seemingly) pure Python modules.
- Need to directly interact from Python with a small C library

Want to wrap this C function?


    void hello(const char *name) {
        printf("hello %s\n", name);
    }

Just install Cython and write this:

    cdef extern from "examples.h":
        void hello(const char *name)
    
    def py_hello(name: bytes) -> None:
        hello(name)

Then create a setup file (details in article), call `python setup.py build_ext --inplace` and you’re good to go.

**Brian #3:** [**Taming Irreversibility with Feature Flags (in Python)**](https://www.vinta.com.br/blog/2018/taming-irreversibility-feature-flags-python/)

- “Feature Flags are a very simple technique to make features of your application quickly toggleable. The way it works is, everytime we change some behavior in our software, a logical branch is created and this new behavior is only accessible if some specific configuration variable is set or, in certain cases, if the application context respects some rules.”

```
    def my_function():
        if is_feature_active('feature_one'):
            do_something()
        else:
            do_something_else()
```

- Benefits
	- Improving team’s response time to bugs. If a new feature causes a bunch of customer problems, just turn it off.
	- Making possible to sync code more frequently. Merge to master with the feature turned off.
	- Having a more fluid feature launching flow. Turn feature on in test/staging server.
	- Validate your features easily with A/B testing, user groups, etc.
- Article discusses:
	- how to implement flags cleanly.
	- measuring success with analytics
	- implementing flags with third party packages and recommends a few.

**Michael #4:** [**pretend: a stubbing library**](https://pypi.org/project/pretend/)

- Heard about this at the end of the pypi episode of Talk Python and wanted to highlight it more.
- Pretend is a library to make stubbing with Python easier.
- Stubbing is a technique for writing tests. A stub is an object that returns pre-canned responses, rather than doing any computation.
- Stubbing is related to mocking, but traditionally with stubs, you don’t care about behavior, you are just concerned with how your system under test responds to certain input data. 
  - However, pretend does include a call recorder feature.
- Nice clean api:

```
    >>> from pretend import stub
    >>> x = stub(country_code=lambda: "US")
    >>> x.country_code()
    'US'
```

```
    >>> from pretend import stub, raiser
    >>> x = stub(func=raiser(ValueError))
    >>> x.func()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "pretend.py", line 74, in inner
        raise exc
    ValueError
```

**Brian #5:** [**The official Flask tutorial**](http://flask.pocoo.org/docs/1.0/tutorial/)

- Has been updated recently.
	- simplified, updated, including the source code for the project.
	- tutorial includes section on testing, including testing with pytest and coverage.
- Flask is part of [Pallets](https://www.palletsprojects.com/), which develops and maintains several projects
	- [Click](https://www.palletsprojects.com/p/click/) — A package for creating beautiful command line interfaces in a composable way
	- [Flask](https://www.palletsprojects.com/p/flask/) — a flexible and popular web development framework
	- [ItsDangerous](https://www.palletsprojects.com/p/itsdangerous/) — cryptographically sign your data and hand it over to someone else
	- [Jinja](https://www.palletsprojects.com/p/jinja/) — a full featured template engine for Python
	- [MarkupSafe](https://www.palletsprojects.com/p/markupsafe/) — a HTML-Markup safe string for Python
	- [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) — a WSGI utility library for Python
- You can now donate to pallets to help with the maintenance costs of these important packages.
	- There’s a donate button on the pallets site that takes you to a PSF page. Therefore, donations are deductible in the US.
  

**Michael #6:** [**An introduction to Python bytecode**](https://opensource.com/article/18/4/introduction-python-bytecode)

- Python is compiled
- Learn what Python bytecode is, how Python uses it to execute your code, and how knowing what it does can help you.
- Python is often described as an interpreted language—one in which your source code is translated into native CPU instructions as the program runs—but this is only partially correct. Python, like many interpreted languages, actually compiles source code to a set of instructions for a virtual machine, and the Python interpreter is an implementation of that virtual machine. This intermediate format is called "bytecode."
- These are your .PYC files

Example:

    def hello()
        print("Hello, World!")


    2           0 LOAD_GLOBAL              0 (print)
                2 LOAD_CONST               1 ('Hello, World!')
                4 CALL_FUNCTION            1


- CPython uses a stack-based virtual machine. That is, it's oriented entirely around stack data structures (where you can "push" an item onto the "top" of the structure, or "pop" an item off the "top").

View and explore using

    import dis
    dis.dis(hello)
