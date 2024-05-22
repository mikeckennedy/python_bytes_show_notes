# Python Bytes 164
Sponsored by Datadog: [**pythonbytes.fm/datadog**](https://pythonbytes.fm/datadog)

**Michael #1: Data driven journalism via** [**cjworkbench**](https://github.com/CJWorkbench/cjworkbench)

- via Michael Paholski
- The data journalism platform with built in training
- Think spreadsheet + ETL automation
- Designed around modular tools for data processing -- table in, table out -- with no code required
- Features include:
	- Modules to scrape, clean, analyze and visualize data
	- An integrated data journalism training program
	- Connect to Google Drive, Twitter, and API endpoints.
	- Every action is recorded, so all workflows are repeatable and transparent
	- All data is live and versioned, and you can monitor for changes.
	- Write custom modules in Python and add them to the module library

**Brian #2:** [**remi: A Platform-independent Python GUI library for your applications.**](https://github.com/dddomodossola/remi)

- Python REMote Interface library.
- “Remi is a GUI library for Python applications which transpiles an application's interface into HTML to be rendered in a web browser. This removes platform-specific dependencies and lets you easily develop cross-platform applications in Python!”
- No dependencies. `pip install git+https://github.com/dddomodossola/remi.git` doesn’t install anything else.
- Yes. Another GUI in a web page, but for quick and dirty internal tools, this will be very usable.
- Basic app:

```
    import remi.gui as gui
    from remi import start, App
    
    class MyApp(App):
        def __init__(self, *args):
            super(MyApp, self).__init__(*args)
    
        def main(self):
            container = gui.VBox(width=120, height=100)
            self.lbl = gui.Label('Hello world!')
            self.bt = gui.Button('Press me!')
            self.bt.onclick.do(self.on_button_pressed)
            container.append(self.lbl)
            container.append(self.bt)
            return container
    
        def on_button_pressed(self, widget):
            self.lbl.set_text('Button pressed!')
            self.bt.set_text('Hi!')
    
    start(MyApp)
```

**Michael #3:** [**Typer**](https://typer.tiangolo.com/)

- Build great CLIs. Easy to code. 
- Based on Python type hints.
- **Typer** is [FastAPI](https://fastapi.tiangolo.com)'s little sibling. And it's intended to be the FastAPI of CLIs.
- Just declare once the types of parameters (arguments and options) as function parameters.
- You do that with standard modern Python types.
- You don't have to learn a new syntax, the methods or classes of a specific library, etc.
- Based on Click
- Example (min version)

```
    import typer
    
    def main(name: str):
        typer.echo(f"Hello {name}")
    
    if __name__ == "__main__":
        typer.run(main)
```

**Brian #4:** [**Effectively using Matplotlib**](https://pbpython.com/effective-matplotlib.html)

- Chris Moffitt
- “… I think I was a little premature in dismissing matplotlib. To be honest, I did not quite understand it and how to use it effectively in my workflow.”
- That very much sums up my relationship with matplotlib. But I’m ready to take another serious look at it.
- one reason for complexity is 2 interfaces
	- MATLAB like state-based interface
	- object based interface (use this)
- recommendations:
	- Learn the basic matplotlib terminology, specifically what is a `Figure` and an `Axes` .
	- Always use the object-oriented interface. Get in the habit of using it from the start of your analysis.
	- Start your visualizations with basic pandas plotting.
	- Use seaborn for the more complex statistical visualizations.
	- Use matplotlib to customize the pandas or seaborn visualization.
- Runs through an example
- Describes figures and plots
- Includes a [handy reference](https://pbpython.com/images/matplotlib-pbpython-example.png) for customizing a plot.
- Related: [StackOverflow answer that shows how to generate and embed a matplotlib image into a flask app without saving it to a file.](https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask#answer-50728936)
- Style it with [pylustrator.readthedocs.io](https://pylustrator.readthedocs.io/en/latest/) :)

**Michael #5:** [**Django Simple Task**](https://django-simple-task.readthedocs.io/)

- `django-simple-task` runs background tasks in Django 3 without requiring other services and workers. 
- It runs them in the same event loop as your ASGI application.
- Here’s a simple overview of how it works:
	1. On application start, a queue is created and a number of workers starts to listen to the queue
	2. When `defer` is called, a task(function or coroutine function) is added to the queue
	3. When a worker gets a task, it runs it or delegates it to a threadpool
	4. On application shutdown, it waits for tasks to finish before exiting ASGI server
- It is required to run Django with ASGI server.
- Example

```
    from django_simple_task import defer
    
    def task1():
        time.sleep(1)
        print("task1 done")
    
    async def task2():
        await asyncio.sleep(1)
        print("task2 done")
    
    def view(requests):
        defer(task1)
        defer(task2)
        return HttpResponse(b"My View")
```

**Brian #6:** [**PyPI Stats at pypistats.org**](https://pypistats.org/)

- Simple interface. Pop in a package name and get the download stats.
- Example use: Why is my open source project now getting PRs and issues?
- I’ve got a few packages on PyPI, not updated much.
	- [cards](https://pypi.org/project/cards/) and [submark](https://pypi.org/project/submark/) are mostly for demo purposes for teaching testing.
	- [pytest-check](https://pypi.org/project/pytest-check/) is a pytest plugin that allows multiple failures per test.
- I only hear about issues and PRs on one of these. So let’s look at traffic.
	- [cards](https://pypistats.org/packages/cards): downloads day: 2 week: 24 month: 339
	- [submark](https://pypistats.org/packages/submark): day: 5 week: 9 month: 61
	- [pytest-check](https://pypistats.org/packages/pytest-check): day: 976 week: 4,524 month: 19,636
- That totally explains why I need to start actually supporting pytest-check. Cool.
- Note: it’s still small.
	- [Top 20 packages](https://pypistats.org/top) are all downloaded over 1.3 million times per day.

Extras:

- Comment from January Python PDX West meetup
	- “Please remember to have one beginner friendly talk per meetup.”
	- Good point. 
	- Even if you can’t present here in Portland / Hillsboro, or don’t want to, I’d love to hear feedback of good beginner friendly topics that are good for meetups.
- [PyCascades 2020](https://2020.pycascades.com/)
    - discount code **listeners-at-pycascades** for 10% off

- FireFox 72 is out with anti-fingerprinting and PIP - [Ars Technica](https://arstechnica.com/gadgets/2020/01/firefox-72-blocks-fingerprinting-scripts-by-default-rethinks-notification-pop-ups/)

Joke:

[**Language essays comic**](https://trello-attachments.s3.amazonaws.com/58e3f7c543422d7f3ad84f33/5dea837f3f05ec8e83bae64a/a1e2f14bc60fbc4b10020eef84951872/6fa85fedca23acd58c2f04d1d99f3d9e.jpg)
