# Python Bytes 151
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/datadog)

**Brian #1:** [**Python alternative to Docker**](https://www.mattlayman.com/blog/2019/python-alternative-docker/)

- Matt Layman
- Using [Shiv](https://shiv.readthedocs.io/en/latest/), from LinkedIn
	- Mentioned briefly in [episode 114](https://pythonbytes.fm/114)
	- Shiv uses zipapp, [PEP 441](https://www.python.org/dev/peps/pep-0441/).
	- Execute code directly from a zip file.
	- App code and dependencies can be bundled together.
	- “Having one artifact eliminates the possibility of a bad interaction getting to your production system.”
	- article includes an example of all the steps for packaging a Django app with Gunicorn.
	- includes talking about deployment.
- Matt includes shoutouts to:
	- Platform as a Service providers
	- Manual steps to do it all.
	- Docker
- Compares the process against Docker and discusses when to choose one over the other.
- Also an interesting read: [Docker is in deep trouble](https://www.zdnet.com/article/docker-is-in-deep-trouble/)

**Michael #2:**  [**How to support open-source software and stay sane**](https://www.nature.com/articles/d41586-019-02046-0)

- via [**Jason Thomas**](https://twitter.com/JDeanThomas) written by [**Anna Nowogrodzki**](#) 
- Releasing lab-built open-source software often involves a mountain of unforeseen work for the developers.
- Article opens: “On 10 April, astrophysicists announced that they had captured the first ever image of a black hole. This was exhilarating news, but none of the giddy headlines mentioned that the image would have been impossible without open-source software.”
- The image was created using Matplotlib, a Python library for graphing data, as well as other components of the open-source Python ecosystem. **Just five days later**, the US National Science Foundation **(NSF) rejected a grant proposal to support that ecosystem**, saying that the software lacked sufficient impact.
- Open-source software is widely acknowledged as crucially important in science, yet it is funded non-sustainably.
- “It’s sort of the difference between having insurance and having a GoFundMe when their grandma goes to the hospital,” says Anne Carpenter
- Challenges
	- Scientists writing open-source software often lack formal training in software engineering.
	- Yet poorly maintained software can waste time and effort, and hinder reproducibility.
- If your research group is planning to release open-source software, you can prepare for the support work
- Obsolescence isn’t bad, she adds: knowing when to stop supporting software is an important skill.
- However long your software will be used for, good software-engineering practices and documentation are essential.
- These include continuous integration systems (such as TravisCI), version control (Git) and unit testing.
- To facilitate maintenance, Varoquaux recommends focusing on code readability over peak performance.

**Brian #3**: [**The Hippocratic License**](https://firstdonoharm.dev/)

- Coraline Ada Ehmke
- Interesting idea to derive from MIT, but add restrictions.
- This license adds these restrictions:
	- “The software may not be used by individuals, corporations, governments, or other groups for systems or activities that actively and knowingly endanger, harm, or otherwise threaten the physical, mental, economic, or general well-being of individuals or groups in violation of the United Nations Universal Declaration of Human Rights”
- I could see others with different restrictions, or this but more.

**Michael #4:** [**MATLAB vs Python: Why and How to Make the Switch**](https://realpython.com/matlab-vs-python/)

- MATLAB® is widely known as a high-quality environment for any work that involves arrays, matrices, or linear algebra.
- I personally used it for wavelet-decomposition of real time eye measurements during cognitively intensive human workloads… That *toolbox* costs $2000 per user.
- Difference in philosophy: Closed, paid vs. open source.
- Since Python is available at no cost, a much broader audience can use the code you develop
- Also, there is [GNU Octave](https://www.gnu.org/software/octave/) is a free and open-source clone of MATLAB apparently

**Brian #5**: [**PyperCard - Easy GUIs for All**](https://pypercard.readthedocs.io/en/latest/)

- Nicholas Tollervey
- Came up on [episode 143](https://pythonbytes.fm/143)
- Also, [episode 89 of Test & Code](https://testandcode.com/89)
- Really easy to quickly set up a GUI specified by a list of “Card” objects. (different from [cards project](https://github.com/okken/cards))
- Simple examples are choose your own adventure type applications, where one button takes you to another card, and another button, a different card.
- However, the “next card” could be a Python function that can do anything, as long as it returns a string with the name of the next card.
- Lots of potential here, especially with input boxes, images, sound, and more.
- Super fun, but also might have business use.
    

**Michae #6**: [**pynode**](https://github.com/fridgerator/PyNode)

- Article: [Bridging Node.js and Python with PyNode to Predict Home Prices](https://thecodinginterface.com/blog/bridging-nodejs-and-python-with-pynode/)
- Call python code from node.js
	- Define a Python method
	- In node: require pynode: `const pynode = require('@fridgerator/pynode')`
	- Start an interpreter: `pynode.startInterpreter()`
	- Call the function
      
```  
    pynode.call('add', 1, 2, (err, result) => {
      if (err) return console.log('error : ', err)
      result === 3 // true
    })
```

**Jokes** 

[**The "Works on My Machine" Certification Program, get certified!**](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)

