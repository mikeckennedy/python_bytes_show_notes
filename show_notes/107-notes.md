# Python Bytes 107
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**glom: restructuring data, the Python way**](https://glom.readthedocs.io/en/latest/index.html)

- glom is a new approach to working with data in Python, featuring:
	- Path-based access for nested structure
		-  `data\['a'\]['b']['c']` → `glom(data, 'a.b.c')`
	- Declarative data transformation using lightweight, Pythonic specifications
		- `glom(target, spec, **kwargs)` with options such as
		  - a default value if value not found
		  - allowed exceptions
	- Readable, meaningful error messages:
		-  `PathAccessError: could not access 'c', part 2 of Path('a', 'b', 'c')` is better than
		- `TypeError: 'NoneType' object is not subscriptable`
	- Built-in data exploration and debugging features
		- `glom.Inspect(``**a*``,` `***kw*``)`
		- The `[**Inspect**](https://glom.readthedocs.io/en/latest/api.html#glom.Inspect)` specifier type provides a way to get visibility into glom’s evaluation of a specification, enabling debugging of those tricky problems that may arise with unexpected data.

**Michael #2:** [**Scientific GUI apps with TraitsUI**](http://docs.enthought.com/traitsui/)

- via Franklin Ventura
- They support: PyQt, wxPython, PySide, PyQt5
- People should be aware of and when combined with [Chaco](http://docs.enthought.com/chaco/user_manual/chaco_tutorial.html) (again from Enthought) the graphing and controlling capabilities really are amazing.
- Tutorial: [Writing a graphical application for scientific programming using TraitsUI 6.0](https://docs.enthought.com/traitsui/tutorials/traits_ui_scientific_app.html)
- Really simple UI / API for mapping object(s) to GUIs and back.

**Brian #3:** [**Pampy: The Pattern Matching for Python you always dreamed of**](https://github.com/santinic/pampy)

- “Pampy is pretty small (150 lines), reasonably fast, and often makes your code more readable and hence easier to reason about.”
- uses `_` as the missing info in a pattern
- simple `match` signature of `match(input, pattern, action)`

- Examples
  - nested lists and tuples

```
    from pampy import match, _
    
    x = [1, [2, 3], 4]
    match(x, [1, [_, 3], _], lambda a, b: [1, [a, 3], b])           # => [1, [2, 3], 4]
  - dicts:
    pet = { 'type': 'dog', 'details': { 'age': 3 } }
    match(pet, { 'details': { 'age': _ } }, lambda age: age)        # => 3
    match(pet, { _ : { 'age': _ } },        lambda a, b: (a, b))    # => ('details', 3)
```

**Michael #4:** [**Google AI better than doctors at detecting breast cancer**](https://www.sciencefocus.com/news/google-ai-better-than-doctors-at-detecting-breast-cancer/)

- Google’s deep learning AI called LYNA able to correctly identify tumorous regions in lymph nodes 99 per cent of the time.
- We think of the impact of AI as killing 'low end' jobs [see [poster](https://www.google.com/search?q=demotivator+robot&client=firefox-b-1-ab&tbm=isch&source=iu&ictx=1&fir=HY_0DIJRLAdG1M%253A%252CTopRdw4TesZqKM%252C_&usg=AI4_-kRZ13zsoCnKopq53qUGwZV3ho31EA&sa=X&ved=2ahUKEwjmpeOb8_DeAhWUKH0KHcTwDaAQ9QEwAHoECAUQBA#imgrc=scl2Ob_gs0DKUM:)], but these are "doctor" level positions.
- The presence or absence of these ‘nodal metastases’ influence a patient’s prognosis and treatment plan, so accurate and fast detection is important.
- In a second trial, six pathologists completed a diagnostic test with and without LYNA’s assistance. With LYNA’s help, the doctors found it ‘easier’ to detect small metastases, and on average the task took half as long.


**Brian #5:** [**2018 Advent of Code**](https://adventofcode.com/2018/about)

Another winter break activity people might enjoy is practicing with code challenges. AoC is a fun tradition.

- a calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.
- don't need a computer science background to participate
- don’t need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.
- There’s a leaderboard, so you can compete if you want. Or just have fun.
- Past years available, back to 2015.
- Some extra tools and info: [awesome-advent-of-code](https://github.com/Bogdanp/awesome-advent-of-code)

**Michael #6:** [**Red Hat Linux 8.0 Beta released, now (finally) updated to use Python 3.6 as default instead of 2.7**](https://www.reddit.com/r/Python/comments/9xms3u/red_hat_linux_80_beta_released_now_finally/)

- First of all, my favorite comment was a correction to the title: legacy python *
- “**Python 3.6 is the default Python implementation in RHEL 8**; limited support for Python 2.7 is provided. No version of Python is installed by default.“
	- Red Hat Enterprise Linux 8 is distributed with Python 3.6. The package is not installed by default. To install Python 3.6, use the yum install python3 command.
	- Python 2.7 is available in the python2 package. However, **Python 2 will have a shorter life cycle and its aim is to facilitate smoother transition to Python 3 for customers**.
	- Neither the default python package nor the unversioned /usr/bin/python executable is distributed with RHEL 8. **Customers are advised to use python3 or python2 directly.** Alternatively, administrators can configure the unversioned python command using the alternatives command. 
- **Python scripts must specify major version in hashbangs** at RPM build time
	- In RHEL 8, executable Python scripts are expected to use hashbangs (shebangs) specifying explicitly at least the major Python version. 

**Extras:**

Michael: We were [**featured on TechMeme**](https://art19.com/shows/techmeme-ride-home/episodes/eee1ffeb-c58e-468b-88b7-726f42c7a235) Long Ride Home podcast. Check out their [**podcast here**](https://art19.com/shows/techmeme-ride-home). Thank you to **Brian McCullough**, the host of the show. I just learned about their show through this exchange but can easily see myself listening from time to time. It’s like Python Bytes, but for the wider tech world and less developer focused but still solid tech foundations.

**Brian:** First story was about glom. I had heard of glom before, but got excited after interviewing Mahmoud for [T&C 55](https://testandcode.com/55), where we discussed the difficulty in testing if you use glom or DSLs in general. A twitter exchange and GH issue followed the episode, with Anthony Shaw. At one point, Ant shared this great joke from Brenan Kellar:


> A QA engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 99999999999 beers. Orders a lizard. Orders -1 beers. Orders a ueicbksjdhd. 
> 
> First real customer walks in and asks where the bathroom is. The bar bursts into flames, killing everyone.
> 
> — Brenan Keller (@brenankeller) [November 30, 2018](https://twitter.com/brenankeller/status/1068615953989087232?ref_src=twsrc%5Etfw)

