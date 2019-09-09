# Python Bytes 146
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

Special guest: Trey Hunner

**Brian #1:** [**Positional-only arguments in Python**](https://deepsource.io/blog/python-positional-only-arguments/)

- by Sanket
- Feature in 3.8
- “To specify arguments as positional-only, a `/` marker should be added *after* all those arguments in the function definition. “
- Great example of a `pow(x, y, /, mod=None)` function where the names `x` and `y` are meaningless and if given in the wrong order would be confusing. 

**Trey #2:** [**django-stubs**](https://sobolevn.me/2019/08/typechecking-django-and-drf)

- Type checking for Django!
- It’s new and from my very quick testing on my Django site it definitely doesn’t work with everything yet, but it’s promising
- I don’t use type annotations in Django yet, but I very well might eventually

**Michael #3:** [**CodeCombat**](https://codecombat.com)

- Super fun game for learning to code
- *Real* code but incredibly easy coding
- Can subscribe or use the free tier
- Just got [$6M VC funding](https://app.getpocket.com/read/2706624094?src=fx_new_tab)

**Brian #4:** [**Four Use Cases for When to Use Celery in a Flask Application**](https://nickjanetakis.com/blog/4-use-cases-for-when-to-use-celery-in-a-flask-application)

- or really any web framework
- by Nick Janetakis
- “Celery helps you run code asynchronously or on a periodic schedule which are very common things you'd want to do in most web projects.”
- examples:
	- sending emails out
	- connecting to 3rd party APIs. 
	- performing long running tasks. Like, really long. 
	- Running tasks on a schedule. 

**Trey #5:** [**pytest-steps**](https://smarie.github.io/python-pytest-steps/#2-usage-explicit-mode)

- Created by smarie
- Can use a generator syntax with yield statements to break a big test up into multiple named “steps” that’ll show up in your pytest output
- If one step fails, the rest of the steps will be skipped by default
- You can also customize it to make optional steps, which aren’t required for future steps to run, or steps which depend on other optional steps explicitly
- The documentation shows a lot of different ways to use it, but the generator approach looks by far the most readable to me (also state is shared between steps with this approach whereas the others require some fancy state-capturing object which looks confusing to me)
- I haven’t tried this, but my use case would be my end-to-end/functional tests, which would work great with steps because I’m often using Selenium to navigate between a number of different pages and forms, one click at a time.

**Michael #6:** [**docassemble**](https://docassemble.org/)

- Created by Jonathan Pyle
- A free, open-source expert system for guided interviews and document assembly, based on Python, YAML, and Markdown.
- Features
	1. WYSIWYG: Compose your templates in [](https://docassemble.org/docs/documents.html#docx%20template%20file)[.docx](https://docassemble.org/docs/documents.html#docx%20template%20file) (with help of a [](https://docassemble.org/docs/playground.html#word%20addin)[Word Add-in](https://docassemble.org/docs/playground.html#word%20addin)) or [](https://docassemble.org/docs/documents.html#pdf%20template%20file)[.pdf](https://docassemble.org/docs/documents.html#pdf%20template%20file) files.
	2. Signatures: Gather touchscreen signatures and embed them in documents.
	3. Live chat: Assist users in real time with live chat, screen sharing, and remote screen control.
	4. AI: Use machine learning to process user input.
	5. SMS: Send text messages to your users
	6. E-mail: Send and receive e-mails in your interviews.
	7. OCR: Use optical character recognition to process images uploaded by the user.
	8. Multilingual: Offer interviews in multiple languages.
	9. Multiuser: Develop applications that involve more than one user, such as mediation or counseling interviews.
	10. Extensible: Use the power of Python to extend the capabilities of your interviews.
	11. Open: Package your interviews and use GitHub and PyPI to share your work with the docassemble user community.
	12. Background Tasks: Do things behind the scenes of the interview, even when the user is not logged in.
	13. Scalable: Deploy your interviews on multiple machines to handle high traffic.
	14. Secure: Protect user information with server-side encryption, two-factor authentication, document redaction, and other security features.
	15. APIs: Integrate with third-party applications using the API, or send your interviews input and extract output using code.

**Extras**

Michael:

- [PyPI closes in on 200k](https://twitter.com/raymondh/status/1163267960040853506)
- [NumPy 1.17.0 released](https://www.mail-archive.com/numpy-discussion@python.org/msg03276.html)
- [Python 3.8.0b4 is out](https://www.python.org/downloads/release/python-380b4/)

**Joke**

via Avram Lubkin

Knock! Knock!
Who's there?
Recursive function.
Recursive function who?
Knock! Knock!

Nice. to get that joke, you’ll have to understand recursion. 
to understand recursion, 

- either google “recursion”, and click on “did you mean “recursion””
- learn it in small steps. step one, recursion

text conversation:

- first person: “Hey, what’s your address?”
- second: <gives IP address>
- first: “No. Your local address”
- second: 127.0.0.1
- first: “No. Your physical address”
- second: <gives MAC address>


