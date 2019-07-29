# Python Bytes 140
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Becoming a 10x Developer : 10 ways to be a better teammate**](https://www.kateheddleston.com/blog/becoming-a-10x-developer)

- Kate Heddleston
- “A 10x engineer isn’t someone who is 10x better than those around them, but someone who makes those around them 10x better.”
	1. Create an environment of psychological safety
	2. Encourage everyone to participate equally
	3. Assign credit accurately and generously
	4. Amplify unheard voices in meetings
	5. Give constructive, actionable feedback and avoid personal criticism
	6. Hold yourself and others accountable
	7. Cultivate excellence in an area that is valuable to the team
	8. Educate yourself about diversity, inclusivity, and equality in the workplace
	9. Maintain a growth mindset
	10. Advocate for company policies that increase workplace equality
- article includes lots of actionable advice on how to put these into practice.
- examples: 
	- Ask people their opinions in meetings.
	- Notice when someone else might be dominating a conversation and make room for others to speak.

**Michael #2**:** **quasar & vue.py**

- via Doug Farrell
- [**Quasar**](https://quasar.dev/) is a Vue.js based framework, which allows you as a web developer to quickly create responsive++ websites/apps in many flavours:
	- SPAs (Single Page App)
	- SSR (Server-side Rendered App) (+ optional PWA client takeover)
	- PWAs (Progressive Web App)
	- Mobile Apps (Android, iOS, …) through Apache Cordova
	- Multi-platform Desktop Apps (using Electron)
- Great for python backends
- tons of vue components
- But could it be all python?
	- vue.py provides Python bindings for [Vue.js](https://www.vuejs.org). It uses [brython](https://github.com/brython-dev/brython) to run Python in the browser.
	- Examples can be found [here](https://stefanhoelzl.github.io/vue.py/examples). 

**Brian #3:** [**Regular Expressions 101**](https://regex101.com/) 

- We talked about regular expressions in [episode 138](https://pythonbytes.fm/138)
- Some tools shared with me after I shared a regex joke on twitter, including this one.
- build expressions for Python and also PHP, JavaScript, and Go
- put in an example, and build the regex to match
- explanations included
- match information including match groups and multiple matches
- quick reference of all the special characters and what they mean
- generates code for you to see how to use it in Python
- Also fun (and shared from twitter):
	- [Regex Golf](https://alf.nu/RegexGolf)
		- see how far you can get matching strings on the left but not the list on the right.
			- I got 3 in and got stuck. seems I need to practice some more

**Michael #4:** [**python-diskcache**](https://github.com/grantjenks/python-diskcache)

- Caching can be HUGE for perf benefits
- But memory can be an issue
- Persistence across executions (e.g. web app redeploy) an issue
- Servers can be issues themselves
- Enter the disk! Python disk-backed cache (Django-compatible). Faster than Redis and Memcached. Pure-Python.
- DigitalOcean and many hosts now offer SSD’s be default
- Unfortunately the file-based cache in Django is essentially broken.
- DiskCache efficiently makes gigabytes of storage space available for caching. 
	- By leveraging rock-solid database libraries and memory-mapped files, cache performance can match and exceed industry-standard solutions. 
	- There's no need for a C compiler or running another process. 
	- Performance is a feature 
	- Testing has 100% coverage with unit tests and hours of stress.
- Nice comparison chart

**Brian #5:** [**The Python Help System**](https://stackabuse.com/the-python-help-system/)

- Overview of the built in Python help system, `help()`
- examples to try in a repl
	- `help(print)`
	- help(dict)
	- `help('assert')`
	- `import math; help(math.log)`
- Also returns docstrings from your non-built-in stuff, like your own methods.

**Michael #6:** **Python Architecture Graphs**

- by David Seddon
-  [Impulse](https://impulse-cli.readthedocs.io/) - a CLI which allows you to quickly see a picture of the import graph any installed Python package at any level within the package.
- Useful to run on an unfamiliar part of a code base, to help get a quick idea of the structure. 
- It's a visual explorer to give you a quick signal on architecture.
- [Import Linter](https://seddonym.me/2019/05/20/meet-import-linter/) - this allows you to declare and check contracts about your dependency graph, which gives you the ability to lint your code base against architectural rules. 
- Helpful to enforce certain architectural constraints and prevent circular dependencies creeping in.

**Extras**

Michael:

- [tabnanny](http://effbot.org/librarybook/tabnanny.htm)
- flask course is out, give it [a look](https://training.talkpython.fm/courses/explore_flask/building-data-driven-web-applications-in-python-with-flask-sqlalchemy-and-bootstrap)
    

**Jokes** 

Two threads walk into a bar. The barkeeper looks up and yells, 'Hey, I want don't any conditions race like time last!’

A string value walked into a bar, and then was sent to stdout.
