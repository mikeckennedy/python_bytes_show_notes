# Python Bytes 42
Sponsored by DataDog! [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)


**Brian #1:**  **What Kenneth Did Last Week (well, recently)**

  - Kenneth Reitz
	- Homebrew Python Tap
		  - Python 2.5 through 3.6 available through homebrew 
		  - [https://github.com/kennethreitz/homebrew-pythons](https://github.com/kennethreitz/homebrew-pythons)
		  - ```
		    $ brew tap kennethreitz/pythons
		    $ brew install python-2.5
		    ```
	- [https://github.com/requests/requests-threads/](https://github.com/requests/requests-threads/)
		  - “ Twisted Deferred Thread backend for Requests.”
		  - Can be used with async/await or with twisted.
	- [https://github.com/kennethreitz/background](https://github.com/kennethreitz/background)
		  - “Runs things in the background.”
	- [https://github.com/kennethreitz/setup.py](https://github.com/kennethreitz/setup.py)
		  - “setup.py (for humans)”
		  - “This repo exists to provide an example setup.py file, that can be used to bootstrap your next Python project. It includes some advanced patterns and best practices for setup.py, as well as some commented–out nice–to–haves.”
	  

**Michael #2:** [**Python 2 Death Clock**](https://pythonclock.org/)

- Python 2.7 will not be maintained past 2020. 
- No official date has been given, so this clock counts down until April 12th, 2020, which will be roughly the time of the 2020 PyCon.
- I am hereby suggesting we make PyCon 2020 the official end-of-life date, and we throw a massive party to celebrate all that Python 2 has done for us.
- Python 2, thank you for your years of faithful service.
- Python 3, your time is now.

**Brian #3:** [**Small Functions considered Harmful**](https://medium.com/@copyconstruct/small-functions-considered-harmful-91035d316c29)

- Cindy Sridharan
- "General programming advice doled out invariably seems to extoll the elegance and efficacy of small functions."
- This is sometimes pushed to the extreme of having one line functions that are only called from one place. Understand that doing this increases your code size by 4 lines every time you do it.
  - 1 line for the function call isn't removed because you moved the guts into a function.
  - 2 lines for function definition and guts
  - 2 lines to properly space your new function around other functions.
- Supposed Benefit: Do one thing; a function should only ever do one thing and do it well.
- Problems:
  - "Instead of a reasonably airtight abstraction that can be understood (and tested) as a single unit, we now end up with even smaller units that’ve been carved out to delineate each and every component of “the one thing” until it’s fully modular and entirely DRY."        
  - "...pragmatism and reason are sacrificed at the altar of a dogmatic adherence to DRY, ..."
  - premature abstractions. breaking up the code into smaller functions before you really understand the problem space can make it harder to refactor later.
  - micro-functions tend to have longer names because you need more names. Longer names aren't always a good thing when you have many long names on a page.
  - loss of locality: One bit of functionality that used to be in one function is now spread across many functions and possibly moved far away from use.
  - class pollution: class interfaces grow with smaller functions and hide the real intended interface.
  - harder to read, especially for newcomers.
- There is still a place for small functions. But use it in moderation. Communicating with future developers clearly is more important than following dogmatic rules about function size.


**Michael #4:** [**Why Python 3**](http://whypy3.com/)

-  All the cool Python 3 features that'll make you switch today!
- Presented as a random code sample surprise
- Examples:
	  - Annotations: `def my_add(a: int, b: int) -> int`
	  - Keyword only arguments: `def f(a, b, *args, option=True)`
	  - Yield from: `yield from range(5)`
	  - Enums: `class Color(Enum)`

**Brian #5:** **EANABs**

- Equally Attractive Non-Alcoholic Beverage
- There is drinking that happens often when you get a bunch of adults together. Often with work or tech gatherings. That’s fine. But make sure you emphasize that drinking is not required. 
- [@treyhunner](https://twitter.com/treyhunner) [brought it up recently](https://twitter.com/treyhunner/status/896081298581635072) and suggested that all conferences and tech events should have this.
	  - "I sometimes feel excluded when events include nice alcohol but only cheap soda"
	- [Stanford site](https://alcohol.stanford.edu/alcohol-drug-info/staying-safe/eanabs) has a bunch of great recipes.
	  - “EANABS are required at all Stanford parties, …”
	- If you have specialty local beers, try to find specialty local sodas.
	- If you have nice spiked punch, have a NA version also.
	- If you have cocktails, advertise your ability to serve mocktails. 

**Michael #6:**  [**The Incredible Growth of Python**](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)

- via StackOverflow
- Recently explored how wealthy countries (those defined as high-income by the World Bank) tend to visit a different set of technologies than the rest of the world. 
- Largest differences we saw was in the programming language Python. 
- High-income countries, the growth of Python is even larger than it might appear from tools like Stack Overflow Trends, or in other rankings.
- [StackOverflow] makes the case that Python has a solid claim to being the fastest-growing major programming language.
- June 2017 was the first month that Python was the most visited tag on Stack Overflow within high-income nations. (Grown has grown by 2.5-fold since 2012)
- **Python compared to smaller, growing technologies** graph is incredible.
- Also: [**Python overtakes R, becomes the leader in Data Science, Machine Learning platforms**](http://www.kdnuggets.com/2017/08/python-overtakes-r-leader-analytics-data-science.html)
