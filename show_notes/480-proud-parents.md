# PB 480

## **Show Intro**

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**The Complete pytest Course**](https://courses.pythontest.com/p/the-complete-pytest-course)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [@mkennedy@fosstodon.org](https://fosstodon.org/@mkennedy) / [@mkennedy.codes](https://bsky.app/profile/mkennedy.codes) (bsky)
- Brian: [@brianokken@fosstodon.org](https://fosstodon.org/@brianokken) / [@brianokken.bsky.social](https://bsky.app/profile/brianokken.bsky.social)
- Show: [@pythonbytes@fosstodon.org](https://fosstodon.org/@pythonbytes) / [@pythonbytes.fm](https://bsky.app/profile/pythonbytes.fm) (bsky)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually **Monday** at 11am PT. Older video versions available there too.

Finally, if you want an artisanal, hand-crafted digest of every week of the show notes in email form? Add your name and email to [our friends of the show list](https://pythonbytes.fm/friends-of-the-show), we'll never share it.

## **Brian #1: [Using Django Tasks in production](https://www.better-simple.com/django/2026/05/06/using-django-tasks-in-production/)**

- Tim Schilling shares how the Djangonaut Space website has been using Django’s new tasks framework and some of the info missing from the official Django docs.
- Tasks require a third party package, [`django-tasks-db`](https://github.com/RealOrangeOne/django-tasks-db) to actually run the tasks.
- Article walks through all changes necessary to get an email process running to notify admins of new testimonials. Cool simple example.
- With the db backend, you can monitor progress of tasks in the admin, to see which tasks are scheduled, completed, or have errors.
- Some wishes for the community to implement
  - new tutorial in the Django docs
  - Django Debug toolbar panel for tasks
  - test/mock backend
- Great title for wish list: Thinks I’d like to see, but I’m too lazy to implement myself.

## **Michael #2: Co-authored with Claude?**

- Via Nik T.
- We don’t put “executed on macOS”, “edited with PyCharm”, etc. in our commits. Why Claude?
- Seems like a growth hack to me, that I don’t really care to participate in.
- Some projects that have formalized their thoughts on this: [The Generative AI Policy Landscape in Open Source](https://redmonk.com/kholterhoff/2026/02/26/generative-ai-policy-landscape-in-open-source/)
- Adjust to turn off in `~/.claude/settings.json` see [the docs](https://code.claude.com/docs/en/settings#attribution-settings).

```json
{
   "attribution": {
      "commit": "",
       "pr": ""
   }
}
```

## **Brian #3: [PyPI packages are increasing rapidly](https://rushter.com/blog/pypi-packages/)**

- Artem Golubin
- There’s been an increase of published packages per week on PyPI
- A pretty big increase in the last handful of months.
- 30% increase since 2025, clearly due to AI
- Artem is building [hexora](https://github.com/rushter/hexora), a malicious Python code detector.
- Cool package too, it can:
  - Audit project dependencies to catch potential supply-chain attacks
  - Detect malicious scripts found on platforms like Pastebin, GitHub, or open directories
  - Analyze IoC files from past security incidents
  - Audit new packages uploaded to PyPi.
- Artem is using hexora to analyze recently published pypi packages and many are obviously vibecoded and trigger false positives for abuses of `eval`, `exec`, and `subprocess`
  - Side note: I don’t think that’s necessarily a false positive. Not malicious, but maybe a stupid-code-detector?
- Lots are LLM related, Lots have bots contributing code
- Publishing rate is crazy, dozens to hundreds of published versions in a day is a bug, not a feature
- Brian’s proposal, PyPI should limit releases per day for any package to something a sane human would do, even if they make a mistake on a release, to maybe like 2-3, definitely under 10, in a day. And if the repo has obvious agent contributors listed, maybe lower to the limit to 1-2 a day? Honestly, “move fast and break things” doesn’t apply to breaking the commons.

## **Michael #4: [httpx2](https://tildeweb.nl/~michiel/httpx2.html)**

- More on the httpx, httpxyz, etc changes: Pydantic people started their own fork, [httpx2](https://github.com/pydantic/httpx2).
- Michiel says “while we think httpxyz was definitely needed, we welcome httpx2 and think it should be the ‘blessed’ fork.”
- Kludex, who is among other things maintainer of Starlette, was considering a fork
- As it stands, httpx2 is lacking the performance improvements they added to httpxyz. But it will not be long before they will add those, too.
- Also they already made some smart decisions:
  - they are switching from certifi to [truststore](https://github.com/pydantic/httpx2/pull/209)
  - they are switching to [compression.zstd](https://github.com/pydantic/httpx2/pull/933) on Python 3.14+, enabling zstd compression by default
  - they [merged httpcore](https://github.com/pydantic/httpx2/commit/160c7f59d7942efe0133516c161d39139780eb45) and vendored it in their repository
- [Discussion on Hacker News](https://news.ycombinator.com/item?id=48127570)

## **Extras**

Brian:

- [The Four Horsemen of the LLM Apocalypse](https://anarc.at/blog/2026-05-16-four-horsemen/) - Anarcat
- [Django/JetBrains 2026 developer survey](https://www.djangoproject.com/weblog/2026/may/12/2026-django-developers-survey/) is open
- [Pyrefly 1.0](https://pyrefly.org/blog/v1.0/) : “meaning we are confident that Pyrefly is ready for production use.”

Michael:

- Just about ready to release Python Web Security: OWASP Top 10 with Agentic AI course. Be sure to be on [the courses newsletter](https://training.talkpython.fm/getnotified) to get notified.

## **Joke:** [Proud Parents](https://x.com/PR0GRAMMERHUM0R/status/1973145866962665752)