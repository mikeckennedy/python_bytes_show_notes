# Python Bytes 108
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**pyjanitor**](https://pyjanitor.readthedocs.io/) **- for cleaning data**

- originally a port of an R package called janitor, now much more.
- “pyjanitor’s etymology has a two-fold relationship to “cleanliness”. Firstly, it’s about extending Pandas with convenient data cleaning routines. Secondly, it’s about providing a cleaner, method-chaining, verb-based API for common pandas routines.”
- functionality:
	- Cleaning columns name (multi-indexes are possible!)
	- Removing empty rows and columns
	- Identifying duplicate entries
	- Encoding columns as categorical
	- Splitting your data into features and targets (for machine learning)
	- Adding, removing, and renaming columns
	- Coalesce multiple columns into a single column
	- Convert excel date (serial format) into a Python datetime format
	- Expand a single column that has delimited, categorical values into dummy-encoded variables
- This `pandas` code:

```
    df = pd.DataFrame(...)  # create a pandas DataFrame somehow.
    del df['column1']  # delete a column from the dataframe.
    df = df.dropna(subset=['column2', 'column3'])  # drop rows that have empty values in column 2 and 3.
    df = df.rename({'column2': 'unicorns', 'column3': 'dragons'})  # rename column2 and column3
    df['newcolumn'] = ['iterable', 'of', 'items']  # add a new column.
- looks like this with pyjanitor:
    df = (
        pd.DataFrame(...)
        .remove_columns(['column1'])
        .dropna(subset=['column2', 'column3'])
        .rename_column('column2', 'unicorns')
        .rename_column('column3', 'dragons')
        .add_column('newcolumn', ['iterable', 'of', 'items'])
    )
```

**Michael #2:** [**What Does It Take To Be An Expert At Python?**](https://www.youtube.com/watch?v=7lmCu8wz8ro)

- Presentation at PyData 2017 by James Powell
- Covers Python Data Model (dunder methods)
- Covers uses of Metaclasses
- All done very smoothly as a series of demos
- Pretty long and in depth, 1.5+ hours

**Brian #3:** [**Awesome Python Applications**](https://github.com/mahmoud/awesome-python-applications)

- pypi is a great place to find great packages you can use as examples for the packages you write. Where do you go for application examples? Well, now you can go to [Awesome Python Applications](https://github.com/mahmoud/awesome-python-applications).
- categories of applications included:
    internet, audio, video, graphics, games, productivity, organization, communication, education, science, CMS, ERP (enterprise resource planning), static site generators, and a whole slew of developer related applications.
- Mahmoud is happy to have help filling this out, so if you know of a great open source application written in Python, go ahead and contribute to this, or open an issue on this project.

**Michael #4:** [**Django Core no more**](https://www.b-list.org/weblog/2018/nov/20/core/)

- Write up by [James Bennett](https://twitter.com/ubernostrum)
- If you’re not the sort of person who closely follows the internals of Django’s development, you might not know there’s [a draft proposal](https://github.com/django/deps/pull/47) to drastically change the project’s governance.
- What’s up: Django the open-source project is OK right now, but difficulty in recruiting and retaining enough active contributors.
- Some of the biggest open-source projects dodge this by having, effectively, corporate sponsorship of contributions.
- Django has become sort of a victim of its own success: the types of easy bugfixes and small features that often are the path to growing new committers have mostly been done already in Django.
- Not managed to bring in new committers at a sufficient rate to replace those who’ve become less active or even entirely inactive, and that’s not sustainable for much longer.
- Under-attracting women contributors too
- Governance:  Some parallels to what the Python core devs are experiencing now. Project leads BDFLs stepped down.
- The proposal: what I’ve proposed is the dissolution of “Django core”, and the revocation of almost all commit bits
	- Seems extreme but they were working much more as a team with PRs, etc anyway.
	- Breaks down the barrier to needing to be on the core team to suggest, change anything.
	- Two roles would be formalized — Mergers and Releasers — who would, respectively, merge pull requests into Django, and package/publish releases. But rather than being all-powerful decision-makers, these would be bureaucratic roles

**Brian #5:** [**wemake django template**](https://github.com/wemake-services/wemake-django-template)

- a cookie-cutter template for serious django projects with lots of fun goodies
- “This project is used to scaffold a `django` project structure. Just like `django-admin.py startproject` but better.”
- features:
	- Always `up-to-date` with the help of `[@dependabot](https://dependabot.com/)`
	- `poetry` for managing dependencies
	- `mypy` for optional static typing
	- `pytest` for unit testing
	- `flake8` and `wemake-python-styleguide` for linting
	- `pre-commit` hooks for consistent development
	- `docker` for development, testing, and production
	- `sphinx` for documentation
	- `Gitlab CI` with full `build`, `test`, and `deploy` pipeline configured by default
	- `Caddy` with `https` and `http/2` turned on by default

**Michael #6:**  [**Django Hunter**](https://github.com/6IX7ine/djangohunter)

- Tool designed to help identify incorrectly configured Django applications that are exposing sensitive information.
- Why? March 2018: 28,165 thousand django servers are exposed on the internet, many are showing secret API keys, database passwords, amazon AWS keys. 
- Example: https://twitter.com/6IX7ine/status/978598496658960384
- Some complained this inferred Django was insecure and said it wasn’t. Others thought “There is a reasonable argument to be made that DEBUG should default to False.”
- One beginner, Peter, chimes in:
	- I probably have one of them, among my early projects that are on heroku and public GitHub repos. 
	- I did accidentally expose my aws password this way and all hell broke loose.
	- The problem is that as a beginner, it wasn't obvious to me how to separate development and production settings and keep production stuff out of my public repository.

Extras:

Michael: Thanks for having me on your show Brian: [https://blog.michaelckennedy.net/2018/12/08/being-a-great-podcast-guest/](https://blog.michaelckennedy.net/2018/12/08/being-a-great-podcast-guest/)

Brian: open source extra:
For Christmas, I want a dragon…

> [pic.twitter.com/RmFAEgqpSr](https://t.co/RmFAEgqpSr)
> — Changelog (@changelog) 

Michael:  Why did the multithreaded chicken cross the road?

- road the side get to the other of to
- to get the side to road the of other
- the side of to the to road other get
- to of the road to side other the get


