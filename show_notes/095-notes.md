# Python Bytes 95
Sponsored by DataDog -- [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**dataset: databases for lazy people**](https://dataset.readthedocs.io/en/latest/)

- **dataset** provides a simple abstraction layer removes most direct SQL statements without the necessity for a full ORM model - essentially, databases can be used like a JSON file or NoSQL store.
- A simple data loading script using **dataset** might look like this:

```
    import dataset
    
    db = dataset.connect('sqlite:///:memory:')
    
    table = db['sometable']
    table.insert(dict(name='John Doe', age=37))
    table.insert(dict(name='Jane Doe', age=34, gender='female'))
    
    john = table.find_one(name='John Doe')
```

**Michael #2:** [**CuPy GPU NumPy**](https://cupy.chainer.org/)

- A NumPy-compatible matrix library accelerated by CUDA
- How many cores does a modern GPU have?
- CuPy's interface is highly compatible with NumPy; in most cases it can be used as a drop-in replacement.
- You can easily make a custom CUDA kernel if you want to make your code run faster, requiring only a small code snippet of C++. CuPy automatically wraps and compiles it to make a CUDA binary
- PyCon 2018 presentation: [Shohei Hido - CuPy: A NumPy-compatible Library for GPU](https://www.youtube.com/watch?v=MAz1xolSB68)
- Code  example

```
    >>> # This will run on your GPU!
    >>> import cupy as np # This is the only non-NumPy line
    
    >>> x = np.arange(6).reshape(2, 3).astype('f')
    >>> x
    array([[ 0.,  1.,  2.],
           [ 3.,  4.,  5.]], dtype=float32)
    >>> x.sum(axis=1)
    array([  3.,  12.], dtype=float32)           
```


**Brian #3:** [**Automate Python workflow using pre-commits**](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/)

- We covered pre-commit in [episode 84](https://pythonbytes.fm/84), but I still had trouble getting my head around it.
- This article by LJ Miranda does a great job with the workflow introduction and configuration necessary to get pre-commit working for black and flake8.
- Includes a nice visual of the flow.
- Demo of it all in action with a short video.

**Michael #4:** [**py-spy**](https://github.com/benfred/py-spy)

- Sampling profiler for Python programs 
- Written by [Ben Frederickson](https://twitter.com/benfrederickson)
- Lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way.
- Written in Rust for speed
- Doesn't run in the same process as the profiled Python program
- Does NOT it interrupt the running program in any way.
- This means Py-Spy is safe to use against production Python code.
- The default visualization is a top-like live view of your python program
- [**How does py-spy work?**](https://github.com/benfred/py-spy#how-does-py-spy-work) Py-spy works by directly reading the memory of the python program using the [process_vm_readv](http://man7.org/linux/man-pages/man2/process_vm_readv.2.html) system call on Linux, the [vm_read](https://developer.apple.com/documentation/kernel/1585350-vm_read?language=objc) call on OSX or the [ReadProcessMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680553(v=vs.85).aspx) call on Windows.

**Brian #5:** [**SymPy is a Python library for symbolic mathematics**](https://docs.sympy.org/latest/tutorial/intro.html)

- “Symbolic computation deals with the computation of mathematical objects symbolically. This means that the mathematical objects are represented exactly, not approximately, and mathematical expressions with unevaluated variables are left in symbolic form.”
- example:

```
    >>> integrate(sin(x**2), (x, -oo, oo))
    √2⋅√π
    ─────
      2
```

- examples on site are interactive so you can play with it without installing anything.

**Michael #6:** [**Starlette ASGI web framework**](https://www.starlette.io/)

- The little ASGI framework that shines.
- It is ideal for building high performance asyncio services, and supports both HTTP and WebSockets.
- Very flask-esq
- Can use 
	- [ultrajson](http://Ultra fast JSON decoder and encoder written in C with Python bindings) (ujson package)
	- aiofiles for file responses
- Run using uvicorn

Extras:

**Michael:** [**PyCon 2019**](https://us.pycon.org/2019/) **dates out, put them on your calendar!**

- Tutorials: May 1-2 • Wednesday, Thursday
- Talks and Events: May 3–5 • Friday, Saturday, Sunday
- Sprints: May 6–9 • Monday through Thursday

**Listener follow up on git pre-commit hooks util:** [**pre-commit package**](https://pre-commit.com/)

- Matthew Layman, [@mblayman](https://twitter.com/mblayman)
- Heard the discussion about Git commit hooks at the end. I wanted to bring up pre-commit as an interesting project (written in Python!) that's useful for Git commit hooks.
- tl;dr:
	- $ pip install pre-commit
	- $ ... create a .pre-commit-config.yaml
	- $ pre-commit install  # This is a one time operation.
- pre-commit's job is to manage a project's Git commit hooks. We use this on my team at work and the devs only need to run `pre-commit install`. This saves us from a bunch of failing CI builds where flake8 or other code style checks would fail.
- We use pre-commit to run flake8 and black before allowing a commit to proceed. Some projects have a pre-commit configuration to use right out of the box (e.g., black [https://github.com/ambv/black#version-control-integration](https://github.com/ambv/black#version-control-integration)).

**Listener: You don't need that (pattern)**

- John Tocher
- PyCon AU [Talk Called "You don't need that](https://2018.pycon-au.org/talks/45184-you-dont-need-that/)” - by Christopher Neugebauer,  it was an interesting take on why with a modern and powerful language like python, you may not need the conventionally described design patterns, ala the "Gang of four".

