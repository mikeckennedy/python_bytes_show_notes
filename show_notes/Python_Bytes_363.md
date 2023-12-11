# Python Bytes 363

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** Ï[**Fixit 2: Meta’s next-generation auto-fixing linter**](https://engineering.fb.com/2023/08/07/developer-tools/fixit-2-linter-meta/)

-  via Bart Kappenburg
- Fixit is dead! Long live Fixit 2 – the latest version of our open-source auto-fixing linter.
- Fixit provides a highly configurable linting framework with support for auto-fixes, custom “local” lint rules, and hierarchical configuration, built on [LibCST](https://libcst.rtfd.io/).
- Fixit 2 is available today on PyPI.
- Created by Meta’s Python Language Foundation team — a hybrid team of both PEs and traditional SWEs — helps own and maintain the infrastructure and tooling for Python.
- Interesting comments on [this article on Hacker News](https://news.ycombinator.com/item?id=38378776)
- I wonder if ruff format was already a thing when Fixit was adopted, whether it would exist?

**Brian #2:** [**FastUI**](https://github.com/samuelcolvin/FastUI?utm_source=pocket_reader)

- Samuel Colvin
- “FastUI is a new way to build web application user interfaces defined by declarative Python code.”
- MK: Reminds me of the code matches DOM style of Flutter. [See code samples at the end](https://www.darttutorial.org/flutter-tutorial/flutter-hello-world/).

**Michael #3:** [Mail list / newsletter conversation](https://fosstodon.org/@mkennedy/111458548009143322)

- I’ve been tired of Mailchimp for a long time
- Raising the prices month over month by $100 several months may be the straw
- But what are the options? [Lets ask Mastodon](https://fosstodon.org/@mkennedy/111458548009143322):
    - [emailoctopus.com](https://emailoctopus.com/)
    - [listmonk.app](https://listmonk.app/) [self hosted, open source]
    - [keila.io](https://www.keila.io/) [self/saas, open source]
    - [mailyherald.org](https://mailyherald.org/) [self hosted, open source]
    - [sendportal.io](https://sendportal.io/) [self hosted, open source]
    - [brevo.com](https://www.brevo.com/)
    - [buttondown.email](https://buttondown.email/) [django]
    - [zoho.com/campaigns/](https://www.zoho.com/campaigns/)
    - [sendy.co](https://sendy.co/) [use your own bulk emailer (e.g. sendgrid or aws ses)
    - [convertkit.com](https://convertkit.com/) 
    - [mautic.org](https://www.mautic.org/) [open source]
    - [constantcontact.com](https://www.constantcontact.com/) 
    - [getresponse.com](https://www.getresponse.com/)
    - [convertkit.com](https://convertkit.com/)

**Brian #4:** **CLIs from type hints**

- From Sander76
- [**Pydantic Argparse**](https://pydantic-argparse.supimdos.com/) “is a Python package built on top of pydantic which provides declarative typed argument parsing using pydantic models.”
  - [**Clipstick**](https://github.com/sander76/clipstick) is a “cli-tool based on Pydantic models.”
  - [**tyro**](https://github.com/brentyi/tyro) “is a tool for generating command-line interfaces and configuration objects in Python.”
    - tyro includes support for dataclasses and attrs in place of Pydantic

**Extras** 

Brian:

- [**Django 5.0 has been released**](https://www.djangoproject.com/weblog/2023/dec/04/django-50-released/)
- [**vim-keybindings-everywhere-the-ultimate-list**](https://github.com/erikw/vim-keybindings-everywhere-the-ultimate-list) - submitted by Paul Barry
- [**PythonTest**](https://podcast.pythontest.com/) (the podcast formerly known as [Test & Code](https://podcast.pythontest.com/), to be read in an undertone similar to the way one used to say “The artist formerly known as Prince”) has moved form testandcode.com to [podcast.pythontest.com](https://podcast.pythontest.com/)
    - Plus more [guests](https://podcast.pythontest.com/people) are listed now. I think I’ve gone backwards from current to episode 182. I tried to get my kid to help out, unsuccessfully. May have to hire someone to help. grrr.

Michael:

- Essay: [Don't Sweat the Ad Blocker Drama](https://mkennedy.codes/posts/dont-sweat-the-ad-blocker-drama/)
- A story: my project this weekend, unify my over 20 domains to one host

**Joke:** [Honest LinkedIn](https://hachyderm.io/@collinsworth/111455073305710058)

