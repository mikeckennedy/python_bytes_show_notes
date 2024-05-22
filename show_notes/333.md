# Python Bytes 333

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Connect with the hosts**

- Michael: [**@mkennedy@fosstodon.org**](https://fosstodon.org/@mkennedy)
- Brian: [**@brianokken@fosstodon.org**](https://fosstodon.org/@brianokken)
- Show: [**@pythonbytes@fosstodon.org**](https://fosstodon.org/@pythonbytes)x

Join us on YouTube at [**pythonbytes.fm/live**](https://pythonbytes.fm/stream/live) to be part of the audience. Usually Tuesdays at 11am PT. Older video versions available there too.

**Michael #1:** [**Introducing Microsoft Security Copilot**](https://blogs.microsoft.com/blog/2023/03/28/introducing-microsoft-security-copilot-empowering-defenders-at-the-speed-of-ai/)

- Security Copilot combines this advanced large language model (LLM) with a security-specific model from Microsoft.
- When Security Copilot receives a prompt from a security professional, it uses the full power of the security-specific model to deploy skills and queries that maximize the value of the latest large language model capabilities.
- Your data and stays within your control. It is not used to train the foundation AI models, and in fact, it is protected by the most comprehensive enterprise compliance and security controls.

**Brian #2:** [**PEP 695 – Type Parameter Syntax**](https://peps.python.org/pep-0695/)

- “This PEP specifies an improved syntax for specifying type parameters within a generic class, function, or type alias. It also introduces a new statement for declaring type aliases.”
- To get a feel for this, [jump to the examples](https://peps.python.org/pep-0695/#summary-examples)
- One example
    - Here is an example of a generic function today.
```
from typing import TypeVar
    
    _T = TypeVar("_T")
    
    def func(a: _T, b: _T) -> _T:
        ...
    - And the new syntax.
      def func[T](a: T, b: T) -> T:
        ...
```

**Michael #3:**  [**Auto-GPT**](https://github.com/Significant-Gravitas/Auto-GPT)

- An experimental open-source attempt to make GPT-4 fully autonomous.
- This program, driven by GPT-4, chains together LLM "thoughts", to autonomously achieve whatever goal you set. 
- Features
    - 🌐 Internet access for searches and information gathering
    - 💾 Long-term and short-term memory management
    - 🧠 GPT-4 instances for text generation
    - 🔗 Access to popular websites and platforms
    - 🗃️ File storage and summarization with GPT-3.5

**Brian #4:** [**Astral : Ruff is now a company**](https://astral.sh/blog/announcing-astral-the-company-behind-ruff)

- Charlie Marsh announces Astral, starting off with a healthy $4m in seed money. Not a bad start
- Astral will continue building high-performance developer tools for the Python ecosystem — to keep building [Ruff](https://github.com/charliermarsh/ruff), and to build more [Ruff](https://github.com/charliermarsh/ruff)-like things.
- “to make the Python ecosystem more productive by building high-performance developer tools.”
- Undoubtedly Rust-ifying more of the Python tool chain.
- Related:
    - In a discussion at PyCon, someone asked me if Ruff was a replacement for Black.
    - My answer, “not really, more of a flake8 replacement and a few other tools, but a partial overlap with Black.
    - [Real answer is at the FAQ](https://beta.ruff.rs/docs/faq/)
        - Is Ruff compatible with Black?
            - Yes. Ruff is compatible with [Black](https://github.com/psf/black) out-of-the-box, as long as the `line-length` setting is consistent between the two.
            - As a project, Ruff is designed to be used alongside Black and, as such, will defer implementing stylistic lint rules that are obviated by autoformatting.”

**Extras** 

Brian:

- Registration open for [**SciPy 2023**](https://www.scipy2023.scipy.org)

Michael:

- [**Android Mobile App is out**](https://play.google.com/store/apps/details?id=fm.talkpython.training.player). Please give us feedback

**Joke:**  [**Releasing to prod**](https://www.reddit.com/r/programminghumor/comments/101in8p/release_to_production/)

