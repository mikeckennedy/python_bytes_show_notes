# Python Bytes 29
Brought to you by Rollbar! [http://rollbar.com/pythonbytes](http://rollbar.com/pythonbytes)

**Brian #1:** [**Responsive Bar Charts with Bokeh, Flask and Python 3**](https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html)

- by Matt Makai at fullstackpython.com
- A walkthrough example of putting together a flask app that uses Bokeh bar charts to visualize data.
- All steps included, no previous experience with Flask or Bokeh required.
- Nice explanation of what the code does without going into too much detail.
- Good jumping off point for further learning, but complete enough to be useful right away.

**Michael #2:** [**Zappa**](https://github.com/Miserlou/Zappa) [**Serverless Python Web Services**](https://github.com/Miserlou/Zappa)

- **Zappa** makes it super easy to build and deploy all Python WSGI applications on AWS Lambda + API Gateway
- Think of it as "serverless" web hosting for your Python apps. 
- That means **infinite scaling**, **zero downtime**, **zero maintenance** - and at a fraction of the cost of your current deployments!
- Better still, with Zappa you only pay for the milliseconds of server time that you use, so it's many **orders of magnitude cheaper** than VPS/PaaS hosts and in most cases, it's completely free. Plus, there's no need to worry about load balancing or keeping servers online ever again.
- Asynchronous Task Execution: 

```
    from flask import Flask
    from zappa.async import task
    app = Flask(__name__)
    
    @task
    def make_pie():
        """ This takes a long time! """
        ingredients = get_ingredients()
        pie = bake(ingredients)
        deliver(pie)
    
    @app.route('/api/order/pie')
    def order_pie():
        """ This returns immediately! """
        make_pie()
        return "Your pie is being made!"
```

**Brian #3:** [**Using a local cache for pip packages**](https://www.dominicrodger.com/2013/03/11/local-pip-cache/)

- In [https://pythonbytes.fm/24](https://pythonbytes.fm/24), **Local package store,** we talked about using pip to cache pypi projects to allow offline installation:
  - `$ pip download --cachedir <somePackage>`
  - `$ pip install --no-index --find-links=/tmp/wheelhouse somePackage`
- Well, Dominic does us one better by wrapping these commands in a couple of aliases. 
- However, his version uses  `pip install` `--``download`, which has been deprecated. Here’s a version with the new syntax:
  - `alias pipcache='pip download --cachedir ${HOME}/.pip-packages'`
  - `alias pipinstall='pip install --no-index --find-links=file://${HOME}/.pip-packages/'`

**Michael #4:** [**Building game AI using ML: Working with TensorFlow, Keras, and the Intel MKL in Python**](https://www.activestate.com/blog/2017/05/building-game-ai-using-machine-learning-working-tensorflow-keras-and-intel-mkl-python)

- From the ActivePython guys
- a classic arcade space shooter game that features enemies powered by machine learning
- we decided to build a Neural Network to drive the behaviour of the enemies in the game
- For the game part of things, we’re using PyGame
- In the training mode, the enemies fire randomly, and then each shot taken by the enemy is recorded as a hit or a miss along with its initial relative position/velocity values. Every one of these shots becomes a row in the training matrix and the network is trained in “realtime” after every row is added so you can see the network build and develop as you train.
- LESSONS LEARNED
  - Choosing the right data to train your network is important.
  - “Prepping” your data is key.
  - Experiment with network topology.
  - Visualization is important.

**Brian #5:** [**Debug Test Failures With Pdb**](https://hackebrot.github.io/pytest-tricks/debug_test_failures/)

- by Raphael Pierzina
- Debugging code with pytest, using:
  - --pdb to jump into the debugger at the point of failure
  - -x to stop after first failure
  - --lf to re-run all the tests that failed last time
- **Note:** Yes. All this and more is covered in [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest). 
  - Shameless plug for my book. Raphael is one of the technical reviewers. 
  - Thank you, Raphael!

**Michael #6:** [**Monitoring my VOIP provider with Home Assistant**](https://medium.com/@davidcameron/monitoring-my-voip-provider-with-home-assistant-83a31f0a8cb9)

- **Integrating it into Home Assistant:** Use [home-assistant.io](http://home-assistant.io/) as a home automation platform in my house. 
- It’s written in Python, open source, and has a large community surrounding it. 
- Unfortunately, there wasn’t anything already built for my Cisco ATA.
- Decided to write, an open source my first python module called [pyciscsospa](https://pypi.python.org/pypi/pyciscospa/) you can download it and use it for your own ATA as well.
- Receive a push notification on my phone when the phone lines go down and come back up

