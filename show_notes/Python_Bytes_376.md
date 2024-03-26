# Python Bytes 376
Sponsored by ScoutAPM: [**pythonbytes.fm/scout**](https://pythonbytes.fm/scout)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**🤖**](https://micro.webology.dev/2024/03/20/on-robotstxt.html?utm_source=pocket_saves) [**On Robots.txt**](https://micro.webology.dev/2024/03/20/on-robotstxt.html)

- Jeff Triplett
- “In theory, this file helps control what search engines and AI scrapers are allowed to visit, but I need more confidence in its effectiveness in the post-AI apocalyptic world.”
- Resources to get started
    - [Block the Bots that Feed “AI” Models by Scraping Your Website](https://neil-clarke.com/block-the-bots-that-feed-ai-models-by-scraping-your-website/)
    - [Go ahead and block AI web crawlers](https://coryd.dev/posts/2024/go-ahead-and-block-ai-web-crawlers/)
    - [Dark Visitors](https://darkvisitors.com/)
    - Django
        - [Add robots.txt to a Django website](https://learndjango.com/tutorials/add-robotstxt-django-website)
        - [How to add a robots.txt to your Django site](https://adamj.eu/tech/2020/02/10/robots-txt/)
    - Hugo
        - [Hugo robots.txt](https://gohugo.io/templates/robots/)
- Podcast questions:
    - Should content creators block AI from our work?
    - Should’t we set up a standard way to do this?
    - I still haven’t found a way to block GitHub repositories. 
        - Is there a way?
        - Licensing is one thing (not easy), but I don’t think any bots respect any protocol for repos.

**Michael #2:** [**niquests**](https://github.com/jawah/niquests)

- Requests but with HTTP/3, HTTP/2, Multiplexed Connections, System CAs, Certificate Revocation, DNS over HTTPS / TLS / QUIC or UDP, Async, DNSSEC, and (much) pain removed!
- **Niquests** is a simple, yet elegant, HTTP library. It is a drop-in replacement for **Requests**, which is under feature freeze.
-  **See why you should switch:** [Read about 10 reasons why](https://medium.com/dev-genius/10-reasons-you-should-quit-your-http-client-98fd4c94bef3)



**Brian #3:**  [**Every dunder method in Python**](https://www.pythonmorsels.com/every-dunder-method/)

- Trey Hunner
- Sure, there’s `__repr__()`, `__str__()`, and `__init__()`, but how about dunder methods for:
    - Equality and hashability
    - Orderability
    - Type conversions and formatting
    - Context managers
    - Containers and collections
    - Callability
    - Arithmetic operators
    - … and so much more … even a cheat sheet.
    

**Michael #4:** [**Lockbox**](https://github.com/mkjt2/lockbox)

- Lockbox is a forward proxy for making third party API calls.
- Why? Automation or workflow platforms like Zapier and IFTTT allow "webhook" actions for interacting with third party APIs.
- They require you to provide your third party API keys so they can act on your behalf. You are trusting them to keep your API keys safe, and that they do not misuse them.
- How Lockbox helps: When a workflow platform needs to make a third party API call on your behalf, it makes a Lockbox API call instead. Lockbox makes the call to the third party API, and returns the result to the workflow platform.



**Extras** 

Brian:

- [**Django: Join the community on Mastodon**](https://adamj.eu/tech/2024/02/10/django-join-community-mastodon/) - Adam Johnson
- [**No maintenance intended**](https://unmaintained.tech/) - Sent in from Kim van Wyk

Michael:

- US sues Apple
    - [Good video on pluses and minuses](https://www.youtube.com/watch?v=_O5XMMvGJ1M)
    - [The hot water just the day before](https://www.youtube.com/watch?v=A69-8XxLbJ4) [[and this one](https://www.youtube.com/watch?v=4ut-de57A2c)]
    - [https://9to5mac.com/2024/03/25/app-store-proposals-rejected/](https://9to5mac.com/2024/03/25/app-store-proposals-rejected/) 
- [PyPI Support Specialist job](https://twitter.com/thepsf/status/1770528868111130683?s=12&t=RL7Nk7OAFSptvENxe1zIqA)
- [VS Code AMA](https://www.youtube.com/watch?v=Jh24NVM2FDY), please [submit your question here](https://forms.gle/thh3pYteN3dGYYvN9) 
- [PyData Eindhoven 2024](https://fosstodon.org/@gthomas/112158142020246243) has a date and open CFP

**Joke:**  [**Windows Certified**](https://ioc.exchange/@rye/112079906909625874)

