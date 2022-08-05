# Python Bytes 295

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Michael #1:** Ï[**Faster routing for Flask & Quart**](https://pgjones.dev/blog/faster-routing-2022/)

- Flask and Quart both utilise Werkzeug's HTTP route
- With the upcoming 2.2 release of Werkzeug this router will be significantly faster, with up to a factor of 5.
- Better for large sets of routes
- Micro-benchmarks are unaffected and are unlikely to show a speedup.
- Started with tree-based radix algorithm
- Moved to state machine algorithm because of wild cards

**Brian #2:** [**Quarto: an open-source scientific and technical publishing system built on Pandoc**](https://quarto.org/)

- suggested by Paul Mackenzie
- Power of Pandoc and Jupyter
- Build
    - documents - html, pdf, word
    - presentations - Revealjs, PowerPoint, Beemer
    - websites 
    - books - html, pdf, word, epub
    - journal articles - acm, plos, elsevier, acs, jss
- Publish
    - GitHub pages, Netlify, …
-  kinda related - [Kindle to support ePub](https://ebookfriendly.com/epub-kindle-things-to-know/)

**Michael #3:** [**Fl**](https://flet.dev)[**e**](https://flet.dev)[**t UI**](https://flet.dev)

- via Mikael Honkala
- New and upcoming UI framework by Feodor Fitzner: **flet**.
- It has a very interesting stack - a Python client driving a Flutter front-end via a Go server.
- That sounds complicated, but the developer experience is incredibly simple. Installation is just pip install flet.
- Here's a quick and stupid but working sample:
  
```
    import time
    
    import flet
    from flet import Column, ElevatedButton, Page, Row, TextField
    
    def main(page: Page):
        text_field = TextField()
    
        def clear_field(event):
            text_field.value = "CLEARING"
            page.update()
            time.sleep(1)
            text_field.value = ""
            page.update()
        
        clear_button = ElevatedButton("Clear the field", on_click=clear_field)
        page.add(Row([Column([text_field, clear_button])], alignment="center"))
        page.update()
    
    flet.app(target=main)
    
    # If you run this, you get a native app window on Mac, Windows or Linux, looking something like this:
```


![](https://paper-attachments.dropbox.com/s_C04B586155456E4F9A6DBBC0E3C98BB673F4D79145882E8AD80B47B15A25DBCA_1659560371560_flet-example.jpg)


- While the example is simple, it shows the handling of an event, updating the UI, and even doing a little sleeping between the updates, without having to worry about threads and such.
- What's more important, if you change the last line to:
  
```
    flet.app(target=main, view=WEB_BROWSER)
```

- You get the exact same functionality, but as a web application in a browser, with support for multiple users and deep linking to different parts of the app. All without leaving the comfortable Python world, with its access to all Python libraries, and without having to learn 3 extra, completely different languages (yes, HTML, CSS and JavaScript).
- As this is Flutter, mobile support is in the works, after the basic UI functionality is all there.
- Check the project front page here: [flet.dev](https://flet.dev)
- Jump directly to the currently available controls: [flet.dev/docs/controls](https://flet.dev/docs/controls)
- Check couple of tutorials here: [flet.dev/docs/tutorials](https://flet.dev/docs/tutorials)
- Or read the plans for the mobile support here: [flet.dev/blog/flet-mobile-strategy](https://flet.dev/blog/flet-mobile-strategy)

**Brian #4:** [**Building an authenticated Python CLI**](https://www.notia.ai/articles/building-an-authenticated-python-cli)

- Project that uses click, rich, and  OAth for using Twitter API
- Persistent authentication
    - requests secret information from user using `getpass` and `input`
        - Client ID, Client Secret, App name
    - fetches bearer token from Twitter API
    - stores token in `netrc` file
- I’m not familiar with netrc, so I don’t know if this is a good idea or not. 
    - So I figured I’d ask Michael

**Extras** 

Michael:

- New course: [**Django - Getting Started**](https://training.talkpython.fm/courses/getting-started-with-django)

**Joke:** [**Light touches kingdom**](https://twitter.com/pr0grammerhum0r/status/1543972967205556225?s=12&t=9gGvVIDpqOfv22I40TQUzw)
