# Python Bytes 48

Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1:**  [**The Python Graph Gallery**](https://python-graph-gallery.com/)

- “cool graphs” x “head explodes with options”

**Michael #2:** [**pynesis**](https://github.com/ticketea/pynesis)

- High level python library for using kinesis streams
- What are Kinesis streams? [AWS Kinesis streams](http://Amazon Kinesis Streams)
	- Enables you to build custom applications that process or analyze [streaming data](https://aws.amazon.com/streaming-data/) for specialized needs.
	- Continuously capture and store terabytes of data per hour from hundreds of thousands of sources such as website clickstreams, financial transactions, social media feeds, IT logs, and location-tracking events.
    
- High level kinesis client. Support python 2.7 and 3.6, and has helpers for using it within Django.
- Some features:
	- Supports python 2 & 3
	- Django helpers included
	- Automatically detects shard count changes
	- Checkpoints/sequences persistence can be customized
	- Provided Checkpointer implementations for memory, django model and redis
	- Provided Dummy kinesis implementation for development/testing

**Brian #3:**  [**Things you need to know about garbage collection in Python**](https://rushter.com/blog/python-garbage-collector/)

**Michael #4: WSGI Is Not Enough Anymore,** [**part 1**](https://medium.com/@amitn241/wsgi-is-not-enough-anymore-part-i-bc9713a79841) **and** [**part 2**](https://medium.com/@amitn241/wsgi-is-not-enough-anymore-part-ii-b78b4cfdd09)

- Explores the factors that make WSGI a less attractive option for developing web applications with Python.
- Most major web frameworks use WSGI (Pyramid, Flask, Django, Bottle, etc.)
- This has been a major benefit / breakthrough
- The Web Server Gateway Interface (WSGI) is a [specification](https://www.python.org/dev/peps/pep-3333/) which was first developed in 2003, and then revised in 2010, in order to create a standard for Python web frameworks to interact with web servers.
- The bad news is that WSGI comes with two major drawbacks:
	- WSGI compatible servers are synchronous
	- WSGI compatible servers only supports the HTTP protocol
- Problem 1:  Concurrency
	- By design, a WSGI server is synchronous. This means it blocks each request until a response arrives from the application.
	- Scaling is done necessarily via threads (with GIL limitations), web gardens (multiple processes per server), and web farms (multiple servers)
- Problem 2: HTTP is the only protocol
	- HTML5 introduced, among other things, web sockets, which create a bi-directional communication layer between servers and clients.
	- But they are not supported, so polling (yuck) is the only option
	- Python frameworks which rely on WSGI do not implement web socket communication and must rely on 3rd party solutions and extra components and resources.
- Part 2 discusses solutions via event driven programming
- Part 3 (pending) talks about libraries for solving the concurrent problem in Python

**Brian #5:**  [**Queues in Python**](https://dbader.org/blog/queues-in-python)

- Dan Bader
- I was in search of a LIFO queue and ran across this article by Dan.
- For LIFO:
```
    ### collections.deque as LIFO queue
    q = collections.deque()
    
    # insert elements
    q.appendleft(item)
    
    #iterate
    for item in q:
        print(item)
    
    ### queue.LifoQueue
    q = queue.LifoQueue()
    
    # insert elements
    q.put(item)
    
    #iterate
    while not q.empty():
        item = q.get()
        print(item)
    
    ### list as LIFO queue
    q = []
    
    # insert elements
    q.append(item)
    
    #iterate
    for item in q[::-1]:
        print(item)
```

**Michael #6:** [**Using Reflection: A Podcast About Humans Engineering**](https://www.podsheets.com/p/using-reflection/#/)

- by Mark Weiss
- Check out Jesse Davis’s [episode for a starter](https://www.podsheets.com/p/using-reflection/#/episode/A.-Jesse-Jiryu-Davis).
- Engineering journey, what they value about engineering and skills they have come to recognize in themselves.
- Dig into what makes teams successful, and how we help them succeed.

## Our news

- Michael: Free MongoDB course has had over 5,000 signups in the first few days. Check it out **[http://freemongodbcourse.com](http://freemongodbcourse.com)** 

