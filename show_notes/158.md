# Python Bytes 158

This episode is sponsored by DigitalOcean - [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian** **#1:** [**Python already replaced Excel in banking**](https://news.efinancialcareers.com/us-en/3002556/python-replaced-excel-banking)

- “If you wanted to prove your mettle as an [entry-level banker](https://news.efinancialcareers.com/uk-en/167611/banks-weird-hierarchies-analysts-associates-vps-mds-really) or trader it used to be the case that you had to know all about financial modeling in Excel. Not any more. These days it's all about [Python](https://news.efinancialcareers.com/us-en/327770/python-for-finance), especially on the trading floor. 
- "Python already replaced Excel," said Matthew Hampson, deputy chief digital officer at Nomura, speaking at last Friday's Quant Conference in London. "You can already walk across the trading floor and see people writing Python code...it will become much more common in the next three to four years."

**Michael #2:** [**GitHub launches 'Security Lab' to help secure open source ecosystem**](https://www.zdnet.com/article/github-launches-security-lab-to-help-secure-open-source-ecosystem/)

- At the GitHub Universe developer conference, GitHub announced the launch of a new community program called [Security Lab](https://securitylab.github.com/)
- GitHub says Security Lab founding members have found, reported, and helped fix more than 100 security flaws already.
- Other organizations, as well as individual security researchers, can also join. A bug bounty program with rewards [of up to $3,000](https://securitylab.github.com/bounties) is also available, to compensate bug hunters for the time they put into searching for vulnerabilities in open source projects.
- Bug reports must contain a CodeQL query. [CodeQL](https://securitylab.github.com/tools/codeql) is a new open source tool that GitHub released today; a semantic code analysis engine that was designed to find different versions of the same vulnerability across vasts swaths of code.
- Starting today automated security updates are generally available and have been rolled out to every active repository with security alerts enabled.
- Once a security flaw is fixed, the project owner can publish the security, and GitHub will warn all upstream project owners who are using vulnerable versions of the original maintainer's code.
- But before publishing a security advisory, project owners can also request and receive a CVE number for their project's vulnerability directly from GitHub.
- And last, but not least, GitHub also updated Token Scanning, its in-house service that can scan users' projects for API keys and tokens that have been accidentally left inside their source code.

**Brian #3:** [**pybit.es now has some test challenges**](https://pybit.es/launch-pytest-bites.html)

- Uses [pytest](https://pytest.org/en/latest/), [coverage.py](https://coverage.readthedocs.io), and [mutpy](https://pypi.org/project/MutPy/) (for mutation testing)
- Most other challenges have tests that validate the code you write.
- New challenges (3 so far) have you write the tests for existing code.
- Tests are evaluated with both coverage.py and mutpy
- another mutation testing tool is [mutmut](https://pypi.org/project/mutmut/), [written about earlier this year by Ned Badtchelder](https://nedbatchelder.com/blog/201903/mutmut.html).

**Michael #4:** [**pyhttptest - a command-line tool for HTTP tests over RESTful APIs**](https://github.com/slaily/pyhttptest)

- via [Florian Dahlitz](https://twitter.com/DahlitzF/status/1186665573968764928)
- A command-line tool for HTTP tests over RESTful APIs
- Tired of writing test scripts against your RESTFul APIs anytime? Describe an HTTP Requests test cases in a simplest and widely used format JSON within a file. Run one command and gain a summary report.
- Example
```
    {
      "name": "TEST: List all users",
      "verb": "GET",
      "endpoint": "users",
      "host": "https://github.com",
      "headers": {
        "Accept-Language": "en-US"
      },
      "query_string": {
        "limit": 5
      }
    }
```

**Brian #5:** [**xarray**](http://xarray.pydata.org)

- suggested by Guido Imperiale
- xarray is a mature library that builds on top of numpy, pandas and dask to offer arrays that are
	- n-dimensional (numpy and dask do it, but pandas doesn't)
	- self-described and indexed (pandas does it, but numpy and dask don't)
	- out-of-memory, multi-threaded, and cloud-distributed (dask does it, but numpy and pandas don't).
- Additionally, xarray can semi-transparently swap numpy with other backends, such as [sparse](https://sparse.pydata.org/) , while retaining the same API.

**Michael #6:** ****[**Animated SVG Terminals**](https://github.com/nbedos/termtosvg)

- [Florian Dahlitz](https://twitter.com/DahlitzF/status/1196091243450839041)
- **termtosvg** is a Unix terminal recorder **written in Python** that renders your command line sessions as standalone SVG animations.
- Features:
	- Produce lightweight and clean looking animations or still frames embeddable on a project page
	- Custom color themes, terminal UI and animation controls via user-defined [SVG templates](https://github.com/nbedos/termtosvg/blob/develop/man/termtosvg-templates.md)
	- Rendering of recordings in asciicast format made with asciinema
- Examples: [nbedos.github.io/termtosvg/pages/examples.html](https://nbedos.github.io/termtosvg/pages/examples.html)

**Extras**

- [pytest 5.3.0](https://docs.pytest.org/en/latest/changelog.html#pytest-5-3-0-2019-11-19) released, please read [changelog](https://docs.pytest.org/en/latest/changelog.html#pytest-5-3-0-2019-11-19) if you use pytest, especially if you use it with CI and depend on `--junitxml`, as they have changed the format to a newer version.

Michael: 

- [PyCon registration](https://us.pycon.org/2020/) is open (via Jacqueline Wilson)
- Facebook: [Microsoft's Visual Studio Code is now our default development platform](https://www.zdnet.com/article/facebook-microsofts-visual-studio-code-is-now-our-default-development-platform/)
- Black friday at Talk Python Training!
- New course coming soon: Python for the .NET developer

**Jokes**

- What do you get when you put root beer in a square glass? Beer.

- **Q:** What do you call optimistic front-end developers?
- **A:** Stack half-full developers.
    
- Also, I was going to tell a version control joke, but they are only funny if you ***git*** them.

