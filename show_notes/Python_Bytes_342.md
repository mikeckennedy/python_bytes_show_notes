# Python Bytes 342

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Brian #1:** [**Plumbum: Shell Combinators and More**](https://plumbum.readthedocs.io/en/latest/)

- Suggested by Henry Schreiner last week.
- (Also, thanks Michael for the awesome search tool on PythonBytes.fm that includes transcripts, so I can find stuff discussed and not just stuff listed in the show notes.)
- Plumbum is “ a small yet feature-rich library for shell script-like programs in Python. The motto of the library is **“Never write shell scripts again”**, and thus it attempts to mimic the **shell syntax** (*shell combinators*) where it makes sense, while keeping it all **Pythonic and cross-platform**.”
- Supports
    - local commands
    - piping
    - redirection
    - working directory changes in a with block. So cool.
    - lots more fun features

**Michael #2:**  [**Our plan for Python 3.13**](https://github.com/faster-cpython/ideas/blob/main/3.13/README.md)

- The big difference is that we have now finished the foundational work that we need:
    - [Low impact monitoring (PEP 669)](https://peps.python.org/pep-0669/) is implemented.
    - The bytecode compiler is a much better state.
    - The interpreter generator is working.
    - Experiments on the register machine are complete.
    - We have a viable approach to create a low-overhead maintainable machine code generator, based on [copy-and-patch](https://fredrikbk.com/publications/copy-and-patch.pdf).
- We plan three parallelizable pieces of work for 3.13:
    - The tier 2 optimizer
    - Enabling subinterpreters from Python code ([PEP 554](https://peps.python.org/pep-0554/)).
    - Memory management
- Details on [superblocks](https://github.com/faster-cpython/ideas/issues/557#issuecomment-1464097006) 


**Brian #3:** [**Some blogging myths**](https://jvns.ca/blog/2023/06/05/some-blogging-myths/#myth-everyone-should-blog)

- Julia Evans
- <from Brian: I’m not sure if I’m including this to convince all of you to blog more, or to convince myself. Hopefully both happens.> 
- myths (more info of each in the blog post):
    - you need to be original
    - you need to be an expert
    - posts need to be 100% correct
    - writing boring posts is bad
    - you need to explain every concept
    - page views matter
    - more material is always better
    - everyone should blog
- I’d add
    - Write posts to help yourself remember something.
    - Write posts to help future prospective employers know what topics you care about.
    - You know when you find a post that is outdated and now wrong, and the code doesn’t work, but the topic is interesting to you. Go ahead and try to write a better post with code that works.

**Michael #4:** [**Jupyter AI**](https://github.com/jupyterlab/jupyter-ai)

- A generative AI extension for JupyterLab
- An `%%ai` magic that turns the Jupyter notebook into a reproducible generative AI playground. This works anywhere the IPython kernel runs (JupyterLab, Jupyter Notebook, Google Colab, VSCode, etc.).
- A native chat UI in JupyterLab that enables you to work with generative AI as a conversational assistant.
- Support for a wide range of generative model providers and models (AI21, Anthropic, Cohere, Hugging Face, OpenAI, SageMaker, etc.).
- Official project from Jupyter 
- Provides code insights
- Debug failing code
- Provides a general interface for interaction and experimentation with currently available LLMs
- Lets you collaborate with peers and an Al in JupyterLab
- Lets you ask questions about local files
- Video presentation: [David Qiu - Jupyter AI — Bringing Generative AI to Jupyter | PyData Seattle 2023](https://www.youtube.com/watch?v=T0rzH_KslKQ)

**Extras**

Brian:

- Textual has some fun releases recently
    - [Textualize youtube channel](https://www.youtube.com/channel/UCo4nHAZv_cIlAiCSP2IyiOA) with 3 tutorials so far
    - [trogon](https://github.com/Textualize/trogon) to turn Click based command line apps into TUIs
        - video example of it working with `sqlite-utils`. 
- [Python in VSCode June Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-june-2023-release/) includes revamped test discovery and execution.
    - You have to turn it on though, as the changes are experimental:
    ```
        "python.experiments.optInto": [
            "pythonTestAdapter",
        ]
    ```
    - I just turned it on, so I haven’t formed an opinion yet. 

Michael:

- Michael’s take on the [MacBook Air 15”](https://www.apple.com/macbook-air-13-and-15-m2/) ([black one](https://images.macrumors.com/article-new/2022/06/m2-macbook-air-midnight.jpeg))

**Joke:**  [**Phishing**](https://devhumor.com/media/phishing)
