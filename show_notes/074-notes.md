# Python Bytes 74
Sponsored by Datadog: [**pythonbytes.**](https://pythonbytes.fm/datadog)[**fm**](https://pythonbytes.fm/datadog)[**/datadog**](https://pythonbytes.fm/datadog)

**Special guest: Matt Harrison -** [**__mharrison__**](https://twitter.com/__mharrison__)

**Brian #1: Contributing to Open Source effectively**
The mechanics and conventions on how to contribute to open source projects can be confusing. After seeing a [very well documented pull request](https://github.com/okken/cards/pull/31) that started with `[WIP]` in the subject line when it was first submitted, I tried to find out more about the conventions and mechanics of it all. I’m still learning, but here are a couple of resources:

- [How to write the perfect pull request](https://blog.github.com/2015-01-21-how-to-write-the-perfect-pull-request/) is more of a mindset of how to initiate and receive PRs
	- Approach to writing a Pull Request, including that [WIP] trick.
	- Offering feedback
	- Responding to feedback
- [Forge Your Future with Open Source](https://pragprog.com/book/vbopens/forge-your-future-with-open-source), [**@**](https://twitter.com/vmbrasseur)[vmbrasseur](https://twitter.com/vmbrasseur) book on contributing to open source, includes:
	- Make a Contribution, which includes PRs
	- Make a difference without making a pull request, which is suggests many ways to contribute to a project without contributing code, like reviewing others contributions, testing, triaging bugs, …
	- Interacting with the community.

**Matt #2:** **Jupyter, Mathematica, and the Future of the Research Paper**

- Paul Romer, economy professor at NYU
- As a longtime Linux user there was constantly the question of the “year of the Linux Desktop”. Maybe this is the year of the “Jupyter desktop” (also beta version of JupyterLab). Not just a tool for innovators or early adopters
- Refers to Article in Atlantic contrasting Mathematica and Jupyter: *open-source developers have flocked to Python because it happens to be the de facto standard for scientific computing. Programming-language communities, like any social network, thrive—or die—on the strength of these feedback loops*. [https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/ ](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/)

Quotes: 

*Jupyter is a new open-source alternative [to Mathmatica] that is well on the way to becoming a standard for exchanging research results.*

*Python libraries let me replicate everything I wanted to do with Mathematica: Matplotlib for graphics, SymPy for symbolic math, NumPy and SciPy for numerical calculations, Pandas for data, and NLTK for natural language processing. Jupyter makes it easy to use Latex to display typeset math. With Matplotlib, Latex works even in the label text for graphs. (I have not yet tried the major update, JupyterLab, which is still in beta testing.)*
*I’m more productive. I’m having fun.*
[https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/](https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/)

**Michael** **#3:** [**Python Developers Survey 2017 Results**](https://www.jetbrains.com/research/python-developers-survey-2017/)

- At the very end of 2017, JetBrains & The PSF teamed up to build a solid picture of the modern Python developer
- Here are some take-aways
	- Almost 4 out of 5 Python developers use it as their main language, while for 21% it’s only a secondary language.
	- Data analysis is as popular as web development with Python: Web development is the only category with a large gap (54% vs 33%) separating those using Python as their main language vs as a supplementary language. For other types of development, the differences are far less significant.
	- At 28% to 27% application, There are as many Python web developers as Python data scientists
	- Python 3 vs Python 2: 75% to 25% and accelerating
	- Top Cloud Platform(s)
		- 67%: AWS
		- 29%: Google App Engine
		- 26%: Heroku
		- 23%: DigitalOcean
		- 16%: Microsoft Azure
	- Team Size
		- 74%: 2-7 people
		- 16%: 8-12 people
		- 5%: 13-20 people
		- 2%: 21-40 people
		- 2%: > 40 people
	- Operating Systems
		- 49%: Windows
		- 19%: Linux
		- 15%: MacOS

**Brian #4**[**:**](https://edgedb.com/blog/edgedb-a-new-beginning) [****](https://edgedb.com/blog/edgedb-a-new-beginning)[**EdgeDB: A New Beginning**](https://edgedb.com/blog/edgedb-a-new-beginning)
This is “news you can’t use” so far, because the product isn’t here yet. So why am I excited and interested in this:

  - It’s from Elvis [**@**](https://twitter.com/elprans)[elprans](https://twitter.com/elprans) and Yury [**@**](https://twitter.com/1st1)[1st1](https://twitter.com/1st1), who have brought us asyncio and uvloop
  - It’s not just a relational DB, it’s a DB based on PostgreSQL but with an entire new way to specify schema and interact with it.
  - Goal is to be fast, user friendly, and remove the need for ORMs

**Matt** **#5:** **Yellowbrick library**
Yellowbrick - http://www.scikit-yb.org/en/latest/ 

- Visualization is important, I’ve found bugs by plotting before. Also important in evaluation of machine learning projects
- This is a project that has been around for about two years. I’ve recently adopted it in place of some home grown libraries for some consulting projects and in my corporate training
- Yellowbrick offers visualization for:
	- Features
	- Classification
	- Regression
	- Clustering
	- Text
- Like sk-learn, uses a similar api (.fit, .transform, .poof (plot))

**Michael #6:** [**Depression AI**](https://github.com/Jflick58/DepressionAI)

- Alexa skill for people suffering with depression. 
- Alexa [store listing](https://www.amazon.com/Depression-AI/dp/B079N6WR6Y/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1522775645&sr=1-1&keywords=depression+ai)
- Based on [Flask-Ask](https://github.com/johnwheeler/flask-ask)
	- Discussed on [Talk Python 146](https://talkpython.fm/episodes/show/146/building-alexa-skills-with-python-and-flask)
- Valley Hackathon 2018 winner
- 71% of people who make their bed in the morning report feeling happy. This was the inspiration behind DepressionAI. 
- The aim behind this skill is to encourage people to perform daily activities that become very difficult when one is depressed.
- The skill detects positive and negative moods. 
- If the user is having a bad day, it asks them a series of questions about what they have done that day (e.g. "Have you gotten out of bed?") and if they haven't, it encourages them to do so.
- Features
	- Mood evaluation by a highly empathetic Alexa bot
	- Suicidal intention detection and prevention attempt
	- Location-based therapy reccomendations
	- Suggestions for small activites to improve the user's mood
	- Displays informative cards in the Alexa app
- Sample Phrases
	- “Alexa, check on me."
	- "I feel down."
	- "I haven't got out of bed today."
	- "Help me feel better."
	- "Help me find a therapist"
