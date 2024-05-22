# Python Bytes 300

Sponsored by [**Microsoft for Startups Founders Hub**](http://pythonbytes.fm/foundershub2022).

Special guest: **[Seth Larson](https://twitter.com/sethmlarson)**


**Brian #1:** **Test your packages and wheels**

- I’ve been building some wheels the last couple of weeks with various tools:
    - flit, flit-core, and flit build
    - hatch, hatchling, and hatch build
    - setuptools, build_meta, and python -m build
- There are a few projects I’ve used to make sure my projects are in good shape
    - [wheel-inspect](https://pypi.org/project/wheel-inspect/) - you can inspect within Python code through `inspect_wheel()` function that converts to json. Or use on the command line with `wheel2json`
    - [check-wheel-contents](https://pypi.org/project/check-wheel-contents/) - a linter for wheels
    - [tox](https://pypi.org/project/tox/) - easily test the building, installation, and running of a package locally
        - I actually start here, then utilize the other two tools
- Should have been obvious, but it wasn’t to me
    - Projects saved on git (such as gitHub) don’t keep wheels in git. (this was obvious)
    - When installing from git using `pip install git+https://path/to/git/repo.git` 
        - Your local pip will run the packaging backend to build the wheel before installing.
        - Yet another way to test packaging.

**Michael #2:**  [**The Jupyter+git problem is now solved**](https://www.fast.ai/2022/08/25/jupyter-git/)

- Jupyter notebooks don’t work with git by default (they inherently have meaningless conflicts).
- With [nbdev2](https://nbdev.fast.ai/), the Jupyter+git problem has been totally solved. 
- Uses a set of hooks which provide clean git diffs, solve most git conflicts automatically, and ensure that any remaining conflicts can be resolved entirely within the standard Jupyter notebook environment.
- The techniques used to make the merge driver work are quite fascinating

**Seth #3:** [**Help us test system trust stores in Python**](https://sethmlarson.dev/blog/help-test-system-trust-stores-in-python)

- Package aiming to replace certifi called “truststore”, use system trust stores for HTTPS instead of a static list of certificates.
- Problem truststore is solving usually manifests in corporate networks: “unable to get local issuer certificate”.
- Experimental support added to pip to prove the implementation
- Users can try out the functionality and report issues.


**Brian #4:** [**Making plots in your terminal with plotext**](https://pybit.es/articles/terminal-plotting-with-plotext/?utm_source=pocket_mylist)

- Bob Belderbos
- Tutorial on using [plotext](https://pypi.org/project/plotext/) - that’s one t in the middle
- With the rise of CLI usage, plots are a nice addition.
- Bob’s plot is great, but check out the options in the plotext docs
    - lots-o-plots
    - streaming data
    - images
    - subplots
- so fun

**Michael #5:** [**jinja2-fragments**](https://github.com/sponsfreixes/jinja2-fragments)

- Carson from HTMX (see [podcast](https://talkpython.fm/episodes/show/321/htmx-clean-dynamic-html-pages) and [course](https://training.talkpython.fm/courses/htmx-flask-modern-python-web-apps-hold-the-javascript)) wrote about [**template fragments**](https://htmx.org/essays/template-fragments/).
- My jinja_partials project sorta fulfills this, but not really.
- I had [**a nice discussion**](https://twitter.com/sponsfreixes/status/1566671693774348288) with Sergi Pons Freixes who uses jinja_partials about this.
- He created [**Jinja2 fragments**](https://github.com/sponsfreixes/jinja2-fragments)

**Seth #6:** [**SLSA 3 Generic Builder for GitHub Actions GA**](https://slsa.dev/blog/2022/08/slsa-github-workflows-generic-ga)

- Supply chain Levels for Software Artifacts, or SLSA (“salsa”)
- Tools to attest to and verify “provenance” of artifacts, ie “where it came from”
- Prove cryptographically that artifacts are built from a specific GitHub repository, commit, tag. Another future defense against stolen PyPI credentials/accounts.
- Generic builder means you can sign anything, like wheels/sdists

**Extras** 

Brian: 

- Bring your pytest books to [PyBay](https://pybay.com), if you want them signed.
    - I’m only bringing a small amount.
- I’ll be presenting 
    - "Sharing is Caring - pytest fixture edition” at 3:05
    - “Experts Panel on Testing in Python” at 7:00
- And be a zombie on my 8 am flight back unless I can change my reservation.
- That’s this weekend, Sat Sept 10, in SF

Michael:

- [**Heroku announces plans to eliminate free plans**](https://techcrunch.com/2022/08/25/heroku-announces-plans-to-eliminate-free-plans-blaming-fraud-and-abuse/)
- [**Banned paywalls**](https://www.extremetech.com/extreme/339162-white-house-bans-paywalls-on-taxpayer-funded-research?source=science)
- PyPI phished identified: [**Actor Phishing PyPI Users Identified**](https://www.darkreading.com/application-security/researchers-identify-threat-actor-behind-recent-phishing-attack-targeting-pypi-users) and [**Actors behind PyPI supply chain attack have been active since late 2021**](https://arstechnica.com/information-technology/2022/09/actors-behind-pypi-supply-chain-attack-have-been-active-since-late-2021/)
- [**Major Python CVE**](https://twitter.com/btskinn/status/1566528546872385542?cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email)**:** [CVE-2020-10735: Prevent DoS by large int<->str conversions](https://twitter.com/btskinn/status/1566528546872385542?cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email)

Seth: 

- [Pyxel, retro game engine for Python](https://github.com/kitao/pyxel), v1.8.0 added experimental [web support](https://twitter.com/kitao/status/1564234852185960449) with WASM

**Joke:**  [**Dev just after work**](https://twitter.com/iamsegunajibola/status/1564996116550242305)

