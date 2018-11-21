# Python Bytes 105
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Colorizing and Restoring Old Images with Deep Learning**](https://blog.floydhub.com/colorizing-and-restoring-old-images-with-deep-learning/)

- Text interview by Charlie Harrington of Jason Antic, developer of [DeOldify](https://github.com/jantic/DeOldify)
- A whole bunch of machine learning buzzwords that I don’t understand in the slightest combine to make a really cool to to make B&W photos look freaking amazing.
- “This is a deep learning based model. More specifically, what I've done is combined the following approaches:
	- **Self-Attention Generative Adversarial Network**
	- Training structure inspired by (but not the same as) **Progressive Growing of GANs.**
	- **Two Time-Scale Update Rule.**
	- **Generator Loss** is two parts: One is a basic Perceptual Loss (or Feature Loss) based on VGG16. The second is the loss score from the critic.”

**Michael #2:** [**PlatformIO IDE for VSCode**](https://platformio.org/platformio-ide)

- via Jason Pecor
- PlatformIO is an open source ecosystem for IoT development
- Cross-platform IDE and unified debugger. Remote unit testing and firmware updates
- Built on Visual Studio Code which has a nice extension for Python
- PlatformIO, combined with the features of VSCode provides some great improvements for project development over the standard Arduino IDE for Arduino-compatible microcontroller based solutions.
- Some of these features are paid, but it’s a reasonable price
- With Python becoming more popular for microcontroller design, as well, this might be a very nice option for designers.
- And for Jason’s, specifically, it provides a single environment that can eventually be configured to handle doing the embedded code design, associated Python supporting tools mods, and HDL development. 
- The PlatformIO Core written in Python.  Python 2.7 (hiss…)
- Jason’s test drive video from Tuesday:  [**Test Driving PlatformIO IDE for VSCode**](https://www.youtube.com/watch?v=pXv_ky6HAVI&feature=youtu.be)

**Brian #3:** [**Python Data Visualization 2018: Why So Many Libraries?**](https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries/)

- Nice overview of visualization landscape, by Anaconda team
- Differentiating factors, API types, and emerging trends
- Related: [Drawing Data with Flask and matplotlib](http://renesd.blogspot.com/2018/11/drawing-data-with-flask-and-matplotlib.html)
	- Finally! A really simple example app in Flask that shows how to both generate and display matplotlib plots.
	- I was looking for something like this about a year ago and didn’t find it.

**Michael #4:** [**coder.com - VS Code in the cloud**](https://coder.com/)

- Full Visual Studio Code, but in your browser
- Code in the browser
- Access up to 96 cores
- VS Code + extensions, so all the languages and features
- Collaborate in real time, think google docs
- Access linux from any OS
- Note: They sponsored an episode of Talk Python To Me, but this is not an ad here...

 
**Brian #5:** ****[**By Welcoming Women, Python’s Founder Overcomes Closed Minds In Open Source**](https://www.forbes.com/sites/oracle/2018/11/20/by-welcoming-women-pythons-founder-overcomes-closed-minds-in-open-source/)

- Forbes’s article about Guido and the Python community actively working to get more women involved in core development as well as speaking at conferences.
- Good lessons for other projects, and work teams, about how you cannot just passively “let people join”, you need to work to make it happen.

**Michael #6:** [**Machine Learning Basics**](http://alpopkes.com/portfolio/portfolio-2/)

- From Anna-Lena Popkes
- Plain python implementations of basic machine learning algorithms
- Repository contains implementations of basic machine learning algorithms in plain Python (modern Python, yay!)
- All algorithms are implemented from scratch without using additional machine learning libraries. 
- Goal is to provide a basic understanding of the algorithms and their underlying structure, not to provide the most efficient implementations.
- Most of the algorithms
	- [Linear Regression](https://github.com/zotroneneis/machine_learning_basics/blob/master/linear_regression.ipynb)
	- [Logistic Regression](https://github.com/zotroneneis/machine_learning_basics/blob/master/logistic_regression.ipynb)
	- [Perceptron](https://github.com/zotroneneis/machine_learning_basics/blob/master/perceptron.ipynb)
	- [k-nearest-neighbor](https://github.com/zotroneneis/machine_learning_basics/blob/master/k_nearest_neighbour.ipynb)
	- [k-Means clustering](https://github.com/zotroneneis/machine_learning_basics/blob/master/kmeans.ipynb)
	- [Simple neural network with one hidden layer](https://github.com/zotroneneis/machine_learning_basics/blob/master/simple_neural_net.ipynb)
	- [Multinomial Logistic Regression](https://github.com/zotroneneis/machine_learning_basics/blob/master/softmax_regression.ipynb)
	- [Decision tree for classification](https://github.com/zotroneneis/machine_learning_basics/blob/master/decision_tree_classification.ipynb)
	- [Decision tree for regression](https://github.com/zotroneneis/machine_learning_basics/blob/master/decision_tree_regression.ipynb)
- Anna-Lena was on Talk Python on 186: http://talkpython.fm/186

Extras:


- Michael: [**PSF Fellow Nominations are open**](https://twitter.com/mkennedy/status/1065017619151912960)
- Michael: [**Shiboken has no meaning**](https://setanta.wordpress.com/2009/08/31/shiboken/)
- Brian: [**Python 3.7 runtime now available in AWS Lambda**](https://aws.amazon.com/blogs/compute/python-3-7-runtime-now-available-in-aws-lambda/)


