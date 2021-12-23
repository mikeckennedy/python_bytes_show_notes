# Python Bytes 262

Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: [**Leah Cole**](https://twitter.com/leahecole)

**Brian #1:** [**pytest 7.0.0rc1**](https://docs.pytest.org/en/7.0.x/announce/release-7.0.0rc1.html)

- Question: Does [the new pytest book](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/) work with pytest 7?
    - Answer: Yes! I’ve been working with pytest 7 during final review of all code, and many pytest core developers have been technical reviewers of the book.
    - A few changes in pytest 7 are also the result of me writing the 2nd edition and suggesting (and in one case implementing) improvements. 
- [Florian Bruhin’s announcement on Twitter](https://twitter.com/the_compiler/status/1468144014889209858?s=20)
    - “I'm happy to announce that I just released [#pytest](https://twitter.com/hashtag/pytest?src=hashtag_click) 7.0.0rc1! After many tricky deprecations, some internal changes, and months of delay due to various issues, it looks like we could finally get a new non-bugfix release this year! (6.2.0 was released in December 2020).”
    - “We invite everyone to test the #pytest prerelease and report any issues - there is *a lot* that happened, and chances are we broke something we didn't find yet (we broke a lot of stuff we already fixed Smiling face with open mouth and cold sweat). See the release announcement for details: https://docs.pytest.org/en/7.0.x/announce/release-7.0.0rc1.html”
- Try it out with `pip install pytest==7.0.0rc1`
- For those of you following along at home (we covered `pip index` briefly in [episode 259](https://pythonbytes.fm/episodes/show/259))
    - to see rc releases with `pip index versions`, add `--pre`
    - ex: `pip index versions` `--``pre pytest` will include `Available versions: 7.0.0rc1, 6.2.5, 6.2.4,`  and let you know if there’s a newer rc available.
- Highlights from the [7.0.0rc1 changelog](https://docs.pytest.org/en/7.0.x/changelog.html)
    - `pytest.approx()` now works on `Decimal` within mappings/dicts and sequences/lists.
    - Improvements to `approx()` with sequences of numbers. Example:
```
    >       assert [1, 2, 3, 4] == pytest.approx([1, 3, 3, 5])
    E       assert comparison failed for 2 values:
    E         Index | Obtained | Expected
    E         1     | 2        | 3 +- 3.0e-06
    E         3     | 4        | 5 +- 5.0e-06
```

- pytest invocations with `--fixtures-per-test` and `--fixtures` have been enriched with:
    - Fixture location path printed with the fixture name.
    - First section of the fixture’s docstring printed under the fixture name.
    - Whole of fixture’s docstring printed under the fixture name using `--verbose` option.
    - *Never again wonder where a fixture’s definition is*
- `RunResult` method `assert_outcomes` now accepts a `warnings` and `deselected` argument to assert the total number of warnings captured. *Helpful for plugin testing.*
- Added `pythonpath` setting that adds listed paths to `sys.path` for the duration of the test session. *Nice for using pytest for applications, and for including test helper libraries.*
- Improved documentation, including 
    - an [auto-generated list of plugins](https://docs.pytest.org/en/7.0.x/reference/plugin_list.html#plugin-list). There were 963 this morning.


**Michael #2:** [**PandasTutor**](https://twitter.com/davidouglasmit/status/1467522704542683139)

- via ****[**David Smit**](https://twitter.com/davidouglasmit)
- **Why use this tool?** Let's say you're trying to explain what this `pandas` code does:

```
    (dogs[dogs['size'] == 'medium']
     .sort_values('type')
     .groupby('type').median()
    )
```

- But this doesn't tell you what's going on behind the scenes.
- **What did this code just do?** This single code expression has 4 steps (filtering, sorting, grouping, and aggregating), but only the final output is shown.
- **Where were the medium-sized dogs?** This code filters for dogs with size `"medium"`, but none of those dogs appear in the original table display (on the left) because they were buried in the middle rows.
- **How were the rows grouped?** The output doesn't show which rows were grouped and aggregated together. (Note that printing a `pandas.GroupBy` object won't display this information either.)
- If you [**ran this same code**](https://pandastutor.com/vis.html#trace=example-code/py_dogs.json) in Pandas Tutor, you can teach students exactly what's going on step-by-step


**Leah #3: Apache Airflow**

- Workflow orchestration tool the originated at Airbnb and is now part of the Apache Software Foundation
- author workflows as directed acyclic graphs (DAGs) of tasks
-  Airflow works best with workflows that are mostly static and slowly changing. When DAG structure is similar from one run to the next, it allows for clarity around unit of work and continuity.
- Typical data analytics workflow is the Extract, Transform, Load (ETL) workflow - I have data somewhere that I need to get (extract), I do something to it (Transform) and I put that result somewhere else (load)
- Airflow has "Operators" and connectors which enable you to perform common tasks in popular libraries and Cloud providers
- Let's talk about a sample - I work on GCP so my sample will be GCP based because that's what I use most. One common workflow I see is running Spark jobs in ephemeral Dataproc clusters. I'm actually writing a tutorial demonstrating this now - literally in progress in another tab
    - BigQuery -> Create Dataproc cluster -> Run PySpark Dataproc job -> Store results in GCS -> delete Dataproc cluster
- Airflow has a really wonderful, active community. Please join us. 


**Brian #4:** [**textwrap.dedent**](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)

- [Suggested by Michel Rogers-Vallée](https://twitter.com/mrvkino/status/1468306098235006981?s=20)
- Small utility but super useful. Also, built in to Python standard library.
- BTW, `textwrap` package has other cool tools you probably didn’t know Python could do right out of the box. It’s worth [reading the docs](https://docs.python.org/3/library/textwrap.html).
- `dedent` akes a multiline string (the ones with tripple quotes).
- Removes all common whitespace.
- This allows you to have multi-line strings defined in functions without mucking up your indenting.
- Example from docs:

```
    def test():
        # end first line with \ to avoid the empty line!
        s = '''\
        hello
          world
        '''
        print(repr(s))          # prints '    hello\n      world\n    '
        print(repr(dedent(s)))  # prints 'hello\n  world\n'
```

Better example:

```
    from textwrap import dedent
    
    def multiline_hello_world():
        print("hello")
        print("  world")
    
    def test_multiline_hello_world(capsys):
        expected = dedent('''\
        hello
          world
        ''')
        multiline_hello_world()
        actual = capsys.readouterr().out
        assert actual == expected
```

**Michael #5:** [**pip-audit**](https://github.com/trailofbits/pip-audit)

- via Dan Bader (from Real Python)
- Audits Python environments and dependency trees for known vulnerabilities
- Are your dependencies containing security issues?
- What about their dependencies, the ones you forgot to list in your requirements files or pin? 
- Just run pip-audit on your requirements file(s)
- Perfect candidate for pipx


**Leah #6 - Using bots to manage samples**

- Another part of my job is working with other software engineers in GCP to oversee the maintenance our Python samples
- We have thousands of samples in hundreds of repos that are part of GCP documentation
- To ensure consistency and that this wonderful group of Devrel Engineers has time to get their work done and also function as a human, we use a lot of automation
- Bots do things like keep our dependencies up to date, check for license headers, auto-assign PRs and issues to code-owners, sync repositories with a centralized config, and more
- the GCP DevRel github automation team has an [open source repo](https://github.com/googleapis/repo-automation-bots) with some of the bots they have developed that we use every day and we use [whitesource renovatebot to manage our dependencies](https://github.com/renovatebot/renovate) and keep them up to date

**Extras**


Michael:

- Github CMD/CTRL+K command palette
- Python 3.10.1 [**is out**](https://www.python.org/downloads/release/python-3101/)

**Joke:**

- [**HTTP status code meanings**](https://twitter.com/mkennedy/status/1466849030047035392)
- [**http.cat**](https://http.cat/)

