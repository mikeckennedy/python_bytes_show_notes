# Python Bytes 172
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Michael #1:** [**Python in Production Hynek**](https://hynek.me/articles/python-in-production/)

- Missing a key part from the public Python discourse and I would like to help to change that.
-  Hynek was listening to [a podcast](https://runninginproduction.com/podcast/10-scholarpack-runs-10-percent-of-the-uks-primary-schools-and-gets-huge-traffic) about running Python services in production. 
- Disagreed with some of the choices they made, it acutely reminded me about what I’ve been missing in the past years from the public Python discourse.
- And **yet** despite the fact that the *details* aren’t relevant to me, the *mindsets*, *thought processes*, and *stories* around it captivated me and I happily listened to it on my vacation.
- Python conferences were a lot more like this. I remember startups and established companies alike to talk about running Python in production, lessons learned, and so on. (Instagram and to a certain degree Spotify being notable exceptions)
- An Offer: So in a completely egoistical move, I would like to encourage people who do interesting stuff with Python to run websites or some kind of web and network services to tell us about it at PyCons, meetups, and in blogs.
- Dan Bader and I covered this back on [**Talk Python, episode 215**](https://talkpython.fm/episodes/show/215/the-software-powering-talk-python-courses-and-podcast).

[**Brian #2:**](https://simonwillison.net/2020/Feb/11/cheating-at-unit-tests-pytest-black/) (https://simonwillison.net/2020/Feb/11/cheating-at-unit-tests-pytest-black/)[**How to cheat at unit tests with pytest and Black**](https://simonwillison.net/2020/Feb/11/cheating-at-unit-tests-pytest-black/)

- Simon Willison
- Premise: “In pure test-driven development you write the tests first, and don’t start on the implementation until you’ve watched them fail.”
- too slow, so …, “cheat”
	- write a pytest test that calls the function you are working on and compares the return value to something obviously wrong.
	- when it fails, copy the actual output and paste it into your test
	- now it should pass
	- run black to reformat the huge return value to something manageable
- Brian’s comments:
	- That’s turning exploratory and manual testing into automated regression tests, not cheating.
	- There is no “pure test-driven development”, we still can’t agree on what a unit is or if mocks are good or evil.

**Michael #3:** [**Goodbye Microservices: From 100s of problem children to 1 superstar**](https://segment.com/blog/goodbye-microservices/)

- Retrospective by Alexandra Noonan
- Javascript but the lessons are cross language
-  Microservices is the architecture du jour
- Segment [adopted this as a best practice](https://segment.com/blog/why-microservices/) early-on, which served us well in some cases, and, as you’ll soon learn, not so well in others.
- Microservices is a service-oriented software architecture in which server-side applications are constructed by combining many single-purpose, low-footprint network services.
- Touted benefits are improved modularity, reduced testing burden, better functional composition, environmental isolation, and development team autonomy.
- Instead of enabling us to move faster, the small team found themselves mired in exploding complexity. Essential benefits of this architecture became burdens. As our velocity plummeted, our defect rate exploded.
- Her post is the story of how we took a step back and embraced an approach that aligned well with our product requirements and needs of the team.

**Brian #4:** [**Helium**](https://github.com/mherrmann/helium)

**Michael #5:** [**uncertainties package**](https://pythonhosted.org/uncertainties/)

- From Tim Head on upcoming Talk Python Binder episode.
- Do you know how uncertainty flows through calculations?
- Example:

```
    Jane needs to calculate the volume of her pool, so that she knows how much water she'll need to fill it. She measures the length, width, and height:
               length  L  =  5.56    +/-  0.14 meters
                          =  5.56 m  +/-  2.5%
    
               width   W  =  3.12    +/-  0.08 meters
                          =  3.12 m  +/-  2.6%
    
               depth   D  =  2.94    +/-  0.11 meters
                          =  2.94 m  +/-  3.7%
```

One can find the percentage uncertainty in the result by adding together the percentage uncertainties in each individual measurement:

```
        percentage uncertainty in volume =   (percentage uncertainty in L) +
                                             (percentage uncertainty in W) +
                                             (percentage uncertainty in D) 
    
                                         =  2.5% + 2.6% + 3.7% 
                                         =  8.8%
```

- We don’t want to deal with these manually! So we use the uncertainties package.
- Example of using the library:

```
    >>> from uncertainties import ufloat
    >>> from uncertainties.umath import *  # sin(), etc.
    >>> x = ufloat(1, 0.1)  # x = 1+/-0.1
    >>> print 2*x
    2.00+/-0.20
    >>> sin(2*x)  # In a Python shell, "print" is optional
    0.9092974268256817+/-0.08322936730942848
```

Brian #6: [**Personalize your python prompt**](https://arpitbhayani.me/blogs/python-prompts)

- Arpit Bhayani
- Those three `>>>` in the interactive Python prompt. you can muck with those by changing `sys.ps1`
- Fun.
- But you can also implement dynamic behavior by creating class and putting code in the `__str__` method. Very clever.
- note to self: task for the day: reproduce the windows command prompt with directory listing and slashes in the other direction.

Extras:

Michael:

- Now that Python for Absolute Beginners is out, starting on a new course: Hybrid Data-Driven + CMS web apps.

**Joke: A Python Editor Limerick** 

- via Alexander A.

CODING ENVIRONMENT, IN THREE PARTS:

*To this day, some prefer BBEdit.*
*VSCode is now getting some credit.*
*Vim and Emacs are fine;*
*so are Atom and Sublime.*
*Doesn't matter much, if you don't let it.*

*But wait! Let's not forget IDEs!*
*Using PyCharm sure is a breeze!*
*Komodo, Eclipse, and IDEA;*
*CLion is my panacea,*
*and XCode leaves me at ease.*

*But Jupyter Notebook is also legit!*
*Data scientists must prefer it.*
*In the browser, you code;*
*results are then showed.*
*But good luck when you try to use git.*




