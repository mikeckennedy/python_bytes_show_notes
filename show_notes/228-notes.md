# Python Bytes 228

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**pytest book**](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Special guest** 
- [**Guy Royse**](https://twitter.com/guyroyse)

**Brian #1:** [**How to make an awesome Python package in 2021**](https://antonz.org/python-packaging/)

- Anton Zhiyanov, [@ohmypy](https://twitter.com/ohmypy)
- Also thanks John Mitchell, [@JohnTellsAll](https://twitter.com/JohnTellsAll) for posting about it.
- Great writing taking you through everything in a sane order.
	- Stubbing a project
    - with just `.gitignore` and a directory with a stub `__init__.py`.
	- Test packaging and publishing
    - use `flit init` to create initial pyproject.toml
    - set up your `~/.pypirc` file
    - publish to the test repo
	- Make the real thing 
    - make an implementation
    - publish
	- Extras
    - Adding `README.md` & `CHANGELOG.md` and updating `pyproject.toml` to include `README.md` and a Python version selector.
    - Adding linting and testing with pytest, tox, coverage, and others
    - Building in the cloud with GH Actions, Codecov, Code Climate
    - Adding badges
    - Task automation with a Makefile
    - Publishing to PyPI from a GH Action
- Missing (but possibly obvious):
	- GitHub project
	- Checking your project name on PyPI early
- Super grateful for:
	- Do all of this early in the project
	- Using `flit publish --repository pypitest` and spelling out how to set up a `~/.pypirc` file.
	- Start to finish workflow
	- Example project with all filled out project files

**Michael #2:** [**Kubestriker**](https://github.com/vchinnipilli/kubestriker)
Kubestriker performs numerous in depth checks on kubernetes infra to identify the security misconfigurations

- Focuses on running in production and at scale.
- **kubestriker** is Platform agnostic and works equally well across more than one platform such as self hosted [kubernetes](https://kubernetes.io/), [Amazon EKS](https://aws.amazon.com/eks), [Azure AKS](https://azure.microsoft.com/en-us/services/kubernetes-service/), [Google GKE](https://cloud.google.com/kubernetes-engine) etc.
- Current Capabilities
	- Scans Self Managed and cloud provider managed kubernetes infra
	- Reconnaissance phase checks for various services or open ports
	- Performs automated scans incase of insecure, readwrite or readonly services are enabled
	- Performs both authenticated scans and unauthenticated scans
	- Scans for wide range of IAM Misconfigurations in the cluster
	- Scans for wide range of Misconfigured containers
	- Scans for wide range of Misconfigured Pod Security Policies
	- Scans for wide range of Misconfigured Network policies
	- Scans the privileges of a subject in the cluster
	- Run commands on the containers and streams back the output
	- Provides the endpoints of the misconfigured services
	- Provides possible privilege escalation details
	- Elaborative report with detailed explanation

**Guy #3:** [**wasmtime**](https://wasmtime.dev/)

- WebAssembly runtime with support for:
	- Python, Rust, C, Go, .NET
	- Documentation here: https://docs.wasmtime.dev/
- Supports [WASI](https://wasi.dev/) (Web Assembly System Interface):
	- WASI supports IO operations—it does for WebAssembly what Node.js did for JavaScript

**Brian #4:** [**Depend-a-lot-bot**](https://github.com/apps/depend-a-lot-bot)

- Anthony Shaw, [@anthonypjshaw](https://twitter.com/anthonypjshaw)
- A bot for GitHub that automatically approves + merges PRs from dependabot and PyUp.io when they meet certain criteria:
	- All the checks are passing
	- The package is on a safe-list (see configuration)
- Example picture shows an auto approval and merge of a tox version update, showing “This PR looks good to merge automatically because tox is on the save-list for this repository”.
- Configuration in a .yml file. *I learned recently that most programming jobs that can be automated eventually devolve into configuring a yml file.*

**Michael #5:** [**Supreme Court sides with Google in API copyright battle with Oracle**](https://arstechnica.com/tech-policy/2021/04/supreme-court-sides-with-google-in-api-copyright-battle-with-oracle/)

- The Supreme Court has [sided with Google](https://www.supremecourt.gov/opinions/20pdf/18-956_d18f.pdf) in its decade-long legal battle with Oracle over the copyright status of application programming interfaces. 
- The ruling means that Google will not owe Oracle billions of dollars in damages. It also has big implications for the broader software industry
- The ruling heads off an expected wave of lawsuits over API copyrights.
- The case dates back to the creation of the Android platform in the mid-2000s.
- Google independently implemented the Java API methods, but to ensure compatibility, it copied Java's method names, argument types, and the class and package hierarchy.
- Over a decade of litigation, Google won twice at the trial court level, but each time, the [ruling](https://law.justia.com/cases/federal/appellate-courts/cafc/13-1021/13-1021-2014-05-09.html) was [overruled](https://arstechnica.com/tech-policy/2018/03/googles-use-of-the-java-api-packages-was-not-fair-appeals-court-rules/) by the Federal Circuit appeals court. The case finally [reached the Supreme Court](https://arstechnica.com/tech-policy/2020/10/googles-supreme-court-faceoff-with-oracle-was-a-disaster-for-google/) last year.
- Writing for a six-justice majority, Justice Stephen Breyer held that Google's **copying of the Java API calls was permissible under copyright's fair use doctrine**.

**Guy #6:** [**RedisAI**](https://oss.redislabs.com/redisai/)

- Module for Redis that add AI capabilities
- Turns Redis into a model server:
	- Supports TF, PyTorch, and [ONNX](https://onnx.ai/) models
- Adds the TENSOR data type
- ONNX + Redis has positive architectural implications
    

**Extras**

**Michael**

- [**git for Windows**](https://gitforwindows.org/)
- [**JupyterLab reaches v3**](https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb) (via via Allan Hansen)
- [**Why not support Python letter by Brian Skinn**](https://gist.github.com/bskinn/cde59de17d00f8260197f6a866f6155d)
- [**Django 3.2 is out & is LTS**](https://www.djangoproject.com/weblog/2021/apr/06/django-32-released/)
- [**PyCharm 2021.1**](https://blog.jetbrains.com/pycharm/2021/04/pycharm-2021-1/) just dropped with [**Code With Me**](https://www.jetbrains.com/code-with-me/)

**Brian**

- [The PSF is hiring a Developer-in-Residence to support CPython!](https://pyfound.blogspot.com/2021/04/the-psf-is-hiring-developer-in.html)


**Joke** 

- [**Vim Escape Rooms**](https://twitter.com/anthonypjshaw/status/1377834823268458498)
- [**Happiness**](https://twitter.com/towernter/status/1379525329778262021?s=20)

