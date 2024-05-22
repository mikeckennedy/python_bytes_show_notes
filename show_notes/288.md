# Python Bytes 288

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:** [**Polars: Lightning-fast DataFrame library for Rust and Python**](https://www.pola.rs/)

- Suggested by a several listeners
- “Polars is a blazingly fast DataFrames library implemented in Rust using [Apache Arrow Columnar Format](https://arrow.apache.org/docs/format/Columnar.html) as memory model.
    - Lazy | eager execution
    - Multi-threaded
    - SIMD (Single Instruction/Multiple Data)
    - Query optimization
    - Powerful expression API
    - Rust | Python | ...”
- Python API syntax set up to allow parallel and execution while sidestepping GIL issues, for both lazy and eager use cases. From the docs: [Do not kill parallelization](https://pola-rs.github.io/polars-book/user-guide/dsl/groupby.html#do-not-kill-the-parallelization)
- The syntax is very functional and pipeline-esque:

```
import polars as pl
    q = (
        pl.scan_csv("iris.csv")
        .filter(pl.col("sepal_length") > 5)
        .groupby("species")
        .agg(pl.all().sum())
    )
    df = q.collect()
```

- [Polars User Guide](https://pola-rs.github.io/polars-book/user-guide/) is excellent and looks like it’s entirely written with Python examples.
- Includes [a 30 min intro video from PyData Global 2021](https://pola-rs.github.io/polars-book/user-guide/dsl/video_intro.html)

**Michael #2:** [**PSF Survey is out**](https://lp.jetbrains.com/python-developers-survey-2021/)

- Have a look, their page summarizes it better than my bullet points will.

**Brian #3:** [**Gin Config: a lightweight configuration framework for Python**](https://github.com/google/gin-config)

- Found through Vincent D. Warmerdam’s excellent [intro videos on gin on calmcode.io](https://calmcode.io/gin/intro-to-gin.html)
- Quickly make parts of your code configurable through a configuration file with the `@gin.configurable` decorator.
- It’s in interesting take on config files. (Example from Vincent)

```
    # simulate.py
    @gin.configurable
    def simulate(n_samples):
      ...
    # config.py
    simulate.n_samples = 100
```

-  You can specify:
    - required settings: `def` ``simulate``(n_samples=gin.REQUIRED)`
    - blacklisted settings: `@gin.configurable(blacklist=["n_samples"])`
    - external configurations (specify values to functions your code is calling)
    - can also references to other functions: `dnn.activation_fn = @tf.nn.tanh`
- Documentation suggests that it is especially useful for machine learning.
- From motivation section:
    - “Modern ML experiments require configuring a dizzying array of hyperparameters, ranging from small details like learning rates or thresholds all the way to parameters affecting the model architecture.
    - Many choices for representing such configuration (proto buffers, tf.HParams, ParameterContainer, ConfigDict) require that model and experiment parameters are duplicated: at least once in the code where they are defined and used, and again when declaring the set of configurable hyperparameters.
    - Gin provides a lightweight dependency injection driven approach to configuring experiments in a reliable and transparent fashion. It allows functions or classes to be annotated as `@gin.configurable`, which enables setting their parameters via a simple config file using a clear and powerful syntax. This approach reduces configuration maintenance, while making experiment configuration transparent and easily repeatable.”


**Michael #4:** [**Performance benchmarks for Python 3.11 are amazing**](https://twitter.com/EduardoOrochena/status/1534913062356099079)

- via Eduardo Orochena
- Performance may be the biggest feature of all
- Python 3.11 has 
    - task groups in asyncio
    - fine-grained error locations in tracebacks
    - the self-type to return an instance of their class
- The "Faster CPython Project" to speed-up the reference implementation. 
    - See my interview with Guido and Mark: [**talkpython.fm/339**](https://talkpython.fm/339)
    - Python 3.11 is 10~60% faster than Python 3.10 according to the official figures
    - And a 1.22x speed-up with their standard benchmark suite.
- Arriving as stable until October

**Extras** 

Michael:

- [**Python 3.10.5 is available**](https://www.python.org/downloads/release/python-3105/) ([changelog](https://docs.python.org/release/3.10.5/whatsnew/changelog.html#python-3-10-5-final))
- [**Raycast**](https://www.raycast.com) (vs Spotlight)
    - e.g. CMD+Space => pypi search:
    ![](https://paper-attachments.dropbox.com/s_89E5FC1F5DBBED983E2558E0DE9902BF8E7733F0236C1030506F258E61A5C2AF_1655219401413_pypisearch.png)


**Joke:**  [**Why wouldn't you choose a parrot for your next application**](https://devhumor.com/media/why-wouldn-t-you-choose-a-parrot-for-your-next-application)

