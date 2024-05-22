# Python Bytes 269

----------

CONNECTION INFO:
**Streamyard video call/stream:**     https://streamyard.com/jynqhh65j6
**Zencaster HQ audio:**                         https://zencastr.com/okken/python-bytes-269
Public YouTube stream:                  https://www.youtube.com/watch?v=7LkGcaehEek

----------

Sponsored by Datadog: [**pythonbytes.fm/datadog**](http://pythonbytes.fm/datadog)

Special guest: Luciana


**Brian #1:**[**rich-cli**](https://github.com/textualize/rich-cli)

- suggested by Lance Reinsmith
- `rich` on the command line.
- why?
    - syntax highlighting
        - `rich example.py`
        - `rich -m README.md` use `-m` for markdown
            - why Will? `.md` seems clear enough to me. 
    - comes with themes. ex: `--theme monokai` 
    - formats json, `--json` or `-j`
- and a bunch of other features I probably won’t use, but you might.
    - alignment, maybe
    - width, yeah, I’ll probably use `-w`
    - a bunch more
- In my .zshrc: `alias cat='rich --theme monokai'` 
    - after `pipx install rich-cli`
    - feel free to tell me that I shouldn’t used cat for looking at file contents. (although, why not?)
    - I’m not, I’m using rich. :)

**Luciana** **#2:** [**debugpy**](https://github.com/Microsoft/debugpy) - a debugger for Python

- The debugger we use in the Python extension for VS Code
- Super heplful features that can save up a lot of time and a lot of folks don’t seem to know about:
    - [Conditional breakpoints](https://code.visualstudio.com/Docs/editor/debugging#_conditional-breakpoints)
        - Helpful when you want the code to break only on a specific condition
        - e.g. # of execution times, or when an expression is true  
    - [Debug console](https://code.visualstudio.com/Docs/editor/debugging#_debug-console-repl)
        - Helpful for quick testing using the context of the program at the breakpoint 
        - Temp edits on variable values, expresison evaluation, etc. 
    - [Jump to Cursor](https://devblogs.microsoft.com/python/python-in-visual-studio-code-february-2020-release/#in-case-you-missed-it-jump-to-cursor) (a.k.a. Set Next Statement) 
        - Control on what is the next line the debugger will execute
        - Including previously executed lines




**Brian #3:** [**Documentation unit tests**](https://simonwillison.net/2018/Jul/28/documentation-unit-tests)

- Simon Willison
- Post talking about using pytest and tests to check documentation.
- Simon has test code that
    - introspects the code
    - introspects the docs
    - then makes sure some items are definitely in the docs
- This is used in Datasette, so you can look at the example in the repo
- What’s tested:
    - config options are all documented
    - plugin hooks are documented
    - views are all documented
- Cool use of parametrize to generate test cases based on introspection
- Nice use of fixtures
- Very cool idea


**Luciana** **#4:** [**PEP 673 — Self Type**](https://www.python.org/dev/peps/pep-0673)

- Heard from Brett Cannon that it has been accepted!
- Interesting for me as I’m learning more about types in Python 
- Adds a way to annotate methods that return an instance of their class 
- Particularly interesting for subclasses, exemple they gave:
    from __future__ import annotations
    class Shape:

```
def set_scale(self, scale: float) -> Shape:
            self.scale = scale
            return self
    
     class Circle(Shape):
        def set_radius(self, r: float) -> Circle:
            self.radius = r
            return self
    
    Circle().set_scale(0.5)  # *Shape*, not Circle
    Circle().set_scale(0.5).set_radius(2.7)
    
    # => Error: Shape has no attribute set_radius
```

**Extras**

Luciana:

- [Black](https://github.com/psf/black/releases/tag/22.1.0) is no longer in beta! Version 22.1.0 is out 🥳
- [PyCascades 2022](https://pretix.eu/pycascades/remote-2022/) reminder (remote!)

**Joke:** 
        

![](https://paper-attachments.dropbox.com/s_EAD62E7479ACC2B6C89E0EA7DECFCDFB25D47F094A3C3B80C5B6BABA8C912139_1643831496855_image.png)

