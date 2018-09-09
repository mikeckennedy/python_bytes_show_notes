# Python Bytes 94
Sponsored by DigialOcean -- [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**Python Patterns**](http://python-patterns.guide/)

- [@brandon_rhodes](https://twitter.com/brandon_rhodes) vs GOF

**Michael #2:** [**Arctic: Millions of rows a sec (time data)**](https://github.com/manahl/arctic)

- Arctic is a high-performance datastore for numeric data. It supports Pandas, numpy arrays and pickled objects out-of-the-box, with pluggable support for other data types and optional versioning.
- Arctic can query millions of rows per second per client, achieves ~10x compression on network bandwidth, ~10x compression on disk, and scales to hundreds of millions of rows per second per MongoDB instance.
- Arctic has been under active development at Man AHL since 2012.
- Super fast, some latency numbers:
	- 1xDay Data 4ms for 10k rows, vs 2,210 ms from SQL Server)
	- Tick Data 1s for 3.5 MB (Python) or 15 MB (Java) vs 15-40sec from “other tick”
- Versioned data
- Built on MongoDB
- [Slides](https://www.slideshare.net/JamesBlackburn1/2015-pydata-highperformance-iot-and-financial-data-storage-with-python-and-mongodb)
- Based on pandas
- Tested with pytest

**Brian #3:** [**PyCon Australia videos**](https://www.youtube.com/playlist?list=PLs4CJRBY5F1KrUr7z_2mur2QdAKXyh-k3)

- [How To Publish A Package On PyPI](https://www.youtube.com/watch?v=QgZ7qv4Cd0Y&t=0s&list=PLs4CJRBY5F1KrUr7z_2mur2QdAKXyh-k3&index=39)
  - Mark Smith [@judy2k](https://twitter.com/judy2k)
[](https://www.youtube.com/watch?v=QgZ7qv4Cd0Y&t=0s&list=PLs4CJRBY5F1KrUr7z_2mur2QdAKXyh-k3&index=39)

**Michael #4:** [**GAE: Introducing App Engine Second Generation runtimes and Python 3.7**](https://cloud.google.com/blog/products/gcp/introducing-app-engine-second-generation-runtimes-and-python-3-7)

- Today, Google Cloud is announcing the availability of Second Generation App Engine standard runtimes, a significant upgrade to the platform that allows you to easily run web apps using up-to-date versions of popular languages, frameworks and libraries.
- Python 3.7 is one of the new Second Generation runtimes that we [announced at Cloud Next](https://cloud.google.com/blog/products/gcp/bringing-the-best-of-serverless-to-you). 
- Based on technology from the [gVisor container sandbox](https://cloud.google.com/blog/products/gcp/open-sourcing-gvisor-a-sandboxed-container-runtime), these Second Generation runtimes eliminate many previous App Engine restrictions, giving you the ability to write portable web apps and microservices that take advantage of App Engine's unique auto-scaling, built-in security and pay-per-use billing model.
- This new runtime allows you to take advantage of Python's vibrant ecosystem of open-source libraries and frameworks. While the Python 2 runtime only allowed the use of specific versions of whitelisted libraries, Python 3 supports arbitrary third-party libraries, including those that rely on C code and native extensions. Just add [Django 2.0](https://docs.djangoproject.com/en/2.0/releases/2.0/), [NumPy](http://www.numpy.org/), [scikit-learn](http://scikit-learn.org/stable/) or your library of choice to a `requirements.txt` file. App Engine will install these libraries in the cloud when you deploy your app.

**Brian #5:** [**I don’t like notebooks**](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g3b55ec3453_0_4)

- [@joelgrus](https://twitter.com/joelgrus)

**Michael #6:** [**PEP 8000 -- Python Language Governance Proposal Overview**](https://www.python.org/dev/peps/pep-8000/)

- This PEP provides an overview of the selection process for a new model of Python language governance in the wake of [Guido's retirement](https://mail.python.org/pipermail/python-committers/2018-July/005664.html). Once the governance model is selected, it will be codified in [PEP 13](https://www.python.org/dev/peps/pep-0013).
- PEPs in the lower 8000s describe the general process for selecting a governance model.
	- [PEP 8001](https://www.python.org/dev/peps/pep-8001) - Python Governance Voting Process
	- [PEP 8002](https://www.python.org/dev/peps/pep-8002) - Open Source Governance Survey
- PEPs in the 8010s describe the actual proposals for Python governance. 
	- [PEP 8010](https://www.python.org/dev/peps/pep-8010) - The BDFL Governance Model
	- [PEP 8011](https://www.python.org/dev/peps/pep-8011) - The Council Governance Model
	- [PEP 8012](https://www.python.org/dev/peps/pep-8012) - The Community Governance Model

Extras

- Free Brian Granger [ACM webcast](https://on.acm.org/t/project-jupyter-from-computational-notebooks-to-large-scale-data-science-with-sensitive-data/879) on Jupyter Friday
- TIOBE jump to #3: https://www.tiobe.com/tiobe-index/
