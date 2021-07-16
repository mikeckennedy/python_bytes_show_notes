# Python Bytes 242

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Al Sweigart**

**Brain #1:** [**just**](https://github.com/casey/just)

- [From a tweet by Jeff Triplett](https://twitter.com/webology/status/1415304388969705482?s=20)
- “`just` is a handy way to save and run project-specific commands.
- Commands, called recipes, are stored in a file called `justfile` with syntax inspired by `make`
- Just is a command runner, not a build system, so it avoids much of Make’s complexity and idiosyncrasies. No need for .PHONY recipes!
- Linux, MacOS, and Windows are supported with no additional dependencies.”
- It’s written in Rust.
- My favorite differences:
	- a couple spaces is fine, no need for tabs
	- Recipes can accept command line arguments
	- Recipes can be [listed from the command line](https://github.com/casey/just#listing-available-recipes).
	- Recipes can be written in [arbitrary languages](https://github.com/casey/just#writing-recipes-in-other-languages), 
```
like Python
    hello:
      echo "Hello World!"
    
    pyhello:
      #!/usr/bin/env python3
      print('Hello from python!')
```

**Michael #2:** [**Strong Typing**](https://twitter.com/roman_the_right/status/1403077836693544966)

- via Roman Right (Beanie)
- Decorator which checks whether the function is called with the correct type of parameters.
- Decorator which **checks at Runtime** whether the function is called with the correct type of parameters.
- ***Raises*** **TypeMisMatch** if the used parameters in a function call where invalid.

**Al #3:**

- New book: [“The Big Book of Small Python Projects”](https://inventwithpython.com/bigbookpython/)
- New book: [“Beyond the Basic Stuff with Python”](https://inventwithpython.com/beyond/)

**Brian #4:** ****[**testbook**](https://testbook.readthedocs.io/en/latest/index.html#)

- [Suggested by David Nicholson](https://twitter.com/nicholdav/status/1415329582014767106?s=20)
	- Write conventional unit tests for Jupyter Notebooks
	- [Execute all or some specific cells before unit test](https://testbook.readthedocs.io/en/latest/usage/index.html#using-execute-to-control-which-cells-are-executed-before-test)
	- [Share kernel context across multiple tests](https://testbook.readthedocs.io/en/latest/usage/index.html#share-kernel-context-across-multiple-tests) (using pytest fixtures)
	- [Support for patching objects](https://testbook.readthedocs.io/en/latest/usage/index.html#support-for-patching-objects)
	- Inject code into Jupyter notebooks
	- Works with any unit testing library, unittest, pytest, etc.
- example `foo.ipynb`:

```
    def foo(a, b):
       return a + b
```
 
-  `test_foo.py`:

```
    from testbook import testbook
    
    @testbook('foo.ipynb', execute=True)
    def test_foo(tb):
       foo = tb.ref("foo")
       assert foo(1, 2) == 3
```

**Michael #5:** [**auto-all**](https://github.com/jongracecox/auto-all)

- Automatically manage the __all__ variable in Python modules.
	- Easily populate the `__all__` variable in modules.
	- Easily exclude imported objects
	- Clearly differentiate between internal and external facing objects.
	- Use simple, intuitive code.
	- Never worry about forgetting to add new objects to `__all__`.
	- Help Python IDE's differentiate between internal and external facing objects.
- Can use “regions” via `start_all()` and `end_all()`
- I prefer the decorator (functions only, seems ripe for a PR for classes)

```
    @public
    def a_public_function():
        pass
```

**Al #6:**

- Next book: Untitled Recursion Book

**Extras**

Michael:

- [**OhMyPosh + auto env**](https://twitter.com/feoh/status/1413678332743495682)
- [**A scalable method of determining physiological endotypes of sleep apnea from a polysomnographic sleep study**](https://academic.oup.com/sleep/article/44/1/zsaa168/5905594)
- Email, inbox woes, and catching up
- [**Microsoft unveils Windows 365**](https://news.microsoft.com/2021/07/14/microsoft-unveils-windows-365-ushering-in-a-new-category-of-computing/)
- [**Facebook and its advertisers are ‘panicking’ as the majority of iPhone users opt out of tracking**](https://9to5mac.com/2021/07/14/facebook-tracking-app-tracking-data/)

**Al**

- [GitHub repo for PyAutoGUI](https://github.com/asweigart/pyautogui)
