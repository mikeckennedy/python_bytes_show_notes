# Python Bytes 77
Sponsored by Datadog: [**pythonbytes.**](https://pythonbytes.fm/datadog)[**fm**](https://pythonbytes.fm/datadog)[**/datadog**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Why Senior Devs Write Dumb Code**](https://hackernoon.com/why-senior-devs-write-dumb-code-and-how-to-spot-a-junior-from-a-mile-away-27fa263b101a)

- “*Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” - Kent Beck*
- Code that is clean, straightforward, obvious, and easy to read actually takes practice to achieve.
- Follow principles like YAGNI, Singe Responsibility, DRY, etc.
- Avoid clever one-liners, weird abstractions.
- Esoteric language features.
- Code needs to be readable and easily understood while under time and stress pressure.

**Michael #2:** [GeoAlchemy 2](https://geoalchemy-2.readthedocs.io/en/latest/)

- GeoAlchemy 2 provides extensions to SQLAlchemy for working with spatial databases.
- GeoAlchemy 2 focuses on PostGIS. Aims to be simpler than its predecessor, GeoAlchemy.
- Using it:
  - Connect (e.g. Postgres)
  - Declare a Mapping
```
    class Lake(Base):
         __tablename__ = 'lake'
         id = Column(Integer, primary_key=True)
         name = Column(String)
         geom = Column(Geometry('POLYGON'))
```
  - Create a table (via the engine)
  - Create an Instance of the Mapped Class
  - Inserts like standard SQLAlchmey
  - Spatial Query
```
    from sqlalchemy import func
    query = session.query(Lake).filter(
             func.ST_Contains(Lake.geom, 'POINT(4 1)'))
             
    query = session.query(Lake.name,
          Lake.geom.ST_Buffer(2).ST_Area().label('bufferarea'))
```

**Brian** **#3:** [**QtPyConvert**](https://github.com/digitaldomain/QtPyConvert)

- An automatic Python Qt binding transpiler to the Qt.py abstraction layer.
- QtPyConvert supports the following bindings out of the box:
	- [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)
	- [PySide](http://pyside.github.io/docs/pyside/)
	- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
	- [PySide2](https://wiki.qt.io/PySide2)
- Conversions leave code comments in place, with the help of RedBaron
- Converts to [Qt.py](https://github.com/mottosso/Qt.py)
	- Minimal Python 2 & 3 shim around all Qt bindings - PySide, PySide2, PyQt4 and PyQt5
	
**Michael #4:**  [You Don't Have To Be a Workaholic To Win: 13 Alternative Ways To Stand Out](https://www.kevinball.com/2018/04/17/you-dont-have-to-be-a-workaholic/)

- Do we have to kill ourselves to get ahead?
- Don’t busy-brag
- Max Q analogy
- The tips
1. Creativity
2. Stubbornness
3. Curiosity
4. Kindness
5. Planning
6. Improvisation
7. Enthusiasm
8. Communication
9. Presence
10. Collaboration
11. Willingness
12. Patience
13. Institutional Knowledge

**Brian** **#5:** [**RedBaron**](https://github.com/PyCQA/Redbaron)

- RedBaron is a python library to make the process of writing code that modify source code as easy and as simple as possible. 
  - writing custom refactoring, generic refactoring, tools, 
- Used by QtPyConvert to achieve the conversion while leaving code comments in place
- Uses the full syntax tree, FST. Like an AST, but keeps all information, including comments and formatting.
- possible uses:
	- rename a variable in a source file... without clashing with things that are not a variable (example: stuff inside a string)
	- inline a function/method
	- extract a function/method from a series of line of code
	- split a class into several classes
	- split a file into several modules
	- convert your whole code base from one ORM to another
	- do custom refactoring operation not implemented by IDE

**Michael #6:**  [Project Beeware AppStore](https://no-title.victordomingos.com/articles/2018/project_beware_launches_app_for_ios/)

- Project BeeWare has just released its first iPhone app made in Python using its Briefcase tool.
- Simple travel app for currency and tip calculations
- Briefcase: A distutils extension to assist in packaging Python projects as standalone applications.
  Briefcase is a tool for converting a Python project into a standalone native application. You can package projects for:
	- Mac
	- Windows
	- Linux
	- iPhone/iPad
	- Android
	- AppleTV
	- tvOS
- While there are other Python GUI toolkits aiming to enable Python developers to build and deploy iOS apps, like for instance the very nice [Pythonista app](http://omz-software.com/pythonista/), the [BeeWare](https://pybee.org) project is a bit different because it aims at cross-platform compatibility and native widgets with a set of different tools, like Briefcase and Toga.

Extras: 

- Michael: Extra ssh breach Did you see that?  [https://www.reddit.com/r/Python/comments/8hvzja/backdoor_in_sshdecorator_package/](https://www.reddit.com/r/Python/comments/8hvzja/backdoor_in_sshdecorator_package/)
- PyCon videos already up at [https://www.youtube.com/pycon2018](https://www.youtube.com/pycon2018)

