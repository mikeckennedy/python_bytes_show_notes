# Python Bytes 383

Sponsored by Mailtrap: [**pythonbytes.fm/mailtrap**](https://pythonbytes.fm/mailtrap)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 10am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Michael #1:** [**I asked 100 devs why they aren’t shipping faster. Here’s what I learned**](https://greptile.com/blog/100-devs)

- by Daksh Gupta (via PyCoders)
- What’s stopping you from shipping faster?
  - Dependency bugs 
  - Complicated codebase
    - \>*There is so much undocumented in our service, including poor records of new features, nonexistent or outdated info on our dependencies, or even essential things like best practices for testing, a lot of time is wasted in syncs trying to find the right information*
- QA Loops
- Waiting for spec
  - *> At Amazon? Meetings, approval, talking to 10 different stakeholders because changing the color of a button affects 15 micro services*
- Writing tests
- Deployment/build speed
- Scope creep
  - \> *The human tendency to stuff last-minute items into the crevices of their luggage minutes before leaving for the airport manifests itself at software companies as scope creep.*
- Unclear requirements
- Excessive meetings
- Motivation
  - *>honest answer is i was on ads*
  - *>and that’s a very old / complicated / large stack* *(edited)*
  - *>and i didn’t understand it*
  - *>my friends on younger teams seemed happier, i was miserable*
- [DORA metrics](https://docs.gitlab.com/ee/user/analytics/dora_metrics.html)

**Brian #2:** [**Python 3.13.0 beta 1 released**](https://pythoninsider.blogspot.com/2024/05/python-3130-beta-1-released.html)

- "Python 3.13 is still in development. This release, 3.13.0b1, is the first of four beta release previews of 3.13.”
- New REPL, featuring multi-line editing, color support, colorized exception tracebacks
- Cool GIL, JIT, and GC features
- Typing changes, including typing.TypeIs . 
  - See last weeks episode and [**TypeIs does what I thought TypeGuard would do in Python**](https://rednafi.com/python/typeguard_vs_typeis/)
- Some nice dead battery removals
- and more
- But seriously, the REPL is cool. Just ask Trey
  - [The new REPL in Python 3.13](https://treyhunner.com/2024/05/my-favorite-python-3-dot-13-feature/) - Trey Hunner

**Michael #3:** [**A theme editor for JupyterLab**](https://blog.jupyter.org/a-theme-editor-for-jupyterlab-8f08ab62894d)

- by Florence Haudin
- **A new tool for authoring JupyterLab themes**
- To lower the bar for customizing JupyterLab we created a new tool providing a simple interface for tuning the JupyterLab appearance interactively.
- See [**jupyterlab-theme-editor**](https://github.com/jupyterlab-contrib/jupyterlab-theme-editor) on github

**Brian #4:** [**rich-argparse**](https://pypi.org/project/rich-argparse)

- “Format argparse and optparse help using [rich](https://pypi.org/project/rich).”
- “*rich-argparse* improves the look and readability of argparse's help while requiring minimal changes to the code.”
- They’re not kidding. 2 line code change.

```
from rich_argparse import RichHelpFormatter
parser = argparse.ArgumentParser(..., formatter_class=RichHelpFormatter)
```

**Extras** 

Brian:

- [**pytest course**](https://courses.pythontest.com/) is now switched to the new platform.
  - I sent out an email including how to save their spot on the old site and mark that spot complete on the new site.
  - There’s now comments on the course now. Trying that out. If you’ve got a question, just ask in that section. 

Michael:

- A new Talk Python course: [Getting Started with NLP and spaCy](https://training.talkpython.fm/courses/getting-started-with-spacy)

**Joke:** [Testing holiday](https://xkcd.com/2928/)