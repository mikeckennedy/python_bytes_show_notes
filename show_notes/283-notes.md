# Python Bytes 283

Sponsored: [**RedHat: Compiler Podcast**](https://pythonbytes.fm/compiler)

Special guest: [**Tonya Sims**](https://twitter.com/TonyaSims)

**Michael #1:** [**Pathy: a Path interface for local and cloud bucket storage**](https://github.com/justindujardin/pathy)

- via Spencer
- Pathy is a python package (*with type annotations*) for working with Cloud Bucket storage providers using a pathlib interface.
-  It provides an easy-to-use API bundled with a CLI app for basic file operations between local files and remote buckets. 
- It enables a smooth developer experience by letting developers work against the local file system during development and only switch over to live APIs for deployment.
- Also has optional local file caching.
- From Spenser
- *The really cool function is "Pathy.fluid" which can take any type of local, GCS, or S3 path string and then just give you back a Path object that you can interact with agnostic of what platform it was. So this has worked amazingly for me in local testing since i can just change the file path from the "s3://bucket/path" that i use in prod to a local "test_dir/path" and it works automatically.* 

**Brian #2:** [**Robyn**](https://robyn.sanskar.wtf/)

- “Robyn is a fast, high-performance Python web framework with a Rust runtime.”
- [Hello, Robyn!](https://www.sanskar.me/hello_robyn.html) - intro article
- [docs](https://sansyrox.github.io/robyn/#/), [repo](https://github.com/sansyrox/robyn)
- Neat things
    - doesn’t need WSGI or ASGI
    - async
    - very Flask-like
- Early, so still needs some TLC
    - docs, etc. getting started and demo apps would be good.


**Tonya** **#3:** [**Python package 'nba_api' is a package to access data for NBA.com**](https://pypi.org/project/nba-api/)

- This package is maintained by [Swar Patel](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md) 
- API Client package for NBA.com, more accessible endpoints, and better documentation 
- The NBA.com API's are not well documented and change frequently (player traded, injured, retired, points per game, stats, etc)
- The nba_api package has tons of features:
- The nba_api starts with static data on players and teams (Full name, team name, etc). Each player and Team has an id.
- Can get game data from the playergamelog API endpoint
- The package also has many different [API endpoints](https://github.com/swar/nba_api/tree/master/nba_api/stats/endpoints) that it can hit by passing in features from the static data to the API endpoints as parameters

**Michael #4:** [**Termshot**](https://github.com/homeport/termshot)

- From Jay Miller
- Creates screenshots based on terminal command output
- Just run `termshot YOUR_CMD`
- or `termshot --show-cmd -- python program.py` 
- Even `termshot /bin/zsh` for full interactive “recording”
- Example I made:
![](https://paper-attachments.dropbox.com/s_C2B8122915964D64A517E66102153405FC6014DDA3BE13B4DEF4E14329EEDC75_1652122396663_termshot-example.png)


**Brian #5:** [**When Python can’t thread: a deep-dive into the GIL’s impact**](https://pythonspeed.com/articles/python-gil/)

- Itamar Turner-Trauring
- Building a mental model of the GIL using profiler graphs of simple two thread applications.
- The graphs really help a lot to see when the CPU is active or waiting on each thread.

**Tonya** **#6:** [**Sportsipy: A free sports API written for python**](https://sportsreference.readthedocs.io/en/stable/#sportsipy-a-free-sports-api-written-for-python)

-  [Free python API](https://pypi.org/project/sportsipy/) that pulls the stats from www.sports-reference.com 
-  sports-reference.com - great website for getting sports stats for professional sports(NBA, NFL, NHL, MLB, college sports)
- Looks like an HTML website for the 90s - great for scraping (email site owners)
- You can get API queries for every sport (North American sports) like the list of teams for that sport, the date and time of a game, the total number of wins for a team during the season, and many more team-related metrics.
- You can also get stats from players and box scores - so you can build cool stuff around how a team performed during a game or during a season.

**Extras** 

Michael:

- [**Python 3.11.0 beta 1 is out**](https://twitter.com/pyblogsal/status/1523635910696652800)
    - [Test with GitHub Actions against Python 3.11](https://til.simonwillison.net/github-actions/python-3-11)

**Joke:** 
[**Finding my family**](https://twitter.com/PR0GRAMMERHUM0R/status/1523528212374069249)

