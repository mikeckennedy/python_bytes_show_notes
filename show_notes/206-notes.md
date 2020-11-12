# Python Bytes 206

Sponsored by Techmeme Ride Home podcast: [**pythonbytes.fm/ride**](http://pythonbytes.fm/ride)

Special guest: [**Steve Dower - @zooba**](https://twitter.com/zooba)

**Brian #1:** [**Making Enums (as always, arguably) more Pythonic**](https://www.cosmicpython.com/blog/2020-10-27-i-hate-enums.html)

- “I hate enums” 
- Harry Percival
- Hilarious look at why enums are frustrating in Python and a semi-reasonable workaround to make them usable.
- Problems with enums of strings:
	- Can’t directly compare enum elements with the values
	- Having to use `.value` is dumb.
	- Can’t do random choice of enum values
	- Can’t convert directly to a list of values
- If you use `IntEnum` instead of `Enum` and use integer values instead of strings, it kinda works better.
- Making your own `StringEnum` also is better, but still doesn’t allow comparison.
- Solution:

```
    class BRAIN(str, Enum):
        SMALL = 'small'
        MEDIUM = 'medium'
        GALAXY = 'galaxy'
    
        def __str__(self) -> str:
            return str.__str__(self)
```

- Derive from both `str` and `Enum`, and add a `*__str(self)__*` method.
- Fixes everything except `random.choice()`.

**Michael #2:** [Python 3.10 will be up to 10% faster](https://twitter.com/1st1/status/1318558048265404420)

- 4.5 years in the making, from Yury Selivanov
- work picked up by Pablo Galindo, Python core developer, Python 3.10/3.11 release manager
- LOAD_METHOD, CALL_METHOD, and LOAD_GLOBAL improved
- “Lot of conversations with Victor about his PEP 509, and he sent me a link to his amazing compilation of notes about CPython performance.  One optimization that he pointed out to me was LOAD/CALL_METHOD opcodes, an idea first originated in PyPy.”
- There is a patch that implements this optimization
- Based on: LOAD_ATTR stores in its cache a pointer to the type of the object it works with, its tp_version_tag, and a hint for PyDict_GetItemHint.  When we have a cache hit, LOAD_ATTR becomes super fast, since it only needs to lookup key/value in type's dict by a known offset (the real code is a bit more complex, to handle all edge cases of descriptor protocol etc).

 
**Steve #3:** **Python 3.9 and no more Windows 7**

- [PEP 11 -- Removing support for little used platforms | Python.org](https://www.python.org/dev/peps/pep-0011/)
- [Windows 7 - Microsoft Lifecycle | Microsoft Docs](https://docs.microsoft.com/en-us/lifecycle/products/windows-7)
- Default x64 download

**Brian #4:** [**Writing Robust Bash Shell Scripts**](https://www.davidpashley.com/articles/writing-robust-shell-scripts/)

- David Pashley
- Some great tips that I learned, and I’ve been writing bash scripts for decades.
- `set -u` : exits your script if you use an uninitialized variable
- `set -e` : exit the script if any statement returns a non-true return value. Prevents errors from snowballing.
- Expect the unexpected, like missing files, missing directories, etc.
- Be prepared for spaces in filenames. `if [ "$filename" = "foo" ];`
- Using `trap` to handle interrupts, exits, terminal kills, to leave the system in a good state.
- Be careful of race conditions
- Be atomic 

**Michael #5:** [**Ideas for 5x faster CPython**](https://twitter.com/anthonypjshaw/status/1318701123692236801)

- Twitter post by Anthony Shaw calling attention to [roadmap by Mark Shannon](https://github.com/markshannon/faster-cpython/blob/master/plan.md)
- **Implementation plan for speeding up CPython:** The overall aim is to speed up CPython by a factor of (approximately) five. We aim to do this in four distinct stages, each stage increasing the speed of CPython by (approximately) 50%: 1.5**4 ≈ 5
- Each stage will be targeted at a separate release of CPython. 
- **Stage 1** -- Python 3.10: The key improvement for 3.10 will be an adaptive, specializing interpreter. The interpreter will adapt to types and values during execution, exploiting type stability in the program, without needing runtime code generation.
- **Stage 2** -- Python 3.11: Improved performance for integers of less than one machine word. Faster calls and returns, through better handling of frames. Better object memory layout and reduced memory management overhead.
- **Stage 3** -- Python 3.12 (requires runtime code generation): Simple "JIT" compiler for small regions.
- **Stage 4** -- Python 3.13 (requires runtime code generation): Extend regions for compilation. Enhance compiler to generate superior machine code.
- [Wild conversation over here](https://www.mail-archive.com/python-dev@python.org/msg110071.html).
- One excerpt, from Larry Hastings:
- *Speaking as the Gilectomy guy: borrowed references are evil.  The definition of the valid lifetime of a borrowed reference doesn't exist, because they are a hack (baked into the API!) that we mostly "get away with" just because of the GIL.  If I still had wishes left on my monkey's paw I'd wish them away (1).*
- * (1) Unfortunately, I used my last wish back in February, wishing I could spend more time at home.*

**Steve #6:** **CPython core developer sprints**

- Hosted by [pythondiscord.com](https://pythondiscord.com)
- [https://youtu.be/gXMdfBTcOfQ](https://youtu.be/gXMdfBTcOfQ) - Core dev Q&A

**Extras**

**Brian:**

- Tools I found recently that are kinda awesome in their own way - Brian
	- [mcbroken.com](https://mcbroken.com/) - Is the ice cream machine near you working? 
	    - just a funny single purpose website
	- [vim-adventures.com](https://vim-adventures.com/) - with a dash. Practice vim key bindings while playing an adventure game. Super cool. 

**Joke:**

Hackobertfest 2020 t-shirt
[https://twitter.com/McCroden/status/1319646107790704640](https://twitter.com/McCroden/status/1319646107790704640) 

![Image](https://pbs.twimg.com/media/ElBTI-zW0AA4Dfy?format=jpg&name=medium)

- [5 Most Difficult Programming Languages in the World](https://levelup.gitconnected.com/5-most-difficult-programming-languages-in-the-world-549c3cf91b23)
	- (Not really long enough for a full topic, but funny. I think I’ll cut short the last code example after we record)
	- suggested by Troy Caudill
	- Author: Lokajit Tikayatray
	- malboge, intercal, brainf***, cow, and whitespace
	- whitespace is my favorite: “Entire language depends on *space*, *tab*, and *linefeed* for writing any program. The Whitespace interpreter ignores Non-Whitespace characters and considers them as code comments.”
	- Intercal is kinda great in that 
	- One thing I love about this article is that the author actually writes a “Hello World!” for each language.
	- Examples of “Hello World!”
    - malboge
```
    (=<`#9]~6ZY32Vx/4Rs+0No-&Jk)"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:'8dc
```
- intercal
```
    DO ,1 <- #13
    PLEASE DO ,1 SUB #1 <- #238
    DO ,1 SUB #2 <- #108
    DO ,1 SUB #3 <- #112
    DO ,1 SUB #4 <- #0
    DO ,1 SUB #5 <- #64
    DO ,1 SUB #6 <- #194
    DO ,1 SUB #7 <- #48
    PLEASE DO ,1 SUB #8 <- #22
    DO ,1 SUB #9 <- #248
    DO ,1 SUB #10 <- #168
    DO ,1 SUB #11 <- #24
    DO ,1 SUB #12 <- #16
    DO ,1 SUB #13 <- #162
    PLEASE READ OUT ,1
    PLEASE GIVE UP
```

- brain**ck (censored)

```
    ++++++++++[>+++++++>++++++++++>+++<<<-]>++.>+.+++++++
     ..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.
```

- cow
```
    MoO MoO MoO MoO MoO MoO MoO MoO MOO moO MoO MoO MoO MoO MoO moO MoO MoO MoO MoO moO MoO MoO MoO MoO moO MoO MoO MoO MoO MoO MoO MoO
     MoO MoO moO MoO MoO MoO MoO mOo mOo mOo mOo mOo MOo moo moO moO moO moO Moo moO MOO mOo MoO moO MOo moo mOo MOo MOo MOo Moo MoO MoO 
     MoO MoO MoO MoO MoO Moo Moo MoO MoO MoO Moo MMM mOo mOo mOo MoO MoO MoO MoO Moo moO Moo MOO moO moO MOo mOo mOo MOo moo moO moO MoO 
     MoO MoO MoO MoO MoO MoO MoO Moo MMM MMM Moo MoO MoO MoO Moo MMM MOo MOo MOo Moo MOo MOo MOo MOo MOo MOo MOo MOo Moo mOo MoO Moo
```

- whitespace
```
    S S S T        S S T        S S S L
    T        L
    S S S S S T        T        S S T        S T        L
    T        L
    S S S S S T        T        S T        T        S S L
    T        L
    S S S S S T        T        S T        T        S S L
    T        L
    S S S S S T        T        S T        T        T        T        L
    T        L
    S S S S S T        S T        T        S S L
    T        L
    S S S S S T        S S S S S L
    T        L
    S S S S S T        T        T        S T        T        T        L
    T        L
    S S S S S T        T        S T        T        T        T        L
    T        L
    S S S S S T        T        T        S S T        S L
    T        L
    S S S S S T        T        S T        T        S S L
    T        L
    S S S S S T        T        S S T        S S L
    T        L
    S S S S S T        S S S S T        L
    T        L
    S S L
    L
    L
```

- [**APL**](https://en.wikipedia.org/wiki/APL_(programming_language)): `(~R∊R∘.×R)/R←1↓ιR`


