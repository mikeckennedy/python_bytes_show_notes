# Python Bytes 27
**Brian #1:**  **PyCon 2017** 

- All videos available: [https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg](https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg)
- Lessons learned:
  - pick up swag on day one. vendors run out.
  - take business cards with you and keep them on you
    - Not your actual business cards unless you are representing your company.
    - Cards that have your social media, github account, blog, or podcast or whatever on them.
  - 3x3 stickers are too big. 2x2 plenty big enough
  - lightening talks are awesome, because they are a lot of ranges of speaking experience
  - will definitely do that again
  - try to go to the talks that are important to you, but don’t over stress about it, since they are taped. However, it would be lame if all the rooms were empty, so don’t everybody ditch.
  - lastly: everyone knows Michael. 
  

**Michael #2:** [**How to Create Your First Python 3.6 AWS Lambda Function**](https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html)

- Tutorial from [Full Stack Python](https://www.fullstackpython.com/)
- Walks you through creating an account
- Select your Python version (3.6, yes!)
- `def lambda_handler(event, context): …` # write this function, done!
- Set and read environment variables (could be connection strings and API keys)

**Brian #3:** [**How to Publish Your Package on PYPI**](https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/)

- jetbrains article
  - structure of the package
    - oops. doesn't include src, see https://pythonbytes.fm/22
  - decent discussion of a the contents of the setup.py file (but interestingly absent is an example setup.py file)
  - good discussion of .pypirc file and links to the test and production PyPi
  - example of using twine to push to PyPI
  - overall: good discussion, but you'll still need a decent example.


**Michael #4:** [**Coconut: Simple, elegant, Pythonic functional programming**](http://coconut-lang.org/)

-  Coconut is a functional programming language that compiles to Python. 
- Since all valid Python is valid Coconut, using Coconut will only extend and enhance what you're already capable of in Python.
- `pip install coconut`
  1. Some of Coconut’s major features include built-in, syntactic support for:
    1. Pattern-matching,
    2. Algebraic data-types,
    3. Tail call optimization,
    4. Partial application,
    5. Better lambdas,
    6. Parallelization primitives, and
    7. A whole lot more, all of which can be found in [Coconut’s detailed documentation](http://coconut.readthedocs.io/en/master/DOCS.html).
- Talk Python episode coming in a week

**Brian #5:**  [**Choose a licence**](https://choosealicense.com/)

- MIT : simple and permissive
- Apache 2.0 : something extra about patents.
- GPL v3 : this is the contagious one that requires derivitive work to also be GPL v3
- Nice list with overviews of what they all mean with color coded bullet points: [https://choosealicense.com/licenses/](https://choosealicense.com/licenses/)

**Michael #6:** [**Python for Scientists and Engineers**](http://pythonforengineers.com/python-for-scientists-and-engineers/)

- **Table of contents**:
- **Beginners Start Here:**
  - [**Create a Word Counter in Python**](http://pythonforengineers.com/create-a-word-counter-in-python/)
  - [**An introduction to Numpy and Matplotlib**](http://pythonforengineers.com/an-introduction-to-numpy-and-matplotlib/)
  - [**Introduction to Pandas with Practical Examples (New)**](http://pythonforengineers.com/introduction-to-pandas/)
- **Main Book**
  - [**Image and Video Processing in Python**](http://pythonforengineers.com/image-and-video-processing-in-python/)
  - [**Data Analysis with Pandas**](http://pythonforengineers.com/data-analysis-with-pandas/)
  - [**Audio and Digital Signal Processing (DSP)**](http://pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/)
  - [**Control Your Raspberry Pi From Your Phone / Tablet**](http://pythonforengineers.com/control-your-raspberry-pi-from-your-phone-tablet/)
- **Machine Learning Section**
  - [**Machine Learning with an Amazon like Recommendation Engine**](http://pythonforengineers.com/machine-learning-with-an-amazon-like-recommendation-engine/)
  - [**Machine Learning For Complete Beginners:**](http://pythonforengineers.com/machine-learning-for-complete-beginners/) ****Learn how to predict how many Titanic survivors using machine learning. No previous knowledge needed!
  - [**Cross Validation and Model Selection**](http://pythonforengineers.com/cross-validation-and-model-selection/): In which we look at cross validation, and how to choose between different machine learning algorithms. Working with the Iris flower dataset and the Pima diabetes dataset.
- **Natural Language Processing**
  - [**Introduction to NLP and Sentiment Analysis**](http://pythonforengineers.com/natural-language-processing-and-sentiment-analysis-with-python/)
  - [**Natural Language Processing with NTLK**](http://pythonforengineers.com/introduction-to-nltk-natural-language-processing-with-python/)
  - [**Intro to NTLK, Part 2**](http://pythonforengineers.com/intro-to-nltk-part-2/)
  - [**Build a sentiment analysis program**](http://pythonforengineers.com/build-a-sentiment-analysis-app-with-movie-reviews/)
  - [**Sentiment Analysis with Twitter**](http://pythonforengineers.com/practice-session-sentiment-analysis-with-twitter/)
  - [**Analysing the Enron Email Corpus**](http://pythonforengineers.com/analysing-the-enron-email-corpus/): The Enron Email corpus has half a million files spread over 2.5 GB. When looking at data this size, the question is, where do you even start?
  - [**Build a Spam Filter using the Enron Corpus**](http://pythonforengineers.com/build-a-spam-filter/)

**In other news**:

- [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest) Beta release and initial feedback is going very well.

