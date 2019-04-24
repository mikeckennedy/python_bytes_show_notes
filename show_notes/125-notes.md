# Python Bytes 125
Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

**Brian #1:** [**My How and Why: pyproject.toml & the 'src' Project Structure**](https://bskinn.github.io/My-How-Why-Pyproject-Src/)

- Brian Skinn
- pyproject.toml
	- but with setuptools, instead of flit or poetry
	- with a `src` dir
	- and tox and black
- all the bits and pieces to make all of this work

**Michael #2:** [**The Deadlock Empire: Slay dragons, master concurrency!**](https://deadlockempire.github.io/)

- A game to test your thread safety and skill!
- Deadlocks occur in code when two threads end up trying to enter two or more locks (RLocks please!)
- Consider `lock_a` and `lock_b`
- Thread one enters `lock_a` and will soon enter `lock_b`
- Thread two enters `lock_b` and will soon enter `lock`_a
- Imagine transferring money between two accounts, each with a lock, and each thread does this in opposite order.

**Brian #3:** [**Cog 3.0**](https://nedbatchelder.com/blog/201904/cog_30.html)

- Ned Batchelder’s `cog` gets an update (last one was a few years ago).
- “[Cog](https://nedbatchelder.com/code/cog) … finds snippets of Python in text files, executes them, and inserts the result back into the text. It’s good for adding a little bit of computational support into an otherwise static file.”
- Development moved from Bitbucket to GitHub. 
- Travis and Appveyor CI.
- The biggest functional change is that errors during execution now get reasonable tracebacks that don’t require you to reverse-engineer how cog ran your code.
-  [mutmut](https://nedbatchelder.com/blog/201903/mutmut.html) mutation testing added. Cool.
- What I want to know more about is this statement: “…now I use it for making all my presentations”. Very cool idea.

**Michael #4:** [**StackOverflow 2019 Developer Survey Results**](https://insights.stackoverflow.com/survey/2019)

- More good news for Python
- Lots of focus on gender in this one
- [Contributing to Open Source](https://insights.stackoverflow.com/survey/2019#developer-profile-_-contributing-to-open-source)
	- About 65% of professional developers on Stack Overflow contribute to open source projects once a year or more. Involvement in open source varies with language. Developers who work with Rust, WebAssembly, and Elixir contribute to open source at the highest rates, while developers who work with VBA, C#, and SQL do so at about half those rates.
- [Competence and Experience](https://insights.stackoverflow.com/survey/2019#developer-profile-_-competence-and-experience)
	- We see evidence here among the most junior developers for *impostor syndrome*, pervasive patterns of self-doubt, insecurity, and fear of being exposed as a fraud. Among our respondents, men grew more confident much more quickly than gender minorities.
- [Programming, Scripting, and Markup Languages](https://insights.stackoverflow.com/survey/2019#technology-_-programming-scripting-and-markup-languages)
	- Python edges out Java, second only to JavaScript (and two non-programming languages)
- [Databases](https://insights.stackoverflow.com/survey/2019#technology-_-databases)
	- MySQL, Postgres, Microsoft SQL Server, SQLite, MongoDB
- [Most Loved, Dreaded, and Wanted Languages](https://insights.stackoverflow.com/survey/2019#technology-_-most-loved-dreaded-and-wanted-languages)
	- Loved: Rust, Python
	- Wanted: Python, JavaScript
	- Dreaded: VBA, ObjectiveC
- [Most Loved, Dreaded, and Wanted Databases](https://insights.stackoverflow.com/survey/2019#technology-_-most-loved-dreaded-and-wanted-databases)
	- Loved: Postgres
	- Wanted: MongoDB
- [Most Popular Development Environments](https://insights.stackoverflow.com/survey/2019#technology-_-most-popular-development-environments)
	- VS Code is crushing it
- [How Technologies Are Connected](https://insights.stackoverflow.com/survey/2019#technology-_-how-technologies-are-connected) is just interesting

**Brian #5:** [**Cuv’ner**](https://github.com/meejah/cuvner/blob/master/cuv/README.rst) **“**A commanding view of your test-coverage"

- Coverage visualizations on the console.

**Michael #6:** [**Mobile apps launched**](https://training.talkpython.fm/apps)

- The tech (sadly only 50% Python)
	- Xamarin, Mono, and C# on the device-side
	- Python, Pyramid, and MongoDB on the server-side
- 90% code sharing or higher
- Native applications
- Build the prototype myself on Windows
- Hired Giorgi via [**TopTal**](http://toptal.com/#we-annexed-perfect-engineers)
	- Get your own developer or get some freelancing work and support my app progress with my referral code: [**toptal.com/#we-annexed-perfect-engineers**](https://www.toptal.com/#we-annexed-perfect-engineers) 
- Dear mobile app developers: You have my sympathy!
- Try the app at [**training.talkpython.fm/apps**](https://training.talkpython.fm/apps) Comes with 2 free courses for anyone who logs in.
- Android only at the moment but not for long

**Extras**

**Brian**:

- Python Bytes Patreon page is up: **[patreon.com/pythonbytes](https://www.patreon.com/pythonbytes)**

**Michael**:

- PyCon Booth
- [**XKCD Plots in Matplotlib**](https://jakevdp.github.io/blog/2013/07/10/XKCD-plots-in-matplotlib/) with [**examples**](https://matplotlib.org/xkcd/examples/showcase/xkcd.html) via Tim Harrison
- [**Fira Code Retina and Font Ligatures**](https://github.com/tonsky/FiraCode)
- The EuroSciPy 2019 Conference will take place from September 2 to September 6 in Bilbao, Spain

**Jokes**

- “When your hammer is C++, everything begins to look like a thumb.”
- “Why don't jokes work in octal? Because 7 10 11” 
	- Over explained: Why is 6 afraid of 7. Cuz 7 8 9.
	- Follow on: Why did 7 eat 9? He was trying to eat 3^2 meals.
- I've been using Vim for a long time now, mainly because I can't figure out how to exit.

