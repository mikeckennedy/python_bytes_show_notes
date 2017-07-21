# Python Bytes 35
**Brian #1:** [**Python Quirks**](https://medium.com/@PhilipTrauner/python-quirks-comments-324bbf88612c) [**: Comments**](https://medium.com/@PhilipTrauner/python-quirks-comments-324bbf88612c)

- Python developers put comments in their code.
```
    # Like this
    """
    And like this
    """
    "And like this."
    ["Not usually like this","but it's possible"]```
- Philip Trauner timed all of these.
- Actual # comments are obviously way faster.
- He also shows the AST difference.
- Don’t abuse the language. Unused unreferenced strings are not free.


**Michael #2:** [**Python 3.6.2 is out!**](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-2)

- **Security**
	- bpo-30730: Prevent environment variables injection in subprocess on Windows. Prevent passing other environment variables and command arguments.
	- bpo-30694: Upgrade expat copy from 2.2.0 to 2.2.1 to get fixes of multiple security vulnerabilities including: CVE-2017-9233 (External entity infinite loop DoS), CVE-2016-9063 (Integer overflow, re-fix), CVE-2016-0718 (Fix regression bugs from 2.2.0’s fix to CVE-2016-0718) and CVE-2012-0876 (Counter hash flooding with SipHash). Note: the CVE-2016-5300 (Use os-specific entropy sources like getrandom) doesn’t impact Python, since Python already gets entropy from the OS to set the expat secret using XML_SetHashSalt().
	- bpo-30500: Fix urllib.parse.splithost() to correctly parse fragments. For example, splithost('//127.0.0.1#@evil.com/') now correctly returns the 127.0.0.1 host, instead of treating @evil.com as the host in an authentification (login@host).
- **Core and Builtins**
	- bpo-29104: Fixed parsing backslashes in f-strings.
	- bpo-27945: Fixed various segfaults with dict when input collections are mutated during searching, inserting or comparing. Based on patches by Duane Griffin and Tim Mitchell.
	- bpo-30039: If a KeyboardInterrupt happens when the interpreter is in the middle of resuming a chain of nested ‘yield from’ or ‘await’ calls, it’s now correctly delivered to the innermost frame.
	- Library
	- bpo-30038: Fix race condition between signal delivery and wakeup file descriptor. Patch by Nathaniel Smith.
	- bpo-23894: lib2to3 now recognizes rb'...' and f'...' strings.
	- bpo-24484: Avoid race condition in multiprocessing cleanup (#2159)
- **Windows**
	- bpo-30687: Locate msbuild.exe on Windows when building rather than vcvarsall.bat
	- bpo-30450: The build process on Windows no longer depends on Subversion, instead pulling external code from GitHub via a Python script. If Python 3.6 is not found on the system (via py -3.6), NuGet is used to download a copy of 32-bit Python.
- **Plus about 40 more fixes / changes**

**Brian #3:** [**Contributing to Open Source Projects: Imposter Syndrome Disclaimer**](https://github.com/adriennefriend/imposter-syndrome-disclaimer)

- “How to contribute” often part of OSS projects.
- Adrienne Lowe of codingwithknives.com has an “Imposter Syndrome Disclaimer” to include in your contributing documentation that’s pretty great.
- She’s also [collecting examples](https://github.com/adriennefriend/imposter-syndrome-disclaimer/blob/master/examples.md) of people using it, or similar.
- From the disclaimer: 

> “*Imposter syndrome disclaimer*: I want your help. No really, I do.
There might be a little voice inside that tells you you're not ready; that you need to do one more tutorial, or learn another framework, or write a few more blog posts before you can help me with this project.
I assure you, that's not the case.
…
And you don't just have to write code. You can help out by writing documentation, tests, or even by giving feedback about this work. (And yes, that includes giving feedback about the contribution guidelines.)“

**Michael #4:** [**The Dark Secret at the Heart of AI**](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/)

- via MIT Technology Review
- There’s a big problem with AI: even its creators can’t explain how it works
- Last year, an experimental vehicle, developed by researchers at the chip maker Nvidia, didn’t look different from other autonomous cars, but it was unlike anything demonstrated by Google, Tesla, or General Motors, and it showed the rising power of artificial intelligence. The car didn’t follow a single instruction provided by an engineer or programmer. Instead, it relied entirely on an algorithm that had taught itself to drive by watching a human do it.
- The result seems to match the responses you’d expect from a human driver. But what if one day it did something unexpected—crashed into a tree, or sat at a green light? 
- As things stand now, it might be difficult to find out why.
- And you can’t ask it: there is no obvious way to design such a system so that it could always explain why it did what it did.
- There’s already an argument that being able to interrogate an AI system about how it reached its conclusions is a fundamental legal right
- We’ve never before built machines that operate in ways their creators don’t understand. How well can we expect to communicate—and get along with—intelligent machines that could be unpredictable and inscrutable

**Brian #5:**  [**Arrange Act Assert pattern for Python developers**](http://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html)

- James Cooke
- Good introduction to test case structure.
- Split your tests into setup, action, assertions.
- Pattern also known by:
  - Given, When, Then
  - Setup, Test, Teardown
  - Setup, Exercise, Verify, Teardown
- Also covered in:
  - http://testandcode.com/10
  - http://pythontesting.net/strategy/given-when-then-2/

**Michael #6:** [**Analyzing GitHub, how developers change programming languages over time**](https://blog.sourced.tech/post/language_migrations/)

- From source{d}: Building the first AI that understands code
- Have you ever been struggling with an nth obscure project, thinking : “I could do the job with this language but why not switch to another one which would be more enjoyable to work with” ?
- Derived from [**The eigenvector of “Why we moved from language X to language Y”**](https://erikbern.com/2017/03/15/the-eigenvector-of-why-we-moved-from-language-x-to-language-y.html)**,** [**Erik Bernhardsson**](https://github.com/erikbern/eigenstuff) ****
- Dataset available
  - 4.5 Million GitHub users
  - 393 different languages
  - 10 TB of source code in total
- I find it nice to visualize developer’s language usage history with a kind of [**Gantt diagram**](https://en.wikipedia.org/wiki/Gantt_chart).
- We did not include Javascript because
- Most popular languages on GitHub
- At last! Here is the reward: the stationary distribution of our Markov chain. This probability distribution is independent of the initial distribution. It gives information about the stability of the process of random switching between languages. 
- | Rank | Language | Popularity, % | Source code, % |
| -- | ------ | ---- | ---- |
| 1. | Python | 16.1 | 11.3 |
| 2. | Java   | 15.3 | 16.6 |
| 3. | C      | 9.2  | 17.2 |
| 4. | C++    | 9.1  | 12.6 |
| 5. | PHP    | 8.5  | 24.4 |
| 6. | Ruby   | 8.3  | 2.6  |
| 7. | C#     | 6.1  | 6.5  |

- Python (16.1 %) appears to be the most attractive language, followed closely by Java (15.3 %). It’s especially interesting since only 11.3 % of all source code on GitHub is written in Python.
- Although there are ten times more lines of code on GitHub in PHP than in Ruby, they have the same stationary distribution.
- What about sticking to a language ?
	- Developers coding in one of the 5 most popular languages (Java, C, C++, PHP, Ruby) are most likely to switch to Python with approx. 22% chance on average.
	- Similarly, a Visual Basic developer has more chance (24%) to move to C# while Erik’s is almost sure in this transition with 92% chance.
	- People using numerical and statistical environments such as Fortran (36 %), Matlab (33 %) or R (40 %) are most likely to switch to Python in contrast to Erik’s matrix which predicts C as their future language.

