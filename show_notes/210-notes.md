# Python Bytes 210

The **[live stream recording on YouTube](https://www.youtube.com/watch?v=WKAeXtLv5-k)**.

Sponsored by us! Support our work through:

- Our [**courses at Talk Python Training**](https://training.talkpython.fm/)
- [**Test & Code**](https://testandcode.com/) Podcast
- [**Patreon Supporters**](https://www.patreon.com/pythonbytes)

**Brian #1:**  [**Analyzing Kickstarter Campaigns with Python Data Science Tools**](https://medium.com/swlh/kickstarter-projects-do-they-succeed-f4a789010585)

- Article title: “Kickstarter Projects — Do They Succeed?”
- Aditya Patkar
- Using a Kaggle dataset of 378,661-ish projects up to 2018.
- Looks at using pandas data frames to explore the data.
- Using `.describe()` data frame method to learn a lot.
- Uses matplotlib and seaborn to analyze the data further.
- Odd statement that I’m not sure is straight faced or a really dry joke: “The data from 1970 seems to be bad or insignificant data.”
- Examples of using heat maps, line graphs, bar charts, to look at different aspects.
- Some results:
	- 35.64% of projects are successful (meaning goal hit)
	- tech asks for the most for goals, and has the highest average per backer.
	- Comics has the lowest pledged amount per backer average.
- Nice that you can use the techniques to ask your own questions of the data.

**Michael #2:** [**GPU Accelerated Python for Machine Learning on Cross-Vendor Graphics Cards**](https://towardsdatascience.com/beyond-cuda-gpu-accelerated-python-for-machine-learning-in-cross-vendor-graphics-cards-made-simple-6cc828a45cc3)

- Building machine learning algorithms using the Vulkan Kompute Python Framework
- When you hear “CUDA”, that means Nvidia 🙂
- Uses [Vulkan Kompute](https://github.com/EthicalML/vulkan-kompute) framework
- A large number of high profile (and new) machine learning frameworks such as Google’s Tensorflow, Facebook’s Pytorch, Tencent’s NCNN, Alibaba’s MNN —between others — have been adopting Vulkan as their core cross-vendor GPU computing SDK.
- As you can imagine, the Vulkan SDK provides very low-level C / C++ access to GPUs, which allows for very specialized optimizations.
- The main disadvantage is the verbosity involved, requiring 500–2000+ lines of C++ code to only get the base boilerplate required to even start writing the application logic.
- [**The Kompute Python package**](https://github.com/EthicalML/vulkan-kompute#vulkan-kompute) is built on top of the Vulkan SDK through optimized C++ bindings, which exposes Vulkan’s core computing capabilities. Kompute is the Python [GPGPU framework.](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)
- The main article talks through a couple of numerical computation examples.

**Jay** **#3:** [Adafruit PyPortal - CircuitPython Powered Internet Display](https://www.adafruit.com/product/4116)

- Gift for the tinkering pythonista
- CircuitPy
- Use it to make plenty of cool things
- Screen/speaker/Light Sensor Built-In

**Brian** **#4:**  [**Introduction to Linear Algebra for Applied Machine Learning with Python**](https://pabloinsente.github.io/intro-linear-algebra)

- Pablo Caceres
- Intended as a reference and not a comprehensive review.
- Still, I very much appreciate it.
- Includes links to both free and paid resources to thoroughly learn linear algebra
- Covers
	- sets, ordered pairs,  relations, functions, 
	- vectors
	- matrices
	- linear and affine mappings
	- matrix decomposition
- Uses numpy, pandas, and altair  for examples
- Quick (but useful) explanations of concepts, along with how to represent and do it with numpy
- I’m really just getting into it, but I’m enjoying it and this is the right level of handholding I needed.

**Michael** **#5:** [**How many notebook frameworks? Many, and now +1 with Deepnote**](https://deepnote.com/)

- Deepnote is a new kind of data science notebook. Jupyter-compatible with real-time collaboration and running in the cloud. 
- Free for individuals, paid for teams and companies
- Real time collaboration is a key feature
- Built in versioning coming
- Code review in the notebook coming
- “View” your variables as a whole environment
- Better — real — autocomplete
- Dashboards coming too

**Jay** **#6:** [**imagekit.io**](https://imagekit.io)

- image cdn
- started using imagekit on my own website and noticed faster load times
- [allows for some responsive “fanciness”](https://imagekit.io/features/image-transformation)
	- Add Blurs
	- Smart Cropping
- [Python API](https://github.com/imagekit-developer/imagekit-python) or URL-Schema

**Extras**

**Michael:**

- The Apple M1 mac mini wait continues. :)
- Talk Python To Me, pro edition
- PSF Fundraiser for the month of December: https://pythonbytes.fm/psf2020

Jay:

- [Elastic Community YouTube Channel](https://www.youtube.com/channel/UC7z5VlhDHnorjUm6oW5dXcw)
	- Just posted my lightning talk on looking at open data from the government.
	- Upcoming interview on one of our newest clients - Eland which is python client to create pandas-like dataframes with elasticsearch datastores.
- My Podcast [The PIT Show](http://podcast.productivityintech.com) weekly insights from me on my developer journey and interviews with amazing folks in the tech space.
- Elastic Blog - Just posted my first Elastic Blog post [**Elastic Contributor Program: How to create a video tutorial**](https://www.elastic.co/blog/elastic-contributor-program-how-to-create-a-video-tutorial)

**Joke:**

via [twitter.com/Spirix3/status/1330611989891207168](https://twitter.com/Spirix3/status/1330611989891207168)

- Q: why can't SQL and NoSQL Developers date one other?
- A: because they don't agree on relationships.
