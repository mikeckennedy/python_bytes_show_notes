# Python Bytes 43
This episode is brought to you by Rollbar: [**https://pythonbytes.fm/rollbar**](https://pythonbytes.fm/rollbar)

**Brian #1:** [**future-fstrings**](https://github.com/asottile/future-fstrings)

- A backport of fstrings to python < 3.6
- Include an encoding string the top of your file (this replaces the utf-8 line if you already have it)
- And then write python3.6 fstring code as usual!
```
    # -*- coding: future_fstrings -*-
    thing = 'world'
    print(f'hello {thing}')
```
- In action:
```
    $ python2.7 main.py
    hello world
```

- I’m still undecided if I like this sort of monkeying with the language through the encoding mechanism back door. 

**Michael #2:** [**The Fun of Reinvention**](https://www.youtube.com/watch?v=js_0wjzuMfc)

- Keynote from PyCon Israel
- David Beazley rocks it again
- Let’s take Python 3.6 features and see how far we can push them
- Builds an aspect-oriented constraint system using just 3.6 features

**Brian #3:** [**Sound Pattern Recognition with Python**](https://medium.com/@almeidneto/sound-pattern-recognition-with-python-9aff69edce5d)

- Using`scipy.io.wavfile.read` to read a .wav file.
- Looking for peaks (knocks).
- Using minimum values to classify peaks, and minimum distance between peaks.
- This is an interesting start into audio measurements using Python.
- Would be fun to extend to some basic scope measurements, like sampling with a resolution bandwidth, trigger thresholds, pre-trigger time guards, etc.

**Michael #4:** [**PEP 550: Execution Context**](https://www.python.org/dev/peps/pep-0550/)

- From the guys at [**magic.io**](http://magic.io)
- Adds a new generic mechanism of ensuring consistent access to non-local state in the context of out-of-order execution, such as in Python generators and coroutines.
- Thread-local storage, such as `threading.local()`, is inadequate for programs that execute concurrently in the same OS thread. This PEP proposes a solution to this problem.
- A few examples of where Thread-local storage (TLS) is commonly relied upon:
  - Context managers like decimal contexts,`numpy.errstate`, and `warnings.catch_warnings`.
  - Request-related data, such as security tokens and request data in web applications, language context for`gettext` etc.
  - Profiling, tracing, and logging in large code bases.
- The motivation from [**uvloop**](https://github.com/magicstack/uvloop) is obviously at work here.

**Brian #5:** [**Intro to Threads and Processes in Python**](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b)

- Beginner’s guide to parallel programming
- Threads and processes are both useful for different kinds of problems.
- This is a good quick explanation of when and where to use either. With pictures!
- Threads
  - Like mini processes that live inside one process.
  - Share mem space with other threads.
  - Cannot run simultaneously in Python (there are some workarounds), due to GIL.
  - Good for tasks waiting on IO.
- Processes
  - Controlled by OS
  - Can run simultaneously
  - Good for CPU intensive work because you can use multiple cores.

**Michael #6:** [**Alternative filesystems for Python**](https://www.pyfilesystem.org/)

-  PyFilesystem: Filesystem Abstraction for Python. 
- Work with files and directories in archives, memory, the cloud etc. as easily as your local drive.
- Uses
  - Write code now, decide later where the data will be stored
  - unit test without writing real files
  - upload files to the cloud without learning a new API
  - sandbox your file writing code
- File system backends
  - [AppFS](https://www.pyfilesystem.org/page/appfs/) Filesystems for application data.
  - [S3FS](https://www.pyfilesystem.org/page/s3fs/) Amazon S3 Filesystem.
  - [FTPFS](https://www.pyfilesystem.org/page/ftpfs/) File Transfer Protocol.
  - [MemoryFS](https://www.pyfilesystem.org/page/memoryfs/) An in-memory filesystem.
  - [MountFS](https://www.pyfilesystem.org/page/mountfs/) A virtual filesystem that can *mount* other filesystems.
  - [MultiFS](https://www.pyfilesystem.org/page/multifs/) A virtual filesystem that combines other filesystems.
  - [OSFS](https://www.pyfilesystem.org/page/osfs/) OS Filesystem (hard-drive).
  - [TarFS](https://www.pyfilesystem.org/page/tarfs/) Read and write compressed Tar archives.
  - [TempFS](https://www.pyfilesystem.org/page/tempfs/) Contains temporary data.
  - [ZipFS](https://www.pyfilesystem.org/page/zipfs/) Read and write Zip files.
  - and more


## Our news

Michael: switch statement extension to Python: [**github.com/mikeckennedy/python-switch**](https://github.com/mikeckennedy/python-switch)

