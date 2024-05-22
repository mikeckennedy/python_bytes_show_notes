# Python Bytes 23
**Sponsored by ADVANCE DIGITAL. Find your Python web job at [http://python.advance.net/](http://python.advance.net/)**

**Brian #1:** [**Grok the GIL** - **How to write fast and thread-safe Python**](https://opensource.com/article/17/4/grok-gil) 

- A. Jesse Jiryu Davis teaches us about the GIL, and how to use that knowledge to decide between threads and processes for parallelism.
- From the article:
  - The GIL's effect on the threads in your program is simple enough that you can write the principle on the back of your hand: "One thread runs Python, while N others sleep or await I/O."
- Discusses and Cooperative multitasking and Preemptive multitasking
- When can a Python process be interrupted? (between bytecodes)
- When do you need to use thread protection? (less than you think)
- *A. Jesse Jiryu Davis will be speaking at* [*PyCon 2017*](https://us.pycon.org/2017/)*, which will be held May 17-25 in Portland, Oregon. Catch his talk,* [*Grok the GIL: Write Fast and Thread-Safe Python*](https://us.pycon.org/2017/schedule/presentation/320/)*, on Friday, May 19.*


**Michael #2:** [**The New NBA by Mark Cuban**](https://twitter.com/mcuban/status/846781342083923969)

- Introduction to machine learning in Python & Jupyter notebooks
- Mark Cuban using Python and ML to play with his NBA team
- “We have a team at the Mavs but I need to know it to help define strategy and make decisions”

**Brian #3:** [**Ian Cordasco gets a Community Service Award from PSF**](http://pyfound.blogspot.com/2017/04/the-ego-less-developer-community.html)

- Ian was on [Test & Code, episode 13](http://testandcode.com/13), talking about Betamax
- From the announcement:
  - Ian Cordasco has been the PSF’s Election Administrator since 2015, volunteering his efforts for this important role. 
  - Cordasco frequently mentors newer coders and supports their Python endeavors. 
  - The Python Software Foundation award the 2017 Q1 Community Service Award to Ian Cordasco for his contributions to PSF elections and active mentoring of women in Python community.
  - Cordasco has a history of going out of his way to support and encourage female developers. When [Carol Willing](https://twitter.com/WillingCarol), a developer for the Jupyter project, wanted to work on the Requests library, she got in touch with Cordasco. “We worked together on the project and my first commit to the Requests library got accepted!” Cordasco later wrote a fantastic post about it on his [blog](http://www.coglib.com/~icordasc/blog/2014/11/sending-json-in-requests.html).

**Sponsored by ADVANCE DIGITAL**

- They have a small team of developers who work in an agile/devops environment– you will make an impact with your work quickly
- They are mostly a python shop, but there is an opportunity to introduce and run other technologies at scale
- They fund employee development and conference attendance
- They are located in beautiful Jersey City, one stop from Manhattan on the PATH
- They are one of the 10 largest news sites by traffic in the US
- Apply at **[http://python.advance.net/](http://python.advance.net/)**

**Michael #4:** [**Release of IPython 6.0**](https://blog.jupyter.org/2017/04/19/release-of-ipython-6-0/)

- by Matthias Bussonnier
- IPython goes Python 3 only
- Our personal experience writing Python3-only source code.
  - The size of the IPython codebase has decreased by about 1500 lines of Python code relative to the last release. Of course, that’s not solely due to the removal of Python 2 support, but a non-negligible amount is.
  - even more remarkable in light of completely new features that required adding hundreds of lines of code
  - This change eases the burden on contributors to IPython. Contributors can can spend less time thinking “what about Python 2”, or rewriting a pull request because the Python 2 test suite fails. 
  - At the same time, our tests now complete more quickly on continuous integration services because they need to run on fewer versions of Python.
  - From a developer point of view we are extremely pleased with having the possibility to write Python3-only code, and are looking forward to even more improvements like [pathlib](https://docs.python.org/3/library/pathlib.html).
  - We hope you will enjoy this release. It will be the base for some awesome features, like async/await REPL.

**Brian #5:** [**Testing & Packaging**](https://hynek.me/articles/testing-packaging/)

- Hynek Schlawack describes why he was convinced to use a src directory in package distributions he works on.
- Just use a src dir (of course it doesn’t have to be exactly “src” but that’s the convention and it should be different than your package name), it will make your life easier.
- Without it, it is easy to think you are testing an installed package, but you’re really testing the modules before install. These can be different. Better to test as close to how your users will see the package as possible, and using a src dir helps that.


**Michael #6:** [**AWS Lambda adds Python 3.6 support**](https://aws.amazon.com/releasenotes/5198208415517126)

- AWS Lambda is a compute service that lets you run code without provisioning or managing servers. 
- AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. 
- You pay only for the compute time you consume - there is no charge when your code is not running.
- You can also build [serverless](https://aws.amazon.com/serverless) applications composed of functions that are triggered by events and automatically deploy them using AWS CodePipeline and AWS CodeBuild. 
- Already good things cometh: [Zappa has Python 3 support](https://github.com/Miserlou/Zappa/issues/793).

