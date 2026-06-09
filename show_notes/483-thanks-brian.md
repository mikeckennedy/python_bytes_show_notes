# #483: Thanks Brian

## Show Intro

Sponsored by us! Support our work through:
- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
**Connect with the hosts**
- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Calvin: [@calvinhp@sixfeetup.social](https://sixfeetup.social/@calvin) / [@calvinhp.com](https://bsky.app/profile/calvinhp.com) (bsky)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)
Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesday at 7am PT. Older video versions available there too.
Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

## Goodbye and Thanks Brian

Thanks Calvin for being part of this and future episodes! Also new time for the live show.
Thanks Brian for all the hard work over the years.

## **Michael #2: [HTTP GET requests with the Python standard library](https://alexwlchan.net/2026/python-http-with-the-stdlib/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026&_bhlid=b271298fb1de431c57a0d4e3bbbd2b9d2a11a213)**

- If you’re doing HTTP in Python, you’re probably using one of three popular libraries: [requests](https://requests.readthedocs.io/en/latest/), [httpx](https://github.com/encode/httpx), or [urllib3](https://github.com/urllib3/urllib3).
- There have been [issues with httpx lately](https://pythonbytes.fm/episodes/show/476/common-themes).
- [Niquest](https://github.com/jawah/niquests) is another option: Drop-in replacement for Requests. Automatic HTTP/1.1, HTTP/2, and HTTP/3. WebSocket, and SSE included.
- But maybe less is more, especially in the age of agentic AI
- A good candidate needs two things to be true at once, not one: the *used surface* is small, and the *behavior behind that surface* is shallow.

## **Calvin #1: Vulnerability and malware checks in uv**

-

## **Michael #4: [alembic-git-revisions](https://github.com/Mergifyio/alembic-git-revisions)**

- By Julien Danjou from ****[Mergify](https://mergify.com/)
- Automatic [Alembic](https://alembic.sqlalchemy.org/) migration chaining based on git commit history. No more `Multiple head revisions are present for given argument 'head'`.
- See [the introductory article](https://julien.danjou.info/blog/fixing-alembics-multiple-heads-problem-with-git/)
- Caused by two migrations landed with the same `down_revision`, and Alembic doesn’t know which one comes first. The fix is always the same: someone manually edits the migration file to re-chain the revisions.
- The insight: git already knows the order

## **Calvin #3: Millions of AI agents imperiled by critical vulnerability in open source package**

-

## **Extras**

### Calvin:
- GNU `make` can do pattern matching in the target. Not new at all, mentioned in the 1994-era docs. `just` and `task` don’t have this super power on the target name yet.
```
train-%:
        uv run ./train.py $* --save-hyper-params --overwrite $(TRAIN_ARGS)
```
### Michael:
- Updated my HTTP client using packages from httpx to [httpx2](https://github.com/pydantic/httpx2): [listmonk](https://pypi.org/project/listmonk/), [umami](https://pypi.org/project/umami-analytics/), and [memberful](https://pypi.org/project/memberful/). For motivation, see [this reddit thread](https://www.reddit.com/r/Python/comments/1rl5kuq/anyone_know_whats_up_with_httpx/?featured_on=pythonbytes).

## **Joke: [Accurate](https://x.com/PR0GRAMMERHUM0R/status/2061508112083714478)**

## Links

- [@calvinhp@sixfeetup.social](https://sixfeetup.social/@calvin)
- [@calvinhp.com](https://bsky.app/profile/calvinhp.com)
- [calvinhp.com](https://calvinhp.com)
- [HTTP GET requests with the Python standard library](https://alexwlchan.net/2026/python-http-with-the-stdlib/?utm_source=www.pythonweekly.com&utm_medium=newsletter&utm_campaign=python-weekly-issue-743-april-30-2026&_bhlid=b271298fb1de431c57a0d4e3bbbd2b9d2a11a213)
- [requests](https://requests.readthedocs.io/en/latest/)
- [httpx](https://github.com/encode/httpx)
- [urllib3](https://github.com/urllib3/urllib3)
- [issues with httpx lately](https://pythonbytes.fm/episodes/show/476/common-themes)
- [Niquest](https://github.com/jawah/niquests)
- [alembic-git-revisions](https://github.com/Mergifyio/alembic-git-revisions)
- [Mergify](https://mergify.com/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [the introductory article](https://julien.danjou.info/blog/fixing-alembics-multiple-heads-problem-with-git/)
- [httpx2](https://github.com/pydantic/httpx2)
- [listmonk](https://pypi.org/project/listmonk/)
- [umami](https://pypi.org/project/umami-analytics/)
- [memberful](https://pypi.org/project/memberful/)
- [this reddit thread](https://www.reddit.com/r/Python/comments/1rl5kuq/anyone_know_whats_up_with_httpx/?featured_on=pythonbytes)
- [Accurate](https://x.com/PR0GRAMMERHUM0R/status/2061508112083714478)
