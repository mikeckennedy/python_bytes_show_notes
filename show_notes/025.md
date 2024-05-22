# Python Bytes 25
**Michael #1:** [**Python in SQL Server 2017: enhanced in-database machine learning**](https://blogs.technet.microsoft.com/dataplatforminsider/2017/04/19/python-in-sql-server-2017-enhanced-in-database-machine-learning/)

-  in-database analytics and machine learning with Python in SQL Server.
- Why?
  - **Elimination of data movement:** You no longer need to move data from the database to your Python application or model. Instead, you can build Python applications in the database. 
  - **Easy deployment:** Once you have the Python model ready, deploying it in production is now as easy as embedding it in a T-SQL script
  - **Rich extensibility:** You can install and run any of the latest open source Python packages in SQL Server to build deep learning and AI applications on huge amounts of data in SQL Server.
  - Works in express edition of SQL Server
- The standard open source CPython interpreter (version 3.5) and some Python packages commonly used for data science are downloaded and installed during SQL Server setup if you choose the Python option in the feature tree.
- Currently, a subset of packages from the popular Anaconda distribution is included along with Microsoft’s RevoScalePy package. The set of packages available for download will evolve as we move toward general availability of this feature.

**Brian #2**: [**Generating Fake Data for Python Unit Tests with Faker**](https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker)

- Used in [Content Negotiation with the Pyramid Web Framework](http://cecilphillip.com/content-negotiation-with-the-pyramid-web-framework/)
- [Faker](https://pypi.python.org/pypi/Faker) is great. From the pypi page:
  - “*Faker* is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.”
- The article above is a great introduction to show you what you can do with it.
- Faker includes localization, so you can get the output to match the proper language you want.

**Brian #3:** [**Stack Overflow Trends tool**](https://stackoverflow.blog/2017/05/09/introducing-stack-overflow-trends/?cb=1)

- Stack overflow introduces a trends tool starting with a graph that shows the questions using the terms Python, PHP, and Perl, plotted year vs % of total questions.
  - [https://zgab33vy595fw5zq-zippykid.netdna-ssl.com/wp-content/uploads/2017/05/languages-2-1024x621.png](https://zgab33vy595fw5zq-zippykid.netdna-ssl.com/wp-content/uploads/2017/05/languages-2-1024x621.png)
- Python’s growth since 2012 has been fairly steady, growing from ~3.5% to over 8%
- Plus, the trends tool looks fun.

**Sponsorship slots are available right now. Please contact us if you’re interested.**

**Michael #4:** [**We asked 20,000 people who they are and how they’re learning to code**](https://medium.freecodecamp.com/we-asked-20-000-people-who-they-are-and-how-theyre-learning-to-code-fff5d668969)

- Thanks Alan Jones
- **Who participated? More than 20,000 new coders responded to this survey. These are people who have been coding for less than 5 years.**
  - 62% of them live outside the US
  - their average age is 28 years old
  - 19% are women
  - They’ve been coding for an average of 21 months
  - 25% have already landed their first developer job
- 40% of them would like to either freelance or start their own business.
- Most of them are interested in working as web developers, but are also interested in a wide variety of developer specializations.
- Most new coders haven’t yet started listening to podcasts, but the ones who do listen to a wide range of them.

 
**Brian #5** [**Introduction to Anomaly Detection**](http://www.datasciencecentral.com/profiles/blogs/introduction-to-anomaly-detection)

- **Anomaly Detection Techniques**
  - Simple Statistical Methods
  - Challenges
- **Machine Learning-Based Approaches**
  - Density-Based Anomaly Detection
  - Clustering-Based Anomaly Detection
  - Support Vector Machine-Based Anomaly Detection
  - Building a Simple Detection Solution Using a Low-Pass Filter
  - Moving Average Using Discrete Linear Convolution


**Michael #6:** [**Beeware: A request for your help**](https://pybee.org/news/buzz/a-request-for-your-help/)

- What is Beeware? Started 4 years ago. Since then, the BeeWare project has grown to encompass support for mobile platforms, two alternate Python implementations, and a cross platform widget set - as well as the developer tools that started the project originally.
- Lots of work done over the last 6 months:
  - Extensive improvements to Batavia and VOC;
  - An Android backend for Toga;
  - A Django backend for Toga, enabling Toga apps to be deployed as web apps;
  - A Winforms backend for Toga, enabling Toga apps to run on Windows with a modern appearance;
- Unfortunately, my contract with Jambon is coming to a close - which means my contributions to BeeWare will go back to being what my spare time allows.
- So - this is an appeal to you - the Python community. If you are excited by the prospect of having access to Python on mobile platforms, or you would like to write applications in Python that have completely native user interfaces - **I need your help** for just **US$10 a month** - you can [join the BeeWare project as a member](http://pybee.org/contributing/membership/),

**Other news**

[pycascades.com](http://www.pycascades.com) is a regional PyCon for the Pacific Northwest. 

