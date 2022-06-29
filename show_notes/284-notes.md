# Python Bytes 284

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:**[**distinctipy**](https://github.com/alan-turing-institute/distinctipy)

- “*distinctipy* is a lightweight python package providing functions to generate colours that are visually distinct from one another.”
- Small, focused tool, but really cool.
- Say you need to plot a dynamic number of lines.
- Why not let distinctipy pick colors for you that will be distinct?
- Also can display the color swatches.
- Some example palettes here: https://github.com/alan-turing-institute/distinctipy/tree/main/examples

```
from distinctipy import distinctipy

# number of colours to generate
N = 36

# generate N visually distinct colours
colors = distinctipy.get_colors(N)

# display the colours
distinctipy.color_swatch(colors)
```

**Michael #2:** [**Soda SQL**](https://docs.soda.io/soda-sql/concepts.html)

- Soda SQL is a free, open-source command-line tool.
- It utilizes user-defined input to prepare SQL queries that run tests on dataset in a data source to find invalid, missing, or unexpected data.
- Looks good for data pipelines and other CI/CD work!

**Daniel #3:** [**Python in Nature**](https://www.nature.com/articles/s41586-020-2649-2)

- There’s a review article from Sept 2020 on array programming with NumPy in the research journal Nature.
- For reference, in grad school we had a fancy paper on quantum entanglement that got rejected from Nature Communications, a sub-journal to Nature. Nature is hard to get into.
- List of authors includes Travis Oliphant who started NumPy. Covers NumPy as the foundation, building up to specialized libraries like QuTiP for quantum computing.
- If you search “Python” on their site, many papers come up. Interesting to see their take on publishing software work.

**Brian #4:** [**Supercharging GitHub Actions with Job Summaries**](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/)

- From a tweet by [Simon Willison](https://twitter.com/simonw/status/1526337395334885377?s=20&t=pFgZ2Ruklh8MLNlSiUmIcA)
    - and an article: [GH Actions job summaries](https://til.simonwillison.net/github-actions/job-summaries)
    
- Also, [Ned Batchelder](https://twitter.com/nedbat/status/1526338136699281408?s=20&t=pFgZ2Ruklh8MLNlSiUmIcA) is using it for Coverage reports

- “You can now output and group custom Markdown content on the Actions run summary page.”

- “Custom Markdown content can be used for a variety of creative purposes, such as:
    - Aggregating and displaying test results
    - Generating reports
    - Custom output independent of logs”
    
- [Coverage.py example:](https://github.com/nedbat/coveragepy/blob/ad824b4585c88d0a153dd248f4585084dea33189/.github/workflows/coverage.yml#L218-L221)

```
- name: "Create summary"
run: |
echo '### Total coverage: ${{ env.total }}%' >> $GITHUB_STEP_SUMMARY
echo '[${{ env.url }}](${{ env.url }})' >> $GITHUB_STEP_SUMMARY
```

**Michael #5:**[**Language Summit is write up out**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit_01678898482.html)

- via Itamar, by Alex Waygood
    - [**Python without the GIL**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-python_11.html): A talk by Sam Gross
    - [**Reaching a per-interpreter GIL**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-per.html): A talk by Eric Snow
    - [**The "Faster CPython" project: 3.12 and beyond**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit_2.html): A talk by Mark Shannon
    - [**WebAssembly: Python in the browser and beyond**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-python.html): A talk by Christian Heimes
    - [**F-strings in the grammar**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-f.html)**:** A talk by Pablo Galindo Salgado
    - [**Cinder Async Optimisations**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit_60.html): A talk by Itamar Ostricher
    - [**The issue and PR backlog**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-dealing.html): A talk by Irit Katriel
    - [**The path forward for immortal objects**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit_11.html): A talk by Eddie Elizondo and Eric Snow
    - [**Lightning talks**](https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit.html), featuring short presentations by Carl Meyer, Thomas Wouters, Kevin Modzelewski, Samuel Colvin and Larry Hastings

**Daniel #6:**[**AllSpice is Git for EEs**](https://www.allspice.io)

- Software engineers have Git/SVN/Mercurial/etc
- None of the other engineering disciplines (mechanical, electrical, optical, etc), have it nearly as good. Altium has their Vault and “365,” but there’s nothing with a Git-like UX.
- Supports version history, diffs, all the things you expect. Even self-hosting and a Gov Cloud version.
- “Bring your workflow to the 21st century, finally.”

**Extras** 

Brian:

- [Will McGugan talks about Rich, Textual, and Textualize on Test & Code 188](https://testandcode.com/188)
- Also 3 other episodes since last week. (I have a backlog I’m working through.)

Michael:

- [**Power On-Xbox Documentary | Full Movie**](https://www.youtube.com/watch?v=je21yaRV_xc)
- [**The 4 Reasons To Branch with Git - Illustrated Examples with Python**](https://www.youtube.com/watch?v=7sxUu-tYcIA)
- [**A Python spotting**](https://www.easypost.com) - via Jason Pecor
- [**2022 StackOverflow Developer Survey**](https://twitter.com/btskinn/status/1524507904929370114) is live, via Brian
- [**TextSniper macOS App**](https://www.textsniper.app)
- PandasTutor on webassembly 

Daniel: 

- I know Adafruit’s a household name, shout-out to [Sparkfun](https://www.sparkfun.com), [Seeed Studio](https://www.seeedstudio.com), [OpenMV](https://openmv.io), and other companies in the field.

**Joke:** 

[**A little awkward**](https://www.reddit.com/r/ProgrammerHumor/comments/un1pmg/i_can_explain_this/)

