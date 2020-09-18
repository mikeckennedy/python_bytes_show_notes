# Python Bytes 200
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python Testing with pytest**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)

**Brian #1:** [**How to be helpful online**](https://nedbatchelder.com/blog/202009/how_to_be_helpful_online.html)

- Ned Batchelder
- When answering questions. Lots of great advice. We’ll focus on just a few here.
	- **Answer the question first.** There may be other problems with their code that they are not asking about that you want to point out. But keep that for after you’ve helped them and built up trust.
	- **No third rails. “**It should be OK for someone to ask for help with a program using sockets, and not have to defend using sockets, especially if the specific question has nothing to do with sockets.” Same for pickle, threads, globals, singletons, etc. Don’t let your strong opinions derail the conversation. The goal is to help people. Strong reactions can make the asker feel attacked.
	- **No dog-piling.**
	- **Meet their level. “**Try to determine what they know, and give them a reasonable next step, not the ultimate solution. A suboptimal solution they understand is better than a gold standard they can’t make use of.”
	- Say yes.
	- Avoid absolutes.
	- Step back.
	- Take some blame.
	- **Use more words. “**IRC and other online mediums encourage quick short responses, which are exactly the kinds of responses that will be easy to misinterpret. Try to use more words, especially encouraging optimistic words.”
	- Understand your motivations.
	- Humility.
	- Make connections.
	- Finally: It’s hard.
- All of Ned’s advice is great. Good meditations for when you read a question and your mouth drops open and your eyes stare in shock. 

**Michael #2: [blackcellmagic](https://github.com/csurfer/blackcellmagic)**

- IPython magic command to format python code in cell using [black](https://github.com/ambv/black).
- Has a great animated gif ;)
- Just do: `%load_ext blackcellmagic`
- Then in any cell `%%black` and magic!
- Accepts “arguments” like `%%black -l 79`
- Tobin Jones has been kind enough to develop a NPM package over blackcellmagic to format all cells at once which can be found [here](https://github.com/tobinjones/jupyterlab_formatblack). But it’s archived so no idea whether it’s current.

**Brian #3:** [**Test smarter, not harder**](https://lukeplant.me.uk/blog/posts/test-smarter-not-harder/)

- Luke Plant
- There’s lots of great advice in here, but I want to highlight two parts that are often overlooked.
- “Write your test code with the functions/methods/classes you wish existed, not the ones you’ve been given.” “If the API you want to use doesn’t exist yet, you still use it, and then make it exist.”
    - This is huge. 
    - People tend to think like this while coding, but forget to do it while testing.
    - Also. Your tests are often the first client for your API, so if the API in question is under your control and you need an easier API for testing, consider adding it to the real API. If it’s easier for testing, it may be easier for other clients of the API as well.
- “Only write necessary tests — specifically, tests whose estimated value is greater than their estimated cost. This is a hard judgement call, of course, but it does mean that at least some of the time you should be saying “it’s not worth it”.”

Michael #4: [**US: The Greatest Package in the World**](https://github.com/unitedstates/python-us)

- by Jeremy Carbaugh
- A package for easily working with US and state metadata:
- all US states and territories
- postal abbreviations
- Associated Press style abbreviations
- FIPS codes
- capitals
- years of statehood
- time zones
- phonetic state name lookup
- is contiguous or continental
- URLs to shapefiles for state, census, congressional districts, counties, and census tracts
- The state lookup method allows matching by FIPS code, abbreviation, and name
- Even a CLI: `$ states md` 

**Brian #5:** [**Think Like A Coder**](https://t.co/6v25yMDtBZ?amp=1)

- Part of TED-Ed
- “… a 10-episode series that will challenge viewers with programming puzzles as the main characters— a girl and her robot companion— attempt to save a world that has been plunged into turmoil.”
- Although, I only count 9 episodes, I was 4 episodes in and hooked. 
- Main cool thing, I think, is introducing terms and topics so they will be familiar when someone really does start coding:
	- loops, for loops, until loops, while loops
	- conditionals
	- variables
	- path logic
	- permutations
	- searches
	- tables
	- recursion
	- Big O
- Also highly recommended for getting excited about coding:
	- [Girls Who Code: Learn to Code and Change the World](https://www.amazon.com/Girls-Who-Code-Learn-Change/dp/042528753X)
- [TED-Ed has tons of other cool series on lots of subjects](https://www.youtube.com/teded/playlists).
- CodeCombat

Michael #6: [**Costs of running a Python web app for 55k monthly users**](https://keepthescore.co/blog/posts/costs-of-running-webapp/)

- How much does running a web app in production actually cost? 
- KeepTheScore is an online software for scorekeeping. Create your own scoreboard for up to 150 players and start tracking points. It's **mostly free** and requires no **user account.**
- [Keepthescore.co](http://Keepthescore.co) is a Python flask application running on DigitalOcean and Firebase. It currently has around 55k unique visitors per month, per day it’s around 3.4k.
- Servers and database on DigitalOcean: Costs per month: $95, the servers are oversized for the load they’re currently seeing.
- Amazon Web Services: Costs per month: $60, use a reporting tool called Metabase to generate insights and reports from the database
- Google Cloud, costs per month: $1.32, for Firebase
- DNS hosting, costs per month: $5
- Disqus, costs per month: $10
- Is it worth it? Is there revenue?
- In total that’s around $171 USD per month. If you’re running a company with employees that would be peanuts, but in this case the cost is being borne by a single indie-developer out of his own pocket.
- The bigger issue is that on the revenue side there’s a big fat zero. This is the reason why we are currently working on monetization. 
- **Some Talk Python stats:**
- Maybe 40k monthly visitors, but oh, the podcast clients
- 3M requests / month just RSS, resulting in 320 GB / mo of XML traffic.
- We run on two prod servers: $10 & $5 as well as a dedicated MongoDB server @ $10. Total $25/mo.
- On the other hand, [Talk Python Training](https://training.talkpython.fm)'s AWS bill last month was over $1,000 USD.
- You can hear a bunch about this on [**Talk Python 215**](https://talkpython.fm/episodes/show/215/the-software-powering-talk-python-courses-and-podcast).

Joke:

- [From twitter, originally from Netlify:](https://twitter.com/AikidoUke/status/1306167769558396929?s=20) 
    - "Oh no! We lost the hackers! Where did they go?"
    - "I don't know! They just ransomware!”

- Number of days since I have encountered an array index error: -1.
