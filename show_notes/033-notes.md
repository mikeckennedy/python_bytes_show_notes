Sponsored by Rollbar! https://pythonbytes.fm/rollbar

**Brian #1:** [**Linting as Lightweight Defect Detection for Python**](https://dev.to/sethmichaellarson/linting-as-lightweight-defect-detection-for-python)

- flake8, 
- pycodestyle, formerly pep8 tool [https://pycodestyle.readthedocs.io/en/latest/](https://pycodestyle.readthedocs.io/en/latest/)
- pep257 can be checked with flake8-docstrings
- pydocstyle, [http://www.pydocstyle.org/](http://www.pydocstyle.org/)


**Michael #2:** [**You should build an Alexa skill**](https://medium.com/@jacquelinewilson/amazon-alexa-skill-recipe-1444e6ee45a6)

- Jacqueline Wilson wrote *Amazon Alexa Skill Recipe with Python 3.6*
- Ingredients:
  - A developer account on [https://developer.amazon.com](https://developer.amazon.com) (“Amazon Developer Console”)
  - An AWS account on [https://aws.amazon.com](https://aws.amazon.com) (“AWS Console”)
  - Beginner knowledge of Python 3.x syntax
- Create a “What’s for dinner” bot
- Amazon calls these utterances:
  - “What should I have for dinner?”
  - “Do you have a dinner idea?”
  - “What’s for dinner?”
- Tie the commands to an AWS Lambda function (returns a JSON response)
- Test via [Alexa Skill Testing Tool](https://echosim.io) 

**Brian #3:** [**RISE**](https://github.com/damianavila/RISE)

- Reveal IPython Slide Extension
- Making slides with Jupyter notebooks

**Michael #4:** [**Closer**](https://haarcuba.github.io/closer/)

- Run, monitor and close remote SSH processes automatically
- Closer was born because I had trouble with killing up processes I set up remotely via SSH. That is, you want to run some SSH process in the background, and then you want to kill it, just like you would a local subprocess.
- Main features:
  - kill the remote process (either by choice, or automatically at the end of the calling process)
  - capture the remote process’s output
  - live monitoring of remote process output
  - get a callback upon remote process’ death

**Brian #5:** [**Checklist for**](http://python.apichecklist.com/) [****](http://python.apichecklist.com/)[**Python libraries APIs**](http://python.apichecklist.com/)

**Michael #6:** [**Fades**](https://fades.readthedocs.io/en/release_6_0/readme.html)

- Fades is a system that automatically handles the virtualenvs in the cases normally found when writing scripts and simple programs, and even helps to administer big projects.
- fades will automagically create a new virtualenv (or reuse a previous created one), installing the necessary dependencies, and execute your script inside that virtualenv, with the only requirement of executing the script with fades and also marking the required dependencies.
- At the moment you execute the script, fades will search a virtualenv with the marked dependencies, if it doesn’t exists fades will create it, and execute the script in that environment.
- Indicating dependencies (in code or via CLI)
```
    import somemodule   # fades == 3
    import somemodule   # fades >= 2.1
    import somemodule   # fades >=2.1,<2.8,!=2.6.5
```
- Can control the Python version the env is based upon
- Can ask for a “refresh” on the virtual env
- You can also configure fades using .ini config files.
- How to clean up old virtualenvs?

**Listener comment,** [**RE: Episode 32**](https://pythonbytes.fm/episodes/show/32/8-ways-to-contribute-to-open-source-when-you-have-no-time#comment-3400891427)**:**

Jan Oglop:  

Hello Michael and Brian, I wanted to thank you for amazing work you do. And let you know that you have helped me to find the working place from my dreams! My colleagues has similar hobbies and loves python as much as I do!

Thank you again!

