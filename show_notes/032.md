# Python Bytes 32

**Brian #1:**  [**Introducing Dash**](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)

- UI library for analytical web applications

**Michael #2:** [**Keeping Python competitive**](https://lwn.net/Articles/723949/)

- Article on LWN, interview with Victor Stinner
- He sees a need to improve Python performance in order to keep it competitive with other languages.
- Not as easy to optimize as other languages. For one thing, the C API blocks progress in this area
- Python 3.7 is as fast as Python 2.7 on most benchmarks, but 2.7 was released in 2010. Users are now comparing Python performance to that of Rust or Go, which had only been recently announced in 2010. 
- In his opinion, the Python core developers need to find a way to speed Python up by a factor of two in order for it to continue to be successful.
- JITs may be part of the answer, notably Pyjion by Dino Viehland and Brett Cannon
- An attendee suggested Cython, which does AoT compilation, but its types are not Pythonic. He suggested that it might be possible to use the new type hints and Cython to create something more Pythonic.

**Brian #3:** [**PyPI Quick and Dirty**](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

- A completely incomplete guide to packaging a Python module and sharing it with the world on PyPI. - Hynek Schlawack

**Michael #4:** [**Minimal examples of data structures and algorithms in Python**](https://github.com/keon/algorithms)

- Simple algorithmic examples in Python, including
  - linked lists
  - reversing linked lists
  - GCD
  - Queues
  - Binary search
  - depth first search
  - many, many more

**Brian #5:** [**8 ways to contribute to open source when you have no time**](https://opensource.com/article/17/6/find-time-contribute)

- 

**Michael #6:** [**NumPy receives first ever funding, thanks to Moore Foundation**](https://www.numfocus.org/blog/numpy-receives-first-ever-funding-thanks-to-moore-foundation/)

- For the first time ever, NumPy—a core project for the Python scientific computing stack—has received grant funding.
- The proposal, “[Improving NumPy for Better Data Science](https://www.moore.org/grant-detail?grantId=GBMF5447)” will receive $645,020 from the Moore Foundation over 2 years, with the funding going to UC Berkeley Institute for Data Science. 
- The principal investigator is [Dr. Nathaniel Smith](https://bids.berkeley.edu/people/nathaniel-smith).
- The NumPy project was started in 2006 by [Travis Oliphant](https://www.numfocus.org/about/people/advisory-council/).

