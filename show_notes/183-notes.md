# Python Bytes 183
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

Special guest: Calvin Hendryx-Parker [@calvinhp](https://twitter.com/calvinhp)

----------

**Brian #1:**  [**fastpages: An easy to use blogging platform, with enhanced support for Jupyter Notebooks.**](https://github.com/fastai/fastpages) 

- Uses GH actions to Jekyll blog posts on GitHub Pages.
- Create posts with code, output of code, formatted text, directory from Jupyter Notebooks.
- Altair interactive visualizations
- Collapsible code cells that can be open or closed by default.
- Metadata like title, summary, in special markdown cells.
- twitter cards and YouTube videos
- tags support
- Support for pure markdown posts 
- and even MS Word docs for posts. (but really, don’t).
- Documentation and introduction written in fastpages itself, [https://fastpages.fast.ai/](https://fastpages.fast.ai/)



----------

**Michael #2:** [**BeeKeeper Studio Open Source SQL Editor and Database Manager**](https://www.beekeeperstudio.io)

- Use Beekeeper Studio to query and manage your relational databases, like **MySQL**, **Postgres**, **SQLite**, and **SQL Server**.
- Runs on all the things  (Windows, Linux, macOS)
-  Features
	- Autocomplete SQL query editor with syntax highlighting
	- Tabbed interface, so you can multitask
	- Sort and filter table data to find just what you need
	- Sensible keyboard-shortcuts
	- Save queries for later
	- Query run-history, so you can find that one query you got working 3 days ago
	- Default dark theme
- Connect: Alongside normal connections you can encrypt your connection with SSL, or tunnel through SSH. Save a connection password and Beekeeper Studio will make sure to encrypt it to keep it safe.
- SQL Auto Completion: Built-in editor provides syntax highlighting and auto-complete suggestions for your tables so you can work quickly and easily.
- Open Lots of Tabs: Open dozens of tabs so you can write multiple queries and tables in tandem without having to switch windows.
- Save queries
- View Table Data: Tables get their own tabs too! Use our table view to sort and filter results by column.



----------

**Calvin #3:** **2nd Annual** [**Python**](https://2020.pythonwebconf.com/) [**Web**](https://2020.pythonwebconf.com/) [**Conference**](https://2020.pythonwebconf.com/)
[](https://2020.pythonwebconf.com/)
- The most in-depth Python conference for web developers
	- Targeted at production users of Python
	- Talks on Django, Flask, Twisted, Testing, SQLAlchemy, Containers, Deployment and more
- June 17th-19th — One day of tutorials and two days of talks in 3 tracks
- Keynote talks by 
	- Lorena Mesa
	- Hynek Schlawack
	- Russell Keith-Magee
	- Steve Flanders
- Fireside Chat with Carl Meyer about Instragram’s infrastructure, best practices
- Participate in 40+ presentations and 6 tutorials
- Fun will be had and connections made
	- Virtual cocktails
	- Online gaming
	- Board game night
- Tickets are $199 and $99 for Students
	- As a bonus, for every **Professional** ticket purchased, we'll donate a ticket to an attendee in a [developing country.](https://unstats.un.org/unsd/methodology/m49/) 
	- As a Python Bytes listener you can get a 20% discount with the code PB20

----------

 **Brian #4:** [**Mimesis - Fake Data Generator**](https://mimesis.name/)

- “…helps generate big volumes of fake data for a variety of purposes in a variety of languages.”
- Custom and generic data providers
- >33 locales
- Lots of locale dependent providers, like address, Food, Person, …
- Locale independent providers. 
- Super fast. Benchmarking with 10k full names was like [60x faster than Faker](https://mimesis.name/foreword.html#advantages).
- Data generation by schema. Very cool

```
    >>> from mimesis.schema import Field, Schema
    >>> _ = Field('en')
    >>> description = (
    ...     lambda: {
    ...         'id': _('uuid'),
    ...         'name': _('text.word'),
    ...         'version': _('version', pre_release=True),
    ...         'timestamp': _('timestamp', posix=False),
    ...         'owner': {
    ...             'email': _('person.email', domains=['test.com'], key=str.lower),
    ...             'token': _('token_hex'),
    ...             'creator': _('full_name'),
    ...         },
    ...     }
    ... )
    >>> schema = Schema(schema=description)
    >>> schema.create(iterations=1)
```

```
- Output:
    [
      {
        "owner": {
          "email": "aisling2032@test.com",
          "token": "cc8450298958f8b95891d90200f189ef591cf2c27e66e5c8f362f839fcc01370",
          "creator": "Veronika Dyer"
        },
        "name": "widget",
        "version": "4.3.1-rc.5",
        "id": "33abf08a-77fd-1d78-86ae-04d88443d0e0",
        "timestamp": "2018-07-29T15:25:02Z"
      }
    ]
``` 


----------

**Michael #5:**  [**Schemathesis**](https://github.com/kiwicom/schemathesis)

- A tool for testing your web applications built with Open API / Swagger specifications.
-  **Supported specification versions**:
	- Swagger 2.0
	- Open API 3.0.x
- Built with:
	- [hypothesis](https://hypothesis.works/)
	- [hypothesis_jsonschema](https://github.com/Zac-HD/hypothesis-jsonschema)
	- [pytest](http://pytest.org/en/latest/)
- It reads the application schema and generates test cases which will ensure that your application is compliant with its schema.
- Use: There are two basic ways to use Schemathesis:
	- [Command Line Interface](https://github.com/kiwicom/schemathesis#command-line-interface)
	- [Writing tests in Python](https://github.com/kiwicom/schemathesis#in-code)
- CLI supports passing options to `hypothesis.settings`.
- To speed up the testing process Schemathesis provides `-w/--workers` option for concurrent test execution
- If you'd like to test your web app (Flask or AioHTTP for example) then there is `--app` option for you
- Schemathesis CLI also available as a docker image
- Code example:

```
    import requests
    import schemathesis
    
    schema = schemathesis.from_uri("http://0.0.0.0:8080/swagger.json")
    
    @schema.parametrize()
    def test_no_server_errors(case):
        # `requests` will make an appropriate call under the hood
        response = case.call()  # use `call_wsgi` if you used `schemathesis.from_wsgi`
        # You could use built-in checks
        case.validate_response(response)
        # Or assert the response manually
        assert response.status_code < 500
```



----------

**Calvin #6:** [Finding secrets by decompiling Python bytecode in public repositories](https://blog.jse.li/posts/pyc/)

- Jesse’s initial research revealed that **thousands of GitHub repositories contain secrets hidden inside their bytecode.**
- It has been common practice to store secrets in Python files that are typically ignored such as `settings.py`, `config.py` or `secrets.py`, but this is potentially insecure
- Includes a nice crash course on Python byte code and cached source
- This post comes with a small capture-the-flag style lab for you to try out this style of attack yourself.
	- You can find it at [https://github.com/veggiedefender/pyc-secret-lab/](https://github.com/veggiedefender/pyc-secret-lab/)
- Look through your repositories for loose `.pyc` files, and delete them
- If you have `.pyc` files and they contain secrets, then revoke and rotate your secrets
- Use a standard [gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore) to prevent checking in `.pyc` files
- Use JSON files or environment variables for configuration


----------

**Extras:**

Michael:

- [Python 3.9.0b1 Is Now Available for Testing](https://pycoders.com/link/4164/yrq2q8ogch)
- [Python 3.8.3 Is Now Available](https://pycoders.com/link/4141/yrq2q8ogch)
- Ventilators and Python: Some particle physicists put some of their free time to design and build a low-cost ventilator for covid-19 patients for use in hospitals. https://arxiv.org/pdf/2003.10405.pdf Search of the PDF for Python: 
	- "Target computing platform: Raspberry Pi 4 (any memory size), chosen as a trade-off between its computing power over power consumption ratio and its wide availability on the market; • Target operating: Raspbian version 2020-02-13; • Target programming language: Python 3.5; • Target PyQt5: version 5.11.3."
	- "The MVM GUI is a Python3 software, written using the PyQt5 toolkit, that allows steering and monitoring the MVM equipment."

Brian:  

-  [Call for Volunteers! Python GitHub Migration Work Group](https://pyfound.blogspot.com/2020/05/call-for-volunteers-python-github.html)
	- migration from bugs.python.org to GitHub

Calvin:

- [Learn Python Humble Bundle](https://www.humblebundle.com/books/learn-you-some-python-no-starch-press-books)
	- Pay $15+ and get an amazing set of Python books to start learning at all levels
	- Book Industry Charitable Foundation
	- The No Starch Press Foundation


----------

**Joke:**

More O’Really book covers


![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e40973c987720803c1b9835/3991d6bf089ee4ebf2732f22bcd062e7/Screen_Shot_2020-05-18_at_1.44.44_PM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e40973c987720803c1b9835/4de00d6aaa4c95f7ffa4c9734dd71acf/Screen_Shot_2020-05-18_at_1.44.20_PM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e40973c987720803c1b9835/5c2dead404a8e52ea4e5fdb0535aec08/Screen_Shot_2020-05-18_at_1.43.45_PM.png)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5e40973c987720803c1b9835/316e93f3caff2b6d04d675860adca8a5/Screen_Shot_2020-05-18_at_1.43.25_PM.png)



