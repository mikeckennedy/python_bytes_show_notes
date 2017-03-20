
**#1 Brain: [python-fire](https://github.com/google/python-fire)**

- Suggested by several listeners
- Under the Google repo set on github but not a Google product.
- “Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.”

*Some Benefits as listed on the project page*

- a simple way to create a CLI in Python. 
- a tool for exploring and debugging Python code. 
- exploring existing code by turning other people's code into a CLI.
- makes transitioning between Bash and Python easier. 

My take: 

- Enough documentation right in the github repo for me to try it out. 
- Concise but thorough documentation, as well.
- I wouldn’t ship a CLI with this, as it’s too heavy.
  - depends on ipython and six
- It would be useful to very quickly throw together a CLI to try out some Python code from bash.
- For internal development and debugging tools.
- I think this week I’m going to try to build a few CLI tools for directly sending and receiving commands to some test instruments. 

**#2 Michael:** [**Simon: Simple macOS menubar system monitor**](https://github.com/hcyrnd/simon)**, written in Python 3.6 + pyobjc**

- Shows how simple a menubar app can be
- Nice example of a platform-native Python app (we need more of these)
- Could use it as a starter app for your ideas on macOS

**#3 Brain:** **Free Food**
A couple of amusing Reddit posts about free food.

- [Finding Free Food with Python](http://jamesbvaughan.com/python-twilio-scraping/)
- [Notification when friends order pizza](https://www.reddit.com/r/Python/comments/5wec78/i_wrote_a_program_that_emails_me_when_one_of_my/) 

**#4 Michael:** [**HTTPie**](https://httpie.org/)

- Pronounced aitch-tee-tee-pie
- A command line HTTP client with an intuitive UI, JSON support, syntax highlighting, wget-like downloads, plugins, and more.
- A picture is worth many words, have a look: https://httpie.org/
- Excellent support for JSON, XML, HTTP response headers, etc
- I spoke before about [Postman](https://www.getpostman.com/) as an API test client, this is the CLI version.

**#5 Brain: [pipdeptree](https://pypi.python.org/pypi/pipdeptree)**

- Sometimes when doing `pip list`  I see way more packages than I remember installing. That’s due to dependent installs. 
- `pipdeptree` is a simple command line tool that shows you your installed packages in an ascii tree structure so you can see who depends on.
- Example. `arrow` ? I don’t remember installing that. Ah. `arrow`  is a dependency of `jinja2-time` ,which is a dependency of `cookiecutter` , that I do remember installing.

**#6 Michael:** [**Not Your Father’s Python: Amazing Powerful Frameworks**](https://blog.signifai.io/not-your-fathers-python-amazing-powerful-frameworks/)

- When we were getting SignifAI off the ground, one of the biggest decisions we had to make right at the beginning was what our stack would be.
  - We know Python but…
  - But it’s important to note that our product and infrastructure must support hundreds of thousands of events per second.
  - So we were happy to see that, with the recent widespread adoption of Python 3 and the introduction of tasks and coroutines as first-class citizens in the language, Python has recently stepped up its game.
  - Python 3 has continued evolving into a new wave of libraries that disrupt and change old assumptions about Python performance for web applications.
  - Python’s GIL, is it a true roadblock?
  - UVLoop is the first ultra-fast asynchronous framework, which is a drop-in replacement for Python 3.5’s built-in asyncio event loop. Both Japronto and Sanic which are reviewed in this post are also based on UVLoop.
  - The future of Python is here: Overall, it looks like fast, asynchronous Python might be here to stay. Now that asyncio appears to be a default in Python and the async/await syntax has found favor among developers, the GIL doesn’t seem like such a roadblock anymore and speed doesn’t need to be a sacrifice.
- Comment: https://blog.signifai.io/not-your-fathers-python-amazing-powerful-frameworks/#comment-3193753282 
- Sasha Cuerda‏’s tweet: https://twitter.com/sashacuerda/status/839839014836453377
  *@mkennedy @brianokken Just used the aiohttp example you talked about to refactor a CLI scraper...went from > 8' to < 45". Blown away.*

