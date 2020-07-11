# Python Bytes 189

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Brian’s pytest book**](https://t.co/AKfVKcveg6?amp=1)

**Brian #1:** [**Improving Python exception chaining with raise-from**](https://blog.ram.rachum.com/post/621791438475296768/improving-python-exception-chaining-with)

- Ram Rachum
- Python3 has a change called [PEP 3134: Exception Chaining and Embedded Tracebacks](https://www.python.org/dev/peps/pep-3134/)
- It should be used more than it is.
- If an exception is raised from an except clause, it could be because:
	- something unexpected happened
	- “An exception was raised, and we decided to replace it with a different exception that will make more sense to whoever called this code. Maybe the new exception will make more sense because we’re giving a more helpful error message. Or maybe we’re using an exception class that’s more relevant to the problem domain, and whoever’s calling our code could wrap the call with an except clause that’s tailored for this failure mode.”
- If it’s the second case, you should change your code to something like this:
```
    try:
        <something>
    except ExpectedExceptionType as e:
        raise BetterException('Better explanation') from e
```
- It’s the `from e` that does the magic.
- And now instead of getting `During handling of the above exception, another exception occurred:`
- You get: `The above exception was the direct cause of the following exception:`
- “That’s how you know you have a case of a friendly wrapping of an exception.”

**Michael #2:** [**Create and publish interactive reports in Python**](https://www.datapane.com/)

- via Tim Pogue
- Datapane is an open source framework which makes it easy to turn scripts and notebooks into interactive reports. 
- Free for individuals, paid(?) for teams
- Build reports in Python and deploy scripts and notebooks as self-service reporting tools.
- **Analyze data in your own tools:** Write code and analyze data in your own editor or environment, whether its Jupyter, Colab, or Airflow.
- **Build reports in code:** Datapane's framework makes it easy to create rich reports from DataFrames, Markdown, and visualization libraries, such as Altair.
- **Publish and share:** Export as standalone HTML files, or publish reports to Datapane.com for free, where they can be shared and embedded.
- Add forms to filter / drive the report
- Everything in Datapane is an API. Deploy scripts and generate reports from your server, GitHub, Airflow, or CI system.
- Check out [the gallery](https://www.datapane.com/gallery/).

**Brian #3:** [**Pickle’s nine flaws**](https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html)

- Ned Batchelder
- Instead of “never use pickle”, Ned says “only use pickle if you are OK with it’s nine flaws”
- The flaws
	- Insecure : Malicious pickles can get the unpickler to run bad code
	- Old pickles look like old code : Any changes to your data structures might break your ability to read old pickles
	- Implicit: All data is serialized as class objects, even if that’s not what you want.
	- Over-serializes: Serializes everything in your objects, even things like cached computation
	- `__init__` isn’t called : during unpickling, even if it really should be for your situation
	- Python only : for the most part, it’s not something you can use with other languages
	- Unreadable: binary, so good luck debugging problems
	- Appears to pickle code: but doesn’t really. Keeping a list of functions or classes? It’ll get pickled as names and get bound to a function/class matching the name during unpickling.
	- Slow
- Some of it you can work around, but then, why?
- Alternatives: JSON, marshmallow, cattrs, protocol buffers, … 

**Michael #4:** [**PEP 602 -- Annual Release Cycle for Python**](https://www.python.org/dev/peps/pep-0602/)

- by Łukasz Langa
- Status accepted
- This PEP proposes that Python 3.X.0 will be developed for around 17 months:
	- The first *five months* overlap with Python 3.(X-1).0's beta and release candidate stages and are thus unversioned.
	- The next *seven months* are spent on versioned alpha releases where both new features are incrementally added and bug fixes are included.
	- The following *three months* are spent on four versioned beta releases where **no new features** can be added but bug fixes are still included.
	- The final *two months* are spent on two release candidates (or more, if necessary) and conclude with the release of the final release of Python 3.X.0.
- Annual release cadence: Feature development of Python 3.(X+1).0 starts as soon as Python 3.X.0 Beta 1 is released. This creates a twelve month delta between major Python versions.
- This change provides the following advantages:
	- makes releases smaller: since doubling the cadence doesn't double our available development resources, consecutive releases are going to be smaller in terms of features;
	- puts features and bug fixes in hands of users sooner;
	- creates a more gradual upgrade path for users, by decreasing the surface of change in any single release;
	- creates a predictable calendar for releases where the final release is always in October (so after the annual core sprint), and the beta phase starts in late May (so after PyCon US sprints), which is especially important for core developers who need to plan to include Python involvement in their calendar;

**Brian #5:** **More git Resources:** 

- [On episode 187](https://pythonbytes.fm/187) we talked about Oh Sh*t, Git!, a zine by Julia Evans 
    I mentioned that I was concerned about buying it for a team due to the mild swearing.
    John Place reached out to tell us there’s a non-swearing version:
	- [Dangit, git!](https://gumroad.com/l/dangit-git), the zine.
    
- Also both of these are inspired by two websites by Katie Sylor-Miller:
	- [dangitgit.com](http://dangitgit.com/)
	- [ohshitgit.com](https://ohshitgit.com/)
	- These are free websites with “something went wrong, how to I fix it” solutions.
	- All issues have titles that are links/anchors, so you can send someone a link if they ask you a question of how to fix something with git, and hopefully they can figure it out themselves sometime.
    
- Also [Git Cheatsheet](http://ndpsoftware.com/git-cheatsheet.html) 
	- Not just a pdf
	- An interactive single page site that is, for one, beautifully designed.
	- There’s 5 columns: Stash, Workspace, Index, Local Repo, Upstream Repo
	- Hover over a column and it shows you git commands that affect that part and flows to other columns.
	- Hover over a command and the description pops up at the bottom.
	- The visual is great for reinforcing how actions move data between different parts of a repository, and a great way to teach people to have that mental model that git is not just your repo, it’s all of these components working together.


- Lastly, [git-pretty](http://justinhileman.info/article/git-pretty/git-pretty.png)
	- Similar goals as the dangit and ohsh*t offerings, this is a single page png flowchart that starts with “so you have a mess on your hands” and asks a bunch of questions to funnel you to how to fix it. A fun thing to print out and pin to your wall.

**Michael #6:** [**PEP 616 -- String methods to remove prefixes and suffixes**](https://www.python.org/dev/peps/pep-0616/)

- Dennis Sweeney
- Status: Accepted
- Question: What does this return? `“saturday is the 1st".strip('st')` 
- Answer: `aturday is the 1`
- If you expected it to remove the string `st`, well, no. That’s PEP 616.
- Add two new methods, `removeprefix()` and `removesuffix()`, to the APIs of Python's various string objects. These methods would remove a prefix or suffix (respectively) from a string, if present, and would be added to Unicode str objects, binary bytes and bytearray objects, and collections.UserString.

Extras:

Michael: 

- [Manning conference Python Bytes event](https://freecontent.manning.com/register-for-livemanning-python/) 
- [Michael's 10 tips for web dev PyCon recording out](https://twitter.com/mkennedy/status/1276193238710390789)
- [Learn Python Humble Bundle](https://talkpython.fm/humble2020)
- Telegram bots
    - by Abhishek Pednekar
    - [Python Bytes](https://t.me/PythonBytesBot)
    - https://t.me/TalkPythonBot

Joke:

Karen Chee (@karencheee):

- **you:** A famous engineer / inventor is coming over for dinner tonight, want to join us?
- **me:** Sure, who is it?
- **you:** His name is Rube Goldberg
- **me:** That name rings a bell, which sets off a trap that undoes a buckle and releases a ball that rolls down a pipe and …

