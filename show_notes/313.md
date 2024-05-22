# Python Bytes 313

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Special guest: [**Kelly Schuster-Paredes**](https://twitter.com/KellyPared)
- Special guest: [**Sean Tibor**](https://twitter.com/smtibor)

**Michael #1:** **How do you say that number?**

- Inflect: [**fosstodon.org/@linuxgal@techhub.social/109430499504962727**](https://fosstodon.org/@linuxgal@techhub.social/109430499504962727)
- Num2Words: [**pypi.org/project/num2words/**](https://pypi.org/project/num2words/)

```
# Inflect:
import inflect
inflector=inflect.engine()
print(inflector.number_to_words(8675309))
# eight million, six hundred and seventy-five thousand, three hundred and nine
    
# Num2Words
from num2words import num2words
print(num2words(8675309))
# eight million, six hundred and seventy-five thousand, three hundred and nine
```

- Num2Words also has a CLI:
- `pipx install num2words`
- `$ num2words 2948475`
- `two million, nine hundred and forty-eight thousand, four hundred and seventy-five`

**Brian #2:** [**The Origins of Python**](https://inference-review.com/article/the-origins-of-python)

- Lambert Meertens
- A wonderful tale starting with TELCOMP, traveling through ABC, and finally reaching Python. 
- This is a long article, but a wonderful story.
- It includes a nice emphasis at all times to keep a language simple enough for the absolute beginner but powerful enough to not be annoying for experienced developers.
- A few quotes from the article:
    - “Ease of learning and ease of use are both desirable attributes in any programming language. Nonetheless, I have often felt that this aspect of language design does not always receive the attention it deserves. And what may seem easy to a designer may not necessarily be easy for a language learner.”
    - Regarding ABC: “To serve our intended users, absolute beginners, we sought to hide low-level implementation details and instead to provide powerful high-level, task-oriented features.
    - Then Python: “The growth in popularity of Python, from its inception thirty years ago as a one-person effort flying under the radar, has been phenomenal, but not meteoric. Instead it has been a long, slow, and steady rise. Python’s ease of learning gave it a competitive advantage in a period when there was a perpetual need for more programmers. Its clean syntax and semantics make it easier to maintain a software base written in Python than other languages—an important consideration given that the cost of maintaining software dwarfs the cost of creating new software.”

**Kelly** **#3:** 

- [Ozobot Evo](https://shop.ozobot.com/cart) Introduces a Python Beta Version. ([**August 17, 2022**](https://ozobot.com/2022/08/17/))
- The original Ozobot model – the Ozobot Bit – is no longer available for purchase . The New Evo Ozobit- has three Kit options. The Entry Kit (single robot), the Ozobot Evo 12-Pack, and the Ozobot Evo 18-Pack. 
- https://beta.python.ozobot.com/doc-python-api/ozobot.html#module-0 
- Still has the updated OzoBlockly platform for Block Programming.
- This tiny bot comes with:
    - Line following
    - Color detection
    - Sound
    - proximity sensor
    - bluetooth
    - Crash detection
    - Students can even code functions
- Ozobot simulator(block) https://games.ozoblockly.com/shapetracer-freeform
- Web beta app: [beta.python.ozobot.com](https://beta.python.ozobot.com)



**Michael #4:** [**setproctitle**](https://pypi.org/project/setproctitle/)

- A Python module to customize the process title

- Awesome for servers and anytime “python” is not enough

- Easy to use directly:

- from setproctitle import setproctitle

- setproctitle("tp-search daemon")

- Used automatically by servers like uwsgi and gunicorn I believe.
  
```
    ###    
    # uWSGI server configuration
    ###
    [uwsgi]
    # uWSGI provides some functionality which can help identify the workers
    procname-prefix = training-
    auto-procname = true
```

- Some nice results, example from Talk Python Training
![](https://python-bytes-static.nyc3.digitaloceanspaces.com/server-with-names.png)


**Brian #5:** **Looking forward to Python 3.12**

- [New features in 3.12a2](https://www.python.org/downloads/release/python-3120a2/)
    - Improved Error Messages
    - lots of other goodies, like `pathlib.walk()`.
- [Release scheduled for Oct 2023](https://peps.python.org/pep-0693/)
- But why wait? Start testing your projects with it now: [Te](http://localhost:1313/testing-with-python-3.12)[sting with Python 3.12](https://pythontest.com/testing-with-python-3-12)
- Note that “During the alpha phase, features may be added up until the start of the beta phase (2023-05-08) and, if necessary, may be modified or deleted up until the release candidate phase (2023-07-31). Please keep in mind that this is a preview release and its use is not recommended for production environments.”
- Actually, with that note, you might want to wait. I don’t. I’ll deal with it when/if I get a failure. 

**Sean** **#6:** [**Re:Invent 2022 EF Education Breakout**](https://www.youtube.com/watch?v=rRBLl7MsZVU&list=PL2yQDdvlhXf9F-GUSSZ2jBtelyiWRFHNV&index=13)

- Presentation at AWS Re:Invent 2022
- Complete redesign of online learning platform by one of the largest education companies in the world
- We’ve all seen Zoom classrooms with rows on rows of students
- A more immersive experience for learning with green screens, digital sets, and props
- Massive amount of analytics around student engagement and learning, including full transcription of every student, engagement tracking, and computer vision
- 
![](https://paper-attachments.dropboxusercontent.com/s_8972A8B4AFB195FA45E7A043E2BDE6670DA22712B4D99F7D7829C7C10300934F_1670335403294_image.png)


**Extras** 


Michael:

- You can support the PSF if you’re selling things on EBay. Check “Donate a portion to charity” and choose “Python Software Foundation” via Joe Riedley
- [Textinator for Windows](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor) (the Windows version of [TextSniper](https://www.textsniper.app))
- [Paperlike](https://paperlike.com) for iPad

Kelly: A new Special Interest Group for the PSF launched 6 days ago.  “Edu-sig, through its [mailing list](http://www.python.org/mailman/listinfo/edu-sig), provides an informal venue for comparing notes and discussing future possibilities for Python in education.” Led by Timothy Wilson.

Sean:

- [Dr. Werner Vogel’s keynote](https://www.youtube.com/watch?v=RfvL_423a-I) - everything is coming up async
- [EventBridge Pipes](https://aws.amazon.com/eventbridge/pipes/)

**Jokes:** 

[fosstodon.org/@kimvanwyk/109389398652030679](https://fosstodon.org/@kimvanwyk/109389398652030679)


And a new mastodon user:

[fosstodon.org/@vruz@mastodon.social/109394538570819699](https://fosstodon.org/@vruz@mastodon.social/109394538570819699)

![Feature Comparison](https://imgs.xkcd.com/comics/feature_comparison.png)

