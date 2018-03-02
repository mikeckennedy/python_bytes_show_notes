# Python Bytes 67
Sponsored by DigitalOcean! [http://**do.co/python**](http://do.co/python)

**Brian #1:** [**Building a blog with Pelican**](http://pythonforundergradengineers.com/how-i-built-this-site-1.html)

- We did cover Pelican in [episode 38](https://pythonbytes.fm/episodes/show/38/hacking-classic-nintendo-games-with-python), but this is a nice tutorial in 7 parts on building a blog.
- Peter Kazarinoff, [@pkazarinoff](https://twitter.com/pkazarinoff)
	- Nice blog with a focus on engineering students.
- Starts with installing Python and git and some other tools.
- Step by step, every action to get a a blog up as a static site hosted on github pages.

**Michael #2:** [**Notifiers**](http://notifiers.readthedocs.io/en/latest/index.html) 

- Got an app or service and you want to enable your users to use notifications with their provider of choice? 
- Working on a script and you want to receive notification based on its output? 
- A one stop shop for all notification providers with a unified and simple interface.
- A unified interface means that you already support any new providers that will be added, no more work needed!
- Some providers
	- Slack
	- Gmail
	- Telegram
	- Gitter
	- …
- Python 3 only

**Brian #3:** [**Using Makefiles in Python projects**](https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html)

- Krzysztof Żuraw, [@krzysztof_zuraw](https://twitter.com/krzysztof_zuraw)
- Alerted to this article from kidpixo, [@kidpixo](https://twitter.com/kidpixo)
- We don’t usually think of Makefiles and Python together, but they can be a handy place to keep common scripts for a project all in one place.
- This article is a nice gentle intro to Makefiles and shows some cool uses:
	- cleaning out .pyc files
	- cleaning out egg directories
	- linting
	- running tests with flags
	- starting a test server
	- deploying
	- sorting import files

**Michael #4:** [**Result of moving Python to Github**](https://www.reddit.com/r/Python/comments/7qt4x3/result_of_moving_python_to_github/)

- See the graph linked in the post
- A couple of quick numbers (including PRs too) from 2017 compared to 2016:
	-     the number of commit has increased by 190%
	-     inserted lines of code has increased by 140%
	-     number of unique contributors has increased by 1300%
	-     number of returning contributors has increased by 900%
- One comment was: “Personally, I would like them moving to Gitlab instead, but still good news.” I tend to disagree.

**Brian #5:** [**Self-Deprecation Needs to**](https://dev.to/mauricehayward/-self-deprecation-needs-to---46fo) [**Stop**](https://dev.to/mauricehayward/-self-deprecation-needs-to---46fo)

- Maurice Hayward, [**@**](https://twitter.com/maurice_hayward)[maurice_hayward](https://twitter.com/maurice_hayward)
- Inspired by some tweets by Stephanie Hurlburt, [**@**](https://twitter.com/sehurlburt)[sehurlburt](https://twitter.com/sehurlburt)
1. **Stop saying these words when describing yourself or your accomplishments.** 
  These words are now under BAN:
  "My project is..."
		- very small/basic/simple
		- not that good
		- a thing I wrote
		- just by a newbie
		- something I didn't spend a lot of time/effort on
		- silly
		- not that useful
  Just state the topic and let others be the judge.
2. **Really think about the value you bring, then let everybody know.**
3. **Be Proud of Yourself!**

**Michael #6:** [**5 speed improvements in Python 3.7**](https://hackernoon.com/5-speed-improvements-in-python-3-7-1b39d1581d86)

1. **Calling methods faster (maybe)**
	1. Python 3.7 adds 2 new Opcodes, LOAD_METHOD and CALL_METHOD for when the compiler sees x.method(...) it uses these new Opcodes.
	2. Bound methods with no arguments are now faster
2. **str.find() is faster for some characters**
	1. Some unicode characters have an unfortunate issue when scanning a string for occurrences using str.find(x), seeing up to 25x slow down.
	2. These are still slower, but now 3x slower than ASCII characters instead of 25x!
3. **os.fwalk is 2x faster**
4. **Regular expressions are faster**
	1. A change was made in Python 3.6 which slowed down this call when flags were passed which were integers. Python 3.7 “fixes” the slowdown but is still not as fast as Python 3.5
5. **Regular expressions are faster for case-insensitive matching**
	1. The speed improvement is significant, if you’re matching ASCII characters you can see up to a 20x improvements in matching time since it’s now doing a lookup instead of running lower() over each character.

Follow up and other news

Brian: 

- [Python package maintainers, help test the new PyPI!](https://pyfound.blogspot.com/2018/02/python-package-maintainers-help-test.html)
- [pytest/pycharm webinar is up](https://blog.jetbrains.com/pycharm/2018/02/webinar-recording-productive-pytest-with-pycharm/). 

