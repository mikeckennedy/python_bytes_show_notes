# Python Bytes 274

Sponsored by [**Microsoft for Startups Founders Hub**](https://pythonbytes.fm/foundershub).

Special guest: Anne Barela

**Brian #1:** [**The Adam Test : 12 Questions for New Dependencies**](https://adamj.eu/tech/2021/11/04/the-well-maintained-testhttps://adamj.eu/tech/2021/11/04/the-well-maintained-test)

- Found through a discussion with Ryan Cheley, who will be on an upcoming episode of Test & Code, talking about Managing Software Teams.
- [The Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) dates back to 2000, and some of it is a bit dated. I should probably do a [Test & Code](https://testandcode.com/) episode or [pythontest](https://pythontest.com/) article on my opinions of this at some point. 
    - Nice shameless plugs, don’t you think?
    - The Joel Test is 12 questions and is a “highly irresponsible, sloppy test to rate the quality of a software team.”
- “The Adam Test” is 12 questions “to decide whether a new package we’re considering depending on is well-maintained.” 
    - He’s calling it “The Well-Maintained Test”, but I like “The Adam Test”
- Here’s the test:
    - Is it described as “production ready”?
    - Is there sufficient documentation?
    - Is there a changelog?
    - Is someone responding to bug reports?
    - Are there sufficient tests?
    - Are the tests running with the latest <Language> version? 
        - like Python 3.10, of course
    - Are the tests running with the latest <Integration> version? 
        - Examples include Django, PostgreSQL, etc.
    - Is there a Continuous Integration (CI) configuration?
    - Is the CI passing?
    - Does it seem relatively well used?
    - Has there been a commit in the last year?
    - Has there been a release in the last year?
- Article has a short discussion of each.
- What score is good? That’s up to you to decide.
- But these questions are good to think about for your dependencies.
- I also think I’ll use these questions for my own projects.
    - I’ve got a README.md, but do I need more examples in it? Should I have RTD docs for it?
    - Have I updated the test matrix to include the newest versions of Python, etc?
    - Have I hooked up CI? 

**Michael #2:** [**Validate emails with email-validator**](https://stackabuse.com/validate-email-addresses-in-python-with-email-validator/)

- When you think about validating emails, you probably think regex (or just nothing) 
- Regex is fine but so is this email: **jane_doe@domain_that_doesnt_exist.com**
- Problem is (at the time of the recording), domain_that_doesnt_exist.com is not a website.
- What about unicode variations that are technically the same but visually different?
- If the passed email address is valid, the `validate_email()` method will return an object containing a **normalized form of the passed email address**.

**Anne #3:** [**The Python on Microcontrollers Newsletter**](https://www.adafruitdaily.com/category/circuitpython/)

One of my main focuses at Adafruit since the pandemic started is as editor of the Python on Microcontrollers Newsletter. 

- With a weekly distribution of almost 9,400 subscribers, it’s the largest newsletter of it’s kind. 
- It mainly focuses on CircuitPython and MicroPython and also discusses Python on single board computers (SBC) like Raspberry Pi.
- News about Python with a small computer emphasis
- Folks may subscribe by going to https://www.adafruitdaily.com/ which is separate from adafruit.com. The information is not sold or used for marketing and it’s easy to unsubscribe (no “do you really want to do this, please reconsider…)
- The challenge, like for Python Bytes and other publications, is to find content. I scour the internet, with a bit of a focus on Twitter as [I have an active account there](https://twitter.com/anne_engineer). We encourage others to put in issues and Pull Requests on the newsletter GitHub https://github.com/adafruit/circuitpython-weekly-newsletter/, email information to cpnews@adafruit.com and using hashtag CircuitPython or MicroPython on Twitter.



**Brian #4:** [**Git Organized: A Better Git Flow**](https://render.com/blog/git-organized-a-better-git-flow)

- Annie Sexton
- Found through [Changelog episode 480: Get your reset on](https://changelog.com/podcast/480)
- A possible and common git workflow
    - Branch off of a main branch to a personal dev branch
    - Commit and Push during development to save your work 
    - When ready to merge, make a PR
- Problems
    - Commits are hard to follow and messy, not ever really intended to separate parts of the workflow or anything.
    - Commits are therefore useless in helping someone code review large changes.
- Annie’s workflow
    - Branch off of a main branch to a personal dev branch
    - Commit and Push during development to save your work. But don’t worry to much about commit messages, “WIP” is sufficient. Or a note to yourself.
    - When ready to merge
        - `git reset origin/main`
        - Re-commit all changes in a logical order that makes more sense than the way the work actually happened.
        - These will be several commits, with descriptive messages.
        - Even partial commits, if there are unrelated changes in a file, work with this process
        - Push all the new commits. (Is `--force` going to be necessary?)
        - Create a PR.
    - Now there are a set of commits that are actually helpful to break up large PRs into small chunks that tell a story.
- I’m looking to try this soon to see how it goes

**Michael #5:** [**CPython**](http://) [**issues moving to GitHub soon**](https://discuss.python.org/t/github-issues-migration-is-coming-soon/13791)

- Update by The Python Developer in Residence, Łukasz Langa
- The Steering Council is working on migrating the data that is currently residing in Roundup at [https://bugs.python.org/](https://bugs.python.org/) (BPO) into the GitHub issues of the CPython repository hosted there.
- Laid out in [**PEP 581 -- Using GitHub Issues for CPython**](https://www.python.org/dev/peps/pep-0581/)
- The ultimate goal is to move user- and core developer-provided issue-reporting entirely to Github.
- Each issue that currently exists on BPO will include metadata indicating where it was moved on Github. 
- New issues will only exist on Github.
- Feedback, please: At the current stage, we’re asking you to take a look at the links and important dates below, and share any feedback you might have.
- Timeline:
    - Friday, March 11th 2022: Github starts transfer of the issues in the temporary repository to [github.com/python/cpython/](https://github.com/python/cpython/) .
    - The migration is estimated to take anywhere from 3 to 7 days, depending on the load on [Github.com](http://github.com/).

**Anne #6: MicroPython, CircuitPython and GitHub**

- What are Microcontrollers and Single Board Computers (SBCs)?
- Why not use CPython on Microcontrollers?
- [MicroPython](https://micropython.org/) was originally created by the Australian programmer and theoretical physicist Damien George, after a successful Kickstarter backed campaign in 2013. Originally it only ran on a number of boards and was based on Python 3.4.
- [CircuitPython](https://circuitpython.org/) was forked from MicroPython in 2017 by Adafruit Industries.
- Both MicroPython and CircuitPython are Open Source under MIT Licenses so adoption and modification by anyone is easy.
- Why fork CircuitPython? 1) Make a requirement that CircuitPython boards can enumerate to computers as a USB thumb drive to add or change code files with any text editor. 2) Aim to make CircuitPython use CPython library syntax whenever possible. 3) Make it easy to use and understand for beginners yet powerful for more advanced users.
- All [CircuitPython code is on GitHub](https://github.com/adafruit/circuitpython). GitHub Actions is used on repos like the Adafruit Learning System code to automate CI with Pylint, Black, and ensuring code has proper [SPDX](https://spdx.dev/) author and license tags, which is a new addition this year.
- Currently there are 283 microcontroller boards compatible with CircuitPython and 87 single board computers can use CircuitPython libraries in CPython via the [Adafruit Blinka abstraction layer](https://circuitpython.org/blinka). Code portability between boards requires little if any changes.
- There are 346 CircuitPython libraries (all on PyPI / pip as well as GitHub) covering a wide range of hardware and real world needs. From blinking LEDs to using [ulab](https://github.com/v923z/micropython-ulab) (microlab), a subset of numpy, for data crunching.
- I just counted and there are exactly 1,000 [Adafruit Learning System guides](https://learn.adafruit.com/) referencing CircuitPython, all free and open source/MIT licensed. https://learn.adafruit.com/


Extras 

Brian: 

- Quick read: [The Thirty Minute Rule](https://daniel.feldroy.com/posts/thirty-minute-rule), by Daniel Roy Greenfield
    - summary: Stuck on a software problem for 30 min? Ask for help.

Michael:

- [**The CircuitPython Show**](https://www.circuitpythonshow.com) by Paul Cutler
- Follow up from my Python 3 == Active Python 3? James wrote:
- *In episode #273, you guys were discussing supporting "Python 3" to mean any currently supported version of Python rather than "Python 3.7+" or similar. That's a really bad idea. There are still tons of people using unsupported versions of Python, and they're not all invalid use cases. For example, I am one of the upstream maintainers for cloud-init, and I was only recently able to remove Python 3.5 in order to make 3.6 our minimum supported version (which will continue for the next year). The reason is that our main consumers are downstream distro packagers (ubuntu, red hat, fedora, etc), and it's not uncommon for software released into long-term supported OS releases to be supported for 5-10 years or more. If I fire up an Ubuntu Trusty container, which still receives extended support until 2024, I get Python 3.4. So even though 3.4 is unsupported by Python upstream, it is still absolutely in use and supported by OS manufacturers.*

Joke: [**A case of the Mondays**](https://twitter.com/PR0GRAMMERHUM0R/status/1498614050208555010)

