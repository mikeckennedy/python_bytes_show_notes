# Python Bytes 153

Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Michael #1: [**Building a Python C Extension Module**](https://realpython.com/build-python-c-extension-module/)

- Tutorial, learn to use the Python API to write Python C extension modules.
- And
	- Invoke C functions from within Python
	- Pass arguments from Python to C and parse them accordingly
	- Raise exceptions from C code and create custom Python exceptions in C
	- Define global constants in C and make them accessible in Python
	- Test, package, and distribute your Python C extension module
- Extending Your Python Program
	- there may be other lesser-used system calls that are only accessible through C
- Steps: Writing a Python Interface in C
	- Figure out the arguments (e.g. `int fputs(const char *, FILE *)` )
	- Implement in C:

```
    #include Python.h
    static PyObject *method_fputs(PyObject *self, PyObject *args) {
        char *str, *filename = NULL;
        int bytes_copied = -1;
        /* Parse arguments */
        if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
            return NULL;
        }
        FILE *fp = fopen(filename, "w");
        bytes_copied = fputs(str, fp);
        fclose(fp);
        return PyLong_FromLong(bytes_copied);
    }
```

- In line 2, you declare the argument types you wish to receive from your Python code
- line 6, then you’ll see that `PyArg_ParseTuple()` copies into the char*’s
- Write regular C code (fopen, fputs)
- Return: PyLong_FromLong() creates a PyLongObject, which represents an integer object in Python. 
- a few extra functions that are necessary
	- write definitions of your module and the methods it contains
	- Before you can import your new module, you first need to build it. You can do this by using the Python package `distutils`.

**Brian #2:** [**What’s New in Python 3.8 - docs.python.org**](https://docs.python.org/3/whatsnew/3.8.html)

We’ve already talked about the big hitters:

- assignment expressions, (the walrus operator)
- positional only parameters, (the / in the param list)
- f-strings support = for self-documenting expressions and debugging

There are a few more goodies I wanted to quickly mention:
- More async: `python -m asyncio` launches a native async REPL
- More helpful warnings and messages when
	- using `is` and `is not` to compare strings and integers and other types intended to be compared with `==` and `!=`
	- Missing the comma in stuff like `[(1,2) (3,4)]`. Happens all the time with parametrized testing
- you can do iterable unpacking in a yield or return statement
	- `x = (1, 2, 3)`
	- `a, *b = x`
	- `return a, *b` <- this used to be a syntax error
		- you had to do `return (a, *b)`
- New module `importlib.metadata` lets you access things like version numbers or dependent library required version numbers, and cool stuff like that.
	- quite a few more goodies. I run through all my favorites on [testandcode.com/91](http://testandcode.com/91)

Michael #3: [**UK National Cyber Security Centre (NCSC) is warning developers of the risks of sticking with Python 2.7, particularly for library writers**](https://www.zdnet.com/article/uk-cybersecurity-agency-warns-devs-to-drop-python-2-due-to-looming-eol-security-risks/)

- NCSC likens companies continuing to use Python 2 past its EOL to tempting another WannaCry or Equifax incident.
	- [Equifax details](https://www.csoonline.com/article/3444488/equifax-data-breach-faq-what-happened-who-was-affected-what-was-the-impact.html): a vulnerability, dubbed CVE-2017-5638, was discovered in Apache Struts, an open source development framework for creating enterprise Java applications that Equifax, along with thousands of other websites, uses…
- Quote: "If you're still using 2.x, it's time to port your code to Python 3," the NCSC said. "If you continue to use unsupported modules, you are risking the security of your organisation and data, as vulnerabilities will sooner or later appear which nobody is fixing."
- Moreover: "If you maintain a library that other developers depend on, you may be preventing them from updating to 3," the agency added. "By holding other developers back, you are indirectly and likely unintentionally increasing the security risks of others.”
- "If migrating your code base to Python 3 is not possible, another option is to pay a commercial company to support Python 2 for you," the NCSC said.
- NCSC: If you don't migrate, you should expect security incidents
- **Python's popularity makes updating code imperative:** The reason the NCSC is warning companies about Python 2's impending EOL is because of the language's success.

Brian #4: [Pythonic News](https://github.com/sebst/pythonic-news)

- Sebastian A. Steins
- “A Hacker News lookalike written in Python/Django”
- “ powering [https://news.python.sc](https://news.python.sc/)"
- Cool that it’s open source, and on github
- Was submitted to us by Sebastian, and a few others too, so there is excitement.
- It’s like 6 days old and has 153 stars on github, 4 contributors, 18 forks.
- Fun. 

Michael #5: [Deep Learning Workstations, Servers, Laptops, and GPU Cloud](https://lambdalabs.com/)

- GPU-accelerated with TensorFlow, PyTorch, Keras, and more pre-installed. Just plug in and start training. Save up to 90% by moving off your current cloud and choosing Lambda.
- They offer:
    - TensorBook: GPU Laptop for $2,934
    - Lambda Quad: 4x GPU Workstation for $21,108  (yikes!)
    - All in: Lambda Hyperplane: 8x Tesla V100 Server, starting at $114,274
- But compare to: 
    - AWS EC2: p3.8xlarge @ $12.24 per Hour => $8,935 / month

**Brian #6: [Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)**

- A comparison of autopep8, yapf, and black
- Auto formatters are super helpful for teams. They shut down the unproductive arguments over style and make code reviews way more pleasant. People can focus on content, not being the style police.
- We love black. But it might be a bit over the top for some people. Here are a couple of other alternatives.
- [autopep8](https://github.com/hhatto/autopep8) - mostly focuses on PEP8
	- “autopep8 automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.”
- [black](https://github.com/psf/black) - does more
	- doesn’t have many options, but you can alter line length, can turn of string quote normalization, and you can limit or focus the files it sees.
	- does a cool “check that the reformatted code still produces a valid AST that is equivalent to the original.” but you can turn that off with `--fast`
- [yapf](https://github.com/google/yapf) - way more customizable. 
	- Great if you want to auto format to a custom style guide.
	- “The ultimate goal is that the code YAPF produces is as good as the code that a programmer would write if they were following the style guide. It takes away some of the drudgery of maintaining your code.”
- Article is cool in that it shows some sample code and how it’s changed by the different formatters.

Extras:

Michael:

- New courses coming
- Financial Aid Launches for PyCon US 2020!

Joke:

- [American Py Song](https://www.reddit.com/r/Python/comments/dfm2zv/american_py/)

- From Eric Nelson:
	- Math joke. “i is as complex as it gets. jk.”