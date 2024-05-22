# Python Bytes 277

Sponsored by: [**Microsoft for Startups Founders Hub**](https://pythonbytes.fm/foundershub).

Special guest: Thomas Gaigher, creator/maintainer [pypyr taskrunner](https://github.com/pypyr/pypyr)

**Michael #1:** [**March Package Madness**](https://twitter.com/_ChrisMay/status/1506761070064680971)

- via Chris May
- Start with 16 packages
- They battle it out 2-on-2 in elimination rounds
- Voting is once a week
- So go vote!

**Brian #2:**  [**nbpreview**](https://nbpreview.readthedocs.io/en/latest/)

- “A terminal viewer for Jupyter notebooks. It’s like cat for ipynb files.”
- Some cool features
    - pretty colors by default
        - piping strips formatting, so you can pass it to grep or other post processing
        - automatic paging
    - syntax highlighting
        - line numbers and wrapping work nicely
    - markdown rendering
    - images converted to block, character, or dots (braille)
    - dataframe rendering
    - clickable links

Thomas **#3:** **pyfakefs**

- A fake file system!
- It intercepts all calls that involve the filesystem in Python - e.g `open()`, `shutil`, or `pathlib.Path`.
- This is completely transparent - your functional code does not know or need to know that under the hood it's been disconnected from the actual filesystem.
- The nice thing about this is that you don't have to go patching `open` using `mock_open` - which works fine, but gets annoying quickly for more complex test scenarios.
    - E.g Doing a mkdir -p before a file write to ensure parent dirs exist.
- What it looks like without a fake filesystem:

```
    in_bytes = b"""[table]
    foo = "bar"  # String
    """
    
    # read
    with patch('pypyr.toml.open',
               mock_open(read_data=in_bytes)) as mocked_open:
        payload = toml.read_file('arb/path.in')
    
    # write
    with io.BytesIO() as out_bytes:
        with patch('pypyr.toml.open', mock_open()) as mock_output:
            mock_output.return_value.write.side_effect = out_bytes.write
            toml.write_file('arb/out.toml', payload)
        
        out_str = out_bytes.getvalue().decode()
    
    mock_output.assert_called_once_with('arb/out.toml', 'wb')
    
    assert out_str == """[table]
    foo = "bar"
    """
```

- If you've ever tried to patch/mock out `pathlib`, you'll know the pain!
- Also, no more annoying test clean-up routines or `tempfile` - as soon as the fake filesystem goes out of scope, it's gone, no clean-up required.
- Not a flash in the pan - long history: originally developed by Mike Bland at Google back in 2006. Open sourced in 2011 on Google Code. Moved to Github and nowadays maintained by  [John McGehee](https://github.com/jmcgeheeiv).
- This has been especially useful for [pypyr](https://pypyr.io), because as a task-runner or automation tool pypyr deals with wrangling config files on disk a LOT (reading, generating, editing, token replacing, globs, different encodings), so this makes testing so much easier.
    - Especially to keep on hitting the 100% test coverage bar!
- Works great with [pytest](https://docs.pytest.org/) with the provided `fs` fixture.
    - Just add the `fs` fixture to a test, and all code under test will use the fake filesystem.
- Dynamically switch between Linux, MacOs & Windows filesystems.
- Set up paths/files in your fake filesystem as part of test setup with some neat helper functions.
- Very responsive maintainers - I had a PR merged in less than half a day. Shoutout to [mrbean-bremen](https://github.com/mrbean-bremen).
- Docs here: [http://jmcgeheeiv.github.io/pyfakefs/release/](http://jmcgeheeiv.github.io/pyfakefs/release/)
- Github here: [https://github.com/jmcgeheeiv/pyfakefs](https://github.com/jmcgeheeiv/pyfakefs)
- Real world example:

```
    @patch('pypyr.config.config.default_encoding', new='utf-16')
    def test_json_pass_with_encoding(fs):
        """Relative path to json should succeed with encoding."""
        # arrange
        in_path = './tests/testfiles/test.json'
        fs.create_file(in_path, contents="""{
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    """, encoding='utf-16')
    
        # act
        context = pypyr.parser.jsonfile.get_parsed_context([in_path])
        
        # assert
        assert context == {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
    
    def test_json_parse_not_mapping_at_root(fs):
        """Not mapping at root level raises."""
        # arrange
        in_path = './tests/testfiles/singleliteral.json'
        fs.create_file(in_path, contents='123')
        
        # act
        with pytest.raises(TypeError) as err_info:
            pypyr.parser.jsonfile.get_parsed_context([in_path])
    
        # assert
        assert str(err_info.value) == (
            "json input should describe an object at the top "
            "level. You should have something like\n"
            "{\n\"key1\":\"value1\",\n\"key2\":\"value2\"\n}\n"
            "at the json top-level, not an [array] or literal.")

```


**Michael #4:** [strenum](https://github.com/irgeek/StrEnum)

- A Python Enum that inherits from str.
- To complement enum.IntEnum in the standard library. Supports python 3.6+.
- Example usage:

```
    class HttpMethod(StrEnum):
        GET = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
    
    assert HttpMethod.GET == "GET"
```

Use wherever you can use strings, basically:

```
    ## You can use StrEnum values just like strings:
    
    import urllib.request
    
    req = urllib.request.Request('https://www.python.org/', method=HttpMethod.HEAD)
    with urllib.request.urlopen(req) as response:
       html = response.read()
```

Can auto-translate casing with `LowercaseStrEnum` and `UppercaseStrEnum`.

**Brian #5:** [Code Review Guidelines for Data Science Teams](https://tdhopper.com/blog/code-review-guidelines)

- Tim Hopper
- Great guidelines for any team
- What is code review for?
    - correctness, familiarity, design feedback, mutual learning, regression protection
    - NOT opportunities for
        - reviewer to impose their idiosyncrasies
        - dev to push correctness responsibility to reviewers
        - demands for perfection
- Opening a PR
    - informative commit messages
    - consider change in context of project
    - keep them short
    - write a description that helps reviewer
    - include tests with new code
- Reviewing
    - Wait for CI before starting
        - I would also add “wait at least 10 min or so, requester might be adding comments”
    - Stay positive, constructive, helpful
    - Clarify when a comment is minor or not essential for merging, preface with “nit:” for example
    - If a PR is too large, ask for it to be broken into smaller ones
    - What to look for
        - does it look like it works
        - is new code in the right place
        - unnecessary complexity
        - tests

Thomas **#6:** **Shell Power is so over. Leave the turtles in the late 80ies.**

- Partly inspired by/continuation of last week’s episode’s mention of running subprocesses from Python.
- Article by [**Itamar Turner-Trauring**](https://twitter.com/itamarst)
    - Please Stop Writing Shell Scripts [https://pythonspeed.com/articles/shell-scripts/](https://pythonspeed.com/articles/shell-scripts/)
- Aims mostly at bash, but I'll happily include bourne, zsh etc. under the same dictum
- If nothing else, solid listing of common pitfalls/gotchas with bash and their remedies, which is educational enough in and of itself already.
    - TLDR; Error handling in shell is hard, but also surprising if you're not particularly steeped in the ways of the shell.
    - Error resumes next, unset vars don't raise errors, piping & sub shells errs thrown away
- If you really-eally HAVE to shell, you prob want this boilerplate on top (aka [unofficial bash strict mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/):

```
#!/bin/bash
    set -euo pipefail
    IFS=$'\n\t'
```

- This will,
    - -e: fail immediately on error
    - -u: fail on Unset vars
    - -o pipefail: raise immediately when piping
    - IFS: set Internal Field Separator to `newline | tab`, rather than `space | newline | tab`. 
        - Prevents surprises when iterating over strings with spaces in them
- Itamar lists common counter-arguments from shell script die-hards:
    - It's always there!
        - But so is the runtime of whatever you're actually coding in, and in the case of a build CI server. . .almost by definition.
    - Git gud! (I'm paraphrasing)
    - Shell-check (linting for bash, basically)
- The article is short & sweet - mercifully so in these days of padded content.
- The rest is going to be me musing out loud, so don't blame the OG author.  So expanding on this, I think there're a couple of things going on here:
- If anything, the author is going a bit soft on your average shell script. If you’re just calling a couple of commands in a row, okay, fine. But the moment you start worrying about retrying on failure, parsing some values into or out of some json, conditional branching - which, if you are writing any sort of automation script that interacts with other systems, you WILL be doing - shell scripts are an unproductive malarial nightmare. 
    - Much the same point applies to Makefile. It’s an *amazing* tool, but it’s also misused for things it was never really meant to do. You end up with Makefiles that call shell scripts that call Makefiles. . .
- Given that coding involves automating stuff, amazingly often the actual automation of the development process itself is deprioritized & unbudgeted.
- Sort of like the shoemaker's kid not having shoes.
    - Partly because when management has to choose between shiny new features and automation, shiny new features win every time.
    - Partly because techies will just "quickly" do a thing in shell to solve the immediate problem… Which then becomes part of the firmament like a dead dinosaur that fossilises and more and more inscrutable layers accrete on top of the original "simple" script.
    - Partly because coders would rather get on with clever but marginal micro-optimisations and arguing over important stuff like spaces vs tabs, rather than do the drudge work of automating the development/deployment workflow.
- There's the glimmering of a point in there somewhere: when you have to choose between shiny new features & more backoffice automation, shiny new features probably win.
    - Your competitiveness in the marketplace might well depend on this.
    - BUT,  we shouldn’t allow the false idea that shell scripts are "quicker" or "lighter touch" to sneak in there alongside the brutal commercial reality of trade-offs on available budget & time.
    - If you have to automate quickly, it's more sensible to use a task-runner or just your actual programming language. If you're in python already, you're in luck, python's GREAT for this.
- Don’t confuse excellent cli programs like `git` , `curl` , `awscli`, `sed` or `awk` with a shell script. These are executables, you don’t need the shell to invoke these.
- Aside from these empirical factors, a couple of psychological factors also.
    - Dealing with hairy shell scripts is almost a Technocratic rite of passage - coupled with imposter syndrome, it's easy to be intimidated by the Shell Bros who're steeped in the arcana of bash.
    - It's the tech equivalent of "back in my day, we didn't even have <<>>", as if this is a justification for things being more difficult than they need to be ever thereafter.
    - This isn't Elden Ring, the extra difficulty doesn't make it more *fun*. You're trying to get business critical work done, reliably & quickly, so you can get on with those new shiny features that actually pay the bills.

**Extras** 


Michael:

- A changing of the guard
    - Firefox → [Vivaldi](https://vivaldi.com) 
        - (here’s [a little more info](https://arstechnica.com/information-technology/2020/08/firefox-maker-mozilla-lays-off-250-workers-says-covid-19-lowered-revenue/) on the state of Firefox/Mozilla financially) 
        - ([threat team](https://arstechnica.com/information-technology/2020/08/firefox-maker-mozilla-lays-off-250-workers-says-covid-19-lowered-revenue/?comments=1&post=39142373) is particularly troubling)
    - Google email/drive/etc → [Zoho](http://Zoho.com)
    - @gmail.com to @customdomain.com 
    - Google search → [DuckDuckGo](https://duckduckgo.com)
    - BTW Calendar apps/integrations and email clients are trouble

**Joke:** [A missed opportunity - and cybersecurity](https://twitter.com/PR0GRAMMERHUM0R/status/1505106836608933892)
