# Python Bytes 382

Sponsored by ScoutAPM: [pythonbytes.fm/scout](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of 

the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

**Brian #1:** [**act: Run your GitHub Actions locally!** ](https://github.com/nektos/act)

- Why?
  - “Fast Feedback - Rather than having to commit/push every time you want to test out the changes you are making to your .github/workflows/ files (or for any changes to embedded GitHub actions), you can use act to run the actions locally. The environment variables and filesystem are all configured to match what GitHub provides.”
  - “Local Task Runner - I love make. However, I also hate repeating myself. With act, you can use the GitHub Actions defined in your .github/workflows/ to replace your Makefile!”
- Docs: [nektosact.com](https://nektosact.com/introduction.html)
- Uses Docker to run containers for each action.

**Michael #2:** [portr](https://portr.dev)

- Open source ngrok alternative designed for teams
- Expose local http, tcp or websocket connections to the public internet
- Warning: Portr is currently in beta. Expect bugs and anticipate breaking changes.
- [Server setup](https://portr.dev/server/) (docker basically).

**Brian #3:** [**Annotating args and kwargs in Python**](https://rednafi.com/python/annotate_args_and_kwargs/)

- Redowan Delowar
-  I don’t think I’ve ever tried, but this is a fun rabbit hole.
- Leveraging bits of PEP-5891, PEP-6462, PEP-6553, and PEP-6924.
- Punchline:

```
from typing import TypedDict, Unpack  *# Python 3.12+*
*# from typing_extensions import TypedDict, Unpack # < Python 3.12*
class Kw(TypedDict):
  key1: int
  key2: bool
def foo(*args: Unpack[tuple[int, str]], **kwargs: Unpack[Kw]) -> None:
  ...
```

- A recent pic from Redowan’s blog: 
  - [TypeIs does what I thought TypeGuard would do in Python](https://rednafi.com/python/typeguard_vs_typeis/)

**Michael #4:** [github badges](https://github.com/Envoy-VC/awesome-badges)

- ![smiling face with sunglasses](https://paper.dropboxstatic.com/static/img/ace/emoji/1f60e.png?version=8.0.0) A curated list of GitHub badges for your next project

**Extras** 

Brian:

- [Fake job interviews target developers with new Python backdoor](https://www.bleepingcomputer.com/news/security/fake-job-interviews-target-developers-with-new-python-backdoor/)
- Later this week, [course.pythontest.com](https://courses.pythontest.com) will shift from Teachable to Podia
  - Same great content. Just a different backend.
  - To celebrate, get 25% off at [pythontest.podia.com](https://pythontest.podia.com) now through this Sunday using coupon code PYTEST
- [Getting the most out of PyCon, including juggling - Rob Ludwick](https://podcast.pythontest.com/episodes/220-juggling-pycon)
  - Latest PythonTest episode, also cross posted to [pythonpeople.fm](https://pythonpeople.fm)
- [3D visualization of dom](https://hci.social/@orion/112167137880858495)

Michael:

- [Djangonauts Space Session 2 Applications](https://djangonaut.space/comms/2024/04/25/2024-opening-session-2/) Open! More background at [Djangonauts, Ready for Blast-Off](https://talkpython.fm/episodes/show/451/djangonauts-ready-for-blast-off) on Talk Python.
- [Self-Hosted Open Source - Michael Kennedy](https://djangochat.com/episodes/michael-kennedy) on Django Chat

**Joke:** [silly games](https://www.reddit.com/r/programminghumor/comments/1ceo0ds/just_a_silly_little_game/)

Closing song: [Permission Granted](https://www.youtube.com/watch?v=pGbodliLFVE)