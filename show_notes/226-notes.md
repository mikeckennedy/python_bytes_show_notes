# Python Bytes 226


Special guests: 

- [**Kelly Schuster-Pared**](https://twitter.com/kellypared)[**es**](https://twitter.com/kellypared)
- [**Sean Tibor**](https://twitter.com/smtibor)


**Brian #1:** [**DataClass vs NamedTuple vs Object: A Battle of Performance in Python**](https://medium.com/@jacktator/dataclass-vs-namedtuple-vs-object-for-performance-optimization-in-python-691e234253b9)

- Jack Song
- I’ve been using dataclass for a while now and love it. For some reason, I thought I heard there was some performance hit from them, so I was a bit worried before reading this.
- Jack came up with “a performance tests to compare the different *size* and *speed* when creating, reading and executing functions for `Object`, `NamedTuple` and the new `DataClass` introduced in Python 3.7”

|                  | **Object**   | **NamedTuple** | **DataClass** |
| ---------------- | ------------ | -------------- | ------------- |
| create           | 2.94 µs      | **2.01 µs**    | 2.34 µs       |
| read property    | **24.7 ns**  | 26.9 ns        | **24.7 ns**   |
| nested property  | **48.1 ns**  | 75.8 ns        | 52.1 ns       |
| execute function | 829 ns       | 946 ns         | **821 ns**    |
| size             | **56 bytes** | 80 bytes       | **56 bytes**  |

- Marvelous. Dataclass is still awesome. At the very least, it’s on the same order of size and speed as other structures.
- Further questions:
	- This was a limited bit of code, and performance metrics always depend on what kind of example code was used. If anyone has info about different performance examples that give wildly different results or even similar results, regarding DataClass, I’d love to hear about it. 

**Michael #2:** [**Can My Water Cooled Raspberry Pi Cluster Beat My MacBook?**](https://www.the-diy-life.com/can-my-water-cooled-raspberry-pi-cluster-beat-my-macbook/)

- Did you know there were Raspberry Pi clusters? Amazing.
- Two primary things of interest
	- Pi clusters exist!
	- All the tools and setup to make the pi cluster nodes run in a grid computing scenario
- Compared against a mediocre HP laptop:
	- 10,000 → 1.69 sec
	- 100,000 → 74 sec
	- 200,000 → 268 sec
- Compared against an Intel MB Air:
	- 10,000 → .88 sec
	- 100,000 → 83 sec
	- 200,000 → 355 sec
- **Pi cluster, one node**:
	- 10,000 → 1.57 sec
	- 100,000 → 148 sec
	- 200,000 → 646 sec
- **Pi cluster, grid computed**:
	- 10,000 → .65 sec
	- 100,000 → 22 sec
	- 200,000 → 85 sec
- Ran the [**same script**](https://www.the-diy-life.com/can-my-water-cooled-raspberry-pi-cluster-beat-my-macbook/#test_script) on my **Mac Mini M1** (on Python 3.9.2 Rosetta, **single threaded**)
	- 10,000 → .33 sec
	- 100,000 → 24 sec
	- 200,000 → 91 sec
- Ran the [**my parallel script**](https://gist.github.com/mikeckennedy/ffe8a65473e974d0582da0c74a8f1c67) on my **Mac Mini M1** (on Python 3.9.2 Rosetta, **multi-threaded**)
	- 10,000 → .28 sec
	- 100,000 → 7 sec
	- 200,000 → 26 sec
	- 500,000 → 2m (vs. 9m on the cluster)
![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/6052ec2a4b948a1595ea0114/f279fa64f7d2ebf93201318397726e26/Screen_Shot_2021-03-21_at_12.31.33_PM.png)

- Ran the [**my parallel script**](https://gist.github.com/mikeckennedy/ffe8a65473e974d0582da0c74a8f1c67) on my **Alienware sim racing machine** (**16 core, multi-threaded**)
	- 10,000 → .27 sec
	- 100,000 → 2.7 sec
	- 200,000 → 10 sec
	- 500,000 → 1m
	- **[Video of the Alienware sound](https://www.youtube.com/watch?v=rkRcvehsP6g)**


**Kelly #3:** [**There is an app for that!**](https://www.programiz.com/learn-python)
I am always trying to find time to practice Python and learn more ways to teach Python Basics. I am always on the go, so having Python Practice online and an online editor is always a plus.

- Programiz a company out of Nepal, has an IOS and Android app for beginner pythonistas
	- From “Hello World” to Generators and Decorators
	- Original Owners of Programiz: Ranjit Bhatta, Aswin Shrestha and Punit Jajodia
	- Swipe, Learn, and Repeat
    - Has an editor built in
    - Leaderboards
    - Quizzes and “Interview Challenges”  (paid)
        - Newest update with 200+ programs
    - Interactive IDE
    - FREE, with minimal app advertising
    - Paid version as well
	- Learn anywhere availability, helps to reduce the Digital Divide
    - 826 million learners online due to Covid19
    - 50% of those learners do not have a household computer
    - 706 million have no at home internet
	- The engineering behind the app and its editor function: [https://www.programiz.com/blog/online-python-compiler-engineering/](https://www.programiz.com/blog/online-python-compiler-engineering/)

**Brian #4:** [**New packaging security funding & NYU**](https://discuss.python.org/t/new-packaging-security-funding-nyu/7792)

- Sumana Harihareswara
- “New York University – specifically Professor Justin Cappos – and I (Sumana) have successfully asked the US National Science Foundation for a grant to improve Python packaging security. The NSF is awarding NYU $800,000 over two years – from mid-2021 to mid-2023 – to further improve the pip dependency resolver and to integrate The Update Framework further into the packaging toolchain.”
- “NYU researchers and developers will
	- Further assess and improve pip’s dependency resolver, following up on the work done in 2020 and making [ResolveLib](https://github.com/sarugaku/resolvelib/) more reusable by other tools in the packaging ecology
	- Secure the PyPI-to-user pipeline by integrating TUF support for signed packages throughout PyPI’s clients (we’re targeting conda, pip, and bandersnatch initially)”
- TUF is [The Update Framework (TUF) specification,](https://www.theupdateframework.com/) 
	- From [theupdateframework.io](https://theupdateframework.io/):
		- “The Update Framework (**TUF**) helps developers maintain the security of software update systems, providing protection even against attackers that compromise the repository or signing keys. TUF provides a flexible framework and specification that developers can adopt into any software update system.
- [ResolveLib](https://github.com/sarugaku/resolvelib/)  “provides a `Resolver` class that includes dependency resolution logic.”. It’s an independent project, but vendored by pip
- [bandersnatch](https://pypi.org/project/bandersnatch/) “is a PyPI mirror client”

**Michael #5: Extra x8, hear all about it**

1. We on [**amazon**](https://music.amazon.com/podcasts/7dc269ab-93df-4a32-b382-9e3e8c41d016/Python-Bytes) and [**audible**](https://www.audible.com/pd/Python-Bytes-Podcast/B08JJRD7D9?qid=1616362521&sr=1-3&ref=a_search_c3_lProduct_1_3&pf_rd_p=83218cca-c308-412f-bfcf-90198b687a2f&pf_rd_r=HCG8XTQVENWMJWPNVSH2) **(so is** [**Teaching Python**](https://music.amazon.com/podcasts/search/python)**)**
2. Sourcery added [**skip refactorings**](https://github.com/sourcery-ai/sourcery/wiki/Skipping-refactorings). I did major refactoring since, favorite:
	1. `url = request.url if request.url else ''` to
	2. `url = request.url or '``'`
3. Via [**Matthew Feickert**](https://twitter.com/HEPfeickert/status/1372425321203568642), it’s easy to become a PSF member and support the PSF
4. [**Beanie adds indexes**](https://roman-right.github.io/beanie/#indexes)!
5. Pycharm (and other JetBrains IDEs) in the browser via Dave Kirby
	1. [**lp.jetbrains.com/projector**](https://lp.jetbrains.com/projector/)
	2. [**github.com/JetBrains/projector-installer**](https://github.com/JetBrains/projector-installer)
6. [**SQLite as a file format comes to Audacity**](https://www.theregister.com/2021/03/19/audacity_3/) (via Jon Bultmeyer)
7. **Prayson Daniel** shared [**his Neo4J examples**](https://github.com/Proteusiq/graphs) using Neomodel.
8. [**Call for proposals for PyCon Latam just went live**](https://twitter.com/ChekosWH/status/1371992445093744641)

**Sean #6:** [**Using Development Containers with VS Code for Students**](https://code.visualstudio.com/blogs/2020/07/27/containers-edu)
* One of the big chores at the start of a course is getting everyone set up in the same development environment. Usually takes at least a few classes and nearly impossible to get everyone with the same environment at the end.
* **Solution -** use Docker images and the Remote-Containers extension to allow students to run a pre-configured container right in VS Code.
* Needs VS Code & Docker Desktop (maybe a remote Docker host could make it even easier?)
* Can deploy directly from a Github repo with persistent storage volumes, default VS Code settings, and even pre-installed packages and environment variables.
* Seems well suited for universities, experienced learners, etc. Also makes it easy to create different environments by assignment or course unit. What if every Talk Python training course had a GitHub container repo with the same starting environment?

Extras:

**Kelly**:
- [https://us.pycon.org/2021/summits/education-training/](https://us.pycon.org/2021/summits/education-training/) 

**Sean:**

- [Repl.it adds Python package caching](https://blog.replit.com/python-package-cache) (and gets a 40% speed boost)
- [Home Assistant (actually Nabu Casa) buys ESPHome](https://www.home-assistant.io/blog/2021/03/18/nabu-casa-has-acquired-esphome/) (makes DIY IoT devices cheap & easy to integrate)
- [It’s good to know a Python programmer if you need a vaccine appointment](https://www.nbcnews.com/tech/security/want-vaccination-appointment-helps-know-python-programmer-rcna457) 

Joke (in honor of our teachers today):

![](https://trello-attachments.s3.amazonaws.com/6041d3db4ddead109a997194/912x670/888520d608537dd14fdd724eb01fe754/Screen_Shot_2021-03-04_at_10.34.37_PM.png)
