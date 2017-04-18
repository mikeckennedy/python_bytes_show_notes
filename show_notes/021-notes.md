# Python Bytes 21
This episode has been **sponsored by Rollbar**. Get a special offer via [http://rollbar.com/pythonbytes](http://rollbar.com/pythonbytes)

**#1 Brain:** [**profile and pstats — Performance Analysis**](https://pymotw.com/3/profile/)

- Doug Hellman is working on the Python 3 MOTW series that was so successful for Python 2.
- Recent edition is profile and pstats, for profiling parts of your code you may have concerns with and finding out where the slow bits are.

**#2 Michael:** [**API Star by Tom Christie**](https://github.com/tomchristie/apistar)

- A smart Web API framework, designed for Python 3.
- A few things to try right away:
```
    $ pip3 install apistar
    $ apistar new --template minimal
    $ apistar run
    $ apistar test
```
- API Star allows you to dynamically inject various information about the incoming request into your views using type annotation.
  - e.g. 
```
    def show_query_params(query_params: http.QueryParams):
        return {
            'params': dict(query_params)
        }
```
- You can instead set the status code or headers by annotating the view as returning a Response
```    def create_project() -> Response: ...```
- Parameters are automatically passed into views from routes (annotations!):
```
    def echo_username(user_id: int):
        return {'message': f'Welcome, user {user_id}!'}
```
- Performance: Faster than sanic!

**#3 Brain:** [**Yes, Python is Slow, and I Don’t Care**](https://hackernoon.com/yes-python-is-slow-and-i-dont-care-13763980b5a1)

- Optimize for your most expensive resource. That’s **YOU**, not the computer.
- Choose a language/framework/architecture that helps you develop quickly (such as Python). Do not choose technologies simply because they are fast.
- When you do have performance issues: find your bottleneck
- Your bottleneck is most likely not CPU or Python itself.
- If Python **is** your bottleneck (you’ve already optimized algorithms/etc.), then move the hot-spot to Cython/C
- Go back to enjoying getting things done quickly

**#4 Michael:** [**A Quick Introduction: Hashing**](https://hackernoon.com/a-quick-introduction-hashing-c32d1dc91871)

- Article by Gerald Nash
- Hashing is a method of determining the equivalence of two chunks of data. 
- A cryptographic hash function is an irreversible function that generates a unique string for any set of data.
-  Example
```
    import hashlib as hash
    sha = hash.sha256()
    # Insert the string we want to hash
    sha.update('Hello World!')
    # Print the hexadecimal format of the binary hash we just created
    print(sha.hexdigest())
    # 4d3cf15aa67c88742e63918825f3c80f203f2bd59f399c81be4705a095c9fa0e
```
- Know when to choose “weak” hashes vs. strong ones
- Straight hashes are not enough for security (e.g. passwords). Use passlib and be done.

**#5 Brain:** [**Wedding at Scale: How I Used Twilio, Python and Google to Automate My Wedding**](https://www.twilio.com/blog/2017/04/wedding-at-scale-how-i-used-twilio-python-and-google-to-automate-my-wedding.html)

- gspread to access a google spreadsheet of guests and phone numbers
- SMS guests with twilio
- replies handled by a flask app
- gathered accept/decline/didn't reply statistics
- reminder texts
- food selections and replies and reminders, all handled by Python


**# 6 Michael:** [**python-alexa: A Python framework for Alexa Development**](https://blog.njsnet.co/python-alexa)

- by Neil Stewart
- Ordered an amazon assistant.
- Before it arrived, I had challenged myself to develop something for it
- Project: VoiceOps, interact with an AWS account, such as telling me how many running and stopped instances there is or what RDS databases are in an account
- Wanted a framework that would make Alexa development super easy.
- Decided a new framework was needed: python-alexa
- [python-alexa on github](https://github.com/nmyster/python-alexa)
- [echo shim](https://echosim.io/) for testing without hardware

**Our news:**

**Michael**: Just added [full text search](https://training.talkpython.fm/search) (including within videos) to Talk Python courses.

**Brian:** [Netflix chaos engineering interview on Test & Code](http://testandcode.com/28)

