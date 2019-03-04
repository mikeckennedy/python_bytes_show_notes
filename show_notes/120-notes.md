# Python Bytes 120
 Sponsored by [**pythonbytes.fm/digitalocean**](http://pythonbytes.fm/digitalocean)

**Brian #1:** [**The Ultimate Guide To Memorable Tech Talks**](https://medium.com/@nnja/the-ultimate-guide-to-memorable-tech-talks-e7c350778d4b)

- Nina Zakharenko
- 7 part series that covers choosing a topic, writing a talk proposal, tools, planning, writing, practicing, and delivering the talk
- I’ve just read the tools section, and am looking forward to the rest of the series.
	- From the tools section: “I noticed I’d procrastinate on making the slides look good instead of focusing my time on making quality content.”

**Michael #2:** ****[**Running Flask on Kubernetes**](https://testdriven.io/blog/running-flask-on-kubernetes/?source=4320ef6a6395)

- via TestDriven.io & Michael Herman
- What is Kubernetes?
- A step-by-step tutorial that details how to deploy a Flask-based microservice (along with Postgres and Vue.js) to a Kubernetes cluster.
- Goals of tutorial
	1. Explain what container orchestration is and why you may need to use an orchestration tool
	2. Discuss the pros and cons of using Kubernetes over other orchestration tools like Docker Swarm and Elastic Container Service (ECS)
	3. Explain the following Kubernetes primitives - Node, Pod, Service, Label, Deployment, Ingress, and Volume
	4. Spin up a Python-based microservice locally with Docker Compose
	5. Configure a Kubernetes cluster to run locally with Minikube
	6. Set up a volume to hold Postgres data within a Kubernetes cluster
	7. Use Kubernetes Secrets to manage sensitive information
	8. Run Flask, Gunicorn, Postgres, and Vue on Kubernetes
	9. Expose Flask and Vue to external users via an Ingress

**Brian #3**: **Changes in the CI landscape**

- [Travis CI joins the Idera family](https://blog.travis-ci.com/2019-01-23-travis-ci-joins-idera-inc) - TravisCI blog
- [#travisAlums](https://twitter.com/hashtag/travisAlums?src=hash&ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1098583889864478720&ref_url=https%3A%2F%2Fabout.gitlab.com%2F2019%2F02%2F21%2Fci-cd-market-consolidation%2F) on Twitter
	- [“TravisCI is laying off a bunch of senior engineers and other technical staff. Look at the #travisAlums hashtag and hire them!”](https://twitter.com/alicegoldfuss/status/1098604563664420865) - alicegoldfuss
- options: [GitHub lists 17 options for CI](https://github.com/marketplace/category/continuous-integration), including GitLab & Azure Pipelines
	- Some relevant articles, resources:
		- [The CI/CD market consolidation](https://about.gitlab.com/2019/02/21/ci-cd-market-consolidation/) - GitLab article
		- [Azure Pipelines with Python — by example](https://medium.com/@anthonypjshaw/azure-pipelines-with-python-by-example-aa65f4070634) - Anthony Shaw
		- [pytest-azurepipelines](https://github.com/tonybaloney/pytest-azurepipelines) - Anthony Shaw
		- [Azure Pipelines Templates](https://github.com/asottile/azure-pipeline-templates) - Anthony Sottile

**Michael #4:** [Python server setup for macOS 🍎](https://github.com/zachvalenta/nginx-wsgi)

- **what**: hello world for Python server setup on macOS 
- **why**: most guides show setup on a Linux server (which makes sense) but macoS is useful for learning and for local dev
- STEP 1: NGINX ➡️ STATIC ASSETS
- STEP 2: GUNICORN ➡️ FLASK
- STEP 3: NGINX ➡️ GUNICORN

**Brian #5:** [**Learn Enough Python to be Useful: argparse**](https://towardsdatascience.com/learn-enough-python-to-be-useful-argparse-e482e1764e05) 

- How to Get Command Line Arguments Into Your Scripts - Jeff Hale
- “argparse is the “recommended command-line parsing module in the Python standard library.” It’s what you use to get command line arguments into your program.
- “I couldn’t find a good intro guide for argparse when I needed one, so I wrote this article.”

**Michael #6:** [AWS, MongoDB, and the Economic Realities of Open Source](https://stratechery.com/2019/aws-mongodb-and-the-economic-realities-of-open-source/)

- Related podcast: https://soundcloud.com/exponentfm/episode-159-inverted-pyramids
- Last week, from the [AWS blog](https://aws.amazon.com/blogs/aws/new-amazon-documentdb-with-mongodb-compatibility-fast-scalable-and-highly-available/):
  > Today we are launching [Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb/), a fast, scalable, and highly available document database that is designed to be compatible with your existing MongoDB applications and tools. Amazon DocumentDB uses a purpose-built SSD-based storage layer, with 6x replication across 3 separate Availability Zones. The storage layer is distributed, fault-tolerant, and self-healing, giving you the the performance, scalability, and availability needed to run production-scale MongoDB workloads.


- Like an increasing number of such projects, MongoDB is open source…or it was anyways. MongoDB Inc., a venture-backed company that IPO’d in October, 2017, made its core database server product available under the [GNU Affero General Public License (AGPL)](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License).
- AGPL extended the GPL to apply to software accessed over a network; since the software is only being used, not copied
- MongoDB’s Business Model
- We believe we have a highly differentiated business model that combines the developer mindshare and adoption benefits of open source with the economic benefits of a proprietary software subscription business model.
- + MongoDB enterprise and MongoDB atlas
- Basically, MongoDB sells three things on top of its open source database server:
	- Additional tools for enterprise companies to implement MongoDB
	- A hosted service for smaller companies to use MongoDB
	- Legal certainty
- What AWS Sells
- the value of software is typically realized in three ways:
	- First is hardware. 
	- Second is licenses. This was Microsoft’s core business for decades: licenses sold to OEMs (for the consumer market) or to companies directly (for the enterprise market). 
	- Third is software-as-a-service.
- AWS announced last week:
  > The storage layer is distributed, fault-tolerant, and self-healing, giving you the the performance, scalability, and availability needed to run production-scale MongoDB workloads.
- AWS is not selling MongoDB: what they are selling is “performance, scalability, and availability.” DocumentDB is just one particular area of many where those benefits are manifested on AWS.
- Thus we have arrived at a conundrum for open source companies:
	- MongoDB leveraged open source to gain mindshare.
	- MongoDB Inc. built a successful company selling additional tools for enterprises to run MongoDB.
	- More and more enterprises don’t want to run their own software: they want to hire AWS (or Microsoft or Google) to run it for them, because they value performance, scalability, and availability.
- This leaves MongoDB Inc. not unlike the record companies after the advent of downloads: what they sold was not software but rather the tools that made that software usable, but those tools are increasingly obsolete as computing moves to the cloud. And now AWS is selling what enterprises really want.
- This tradeoff is inescapable, and it is fair to wonder if the golden age of VC-funded open source companies will start to fade (although not open source generally). The monetization model depends on the friction of on-premise software; once cloud computing is dominant, the economic model is much more challenging.

**Extras:**

[PyTexas](https://twitter.com/hashtag/PyTexas?src=hashtag_click) 2019 at [#Austin](https://twitter.com/hashtag/Austin?src=hashtag_click) on Apr 13th and 14th. Registrations now open. More info at [pytexas.org/2019/](https://t.co/6ZkLqWws2F?amp=1)

Michael: Sorry Ant!

Michael: RustPython follow up: [https://rustpython.github.io/](https://rustpython.github.io/)demo/

**Joke:**

* **Q:** Why was the developer unhappy at their job?
* **A:** They wanted arrays.

* **Q:** Where did the parallel function wash its hands?
* **A:** Async

