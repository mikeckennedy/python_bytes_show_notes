# Python Bytes 179
Sponsored by DigitalOcean: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: [**Guido van Rossum**](https://twitter.com/gvanrossum/)


----------

**Brian #1:** [**New governance model for the Django project**](https://www.djangoproject.com/weblog/2020/mar/12/governance/)

- James Bennet on DjangoProject Blog
- [DEP 10](https://github.com/django/deps/blob/master/accepted/0010-new-governance.rst) (Django Enhancement Proposal)
- Looks like it’s been in the making since at least 2018
- The specifics are definitely interesting
	- “core team” dissolved
	- new role, “merger” with commit access only for merging pull requests.
		- hold no decision making privileges
	- technical decisions made in public venues
	- “technical board” kept where necessary, but historically it’s rare.
		- no longer elected by committers, but anyone can run and be elected by DSF individual members.
- More interesting to me is the rationale
	- Grow the set of people contributing to Django
	- Remove the barriers to participation
	- Looking at how decisions are made anyway historically, by reviewing pull requests, and merges done by “Fellows”, paid contractors of the DSF.
- Specifically, taking into account the specifics of the current state of participation in Django, trying to set it up for inclusion and growth in the future, and the specifics of this project. Not trying to clone the governance of a different project.


----------

**Michael #2:** [**missingno**](https://github.com/ResidentMario/missingno)

- Missing data visualization module for Python.
- A small toolset of flexible and easy-to-use missing data visualizations 
- Quick visual summary of the completeness (or lack thereof) of your dataset
- Just call `msno.matrix(collisions.sample(250))` and here’s what you’ll see:

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e99eacb174b2331ce3ea70c/0aff57a3b346073ae0c832551d9ef35f/image.png)

- The sparkline at right summarizes the general shape of the data completeness and points out the rows with the maximum and minimum nullity in the dataset.
- Other visualizations are available (heat maps, bar charts, etc)
- The dendrogram allows you to more fully correlate variable completion, revealing trends deeper than the pairwise ones visible in the correlation heatmap.
- The dendrogram uses a [hierarchical clustering algorithm](http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html) (courtesy of `scipy`) to bin variables against one another by their nullity correlation.


----------

**Guido #3:** Announcements from the language summit.

* See the schedule of [topics covered here](https://us.pycon.org/2020/events/languagesummit/).

----------

 **Brian #4:** **Codes of Conduct and Enforcement**

- I’ve been thinking about this a lot lately. No reason. Just interesting topic, I think.
- Interesting the differences in CoC and enforcement clauses of different projects based on the types of interaction most likely to need enforcement.
- Two examples
	- PSF
		- Scope (focus seems to be first on events, second on online)
		- [PSF Code of Conduct](https://www.python.org/psf/conduct/)
			- being open
			- focus on what’s best for the community
			- acknowledging time and effort
			- being respectful of different viewpoints and experiences
			- showing empathy towards other community members
			- being considerate
			- being respectful
			- gracefully accepting constructive criticism
			- using welcoming and inclusive language
			- + list of inappropriate behavior
    - [PSF CoC Enforcement Procedures](https://www.python.org/psf/conduct/enforcement/)
	    - 2/3 majority vote among non conflicted work group members.
	    - Process for disagreement of the work group
    - Django
	    - Scope (focus on online spaces, events seem to be covered elsewhere)
	    - [Django Code of Conduct](https://www.djangoproject.com/conduct/)
		    - be friendly and patient
		    - be welcoming
		    - be considerate
		    - be respectful
		    - be careful in the words you choose
	        - Includes examples of harassment and exclusionary behavior that isn’t acceptable.
        - when we disagree try to understand why
    - [Django CoC Enforcement Manual](https://www.djangoproject.com/conduct/enforcement-manual/)
	    - Resolution timelines in place. Aiming for resolution within a week.
	    - Unilateral authority: Any committee member may act immediately (before consensus) to end the situation if the act is ongoing or threatening.
	    - Otherwise, consensus must be reached.
	    - Otherwise, it’s turned over to the DSF board for resolution. 
- Differences are interesting
	- The focus on online interactions and the Django push to try to get more people involved I think are part of the need for really fast reaction times for problems, and then trying to reach consensus.
	- The ability to bump the decision up to the DSF is interesting too.
	- Also the 2/3 vs consensus.
- For other projects
	- Looking at these two examples, why they are different, and what similarities and needs for inclusion and growth of more developers, online vs events, etc, before deciding how to enforce CoC on your project.
	- Enforcement and quick enforcement and public statement of what enforcement looks like seems really important. Don’t ignore it.  Figure out the process before you have to use it.

----------

**Michael #5:**  [**Myths about Indentation**](https://twitter.com/gvanrossum/status/1249549091584892928)

- Python can come across as a funky language using spacing, not { } for code blocks
- So let’s talk about some myths
- **#1 Whitespace is significant in Python source code.**
	- No, **not in general**. Only the indentation level of your statements is significant (i.e. the whitespace at the very left of your statements). 
	- Everywhere else, whitespace is not significant and **can be used as you like**, just like in any other language. 
	- The **exact amount of indentation doesn't matter at all**, but only the relative indentation of nested blocks (relative to each other). 
	- Furthermore, the indentation level is **ignored when you use explicit or implicit continuation lines**.

```
    # For example:
    >>> foo = [
    ...            'some string',
    ...         'another string',
    ...           'short string'
    ... ]
```

- **#2 Python forces me to use a certain indentation style**
	- **Yes and no**. You can write the inner block all on one line if you like, therefore not having to care about indentation at all. These are equivalent

```
    >>> if 1 + 1 == 2:
    ...     print "foo"
    ...     print "bar"
    ...     x = 42
    
    >>> if 1 + 1 == 2:
    ...     print "foo"; print "bar"; x = 42
    
    >>> if 1 + 1 == 2: print "foo"; print "bar"; x = 42 
```

	-  If you decide to write the **block on separate lines, then yes, Python forces you to obey** its indentation rules
	- The conclusion is: **Python forces you to use indentation that you would have used anyway**, unless you wanted to obfuscate the structure of the program.
	- Seen C code like this:

```
if (some condition)
	    if (another condition)
	            do_something(fancy);
else
	    this_sucks(badluck); 
```

- Either **the indentation is wrong, or the program is buggy**. In Python, this error cannot occur. The program always does what you expect when you look at the indentation.
- **#3 You cannot safely mix tabs and spaces in Python**
	- **That's right, and you don't want that.** 
	- Most good editors support transparent translation of tabs, automatic indent and dedent.
	- It's behaving like you would expect a tab key to do, but still maintaining portability by using spaces in the file only. This is convenient and safe.
- **#4 I just don't like it**
		- **That's perfectly OK**; you're free to dislike it
		- But it does have a **lot of advantages, and you get used to it very quickly** when you seriously start programming in Python. 
- **#5 How does the compiler parse the indentation**
	- The parsing is well-defined and **quite simple**. 
	- Basically, changes to the **indentation level are inserted as tokens into the token stream**.
	- After the lexical analysis (before parsing starts), **there is** ***no*** **whitespace left in the list of tokens** (except possibly within string literals, of course). In other words, the indentation is handled by the lexer, not by the parser.

----------

**Guido #6:** Parsers and LibCST

-[ https://github.com/Instagram/LibCST ](https://github.com/Instagram/LibCST)

----------

**Extras:**

Michael:

-  **Django no longer supports Python 2 AT ALL** (via Adam (Codependent Codr)). April 1st this year, the 1.11 line of Django has left Long Term Support (LTS). Leaving only 2.2.12+ with exclusively Python 3 support.
- Quick follow up on “Coding is Googling”. I went through a recent blip of mad googling.

Brian:  

-  Gotta get my talk recorded this week, deadlines Friday. A little worried. As a writer and developer, me and deadlines don’t always see eye to eye.
- Follow-ups from previous episodes:
	- Got lots of help with my Mac / Windows problem and modifier keys. Thanks everyone. Simplest solution Apple→System Prefs→Keyboard→Modifier Keys, and swap control and command for my external keyboard. So far, so good.
	- You can’t use the setuptools_scm trick to get github actions to automatically publish to Test PyPI or PyPI for Flit or Poetry projects, since the version number is a simple string in the repo.  Would love to hear if anyone has a solution to this one. Otherwise I’m fine with a make or tox snippet for publishing that combines bumping the version.  

Guido:

- PyCon goes [online](https://us.pycon.org/2020/online/). 
- Python 2.7.8 was [released](https://mail.python.org/archives/list/python-dev@python.org/message/OFCIETIXLX34X7FVK5B5WPZH22HXV342/), the last Python 2 release ever.


----------

**Joke:**

Via [https://twitter.com/derchambers/status/1226760532763410432](https://twitter.com/derchambers/status/1226760532763410432)

How can you borrow more money at the same time? With **asyncIO**Us!

