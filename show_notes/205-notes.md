# Python Bytes 205
Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Michael #1:**  [Awkward arrays](https://awkward-array.org)

- via Simon Thor
- Awkward Array is a library for **nested, variable-sized data**, including arbitrary-length lists, records, mixed types, and missing data, using **NumPy-like idioms**.
- This makes it better than numpy at handling data where e.g. the rows in a 2D array have different lengths. It can even be used together with numba to jit-compile the code to make it even faster.
- Arrays are **dynamically typed**, but operations on them are **compiled and fast**. Their behavior coincides with NumPy when array dimensions are regular and generalizes when they’re not.
- Recently rewritten in C++ for the 1.0 release and can even be used from C++ as well as Python.
- Careful on installation: `pip install awkward1` ← Notice the 1.

**Brian #2:** [**Ordered dict surprises**](https://nedbatchelder.com/blog/202010/ordered_dict_surprises.html)

- Ned Batchelder
- “Since Python 3.6, regular dictionaries retain their insertion order: when you iterate over a dict, you get the items in the same order they were added to the dict. Before 3.6, dicts were unordered: the iteration order was seemingly random.”
- The surprises:
	- You can’t get the first item, like d[0], since that’s just the value matching key 0, if key 0 exists. (I’m not actually surprised by this.)
	- equality and order (this I am surprised by)
		- Python 3.6+ dicts ignores order when testing for equality
        - `{"a": 1, "b": 2} == {"b": 2, "a": 1}`
    - OrderdDicts care about order when testing for equality
        - `OrderedDict([("a", 1), ("b", 2)]) != OrderedDict([("b", 2), ("a", 1)])`

**Michael #3:**  [jupyter lab autocomplete and more](https://github.com/krassowski/jupyterlab-lsp)

- via Anders Källmar
- Examples show Python code, but most features also work in R, bash, typescript, and many other languages.
- **Hover:** Hover over any piece of code; if an underline appears, you can press Ctrl to get a tooltip with function/class signature, module documentation or any other piece of information that the language server provides
- **Diagnostics:** Critical errors have red underline, warnings are orange, etc. Hover over the underlined code to see a more detailed message
- **Jump to Definition:** Use the context menu entries to jump to definitions
- **Highlight References:** Place your cursor on a variable, function, etc and all the usages will be highlighted
- **Automatic Completion:** Certain characters, for example '.' (dot) in Python, will automatically trigger completion
- **Automatic Signature Suggestions:** Function signatures will automatically be displayed
- **Rename:** Rename variables, functions and more, in both: notebooks and the file editor.

**Brian #4:** [**Open Source Tools & Data for Music Source Separation**](https://source-separation.github.io/tutorial/landing.html)

- An online “book” powered by Jupyter Book
- By Ethan Manilow, Prem Seetharaman, and Justin Salamon
- A tutorial intended to guide people “through modern, open-source tooling and datasets for running, evaluating, researching, and deploying source separation approaches. We will pay special attention to musical source separation, though we will note where certain approaches are applicable to a wider array of source types.”
- Uses Python and interactive demos with visualizations.
- Section “basics of source separation” that includes a primer on digitizing audio signals, a look time frequency representations, what phase is, and some evaluations and measurements.
- Includes 
	- use of a library called nussl
	- deep learning approaches
	- datasets
	- training deep networks
- Brian’s comments:
	- Very cool this is an open source book
	- Even if you don’t care about source separation, the primer on waveform digitization is amazing.
	- The interactive features are great.

**Michael #5:** [**Pass by Reference in Python: Background and Best Practices**](https://realpython.com/python-pass-by-reference/)

- Does Python have pointers?
- Some languages handle function arguments as **references** to existing variables, which is known as **pass by reference**. Other languages handle them as **independent values**, an approach known as **pass by value**.
- Python uses pass by assignment, very similar to pass by ref.
- In languages that default to passing by value, you may find performance benefits from passing the variable by reference instead
- If you actually want to change the value, consider
	- Returning multiple values with tuple unpacking
	- A mutable data type
	- Returning optional “value” types
    - For example, how would we recreate this in Python?
    public static bool TryParse (string s, out int result);
- Tuple unpacking

```
    def tryparse(string, base=10):
        try:
            return True, int(string, base=base)
        except ValueError:
            return False, None
```

```
    success, result = tryparse("123")
```

- Optional types:

```
    def tryparse(string, base=10) -> Optional[int]:
        try:
            return int(string, base=base)
        except ValueError:
            return None
```

```
    if (n := tryparse("123")) is not None:
        print(n)
```

- Best Practice: Return and Reassign

**Brian #6:** [**Visualizing Git Concepts**](https://onlywei.github.io/explain-git-with-d3/)

- by [onlywei](https://github.com/onlywei) Wei Wang
- [Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) is good, and important, but hard to get all these concepts to sink in well until you play with it.
- [Visualizing Git Concepts with D3](https://onlywei.github.io/explain-git-with-d3/) solidifies the concepts
- Practice using git commands without any code, just visualizing the changes to the repository (and sometimes the remote origin repository) while typing commands.
	- commit, branch, checkout, checkout -b
	- reset, revert
	- merge, rebase
	- tag
	- fetch, pull, push
- Incredibly powerful to be able to play around with these concepts without using any code or possibly mucking up your repo.

Extras:

Brian: 

- [micro:bit now has a speaker and a microphone](https://microbit.org/new-microbit/) - available in November

Michael:

- [**Firefox containers**](https://twitter.com/mkennedy/status/1316837032916705280)
- [**Twitch!**](https://twitter.com/ChristosMatskas/status/1318551481021272064) 

Joke:

**Q:** Where do developers drink?
**A:** The Foo bar

**-** Knock Knock!
**-** An async function
**-** Who's there?
