# Python Bytes 197
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [Test & Code](https://testandcode.com/) Podcast

**Michael #1:** [**Structured concurrency in Python with AnyIO**](https://mattwestcott.co.uk/blog/structured-concurrency-in-python-with-anyio)

- [AnyIO](https://github.com/agronholm/anyio) is a Python library providing structured concurrency primitives on top of asyncio.
- **Structured concurrency** is a [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) aimed at improving the clarity, quality, and development time of a [computer program](https://en.wikipedia.org/wiki/Computer_program) by using a structured approach to [concurrent programming](https://en.wikipedia.org/wiki/Concurrent_computing). The core concept is the encapsulation of concurrent threads of execution (here encompassing kernel and userland threads and processes) by way of control flow constructs that have clear entry and exit points and that ensure all spawned threads have completed before exit. — Wikipedia
- The best overview is [Notes on structured concurrency](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) by Nathaniel Smith (or his [video](https://www.youtube.com/watch?v=oLkfnc_UMcE) if you prefer).
- Python has three well-known concurrency libraries built around the async/await syntax: [asyncio](https://docs.python.org/3/library/asyncio.html), [Curio](https://github.com/dabeaz/curio), and [Trio](https://github.com/python-trio/trio). (WHERE IS [unsync](https://asherman.io/projects/unsync.html)?!?! 🙂 )
- Since it's the default, the overwhelming majority of async applications and libraries are written with asyncio.
- The second and third are attempts to improve on asyncio, by David Beazley and Nathaniel Smith respectively
- The [AnyIO](https://github.com/agronholm/anyio) library by Alex Grönholm describes itself as follows:
    > an asynchronous compatibility API that allows applications and libraries written against it to run unmodified on asyncio, curio and trio.

Example:

```
    import anyio
    
    async def task(n):
        await anyio.sleep(n)
    
    async def main():
        try:
            async with anyio.create_task_group() as tg:
                await tg.spawn(task, 1)
                await tg.spawn(task, 2)
        finally:
            # e.g. release locks
            print('cleanup')
    
    anyio.run(main)
```

- AnyIO also provides other primitives to replace the native asyncio ones if you want to benefit from structured concurrency's cancellation semantics:
- [Synchronisation primitives (locks, events, conditions)](https://anyio.readthedocs.io/en/latest/synchronization.html)
- [Streams (similar to queues)](https://anyio.readthedocs.io/en/latest/streams.html)
- [Timeouts (e.g.](https://anyio.readthedocs.io/en/latest/api.html#timeouts-and-cancellation) `[move_on_after](https://anyio.readthedocs.io/en/latest/api.html#timeouts-and-cancellation)`[,](https://anyio.readthedocs.io/en/latest/api.html#timeouts-and-cancellation) `[fail_after](https://anyio.readthedocs.io/en/latest/api.html#timeouts-and-cancellation)`[)](https://anyio.readthedocs.io/en/latest/api.html#timeouts-and-cancellation)
- [... and more](https://anyio.readthedocs.io/en/latest/api.html)

**Brian #2:** [**The Consortium for Python Data API Standards**](https://data-apis.org/blog/announcing_the_consortium/)

- One unintended consequence of the advances in multiple frameworks for data science, machine learning, deep learning and numerical computing is fragmentation and differences in common function signatures.
- The Consortium for Python Data API Standards aims to tackle this fragmentation by developing API standards for arrays (a.k.a. tensors) and dataframes.  
- They intend to work with library maintainers and the community and have a review process.
- One example of the problem, “mean”. Five different interfaces over 8 frameworks:

```
    numpy:         mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)
    dask.array:    mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)
    cupy:          mean(a, axis=None, dtype=None, out=None, keepdims=False)
    jax.numpy:     mean(a, axis=None, dtype=None, out=None, keepdims=False)
    mxnet.np:      mean(a, axis=None, dtype=None, out=None, keepdims=False)
    sparse:        s.mean(axis=None, keepdims=False, dtype=None, out=None)
    torch:         mean(input, dim, keepdim=False, out=None)
    tensorflow:    reduce_mean(input_tensor, axis=None, keepdims=None, name=None,   
                               reduction_indices=None, keep_dims=None)
```

- They are going to start with array API
- Then dataframes
- Also, it’s happening fast, hoping to make traction in next few months.


**Michael #3:** [**Ask for Forgiveness or Look Before You Leap?**](https://switowski.com/blog/ask-for-permission-or-look-before-you-leap)

- via PyCoders
- Think C++ style vs Python style of error handling 
- Or any exception-first/only language vs. some hybrid thing
- If you “look before you leap”, you first check if everything is set correctly, then you perform an action.
- Example:

```
    from pathlib import Path
    if Path("/path/to/file").exists():
        ...
```

- With “ask for forgiveness,” you don’t check anything. You perform whatever action you want, but you wrap it in a `try/catch` block.

```
    try:
        with open("path/to/file.txt", "r") as input_file:
            return input_file.read()
    except IOError:
        # Handle the error or just ignore it
```

- Their example, “Look before you leap” is around 30% slower (155/118≈1.314). Testing for subclass basically with no errors
- But if there are errors: The tables have turned. “Ask for forgiveness” is now over **four times** as slow as “Look before you leap” (562/135≈4.163). That’s because this time, our code throws an exception. And **handling exceptions is expensive**.
- If you expect your code to fail often, then “Look before you leap” might be much faster.
- Michael’s counter example: [gist.github.com/mikeckennedy/00828db1d49d2cd2dac8fa0295e54c23](https://gist.github.com/mikeckennedy/00828db1d49d2cd2dac8fa0295e54c23)


**Brian #4:** [**myrepos**](https://myrepos.branchable.com/)

- “You have a lot of version control repositories. Sometimes you want to update them all at once. Or push out all your local changes. You use special command lines in some repositories to implement specific workflows. Myrepos provides a `mr` command, which is a tool to manage all your version control repositories.”
- Run `mr register` for all repos under a shared directory.
- Then be able to do common operations on a subtree of repos, like `mr status`, `mr update`, `mr diff`, or really anything.
- See also: [**Maintaining Multiple Python Projects With myrepos**](https://adamj.eu/tech/2020/04/02/maintaining-multiple-python-projects-with-myrepos/) **-** Adam Johnson


**Michael #5:** [**A deep dive into the official Docker image for Python**](https://pythonspeed.com/articles/official-python-docker-image/)

- by [Itamar Turner-Trauring](mailto:itamar@pythonspeed.com), via PyCoders
- Wait, there’s [an official Docker image](https://hub.docker.com/_/python) for Python
- The base image is Debian GNU/Linux 10, the current stable release of the Debian distribution, also known as Buster because Debian names all their releases after characters from Toy Story
- Next, environment variables are added: `ENV PATH /usr/local/bin:$PATH`
- Next, the locale is set: `ENV LANG C.UTF-8` 
- There’s also an environment variable that tells you the current Python version: `ENV PYTHON_VERSION 3.8.5` 
- In order to run, Python needs some additional packages (the dreaded certificates, etc)
- Next, a compiler toolchain is installed, Python source code is downloaded, Python is compiled, and then the unneeded Debian packages are uninstalled. Interestingly, The packages—`gcc` and so on—needed to compile Python are removed once they are no longer needed.
- Next, `/usr/local/bin/python3` gets an alias `/usr/local/bin/python`, so you can call it either way
- the `Dockerfile` makes sure to include that newer `pip`
- Finally, the Dockerfile specifices the entrypoint: `CMD ["python3"]` Means docker run launches into the REPL:
    
```
    $ docker run -it python:3.8-slim-buster
    Python 3.8.5 (default, Aug  4 2020, 16:24:08)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
```

**Brian #6:** **“Only in a Pandemic” section**
[**nannernest: Optimal Peanut Butter and Banana Sandwiches**](https://www.ethanrosenthal.com/2020/08/25/optimal-peanut-butter-and-banana-sandwiches/)

- Ethan Rosenthal
- Computer vision, deep learning, machine learning, and Python come together to make sandwiches.
- Just a really fun read about problems called “nesting” or “packing” and how to apply it to banana slices and bread.

Extras:

Brian:

- [Patreon link](https://www.patreon.com/pythonbytes)

Michael:

- Sign up for the free [Excel to Python webcast on Sept 29](https://www.crowdcast.io/e/tips-and-techniques-to-move-from-excel-to-python).
- Check out the early access version of [the memory course](https://talkpython.fm/mem).

Joke

via [Eduardo Orochena](https://twitter.com/EduardoOrochena/status/1291427366867263489)

![](https://paper-attachments.dropbox.com/s_5445676B90B80E929E8439B748DE93536CF760170EF956F45AA1F48A2AD952B3_1598468369037_EelADOtWkAEVZ6o.png)
