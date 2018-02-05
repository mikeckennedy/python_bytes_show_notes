# Python Bytes 63
Sponsored by DigitalOcean: **[http://do.co/python](http://do.co/python)**

**Brian #1:** [**A brief tour of Python 3.7 data classes**](https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517)

- a great write-up of the upcoming data classes via Anthony Shaw
- “Data classes are a way of automating the generation of boiler-plate code for classes which store multiple properties. They also carry the benefit of using Python 3’s new type hinting.”
- Default magic methods
	- In the default setting, any dataclass will implement `__init__`, `__repr__`, `__str__` and `__eq__` for you.
	- The `__init__` method will have **keyword-arguments** with the same type annotations that are specified on the class.
	- The `__eq__` method will compare all dataclass attributes in order.
	- All fields are declared at the top of the class and type hinting is **required**.
- Also covered
	- type hinting
	- mutability (and frozen)
	- customizing the fields
	- post-init processing : optional `__``*post_init_*``_` will run after the generated `_``*_init_*``_`
	- inheritance

**Michael #2:** SQLite [The Databaseology Lectures - CMU Fall 2015]

-  Lots of DBs covered here: **[http://db.cs.cmu.edu/seminar2015/](http://db.cs.cmu.edu/seminar2015/)**
- SQLite at this [**YouTube video**](https://www.youtube.com/watch?v=gpxnbly9bz4&index=2&list=PLSE8ODhjZXjakeQR57ZdN5slUu2oPUr1Y)

**Brian #3:** [**dryable**](https://haarcuba.github.io/dryable/) [**:**](https://haarcuba.github.io/dryable/) [**a useful dry-run decorator for python**](https://haarcuba.github.io/dryable/)

- short circuit methods within your project during dry runs.
- example shows how to add a command line flag `--dry-run`.
- The test code is useful for understanding it also.
- Example something.py
    import dryable
    
    @dryable.Dryable('foo')
    def return_something():
        return 'something'

test_something.py

    from something import return_something
    import dryable
    
    def test_normal_return():
        dryable.set(False) 
        assert return_something() == 'something'
    
    def test_dry_return(capsys):
        dryable.set(True) 
        assert return_something() == 'foo'


**Michael #4:** 

- These are some pretty cool examples.
	- [https://github.com/victordomingos/PT-Tracking/](https://github.com/victordomingos/PT-Tracking/)
	- [https://github.com/victordomingos/RepService/](https://github.com/victordomingos/RepService/)
	- [https://github.com/victordomingos/ContarDinheiro.py](https://github.com/victordomingos/ContarDinheiro.py)

**Brian #5:** [**PEP Explorer - Explore Python Enhancement Proposals**](https://tonybaloney.github.io/pep-explorer/#)

- Cool idea. Might need some work though. I can’t find any accepted PEPs for 3.7, including [557, data classes](https://www.python.org/dev/peps/pep-0557/).
- I’m ok with giving Anthony some shade on this, as we highlighted his writing in the first item.

**Michael #6:** [**TKInter Tutorial**](https://likegeeks.com/python-gui-examples-tkinter-tutorial/)

- via @likegeeks
- Create your first GUI application
- Create a label and button widgets
- Input and combo boxs, menus, progressbars and more

## Our news

Michael

- I built something with [Gooey](https://github.com/chriskiehl/Gooey) this weekend, it was wonderful.
- Self-serve team purchases and discounts at Talk Python Training

