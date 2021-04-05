# Python Bytes 227

Sponsored by **us!**
Special guest: [**Micaela Reyes**](https://twitter.com/codemickeycode)

**Brian #1:** **Number One, that's "retract plank," not "remove plank."**

- Yanking vs removing versions on PyPI
- [https://twitter.com/nedbat/status/1376901333958201352?s=20](https://twitter.com/nedbat/status/1376901333958201352?s=20)
[- https://pypi.org/help/#yanked](https://pypi.org/help/#yanked)
- see also [https://doughellmann.com/posts/so-youve-released-a-broken-package-to-pypi-what-do-you-do-now/](https://doughellmann.com/posts/so-youve-released-a-broken-package-to-pypi-what-do-you-do-now/)


**Michael #2:** [**SQLAlchemy 1.4.0 Released**](https://www.sqlalchemy.org/blog/2021/03/15/sqlalchemy-1.4.0-released/)

- Exciting: 1st release to properly support an [**async API**](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm)
- Has a new `select()` + `execute()` rather than `session.query()` API
- Intended to unify Core and ORM.
- See [**new vs. old API compared**](https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-orm-usage).
- Requires aiosqlite for async API + SQLite: `conn_str = 'sqlite+aiosqlite:///filename'`

**Micaela #3:** [**django-tenants**](https://github.com/django-tenants/django-tenants)

- by [Tom Turner](https://github.com/tomturner)
- Multi-tenancy Implementation for Django (typically for SaaS websites e.g. Shopify)
- currently on v3.2.1 (Aug 2020) release
- Requirements: Django 2 and PostgreSQL
- It was largely based on `django-tenant-schemas` library
- Data Architecture: shared database, separate schema for each tenant
- Domain setup / URL routing for root and per tenant:
	- Examples:
		- http://my-domain.com:8000/
		- http://tenant.my-domain.com:8000/
		- http://tenant2.my-domain.com:8000/
- Possible Use-cases:
	- a hospital with different branches
	- restaurant franchise with different branches
- Possible Limitations:
	- You can’t use the normal migration commands (`python manage.py migrate_schemas` instead of `python manage.py migrate`)
	- Reports - when you need to create a report regarding all the clients/tenants, tenant data will be on separate schemas
- see also: [How to get Django Tenants up and Running](https://paper.dropbox.com/doc/Python-Bytes-227--BH9SEMD~TSzQVy__6P4cupRSAQ-uWYJJnYTkn2pA7seRCCcJ)

**Brian #5:** [**pre-commit ci**](https://pre-commit.ci/)

- [pre-commit](https://pre-commit.com/) is “a framework for managing and maintaining multi-language pre-commit hooks.”
- Hooks can be run during commits, but also hooked other events, such as merge, push, after switching branches, etc.
- Even if you run pre-commit yourself, it’d be nice to make sure all hooks are run by people submitting pull requests.
- [**pre-commit ci**](https://pre-commit.ci/) ****is a service that “enforces that these issues are discovered (which is opt-in for each developer's workflow via **pre-commit**) but also fixes the issues automatically, letting developers focus their time on more valuable problems.”

**Michael #4:** [**Snyk (Python) Package Advisor**](https://snyk.io/advisor/python)

- via [**David Smit**](https://twitter.com/davidouglasmit/status/1373476836555042816)
- Provides package health score, built up from
	- Popularity
	- Maintenance
	- Security
	- Community
- Code of conduct and related metrics
- Number of releases, commits, maintainers, age, etc.
- Lots of nice graphs and ways you can contribute


**Micaela #6:** [**PyWebIO**](https://pywebio.readthedocs.io/)

- by [Wang Weimin](https://github.com/wang0618)
- Allows you build simple web applications or browser-based GUI applications without the need to write HTML and JavaScript.
- Has input and output modules
- Based on tornado
- Possible Use-cases:
	- Hobby projects - for people who know how to write Python code but want to do away with JavaScript
	- Could be a good teaching tool - ex. if you’re teaching kids or beginners and you want to make them appreciate the concept of input and output
- Possible Limitation: once you need to style your HTML, it might be a bit difficult to do so since it’s tightly coupled with the Python code

**Extras**

**Michael**

- [**absolufy-imports**](https://github.com/MarcoGorelli/absolufy-imports) by Marco Gorelli
- Anthony Shaw actually made [**a Beanie Baby in the terminal**](https://twitter.com/anthonypjshaw/status/1374976709968060416) within a day of the last episode!
- [**PHP supply chain hack**](https://arstechnica.com/gadgets/2021/03/hackers-backdoor-php-source-code-after-breaching-internal-git-server/)

**Brian**

- packages: pytest-yuk, pytest-srcpaths, pytest-check

**Micaela**

- Last day of March membership drive for the PSF https://twitter.com/ThePSF/status/1377000184375296003

**Joke:** [**Commenting your code**](https://twitter.com/riferrei/status/1358180071081713670)

![](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/6026df817e1cf8188020173d/3e4539e3271c4954e92a946f7c3d931d/Etk5k5uXUAMajx9.jpg)
