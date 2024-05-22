# Python Bytes 257

Sponsored by **Shortcut - Get started at** [**shortcut.com/pythonbytes**](http://shortcut.com/pythonbytes)

Special guest: **Morleh So-kargbo**


**Michael #1:** [**Django 4.0 beta 1 released**](https://www.djangoproject.com/weblog/2021/oct/25/django-40-beta-1-released/)
- Django 4.0 beta 1 is now available.
- Django 4.0 has an abundance of [**new features**](https://docs.djangoproject.com/en/4.0/releases/4.0/)
    - The new `[*expressions](https://docs.djangoproject.com/en/4.0/ref/models/constraints/#django.db.models.UniqueConstraint.expressions)` positional argument of `[UniqueConstraint()](https://docs.djangoproject.com/en/4.0/ref/models/constraints/#django.db.models.UniqueConstraint)` enables creating functional unique constraints on expressions and database functions.
    - The new [scrypt password hasher](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/#scrypt-usage) is more secure and recommended over PBKDF2.
    - The new `django.core.cache.backends.redis.RedisCache` cache backend provides built-in support for caching with Redis.
    - To enhance customization of `[Forms](https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form)`, [Formsets](https://docs.djangoproject.com/en/4.0/topics/forms/formsets/), and `[ErrorList](https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.ErrorList)` they are now rendered using the template engine.


**Brian #2: py - The Python launcher**

- `py` has been bundled with Python for Windows only since Python 3.3, as `py.exe`
    - See [Python Launcher for Windows](https://docs.python.org/3/using/windows.html#launcher) 
    - I’ve mostly ignored it since I use Python on Windows, MacOS, and Linux and don’t want to have different workflows on different systems.
- But now Brett Cannon has developed [python-launcher](https://github.com/brettcannon/python-launcher) which brings `py` to MacOS and various other Unix-y systems or any OS which supports Rust. 
- Now
    - `py` is everywhere I need it to be, and I’ve switched my workflow to use it.
- Usage 
    - `py` : Run the latest Python version on your system
    - `py -3` : Run the latest Python 3 version
    - `py -3.9` : Run latest 3.9 version
    - `py -2.7` : Even run 2.x versions
    - `py` `--``list` : list all versions (with py-launcher, it also lists paths)
    - `py` `--``list-paths` : py.exe only - list all versions with path
- **Why is this cool?** 
        - **I never have to care where Python is installed or where it is in my search path.**
        - **I can always run any version of Python installed without setting up symbolic links.**
        - **Same workflow works on Windows, MacOS, and Linux**
    - Old workfow
        - Make sure latest Python is found first in search path, then call `python3 -m venv venv`
        - For a specific version, make sure `python3.8`, for example, or `python38` or something is in my Path. If not, create it somewhere.
    - New workflow.
        - `py -m venv venv` - Create a virtual environment with the latest Python installed. 
        - After activation, everything happens in the virtual env.
    - Create a specific venv to test something on an older version:
        - `py -3.8 venv venv` `--``prompt` `'``3.8``'`
    - Or even just run a script with an old version
        - `py -3.8 script_name.py`
    - Of course, you can run it with the latest version also
        - `py script_name.py`
- Note: if you use `py` within a virtual environment, the default version is the one from the virtual env, not the latest. 


Morleh **#3:** [**Transformers As General**](https://www.stateof.ai/2021-report-launch.html)[-](https://www.stateof.ai/2021-report-launch.html)[**Purpose Architecture**](https://www.stateof.ai/2021-report-launch.html)

- The [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper first proposed Transformers in June 2017.  
- The [Hugging Face (🤗) Transformers](https://huggingface.co/) package is a popular PYTHON library providing pre-trained models that are extraordinarily useful for various natural language processing (NLP) tasks. 
- It earlier supported only PyTorch, but, in 2019, it supported TensorFlow 2 
- 🤗 Transformers provides the following tasks out of the box: Sentiment analysis, Text generation, Question answering, Filling masked text, Summarization, Language Translation, Feature Extraction.
- The [State of AI Report 2021](https://www.stateof.ai/2021-report-launch.html) (Nathan Beniach and Ian Hogarth) came out in late October, highlighting the role of transformers.
- "Transformers have emerged as a general-purpose architecture for ML. Not just for Natural Language Processing, but also Speech, Computer Vision or even protein structure prediction."
    - Examples include Google's [Vision Transformer (ViT)](https://arxiv.org/abs/2010.11929) and CoAtNet
- Transformers are fulfilling the [Transfer Learning promise](https://becominghuman.ai/the-age-of-machine-learning-as-code-has-arrived-9eb00e0eb7a8), saving training time and costs.
- 🤗 Transformers has a partnership with AWS to make it easier to leverage Machine Learning models.


**Michael #4:** [**Model bakery**](https://model-bakery.readthedocs.io/en/latest/)

- Model Bakery offers you a smart way to create fixtures for testing in Django.
- [**Usage example**](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#basic-usage) **- generates a randomly populated Django Model (DB Entity)**
- If you’re not comfortable with random data or even if you just want to improve the semantics of the generated data, there’s hope for you. [**Use recipes**](https://model-bakery.readthedocs.io/en/latest/recipes.html#recipes). 


**Brian #5:**  [**Coverage goals, goals.py**](https://nedbatchelder.com/blog/202111/coverage_goals.html)

- Ned Batchelder
- Ned wrote `goals.py` as a proof of concept to try out a feature request for coverage.py
- Allows something like “100% coverage in tests and 85% in product code” requirements.
- You give it a percentage number, and a list of glob patterns, and the return code indicates failure.
- You can run it several times on the same coverage output to have complex requirements.
- Example

```
    # We want to make sure all tests are run
    $ python goals.py --group 100 'tests/*.py'
    
    # Check all Python files collectively, except in the tests/ directory.
    $ python goals.py --group 85 '**/*.py' '!tests/*.py'
    
    # We definitely want complete coverage of anything related to html.
    $ python goals.py --group 100 '**/*html*.py'
    
    # No Python file should be below 90% covered.
    $ python goals.py --file 90 '**/*.py'
```

Morleh **#6:** [Web3.py](https://web3py.readthedocs.io/en/stable/)

- Web3.py is the PYTHON library for interacting with the Ethereum Blockchain.
- Web3.py lets you develop clients that interact with the Ethereum Blockchain.
- Web3.py is a collection of libraries that enable you to create Ethereum transactions.
- It is found in decentralized apps (dapps) to help with sending transactions, interacting (write or read) with and executing smart contracts or business logic. 

**Extras**

Michael:

- [**mcfly**](https://github.com/cantino/mcfly) update
- [**PWC 2022**](https://2022.pythonwebconf.com/) - extended the Call for Papers until Monday, Nov. 15
- Anker GAN charger for M1s - [**Anker Nano II 65W**](https://us.anker.com/collections/chargers/products/a2663111)
- [**And Ars view of the new M1s**](https://arstechnica.com/gadgets/2021/10/2021-macbook-pro-review-yep-its-what-youve-been-waiting-for/) ****
    - *Rest assured: If you didn't like the direction Apple has been taking with the MacBook Pro for the last five years, this laptop mostly feels like an explicit apology for all of that. The result: It's the best laptop money can buy for many use cases, provided you have* ***a lot*** *of money.*
- M1 vs. M1 Max **perf comparison**
![](https://paper-attachments.dropbox.com/s_8E8281B2CA8C1C3C9AE11A04DA91D552F3FA3E7EE538F53906E38B3CD5001F84_1635868945210_m1-vs-m1-max-video.jpg)

**Joke:** [**Competing standards**](https://xkcd.com/927/)

