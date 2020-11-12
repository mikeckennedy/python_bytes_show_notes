# Python Bytes 207

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Michael #1:** [**fastapi-chameleon**](https://twitter.com/mkennedy/status/1320769596832374785) **(and** [**fastapi-jinja**](https://twitter.com/AGeekInside/status/1320926762377904129)**)**

- Chameleon via Michael, Jinja via Marc Brooks
- Convert a FastAPI API app to a proper web app
- Then just decorate the FastAPI view methods (works on sync and async methods):

```
    @router.post('/')
    @fastapi_chameleon.template('home/index.pt')
    async def home_post(request: Request):
        form = await request.form()
        vm = PersonViewModel(**form) 
    
        return vm.dict() # {'first':'Michael', 'last':'Kennedy', ...}
```

- The view method should return a `dict` to be passed as variables/values to the template.
- If a `fastapi.Response` is returned, the template is skipped and the response along with status_code and other values is directly passed through. This is common for redirects and error responses not meant for this page template.


**Brian #2:**  [**Django REST API in a single file, without using DRF**](https://adamj.eu/tech/2020/10/15/a-single-file-rest-api-in-django/)

- Adam Johnson
	- He’s been on Test & Code a couple times, [128](https://testandcode.com/128) & [135](https://testandcode.com/135)
- Not sure if you should do this, but it is possible.
- Example Django app that is a REST API that gives you information about characters from Rick & Morty. Specifically, just Rick and Morty.
	- / - redirects to /characters/
	- /characters/ - returns a JSON list
	- /characters - redirects to /characters/
	- /characters/1  - returns JSON info about Rick
	- /characters/2 - same, but for Morty
- Shows off how with Django off the shelf, can do redirects and JSON output.
- Shows data using dataclasses. Hardcoded here, but easy to see how you could get this data from a database or other part of your system.

**Michael #3:** [**2020 StackOverflow survey results**](https://insights.stackoverflow.com/survey/2020)

- Most Popular Technologies
- Languages: JavaScript (68%), Python (44%), Java(40%)
- Web frameworks: Just broken, jQuery? Seriously!?!
- Databases: MySQL (56%), PostgreSQL (36%), Microsoft SQL Server (33%), MongoDB (26%)
- Platforms: Windows (46%), macOS (28%), Linux(27%)
- Most loved languages: Rust, TypeScript, Python
- Most wanted languages: Python, JavaScript, Go
- Most dreaded language: VBA & ObjectiveC
- Most loved DBs: Redis (67%), PostgreSQL (64%), Elasticsearch (59%), MongoDB (56%)
- Most wanted DBs: MongoDB (19%), PostgreSQL (16%)
- Most dreaded DB: DB2

**Brian #4:**  [**A Visual Guide to Regular Expression**](https://amitness.com/regex/)

- Amit Chaudhary
- Gentle introduction to regex by building up correct mental models using visual highlighting.
- Goes through different patterns:
	- specific character
	- white space (any whitespace \s, tab \t, newline \n)
	- single-digit number \d
	- word characters \w : lowercase, uppercase, digits, underscore
		- this sometimes throws me, since w seems like it might somehow be related to whitespace. It’s not.
	- dot . : anything except newline
	- pattern negations:
    - \d is digits, \D is anything that is not a digit
    - \s whitespace, \S not whitespace
    - \w word characters, \W everything else
	- character sets with square brackets [], and optionally dash - for range
	- anchors
    - ^ beginning of line
    - $ end of line
	- escaping patterns with \
	- repetition with {}, *, +, ?
- Using Python re module
	- findall
	- match and match.group
	- search

**Michael #5:** [**Taking credit**](https://twitter.com/tim_nolet/status/1317061818574082050)

- by [Tim Nolet](https://twitter.com/tim_nolet)
- Oh [@awscloud](https://twitter.com/awscloud) I really do love you! But next time you fork my OS project [https://github.com/checkly/headless-recorder](https://t.co/6MCUyRxxYv?amp=1) and present it as your new service, give the maintainers a short "nice job, kids" or something. 
- Not necessary as per the APLv2 license, but still, ya know?
- Amazon CloudWatch Synthetics launches Recorder to generate user flow scripts for canaries
- A Chrome browser extension, to help you create canaries more easily.

**Brian #6:**  [**Raspberry Pi 400**](https://www.raspberrypi.org/products/raspberry-pi-400/?resellerType=home&variant=raspberry-pi-400-us-kit)

- “complete personal computer, built into a compact keyboard”
- by itself, or as a kit with mouse and power adapter and cables and such, for $100
- 4 core, 64-bit processor, 4 GB RAM, wifi & LAN, can drive 2 displays, 4K video
- 40-pin GPIO header, so you can still play with hardware and such.
- There’s an [adafruit video with Limor Fried](https://www.youtube.com/watch?v=OtotErWPEA8&feature=youtu.be) where she describes this as something as close as we get today to an Apple IIe from my youth.
- For me, IIe was at school, at home I had a TRS80 plugged into an old TV and using my sisters tape deck for disk storage.
- This seems great for education use, but also as a second computer in your house, or a kids computer.  
- Comes with a Beginner’s Guide that includes getting started with Python

Extras:

Brian: 

-  [vim-adventures.com](https://vim-adventures.com/) - with a dash. Practice vim key bindings while playing an adventure game. Super cool. 

Michael:

-  [TIOBE Index for November 2020](https://www.tiobe.com/tiobe-index/) via Tyler Pedersen

Joke:

**[You built it, you run it.](http://geek-and-poke.com/geekandpoke/2019/10/4/you-build-it-you-run-it)**
