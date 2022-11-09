# Python Bytes 309


Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael: #0: Python Bytes is 6 years** old this week. Thank you!  🎉

**Michael #1:** [**Malicious proof-of-concepts are exposing GitHub users to malware and more**](https://portswigger.net/daily-swig/malicious-proof-of-concepts-are-exposing-github-users-to-malware-and-more)

- [**The paper**](https://arxiv.org/abs/2210.08374)
- They found that of the 47,313 GitHub repositories they had downloaded and checked, 4,893 (10.3%) were malicious.
- In some the attackers were trying to plant malware on users’ machines, while in others, they tried to open backdoors using CobaltStrike, for example
- Ignoring this problem can cause damage that ranges from infecting yourself as [a] user, to infecting your company and likely your customers as well if it’s a more sophisticated attack,” El Yadmani warned.
- Languages
    - Ruby 379 
    - Go 400 
    - JavaScript 548 
    - Shell 652 
    - C++ 962
    - Java 1071 
    - C 1686 
    - **Python 8305** 
    - Undetected 31858
- Example Python exfile script included in the paper

**Brian #2:** **The great Mastodon experiment**

- Context should be obvious re Twitter news.
- A lot of Python people have kept in touch via Twitter.
- A lot are now experimenting with [Mastadon](https://joinmastodon.org),
- What I did
    - asked Twitter people which server to use, then just picked fosstodon.org, but there are [many servers](https://joinmastodon.org/servers)
    - This is me:  [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
    - Michael got in too: **https://fosstodon.org/@mkennedy**
    - just started using it, following people, trying iOS clients, etc.
- Now I’m ready for some tutorials, and here’s a list that looks decent:
    - [An Increasingly Less-Brief Guide to Mastodon](https://github.com/joyeusenoelle/GuideToMastodon?utm_source=pocket_saves)
    - [Everything I know about Mastodon](https://blog.djnavarro.net/posts/2022-11-03_what-i-know-about-mastodon/#etiquette-on-cross-posting-from-twitter)
        - A hastily written guide for data science folks trying to navigate the fediverse.
    - [Mastodon is just blogs](https://simonwillison.net/2022/Nov/8/mastodon-is-just-blogs/) - Simon Willison is running his own server.
    - [Eight Mastodon apps for iPhone](https://transponderings.blog/2022/05/21/eight-mastodon-apps-for-iphone/) - I’m currently trying like 4, but you can also just log into your sever and do everything there.
    - [Fedi.Tips](https://fedi.tips) and their [Beginners Start Here](https://fedi.tips/mastodon-and-the-fediverse-beginners-start-here/) page


**Michael #3:** [**Gitpod and the traveling dev**](https://twitter.com/titimoby/status/1585566185961263104?s=12&t=4h7RIi-8kG9bjNWYyonA4Q)

- Gitpod is an open-source Kubernetes application for ready-to-code developer environments that spins up fresh, automated dev environments for each task, in the cloud, in seconds.
- Gitpod is paid, but there are decent free tiers
- [Features](https://github.com/gitpod-io/gitpod#features)
- Run a desktop or browser based version of VS Code or any JetBrains IDE and customise it to your individual needs - from themes to extensions, you have full control.

**Brian #4:** **Color in the terminal**

- pytest-check currently doesn’t use color
    - but a little red for failures would be good (and was requested via an issue)
- I could use [rich](https://pypi.org/project/rich/), but maybe that’s a slightly larger hammer than I need for this job
- Maybe raw escape sequences like `print('\033[31m' + 'some red text')`
    - kinda gross
    - won’t work out of the box on Windows.
- But [colorama](https://pypi.org/project/colorama/) can fix Windows.
    - It just recently added `just_fix_windows_console()`, which apparently works better than `init()` in that it can be called multiple times without blowing up. 
    - Includes easier to read codes for some basic colors, so this works:
```
from colorama import just_fix_windows_console
    from colorama import Fore, Style
    just_fix_windows_console()
    
    print(Fore.RED + 'some red text')
    print(Style.RESET_ALL)
    print('back to normal now')
```

**Extras** 

Brian:

- Simon Willison wrote [What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/?utm_source=pocket_saves), which includes 
    - TIL (today I learned) posts that don’t need to be full tutorials
    - Projects you’ve built
- I’d like to include
    - Projects in progress
    - Bug fixes or feature additions where you needed to learn a bit of something beforehand
        - Example: I should write up “Adding red to pytest-check”

Michael: 

- Beanie reorg: There is no sync version here more. Please use [Bunnet](https://github.com/roman-right/bunnet) instead
- https://twitter.com/nicholdav/status/1589643652598759424 ? 
- [**PyCon Days Breakdown**](https://twitter.com/mariatta/status/1589656718635839488)
- Been playing with GeForce now, really impressive. Meanwhile, why is google still selling stadia?
- New video: [**A Walrus Meets a Python - What is the := Walrus Operator?**](https://www.youtube.com/watch?v=kmAe3VUW3zU)
- New video: [**Python GC Settings - Change This and Go 20% Faster!**](https://www.youtube.com/watch?v=p4Sn6UcFTOU)

**Joke:**  [**Relaxation**](https://devhumor.com/media/pure-relaxation-server-sounds)

