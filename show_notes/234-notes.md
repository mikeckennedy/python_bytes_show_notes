# Python Bytes 234

Sponsored by Sentry:

- Sign up at [**pythonbytes.fm/sentry**](https://pythonbytes.fm/sentry)
- And please, when signing up, click ***Got a promo code? Redeem*** and enter **PYTHONBYTES**

Special guest: [**Dr. Becky Smethurst**](https://www.youtube.com/c/DrBecky)

**Brian #1:** [**Powering the Python Package Index in 2021**](https://dustingram.com/articles/2021/04/14/powering-the-python-package-index-in-2021/)

- Dustin Ingram
- A lot has changed in 5 years since the previous write-up
- From 3 people to 
	- 3 maintainers/admins
	- 5 moderators
	- 3 commiters
- Companies donate about $1.8M per month in services
	- Fastly, mostly
	- Google Cloud ~ $10K
	- AWS ~ $7K
	- Also Statuspage, Sentry, Datadog, Digicert, Pingdom
- Awesome grants to fund projects
	- rewrite of PyPI
	- Localization, internationalization, API tokens and 2FA
	- Malware Detection and Update Framework
	- Foundational Tool Improvements & Productionized Malware Detection
	- Support Staff (a project manager)
- Growth, now up to (per day)
	- 1.7 B requests pypi
	- 55.4 TB pypi
- Next steps
	- [FUNDABLES.md](https://github.com/psf/fundable-packaging-improvements/blob/master/FUNDABLES.md), which is a non-exhaustive wishlist of large projects we’d like to see happen
	- become a member, donate, or volunteer

**Michael #2:** [**The Leuven Star Atlas**](https://papics.eu/?p=3969)

- via [**Shahrin Ahmad**](https://twitter.com/shahgazer/status/1392431981288321024)
- Making a publication-quality stellar atlas from scratch
- **Plotting one page of the atlas:** There is one single python script that takes care of the plotting of a single page of the atlas (plot_map.py). At the moment it is 1545 lines long
- The goal was to produce a publication quality, both practical and visually pleasing star atlas aimed at amateur astronomers.
- Took about 1.5 months to build/develop
- **Libraries used:**
- [numpy](http://www.numpy.org) for all kinds of data handling and numerical operations
- [pylab / matplotlib](http://matplotlib.org/index.html) for all the main plotting operations
- [basemap](http://matplotlib.org/basemap/) for the mapping (takes care of the projection and the related transformations)
- [scipy](https://www.scipy.org) for some specific interpolations and contours connected to the Milky Way
- [astropy](http://www.astropy.org) and [pyephem](http://rhodesmill.org/pyephem/) for celestial coordinate transformations
- **Source data**: All databases that I am using are either publicly available from the internet (under various licenses), or they are compiled by me from publicly available data (links in the article)
- One of the main new features of my atlas (compared to other atlases on the market) is the inclusion of the (as) precise (as possible) contours of the Milky Way on its pages.
- Interesting library: [adjustText](https://github.com/Phlya/adjustText) - automatic label placement for `matplotlib`
- The whole process takes around 4 hours on my laptop (using 4 cores in parallel).
- Whole thing reminds me of the quote: “Data cleanin√g isn’t grunt work, it is THE work.”

**Becky #3:** *[**TI-84 Plus CE Python graphing calculator**](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-plus-ce-python)

- I remember being so attached to my graphica calculator at school and I swear I haven’t used it since I was 18 - they were banned from my university exams 
- Remember very pixelated screen, almost like an original GameBoy, and plotting was the worst - but what if could have colour plots in Python
- Teaching kids to code early is so important, but learning to code with no purpose is also incredibly difficult. Learn alongside everything else makes it second nature and when something is second nature it becomes a tool you can use to solve a whole host of problems

**Brian #4:** [**Python Package CI/CD with GitHub Actions**](https://forcepush.tech/python-package-ci-cd-with-git-hub-actions)

- Johanan Idicula
- Nice write up of working with GH Actions
- Triggers from push or pull request
- Matrix runs
	- Running jobs across different build environenments
    - ubuntu
    - macos
    - windows
	- Diff python versions
- Caching some tools to not have to load them for each combination
	- example caches Poetry
- Running tests, of course
- Checking artifacts
- Auto-merge some branches
- Release automation to pypi on ‘v*’ tag pushes


**Michael #5:** [**SpaceX is using Python for prototyping their Starlink satellite software**](https://stackoverflow.blog/2021/05/11/building-a-space-based-isp/)

- via [**Garett Dunn**](https://twitter.com/garettmd/status/1392532914865418245)
- From [**four-part series on the software that powers SpaceX**](https://stackoverflow.blog/tag/software-in-space/)
- The software breaks down roughly into two parts: **1) software that flies** and **2) software that supports the flying components**.
- For Starlink, one of the main challenges is that our “towers” are orbiting Earth, forcing your path to the internet to change very frequently.
- The Earth-side network then provides continuous updates on traffic conditions and constellation changes, while each satellite updates the ground on its planned trajectory.
- Starlink software, both in satellites and on the ground, is written almost exclusively in C++
- But the prototyping is done in … Python.
- The software is developed in a continuous integration environment, with teams merging into the master development branch often and deploying to the fleet of satellites in space each week. 
- Live view [**findstarlink.com**](https://findstarlink.com/#1589;3) **and** [**starlink.sx**](https://starlink.sx/) **and** [**starlinkradar.com/livemap.html**](https://starlinkradar.com/livemap.html)
- The Python version allows for rapid iteration during the design phase. Once we are happy with the results of an algorithm, we port it to C++ so it runs efficiently in production.

**Becky #6:**: **[A beginner’s guide to working with astronomical data](https://arxiv.org/pdf/1905.13189.pdf)**
- it’s a scientific paper but huge sections on using Python to analyse images, remove noise, all the steps needed not just for me as professional but one I hope amateurs will find useful too
- Huge shoutout to astropy, Michael mentioned it before, revolutionised the field but also those keen amateur astrophotographers who perhaps use a Raspberry Pi to drive their telescope or to analyse their images


**Extras**

**Michael**

- [**Python for Astronomy with Dr. Becky episode**](https://talkpython.fm/episodes/show/303/python-for-astronomy-with-dr.-becky) on Talk Python
- [**KFocus laptops**](https://pythonbytes.fm/focus) a company looking to build software + hardware stack kind of like Apple with macOS. Very focused on AI workloads and high-end GPUs (e.g. [**3080**](https://www.officedepot.com/a/products/7189374/PNY-GeForce-RTX-3080-10GB-GDDR6X/?cm_mmc=Affiliates-_-CJ-_-5263653-_-13474833&utm_medium=affiliate&cjevent=5342e96cb83511eb825400b30a1c0e0b&siteid=CJ_13474833_100120709_dc1-kls-prod-srv-01.prod.dc1.kelkoo.net_1621382471619_634751&utm_source=cj&utm_campaign=ODOMX%20Google%20Feed_Kelkoo.com%20&#40;UK&#41;%20Ltd))

**Becky**

- [**Books**](https://www.amazon.com/Dr-Becky-Smethurst/e/B07RGQWS7N%3Fref=dbs_a_mng_rwt_scns_share)! 

**Joke** 


- [Uber](https://instaglobal.co/wp-content/uploads/2019/09/Funny-Space-Nasa-Memes.jpg)
- [Flaws](https://cdn.acidcow.com/pics/20181217/space_memes_27.jpg)
- [Distracted](http://s2.quickmeme.com/img/db/db376bf097275c58fb2f677189c1ab3409fc6a8b7679b8b92ae63000c24ebd1d.jpg)
- [Space-Vegas](https://piximus.net/media2/55523/space-memes-18.jpg)
