# Python Bytes 225

Sponsored by **Linode!** [**pythonbytes.fm/linode**](https://pythonbytes.fm/linode)
Special guest: [**Sebastian Witowski**](https://twitter.com/SebaWitowski)

YOUTUBE id=Omdzzl6XHDE

**Brian #1:** **Raspberry Pi Pico**

- [Release Announcement](https://www.raspberrypi.org/blog/raspberry-pi-silicon-pico-now-on-sale/)
- [A review](https://www.tomshardware.com/reviews/raspberry-pi-pico-review)
- $4 microcontroller
- Small
- Extremely low power needs.
- Built on RP2040, a brand-new chip developed by Raspberry Pi
- Related: [**Mu : codewith.mu**](https://codewith.mu/)**,** [1.1.0-beta.2](https://mu.readthedocs.io/en/latest/changes.html)
	- Mu is “a simple Python editor for beginner programmers.”
	- 1.1.0 support new boards, including Pico, Lego Spike, plus lots of new fixes.

**Michael #2:** [**New MongoDB ODM: Beanie**](https://dev.to/romanright/announcing-beanie-mongodb-odm-56e) 

- via PyCoders
- Beanie - is an asynchronous ODM for MongoDB, based on [Motor](https://motor.readthedocs.io/en/stable/) and [Pydantic](https://pydantic-docs.helpmanual.io/).
- Very new but also very exciting.
- Main component of Beanie is [Pydantic](https://pydantic-docs.helpmanual.io/). It helps to implement the main feature - data structuring. 
- Beanie `Document` - is an abstraction over the Pydantic `BaseModel` that allows working with Python objects at the application level and JSON objects at the database level.
- Example, classes:

```
    class TagColors(str, Enum):
        RED = "RED"
        BLUE = "BLUE"
        GREEN = "GREEN"
    
    class Tag(BaseModel):
        name: str
        color: TagColors = TagColors.BLUE
    
    class Note(Document):  # This is the document structure
        title: str
        text: Optional[str]
        tag_list: List[Tag] = []
```


**Sebastian #3:** [**Sourcery**](https://sourcery.ai/) 

- No, not the Terry Pratchett novel (although this one is pretty cool too!)
- Gives you refactoring recommendations in your code editor
- Integrates with PyCharm and VS Code
- Super easy to use - you get suggestions as you type and with one click you can apply them
- Free to use in the code editor (you will need a personal token) and paid plans with analytics, CI integration, etc.
- It keeps finding errors in my code (well, maybe I'm just a bad programmer 😉)

**Michael #4:** [**Neomodel**](https://neomodel.readthedocs.io/en/latest/)

- An Object Graph Mapper (OGM) for the [neo4j](https://www.neo4j.org) graph database, built on the awesome [neo4j_driver](https://github.com/neo4j/neo4j-python-driver)
- Features:
- Familiar Django model style definitions.
- Powerful query API.
- Enforce your schema through cardinality restrictions.
- Full transaction support.
- Thread safe.
- pre/post save/delete hooks.
- Django integration via [django_neomodel](https://github.com/neo4j-contrib/django-neomodel)
- Example of classes
```
    from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
        UniqueIdProperty, RelationshipTo)
    
    config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
    
    class Country(StructuredNode):
        code = StringProperty(unique_index=True, required=True)
    
    class Person(StructuredNode):
        uid = UniqueIdProperty()
        name = StringProperty(unique_index=True)
        age = IntegerProperty(index=True, default=0)
    
        # traverse outgoing IS_FROM relations, inflate to Country objects
        country = RelationshipTo(Country, 'IS_FROM')
```

- Relationships
```
    germany = Country.nodes.filter(code='DE)
    jim = Person.nodes.get(name='Jim')
    jim.country.connect(germany)
    
    if jim.country.is_connected(germany):
        print("Jim's from Germany")
    
    for p in germany.inhabitant.all():
        print(p.name) # Jim, ...
    
    len(germany.inhabitant) # N: int
    
    # Find people called 'Jim' in germany
    germany.inhabitant.search(name='Jim')
    
    # Find all the people called in germany except 'Jim'
    germany.inhabitant.exclude(name='Jim')
```

**B****rian** **#:** [**A mock must always have a spec**](https://blog.thea.codes/my-python-testing-style-guide/#a-mock-must-always-have-a-spec)

- From Stargirl Flowers “[My Python testing style guide](https://blog.thea.codes/my-python-testing-style-guide/)”
- Great guide altogether, but this bit about mock specs is awesome.
- Some mocking guidance:
	- Use real objects for collaborators whenever possible
	- A mock must always have a spec with `mock.create_autospec()` or `mock.patch(..., autospec=True)`.
	    - “This ensures there's some connection between your mock and the real collaborator's interface. If you change the collaborator's interface in a way that breaks downstream targets, those targets tests will rightfully fail.”
	- Consider using a stub or fake (with examples)
	- Consider a spy (real object + mock wrapper lets you assert called and such)
	- Don't give mock/stubs/fakes special names
	- Use factory helpers to create complex collaborators
- And then some random weird advice:
	- “Use fixtures sparingly” - Now them’s fighting words. :)

**Sebastian #6:** [**Conference radar**](https://pypi.org/project/conference-radar/)

- The PyCon 2021 Call for Proposal acceptance emails will be sent soon, so let's talk about conferences.
- It's 2021, and just like the last year, most conferences are moving to an online format.
- Which is great, because it's so much easier to attend them. Not only the tickets got cheaper or even free, but you also don't have to pay for the accommodation, plane tickets and you don't have to actually fly anywhere.
- But how do you find what are the upcoming conferences? There is a list of conferences at python.org, but it doesn't have the smaller, local events, and you don't immediately see when each conference is taking place.
- I've found a tool called "conference radar" - a Python package that gives you a CLI tool to check for upcoming Python conferences!
- It prints a nice ASCII table with the dates of each conference. There are even some options that you can pass, for example, to see which conferences have an open Call for Proposal, in case you want to submit something. 
- The main downside is that plenty of conferences are not included there, but I hope that the list of sources will be expanded in the future. The CFP flag is also not working very well, I guess, because it's hard to parse the data sources and extract this information automatically.
- So far, my best way to stay on top of the open CFPs is to follow my friend Miroslav on Twitter.
- MK: Heads up on installation. They say you can `pip install conrad` but the actual command is `pip install conference-radar`

**Extras**

Michael

- Announcing Modern Python Projects course: [**talkpython.fm/modern-python-projects**](https://talkpython.fm/modern-python-projects)
- Now highlighting **live** livestreams on Python Bytes: [**pythonbytes.fm/stream/live**](https://pythonbytes.fm/stream/live)
- Mars again. Yes, **Python IS on Mars**. See [tweet](https://twitter.com/tjmcgrew/status/1370009196167626752).
- Signups for the Python Language Summit at PyCon (online only) [**are now open**](https://twitter.com/gvanrossum/status/1371563816786358274?cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email).

Sebastian

- I've started using VS Code in the browser (a new project for a new client), and it's surprisingly good! I would never try it myself (I love to have all my tools installed locally on my computer). The worst part? Learning to not click "Ctrl+W" when I want to close a tab in VS Code (as it closes the whole tab in my browser). I'm curious to see if it will ever become a standard in programming. It's definitely a great way to set up a standardized development platform for the whole team.

**Joke**: **[He has WiFi](https://trello-attachments.s3.amazonaws.com/6041d3e66056524cad8fd110/460x936/02ad871763c0031a1fab0ef4c57be88f/Screen_Shot_2021-03-04_at_10.35.54_PM.png)**


