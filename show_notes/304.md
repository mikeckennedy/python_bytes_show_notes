# Python Bytes 304

Sponsored by [**Complier Podcast from RedHat**](https://pythonbytes.fm/compiler)

**Brian #1:** [**Ten tasty ingredients for a delicious pull request**](https://wagtail.org/blog/ten-tasty-ingredients-for-a-delicious-pull-request/?utm_source=pocket_mylist)

- on wagtail blog, from LB
- Great tips for helping out with open source projects. 
- But even for closed source, there’s good stuff there to know for people transitioning to single person projects to working on a team.
- The tips
    - Read the [development] instructions. The contributing guide, etc.
    - Read the issue and comments
    - Create a fresh branch for your contribution
    - Keep the changes focused
    - Write unit tests
        - also, extending tests for untested or under-tested features are a great way to contributes
    - Give your pull request a name with context
    - Reference the issue being fixed or resolved in the pull request
    - Review & fix the CI failures
    - Push to the same branch with fixes and do not open a new pull request
    - Be patient. (Article lists this as “Eagerness balanced with patience”).

**Michael #2:**  [**textX**](https://pypi.org/project/textX/)

- via [**Rhet Turnbull**](https://twitter.com/RhetTurnbull)
- textX is a meta-language for building Domain-Specific Languages (DSLs) in Python. It is inspired by [Xtext](http://www.eclipse.org/Xtext/).
- In a nutshell, textX will help you build your textual language in an easy way. You can invent your own language or build a support for already existing textual language or file format.
- From a single language description (grammar), textX will build a parser and a meta-model (a.k.a. abstract syntax) for the language


**Brian #3:** [**Reasoning about asyncio.Semaphore**](https://neopythonic.blogspot.com/2022/10/reasoning-about-asynciosemaphore.html)

- Guido van Rossum
- Article uses a fast food restaurant analogy to reason about concurrency, asyncio, locks, and semaphores.
- A lock is like a single table restaurant with buzzers handed out to people waiting.
- A semaphore is like the same thing but with more than one table.
- Great discussion of the complexities of the Semaphore implementation.
- Also of concurrency.
- But almost as important, it’s an excellent example of utilizing a fairly easy to visualize analogy to reason about a complex problem. It also hits parts of the problem difficult to fit into the analogy, and pragmatically abandons the analogy when necessary.

**Michael #4:** [**Turnstile**](https://blog.cloudflare.com/turnstile-private-captcha-alternative/)

- A user-friendly, privacy-preserving alternative to CAPTCHA
- I created a Python library based on Pydantic to validate the forms: [**turnstile.py**](https://gist.github.com/mikeckennedy/66d6298106671a3c6215c9262c102d74) (should I make this proper package and GitHub repo?)


**Extras** 

**Brian**: 

- Choosing a place to host your Python application.
    - aka [**Heroku Alternatives for Python-based Applications**](https://testdriven.io/blog/heroku-alternatives/#railwayapp)
- Kicking around the idea of starting cohort based pytest training, possibly starting mid Dec.
    - Please let me know if you think this is a good idea and you might be interested. 
    - message me [@brianokken](https://twitter.com/brianokken)

**Michael**:

- **Cppfront project aims to modernize C++**
- [**New pyscript**](https://twitter.com/JeffersGlass/status/1575940781516673024?cxt=HBwWgMDS1dDy7t4rAAAA&cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email) (will cover in more depth soon)
- [**NextDNS**](https://nextdns.io/?from=a743zhpr) follow up
    - [**https://nextdns.io/**](https://nextdns.io/?from=a743zhpr) 
    - Yes, it’s basically PiHole in the Cloud with tons of options
    - Currently outdoing my NordVPN protections
    - Try with [**https://adblock-tester.com**](https://adblock-tester.com)
    - Had to manually set DNS-over-HTTPS in Vivaldi to work with VPN
    - Add additional blocking lists
- Got a [**Feather ESP32-S2**](https://www.adafruit.com/product/5000) and put CircuitPython on it

**Joke:** [**Getting help with code**](https://twitter.com/PR0GRAMMERHUM0R/status/1571393611396169728)
