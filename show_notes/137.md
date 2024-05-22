# Python Bytes 137
Sponsored by Rollbar: [**https://pythonbytes.fm/rollbar**](https://pythonbytes.fm/rollbar)

**Brian #1:**  [**Comparing the Same Project in Rust, Haskell, C++, Python, Scala and OCaml**](http://thume.ca/2019/04/29/comparing-compilers-in-rust-haskell-c-and-python/)

- Tristan Hume, writing about a university project
- Teams of up to 3 people, multi month, write a Java to x86 compiler in language of choice
- Needed to pass both known and unknown tests.
- Secret tests to be run after submission encouraged teams to add more testing than provided.
- Nothing but standard libraries, and no parsing libraries, even if in standard.
- Lines of  code
	- Rust baseline
	- Haskell: 1-1.6x 
	- C++: 1.4x
	- Rust (another team): 3x
	- Scala: 0.7 x
	- OCaml: 1-1.6x
	- Python: about half the size
- Python version
	- one person
	- used metaprogramming
	- more extra features than any other team
	- passed all public and secret tests

**Michael #2 :** [**Pylustrator is a program to style your matplotlib plots**](https://pylustrator.readthedocs.io/en/latest/)

- via Len Wanger
- Pylustrator is a program to style your matplotlib plots for publication. 
- Subplots can be resized and dragged around by the mouse, text and annotations can be added. 
- Changes can be saved to the initial plot file as python code.

**Brian #3:**  [**MongoDB 4.2**](https://www.prnewswire.com/news-releases/mongodb-4-2-adds-distributed-transactions-field-level-encryption-updated-kubernetes-operator-and-more-to-the-leading-modern-general-purpose-database-300870262.html) 

- Distributed Transactions
	- extends multi-document ACID transactions across documents, collections, dbs in a replica set, and sharded cluster.
- Field Level Encryption
	- encryption done on client side
	- satisfies GDPR by allowing customer key destruction rendering server data on customer useless.
	- system administration can be done with no exposure to private data

**Michael #4:** [**Deep Difference and search of any Python object/data**](https://github.com/seperman/deepdiff)

- via [François Leblanc](https://twitter.com/leblancfg1)
- **DeepDiff**: Deep Difference of dictionaries, iterables, strings and other objects. It will recursively look for all the changes.
- Lots of nice touches:
	- List difference ignoring order or duplicates
	- Report repetitions
	- Exclude certain types from comparison
	- Exclude part of your object tree from comparison
	- Significant Digits
- **DeepSearch**: Search for objects within other objects.
- **DeepHash**: Hash of ANY python object based on its contents even if the object is not considered hashable! DeepHash is supposed to be deterministic in order to make sure 2 objects that contain the same data, produce the same hash.

**Brian #5:** [**Advanced Python Testing**](https://joshpeak.net/posts/2019-06-18-Advanced-python-testing.html)

- Josh Peak
- “This article is mostly for me to process my thoughts but also to pave a path for anyone that wants to follow a similar journey on some more advanced python testing topics.”
- Learning journey (including some great podcasts and an awesome book on testing)
- Testing tools
	- basic test structure
	- adding black to testing with pytest-black
	- linting with pylint
		- including a very cool speed up trick to only lint modified files.
	- flake8, including docstring checking
	- tox.ini modifications
	- code coverage goals and how to ratchet up to that goal with `--cov-fail-under`
	    - cool learning: “Increase code coverage by testing more code OR deleting code.”
	- fixtures for database connections
	- utilizing mocks, spies, stubs, and monkey patches, including `pytest-mock`
	- `pytest-vcr` to save network interactions and replay them in future test runs, resulting in a 10x speedup.
- Lots of links and tangents possible from this article.

**Michael #6:**  [**Understanding Python's del**](https://www.programiz.com/python-programming/del)

- via Kevin Buchs 
- [**Official docs**](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)
- General confusion of what this does
- Looks like memory management, and it mostly isn’t
- Primary use: remove an item from a list given its index instead of its value or from a dictionary given its key: `del person['profession'] # person is a dict`  
- del statement can also be used to remove slices from a list `del lst[2:4]`
- del can also be used to delete entire variables: `del variable`
- Recently covered how [**The CPython Bytecode Compiler is Dumb**](https://nullprogram.com/blog/2019/02/24/). Proactive dels could help.

**Extras**

Michael:

-  [**Pynsource**](https://www.pynsource.com/): Reverse engineer Python source code into UML diagrams (via Anders Klint)
- [**Language Bar chart**](https://www.youtube.com/watch?v=cKzP61Gjf00&feature=youtu.be) race (via [Josh Thurston](https://twitter.com/JoshT_Thurston/status/1142432580442234880))
- [**My Local maximum appearance**](http://localmaxradio.com/73).

**Jokes** 

Optimist: The glass is half full. Pessimist: The glass is half empty. Programmer: The glass is twice as large as necessary.

Pragmatist: allowing room for requirements oversights, scope creep, and schedule overrun.

From “The Upside” with Kevin Hart and Bryan Cranston (watched it last night):
K: Would you invest in <business idea>?
B: That seems too niche.
K: What’s “niche” mean?
B: It’s the girl version of “nephew”.
