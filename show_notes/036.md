# Python Bytes 36
Brought to you by **Rollbar**! Create an account and get special credits at https://pythonbytes.fm/rollbar

**Brian #1:** [**Craft Your Python Like Poetry**](http://treyhunner.com/2017/07/craft-your-python-like-poetry/)

- Line length is important. Shorter is often more readable.
- line break placement makes a huge difference in readability and applies to
  - comprehensions
  - function call parameters
  - chained function calls. (Dot alignment is pleasing and nothing I have considered previously)
  - dictionary literals

[](https://trello.com/c/ME7ijnKw/88-https-devguidepythonorg)
**Michael #2:** [**The Fedora Python Classroom Lab**](https://labs.fedoraproject.org/en/python-classroom/)

- Makes it easy for teachers and instructors to use Fedora in their classrooms or workshops.
- Ready to use operating system with important stuff pre-installed
- With GNOME or as a headless environment for Docker or Vagrant
- Lots of prebuilt goodies, especially around data science:
  - IPython, Jupyter Notebook, multiple Pythons, virtualenvs, tox, git and more

**Brian #3:** [**How a VC-funded company is undermining the open-source community**](https://theoutline.com/post/1953/how-a-vc-funded-company-is-undermining-the-open-source-community)

- A San Francisco startup called Kite is being accused of underhanded tactics.
- An Atom plugin called Minimap, downloaded more than 3.5 M times, open source, and developed primarily by one person. @abe33
- abe33 hired by Kite, then adds a “Kite Promotion” “feature” to Minimap that examines user code and inserts links to related parts of Kite website. (Presumably in the minimap?)
- Users rightfully ticked.
- Next. autocomplete-Python, also an Atom addon, seems to be taken over by Kite engineers and changes the autocomplete from local Jedi engine to cloud Kite engine (also therefore sending users code to Kite). 
- Seems like that ought to have been a separate plugin, not a take over of an existing one.
- Again, users not exactly supportive of the changes.

**Michael #4:** [**Newspaper Python Package**](https://github.com/codelucas/newspaper/)

- News, full-text, and article metadata extraction in Python 3
- Behold the example code:

```
    from newspaper import Article
    url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    article = Article(url)
    
    article.download()
    
    article.parse()
    article.authors
    # ['Leigh Ann Caldwell', 'John Honway']
    article.publish_date
    # datetime.datetime(2013, 12, 30, 0, 0)
    
    article.nlp()
    article.keywords
    # ['New Years', 'resolution', ...]
    article.summary
    # 'The study shows that 93% of people ...'
```

**Brian #5:** [**IEEE Spectrum:**](http://spectrum.ieee.org/static/interactive-the-top-programming-languages-2017) [**The Top Programming Languages 2017**](http://spectrum.ieee.org/static/interactive-the-top-programming-languages-2017)

- We’re #1. We’re #1.
- Python on top of the list
- IEEE very open about [their methodology.](http://spectrum.ieee.org/ns/IEEE_TPL_2017/methods.html)
  - Combo of Google, Google Trends, GitHub, Twitter, Reddit, StackOverflow, HackerNews, CareerBuilder, Dice, and IEEE Xplore Digital Library
- Python #1 in lots of categories. Java still has more job openings, supposedly. Although I think it’s because Java people are quitting to go work on Python projects. 

**Michael #6:** [**SciPy 2017 videos are out**](https://www.youtube.com/playlist?list=PLYx7XA2nY5GfdAFycPLBdUDOUtdQIVoMf)

- Bunch of tutorials
- Keynote - Coding for Science and Innovation, Gaël Varoquaux
- Dash - A New Framework for Building User Interfaces for Technical Computing, 
- Dask - Advanced Techniques, Matthew Rocklin
- Scientific Analysis at Scale - a Comparison of Five Systems, Jake V.
- Keynote - Academic Open Source, Kathryn Huff
- Plus lots more

