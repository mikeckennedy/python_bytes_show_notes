# Python Bytes 312

Sponsored by [**Complier Podcast from RedHat**](https://pythonbytes.fm/compiler)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)

**Brian #1:** [**Coping strategies for the serial project hoarder**](https://simonwillison.net/2022/Nov/26/productivity/)

- Simon Willison
- Also a talk from DjangoCon2022
    - [Massively increase your productivity on personal projects with comprehensive documentation and automated tests.](https://www.youtube.com/watch?v=GLkRK2rJGB0)
- I’m actually not sure what title would be best, but this is an incredible video that I’m encouraging every developer to watch, whether or not you work with open source projects.
- Covers
    - The perfect commit
        - Implementation, Tests, Documentation, and a link to an issue thread
    - Tests
        - Prove the implementation works, pass if it works, fails otherwise
        - A discussion of how adding tests is way easier than starting testing a project, so get the framework in place early, and devs won’t be afraid to add to it.
    - Cookiecutter repo templates for projects you will likely start
        - super cool idea to have your own that you keep up to date with your preferred best practices
    - A trick for using GitHub actions to use those templates to populate new repos
        - Trying this out is on my todo list
    - Documentation must live in the same repo as the code
        - and be included in PRs for the PR to be accepted by code review
        - maybe even test this using documentation unit tests
    - Everything links to an issue thread
        - Keep all of your thoughts in an issue thread
        - Doesn’t have to be a dialog with anyone but yourself
        - This allows you to NOT HAVE TO REMEMBER ANYTHING
    - Tell people what you did
        - This is just as important in work projects as it is in open source
        - Blog about it 
        - Post on Twitter (or Mastodon, etc.)
    - Avoid side projects with user accounts
        - “If you build something that people can sign into, that’s not a side-project, it’s an unpaid job. It’s a very big responsibility, avoid at all costs!” - this is hilarious and something I’m probably not going to follow


**Michael #2:** [**GitHub copilot lawsuit**](https://githubcopilotlitigation.com/)

- First, we aren’t lawyers
- Lawsuit filed on November 3, 2022
- We’ve filed a lawsuit challenging GitHub Copilot, an AI product that relies on unprecedented open-source software piracy.
- GitHub copilot is trained on projects on GitHub, including GPL and other restrictive licenses
- This is the first class-action case in the US challenging the training and output of AI systems.

**Brian #3:** [**Use Windows Dialog Boxes from Python with no extra libraries**](https://mfcallahan.blog/2022/11/10/display-a-message-box-with-python-without-using-a-library-or-other-dependency-windows/)

- Actual title: **Display a message box with Python without using a non-standard library or other dependency (Windows)**
- By Matt Callahan / learned about from from PyCoders weekly
- When I need a simple pop up dialog box that’s cross platform, [PySimpleGUI](https://www.pysimplegui.org/en/latest/) is awesome and so easy.
- But when I KNOW it’s only going to run on Windows, why not just use native dialog boxes?
- Matt’s article shows you how, using [ctypes](https://docs.python.org/3/library/ctypes.html?utm_source=pocket_saves) to call into a Windows dll.
- Small example from article:

```
import ctypes
    
    def main():
        WS_EX_TOPMOST = 0x40000
        windowTitle = "Python Windows Message Box Test"
        message = "Hello, world!"
        # display a message box; execution will stop here until user acknowledges
        ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)
        print("User clicked OK.")
    
    if __name__ == "__main__":
        main()

```

-  Notes:
    - The uType (fourth) parameter is a multi-use value that can be or-ed for things like:
        - Type of dialog box: Help, OK, OK/Cancel, Retry/Cancel, Yes/No, etc.
        - The icon to use: Exclamation, Info, Question, etc.
        - Modality, …
    - Return value is used to understand how user reacted:
        - 1 - OK, 2 - Cancel (or x), …,  6 - Yes, 7 - No, …


**Michael #4:** **Extra Extra Extra**

- [**Python browser extensions**](https://twitter.com/pycoders/status/1593259414437478400) 
- [**takahe**](https://jointakahe.org) - Mastodon on Python - the right way
- [**Michael’s article in Black Friday perf**](https://mkennedy.codes/posts/black-friday-almost-melted-servers/) 
    - We could scale down our server after what I’ve learned. But we’d pay 10x more in bandwidth overages ironically: Last month Talk Python broadly transferred 20.2 TB of data from our servers
- Moved our static traffic to [**Bunny CDN**](https://bunny.net?ref=b4f3tqcyae), highly recommended service
- RSS revival 
    - My blog: [**mkennedy.codes**](https://mkennedy.codes) 
    - [**Reeder 5 app**](https://reederapp.com) on iOS and macOS
- Rivers Cuomo (from Weezer) and Guido [**sit down for a talk together**](https://www.singforscience.org/episodes/rivers-cuomo-guido-van-rossum)
    - Also check out the Talk Python episode with Rivers: [**talkpython.fm/327**](https://talkpython.fm/episodes/show/327/little-automation-tools-in-python)
- [**Kite is saying farewell**](http://www.libhunt.com/ahoy/messages/ARRuCh7igpeLGSpmZv3TX5meA1oAEq79/click?signature=487fbf5cec0d22c6fdf56d1cfccc493fac8d2044&url=https%3A%2F%2Fwww.kite.com%2Fblog%2Fproduct%2Fkite-is-saying-farewell)



