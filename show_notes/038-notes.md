# Python Bytes 38


**Matt #1: [Hacking Classic Nintendo Games with Python](https://www.youtube.com/watch?v=v75rNdPukuI) [](https://www.youtube.com/watch?v=v75rNdPukuI)**

- Gist: used the FCEUX ([http://www.fceux.com/web/home.html](http://www.fceux.com/web/home.html)) Nintendo emulator’s debugger to hex edit memory and change what’s happening during play
- Hex changing is how the old school Game Genie worked
- Given by my Twilio colleague Sam Agnew at PyCon 2017, and all the talks are up on YouTube
- Sam was inspired by Guto Maia’s PyNES: [https://gutomaia.net/pyNES/](https://gutomaia.net/pyNES/)
- Sam uses the Lua programming language to automate changing the Mario and Zelda’s hex values. 
- He then creates a Flask app where PyCon attendees could send a text message containing a hex address and 2 digit hex value to a phone number. the input would then be read into the game as he was playing
- What I particularly enjoyed about this talk is that it takes a bunch of topics that sound really complicated, like hex editing memory values, and makes it more accessible to less experienced developers because they can see the results
- Follow along with this blog post: [https://www.twilio.com/blog/2015/08/romram-hacking-building-an-sms-powered-game-genie-with-lua-and-python.html](https://www.twilio.com/blog/2015/08/romram-hacking-building-an-sms-powered-game-genie-with-lua-and-python.html)


**Brian** **#2**: [**The Pac-Man Rule at Conferences**](http://ericholscher.com/blog/2017/aug/2/pacman-rule-conferences/)

- by Eric Holscher
- “When standing as a group of people, always leave room for 1 person to join your group.”
- “Leaving room for new people when standing in a group is a physical way to show an inclusive and welcoming environment. “

**Matt #3:** **Bokeh**

- Python data visualization library where the visualization output is designed for presentation in web browsers
- Just released v0.12.6 in June, which has a slew of improvements. awesome development team and constantly improving
- v0.12.6 is last planned release before 1.0
- Wide range of visualizations you can create with Bokeh, including classic ones just bar charts box plots, and also interactive visuals
- Basically if you thought d3.js visualizations were awesome but didnt want to spend that much time hand crafting some complicated JavaScript, Bokeh will be your jam
- Flask-based tutorial: [https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html](https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html)

**Brian #4:** [**Mosh (mobile shell)**](https://mosh.org/)

- Persuasive video: [https://www.youtube.com/watch?v=XsIxNYl0oyU](https://www.youtube.com/watch?v=XsIxNYl0oyU) from 2012
- From the main page:
  - Remote terminal application that allows **roaming**, supports **intermittent connectivity**, and provides intelligent **local echo** and line editing of user keystrokes.
  - Mosh is a replacement for SSH. It's more robust and responsive, especially over Wi-Fi, cellular, and long-distance links.
  - Mosh is free software, available for GNU/Linux, BSD, macOS, Solaris, Android, Chrome, and iOS.
- This has been around since 2012. I just heard of it. Are people using it?

**Matt** **#5:** [**Pelican static site generator**](https://github.com/getpelican/pelican/tree/3.7.1)

- Static site generators take in a markup format such as reStructuredText or Markdown, along with a template engine such as Jinja and output HTML (or XML, JSON, etc) files that can be hosted anywhere
- It’s kind of a throw back to the early days of the web when everything was snappy
- Major new version 3.7.0 released at the end of 2016 with a minor v3.7.1 bump released early this year
- Lots of improvements to Python 3 compatibility. I use Pelican with Python 3.6.2. exclusively now.
- Significant customization by changing the configuration files.
- Lots of folks think static site generators are just for blogs, which is what most of the original static generators were built to create, but you really can create any type of site, including single page apps (when you combine a static site generator with a front end JavaScript framework).
- Just wrote a getting started tutorial: [How to Create Your First Static Site with Pelican and Jinja2](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html)

**Brian** **#6:**  [**pytest-watch**](https://pypi.python.org/pypi/pytest-watch)

- [pytest 3.2.0](https://docs.pytest.org/en/latest/changelog.html) was released recently.
- Great for pytest users. Bummer for me that just recently tested all the code examples in the [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) book against pytest 3.1.3.
- So I wrote a bunch of tests to check every invocation of pytest in the book.
- I’m running it against both pytest 3.1.3 and pytest 3.2.0
- I’m automating this by running both versions every time I save a new test with pytest-watch
```
    $ pip install pytest-watch
    $ cd <test directory>
    $ ptw .
```
- Run `ptw .` in two windows, each with a virtualenv with different pytest versions, and I can test both constantly as I save tests.
- Will later convert this to tox, but for now, this is a huge timesaver.

**(bonus) Matt #7: [Twilio Voices](http://www.twiliovoices.com)**

- New program where you get paid $500 for each published technical blog post you write for the Twilio blog. Every post has the code and walks the reader through how to recreate something you built.
- Examples: [Wedding at Scale](https://www.twilio.com/blog/2017/04/wedding-at-scale-how-i-used-twilio-python-and-google-to-automate-my-wedding.html), [How I Hack My University Registration System](https://www.twilio.com/blog/2017/06/hacked-my-universitys-registration-system-python-twilio.html)
- Tell stories with code
- We put each post through a rigorous outline, voice and tech review process
- Doesn’t have to use Twilio, so you can write a post on pytest-watch, Mosh, Pelican, Bokeh, or any other library you’ve been meaning to work with and get paid when the post is published
- This is what I’ve been working on at Twilio for the past couple of months so we’ll work directly together on the posts




