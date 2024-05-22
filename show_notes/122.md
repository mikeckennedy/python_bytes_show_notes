# Python Bytes 122
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** **Combining and separating dictionaries**

- [PEP 584 -- Add + and - operators to the built-in dict class.](https://www.python.org/dev/peps/pep-0584/)
  - Steven D'Aprano
  - Draft status, just created 1-March-2019
  - d1 + d2 would merge d2 into d1
		- like `{**d1, **d2}`
		- or on two lines

```
    d = d1.copy()
    d.update(d2)
```    

  - of note, (d1 + d2) != (d2 + d1)
  - Currently no subtraction equivalent
- [Guido’s preference of + over |](https://mail.python.org/pipermail/python-ideas/2019-February/055519.html)
- Related, [Why operators are useful](https://neopythonic.blogspot.com/2019/03/why-operators-are-useful.html) - also by Guido

**Michael #2:** [**Why I Avoid Slack**](https://matthewrocklin.com/blog/2019/02/28/slack-github)

- by Matthew Rocklin
- I avoid interacting on Slack, especially for technical conversations around open source software. 
- Instead, I encourage colleagues to have technical and design conversations on GitHub, or some other system that is public, permanent, searchable, and cross-referenceable.
- Slack is fun but, internal real-time chat systems are, I think, bad for productivity generally, especially for public open source software maintenance.
- Prefer GitHub because I want to
	- **Engage collaborators** that aren’t on our Slack
	- **Record the conversation** in case participants change in the future.
	- **Serve the silent majority** of users who search the web for answers to their questions or bugs.
	- **Encourage thoughtful discourse**. Because GitHub is a permanent record it forces people to think more before they write.
	- **Cross reference issues**. Slack is siloed. It doesn’t allow people to cross reference people or conversations across Slacks

**Brian #3:** [**Hunting for Memory Leaks in Python applications**](https://medium.com/zendesk-engineering/hunting-for-memory-leaks-in-python-applications-6824d0518774)

- Wai Chee Yau
- Conquering memory leaks and spikes in Python ML products at Zendesk.
- A quick tutorial of some useful memory tools
- The `memory_profiler` package and `matplotlib` to visualize memory spikes.
- Using `muppy` to heap dump at certain places in the code.
- `objgraph` to help memory profiling with object lineage.
- Some tips when memory leak/spike hunting:
	- strive for quick feedback
	- run memory intensive tasks in separate processes
	- debugger can add references to objects
	- watch out for packages that can be leaky
		- `pandas`? really?

**Michael #4:** [**Give Me Back My Monolith**](http://www.craigkerstiens.com/2019/03/13/give-me-back-my-monolith/)

- by [Craig Kerstiens](http://www.craigkerstiens.com/)
- Feels like we’re starting to pass the peak of the hype cycle of microservices
- We’ve actually seen some migrations from [micro-services back to a monolith](https://segment.com/blog/goodbye-microservices/).
- Here is a rundown of all the things that were simple that you now get to re-visit
- Setup went from intro chem to quantum mechanics
	- Onboarding a new engineering, at least for an initial environment would be done in the first day. As we ventured into micro-services onboarding time skyrocketed
- So long for understanding our systems
	- Back when we had monolithic apps if you had an error you had a clear stacktrace to see where it originated from and could jump right in and debug. Now we have a service that talks to another service, that queues something on a message bus, that another service processes, and then we have an error.
- If we can’t debug them, maybe we can test them
- All the trade-offs are for a good reason. Right?

**Brian #5:** [**Famous Laws Of Software Development**](https://www.timsommer.be/famous-laws-of-software-development/)

- Tim Sommer
- 13 “laws” of software development, including
	- Hofstadter’s Law: “It always takes longer than you expect, even when you take into account Hofstadter's Law.”
	- Conway’s Law: “Any piece of software reflects the organizational structure that produced it.”
	- The Peter Principle: “In a hierarchy, every employee tends to rise to his level of incompetence.”
	- Ninety-ninety rule: “The first 90% of the code takes 10% of the time. The remaining 10% takes the other 90% of the time”

**Michael #6:** [**Beer Garden Plugins**](https://beer-garden.io/)

- A powerful plugin framework for converting your functions into composable, discoverable, production-ready services with minimal overhead.
- Beer Garden makes it easy to turn your functions into REST interfaces that are ready for production use, in a way that’s accessible to anyone that can write a function.
- Based on MongoDB, Rabbit MQ, & modern Python
- Nice docker-compose option too

**Extras**

Michael:

- [Firefox Send](https://send.firefox.com/)
- Ethical ads on Python Bytes (and Talk Python)

Brian: 

- [T&C 69: The Pragmatic Programmer — Andy Hunt](https://testandcode.com/69)
  - not up yet, but will be before this episode is released


**Jokes**

- From [Derrick Chambers](https://twitter.com/derchambers/status/1107843771557765120)

    “What do you call it when a python programmer refuses to implement custom objects? 
    self deprivation!
    Sorry, that joke was really classless.”
    
- via [pyjokes](https://github.com/pyjokes/pyjokes): I had a problem so I thought I'd use Java. Now I have a `ProblemFactory`.

