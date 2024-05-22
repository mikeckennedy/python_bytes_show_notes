# Python Bytes 184
Sponsored by **DigitalOcean**: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean) - $100 credit for new users to build something awesome.

**Michael #1:** [**Waiting in asyncio**](https://hynek.me/articles/waiting-in-asyncio/)

- by  [Hynek Schlawack](https://hynek.me/)
- One of the main appeals of using Python’s `asyncio` is being able to fire off many coroutines and run them concurrently. How many ways do you know for waiting for their results?
- The simplest case is to *await* your coroutines:
```
    result_f = await f()
    result_g = await g()
```
- Drawbacks:
	1. The coroutines do **not** run concurrently. `g` only starts executing after `f` has finished.
	2. You can’t cancel them once you started awaiting.
-  `[asyncio.Task](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task)`[s](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task) wrap your coroutines and get independently *scheduled* for execution by the event loop whenever you yield control to it
```
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g())
    
    await asyncio.sleep(0.1) # <- f() and g() are already running!
    result_f = await task_f
    result_g = await task_g
```

- Your tasks now run *concurrently* and if you decide that you don’t want to wait for `task_f` or `task_g` to finish, you can cancel them using `task_f.cancel()`
- `[asyncio.gather()](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)` takes 1 or more awaitables as `*args`, wraps them in tasks if necessary, and waits for all of them to finish. Then it returns the **results** of all awaitables **in the same order**
```
    result_f, result_g = await asyncio.gather(f(), g())
```
- `[asyncio.wait_for()](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for)` allows for passing a time out
- A more elegant approach to timeouts is the [*async-timeout*](https://pypi.org/project/async-timeout/) [package](https://pypi.org/project/async-timeout/) on PyPI. It gives you an asynchronous context manager that allows you to apply a *total* timeout even if you need to execute the coroutines **sequentially**
```
    async with async_timeout.timeout(5.0):
        await f()
        await g()
```

- `[asyncio.as_completed()](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed)` takes an iterable of awaitables and returns an iterator that yields `[asyncio.Future](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future)`s in the order the awaitables are done
```
    for fut in asyncio.as_completed([task_f, task_g], timeout=5.0):
        try:
            await fut
            print("one task down!")
        except Exception:
            print("ouch")
```
- Michael’s [Async Python course](http://talkpython.fm/async).

**Brian #2:** **virtualenv is faster than venv**

- [virtualenv docs](https://virtualenv.pypa.io/en/latest/):
    “`virtualenv` is a tool to create isolated Python environments. Since Python `3.3`, a subset of it has been integrated into the standard library under the [venv module](https://docs.python.org/3/library/venv.html). The `venv` module does not offer all features of this library, to name just a few more prominent:
	- is slower (by not having the `app-data` seed method),
	- is not as extendable,
	- cannot create virtual environments for arbitrarily installed python versions (and automatically discover these),
	- is not upgrade-able via [pip](https://pip.pypa.io/en/stable/installing/),
	- does not have as rich programmatic API (describe virtual environments without creating them).”
- pro: faster: under 0.5 seconds vs about 2.5 seconds
- con: the `--prompt` is weird. I like the parens and the space, and 3.9’s magic “.” option for prompt to name it after the current directory.
- pro: the pip you get in your env is already updated
- conclusion: 
	- I’m on the fence for my own use. Probably leaning more toward keeping built in. But not having to update pip is nice.
	- For teaching, I’ll stick with the built in `venv`.
	- The “extendable” and “has an API” parts really don’t matter much to me. 

```
    $ time python3.9 -m venv venv --prompt .
    
    real 0m2.698s
    user 0m2.055s
    sys 0m0.606s
    $ source venv/bin/activate
    (try) $ deactivate
    $ rm -fr venv
    $ time python3.9 -m virtualenv venv --prompt "(try) "
    ...
    real 0m0.384s
    user 0m0.202s
    sys 0m0.255s
    $ source venv/bin/activate
    (try) $
```

**Michael #3:** [Latency in Asynchronous Python](https://nullprogram.com/blog/2020/05/24/)

- Article by Chris Wellons
- Was debugging a misbehaving Python program that makes significant use of [Python’s asyncio](https://docs.python.org/3/library/asyncio.html).
- The program would eventually take very long periods of time to respond to network requests.
- The program’s author had made a couple of fundamental mistakes using asyncio.
- Scenario:
	- Have a “heartbeat” async method that beats once every ms:
		- heartbeat delay = 0.001s
		- heartbeat delay = 0.001s
		- …
	- Have a computational amount of work that takes 10ms
	- Need to run a bunch of these computational things (say 200).
	- But starting the heartbeat blocks the asyncio event loop
	- See my example at https://gist.github.com/mikeckennedy/d9ac5a600f91971c6933b4f41a8df480
- [Unsync](https://github.com/alex-sherman/unsync) fixes this and improves the code! Here’s my example: https://gist.github.com/mikeckennedy/f23b9b5abd9452cdc8b3bacaf1c3da20
- Need to limit the number of “active” tasks at a time.
- **Solving it with a job queue:** Here’s what does work: a [job queue](https://docs.python.org/3/library/asyncio-queue.html). Create a queue to be populated with coroutines (not tasks), and have a small number of tasks run jobs from the queue.


**Brian #4:** [**How to Deprecate a PyPI Package**](https://www.dampfkraft.com/code/how-to-deprecate-a-pypi-package.html)

- Paul McCann, [@polm23](https://twitter.com/polm23)
- A collection of options of how to get people to stop using your package on PyPI. Also includes code samples ore example packages that use some of these methods.
- Options:
	- **Add deprecation warnings:** Useful for parts of your package you want people to stop using, like some of the API, etc.
	- **Delete it:** Deleting a package or version ok for quick oops mistakes, but allows someone else to grab the name, which is bad. Probably don’t do this.
	- **Redirect shim:** Add a setup.py shim that just installs a different package. Cool idea, but a bit creepy. 
	- **Fail during install:** Intentionally failing during install and redirecting people to use a different package or just explain why this one is dead. I think I like this the best.


**Michael #5:**  [**Another progress bar library: Enlighten**](https://pypi.org/project/enlighten/)

- by Avram Lubkin
- A few unique features:
- **Multicolored progress bars - It's like many progress bars in one!** You could use this in testing, where red is failure, green is success, and yellow is an error. Or maybe when loading something in stages such as loaded, started, connected, and the percentage of the bar for each color changes as the services start up. Has 24-bit color support.
- **Writing to stdout and stderr just works!** There are a lot of progress bars. Most of them just print garbage if you write to the terminal when they are running.
- **Automatically handles resizing! (except on Windows)**
- See the animation on the home page.


**Brian #6:** [**Code Ocean**](https://codeocean.com/)

- Contributed by Daniel Mulkey
- From Daniel “a peer-reviewed journal I read (SPIE's Optical Engineering) has a recommended platform for associating code with your article. It looks like it's focused on reproducibility in science. “
- Code Ocean is a research collaboration platform that supports researchers from the beginning of a project through publication.
- This is a paid service, but has a free tier.
- Supports:
	- C/C++
	- Fortran
	- Java 
	- Julia
	- Lua
	- MATLAB
	- Python (including jupyter) (why is this listed so low? should be at the top!) 
	- R
	- Stata
- From the “About Us” page: 
	- “We built a platform that can help give researchers back 20% of the time they spend troubleshooting technology in order to run and reproduce past work before completing new experiments.”
	- “Code Ocean is an open access platform for code and data where users can develop, share, publish, and download code through a web browser, eliminating the need to install software on personal computers. Our mission is to make computational research easier, more collaborative, and durable.”


    

Extras:

Brian:

- [Python 3.9.0b1 is available for testing](https://pythoninsider.blogspot.com/2020/05/python-390b1-is-now-available-for.html)

Michael:

- SpaceX launch, lots of Python in action.

Joke:

- Sent over by [Steven Howell](https://twitter.com/StevenCHowell)
- [https://twitter.com/tecmint/status/1260251832905019392](https://twitter.com/tecmint/status/1260251832905019392)


- From Bert, [https://twitter.com/schilduil/status/1264869362688765952](https://twitter.com/schilduil/status/1264869362688765952)
- But modified for my own experience:
- “What does pyjokes have in common with Java? It gets updated all the time, but never gets any better.”

