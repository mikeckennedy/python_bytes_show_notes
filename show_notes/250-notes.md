# Python Bytes 250


Sponsored by **us:**

- Check out the [**courses over at Talk Python**](https://training.talkpython.fm/courses/all)
- And [**Brian’s book too**](https://pythontest.com/pytest-book/)!

Special guest: **Prayson Daniel**

**Brain #1:** [**Exciting New Ways To Be Told That Your Python Code is Bad**](https://nickdrozd.github.io/2021/09/02/new-pylint-checks.html)

- Two new pylint errors
	- consider-ternary-expression
```
    if condition():
        x = 4
    else:
        x = 5
```

``` 
    x = 4 if condition() else 5
```

- while-used
	- it unconditionally flags every use of while expressions.
	- generally, while should be avoided.

**Michael #2:** [**GitHub Readme Stats**](https://github.com/anuraghazra/github-readme-stats)

- via Роман Великий
- Dynamically generated stats for your github readmes
- This are for your repo or your stats (others too I suppose) posted somewhere outside of github
- Card for a project: [https://github-readme-stats.vercel.app/api/pin/?username=mikeckennedy&repo=python-switch](https://github-readme-stats.vercel.app/api/pin/?username=mikeckennedy&repo=python-switch)
- Card for a user: [https://github-readme-stats.vercel.app/api?username=mikeckennedy&show_icons=true&theme=radical](https://github-readme-stats.vercel.app/api?username=mikeckennedy&show_icons=true&theme=radical)
- Card for your languages: [https://github-readme-stats.vercel.app/api/top-langs/?username=mikeckennedy&repo=python-switch](https://github-readme-stats.vercel.app/api/top-langs/?username=mikeckennedy&repo=python-switch)

**Prayson #3:**  [**Nox**](https://nox.thea.codes/en/stable/)

- Nox appeared as “footnotes” in Episodes 182 and 248 (Hypermodern Python …)
- It does [tox](https://tox.readthedocs.io/en/latest/) what [invoke](http://www.pyinvoke.org/) did (substituting GNU Make) 

**Brian #4:** **Two tools for dealing with text**

- [python-easyfrontmatter](https://github.com/eyeseast/python-frontmatter) - a small package to load and parse files (or just text) with YAML (or JSON, TOML or other) front matter.
```
    >>> post = frontmatter.load('tests/yaml/hello-world.txt')
    >>> print(post['title'])
    Hello, world!
```
- Tried it with a helper script I’m using with Hugo, and it parses Hugo metadata in blog posts like a dream.
- [ftfy](https://ftfy.readthedocs.io/en/v6.0/) - fixes text for you
- “Take in bad Unicode and output good Unicode”
```
    >>> import ftfy
    >>> ftfy.fix_text('âœ” No problems')
    '✔ No problems'
```

**Michael #5:** [**MPIRE (MultiProcessing Is Really Easy)**](https://github.com/Slimmer-AI/mpire)

- A Python package for easy multiprocessing, but faster than multiprocessing
- It combines the 
- convenience of map like functions of `multiprocessing.Pool` 
- with the benefits of using copy-on-write shared objects of `multiprocessing.Process`, 
- together with easy-to-use worker state, worker insights, and progress bar functionality.
- [Many features](https://github.com/Slimmer-AI/mpire#features)
- Requisite shoutout to [**unsync**](https://asherman.io/projects/unsync.html) too.

**Prayson #6:** [**skorch**](https://github.com/skorch-dev/skorch)

- Going deep learning with scikit-learn pipelines (Breaking limits of [multi-layer perceptron (MLP)](https://scikit-learn.org/stable/modules/neural_networks_supervised.html))
- Using PyTorch, skorch provides an API to extend neural networks models in scikit-learn.
- Example: [Penguins Classification shameless Gist](https://gist.github.com/Proteusiq/9fb0f07a2887e124d99a219047f76e88)

**Extras**

Michael

- [**vim + jupyter**](https://github.com/jupyterlab-contrib/jupyterlab-vim), via Marco Gorelli
- [**PyBay talk**](https://twitter.com/mkennedy/status/1437988254213570560)

Prayson

- [python-decouple](https://github.com/henriquebastos/python-decouple/)

**Joke:** [**Adoption**](https://www.monkeyuser.com/assets/images/2021/205-adoption.png)

