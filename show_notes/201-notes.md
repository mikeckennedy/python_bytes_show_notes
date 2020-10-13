# Python Bytes 201
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python Testing with pytest**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)

**Michael #1:** [**Under the hood of calling C/C++ from Python**](https://azhpushkin.me/posts/python-c-under-the-hood)

- Basics first: what C compiles to?
	- Each operating system features some exact format to work with. Among the most popular ones are:
	- **ELF** (Executable and Linkable Format), used by most of Linux distros
	- **PE** (Portable Executable), used by Windows
	- **Mach-O** ([Mach](https://en.wikipedia.org/wiki/Mach_(kernel)) object), used by Apple products
- We also need to make our library visible to our programs. An easiest way to do so is to copy it to `/usr/lib/` - default system-wide directory for libraries. Maybe put it in system / system32 on Windows?
- **ctypes: the simplest way**
	- With the shared object compiled, we are ready to call it.
	- Consider ctypes to be the easiest way to execute some C code, because:
    - it’s included in the standard library,
    - writing a wrapper uses plain Python.
	- `lib = ctypes.CDLL(f'/usr/lib/libdullmath.so')`
	- `lib.get_pi`
- For C: You need to be clear about the calling convention (extern “C” for example)
	- Now we can load libraries at runtime, but we are still missing the way to generate correct caller ABI to use external C libraries. Do deal with it, `libffi` was created.
	- [**Libffi**](https://github.com/libffi/libffi) is a portable C library, designed for implementing FFI tools, hence the name. Given structs and functions definitions, it **calculates an ABI of function calls at runtime**.
- A mature approach to improve in this area is **to allow libraries to introduce themselves**. We can oblige every library to define a function named `entry_point`, which will return metadata about functions it contains.
- **Final destination: C/C++ extensions and Python/C API**
	- CPython provides a similar API for implementing C-based extensions: [**“Extending and Embedding the Python Interpreter”**](https://docs.python.org/3/extending/index.html).
        
```
// NOTE: entry point function has dynamic name PyInit_<module>
PyMODINIT_FUNC PyInit_mymath(void)
{
    return PyModule_Create(&mymathmodule);
}
```

- The main difference is that we have to wrap initial C functions with Python-specific ones. CPython interpreter uses its own `PyObject` type internally rather than raw `int`, `char*`, and so on, and we need the wrappers to perform the conversion.
- **Cython, Boost.Python, pybind11 and all all all**
	- The main challenge of writing pure C extensions is a massive amount of boilerplate that needs to be written. Mainly this boilerplate is related to wrapping and unwrapping PyObject. It becomes especially hard if a module introduces its own classes (object types).
	- To solve this issue, a plethora of different tools was created. All of them introduce a certain way to generate wrapping boilerplate automatically. They also provide easy access to C++ code and advanced tools for the compilation of extensions.
	- Examples
	- [aiohttp](https://github.com/aio-libs/aiohttp) - asyncio web framework that uses Cython for HTTP parsing,
	- [uvloop](https://github.com/MagicStack/uvloop) - event loop that is wrapping `libuv`, fully written in Cython,
	- [httptools](https://github.com/MagicStack/httptools) - bindings to nodejs HTTP parser, also fully written in Cython (a lot of other big projects like sanic or uvicorn use httptools).

**Cecil #2: [ugit: DIY Git in Python](https://www.leshenko.net/p/ugit/#)**

**Michael #3:** [**Things I Learned to Become a Senior Software Engineer**](https://neilkakkar.com/things-I-learned-to-become-a-senior-software-engineer.html)

- by Niel Kakkar
- Growing using different ladders of abstraction
	- Entering my second year, I had all the basics in place. 
	- I did figure out something insightful. I’m working inside the software development lifecycle, but this lifecycle is part of a bigger lifecycle: the product and infrastructure development lifecycle.
- Learning what people around me are doing
	- Since we’re not in a closed system, it makes sense to better understand the job of the product managers, the sales people, and the analysts.
	- Product managers are the best source for this. They know how the business makes money, who are the clients, and what do clients need.
- Learning good habits of mind
	- Thinking well: Diving into cog sci, one output was [a framework for critical thinking](https://neilkakkar.com/Bayes-Theorem-Framework-for-Critical-Thinking.html). It’s compounding, [and compounding is powerful](https://neilkakkar.com/year-in-review-2019.html#compounding-is-powerful-building-intuition-for-compounding-even-more-so).
- Strategies for making day-to-day more effective:  The other side of the coin is habits that allow you to think well. It starts with noticing little irritations during the day, inefficiencies in meetings, and then figuring out strategies to avoid them. 
- Some good habits I’ve noticed:
	- Never leave a meeting without making the decision / having a next action
	- Decide who is going to get it done. Things without an owner rarely get done.
	- Document design decisions made during a project
- Acquiring new tools for thought & mental models
	- New tools for thought are related to thinking well, but more specific to software engineering.
	- For example, I was recently struggling with a domain with lots of complex business logic. Edge cases were the norm, and we wanted to design a system that handles this cleanly. That’s when I read about [Domain Driven Design](https://amzn.to/2FdCYUQ)
- Protect your slack
	- When I say slack, I don’t mean the company, but the adjective.
	- One thing that gives me high output and productivity gains is to “slow down”. Want to get more done? Slow down.
	- When [there is slack](https://www.lesswrong.com/posts/yLLkWMDbC9ZNKbjDG/slack), you get a chance to experiment, learn, and think things through. This means you get enough time to get things done.
	- When there is no slack, deadlines are tight, and all your focus goes into getting shit done.
- Ask Questions
	- Q: What is a package?
	- A: It’s code wrapped together that can be installed on a system.
	- Q: Why do I need packages? A: They give a consistent way of getting all the files you need in the right place. Without them, things are easy to mess up. You need to ensure every file is where it’s supposed to be, the system paths are set up, and dependent packages are available.
	- Q: How do packages differ from applications I can install on my system? A: It’s a very similar idea! Windows installer is like a package manager that helps install applications. Similarly, DPKG and rpm packages are like `.exe`s that you can install on Linux systems, with the help of `apt` and `yum` package managers, which are like the windows installers.
- Force multipliers
	- One sprint I didn’t get much done *myself*. I wrote very limited code. Instead, I co-ordinated which changes should go out when (it was a complicated sprint), tested they worked well, did lots of code reviews, made alternate design suggestions, and pair-programmed wherever I could to get things un-stuck. We got everything done, and in this case, zooming out helped make decisions for PRs easier. It was one of our highest velocity sprints.
- Embrace fear: I’ve learned to embrace this feeling. It excites me. It’s information about what I’m going to learn. I’ve taken it so far that I’ve started tracking it [in my human log](https://neilkakkar.com/the-human-log.html) - “Did I feel fear this week?” If the answer is no too many weeks in a row, I’ve gotten too comfortable.
- Super powers
	- Getting into the source code when documentation isn’t enough
		- Quest: Reading open source code.
	- Quickly build a mental model for the code you’re looking at
		- Quest: Reading open source code.
	- Embracing fear
		- Quest: Build a side project.
	- Confidence to express ignorance
		- Quest: Overcome the first gotcha with growing.

**Cecil #4**: [**Build tech skills for space exploration**](https://docs.microsoft.com/learn/topics/nasa?WT.mc_id=nasa-pythonbytes-cephilli)

**Michael #5:** [**Profiling Django Views**](https://medium.com/kami-people/profiling-in-django-9f4d403a394f)

- by Farhan Azmi
- We know we need to profile our code
- Many Python profiling tools exist, but this article will limit only to the most used tools: `cProfile` and `django-silk` . The two tools mainly profile in regards to function calls and execution time.
- To incorporate `cProfile` to Django views, we can write our own middleware that captures the profiling on every request sent to our Django views.
- Thankfully, there exists a simpler solution: **django-cprofile-middleware**. It is a simple profiling middleware created by a Github user *omarish*.
- To profile this view with the installed middleware, we can just append `prof` parameter to the end of the URL, i.e. `http://localhost:8000/api/auth/users/availability/?username=<name>&email=<email>&prof`
- We can visualize the profile result further with Python profiler visualizing library, such as `SnakeViz`. Just add &download to the request.
- the profile result could not show which database query that brings performance hit. This is needed especially when our application is centered around database (SQL) queries: That’s where `django-silk` comes in.
- Add as middleware: Silk will automatically intercept requests we make to our views and the UI can be accessed from the path `/silk/` .
- Dive into a request to see all the headers/form/etc + DB query and perf.

**Cecil #6**: [**Send an SMS message with Azure Communication Services**](https://docs.microsoft.com/azure/communication-services/quickstarts/telephony-sms/send?pivots=programming-language-python&WT.mc_id=nasa-pythonbytes-cephilli)

Extras:

- Michael: Was on [Real Python podcast](https://realpython.com/podcasts/rpp/26/)
- Cecil: [https://studentambassadors.microsoft.com/](https://studentambassadors.microsoft.com/)

Joke: [**Dependencies**](https://xkcd.com/2347/)
