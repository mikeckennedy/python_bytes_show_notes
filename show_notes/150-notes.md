# Python Bytes 150

Sponsored by Datadog: [*pythonbytes.fm/datadog*](http://pythonbytes.fm/datadog)

Michael #1: [**How to Stand Out in a Python Coding Interview**](https://realpython.com/python-coding-interview-tips/)

- Real Python, by [James Timmins](https://realpython.com/python-coding-interview-tips/#author)
- Are tech interviews broken? Well at least we can try to succeed at them anyway
- You’ve made it past the phone call with the recruiter, and now it’s time to show that you know how to solve problems with actual code…
- Interviews aren’t just about solving problems: they’re also about showing that you can write clean production code. This means that you have a deep knowledge of Python’s built-in functionality and libraries.
- Things to learn
	- Use `enumerate()` to iterate over both indices and values
	- Debug problematic code with `breakpoint()`
	- Format strings effectively with f-strings
	- Sort lists with custom arguments
	- Use generators instead of list comprehensions to conserve memory
	- Define default values when looking up dictionary keys
	- Count hashable objects with the `collections.Counter` class
	- Use the standard library to get lists of permutations and combinations

**Brian #2:** [**The Python Software Foundation has updated its Code of Conduct**](http://pyfound.blogspot.com/2019/09/the-python-software-foundation-has_24.html)

- There’s now one code of conduct for PSF and PyCon US and other spaces sponsored by the PSF
- This includes some regional conferences, such as PyCascades, and some meetup groups, (ears perk up)
- The docs
	- [Code of Conduct](https://www.python.org/psf/conduct/)
	- [Enforcement Guidelines](https://www.python.org/psf/conduct/enforcement/)
	- [Reporting Guidelines](https://www.python.org/psf/conduct/reporting/)
- Do we need to care?
	- all of us, yes. If there weren’t problems, we wouldn’t need these.
	- attendees, yes. Know before you go.
	- organizers, yes. Better to think about it ahead of time and have a plan than have to make up a strategy during an event if something happens.
	- me, in particular, and Michael. Ugh. yes. our first meetup is next month. I’d like to be in line with the rest of Python. So, yep, we are going to have to talk about this and put something in place.

Michael #3: [**The Interview Study Guide For Software Engineers**](https://dev.to/seattledataguy/the-interview-study-guide-for-software-engineers-764)

- A checklist on my last round of interviews that covers many of the popular topics.
- Warm Up With The Classics
	1. [Fizz Buzz](https://www.hackerrank.com/challenges/fizzbuzz/problem)
	2. [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
	3. [Arrays: Left Rotation](https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)
	4. [Strings: Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)
	5. [Nth Fibonacci](https://www.algoexpert.io/questions/Nth%20Fibonacci)
- Many many videos on interview topics and ideas
	- Data Structures 
	- Algorithms 
	- Big O Notation
	- Dynamic Programming
	- String Manipulation
	- System Design
	- Operating Systems
	- Threads
	- Object Oriented
	- Design Patterns
	- SQL
- Fun conversation in the comments

**Brian #4:** [**re-assert**](https://github.com/asottile/re-assert) **: “show where your regex match assertion failed”**

- Anthony Sotille
- “`re-assert` provides a helper class to make assertions of regexes simpler.”
- The `Matches` objects allows for useful pytest assertion messages
- In order to get my head around it, I looked at the test code:
	- [https://raw.githubusercontent.com/asottile/re-assert/master/tests/re_assert_test.py](https://raw.githubusercontent.com/asottile/re-assert/master/tests/re_assert_test.py)
	- and modified it to remove all of the `with pytest.raises(AssertionError)…` to actually get to see the errors and how to use it.
    
```
        def test_match_old():
    >       assert re.match('foo', 'fob')
    E       AssertionError: assert None
    E        +  where None = <function match at 0x101aaa268>('foo', 'fob')
    E        +    where <function match at 0x101aaa268> = re.match
    
    test_re.py:8: AssertionError
    ____________ test_match_new ___________________
    
        def test_match_new():
    >       assert Matches('foo') == 'fob'
    E       AssertionError: assert Matches('foo') ^ == 'fob'
    E         -Matches('foo')
    E         -    # regex failed to match at:
    E         -    #
    E         -    #> fob
    E         -    #    ^
    E         +'fob'
```

Michael #5: [**awesome-python-typing**](https://github.com/typeddjango/awesome-python-typing)

- Collection of awesome Python types, stubs, plugins, and tools to work with them.
- Taxonomy
	- [Static type checkers](https://github.com/typeddjango/awesome-python-typing#static-type-checkers)
	- [Stub packages](https://github.com/typeddjango/awesome-python-typing#stub-packages)
	- [Tools](https://github.com/typeddjango/awesome-python-typing#tools)
	- [Integrations](https://github.com/typeddjango/awesome-python-typing#integrations)
	- [Articles](https://github.com/typeddjango/awesome-python-typing#articles)
	- [Communities](https://github.com/typeddjango/awesome-python-typing#communities)
	- [Related](https://github.com/typeddjango/awesome-python-typing#related)
- Static type checkers: [mypy](https://github.com/python/mypy) - Optional static typing for Python 3 and 2 (PEP 484).
- Stub packages: [Typeshed](https://github.com/python/typeshed) - Collection of library stubs for Python, with static types.
- Tools (super category): [pytest-mypy](https://github.com/dbader/pytest-mypy) - Mypy static type checker plugin for Pytest.
- Articles: [Typechecking Django and DRF](https://sobolevn.me/2019/08/typechecking-django-and-drf) - Full tutorial about type-checking django.

**Brian #6:** [**Developer Advocacy: Frequently Asked Questions**](https://dev.to/di/developer-advocacy-frequently-asked-questions-577k)

- Dustin Ingram
- I know a handful of people who have this job title. What is it? 
- disclaimer: Dustin is a DA at Google. Other companies might be different
- What is it? 
	- “I help represent the Python community at [company]"
	- “part of my job is to be deeply involved in the Python community.”
	- working on projects that help Python, PyPI, packaging, etc.
	- speaking at conferences
	- talking to people. customers and non-customers
	- talking to product teams
	- being “user zero” for new products and features
	- paying attention to places users might raise issues about products
	- working in open source
	- creating content for Python devs
	- being involved in the community as a company rep
	- representing Python in the company
	- coordinating with other DAs
- Work/life?
	- Not all DAs travel all the time. that was my main question.
    
- Talk Python episode: [War Stories of the Developer Evangelists](https://talkpython.fm/episodes/show/189/war-stories-of-the-developer-evangelists)

Extras:

- [https://www.meetup.com/Python-PDX-West/](https://www.meetup.com/Python-PDX-West/)

Michael:

- [requests moves to PSF](https://www.reddit.com/r/Python/comments/d6dnrd/requests_moved_to_python_software_foundation/)

Joke:

via [https://twitter.com/NotGbo/status/1173667028965777410](https://twitter.com/NotGbo/status/1173667028965777410)

[Web Dev Merit Badges](https://css-tricks.com/web-development-merit-badges)
