# Python Bytes 204

Sponsored by Techmeme Ride Home podcast: [**pythonbytes.fm/ride**](http://pythonbytes.fm/ride)

Special guests
- [Carlton Gibson](https://twitter.com/carltongibson)
- [William Vincent](https://twitter.com/wsv3000)

**Brian #1:** [**nbQA : Quality Assurance for Jupyter Notebooks**](https://github.com/nbQA-dev/nbQA)

- Sent in by listener and Patreon supporter (woohoo!!!) Marco Gorelli.
- We’ve now talked about running black on Jupyter notebooks in the past (at least 2) shows?
- Marco’s recommendation is nbQA
- nbQA lets you run all this on notebooks:
	- black
	- isort
	- mypy
	- flake8
	- pylint
	- pyupgrade to upgrade syntax 
	- doctest to check examples 
- Run as a pre-commit hook
- Configure in pyproject.toml
- Also (from Marco) better than standalone black due to:
	- can run on a directory, not just one file at a time
	- keeps diffs minimal and easier to read then black
	- preserves trailing semicolons, as they are used to suppress output in notebooks
	- supports most standard magic commands
- And the nbQA project is tested with …. drum roll …. pytest (of course)

**Michael #2:** [**The PSF yearly survey is out, go take it now!**](https://surveys.jetbrains.com/s3/c6-python-developers-survey-2020)

- This is the fourth iteration of the official Python Developers Survey.
- The results of this survey serve as a major source of knowledge about the current state of the Python community
- Takes about 10 minutes
- They will randomly choose **100 winners** (from those who complete the survey in its entirety), who will each receive an amazing **Python Surprise Gift Pack**.
- Analysis is really well done, see the [2019 results](https://www.jetbrains.com/lp/python-developers-survey-2019/).

Will #3: **From Prototype to Production in Django**

- Django defaults to local/prototype settings initially when run `startproject` command. 
-  `settings.py` file contains global configs for a project. What needs to change for production?
	- `DEBUG` set to `False`
	- `SECRET_KEY` actually secret and not in source control
	- `ALLOWED_HOSTS`
	- Database probably not SQLite 
	- Configure static/media files
	- Change admin path away from `/admin`
	- User registration, typically use [django-allauth](https://github.com/pennersr/django-allauth)
- Environment variables preferred method to have local/production settings. [environs](https://github.com/sloria/environs) is Will’s favorite 3rd party package but multiple others.
- Use [Django deployment checklist](https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/) aka `python check` `--``deploy`, add HTTPS all over basically
- [DJ Checkup website](https://djcheckup.com/pony/)
- What else? Testing, logging, performance, security, etc etc etc
- [Django for Professionals](https://learndjango.com/books/) book covers all of this and more including Docker

Carlton #4: **Deployment: Getting your app online**

- Deployment (and how hard it it) seem to come up almost every week on Django Chat. 
- I think a lot about *The Deployment Gap* that exists: a new user finishes the Django tutorial, or the DRF tutorial or Will’s [Django for Beginners book](https://djangoforbeginners.com/), and they’re still **a long way** from being able to deploy. 
- PaaS look like a good option. (Heroku/App Service/DO’s new one, and so on) but they’re a bit of a cul-de-sac (do you use that in America?) — you drive in, get to the end and then have to drive out again.
- On the other hand, DIY all looks far-too-scary™: there’s provisioning servers, *private clouds*, firewalls, permissions, block stores, objects stores, … — Argh! (On top of all the usual DNS, and all the rest of it.) 
	- **Plus** there’s a tendency I think towards fashion: you’d think you can’t possibly deploy without adopting a micro-service architecture, or a container orchestration platform. **It’s too much**.
	- This is same as, *You couldn’t possibly use Django, Postgres… — you have to use the New Hotness™*. 
- I think there’s a simpler story: start with a VM, a relational database, a simple network setup, and grow from there. There’s still moving parts, but it’s not **that** complex.
- I’m working on a tool for all this, **Button**. It’s coming in 2021. It’s a simpler deployment story. It’s part tool, part guide. It get’s you through the *Argh! It’s too scary bit.* 
- You can sign up for early updates at https://btn.dev 
    

**Brian #5:** [**All Contributors**](https://allcontributors.org/docs/en/overview)
“This is a specification for recognizing contributors to an open source project in a way that rewards each and every contribution, not just code.
The basic idea is this:

> Use the project README (or another prominent public documentation page in the project) to recognize the contributions of members of the project community.

People are giving themselves and their free time to contribute to open source projects in so many ways, so we believe everyone should be praised for their contributions (code or not).”

- used by nbQA
- It is a specification for how to be consistent in listing contributors.
- Also includes an [Emoji Key](https://allcontributors.org/docs/en/emoji-key), to be used with contributors name (and optionally avatar) to denote the kind of contribution they’ve made:
	- 💻 `code`
	- 📖 `doc`
	- 🎨 `design`
	- 💡 `example`
	- 🚧 `maintenance`
	- 🔌 `plugin`
	- and many, many more
- And a [GitHub bot](https://allcontributors.org/docs/en/bot/overview) to automate acknowledging contributors to your open source projects.
	- Uses natural language parsing to add people as contributors and add the appropriate emoji
- Also includes a cli for adding contributors, comparing GitHub contributors to your listed contributors, and more.

**Michael #6:** [**MovingPandas**](https://anitagraser.github.io/movingpandas/)

- A Python library for handling movement data based on Pandas and GeoPandas
- It provides trajectory data structures and functions for analysis and visualization.
- MovingPandas development started as a QGIS plugin idea in 2018. But made more sense as its own library
- Features
	- Convert GeoPandas GeoDataFrames of time-stamped points into MovingPandas Trajectories and TrajectoryCollections
	- Add trajectory properties, such as movement speed and direction
	- Split continuous observations into individual trips
	- Generalize Trajectories
	- Aggregate TrajectoryCollections into flow maps
	- Create static and interactive visualizations for data exploration
- MovingPandas makes it straightforward to compute movement characteristics, such as trajectory length and duration, as well as movement speed and direction.
- Example
```
    df = pd.DataFrame([
      {'geometry':Point(0,0), 't':datetime(2018,1,1,12,0,0)},
      {'geometry':Point(6,0), 't':datetime(2018,1,1,12,6,0)},
      {'geometry':Point(6,6), 't':datetime(2018,1,1,12,10,0)},
      {'geometry':Point(9,9), 't':datetime(2018,1,1,12,15,0)}
    ]).set_index('t')
    gdf = gpd.GeoDataFrame(df, crs=CRS(31256))
    traj = mpd.Trajectory(gdf, 1)
```

**Extras**

**Carlton:**

- Listen to [Django Chat](https://djangochat.com/)
- Check out [Will’s Tutorials and Books](https://learndjango.com/)
- Sign up for early updates on [Button](https://btn.dev)

**Michael:**

- Transcripts are back!
- Trying to live in [DuckDuckGo land](https://duckduckgo.com/). Crazy or smart? :)
- And remember to do your periodic [Google Takeout](https://takeout.google.com/)
- Deployed my first [Fast API web API & site](https://weather.talkpython.fm)

**Joke:**

“Give a person a program, frustrate them for a day. Teach them to program, frustrate them for a lifetime. 🙂” *(…unless you teach them to test at the same time. - Brian)*

The failed interview: “Sorry, we’re looking for someone aged 22-26… with 30 years of experience with Flask”
