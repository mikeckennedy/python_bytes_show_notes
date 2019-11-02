# Python Bytes 155

Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog) 

**Michael #1:** [**Guido retires**](https://twitter.com/gvanrossum/status/1189546865114529792)

- Guido van Rossum has left DropBox and retired ([post](https://blog.dropbox.com/topics/company/thank-you--guido))
- Let’s all take a moment to say thank you.
- I wonder what will come next in terms of creative projects
- Some comments from community members (see [Twitter thread](https://twitter.com/gvanrossum/status/1189546865114529792))

**Brian #2:** [**SeleniumBase**](https://github.com/seleniumbase/SeleniumBase)

- Automated UI Testing with [Selenium WebDriver](https://www.seleniumhq.org/) and [pytest](https://docs.pytest.org/en/latest/).
- Very expressive and intuitive automation library built on top of Selenium WebDriver. [method overview](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/method_summary.md)
- very readable (this is a workflow test, but still, quite readable):
    from seleniumbase import BaseCase
    
```
    class MyTestClass(BaseCase):
        def test_basic(self):
            self.open("https://xkcd.com/353/")
            self.assert_title("xkcd: Python")
            self.assert_element('img[alt="Python"]')
            self.click('a[rel="license"]')
            self.assert_text("free to copy and reuse")
            self.go_back()
            self.click("link=About")
            self.assert_text("xkcd.com", "h2")
            self.open("https://store.xkcd.com/collections/everything")
            self.update_text("input.search-input", "xkcd book\n")
            self.assert_exact_text("xkcd: volume 0", "h3")
```

- includes plugins for including screenshots in test results.
- supports major CI systems
- some cool features that I didn’t expect
	- user onboarding demos
	- assisted QA (partially automated with manual questions)
	- support for selenium grid
	- logs of command line options, including headless


**Michael #3:** [**Reimplementing a Solaris command in Python gained 17x performance improvement from C**](https://blogs.oracle.com/solaris/reimplementing-a-solaris-in-python-gained-17x-performance-improvement-from-c)

- Postmortem by Darren Moffat
- Is Python slow?
- A result of fixing a memory allocation issue in the [/usr/bin/listusers](https://docs.oracle.com/cd/E88353_01/html/E37839/listusers-1.html#scrolltoc) command
- Decided to investigate if this ancient C code could be improved by conversion to Python.
- The C code was largely untouched since 1988 and was around 800 lines long, it was written in an era when the number of users was fairly small and probably existed in the local files /etc/passwd or a smallish NIS server.
- It turns out that the algorithm to implement the listusers is basically some simple set manipulation.
- Rewrite of listusers in [Python 3](https://blogs.oracle.com/solaris/future-of-python-on-solaris) turned out to be roughly a 10th of the number of lines of code
- But Python would be slower right ?  Turns out it isn't and in fact for some of my datasets (that had over 100,000 users in them) it was 17 times faster.
- A few of the comments asked about the availability of the Python version.  The listusers command in Oracle Solaris 11.4 SRU 9 and higher.  Since we ship the /usr/bin/listusers file as the Python code you can see it by just viewing the file in an editor.  Note though that is not open source and is covered by the Oracle Solaris licenses.

**Brian #4:** ****[**20 useful Python tips and tricks you should know**](https://dev.to/duomly/20-useful-python-tips-and-tricks-you-should-know-3h8c)

- I admit it, I’m capable of getting link-baited by the occasional listicle.
- Some great stuff, especially for people coming from other languages.
	- Chained assignment: `x = y = z = 2`
	- Chained comparison: 
		- `2 < x <= 8`
		- `2 < x > 4`
		- `0 < x < 4 < y < 16`
- Multiple assignment: `x, y, z = 2, 4, 8`
- More Advanced Multiple Assignment: `x, *y, z = 2, 4, 8, 16`
	- I’ve been using the * for unpacking a lot, especially with `*_`
- Merge dictionaries: `z = {**x, **y}`
- Join strings: `'_'.join(['u', 'v', 'w'])`
- using `list(set(something))` to remove duplicates.
- aggregate elements. using zip to element-wise combine two or more iterables. 
```
    >>> x = [1, 2, 3]
    >>> y = ['a', 'b', 'c']
    >>> zip(x, y)
    [(1, 'a'), (2, 'b'), (3, 'c')]
```

- and then some other weird stuff that I don’t find that useful.

Michael #5: [Complexity Waterfall](https://sobolevn.me/2019/10/complexity-waterfall)

- via [Ahrem Ahreff](https://twitter.com/AikidoUke/status/1186691544952266759)
- Heavy use of [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
- Code smells!
- Use your refactoring tools and write tests.
- Automation enable an opportunity of “Continuous Refactoring” and “Architecture on Demand” development styles.

**Brian #6:** [**Plynth**](https://www.plynth.net/)

- Plynth is a GUI framework for building cross-platform desktop applications with HTML, CSS and Python.
- Plynth has integrated the standard CPython implementation with Chromium's rendering engine. You can run your python scripts seamlessly with HTML/CSS instead of using Javascript with modules from pip
- Plynth uses Chromium/Electron for its rendering. With Plynth, every Javascript library turns into a Python module.
- Not open source. But free for individuals, including commercial use and education.
- A bunch of tutorial videos that are not difficult to follow, and not long, but… not really obvious code either. 
- Python 3.6 and 3.7 development kits available

Extras:

Michael: 

- [Google Is Uncovering Hundreds Of Race Conditions Within The Linux Kernel](https://www.phoronix.com/scan.php?page=news_item&px=Google-KCSAN-Sanitizer)

Joke:

- **Q**: What's a web developer's favorite tea?
- **A**: URL gray
- via Aideen Barry


