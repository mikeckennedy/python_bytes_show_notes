# Python Bytes 26
Sponsored by rollbar: [rollbar.com/pythonbytes](http://rollbar.com/pythonbytes)

**Brian #1: Two part series on interactive terminal applications**

**Part 1:** [**4 terminal applications with great command-line UIs**](https://opensource.com/article/17/5/4-terminal-apps)

- For Comparison: both ok but could be better
  - MySQL REPL
  - Python REPL
- [bpython](https://bpython-interpreter.org/) adds autocompletion and other goodies
  - also check out [ptpython](https://pypi.python.org/pypi/ptpython) as a REPL replacement
- [mycli](http://mycli.net/) adds context aware completion to MySQL
[mycli](http://mycli.net/) - [pgcli](https://www.pgcli.com/) for postgress that adds fuzzy search
- [fish](https://fishshell.com/) : like bash, but has better search history

**Part 2:** [**4 Python libraries for building great cli's**](https://opensource.com/article/17/5/4-practical-python-libraries)

- [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/latest/) - for building a REPL like interface
  - includes command history, auto-suggestion, auto-completion
- [click](http://click.pocoo.org/5/)
  - includes pager and ability to launch an editor
- [fuzzyfinder](https://pypi.python.org/pypi/fuzzyfinder) - make suggestions
  - article shows how to combine that with prompt_toolkit
- [pygments](http://pygments.org/) - syntax highlighting

**Michael #2:** [**How have you automated your life with python?**](https://www.reddit.com/r/Python/comments/69ba93/how_have_you_automated_your_life_with_python_if/)

- There is something magical about writing code that interacts with the physical world.
- I have a script which runs every 5 minutes between 17:00 and 17:30 which scrapes the train times website and sends me desktop notifications saying whether or not my trains home are delayed / cancelled.
- I recently wrote a quick python script that tells me when my girlfriend comes home: It sniffs the network for DHCP traffic, when her phone joins the wifi network outside it uses the say command to let me know.
- Wrote a script to check if nearby ice cream shops are stocking my favourite (rare) flavour by scanning their menu page for keywords.
- A script to check the drive time too/from work using a route with tolls or without tolls.. to try and save some money when the times aren't too different. Using google maps API and a flask site.
- I have a script that generates weekly status update emails based off my git commit messages and pull requests. It also creates timesheets in Harvest based on the projects I'm assigned.
- I have thrown together some python that automatically controls my reverse-cycle AC system so that it makes optimal use of my solar panels on my roof.

**Brian #3**: [**Building a Simple Birthday App with Flask-SQLAlchemy**](http://pybit.es/flask-sqlalchemy-bday-app.html)

- Nice simple application with a clear need.
  - Keep track of upcoming birthdays
  - Avoid Faceboook
  - Build a simple Flask app
  - Try SQLAlchemy


**Sponsored by Rollbar**, try them at [rollbar.com/pythonbytes](http://rollbar.com/pythonbytes) and don't forget to visit their booth at PyCon!

**Michael #4:** [**Spelling with Elemental Symbols**](https://www.amin.space/blog/2017/5/elemental_speller/)

- How does it work?
  - Input: "Amputations"
  - Output: "AmPuTaTiONS", "AmPUTaTiONS"
- Generating Character Groupings: 
  - 'AmPuTaTiONS' `(2,2,2,2,1,1,1)`
  - 'AmPUTaTiONS' `(2,1,1,2,2,1,1,1)`
  - How many are there in general for a given word? `fib(n + 1)`!
- Addressing Performance Issues: A few attempts don’t add much but
- Memoization: The technique of saving a function's output and returning it if the function is called again with the same inputs. A memoized function only needs to generate output once for a given input. This can be very helpful with expensive functions that are called many times with the same few inputs, but only works for pure functions. → 30% faster
- Algorithms: Switch to directed graphs and recursion, changes O(2^n) to O(n) and time from 16min to 10 sec.
- Learned a great deal along the way. This project introduced:
  - Combinatorics
  - Performance profiling
  - Time complexity
  - Memoization
  - Recursion
  - Graphs and trees

**Brian #5:** **IDE's for beginners**

- [Recent discussion on Reddit about Thonny](https://www.reddit.com/r/Python/comments/6ahnsb/thonny_python_ide_for_beginners/)
- I have mixed feelings about encouraging beginner IDE's.
  - Mostly negative feelings.
  - And yet there is IDLE, there is Thonny, ...
- Are these useful? Anti-useful?
- Isn't learning a decent editor part of learning to program?

**Michael #6:** [**PDF Plumber**](https://twitter.com/dtizzlenizzle/status/861024781273112576)

- Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables.
- Visual debugging with `.to_image()`
- Extracting tables
  - pdfplumber's approach to table detection borrows heavily from Anssi Nurminen's master's thesis, and is inspired by Tabula. It works like this:
  - For any given PDF page, find the lines that are (a) explicitly defined and/or (b) implied by the alignment of words on the page.
  - Merge overlapping, or nearly-overlapping, lines.
  - Find the intersections of all those lines.
  - Find the most granular set of rectangles (i.e., cells) that use these intersections as their vertices.
  - Group contiguous cells into tables.
  - Check out the demonstrations section.

