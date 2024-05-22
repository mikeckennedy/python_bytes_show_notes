# Python Bytes 56
Sponsored by Rollbar! [pythonbytes.fm/rollbar](https://pythonbytes.fm/rollbar)

**Brian #1:** [**Pendulum**](https://pendulum.eustace.io/) **for datetimes**

- [on github](https://github.com/sdispater/pendulum)
- See also
  - [arrow](http://arrow.readthedocs.io/en/latest/)
  - [maya](https://github.com/kennethreitz/maya)
  - [datetime](https://docs.python.org/3/library/datetime.html), and [Dealing with datetimes like a pro in Python](https://codeburst.io/dealing-with-datetimes-like-a-pro-in-python-fb3ac0feb94b)
  - [dateutil](https://dateutil.readthedocs.io/en/stable/)

**Michael #2:** [**Flask asynchronous background tasks with Celery and Redis**](http://allynh.com/blog/flask-asynchronous-background-tasks-with-celery-and-redis/)

- Easiest way to a significant scalability to your app: queuing
- What is Celery: Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well
- How Celery works:
  - Celery client: This will be connect your Flask application to the Celery task
  - Celery worker: A process that runs a background task
  - Message broker: The Celery client communicates to the Celery worker through a message broker (redis in this case)
- All examples on Windows 

**Brian #3:** [**Building a Simple Web App With Bottle, SQLAlchemy, and the Twitter API**](https://realpython.com/blog/python/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/)

- Guest article on RealPython, by [Bob Belderbos](https://twitter.com/bbelderbos) of [PyBytes](https://twitter.com/PyBytes)
- Fun full project start to finish using [Tweepy](https://github.com/tweepy/tweepy) to load tweets.
- Ends with a bottle app running on Heroku

**Michael #4:** [**Python extension for VSCode updated, now brought to you by Microsoft**](https://www.reddit.com/r/vscode/comments/7burdg/python_extension_for_vscode_updated_now_brought/)

- Don Jayamanne, creator of the Python extension for Visual Studio Code, joins Microsoft
- Full announcement: **[https://blogs.msdn.microsoft.com/pythonengineering/2017/11/09/don-jayamanne-joins-microsoft/](https://blogs.msdn.microsoft.com/pythonengineering/2017/11/09/don-jayamanne-joins-microsoft/)**
- Had Don on Talk Python back on [**episode 101**](https://talkpython.fm/episodes/show/101/adding-a-full-featured-python-environment-to-visual-studio-code).
- What does Microsoft Python team publishing the extension mean?
- For all practical purposes the transition should be transparent to you. Additionally:
  - The extension will remain open source and free
  - Development will continue to be on GitHub, under the existing license
  - More dev resources means (generally) faster turnaround on bug fixes and new features
- Microsoft is hiring for Visual Studio Code / Python! They are hiring devs immediately to continue and expand work on our Python support for Visual Studio Code. If you are passionate about developer tools and productivity, this could be an ideal endeavor!

**Brian #5:** [**A Comprehensive Guide To Web Design**](https://www.smashingmagazine.com/2017/11/comprehensive-guide-web-design/)

- Crash course in web design principles, not the mechanics

**Michael #6:** [**Requestium**](https://github.com/tryolabs/requestium)

- Integration layer between Requests and Selenium for automation of web actions.
- Merges the power of [Requests](https://github.com/requests/requests), [Selenium](https://github.com/SeleniumHQ/selenium), and [Parsel](https://github.com/scrapy/parsel) into a single integrated tool for automatizing web actions.
- The library was created for writing web automation scripts that are written using mostly Requests but that are able to seamlessly switch to Selenium for the JavaScript heavy parts of the website, while maintaining the session.
- Features
  - Enables switching between a Requests' Session and a Selenium webdriver while maintaining the current web session.
  - Integrates Parsel's parser into the library, making xpath, css, and regex much cleaner to write.
  - Improves Selenium's handling of dynamically loading elements.
  - Makes cookie handling more flexible in Selenium.
  - Makes clicking elements in Selenium more reliable.
  - Supports Chrome and PhantomJS.

**Our news**

- [Test & Code 33: Testing in Data Science with Kathrine Jarmul](http://testandcode.com/33)
- Thanks to the 9 folks to that have left an Amazon review for [Python Testing with pytest](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409#customerReviews). 
