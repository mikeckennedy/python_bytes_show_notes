# Python Bytes 34
Sponsored by Rollbar! Get the bootstrap plan at [pythonbytes.fm/rollbar](https://pythonbytes.fm/rollbar)

**Brian #1:** [**Easy Python logging with daiquiri**](https://julien.danjou.info/blog/python-logging-easy-with-daiquiri)

- Standard library logging package is non-intuitive. 
- Daiquiri is better.
- Logs to stderr by default.
- Use colors if logging to a terminal.
- Support file logging.
- Use program name as the name of the logging file so providing just a directory for logging will work.
- Support syslog.
- Support journald.
- JSON output support.
- Support of arbitrary key/value context information providing.
- Capture the warnings emitted by the warnings module.
- Native logging of any exception.
- This works:

```
    import daiquiri
    daiquiri.setup()
    logger = daiquiri.getLogger()
    logger.error("something wrong happened")
```


- Also check out [logzero](https://github.com/metachris/logzero/blob/master/README.rst)

```
    from logzero import logger
    logger.debug("hello")
    logger.info("info")
    logger.warn("warn")
    logger.error("error")
  ```

**Michael #2:** [**The Real Threat of Artificial Intelligence**](https://www.nytimes.com/2017/06/24/opinion/sunday/artificial-intelligence-economic-inequality.html)

- What worries you about the coming world of artificial intelligence?
- Too often the answer to this question resembles the plot of a sci-fi thriller. People worry that developments in A.I. will bring about the “singularity”
- This doesn’t mean we have nothing to worry about. 
- On the contrary, the A.I. products that now exist are improving faster than most people realize and promise to radically transform our world, not always for the better
- AI will reshape what work means and how wealth is created, leading to unprecedented economic inequalities and even altering the global balance of power
- This kind of A.I. is spreading to thousands of domains (not just loans), and as it does, it will eliminate many jobs. Bank tellers, customer service representatives, telemarketers, stock and bond traders, even paralegals and radiologists will gradually be replaced by such software.
- Part of the answer will involve educating or retraining people in tasks A.I. tools aren’t good at. Artificial intelligence is poorly suited for jobs involving creativity, planning and “cross-domain” thinking — for example, the work of a trial lawyer. 
- The solution to the problem of mass unemployment, I suspect, will involve “service jobs of love.” These are jobs that A.I. cannot do, that society needs and that give people a sense of purpose. Examples include accompanying an older person to visit a doctor, mentoring at an orphanage
- This leads to the final and perhaps most consequential challenge of A.I. The Keynesian approach I have sketched out may be feasible in the United States and China, which will have enough successful A.I. businesses to fund welfare initiatives via taxes. But what about other countries?

**Brian #3:** [**The three laws of config dynamics**](https://blog.buildo.io/the-three-laws-of-config-dynamics-1e9724593aa9)

- The birth of configuration files
- **Law 1** Config values can be transformed from one form to another, but can be neither created nor destroyed.
- **Law 2** The total length of a config file can only increase over time.
- **Law 3** The length of a perfect config file in a development environment is exactly equal to zero.
- Docker can help

**Michael #4:** [**Five Tips To Get You Started With Jupyter Notebook**](https://medium.com/arcgis-api-for-python-explorers-corner/a-few-tips-to-get-you-started-with-jupyter-notebook-8f9b172d98cb)

- Don’t Put Your Entire Code in a Single Cell
- There are different types of cells
- Executing Cells (shift + enter)
- Explore Interactive Mapping Options (via ArcGIS)
- To explore new modules, use questions and TAB auto-complete (Object?)

**Brian #5:** [**Cost of Coupling Versus Cost of De-coupling**](https://m.facebook.com/notes/kent-beck/cost-of-coupling-versus-cost-of-de-coupling/1578239345542257/)

- Two elements are coupled wrt a given change iff changing one element implies changing the other.
- Decoupled code, or loosely coupled, follows DRY principles, uses smaller components, is more modular, etc. But also has more files, more classes, handles more cases, and takes longer to write.
- There is a place for both. 
- Kent describes two phases, Explore and Extract.
- Explore
  - more learning
  - tracer bullets, spike projects, first drafts, happy path implementation
  - coupled code, copy/paste coding, etc work fine and are faster because the design and architecture aren’t the goal, learning is the goal
  - answer questions quickly
  - ask better questions based on learnings
- Extract
  - Candidate Release, final draft, architected
  - Economies of scale take over
  - Return on investment
  - Minimize cost of changes as code base grows.

**Michael #6:** [**100 Days of Code at PyBites**](https://pybit.es/special-100days-of-code.html)

- The Challenge: [Join the #100DaysOfCode](https://medium.freecodecamp.org/join-the-100daysofcode-556ddb4579e4)
- Stats: [We wrote roughly 5K lines of code](https://github.com/pybites/100DaysOfCode/tree/master/100), divided into 100 scripts, one each day
- We [auto-tweeted](https://github.com/pybites/100DaysOfCode/tree/master/007) our progress each day which was tracked in our [log file](https://github.com/pybites/100DaysOfCode/blob/master/LOG.md).
- Module Index: We ended up using exactly 100 modules as well (weird coincidence LOL)
- Showcase of 10 Utilities
- The rumors are true: our next 100 days project will be around learning Django

Extra:

- First book review of up, [http://chrisshaver64.ddns.net/bl0046](http://chrisshaver64.ddns.net/bl0046)
- Python for Entrepreneurs has officially launch! Over 19 hours of content. Get it at [https://talkpython.fm/launch](https://talkpython.fm/launch)

