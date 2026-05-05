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

**Brian #1: [profiling-explorer](https://github.com/adamchainz/profiling-explorer)**

- Adam Johnson
- And intro post [Python: introducing profiling-explorer](https://adamj.eu/tech/2026/04/03/python-introducing-profiling-explorer/)
- “[profiling-explorer](https://pypi.org/project/profiling-explorer/) is a tool for exploring profiling data from Python’s built-in profilers, which are stored in pstats files. ”
- Features
  - Dark mode
  - Click the **calls**, **internal ms**, or **cumulative ms** column headers to sort by that column.
  - Use the search box to filter by filename or function name.
  - Hover by a filename + line number pair to reveal the copy button, which copies the location to your clipboard for faster opening.
  - Click the **callers** or **callees** links on the right of a row (not pictured above) to see the callers or callees of that function.

**Michael #2: [Reverting the incremental GC in Python 3.14 and 3.15](https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014)**

- Python 3.14 shipped with a new incremental garbage collector, but production reports of severe memory pressure (Neil Schemenauer measured up to 5× peak RSS on pathological cyclic workloads) have pushed the core team and Steering Council to revert it in both 3.14 and 3.15 - returning to the 3.13-era generational GC.
- This is the second time the inc GC has been pulled back: it was also reverted right before 3.13.0 final, and it shipped in 3.14 without going through the PEP process.
- The tradeoff is real: Neil's benchmarks showed max GC pause times of 1.3ms with inc GC versus 26ms with the generational one - great for latency-sensitive apps, terrible for memory-constrained ones.
- Release manager Hugo van Kemenade will ship 3.14.5 early with the revert, and Gregory Smith floated the idea of a 3.14.5rc1 - the first patch-release RC since 3.9.2 back in 2021.
- Tim Peters spent the thread doing live forensics on Windows, running a toy deque program that should cap at 1GB and watching it balloon to 15.6GB on a 16GB machine - and discovered the gen0 collector effectively never fires under the new scheme.
- Tim's bigger meta-point: CPython has a chronic shortage of real-world GC benchmarks, pyperformance has "basically no interesting" cyclic workloads, and users almost never share real data - so core devs keep flying blind on changes like this.
- Django maintainer Adam Johnson published a blog post mid-thread documenting a real memory "leak" in Django's migration system caused by inc GC, with a manual `gc.collect()` workaround - the listener-facing receipt that this wasn't just theoretical.
- If the inc GC comes back for 3.16, it'll go through a proper PEP, and the discussion is already shifting toward keeping both collectors available via a startup flag - which Neil and Sergey Miryanov have both prototyped.

**Brian #3: VSCode AI Co-author defaults to on, then off**

- VSCode merges [Enabling ai co author by default](https://github.com/microsoft/vscode/pull/310226) - 3 week ago
- Ton’s of “why would you do this” and related comments
- VSCode merges [Change default for git.addAICoAuthor to off](https://github.com/microsoft/vscode/pull/313931) - yesterday
- Take-away, don’t rely on default, set addAICoAuthor to off yourself

**Michael #4: [django freeze](https://github.com/fabiocaccamo/django-freeze)**

- Convert your dynamic django site to a static one with one line of code.
- Just run `python manage.py generate_static_site` :)
- Features
  - **Generate** the **static version** of your Django site, optionally compressed **.zip file**
  - **Generate/download** the static site using **urls** *(only superuser and staff)*
  - Follow **sitemap.xml** urls
  - Follow **internal links** founded in each page
  - Follow **redirects**
  - **Report** invalid/broken urls
  - Selectively **include/exclude media and static files**
  - Custom **base url** *(very useful if the static site will run in a specific folder different by the document-root)*
  - Convert urls to **relative urls** *(very useful if the static site will run offline or in an unknown folder different by the document-root)*
  - Prevent local directory index

**Extras**

Brian:

- [Thinking Less, Trusting More: GenAI’s Impacts on Students’ Cognitive Habits](https://arxiv.org/html/2601.22430v2)

Michael:

- [Vercel breached, employee to blame](https://www.reddit.com/r/technology/comments/1sr2wwt/ai_cloud_company_vercel_breached_after_employee/)
- [Introducing the new Talk Python web player](https://talkpython.fm/blog/posts/rebuilt-the-web-audio-experience/)
- GitHub uptime (a couple of views [1](https://github.blog/news-insights/company-news/an-update-on-github-availability/), [2](https://mrshu.github.io/github-statuses/))

**Joke: [Friends in tech](https://x.com/pr0grammerhum0r/status/2046650199930458334?s=46)**