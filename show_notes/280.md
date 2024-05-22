# Python Bytes 280


**Sponsored by** [**Mergify**](https://pythonbytes.fm/mergify)! 

Special guest: Pat Decker

**Michael #0**: New live stream / recording time: 12pm US PT on **Tuesdays**. Please [**subscribe to our YouTube channel**](https://www.youtube.com/c/PythonBytesPodcast) to get notified and be part of the episodes.

**Brian #1:** **BTW, don’t make a public repo private**

- [How we lost 54k GitHub stars](https://httpie.io/blog/stardust)
    - Jakub Roztočil
    - HTTPie kinda sorta accidentally flipped their main repo to private for a sec.
    - And dropped the star count from 54k to 0
    - oops
    - They’re back up to 16k, as of today. But ouch.
- “HTTPie is a command-line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible. HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers. The http & https commands allow for creating and sending arbitrary HTTP requests. They use simple and natural syntax and provide formatted and colorized output.”
- Actually, pretty cool tool to use for developing and testing APIs.


**Michael #2:** [**The counter-intuitive rise of Python in scientific computing**](https://cerfacs.fr/coop/fortran-vs-python)

- via Galen Swint
- In our laboratory, a polarizing debate rages since around 2010, summarized by this question: **Why are more and more time-critical scientific computations formerly performed in Fortran now written in Python, a slower language?**
- Python has the reputation of being slow, *i.e.* significantly slower than compiled languages such as Fortran, C or Rust.
- **So yes, plain Python is much slower than Fortran.**
- However, this comparison makes little sense, as scientific uses of Python do not rely on plain Python.
- **Used the right way, Python is slightly slower than compiled code.**

**Pat #3:** 

- Meta donates $300,000 to PSF to add a second year for the Developer in Residence
-     https://www.realmicentral.com/2022/03/25/meta-donates-300000-to-the-python-software-foundation/

**Brian #4:** **Dashboards in Python**

- Two suggestions from Marc Skov Madsen
- [**The Easiest Way to Create an Interactive Dashboard in Python**](https://towardsdatascience.com/the-easiest-way-to-create-an-interactive-dashboard-in-python-77440f2511d1)
    - Sophia Yang & Mark Skov Madsen
    - Includes 
        - animated gif showing the dashboard
        - video of Sophia walking through the article in under 6 minutes
    - “Turn Pandas pipelines into a dashboard using hvPlot .interactive"
    - hvPlot is part of HoloViz and this example is pretty short and amazing to get a great dashboard with controls up very quickly.
- [**Python Dashboarding Shootout and Showdown | PyData Global 2021**](https://www.youtube.com/watch?v=4a-Db1zhTEw)
    - 5 speakers, 4 dashboard libraries, nice for comparison. 
    - Nice clickable index posted by Duy Nguyen
        - [00:00](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=0s) - Begin and Welcome
        - [03:15](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=195s) - Intro to the 4 Dashboarding libraries
        - [07:04](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=424s) - Plotly - Nicolas Kruchten
        - [22:01](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=1321s) - Panel - Marc Skov Madsen
        - [37:38](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=2258s) - voila - Sylvain Corlay
        - [51:36](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=3096s) - Streamlit - Adrien Treuille
        - [01:10:52](https://www.youtube.com/watch?v=4a-Db1zhTEw&t=4252s) - Discussion Topics

**Michael #5:** [**sourcepy**](https://github.com/dchevell/sourcepy)

- by Dave Chevell
- Sourcepy lets you source python scripts natively inside your shell
- Imagine a Python script with functions in it. This converts those to CLI commands (kind of like entrypoints, but simpler)
- Type hints can be used to coerce input values into their corresponding types.
-  standard `IO` type hints can be used to target stdin at different arguments and to receive the `sys.stdin`
- Sourcepy has full support for asyncio syntax

**Pat #6:** [**Xonsh**](https://itsfoss.com/xonsh-shell/)

- Xonsh Shell Combines the Best of Bash Shell and Python in Linux Terminal
- Awesome demo video (50 min) https://youtu.be/x85LSyCxiw8

**Extras** 


Pat: 
- Donate to the PSF by using https://rewards.microsoft.com

**Joke:** [**Can you really quit vim**](https://twitter.com/PR0GRAMMERHUM0R/status/1507583148921659395)?

**Joke**: [**Forgetting how to count**](https://twitter.com/mediocreheroes/status/1498738648459657222?s=20&t=HE_YXD6EefxEURDpy3szWw)

