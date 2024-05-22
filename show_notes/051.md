# Python Bytes 51
This episode is brought to you by Datadog: [pythonbytes.fm/datadog](https://pythonbytes.fm/datadog)

**Brian #1:** [**Exploring United States Policing Data with Python**](https://blog.patricktriest.com/police-data-python/)

- How to take a publicly available data set and, using jupyter, ipython, matplotlib, numpy, pandas, and scipy:
  - ask questions of the data and get answers
  - visualize results with plots
  - fill in and/or remove blank data
- The example is interesting, and easy to follow. It doesn’t explain all the code, just shows it. You can go look that stuff up later.
- A few notes as I worked through half of the example:
  - pip install scipy
  - step 1.7 plt.show()
  - end of 2.3, don't need `.to_html().replace('\n','')`
  - Use shift-enter to run a cell
- I’m concerned with the validity of the results due to the dropping of rows with missing data. Some columns aren’t used for some questions, so for those purposes, the data shouldn’t be abandoned.
- Still a very nice tutorial.

**Michael #2:** [**How to make your code 80 times faster**](https://morepypy.blogspot.it/2017/10/how-to-make-your-code-80-times-faster.html)

- Often hear people who are happy because PyPy makes their code 2 times faster or so. Here is a short personal story which shows PyPy can go well beyond that.
- Evolutionary algorithms: the ambitious plan was to automatically evolve a logic which could control a (simulated) quadcopter
- To drive the quadcopter, a Creature has a run_step method which runs at each delta_t
  - inputs is a numpy array containing the desired setpoint and the current position on the Z axis;
  - outputs is a numpy array containing the thrust to give to the motors. To start easy, all the 4 motors are constrained to have the same thrust
- run_step is called at 100Hz
- simply tried to run this code on CPython: ~6.15 seconds/generation
- Then tried with PyPy 5.9: Ouch! We are ~5.5x slower than CPython. This was kind of expected: numpy is based on cpyext, which is infamously slow
- first obvious step is to use numpypy instead of numpy: PyPy+numpy, and more than 2x faster than the original CPython
- So, let's try to do better. As usual, the first thing to do is to profile and see where we spend most of the time. 
- we know that the matrix is small, and always of the same shape. So, let's unroll the loop manually
- **Tada**: This is around 80 (eighty) times faster than the original CPython+numpy implementation, and around 35-40x faster than the naive PyPy+numpypy one

**Brian #3:** [**Giving Open-Source Projects Life After a Developer's Death**](https://www.wired.com/story/giving-open-source-projects-life-after-a-developers-death/amp)

**Michael #4:** [**Solar Powered Internet Connected Lawn Sprinkler Project**](http://www.movingelectrons.net/blog/2017/10/18/solar-powered-internet-connected-lawn-sprinkler.html)

- via listener suggestion / written: Lenin
- a little project with Adafruit’s Feather HUZZAH board and MicroPython
- Combines with Home Assistant
- Mostly based on AdaFruit, they have a detailed list of the hardware used.
- based on the [**MQTT protocol**](http://mqtt.org/), which is a Client-Server *Internet of Things* connectivity protocol, comes with micropython
- Nice references back to AdaFruit tutorials
- Talk Python #108: MicroPython and Open Source Hardware at Adafruit: **[https://talkpython.fm/108](https://talkpython.fm/108)**

**Brian #5:** **Some New Python Books**

- [Python Tricks: A Buffet of Awesome Python Features](http://amzn.to/2zEkfO7)
  - by Dan Bader
- [Illustrated Guide to Python 3](http://amzn.to/2yfE61T)
  - by Matt Harrison
- While we’re at it, there are some older Python books that could use some review love. If you’ve read these, please leave a review. It helps more than you may realize.
  - [Python Testing with pytest](http://amzn.to/2zrQZcv), by Brian Okken
  - [Test-Driven Development with Python](http://amzn.to/2zqJcf5), by Harry Percival
  - [Two Scoops of Django](http://amzn.to/2zpBWxP), Daniel & Audrey Roy Greenfield

**Michael #6:** [**Anaconda Distribution 5.0 released**](https://www.anaconda.com/blog/developer-blog/announcing-the-release-of-anaconda-distribution-5-0/)

- Over 100 packages have been updated or added to the distribution. JupyterLab alpha preview 0.27.0 is now included, and MKL has been updated to 2018.0.0.
- The new version features all new compilers on macOS and Linux, providing substantial security and performance improvements.
- Where possible, all build recipes are now using conda-forge as a base, via https://github.com/AnacondaRecipes.
- A new channel, pkgs/main, has been added to defaults. The new channel is given top priority within defaults and holds packages built with the new compiler stack.
- The new version of Anaconda Distribution now features more flexible dependency pinning.

