# Python Bytes 78

Sponsored by Datadog: [https://pythonbytes.fm/datadog](https://pythonbytes.fm/datadog) 
Special guest: Kojo Idrissa -- [https://twitter.com/Transition](https://twitter.com/Transition)

Brian #1: [**The Forgotten Optional `else` in Python Loops**](https://medium.com/@s16h/the-forgotten-optional-else-in-python-loops-90d9c465c830)

- “Both for and while loops in Python also take an optional else suite (like the if statement and the try statement do), which executes if the loop iteration completes normally. In other words, the else suite will be executed if we don’t exit the loop in any way other than its natural way. So, no break statements, no return statement, or no exceptions being raised inside the loop.”
- Why? So you don’t have to invent a flag to indicate something wasn’t found if you are using the loop to search for something. 

Kojo #2:

-  [https://libraries.io/](https://libraries.io/)
	- Find out what your dependencies are!
	- Look into [https://tidelift.com/](https://tidelift.com/)

Michael #3: [The other (great) benefit of Python type annotations](https://medium.com/@shamir.stav_83310/the-other-great-benefit-of-python-type-annotations-896c7d077c6b)

- We've had type annotations for awhile
- When and why is sometimes unclear
	- Lack of types an issue sometimes, especially annoying while learning new APIs or diving into a new large codebase, and made me completely reliant on documentation.
	- Optional:
		- You can’t break the code by adding them
		- They have no effect performance-wise
		- You may add them only where you see fit
- Straightforward benefits
	- Employ static code analysis to catch type errors prior to runtime
	- Cleaner code/the code is self-documenting: “don’t use a comment when you can use a function or a variable”, we can now say “don’t use comments to specify a type, when you can use type annotation”
- The other benefit (it's massive!): Code completion

Brian #4: [**Setting Expectations for Open Source Participation**](https://www.youtube.com/watch?v=tzFWz5fiVKU&feature=youtu.be&t=48m55s)

- Or **Pay for Open Source with Kindness**
- Brett Cannon’s morning talk this last Sunday at PyCon 2018
- This talk (or a variation of it and it’s content) is essential material for anyone working with open source.
- Everything in open source has a cost whether it’s time, effort, or emotional output.
- Open source should be a series of unsolicited kindnesses.
- Be open, considerate, and respectful
- Remember most of this runs on volunteer time and that people have lives.
- Guidelines for communicating online:
	- Assume you are asking for a favor.
	- Assume your boss will read what you say.
	- Assume your family will read what you say.

Kojo #5:

-  Python Community Events
	- Michael and I (along with Trey Hunner) helped lead a New Attendee Orientation
	- Join your local Python community
	- Be kind to your fellow Pythonistas

Michael #6: [ngrok](https://ngrok.com/)

- ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels.
- Public URLs for testing on mobile devices, testing your chatbot, SSH access to your Raspberry Pi, sharing your local dev work on full stack web apps.
- Just a commandline away
- My use case: Course app development
- Features:
	- Secure Tunnels
	- Request Inspection
	- Fast (HTTP 2)

Extras and our news:

Michael:

- Live recording video is out: [https://youtu.be/s9uUSQvrIaE](https://youtu.be/s9uUSQvrIaE)
- Now up to 8 video servers around the world, Japan, Sao Paulo, and Mumbai are the latest. Based on the systemd thing we discussed way back when ([episode 54](https://pythonbytes.fm/episodes/show/54/pyannotate-your-way-to-the-future))



