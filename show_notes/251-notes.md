# Python Bytes 251

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **[Brett Cannon](https://twitter.com/brettsky)**

**Michael #1:** [**auto-optional**](https://auto-optional.daanluttik.nl/)

- by Daan Luttik
- Did you know that concrete types cannot be None in Python typing?
- This is wrong:
```
    def do_a_thing(extra_info: str = None): ...
```
- auto-optional will fix it:
```
    def do_a_thing(extra_info: Optional[str] = None): ...
```
- Why would you want this?
- Easily modify external libraries that didn't pay attention to proper use of optional to improve mypy linting.
- Force consistency in your own code-base: Enforcing that None parameter implies an Optional type.
- Run via the CLI: `auto-optional [path]`

**Brian #2:** [**Making World-Class Docs Takes Effort**](https://daniel.haxx.se/blog/2021/09/04/making-world-class-docs-takes-effort)

- Daniel Stenberg
- Six requirements for a project to get a gold star
	- docs in the code repo
	- NOT extracted from the code
	- examples, lots of examples, more than you think you need
	- document every API call you provide
	- easily accessible and browsable
    - and hopefully offline readable as well
	- easy to contribute to
- Non-stop iterating is key to having good docs.
- extra goodness
	- consistency for section titles
	- cross-references
- I’d add
	- Check for grammar and spelling mistakes
	- Consistency in all things, formatting, style, tone, depth of info of diff topics
	- Don’t be afraid to have a personality. docs that include easter eggs, fun examples, tasteful jokes, etc are nice, as long as that fun stuff doesn’t complicate the docs.
	- Don’t slam projects for having bad docs. Not all open source projects exist for your benefit. 
		- You can make them better by contributing. :)


**Brett #3:** [**Starship**](https://starship.rs/)

- Continuing the trend of stuff to help make your coding better, Python or not. 😉
- Also to make Michael’s new love of nerd fonts more useful. 😁
- And more Rust on this show as Paul Everitt says I must do. 😉
- Gives you a common shell prompt no matter which shell you use; I also find it easy to set up compared to most shells for their prompts
- Lots of integrated support for various developer things such as printing what Python version you have when the directory has a `pyproject.toml` file.
- Works nicely with the Python Launcher (as I mentioned the last time I was on).
- Has some pyenv support that I don’t use. 😁


**Michael #4:** [**JMESPath**](https://pypi.org/project/jmespath/)

-  via Josh Thurston
- Spent tons of time figuring out how to parse the pretty print results that had layers of nested dictionaries and lists. This module saved me time in a big way.
- JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document.
- For example, given this document:
```
    {"foo": {"bar": "baz"}}
```
- The jmespath expression `foo.bar` will return “baz”.
- Even works with a projection-like result:
```
    {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
```
- The expression: `foo.bar[*].name` will return `["one", "two"]`. 
- Negative indexing is also supported (-1 refers to the last element in the list). 
- Given the data above, the expression `foo.bar[-1].name` will return `"two"`.

**Brian #5:**  [**pedalboard**](https://github.com/spotify/pedalboard) - audio effects library

- from Spotify
- The “power, speed, and sound quality of a DAW”, but in Python.
- [Introduction Article](https://engineering.atspotify.com/2021/09/07/introducing-pedalboard-spotifys-audio-effects-library-for-python) (warning: weird color changing header image that is painful to look at, so scroll past that quickly)
	- Built-in support for a number of basic audio transformations:
    - `Convolution`, `Compressor`, `Chorus`, `Distortion`
    - `Gain`, `HighpassFilter`, `LadderFilter`, `Limiter`, `LowpassFilter`
    - `Phaser`, `Reverb`


**Brett #6:** [**PEP 665**](https://www.python.org/dev/peps/pep-0665/) **(and the** [**journey so far**](https://discuss.python.org/t/pep-665-specifying-installation-requirements-for-python-projects/9911/152)**)**

- Attempt to standardize lock files for Python.
- Spent six months talking w/ folks privately to come up with the first public draft.
- Initially a strict lock file, but Poetry and PDM feedback was platform-agnostic was important.
- Proposal morphed to cover that.
- Took it public and led to over 150 comments on Discourse.
- People disliked it: from the title to the explanation to the proposed problem space to the actual solution.
- Gone back to the drawing board privately w/ one of the original objectors participating; looking like we are reaching a good consensus on how to frame things and how it should ultimately look.
- (Packaging) PEPs are hard.


**Extras**

Brian

- Python is popular, apparently, and [“on the verge of another big step forward”](https://www.zdnet.com/article/programming-languages-python-is-on-the-verge-of-another-big-step-forward/) (another good place for dun, dun, duuunnn, ?)
	- "It only needs to bridge 0.16% to surpass C. This might happen any time now. If Python becomes number 1, a new milestone has been reached in the TIOBE index. Only 2 other languages have ever been leading the pack so far, i.e. C and Java."

Michael

- [**Nerd Fonts**](https://www.nerdfonts.com/)
- [**Evrone interview with me**](https://evrone.com/michael-kennedy-interview)
- [**Henry Schreiner’s Fish setup**](https://twitter.com/HenrySchreiner3/status/1438227200466202625)
- [**Aliases rather than CLI/venvs**](https://linuxize.com/post/how-to-create-bash-aliases/)

Brett

- [Will McGugan did a webinar w/ Paul Everitt](https://www.youtube.com/watch?v=1kTWxamIJ_k) about Textual (because it’s not a Python Bytes episode if Will’s name is not brought up).
- Python Launcher officially launched! (Last covered [30 episodes ago](https://pythonbytes.fm/episodes/show/221/pattern-matching-and-accepting-change-in-python-with-brett-cannon).)
	- Available in AUR, Fedora, and Homeberw (both macOS and Linux).
	- No reported bugs since launch!
- Still doing my [syntactic sugar blog posts](https://snarky.ca/tag/syntactic-sugar/).
- The Python extension for VS Code has a [refreshed testing UX](https://code.visualstudio.com/docs/python/testing); we’re coming for you, Brian. 😉

**Joke:** [**Last 5%**](https://geek-and-poke.com/geekandpoke/2021/2/2/the-last-5)
