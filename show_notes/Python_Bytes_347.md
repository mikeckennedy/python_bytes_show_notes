# Python Bytes 347

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Python People**](https://pythonpeople.fm) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**async-timeout**](https://pypi.org/project/async-timeout/)

- An asyncio-compatible timeout context manager.
- The context manager is useful in cases when you want to apply timeout logic around block of code or in cases when `asyncio.wait_for()` is not suitable.
- Not finished yet timeout can be rescheduled by `shift_by()` or `shift_to()` methods

**Brian #2:** [**PyPI Project URLs Cheatsheet**](https://daniel.feldroy.com/posts/2023-08-pypi-project-urls-cheatsheet)

- Daniel Roy Greenfield
- There’s some cool icons available under “Project Links” on pypi.org project pages.
- How do you get those? And which ones are available.
- Daniel has found out where to look, and built us a cheat sheet. Nice.

**Michael #3:** [**httpx-sse**](https://pypi.org/project/httpx-sse/)

- Consume [Server-Sent Event (SSE)](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) messages with [HTTPX](https://www.python-httpx.org/).
- SSE are super lightweight, server → client only subscriptions. 
- Like websockets but less overhead (especially for iot and mobile devices)
- `httpx-sse` provides the `[connect_sse](https://github.com/florimondmanca/httpx-sse#connect_sse)` and `[aconnect_sse](https://github.com/florimondmanca/httpx-sse#aconnect_sse)` helpers for connecting to an SSE endpoint.
- The resulting `[EventSource](https://github.com/florimondmanca/httpx-sse#eventsource)` object exposes the `[.iter_sse()](https://github.com/florimondmanca/httpx-sse#iter_sse)` and `[.aiter_sse()](https://github.com/florimondmanca/httpx-sse#aiter_sse)` methods to iterate over the server-sent events.

**Brian #4:** [**Creating a context manager in Python**](https://www.pythonmorsels.com/creating-a-context-manager/)

- Trey Hunner
- Context managers are those things you use in a `with` block.
- There’s a bunch of cool built in ones. 
- Building your own is a handy skill to have to clean up your code, and they’re pretty easy, with Trey’s tutorial.
- Shown is a great example of temporarily modifying an environmental variable.
- Then he gets into what you need to know about `as`, `__enter__`, and `__exit__`.

**Extras** 

Brian:

- I think I’ll nix the intro music to Python People. I didn’t know what music to use, so I re-used the music from Test & Code. And I got some very honest feedback that it just doesn’t fit and was better without it. So I’ll rip it out soon. 
- BTW, next episode to be released is with Bob Belderbos from PyBites. Should be later this week.

Michael:

- [**Facebook and Instagram start blocking news in Canada**](https://www.theverge.com/2023/8/1/23815994/meta-facebook-instagram-canada-news-act-blocking)

**Joke:** 

- [**day 1 and I hate it**](https://www.reddit.com/r/programminghumor/comments/14e6ab6/was_about_to_define_a_datetime_format_in_a/)

