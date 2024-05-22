# Python Bytes 285

Sponsored: [**RedHat: Compiler Podcast**](https://pythonbytes.fm/compiler)

Special guest: 

- Mark Little
- Ben Cosby

**Michael #1:** [**libgravatar**](https://libgravatar.readthedocs.io/en/latest/)

- A library that provides a Python 3 interface to the Gravatar APIs.
- If you have users and want to show *some* sort of an image, Gravatar is OK
- PyPI uses this for example (gravatar, not necessarily this lib)

Usage:

    >>> g = Gravatar('myemailaddress@example.com')
    >>> g.get_image()
    'https://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

**Brian #2:** [**JSON to Pydantic Converter**](https://jsontopydantic.com/)

- [Suggested by Chun Ly](https://twitter.com/astrochunly/status/1523745834940067840?s=20&t=nJGxm1vQ_4DyIRD5QSHKVg), “this awesome JSON to [@samuel_colvin](https://twitter.com/samuel_colvin)'s pydantic is so useful. It literally saved me days of work with a complex nested JSON schema.“
- “JSON to Pydantic is a tool that lets you convert JSON objects into Pydantic models.”
- It’s a live site, where you can plop JSON on one the left, and Pydantic models show up on the right.
- There’s a couple options:
    - Specify every field as Optional
    - Alias camelCase fields as snake_case
- It’s also [an open source project](https://github.com/brokenloop/jsontopydantic), built with FastAPI, Create React App, and a project called [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator).

**Mark** **#3:** [**tailwindcss**](https://tailwindcss.com/)**,** [**tailwindui**](https://tailwindui.com/)

- Not python, but helpful for web UI and open source business model example
- tailwindcss generates CSS 
- Used on the **[Lexchart app](https://lexchart.com)**
- Benefits of tailwindcss and tailwindui:
    - Just-in-Time makes it fast. Output includes only classes used for the project.
    - Stand on shoulders of design thinking from [Steve Schoger](https://www.steveschoger.com/) and Adam Wathan. See also [refactoingui.com](https://www.refactoringui.com/).
    - Use in current projects without CSS conflicts. [Custom namespace with](https://www.youtube.com/watch?v=oG6XPy1t1KA) [**prefix**](https://www.youtube.com/watch?v=oG6XPy1t1KA) in tailwind.config.js. Bonus: custom namespace prefixes work with the tailwind plug-ins for VS Code and PyCharm.
    - Works well with template engines like, Chameleon. We use tailwind for our app UI. Toolbar template example.
    - Another example of docs and tutorials being a strategic business asset.
- Resources
    - [tailwindcss.com](https://tailwindcss.com/docs/installation)
    - [tailwindlabs](https://www.youtube.com/c/TailwindLabs) on YouTube, great tutorials from Simon at Tailwind
    - Beginner friendly tutorials: [Thirus, example of tailwind install methods](https://www.youtube.com/watch?v=h9Zun41-Ozc&t=1s)


**Michael #4:** [**PEP 690 – Lazy Imports**](https://peps.python.org/pep-0690/)

- From Itamar
- Discussion at https://discuss.python.org/t/pep-690-lazy-imports/15474
- PEP proposes a feature to transparently defer the execution of imported modules until the moment when an imported object is used.
- PEP 8 says imports go a the top, that means you pay the full price of importing code
- This means that importing the main module of a program typically results in an immediate cascade of imports of most or all of the modules that may ever be needed by the program.
- Lazy imports also mostly eliminate the risk of import cycles or crashes.
- The implementation in this PEP has already [demonstrated](https://github.com/facebookincubator/cinder/blob/cinder/3.8/CinderDoc/lazy_imports.rst) startup time improvements up to 70% and memory-use reductions up to 40% on real-world Python CLIs.

**Brian #5:** **Two small items**

- [**pytest-rich**](https://github.com/nicoddemus/pytest-rich)
    - Suggested by Brian Skinn
    - Created by Bruno Oliveira as a proof of concept
    - pytest + rich, what’s not to love?
    - Now we just need a maintainer or two or three….
- [Embedding images in GitHub README](https://www.youtube.com/watch?v=8088ORqS3uY)
    - Suggested by Henrik Finsberg
    - Video by Anthony Sottile
    - This is WITHOUT putting the image in the repo.
    - Upload or drop an image to an issue comment.
        - Don’t save the comment, just wait for GitHub to upload it to their CDN.
        - GH will add a markdown link in the comment text box with a link to the now uploaded image.
        - Now you can use that image in a README file.
    - You can do the same while editing the README in the online editor. 


**Ben** **#6:** [**pyotp**](https://pyauth.github.io/pyotp/)

- A library for generating and verifying one-time passwords (OTP).
- Helpful for [implementing multi-factor authentication (MFA)](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) in web applications.
- Supports [HMAC-based one-time passwords (HOTP)](https://en.wikipedia.org/wiki/HMAC-based_one-time_password) and [time-based one-time passwords (TOTP)](https://en.wikipedia.org/wiki/Time-based_one-time_password).
    - While HOTP delivered via SMS text messages is a common approach to implementing MFA, [SMS is not really secure](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html#sms-messages-and-phone-calls).
    - TOTP using an authenticator app on the user’s device such as Google Authenticator or Microsoft Authenticator is more secure, fairly easy to implement, and free (no SMS messaging fees and multiple free authenticator apps available for users).
    - TOTP works best by making a QR code available to simplify the setup for the user in their authenticator app. Lots of easy to implement QR code generators to choose from ([qrcode](https://www.npmjs.com/package/qrcode) is a popular one if you use javascript on the front end).

TOTP quick reference:

    import pyotp
    
    def generate_shared_secret():
        # securely store this shared secret with user account data
        return pyotp.random_base32()
    
    def generate_provisioning_uri(secret, email):
        # generate uri for a QR code from the user's shared secret and email address
        return pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name='YourApp')
    
    def verify_otp(secret, otp):
        # verify user's one-time password entry with their shared secret
        totp = pyotp.TOTP(secret)
        return totp.verify(otp)

**Extras** 

Brian:

- [**PyConUS 2022 videos now up**](https://www.youtube.com/watch?v=nWnIRYQrVtk&list=PL2Uw4_HvXqvYeXy8ab7iRHjA-9HiYhRQl)
- [**A few more Python related extensions for VSCode**](https://devblogs.microsoft.com/python/python-in-visual-studio-code-may-2022-release/)
    - [black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), [pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint), [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort), and [Jupyter PowerToys](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-powertoys)
- Work has begun on a [**pytest course**](https://pythontest.com/courses/)
    - Saying this in public to inspire me to finish it.
    - No ETA yet
- **[Sad Python Girls Club podcast](https://anchor.fm/sad-python-girls-club/)**

Michael:

- [**PyTorch M1**](https://www.macrumors.com/2022/05/18/pytorch-gpu-accelerated-training-apple-silicon/)
- [**Mission Encodable**](https://missionencodeable.com)
- [**PWAs and pyscript**](https://github.com/mikeckennedy/pyscript-pwa-example)
  - Michael's now released **[pyscript PWA YouTube video](https://www.youtube.com/watch?v=lC2jUeDKv-s)**

- [**cal.com**](https://cal.com) (open source calendly)
- [**Supabase**](https://supabase.com) (open source Firebase)

**Joke:** [**Beginner problems**](https://twitter.com/PR0GRAMMERHUM0R/status/1527725881598287873)

