Welcome to Python Bytes. Python headlines delivered directly to your earbuds. In this second episode we cover a couple of key python package releases, pycon, awesome python, python developer job prospects, and more!

## News items

[**Celery 4.0**](http://docs.celeryproject.org/en/latest/whatsnew-4.0.html)
- A task queue and scheduling subsystem
- Supposedly a massive release with over 2 years of changes
- Will be the last major release with Python 2.x support, already dropping 2.6

[**Psutil 5.0.0**](http://grodola.blogspot.com/2016/11/psutil-500-is-around-twice-as-fast.html)
- Used for process monitoring, system utilization, and other cross platform os things.
- We use it with some tools and it can be the bottleneck, so a speedup is very welcome.

[**Pytest 3.0.4**](http://doc.pytest.org/en/latest/changelog.html)
- Mostly a bug fix release. Check out the change log to see if you care about anything they fixed.
- Report teardown output on test failure. Already did report setup output.

[**Registration is open for PyCon 2017!**](http://us.pycon.org/2017/registration)
- Don't wait! Take advantage of the early bird discount 
- We are having a booth!

[**PyCon Tutorial proposals due on November 30**](http://pycon.blogspot.com/2016/11/tutorial-proposals-are-due-in-two-weeks.html)
- Tutorial proposals are due on 2017 November 30
- Talk proposals will be due on 2017 January 3
- Poster proposals will be due on 2017 January 3
We'll be hosting a Podcast open session


[**Github awesome-python**](https://github.com/vinta/awesome-python)
- A curated list of awesome Python frameworks, libraries, software and resources
- A sampling of the topic areas:
   - Authentication
   - Data Validation
   - Date and Time
   - Debugging Tools
   - Machine Learning
   - Search

[**Timing Tests in Python for Fun and Profit**](https://hackernoon.com/timing-tests-in-python-for-fun-and-profit-166314457)
- Fun example of how and why you'd ever want to customize a test runner.
- Final solution is pretty cool. However, I'm not sure if it includes setup/teardown time.
- BTW, pytest has this built in, `pytest --durations=0` time every setup, teardown, and test method. `pytest --durations=3` shows the slowest 3, etc. As well as shows the time of each. Also works on unittest code.

[**What's the Average Python Developer Salary in the US, and Why Is Python So Popular, Anyway?**](https://www.daxx.com/article/python-developer-salary-usa)
- 2015 and 2016 have been big years for Python. According to the 2016 Developer Survey by StackOverflow, Python ranks as the world's sixth most popular programming language for the second year in a row, and is also rated the fourth most wanted technology of the year.
- Python is also one of the hottest tech skills to have, according to research by Dice, with demand slightly outstripping supply.
- Python is one of the highest-paying programming languages in the USA. In fact, at $103,492 per year or by Indeed - $116,129
- Why?
   - The world's tech giants love it. 
   - With the rise of data science, Python's popularity as a scientific language has soared
   - It's perfect for beginners
   - It might just be the only language you need

## Our personal news

### Brian
- T&C #24: Raphael Pierzina, on cookie cutter, pytest 3.0, and contributing to both: [http://pythontesting.net/podcast/24-pytest-raphael-pierzina/](http://pythontesting.net/podcast/24-pytest-raphael-pierzina/) 
- T&C #25: Dave Hunt, recorded. Hope to get that out this week. We talk about his work on Selenium, pytest-selenium, pytest-html, tox, and how Mozilla does some of it's testing with these tools.
- Looking for more people to interview. A few in the pipeline, including David Hussman from [http://devjam.com/](http://devjam.com/), but I'd love suggestions. Doesn't have to be testing. I'll be talking to David about Dude's Law, his view of modern agile practices, and other high level topics.

### Michael
- [Python: An Amazing Second Language for .NET Developers on PyVideo](http://pyvideo.org/ndc-oslo-2016/python-an-amazing-second-language-for-dotnet-developers.html)
- [Mutation Testing in Python with Cosmic Ray on PyVideo](http://pyvideo.org/ndc-oslo-2016/mutation-testing-in-python-with-cosmic-ray.html)
- New content in my python for entrepreneurs course
85

