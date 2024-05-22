# Python Bytes 52

Sponsored by DigitalOcean. They just launched Spaces, get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Brian #1:** [**Restful API testing**](https://taverntesting.github.io/) [**with Tavern**](https://taverntesting.github.io/)

**Michael #2:** [**Uplink**](https://uplink.readthedocs.io/en/latest/)

- RESTful client API via decorators
- Create a class to represent the API
- Add methods with arguments, map to API calls.
- e.g.  
```python
    @get("/users/{username}")
    def get_user(self, username):
       """Get a single user."""        
```
- Uplink includes support for concurrent requests with asyncio (for Python 3.4+) 
- Twisted (for all supported Python versions)
- Not production ready, but very exciting.

**Brian #3:** [**Using json-schema for REST API endpoint tests**](https://engineering.ticketea.com/using-json-schema-for-rest-api-endpoint-tests/)

**Sponsor DIGITAL OCEAN SPACES**
Get started today with a free 2 month trial of Spaces by going to [**do.co/python**](https://do.co/python)

**Michael #4:** [**Live coding to music!**](https://twitter.com/watty62/status/923945051616698369)

- via Ian Watt
- Talk at PyCon UK by Ryan Kirkbride called “Programming Music for Performance: Live coding with FoxDot”

**Brian #5:** [**Weekly Python Chat**](http://www.weeklypython.chat/)


**Michael #6:**  [**10 common beginner mistakes in Python**](https://py.checkio.org/blog/10-common-beginner-mistakes-in-python/)

- Via checkIO:  https://py.checkio.org/


1. Incorrect indentation, tabs and spaces
2. Using a Mutable Value as a Default Value
3. Write a lot of comments and docstrings
4. Scoping
5. Edge cases first (let’s go easy on the indents)
6. Copying
7. Creating count-by-one errors on loops (range is half closed)
8. Wrong capitalization
9. Using class variables incorrectly

**Our news**

Michael: 

- Flash briefing?
- Firefox Quantum!