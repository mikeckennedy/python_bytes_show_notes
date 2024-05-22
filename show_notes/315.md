# Python Bytes 315

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)


**Michael #1:** [Jupyter Server 2.0 is released!](https://blog.jupyter.org/jupyter-server-2-0-is-released-121ac99e909a)

- Jupyter Server provides the core web server that powers JupyterLab and Jupyter Notebook.
- **New Identity API**: As Jupyter continues to innovate its real-time collaboration experience, identity is an important component.
- **New Authorization API**: Enabling collaboration on a notebook shouldn’t mean “allow everyone with access to my Jupyter Server to edit my notebooks”. What if I want to share my notebook with e.g. a subset of my teammates?
- **New Event System API**: [jupyter_events](https://github.com/jupyter/jupyter_events)—a package that provides a JSON-schema-based event-driven system to Jupyter Server and server extensions.
- **Terminals Service is now a Server Extension**: Jupyter Server now ships the “Terminals Service” as an extension (installed and enabled by default) rather than a core Jupyter Service.
- **pytest-jupyter**: A pytest plugin for Jupyter

**Brian #2:** **Converting to pyproject.toml**

- Last week, [episode 314](https://pythonbytes.fm/episodes/show/314/what-are-you-a-wise-guy-sort-it-out), we talked about “Tools for rewriting Python code” and I mentioned a desire to convert setup.py/setup.cfg to pyproject.toml
- Several of you, including Christian Clauss and Brian Skinn, let me know about a few tools to help in that area. Thank you.
- [ini2toml](https://pypi.org/project/ini2toml/) - Automatically translates .ini/.cfg files into TOML
    - “… can also be used to convert any compatible [.ini/.cfg](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure) file to [TOML](https://toml.io/en/).”
    - “ini2toml comes in two flavours: *“lite”* and *“full”*. The “lite” flavour will create a TOML document that does not contain any of the comments from the original .ini/.cfg file. On the other hand, the “full” flavour will make an extra effort to translate these comments into a TOML-equivalent (please notice sometimes this translation is not perfect, so it is always good to check the TOML document afterwards).”
- [pyproject-fmt](https://github.com/tox-dev/pyproject-fmt) - Apply a consistent format to `pyproject.toml` files
    - Having a consistent ordering and such is actually quite nice.
    - I agreed with most changes when I tried it, except one change.
        - The faulty change: it modified the name of my project. Not cool.
        - pytest plugins are traditionally named pytest-something.
            - the tool replaced the - with _. Wrong. 
            - So, be careful with adding this to your tool chain if you have intentional dashes in the name.
        - Otherwise, and still, cool project.
- [validate-pyproject](https://github.com/abravalheri/validate-pyproject) - Automated checks on pyproject.toml powered by JSON Schema definitions
    - It’s a bit terse with errors, but still useful.

```
    $ validate-pyproject pyproject.toml
    Invalid file: pyproject.toml
    [ERROR] `project.authors[{data__authors_x}]` must be object
        
    $ validate-pyproject pyproject.toml
    Invalid file: pyproject.toml
    [ERROR] Invalid value (at line 3, column 12)
```

- I’d probably add [tox](https://tox.wiki/en/latest/)
    - Don’t forget to build and test your project after making changes to pyproject.toml
    - You’ll catch things like missing dependencies that the other tools will miss.

**Michael #3:**  [aws-lambda-powertools-python](https://github.com/awslabs/aws-lambda-powertools-python)

- Via Mark Pender
- A suite of utilities for AWS Lambda Functions that makes distributed tracing, structured logging, custom metrics, idempotency, and many leading practices easier
- Looks kinda cool if you prefer to work almost entirely in python and avoid using any 3rd party tools like Terraform etc to manage the support functions of deploying, monitoring, debugging lambda functions
[](https://awslabs.github.io/aws-lambda-powertools-python/2.4.0/core/tracer/)- [**Tracing**](https://awslabs.github.io/aws-lambda-powertools-python/2.4.0/core/tracer/): Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions
- [**Logging**](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/) - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details
- [**Metrics**](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/) - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)
- [**Event handler: AppSync**](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/appsync/) - AWS AppSync event handler for Lambda Direct Resolver and Amplify GraphQL Transformer function
- [**Event handler: API Gateway and ALB**](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/) - Amazon API Gateway REST/HTTP API and ALB event handler for Lambda functions invoked using Proxy integration
- [**Bring your own middleware**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/middleware_factory/) - Decorator factory to create your own middleware to run logic before, and after each Lambda invocation
- [**Parameters utility**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parameters/) - Retrieve and cache parameter values from Parameter Store, Secrets Manager, or DynamoDB
- [**Batch processing**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/) - Handle partial failures for AWS SQS batch processing
- [**Typing**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/typing/) - Static typing classes to speedup development in your IDE
- [**Validation**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/validation/) - JSON Schema validator for inbound events and responses
- [**Event source data classes**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/) - Data classes describing the schema of common Lambda event triggers
- [**Parser**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parser/) - Data parsing and deep validation using Pydantic
- [**Idempotency**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/idempotency/) - Convert your Lambda functions into idempotent operations which are safe to retry
- [**Feature Flags**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/feature_flags/) - A simple rule engine to evaluate when one or multiple features should be enabled depending on the input
- [**Streaming**](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/streaming/) - Streams datasets larger than the available memory as streaming data.

**Brian #4:** [**How to create a self updating GitHub Readme**](https://pybit.es/articles/how-to-create-a-self-updating-github-readme/)

- Bob Belderbos 
- [Bob’s GitHub profile](https://github.com/bbelderbos) is nice
    - Includes latest Pybites articles, latest Python tips, and even latest Fosstodon toots
    - And he includes a link to [an article](https://pybit.es/articles/how-to-create-a-self-updating-github-readme/) on how he did this.
- A Python script that pulls together all of the content, [build-readme.py](https://github.com/bbelderbos/bbelderbos/blob/main/build-readme.py)
    - and fills in a [TEMPLATE.md](https://github.com/bbelderbos/bbelderbos/blob/main/TEMPLATE.md) markdown file.
    - It gets called through a GitHub action workflow, [update.yml](https://github.com/bbelderbos/bbelderbos/blob/main/.github/workflows/update.yml)
    - and automatically commits changes,
    - currently [daily at 8:45](https://crontab.guru/#45_8_*_*_*)
- This happens every day, and it looks like there are only commits if 
- Note:
    - We covered [Simon Willison’s notes on self updating README](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/) on [episode 192 in 2020](https://pythonbytes.fm/episodes/show/192/calculations-by-hand-but-in-the-compter-with-handcalcs)


**Extras** 

Brian:

- [GitHub can check your repos for leaked secrets.](https://github.blog/2022-12-15-leaked-a-secret-check-your-github-alerts-for-free/)
- Julia Evans has released a new zine, [The Pocket Guide to Debugging](https://wizardzines.com/zines/debugging-guide/)
- [Python Easter Eggs](https://github.com/OrkoHunter/python-easter-eggs) 
    - Includes this fun one from 2009 from Barry Warsaw and Brett Cannon
```
    >>> from __future__ import barry_as_FLUFL
    >>> 1 <> 2
    True
    >>> 1 != 2
      File "<stdin>", line 1
        1 != 2
           ^
    SyntaxError: invalid syntax
```
- [Crontab Guru](https://crontab.guru/#*_*_*_*_*)

Michael:

- [Canary Email AI](https://canarymail.io)
- [3.11 delivers](https://twitter.com/pypi/status/1603089763287826432)
- First chance to try “iPad as the sole travel device.” Here’s a report.
    - Follow up from [306](https://pythonbytes.fm/episodes/show/306/some-fun-pytesting-tools) and [309](https://pythonbytes.fm/episodes/show/309/when-malware-pocs-are-themselves-malware) discussions.
- [Maps be free](https://arstechnica.com/gadgets/2022/12/linux-amazon-meta-and-microsoft-want-to-break-the-google-maps-monopoly/)
- [New laptop design](https://python-bytes-static.nyc3.digitaloceanspaces.com/michaels-new-laptop-design.jpg)

![](https://python-bytes-static.nyc3.digitaloceanspaces.com/michaels-new-laptop-design.jpg)

**Joke:**  [What are clouds made of?](https://www.reddit.com/r/programminghumor/comments/z3pj3j/dose_the_cloud_rains_code_then/)

