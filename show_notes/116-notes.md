# Python Bytes 116
Sponsored by [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Inside python dict — an explorable explanation**](https://just-taking-a-ride.com/inside_python_dict/chapter1.html)

- Interactive tutorial on dictionaries
	- Searching efficiently in a list
	- Why are hash tables called has tables?
	- Putting it all together to make an “almost”-Python-dict
	- How Python dict really works internally
- Yes this is a super deep dive, but wow it’s cool.
- Tons of the code is runnable right there in the web page, including moving visual representations, highlighted code with current line of code highlighted.
- Some examples allow you to edit values and play with stuff.

**Michael #2:**  [**Embed Python in Unreal Engine 4**](https://github.com/20tab/UnrealEnginePython) 

- You may notice a theme throughout my set of picks on this episode
- Games built on Unreal Engine 4 include
	- [*Fortnite: Save the World*](https://en.wikipedia.org/wiki/Fortnite:_Save_the_World)
	- [*Gears of War 4*](https://en.wikipedia.org/wiki/Gears_of_War_4)
	- [*Marvel vs. Capcom: Infinite*](https://en.wikipedia.org/wiki/Marvel_vs._Capcom:_Infinite)
	- [*Moto Racer 4*](https://en.wikipedia.org/wiki/Moto_Racer_4)
	- [*System Shock (remake)*](https://en.wikipedia.org/wiki/System_Shock_(upcoming_video_game))
- Plugin embedding a whole Python VM in Unreal Engine 4 (both the editor and runtime).
- This means you can use the plugin to write other plugins, to automate tasks, to write unit tests and to implement gameplay elements.
- Here is an [example usage](https://github.com/20tab/UnrealEnginePython/blob/master/tutorials/YourFirstAutomatedPipeline.md). It’s a really nice overview and tutorial for the editor.
- For game elements, check out [this section](https://github.com/20tab/UnrealEnginePython/blob/master/tutorials/YourFirstAutomatedPipeline.md).

**Brian #3: Redirecting stdout with contextlib**

- When I want to test the stdout output of some code, that’s easy, I grab the [capsys fixture](https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function) from pytest.
- But what if you want to grab the stdout of a method NOT while testing?
- Enter `[contextlib.redirect_stdout(new_target)](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout)`
- so cool. And very easy to read.
- ex:
```
    f = io.StringIO()
    with redirect_stdout(f):
        help(pow)
    s = f.getvalue()
```
- also a version for `stderr`

**Michael #4:** [Panda3D](https://www.panda3d.org/)

- via Kolja Lubitz
- Panda3D is an open-source, completely free-to-use engine for realtime 3D games, visualizations, simulations, experiments
- Not just games, could be science as well!
- The full power of the graphics card is exposed through an easy-to-use API. Panda3D combines the speed of C++ with the ease of use of Python to give you a fast rate of development without sacrificing on performance.
- Features:
	- **Platform Portability**
	- **Flexible Asset Handling**: Panda3D includes command-line tools for processing and optimizing source assets, allowing you to automate and script your content production pipeline to fit your exact needs.
	- **Library Bindings**: Panda3D comes with out-of-the-box support for many popular third-party libraries, such as the Bullet physics engine, Assimp model loader, OpenAL
	- **Performance Profiling**: Panda3D includes pstats — an over-the-network profiling system designed to help you understand where every single millisecond of your frame time goes.

**Brian #5:** [**Why PyPI Doesn't Know Your Projects Dependencies**](https://dustingram.com/articles/2018/03/05/why-pypi-doesnt-know-dependencies/)

- Some questions you may have asked:
  > How can I produce a dependency graph for Python packages?
  > Why doesn’t PyPI show a project’s dependencies on it’s project page?
  > How can I get a project’s dependencies without downloading the package?
  > Can I search PyPI and filter out projects that have a certain dependency?
- If everything is in `requirements.txt`, you just might be able to, but…
- `setup.py` is dynamic. You gotta run it to see what’s needed.
- Dependencies might be environment specific. Windows vs Linux vs Mac, as an example.
- Nothing stopping someone from putting `random.choice()` for dependencies in a `setup.py` file. But that would be kinda evil. But could be done. (Listener homework?)
- The `wheel` format is way more predictable because it limits some of this freedom. `wheel`s don’t get run when they install, they really just get unpacked.
- More info on wheels: Kind of a tangent, but what why not:
  - From: [https://pythonwheels.com](https://pythonwheels.com)
  - “**Advantages of wheels**
		- Faster installation for pure Python and native C extension packages.
		- Avoids arbitrary code execution for installation. (Avoids setup.py)
		- Installation of a C extension does not require a compiler on Linux, Windows or macOS.
		- Allows better caching for testing and continuous integration.
		- Creates .pyc files as part of installation to ensure they match the Python interpreter used.
		- More consistent installs across platforms and machines.”

**Michael #6:  PyGame series**

-  via Matthew Ward
- [Learn how to program in Python by building a simple dice game](https://opensource.com/article/17/10/python-101)
- [Build a game framework with Python using the PyGame module](https://opensource.com/article/17/12/game-framework-python)
- [How to add a player to your Python game](https://opensource.com/article/17/12/game-python-add-a-player)
- [Using PyGame to move your game character around](https://opensource.com/article/17/12/game-python-moving-player)
- [What's a hero without a villain? How to add one to your Python game](https://opensource.com/article/18/5/pygame-enemy)
- [Put platforms in a Python game with PyGame](https://opensource.com/article/18/7/put-platforms-python-game?sc_cid=70160000001273HAAQ)
- Also: Shout out to [Mission Python book: Code a Space Adventure Game!](https://amzn.to/2My32JC)

Extras:

Joke (maybe, Brain feel free to pick another one):

- via [@realpython](https://twitter.com/realpython/status/1087874671763173377)
- Why do Pythons live on land? They are above C-level!
