# Python Bytes 41
Brought to you by **Rollbar**! Create an account and get special credits at https://pythonbytes.fm/rollbar

Guest co-host: [Miguel Grinberg](https://blog.miguelgrinberg.com/index)

**Miguel #1:** [**lolviz**](https://github.com/parrt/lolviz)

- Generates graphical representations of Python data structures using graphviz.
- Great as a teaching tool!
- Currently supports dicts, lists, lists of lists, linked lists and binary trees.
- Jupyter knows how to render these graphics. In regular Python it can also be used, but it is a bit cumbersome.
- I hope the project grows to support more complex data structures in the future!

**Michael #2:** [**Odo for data transforms**](https://odo.readthedocs.io/en/latest/overview.html)

- Odo migrates between many formats.

```
odo(df, list)  # create new list from Pandas DataFrame
odo(df, [])  # append onto existing list
odo(df, 'myfile.json')  # Dump dataframe to line-delimited JSON
odo('myfiles.*.csv', Iterator) # Stream through many CSV files
odo(df, 'postgresql://hostname::tablename')  # Migrate dataframe to Postgres
odo('myfile.*.csv', 'postgresql://hostname::tablename')  # Load CSVs to Postgres
odo('postgresql://hostname::tablename', 'myfile.json') # Dump Postgres to JSON
odo('mongodb://hostname/db::collection', pd.DataFrame) # Dump Mongo to DataFrame
```

**Miguel #3:** [**Python Concurrency From the Ground Up**](https://www.youtube.com/watch?v=MCs5OvhV9S4)

- This is probably my favorite tech talk of all times.
- There are no slides, the entire talk is a live coding session.
- David Beazley covers concurrency with threads and processes, and then goes on to build an asynchronous framework along the lines of asyncio just using generators, all in front of your eyes.
- If you spend 45 minutes watching this talk you’ll end up with a much better understanding of Python concurrency.

**Michael #4:** [**FAT Python : the next chapter in Python optimization**](https://hackernoon.com/fat-python-the-next-chapter-in-python-optimization-69dc974bcca2)

- via Anthony Shaw
- The FAT Python project was started by Victor Stinner in October 2015 to try to solve issues of previous attempts of “static optimizers” for Python.
- The PEPs
  - PEP 511 is a proposal to add a process to optimize an AST instance. The AST instance is a object-oriented representation of your code. 
  - A bespoke optimizer could look at a set of domain specific changes, e.g. NumPy or Pandas “anti-patterns” and optimize them in the syntax tree. In replacement of a static linter that simply recommends changes, the optimizer could make those changes for you.
  - PEP 509: Python is hard to optimize because almost everything is mutable: builtin functions, function code, global variables, local variables, … can be modified at runtime.
  - The speedup of optimizations depends on the speed of guard checks. PEP 509 proposes to add a private version to dictionaries to implement fast guards on namespaces.
  - PEP 510 proposes to add a public API to the Python C API to add specialized codes with guards to a function. When the function is called, a specialized code is used if nothing changed, otherwise use the original bytecode.
- Can download and compile this variation of CPython
- Basic function with a return is 24% improvement over 3.6 (and 46% faster than 2.7)
- Combining these 3 PEPs, we could see both implementation of guards as well as well as a range of optimizers out on PyPi.

**Miguel #5:** [**sshuttle**](http://sshuttle.readthedocs.io/)

- You probably know that there are security risks when going online at public wi-fi hotspots at coffee shops, hotels or airports.
- Most people don’t realize this, but even if you access sites over https://, DNS queries made to connect to those sites are not encrypted, so they give away which sites you visit.
- sshuttle is fantastic tool (written in Python, BTW) that creates a secure tunnel between your machine and another machine (which can be in a secure location such as your home or office) and forwards all network traffic through that other system with strong encryption. A poor man’s VPN!
- All you need to use sshuttle is SSH access to the secure system. No need to install anything on the remote system besides SSH!
- Simply run **sshuttle --dns --r username@your-server 0.0.0.0/0** and from then on all traffic will be tunneled to your secure server with strong encryption, including DNS queries!

**Michael #6:** [**Node.js forks again – this time it's a war of words over codes of conducts**](https://www.theregister.co.uk/2017/08/24/nodejs_forks_ayo_code_of_conduct/)

- After years of battling a string of systematic failures of governance and leadership, the Node.js community reached a breaking point.
- Monday saw a stream of resignations, one after the other throughout the day from Node.js' technical steering committee (TSC), a group that manages the day-to-day governance for the Node.js project.
- A third of the committee had quit their positions by the end of the day, including its first woman member.
- One person has left the project entirely.
- The resignations followed a single event -- a vote that failed to remove a former director, a longstanding member of the community, from the leadership group. Many of the complaints, since removed from the committee's pages, document a litany of violations of the community's code of conduct.
- The failure to have him removed from the position was seen as the embodiment of years of efforts to reform a pattern of harmful behaviors that was tearing the community apart.
- The inability for members of the TSC to "look at the entire picture" of a person's behavior rather than each broken rule is where trust in the system broke down, Kapke said.
- Moments after the failed leadership vote, Kat Marchán pushed the button that created Ayo.js, a new open-source project forked from Node.js.

**Our news**

Miguel: 

- [Blog](https://blog.miguelgrinberg.com) 
- [The New and Improved Flask Mega-Tutorial](https://www.kickstarter.com/projects/1124925856/the-new-and-improved-flask-mega-tutorial)

Michael: 

- [RESTful and HTTP APIs in Pyramid](https://training.talkpython.fm/courses/explore_restful_pyramid_course/creating-a-restful-http-api-with-pyramid-and-python-mega-course)

