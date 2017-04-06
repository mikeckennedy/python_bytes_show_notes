**Sponsored by Rollbar, thank you! [rollbar.com/pythonbytes](http://rollbar.com/pythonbytes)**

**#1 Brian:** [**Duplicate image detection with perceptual hashing in Python**](http://tech.jetsetter.com/2017/03/21/duplicate-image-detection/)

- Ben Hoyt
- From [Jetsetter.com](https://www.jetsetter.com/), Invitation-Only Travel Community
- We use a perceptual image hash called dHash (“difference hash”), which was developed by Neal Krawetz in his work on photo forensics. It’s a very simple but surprisingly effective algorithm that involves the following steps (to produce a 128-bit hash value)
  - Convert the image to grayscale
  - Downsize to a 9x9 square of gray values (or 17x17 for a larger, 512-bit hash)
  - Calculate the “row hash”: for each row, move from left to right, and output a 1 bit if the next gray value is greater than or equal to the previous one, or a 0 bit if it’s less (each 9-pixel row produces 8 bits of output)
  - Calculate the “column hash”: same as above, but for each column, move top to bottom
  - Concatenate the two 64-bit values together to get the final 128-bit hash
- Fast: Python is not very fast at bit twiddling, but all the hard work of converting to grayscale and downsizing is done by a C library: ImageMagick+wand or PIL.
- Available via github: [https://github.com/Jetsetter/pybktree](https://github.com/Jetsetter/pybktree)

**#2 Michael:** [**Google Open Source/Python**](https://opensource.google.com/projects/search?q=python)

- subprocess32: A reliable subprocess module for Python 2
- Grumpy: A Python to Go transcompiler and runtime
- Python Fire: Automatically turns any Python object or module into a command line interface (CLI)
- Python Client for Google Maps Services: Python client library for Google Maps API Web services
- Hyou: Pythonic Interface to manipulate Google Spreadsheet
- oauth2l: A simple CLI tool to get an OAuth token
- mock_maps_apis: Small AppEngine application that can mock some of the Google Maps APIs
- TensorFlow: TensorFlow is a fast, flexible, and scalable open source machine learning library 

**#3 Brian:** [**How to Handle Missing Data with Python**](http://machinelearningmastery.com/handle-missing-data-python/)

- Jason Brownlee
- Real-world data often has missing values.
- Data can have missing values for a number of reasons such as observations that were not recorded and data corruption.
- Handling missing data is important as many machine learning algorithms do not support data with missing values.


**#4 Michael:** [**hug REST framework**](http://www.hug.rest/)

- Drastically simplify API development over multiple interfaces
- With hug, design and develop your API once, then expose it however your clients need to consume it (locally, over HTTP, or through the command line)
- hug is the fastest and most modern way to create APIs on **Python3**
- hug has been built from the ground up with performance in mind.
  - It is built to consume resources only when necessary
  - compiled with Cython to achieve amazing performance
- Built in version management
- Automatic documentation
- Annotation powered validation
- Write once. Use everywhere (CLI, Python package, Web API)

**#5 Brian** **CLI with Click**

- I needed a cli interface that apparently fell into the “complex” category, because of subcommands, go figure. argparse ticked me off, so I tried click. It’s a joy to work with.
- [http://click.pocoo.org/](http://click.pocoo.org/)
- [https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/) - Just enough click tutorial to do exactly what I wanted. From 2015, realpython blog. (But argparse tutorial is a bit broken. in 3.5/3.6 😞 )

**#6 Michael:** [**Python's Instance, Class, and Static Methods Demystified**](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/)

- From [realpython.com](https://realpython.com), guest post from Dan Bader
- demystify what’s behind class methods, static methods, and regular instance methods
- Python 3 by default


    class MyClass:
        def method(self):
            return 'instance method called', self
    
        @classmethod
        def classmethod(cls):
            return 'class method called', cls
    
        @staticmethod
        def staticmethod():
            return 'static method called'
- Instances is clear but static and class are not so much
  - static and class methods are also available on instances
  - choice between class vs static method (do you want inheritance?)
  - instance methods can also access the class itself through the self.__class__ attribute

**Follow ups**

David Bieber from Google and Python Fire sent us this note: The program noted that Fire has one "heavy" dependency, IPython. Just wanted to chime in with this: we have a [game plan to remove IPython as a required dependency](https://github.com/google/python-fire/issues/7#issuecomment-284266940), but we're not there yet. (Contributions are welcome!)


- pdir2 now supports color, https://github.com/laike9m/pdir2/wiki/User-Configuration. With the example given, I’ve added a .pdir2config file and changed doc-color to magenta, and I can see the doc lines in both a white and black terminal.

**News from us**

**Brian** 

- [Python Testing with pytest book](https://pragprog.com/book/bopytest/python-testing-with-pytest) page has been spotted in the wild by Jakob Jarosz, https://twitter.com/qba73/status/848189279587229696. That was unexpected and cool to see.

**Michael**

- Launched / launching two new courses at Talk Python Training
  - [Managing Python Dependencies with pip and Virtual Environments](https://training.talkpython.fm/courses/explore_python_dependencies_course/managing-python-dependencies-with-pip-and-virtual-environments)
  - [Using and Mastering Cookiecutter](https://training.talkpython.fm/courses/explore_cookiecutter_course/using-and-mastering-cookiecutter-templates-for-project-creation)
- Course bundles now available: https://training.talkpython.fm/courses/all



