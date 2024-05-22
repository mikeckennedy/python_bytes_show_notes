# Python Bytes 166
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Michael #1:** [**Amazon is now offering quantum computing as a service**](https://www.theverge.com/2019/12/2/20992602/amazon-is-now-offering-quantum-computing-as-a-service)

- [**Amazon Braket**](https://aws.amazon.com/braket) – A fully managed service that allows scientists, researchers, and developers to begin experimenting with computers from multiple quantum hardware providers in a single place.
- We all know about **bits**. Quantum computers use a more sophisticated data representation known as a [qubit](http://en.wikipedia.org/wiki/Qubit) or quantum bit. Each qubit can exist in state 1 or 0, but also in superpositions of 1 and 0, meaning that the qubit simultaneously occupies both states. Such states can be specified by a two-dimensional vector that contains a pair of complex numbers, making for an infinite number of states. Each of the complex numbers is a probability amplitude, basically the odds that the qubit is a 0 or a 1, respectively.
- Amazon Braket is a new service designed to let you get some hands-on experience with qubits and quantum circuits. You can build and test your circuits in a simulated environment and then run them on an actual quantum computer.
- See [linked announcement](https://aws.amazon.com/blogs/aws/amazon-braket-get-started-with-quantum-computing/?tag=theverge02-20). Language looks familiar:

```
    [1]:
    bell = Circuit().h(0).cnot(0, 1)
    print(device.run(bell, s3_folder).result().measurement_counts())
```

- **How it Works**: Quantum computers work by manipulating the amplitudes of the state vector. To program a quantum computer, you figure out how many qubits you need, wire them together into a quantum circuit, and run the circuit. When you build the circuit, you set it up so that the correct answer is the most probable one, and all the rest are highly improbable.

**Brian #2:** [**A quick-and-dirty guide on how to install packages for Python**](https://snarky.ca/a-quick-and-dirty-guide-on-how-to-install-packages-for-python/)

- Brett Cannon
- Good modern intro to venv use.
- Pro
	- short. simple. quick
	- uses --prompt in every example (more people need to use this)
		- and suggests using the directory name containing the env. 
	- send it to all your co-workers that STILL aren’t using virtual environments
	- hints at an improved form of --prompt coming in Python 3.9
- Con
	- uses .venv, I’m a venv (no dot kinda guy)
	- hints at an improved form of --prompt coming in Python 3.9
		- `--prompt .` will deduce the directory name. In 3.8 it just names your env “.”.

**Michael #3:** [**Say No to the no code movement**](https://www.alexhudson.com/2020/01/13/the-no-code-delusion/)

- Article by Alex Hudson
- 2020 is going to be the year of “no code”: the movement that say you can write business logic and even entire applications without having the training of a software developer.
- Every company is a software company
- But software devs are in short supply and outcomes are variable
- two distinct benefits to transitioning business processes into the software domain
	- “change control” becomes a software problem rather than a people problem.
	- it’s easier to innovate on what makes a business distinct.
- The basic problem with “no code”
- the idea of writing business logic in text form according to the syntax of a technical programming language is anathema.
- The “simpler abstraction” misconception
- The “simpler syntax” misconception
- Configuration over code: Many No Code advocates are building significant systems by pulling together off-the-shelf applications and integrating them. But the logic has been implemented as configuration as opposed to code. 
- The equivalence of code: There are reasons why developers still use plain text, if something came along that was better, many (not all!) developers would drop text like a hot rock.
- Where does “No code” fail in practice? 80% there and then …
- Where does “No code” succeed? “No Code” systems are extremely good for putting together proofs-of-concept which can demonstrate the value of moving forward with development.

**Brian #4:** [**What I learned going from prison to Python**](https://opensource.com/article/20/1/prison-to-python)

- Shadeed “Sha” Wallace-Stepter
- Presented at North Bay Python
- I got this recommended to be by many people, even those not in the Python community, including my good friends Chuck Forbes and Dr. Donna Beegle, who work to fight poverty.
- Amazing story. Go listen to it.

**Michael #5:** [**A real QUICK → Qt5 based gUI generator for ClicK**](https://github.com/szsdk/quick)

- Via [**Ricky Teachey**](https://twitter.com/rickyteachey/status/1207770099526127616).
- Inspired by [Gooey](https://github.com/chriskiehl/Gooey), the GUI generator for classical Python `argparse`-based command line programs.
- Take a standard Click-based app, add `--gui` to the command line and you get a GUI!

**Brian #6:** [**Falsehoods programmers believe about time**](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time)

- also [**More falsehoods programmers believe about time; “wisdom of the crowd” edition**](https://infiniteundo.com/post/25509354022/more-falsehoods-programmers-believe-about-time)

All of these assumptions are wrong

1. There are always 24 hours in a day.
2. Months have either 30 or 31 days.

…

6. A week always begins and ends in the same month.

…

11. The system clock will always be set to the correct local time
12. The system clock will always be set to a time that is not wildly different from the correct local time.
13. If the system clock is incorrect, it will at least always be off by a consistent number of seconds.

…

27. It will never be necessary to set the system time to any value other than the correct local time.
28. Ok, *testing* might require setting the system time to a value other than the correct local time but it will never be necessary to do so *in production.*

…

34. Human-readable dates can be specified in universally understood formats such as 05/07/11.

… from more …

16. The day before Saturday is always Friday.

…

79. Two subsequent calls to a getCurrentTime() function will return distinct results.
80. The second of two subsequent calls to a getCurrentTime() function will return a larger result.
81. The software will never run on a space ship that is orbiting a black hole.

Extras

Michael:

- [REMI GUI editor](https://github.com/dddomodossola/remi/tree/master/editor)

**Joke**

[https://twitter.com/mbbillz/status/921119218703257600](https://twitter.com/mbbillz/status/921119218703257600)