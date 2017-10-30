# Python Bytes 49
Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1: Conference videos for DjangoCon 2017 and PyGotham 2017**

- [PyGotham 2017 videos on pyvideo](http://pyvideo.org/events/pygotham-2017.html)
- [DjangoCon 2017 on YouTube](https://www.youtube.com/watch?v=ujGCN9MOrRk&list=PL2NFhrDSOxgXmA215-fo02djziShwLa6T)
- One I’ve watched so far: 
  - [DjangoCon US 2017 - Django vs Flask by David "DB" Baumgold](https://www.youtube.com/watch?v=UY2JMZjQspY&index=31&list=PL2NFhrDSOxgXmA215-fo02djziShwLa6T)
  - [slides](http://bit.ly/djangocon-flask)
  - Very good introduction to Flask while comparing some of the features of Django to Flask and what the current frequent practices are for doing things in Flask like:
    - Data modeling with SQLAlchemy, MongoEngine, or Peewee
    - User admin with Flask-Security, which wraps Flask-Login, Flask-Permissions, and other commonly used together packages.
    - Blueprints in Flask solve a similar problem as apps in Django.
    - Flask-Marshmallow for APIs

**Michael #2: [Python 3.6.3 released on Tue. All machines at FB are already running it](https://twitter.com/llanga/status/916460954128285696) (3 days)**

- Tweet: Did you hear that 3.6.3 was released on Tue? How about that all machines at FB are already running it? Over 36.3% of our Python apps are 3.6 via [@llanga](https://twitter.com/llanga/status/916460954128285696)
- See Jason Fried’s presentation on culture: [Rules for Radicals: Changing the Culture of Python at Facebook](https://www.youtube.com/watch?v=nRtp9NgtXiA)
- More Python 3 news
  - Ubuntu 17.10: *“Python 2 is no longer installed by default. Python 3 has been updated to 3.6.”*
  - PSA: Python 3.3 is end-of-life in 2 days. Are you prepared?

**Brian #3:** [**Your technical skills are obsolete: now what?**](https://codewithoutrules.com/2017/10/23/obsolete-skills/)

- by Itamar Turner-Trauring
- We’re big proponents of keeping your skills current, of learning new techniques and technologies. But how does that fit in with life and work.
- This article is an opinion of how to work on new skills while at work, do it quickly, and look good to your manager.
- It starts with a good discussion of real business reasons why some projects use older technology. Basically, cost vs benefit of change.
- Steps to be part of the solution:
	- Identify obsolete and problematic technologies.
	- Identify potential replacements.
	- Get management buy in to get resources (you) to do a pilot project exploring new technology.
- This process will help you be better at identifying problems, even if you don’t get approval to fix it.
- He ends with a comment that if you don’t get approval, all is not lost, you have skills to apply to a new job.
- I’d like to make sue you do a few more steps before giving up and looking for a new job. Before you consider a move to a new team or company, I think…
	- You should give your manager the benefit of the doubt and use this to start a conversation. Make sure you understand their reasons for saying no.
	- Make sure you are not proposing too much time taken away from your primary role in the company.
	- State that you want to improve your skills by providing value for the team and the company. 
	- Is the “no” due to just bad timing? Is there a higher priority problem to work on? 
	- You’ve just shown that you are someone interested in keeping your skills sharp and helping the company by expanding your role. If you’re still stuck at this point, then consider a move but also, …
- Read this:
  - [Team Geek: A Software Developer's Guide to Working Well with Others](http://amzn.to/2xjDBmI) - Brian Fitzpatrick
  - Especially:
			- pg 117 : “Offensive vs Defensive work”. 50-70% of your time at work needs to be focused on creating new value for your company or your customers. No more than 30-50% on repaying technical debt. (Okken: Limit your process improvement / new technology exploration to no more than 10-20%, but try to never drop it below 5% of your time)
			- pg 113 : “It’s easier to ask for forgiveness than permission.” This is a fine line between doing the right thing and doing something you can get reprimanded for. Use good judgement. 
			- Forgotten page number: A big part of your job is making your boss’s job easier and making your boss and your team look good.

**Michael #4:** [**Visualizing Garbage Collection Algorithms**](https://spin.atomicobject.com/2014/09/03/visualizing-garbage-collection-algorithms/)

- By Ken Fox
- Follow up from the excellent deep dive article in GC from Brian
- Most developers take automatic garbage collection for granted.
- It’s very difficult to see how GCs actually work.
- **GCs visualized** (click on each image):
	  - **Cleanup At The End: aka No GC** (e.g. Apache web server creates a small pool of memory per request and throws the entire pool away when the request completes)
	  - **Reference Counting Collector** (e.g. Python’s first pass GC, Microsoft COM, C++ Smart Pointers. Memory fragmentation is interesting)
		  - The red flashes indicate reference counting activity. A very useful property of reference counting is that garbage is detected as soon as possible — you can sometimes see a flash of red immediately followed by the area turning black.
	  - **Mark-Sweep Collector** (e.g. is this Python’s secondary collector? Probably is my guess)
		  - Mark-sweep eliminates some of the problems of reference count. It can easily handle cyclic structures and it has lower overhead since it doesn’t need to maintain counts.
	  - **Mark-Compact Collector** (Oracle’s Hotspot JVM’s tenured object space uses mark-compact)
		  - Mark-compact disposes of memory, not by just marking it free, but by moving objects down into the free space
		  - The crazy idea of moving objects means that new objects can always just be created at the end of used memory. This is called a “bump” allocator and is as cheap as stack allocation, but without the limitations of stack size.
	  - **Copying Collector, aka Generational GC**
		  - The foundation of most high-performance garbage collection systems

**Brian #5:** [**pathlib — Filesystem Paths as Objects**](https://pymotw.com/3/pathlib/)

- from Doug Hellman’s PyMOTW-3
- pathlib was introduced with Python 3.4
- If you need to work with the file system in Python, you should be using pathlib.
- Doug’s article is a really good overview.
- Features
	- Building paths with overloaded / operator
	- Parsing paths with `.parts`, `.parents`, `.suffix`, `.stem`
	- Concrete paths such as `Path.home()`, `Path.cwd()`
	- Getting directory contents with `.iterdir()`
	- Pattern matching with `.glob()` and `.rglob()`
	- Reading and writing files with path objects.
	- Working with directories and symbolic links
	- File properties, permissions
	- Deleting files and directories
- see also
	- [https://docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
	- The official docs are pretty good too

**Michael #6:** [**LUMINOTH: Open source Computer Vision toolkit**](https://luminoth.ai/)

- Deep Learning toolkit for Computer Vision
- Supports object detection and image classification, but are aiming for much more.
-  It is built in Python, using [TensorFlow](https://www.tensorflow.org/) and [Sonnet](https://github.com/deepmind/sonnet) (Google’s Deep Learning framework and DeepMind’s graph library)
- Easily train neural networks to detect and classify objects with custom data. 
- Use state of the art models such as Faster R-CNN (Region-based Convolutional Neural Networks)
- Comes with GPGPU support
- Simple training
	- Train your model by just typing lumi train. Do it locally or using Luminoth's built-in Google Cloud Platform support to train in the cloud.
	- Once training is done, you can use our Tensorboard integration to visualize progress and intermediate results. 
- Are also working on providing **pre-trained checkpoints** on popular datasets such as [Pascal VOC2012](http://host.robots.ox.ac.uk:8080/pascal/VOC/voc2012/index.html)

**Bonus article:**

[The Cleaning Hand of Pytest - My experiences with different approaches to testing](https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684)

  - by Wiktor Żurawik
  - Two case studies of having to use unittest after using pytest
  - Be sure to check out the “useful links” at the end of the article.

## Our news
- [PyTennessee 2018](https://www.pytennessee.org/)
- Movie: All work, all play (available on netflix, here’s the [trailer](https://www.youtube.com/watch?v=fjoCwM1xMuM))

