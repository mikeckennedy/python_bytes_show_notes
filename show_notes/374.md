# Python Bytes 374
Sponsored by ScoutAPM: [**pythonbytes.fm/scout**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)


Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**6 ways to improve the architecture of your Python project (using import-linter)**](https://www.piglei.com/articles/en-6-ways-to-improve-the-arch-of-you-py-project/)

- Piglei
- Using [import-linter](https://github.com/seddonym/import-linter) to 
    - define architectural layers
    - check to make sure imports don’t violate (import from upper layers)
    - can also check for more contracts, such as 
        - forbidden - disallow a specific from/to import 
        - independence - list of modules that shouldn’t import from each other
- Fixing violations
    - a process introduced to set exceptions for each violation in a config file
    - then fix violations 1 at a time (nice approach)
    - use the whole team if you can
- Common methods for fixing dependency issues
    - Merging and splitting modules
    - Dependency Injection, including using protocols to keep type hints without the need to import just for types
    - Use simpler dependency types
    - Delaying function implementations
        - module global methods set by caller, or adding a simple plugin/callback system
    - Configuration driven
        - Setting import statements in a config file and using `import_string()`  at runtime
    - Replace function calls with event-driven approaches

**Michael #2:** [Mountaineer](https://github.com/piercefreeman/mountaineer)

- Mountaineer is a batteries-included web framework for Python and React.
- Mountaineer focuses on developer productivity above all else, with production speed a close second.
    - 📝 Typehints up and down the stack: frontend, backend, and database
    - 🎙️ Trivially easy client<->server communication, data binding, and function calling
    - 🌎 Optimized server rendering for better accessibility and SEO
    - 🏹 Static analysis of web pages for strong validation: link validity, data access, etc.
    - 🤩 Skip the API or Node.js server just to serve frontend clients

**Brian #3:** [**Why Python's Integer Division Floors**](https://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html)

- Guido van Rossum
- Integer division always floors (toward negative infinity) instead of truncating. (C truncates)
- 5//2 → 2
- -5//2 → -3
- 5//-2 → -3
- Reason, 
    - For nice mathematical relationships with // and % (modulo).
    -  a//b = quotient (q), a%b = remainder (r)
    - such that b*q + r = a, and  0 <= r < b 
        - This works for both positive and negative a values
        - For negative b, the second rule has to change to 0 >= r > b 
- If you truncate (like C does), you have to use abs(r) for the first rule to work.
- Theory of why C doesn’t do it this way: Probably a hardware limitation at the time when C was designed, due to “sign + magnitude” integers instead of modern two’s compliment integers.

**Michael #4:** [**Hatchet**](https://hatchet.run)

- Hatchet is a distributed, fault-tolerant task queue which replaces traditional message brokers and pub/sub systems. 
- It’s built to solve problems like concurrency, fairness, and durability
- Concurrency, Fairness, and Rate limiting: Enable FIFO, LIFO, Round Robin, and Priority Queues with built-in strategies to avoid common pitfalls.
- Architected for Resiliency: Customizable retry policies and built-in error handling to recover from transient failures.

**Extras** 

Brian:

- [**Charlie Marsh on uv in PythonTest episode 216**](https://pythontest.com/216)

Michael:

- [**Build An Audio AI App Course**](https://training.talkpython.fm/courses/build-an-audio-ai-app-with-python-and-assemblyai) [free!]
- [**Rock Solid Python with Python Typing Course**](https://training.talkpython.fm/courses/python-type-hint-course-with-hands-on-examples)
- [**Coolio**](https://mstdn.social/@RayScript/111919177551660638)

**Joke:** [**Breaking Prod**](https://workchronicles.com/not-if-but-when/)

