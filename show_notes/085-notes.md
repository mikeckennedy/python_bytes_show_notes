# Python Bytes 85
Sponsored by DigitalOcean: [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean)

**Brian #1:** [**the state of type hints in Python**](https://www.bernat.tech/the-state-of-type-hints-in-python/)

- “Therefore, type hints **should be used whenever unit test are worth writing.”**
- Type hints, especially for function arguments and return values, help make your code easier to read, and therefore, easier to maintain.
- This includes refactoring, allowing IDEs to help with code completion, and allow linters to find problems.
- For CPython
	- No runtime type inference happens.
	- No performance tuning allowed. 
	- Of course, third party packages are not forbidden to do so.
- Non-comment type annotations are available for functions in 3.0+
- Variable annotations for 3.6+
- In 3.7, you can postpone evaluation of annotations with:
    from `__future__` import annotations
- Interface stub files `.pyi` files, are allowed now, but this is extra work and code to maintain.
  - typeshed has types for standard library plus many popular libraries.
- How do deal with multiple types, duck typing, and more discussed.
- A discussion of type generation and checking tools available now, including mypy
- See also: [Stanford Seminar - Optional Static Typing for Python - Talk by  Guido van Rossum](https://youtu.be/GiZKuyLKvAA) 
	- Interesting discussion that starts with a bit of history of where mypy came from.

**Michael** **#2:** [**Django MongoDB connector**](https://nesdis.github.io/djongo/)

- Via Robin on Twitter
- Use MongoDB as the backend for your Django project, without changing the Django ORM.
- Use Django Admin to access MongoDB
- Use Django with MongoDB data fields: Use MongoDB embedded documents and embedded arrays in Django Models.
- Connect 3rd party apps with MongoDB: Apps like Django Rest Framework and Viewflow app that use Django Models integrate easily with MongoDB.
- Requirements:
	- Python 3.6 or higher.
	- MongoDB 3.4 or higher.
- Example

```python
       inner_qs = Blog.objects.filter(name__contains='Ch').values('name')
       entries = Entry.objects.filter(blog__name__in=inner_qs)

**Brian #****3****:**  ****[**Python Idioms: Multiline Strings**](https://amir.rachum.com/blog/2018/06/23/python-multiline-idioms/)
```

- or “How I use dedent”
- Example:
```python
    def create_snippet():
        code_snippet = textwrap.dedent("""\
            int main(int argc, char* argv[]) {
                return 0;
            }
        """)
        do_something(code_snippet)
```

**Michael #4:** [**Flaskerizer**](https://github.com/brettvanderwerff/Flaskerizer)

- A program that automatically creates Flask apps from Bootstrap templates 
- Bootstrap templates from websites like [https://Bootstrapmade.com/](https://Bootstrapmade.com/) and [https://startBootstrap.com](https://startBootstrap.com) are a fast way to get very dynamic website up and running
- Bootstap templates typically don't work "out of the box" with the python web framework Flask and require some tedious directory building and broken link fixing before being functional with Flask. 
- The Flaskerizer automates the necessary directory building and link creation needed to make Bootstrap templates work "out of the box" with Flask. 
- Queue black turtleneck!

**Brian #*5:** [**Learn Python the Methodical Way**](https://realpython.com/learn-python-the-methodical-way/)

- From the article: 
	- Make your way through a tutorial/chapter that teaches you some discrete, four-to-six-step skill.
	- Write down those steps as succinctly and generically as possible.
	- Put the tutorial/chapter and its solutions away.
	- Build your project from scratch, peeking only when you’re stuck.
	- Erase what you built.
	- Do the project again.
	- Drink some water.
	- Erase what you built and do it again.
	- A day or two later, delete your work and do it again – this time without peeking even once.
	- Erase your work and do it again.
- The notion of treating code like you treat creative writing with rough drafts and sometimes complete do-overs is super liberating. 
- You’ll be surprised how fast you can do something the second time, the third time, the fourth time. And it’s very gratifying.

**Michael #6:** [**PixieDebugger**](https://medium.com/ibm-watson-data-lab/the-visual-python-debugger-for-jupyter-notebooks-youve-always-wanted-761713babc62)

- The Visual Python Debugger for Jupyter Notebooks You’ve Always Wanted
- Jupyter already supports pdb for simple debugging, where you can manually and sequentially enter commands to do things like inspect variables, set breakpoints, etc.
- Check out the video to get a good idea of its usage: [https://www.youtube.com/watch?v=Z-tPeEkVqjk](https://www.youtube.com/watch?v=Z-tPeEkVqjk)

