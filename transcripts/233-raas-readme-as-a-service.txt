00:00:00 >> Hello and welcome to Python Bytes, where we deliver news and headlines directly to your earbuds.

00:00:05 This is Episode 233, recorded May 12th, 2021, and I'm Brian Okken.

00:00:11 >> I'm Michael Kennedy.

00:00:12 >> I'm Marlene Mangami.

00:00:14 >> Well, welcome Marlene.

00:00:15 For people who don't know you, can you introduce who you are?

00:00:18 >> I am a Pythonista, of course.

00:00:22 Based in Harare, Zimbabwe, I am also really involved with the Python community.

00:00:30 So I'm currently the vice chair of the PSA board of directors.

00:00:34 The board I think for about coming up on four years now, which is really exciting and it's been really a very cool experience for me.

00:00:45 I'm also a software engineer.

00:00:47 I work right now with the RAPIDS team at NVIDIA and have just been doing software engineering with them.

00:00:54 and we'll talk a bit about that later.

00:00:56 But yeah, I'm trying to think what else.

00:00:59 I'm also a very avid reader and just like doing other things besides software.

00:01:05 So yeah, that's pretty much me.

00:01:08 - Cool.

00:01:08 - That's awesome.

00:01:09 You're doing a bunch of cool stuff.

00:01:10 I think RAPID seems like a really neat project to work on as well.

00:01:14 Of course, the Python community side is great.

00:01:17 So super happy to have you here.

00:01:19 Brian, you know, having a good readme is really important to a project, wouldn't you say?

00:01:23 >> Yeah, definitely. For some reason, I don't know.

00:01:28 Readmes are not difficult to write, but I freeze up.

00:01:31 It's a blank page syndrome, I think.

00:01:33 Often I've gone through and just copied from some other project.

00:01:37 What's in there, Readme?

00:01:39 But I don't think that that's the best way to go about it, really, because sometimes you forget stuff.

00:01:46 We have a recommendation from Johnny Metz.

00:01:49 It's a tool called Readme.so.

00:01:53 This is totally fun.

00:01:56 It's just this interactive thing where you get to add stuff.

00:02:01 We've got the title.

00:02:02 On the left-hand side, there's a bunch of sections where you can select what you want to go into the README.

00:02:09 Then it shows a preview on the right, but you can also see the raw markdown.

00:02:15 Then in the middle, there's an editor, so you can actually just edit the whole thing here.

00:02:19 But really, I don't know if I really would.

00:02:21 >> Project title.

00:02:24 What I'd probably do is go through and pick out to look at what things I'd want.

00:02:30 I'd probably maybe some acknowledgments if I got some help from somebody.

00:02:35 Maybe an API reference if it's a library.

00:02:39 How to contribute.

00:02:41 Badges, definitely want badges.

00:02:43 >> Yeah.

00:02:44 >> Then maybe how to run tests if you want to contribute.

00:02:49 If there's other cool projects using it, I'd want to use by all these things.

00:02:54 The editor only selects, it only shows you the ones one at a time, which is nice.

00:03:01 But then you've got this whole generated really nice looking, read me what tables and everything built in, and you can either just copy it or download it and just run with it.

00:03:12 I think this is really great.

00:03:14 I'll probably use this in the future.

00:03:16 >> I really love this and I'm surprised about the psychological benefit of just showing the little, the section with the one heading.

00:03:24 So for like example, acknowledgments, you just have #acknowledgements and the few things, even though you're editing the whole readme, it seems so much more like, oh, I'm gonna just work on that section.

00:03:34 It's really cool.

00:03:35 Marlene, what do you think?

00:03:36 - It's really, really cool.

00:03:37 I like it.

00:03:38 I think I'm gonna try it out.

00:03:40 I have put no effort at all in this.

00:03:45 So I think it's something I need to put more effort into and this looks like a really good way to do that.

00:03:52 - Yeah.

00:03:53 - I think that it would also be great to just, like if you have an existing readme and you wanna add some new sections, you're not quite sure how it should look, using this as a jumping point of just to grab sections of a readme to add to an existing one too, this would be great.

00:04:06 - Yeah, this is really, really cool.

00:04:08 How do you, how do you, can you start with a new one?

00:04:12 Like can I, well, sorry, let me take it back.

00:04:14 Can I start with an existing one?

00:04:15 Can I somehow upload an existing one?

00:04:17 I don't see.

00:04:18 - I don't think so.

00:04:19 - Wait, I can go to raw, hold on.

00:04:22 - Oh, you can probably just drop it into raw.

00:04:24 - Maybe, yes, you can drop it into the raw, that's it.

00:04:26 Okay, perfect.

00:04:27 You go to raw, which it doesn't hide the sections.

00:04:29 It's just pure markdown.

00:04:31 And then you just throw it in there.

00:04:31 Okay.

00:04:32 - But you can't edit there.

00:04:34 - No, no, but you can flip it back, I think, probably once you edit it there.

00:04:37 - I don't think you can edit.

00:04:39 So you can only edit in the editor part.

00:04:42 So.

00:04:42 - Yeah, it still looks really, really cool.

00:04:44 I've heard of platform as a service.

00:04:46 I've heard of infrastructure of a service.

00:04:49 I've heard of database as a service, but I guess now we have readme as a service.

00:04:52 I don't know, you just go to the website.

00:04:54 (laughing)

00:04:55 - Exactly. - That's pretty cool.

00:04:57 - Yeah, I'm pretty excited about this.

00:04:59 Actually, I might play around with this for my next project.

00:05:02 I've got some stuff that may end up on PyPI soon and it'd be cool to do it.

00:05:07 All right, so I've got the next item and it's a bit of a skateboarding dog type of thing.

00:05:13 It's not something I think a lot of us will take advantage of, but it's something that is pretty interesting as we kind of look at how Python is finding its way into the larger computing space.

00:05:23 Yeah, and oh, Sam Morley out there on the live stream before we move on says, "It'd be really cool if you could point this "at a GitHub repo and edit your repo directly, "the readme directly on your repo." Yes, absolutely, that's fantastic.

00:05:36 Yeah, it's a really good idea, really good idea.

00:05:39 All right, back to my skateboarding dog.

00:05:41 So there's a company called Cerebras, and this was sent over to us by Galen Swint, who is a PhD researcher who does high-performance computing and stuff.

00:05:53 So in that world, I think this may be a real thing.

00:05:57 You look through the article here that talks about this announcement, and it's like, well, there's like these 12 customers or 15 customers of this chip.

00:06:06 But for those of you watching, or you check out the article, there's a woman holding a chip.

00:06:11 And normally we think of computer chips as little tiny things.

00:06:13 This is a 12 inch by 12 inch computer chip, or you wanna go metric 30 centimeters by 30 centimeters.

00:06:21 It is a big, big computer chip.

00:06:24 And the idea is we've had small little chips come along to do special types of processing.

00:06:29 We've had GPUs come along and do, be adapted, I guess, for things like machine learning, training machine learning models and so on.

00:06:38 this thing just takes that idea to an entire new level.

00:06:41 So for example, I'm always going on and on and raving about my Mac mini, my M1, where it's a cheap little computer relative to Apple stuff, I guess, but it's super fast.

00:06:53 But it has four performance cores and four efficiency cores, that's it.

00:06:58 Your GPU, if you've got a really high-end one, might have 4,000 cores.

00:07:02 This insane little chip here has 850,000 AI cores on one chip, is that insane?

00:07:09 What do you think?

00:07:10 - I'm curious how they, I mean, this is some major advances in wafer technology 'cause how do you get that big of a chip with no defects in it?

00:07:19 - Yeah, and they have apparently 100% efficiency.

00:07:23 Well, first of all, one of the ways you do it is you use the TSMC foundry, who seems to be taking over all these small, high efficiency type of things.

00:07:32 And so they had a previous one that they've more than doubled the core count for.

00:07:37 And another way to kind of appreciate like how much is going on in this chip, I, you know, go back to my M1, it has 0016 billion transistors.

00:07:48 This has 2.6 trillion.

00:07:49 Or is that another way?

00:07:51 2,600 billion, yeah, billion transistors versus 1.6 billion.

00:07:55 Like it's 2000 times more on this chip.

00:07:58 So super, super cool.

00:08:00 And now you may be wondering, all right, all this is interesting and tips are neat.

00:08:03 What is the Python angle?

00:08:05 Like why would I bother putting this on here?

00:08:08 'Cause you know, we don't really talk about chips that much except for when I go on and on about my M1.

00:08:12 Here's the deal, if you scroll down in this article a little bit, you'll see users program this insane machine transparently in machine learning frameworks such as specifically TensorFlow and PyTorch.

00:08:24 - Sweet.

00:08:25 - Isn't that crazy?

00:08:26 - That's really interesting.

00:08:28 - Isn't it?

00:08:29 Yeah, I was just thinking about you as I'm going through this 'cause you're working on the Rapids project, which is not the same thing obviously, but it's kind of in that space, right?

00:08:37 - Yeah, it is.

00:08:38 - Have you heard of this before?

00:08:39 - No, I haven't heard of this.

00:08:41 This is, yeah, this is really big and I have not heard of it.

00:08:46 I will definitely be reading a bit more about it after.

00:08:49 - Yeah, yeah, for sure.

00:08:51 So there's a lot of interesting things.

00:08:52 And one of the, I can't remember where exactly they spoke about it, but they basically say, what you do is you program in TensorFlow and PyTorch as normal.

00:09:01 And then they have this custom compiler that rewrites, that extracts this execution graph to actually scale out to the 850,000 cores so the developers don't have to think about how they program against something like this.

00:09:17 I don't wanna spend too much time on this 'cause there's something, my next item is super amazing and I wanna take the time to dive into it.

00:09:22 But there's another thing that's really interesting, just as you look at it, like this thing takes an insane amount of power, like oh, for this one chip, you're gonna need a four kilowatt power supply with up to a peak power of 23 kilowatts.

00:09:39 - Yeah.

00:09:39 - Oh wow.

00:09:40 - I mean, when you plug in an electric car at one of the high speed home chargers, that's seven kilowatts, just to give you a sense.

00:09:47 This is like insane amounts for one chip, right?

00:09:51 You could think of it as a super computer, like it's one chip.

00:09:53 So anyway.

00:09:54 - Yeah, our entire lab doesn't draw that much, so.

00:09:59 - So I call, the reason I said it's a skateboarding dog I don't think most of us will be able to ever even interact with one of these, much less buy one.

00:10:06 They're going to be shipping in the later part of this year and the price is something like 3 million US dollars plus.

00:10:13 So this is certainly super computer level, but I do think it opens the door for really interesting stuff going on in the high performance Python space.

00:10:22 So yeah, glad that Galen sent it over.

00:10:25 Well, I'm totally going to put 25 bucks into Dogecoin so that I can afford this later this year.

00:10:30 - Yeah. - Speaking of which.

00:10:31 (laughing)

00:10:32 Exactly.

00:10:33 Well, what about, I think maybe you get this and you create an AI that can more intelligently mine Dogecoin and then you take over the world.

00:10:40 Just an investment.

00:10:43 - Yeah. - Just an investment.

00:10:44 All right, so speaking of large-scale high-performance computing, Marlene, take it away.

00:10:49 - Sure, I have the next item, which is RAPIDS.

00:10:53 And I wanted to speak about this because I'm working on it and it's what I've been working on for, I think, yeah, well, it's been about a year since I have been with NVIDIA, working as a software engineer there and working specifically on the Rapids project.

00:11:12 And so Rapids, I think is really interesting because the goal of Rapids, similarly, like the last thing Michael just showed us is to speed up data science, but this is with GPUs.

00:11:25 So I think it's been really cool to work on the RAPIDS project, and I think it's really interesting as well because it's open source.

00:11:37 It's also there's a lot of Python involved.

00:11:40 So it's not entirely, it's not mostly Python.

00:11:44 Actually, there's a lot of C++ and Cuda code in there as well.

00:11:49 But I am not, you know, personally, I'm not, I'm not, my aim is not to learn CUDA, it's to try and avoid that as much as possible.

00:11:58 And also avoid as much C++ as possible, so that's a bit more reasonable.

00:12:04 But one of the goals of the RAPIDS project is to allow people who are Pythonistas to work primarily with GPUs and to get those speed ups without having to know any CUDA code or to know any C++.

00:12:22 And so I have been working primarily on the Python side of things and have really been enjoying it.

00:12:29 I work specifically on with the QDF DataFrame library and QDF is basically a, it mirrors, it's a GPU DataFrame library that mirrors pandas.

00:12:43 So if you have a dataset and you'd like to do computations on your dataset or do different operations on your dataset.

00:12:51 If you can do that with pandas, you should be able hopefully to do the same thing with 3DF.

00:12:58 But the good thing is that it will probably be faster.

00:13:03 I actually can't definitively say that it will be faster because I remember when I first joined the project as well, I'm very enthusiastic and I really enjoy sharing when I'm learning something new.

00:13:19 And I remember I was like going around and speaking and saying that, you know, Kudieff is so much better than Pandas because it's just so much faster.

00:13:29 And then my manager was just like, you need to stop saying that because it's not true all of the time.

00:13:36 It's true most, like some of the time.

00:13:38 So for smaller data sets, it's probably better to stick with Pandas because the--

00:13:47 - Yeah, there's always this overhead, right?

00:13:49 Like, as you scale things out and stuff, there's probably like, well, how do we convert this over and get it onto the GPU?

00:13:55 And if that process takes half the time of what, just doing the computation, you might as well just do the computation, right?

00:14:01 - Exactly.

00:14:02 Like, if you're already, if you're mainly doing, right, I agree.

00:14:06 Like, if you're working with smaller data sets and you are fine with that and that works for you and your time is not being wasted a lot, then I would say, please go ahead and stick with Pandas.

00:14:17 But if you are working on larger datasets, and the larger your datasets get, the more the difference is gonna be in terms of your speedup.

00:14:27 So with very large datasets, QDF is gonna take a much shorter time to do computations and things like that.

00:14:34 - Yeah, you actually put a really interesting example in the show notes here, right?

00:14:38 Showing how many zeros is that?

00:14:41 100 million items or something like that?

00:14:44 - Yeah, it's a hundred million.

00:14:45 I just kind of like randomly chose a number to try and make it like, I didn't also want to take a number that was too big because I didn't want to spend like a long time doing it.

00:14:58 And I know like for a lot of data scientists, like I think increasingly people are working with larger and larger data sets, just depending which field you're in.

00:15:06 For the example, I put it on the show notes and it's on the screen right now.

00:15:11 But if you take a pound is sort of data frame and try and calculate the mean, and you take the same QDF dataset and try and calculate the mean, it will take, I think, I'm trying to look at the notes, it's 105 milliseconds for pandas, and it's like 1.83 milliseconds for QDF, which is just--

00:15:32 - That's awesome.

00:15:33 - And that's like a smaller scale, I would say, dataset compared to some people.

00:15:38 - Yeah, just 100 million, I don't know.

00:15:41 - It's just 100 million, so it's not a lot.

00:15:44 I mean, it depends, but yeah, I think it's definitely significant once you get to a certain threshold, which is pretty cool.

00:15:52 - Yeah. - Yeah.

00:15:52 - Yeah, over on the Rapid site, it's a Rapid site AI, it says it scales out on multiple GPUs, so seamlessly scale from a GPU workstation to multi GPU servers and multi node clusters working with Dask as well.

00:16:05 So that's, you know, Dask is also kind of about scaling pandas and combining those, that's pretty awesome.

00:16:10 - I actually saw that you have a DOS course out, like I recently saw it.

00:16:16 - Yes.

00:16:17 - Definitely gonna take that.

00:16:18 'Cause I mean--

00:16:19 - Yeah, check it out.

00:16:19 - I'll be diving into DOS a bit later.

00:16:21 - Awesome, yeah, yeah.

00:16:22 We put that together with Matthew Rocklin and team over at Coiled.

00:16:27 Yeah, and that's actually free, so people can just drop in and take that course.

00:16:30 I think maybe I can put it in the show notes at the end.

00:16:32 I think it was just announced, let's see.

00:16:35 - Very cool.

00:16:36 - No, that was last week.

00:16:37 But yeah, this is super cool.

00:16:38 But this one is certainly within normal person's reach.

00:16:43 You get a GPU and you're good to go, right?

00:16:46 - Yeah, I think, yeah.

00:16:47 I mean, I'm just using it on my laptop with the GPU.

00:16:50 You can also use it like online.

00:16:52 So there's also a Colab notebook on the rapid side, I think that you can click and then you can like kind of experiment if you just wanted to do it online, or I think you can use any sort of online GPU that you have access to.

00:17:09 So it's very, I think it's trying to make it more accessible which is great.

00:17:14 - Yeah, that's super cool.

00:17:15 Yeah, very neat.

00:17:16 Well, like I said, I think this is a cool project to be working on.

00:17:19 So thanks for sharing it with us.

00:17:21 Brian, is it time for the next one?

00:17:24 - Is it time for the next one?

00:17:26 This was a recommended by a listener, Ira Horeca, I think.

00:17:32 So mentioned this in, it's kind of a rabbit hole.

00:17:35 I spent a whole bunch of time playing with all this stuff.

00:17:37 last night, he recommended DateFinder.

00:17:39 This is a Python utility and it is amazing.

00:17:43 It's a combination of a couple of things.

00:17:46 He pointed us to a Comcode video, which I'm totally a fan of Comcode stuff because they go through some of the Python libraries and a lot of other things, but just have a quick demo of what it does and I really appreciate that.

00:18:03 It actually, the demo here is better than the read me in the DateFinder read me.

00:18:08 Maybe I guess a pull request is necessary.

00:18:11 But anyway, what DateFinder does is it takes, I'm going to scroll down a little bit.

00:18:18 DateFinder parses dates, it finds them.

00:18:23 You give it a string or a bunch of list of strings or something, and it can find where the dates are in there.

00:18:31 If you've got a sentence or a paragraph an entire page that has a whole bunch of dates in it.

00:18:38 It'll find all of them and then return you a list of dates that it found.

00:18:43 It actually does a whole bunch of things, but that's the default or the one that we're talking about, find dates.

00:18:49 There's a bunch of other less documented features of Date Finder, but this is the one that is demonstrated here and it's pretty cool.

00:18:58 What it does, it finds those dates and then it converts them to date times.

00:19:03 so findDates will find them and convert them to date times.

00:19:06 It does that by passing them off to the DateUtil library.

00:19:10 This is just a really cool demo.

00:19:12 The list, the little video is a good demo of showing how to do this.

00:19:19 I also really liked this way to play, so the video shows this way to play with things.

00:19:24 It just had a list of strings and then used a comprehension to convert that, to call a function on a whole bunch of strings.

00:19:33 and I thought this was just kind of a clever way to just play with a function that translates things.

00:19:38 This is a neat thing to do.

00:19:40 I would have probably-- - It's usually so hard.

00:19:41 Yeah, it's super hard normally because it's so picky, right?

00:19:45 You've gotta go to the date, time, parsing language almost lookup.

00:19:50 So if I put %DDDD, that might mean the year, but if it's capital D, it might mean something different.

00:19:56 So you might say month, day, comma, year, but like there's an example here with month, day, year without the commas like March 12, 2010.

00:20:04 But if they forget the comma, it won't parse.

00:20:06 All those things are really annoying about working with converting strings to dates.

00:20:11 This looks like it just doesn't care. It's nice.

00:20:13 >> Yeah. Then it's a nice clean interface to it as well.

00:20:18 A limited documentation is just a focus tool, which is nice.

00:20:23 It's interesting that this is just a focus tool that apparently a lot of people need because according to GitHub, there's 662 projects using this.

00:20:32 It's used all over the place.

00:20:34 The behind the scenes though, it's taking the dates that it found, the strings, and passing those to DateUtil.

00:20:42 If you want to avoid the finding part, this actually is also a good library to look at for the usage of how to use DateUtil to easily convert dates.

00:20:53 and DateUtil is an amazing tool as well.

00:20:57 I told you this is a rabbit hole.

00:21:00 One of the cool things about it is it doesn't just parse dates, but you can do relative dates.

00:21:05 You can say today plus three weeks or something, and it'll figure that out.

00:21:11 Then you can take two dates and do date math with it really well.

00:21:17 Also, DateUtil has an amazing time zone support, probably the best in Python.

00:21:22 This is pretty cool.

00:21:24 Also, I think I was looking through the test code.

00:21:27 The test code for DateUtil is a neat mix of unit test and pytest.

00:21:34 Both of them are good examples of how to do both.

00:21:37 I like some of the newer stuff is using pytest with parameterization, but it's good.

00:21:42 >> Yeah, I like this a lot.

00:21:43 Marlene, what do you think?

00:21:44 >> Yeah, I like it. I'm not actually working with dates quite often, so I'm trying to think of use cases for myself.

00:21:52 Other than maybe converting time zones, which is a nightmare.

00:21:57 >> You can say that again. Oh my God.

00:22:01 >> Maybe that, but it looks like it would be really useful for people that are working with dates a lot.

00:22:09 >> Yeah. I'm showing up some of the examples from DateUtil of how to use it.

00:22:16 I imagine this is one of the reasons why Dave Finder is so used, because this is non-trivial even to use Dave Tilt.

00:22:23 >> Yeah, that's cool.

00:22:26 I got the next one.

00:22:27 This one doesn't exactly come to us from Anthony Shaw, but I was talking to Anthony about something else and he's like, "Oh, have you heard of this?

00:22:35 Have you heard of Cinder?" Cinder is pretty awesome.

00:22:40 Anthony is doing interesting work around Python and performance at the CPython level, especially now, I think he's giving a talk on Pigeon or Piston, I believe it is.

00:22:50 I'm not 100% sure, I might be remembering which one's wrong at PyCon, which is, you know, we're going to talk more about that in just a second as well.

00:22:57 But Sender is a really interesting fork of CPython from Instagram.

00:23:03 So it's under the Facebook Incubator Project.

00:23:06 And I think we've mentioned it before, I definitely have talked about it before other presentations, that Instagram has done really interesting things like disable the garbage collector, just turn it off 100% and they got less memory usage, not more memory usage by just allowing the cycles to leak, which is insane.

00:23:24 But this is like, speaking of insane, this takes it to a whole nother level.

00:23:27 So this is, they've been doing all these low level things inside of CPython, it is based on 3.8.

00:23:33 Hopefully some of these ideas can be brought forward and shared with everyone because there's a lot going on.

00:23:38 So let me just cruise down here.

00:23:40 I'll just read the little intro part because it's jam-packed, and then I'll go into some of the details.

00:23:45 So it says, "This is the internal performance-oriented production version of CPython 3.8, and it contains a number of performance optimizations." I feel like performance is some sort of theme of this episode.

00:23:57 It includes bytecode inline caching, eager evaluations of coroutines, a JIT, just-in-time compiler, an experimental bytecode compiler that uses type annotations in some incredibly interesting ways to emit type specialized byte code that performs better.

00:24:15 So just to give you an example, one of the reasons that math in the pure Python layer is slower than say C++ or C# is C++ and C# work with just the value.

00:24:27 So if you have the value seven, you might have two or four bytes that represent the value seven.

00:24:32 In Python, you have a pyobject pointer, which is like 28 bytes pointing out to a thing on the heap that represents the number seven.

00:24:40 and it's a whole lot more work to interact with that and set the reference count on that and so on, instead of just working with the value seven, right?

00:24:48 So one of the things they do is they actually have typed, they use Python type annotations to understand, oh, this is an integer, this is a long and so on type of thing and actually convert those to the machine oriented numbers, right?

00:25:04 So just the value four instead of a pointer and then it will use what's called boxing.

00:25:07 If something else that's outside of this world needs it, it'll up level that to like a pylon object pointer type thing and hand it off.

00:25:15 So there's all sorts of stuff like that going on.

00:25:18 Interestingly, the first question is, is this supported?

00:25:21 No, not supported.

00:25:22 (laughing)

00:25:24 But there's some interesting things going on here.

00:25:28 And all of this has to be taken with an understanding that it's in a very specific context and that may or may not be useful for you.

00:25:36 Brian had pointed out some articles and ideas around that you're not Instagram, you're not Facebook, you're not Netflix and so on.

00:25:44 Most of the time people are building much smaller software with different constraints.

00:25:49 So they start out by saying, look, Instagram uses a multi-process web server architecture where the parent process starts, performs initialization and then forks 10 worker processes to handle requests.

00:26:01 This is super common.

00:26:03 Like for example, TalkByThon training literally does exactly this.

00:26:06 It uses micro-WSGI, it starts up and it creates 10 worker processes to handle like people wanting to take courses.

00:26:11 So it's not uncommon in the web, but it's not how all Python code runs.

00:26:16 And so the first optimization they did is they created what are called immortal instances.

00:26:22 The reason they were so focused on the garbage collector and all those sorts of things was when you fork these processes, initially, there's a bunch of memory that can be shared, and that helps with cache locality, that helps with overall memory usage, all sorts of things.

00:26:37 But as soon as something is changed about one of those items, it has to copy a whole page of memory.

00:26:43 And they realized that when an object's reference count is modified in one of the processes, it has to copy, replicate, and sort of fork off a bunch of the memory that used to be shared across all those processes.

00:26:56 So they created what they call immortal instances that cannot be, that don't participate in reference counting or garbage collection.

00:27:04 And that prohibits their reference count number to change so they can be shared.

00:27:07 So they can mark like a whole bunch of the startup stuff as like, just don't even look at this or change it and don't do reference counting on it.

00:27:14 So in their world, they may, it got things faster, but it doesn't always, they said it's something a little bit slower in straight line code, but in this sort of forked world, it's better.

00:27:22 The next one is shadow bytecode, which is an inline caching implementation.

00:27:27 And it goes through, applies in certain optimization cases for generic Python opcodes, and it'll observe those for functions that take a lot of time and dynamically replace those with specialized opcodes that it thinks are going to be better.

00:27:45 Another thing it does that's pretty interesting is it will eagerly evaluate coroutines.

00:27:49 So if I say, this is an async method, and then in that method, I call await some function call, normal Python's going to create a coroutine.

00:27:58 It's gonna schedule it on the asyncio event loop, and it's gonna get to it.

00:28:01 And that's a lot of overhead, but maybe that function says inside, the first thing is, if this case, just return the cached answer, otherwise go to the database, await the response and so on.

00:28:13 And what they realized is, if it's going to go through that first case, it's not actually awaiting something.

00:28:19 So they'll actually execute the awaited thing up until it actually needs to become async.

00:28:25 So it'll like look, or effectively look inside the function and say, is the path we're going on this time gonna be async or not?

00:28:32 and if the answer is no, it will run it without async, which means it skips all that context switching and all that stuff, which is pretty crazy.

00:28:39 It also has the sender JIT, which is a method in time JIT compiler, I think C#, Java, maybe even JavaScript V8.

00:28:49 So it's enabled for every function that is called.

00:28:52 Actually, it's not, sorry.

00:28:54 If it is, it'll make it slow.

00:28:56 So you can basically say which functions should be optimized but they say it supports almost everything that Python can do and it has a 1.5 to four times speed up of the Python benchmarks, which is pretty interesting.

00:29:10 They also have this thing called strict modules, which is actually a static analyzer capable of validating top-level code to see if a module has side effects and can treat it differently if it doesn't.

00:29:21 You can have an immutable strict module type that is sort of a replacement for Python's regular module it behaves and loads differently, and so on.

00:29:32 And then the thing I talked about, the numbers, more broadly is under this category of static Python.

00:29:37 It's an experimental byte code compiler that makes use of type annotations to emit better things.

00:29:43 And check this out, it can deliver performance similar to mypyC or Cython, and this thing will go up to seven times faster than regular Python for the Richards benchmarks.

00:29:55 And I don't know if the 4x improvement before is like in addition to this, so you get 28 or you just get seven, I don't really know.

00:30:02 But there's a lot of things going on here and a lot of different ideas about how this works.

00:30:08 So I'm just scratching the surface on the details, but I feel like I've gone on and on about it.

00:30:13 - That's really interesting.

00:30:14 I saw, I think, is there a talk about it at Python?

00:30:18 I think that-- - It is coming up, yes.

00:30:21 They're going to give a talk on this at Python.

00:30:22 - Yeah, it was one of the talks I was looking forward to listening to. Yeah, just because I think it's super interesting to be able to kind of play around with that they were able to kind of make their own version of Python. And it might, I don't know, like, I think that there's, like you mentioned, Anthony, and I also know Victor, I think, and someone else were also working on like sub interpreters and different and things to make Python faster.

00:30:52 So I'm really curious to see if the core devs or people will also be listening to this talk and maybe take some ideas from it.

00:31:02 It would be really cool to kind of see and I mean it's always good to get speed ups even if they, I don't know.

00:31:09 I don't know if it will help like general, like normal Python users, but I think it's always good to look into.

00:31:18 - Yeah, yeah, I agree.

00:31:20 I think some things here are absolutely convert, transferable to regular general purpose CPython, and some of them might not be.

00:31:28 For example, the immortal, the immortal instances, that might be a thing that just, they do that, and it makes sense for their large-scale farm of servers.

00:31:37 But the JIT that takes the type information and does math many, many times faster, that, everybody would want that.

00:31:44 Like, we all work with numbers at some level or another.

00:31:47 Brian?

00:31:48 >> One of the things I love about, this applies to all of these speed-up projects.

00:31:54 One of the things I love about Python is that just the generalness of it.

00:31:57 You can throw it, data structures can hold anything.

00:32:01 But there are times where you really are using a huge array of floats or a huge array of integers or a huge array of a fixed data size.

00:32:13 Those are times where I don't need it to be generic, I just need it to be fast.

00:32:19 Having something, that's the part where I think it'd be interesting to pull into regular Python.

00:32:26 But don't we get that with some of the data science stuff anyway?

00:32:31 >> With NumPy and stuff?

00:32:34 Yeah, you do, but you can't do generic programming with it.

00:32:38 You do matrix math type of things.

00:32:42 The answer used to be, "Okay, well, this function is slow.

00:32:45 this serialization deserialization section might be slow.

00:32:48 So rewrite that in Cython, for example.

00:32:50 And what's really cool about this is you can write regular Python and just put type annotations on it.

00:32:57 And then it goes as fast as Cython.

00:32:59 And you don't even have to do like a separate compiler, I believe in this world, right?

00:33:04 Because they have the JIT just knows that.

00:33:06 And then we'll like as you run it, it'll just compile and run it.

00:33:09 So which is, I think it just sort of makes some of those ideas closer and more automatic for most people.

00:33:16 >> I think I foresee a future where we have some types that affect runtime.

00:33:24 There's this tension that I sense in the Python core people of whether or not types should be just an afterthought, or whether they should be really part of the runtime.

00:33:36 I think there are some cases where having them be part of the runtime might be a good thing.

00:33:42 - Yeah, this is interesting because what they do is they define these static modules and then in there they can treat them differently.

00:33:51 - I feel like I always see on Twitter some people kind of like ranting about how they don't like that direction that Python is going in, like the idea of putting in like different annotations and things like that.

00:34:03 I've seen some people that are not super big fans of that.

00:34:07 I'm not really sure why.

00:34:09 I generally would like to understand, I think most people, or not most people, but I think some people would prefer Python to maybe remain as it is, but I do think that there's like, just having it be a bit faster in a couple of cases would be helpful.

00:34:24 So I don't know, I don't know if it's in that direction.

00:34:27 - I'm with you, and one of the things they point out in this readme announcing the project is that you can still do gradual typing.

00:34:35 So you can, in some places, have no types, in some places have some types, and the thing can convert and just deal with that automatically.

00:34:42 And I think that's the reason that the types are really welcome in Python, is because you can use them if you want, but you don't have to.

00:34:48 As opposed to places like TypeScript, which said, "Well, JavaScript doesn't have types, so we're going to add this very strict type system, and if you don't fit it exactly, we're going to not compile and complain, and it's going to be really not good." This feels like it continues that forgiving nature of Python to let you opt into it.

00:35:05 But if you do, it can go faster.

00:35:08 - That's the direction I'd like to see.

00:35:09 I'd like to see, I personally would like to see types be really a full-fledged feature of Python.

00:35:16 - Yeah, I agree.

00:35:18 - I love that they're optional, but if they're there, let's see how much we can do and improve things with them, right?

00:35:24 - 100%.

00:35:25 - Yeah, all right.

00:35:26 Marlene, you got the last one.

00:35:27 I got it on screen for you.

00:35:28 - Okay, yes.

00:35:29 The last one for today is PyCon US, which I'm very excited about.

00:35:35 It started today, which is really great.

00:35:39 Are both you attending?

00:35:41 I don't know if you're attending.

00:35:43 But-- - Yes, absolutely.

00:35:45 - Okay.

00:35:47 Brian, are you attending? - Yes.

00:35:48 - Yay.

00:35:50 Yeah, I think it's such a great event in terms of the fact that I know it's PyCon US, but it is, at the moment, it's the largest Python gathering or largest PyCon on Earth, I think, which is very cool because it means that you can meet people from all around the world.

00:36:08 Like I remember, I'm really sad that it's not in person because like last year, like I've, not last year, but the year before that, that's where I actually met you, Michael, for the first time.

00:36:20 I think we were literally, I think we were like at a table with like you and Anthony Shaw and like Lucas Longa.

00:36:27 And it was like, and I was just randomly there, but it was such a cool discussion.

00:36:33 and I really love the idea of being able to be in a room with people that are contributing to Python.

00:36:41 So very excited.

00:36:42 - That's my favorite part of PyCon.

00:36:43 - Yeah, it is.

00:36:44 - It was so nice to meet you as well.

00:36:46 That is actually my favorite part of PyCon, is the, just, you happen to end up at a table or out for a beer or coffee with this group of people and you're like, wow, I got these connections and this experience that just, I wouldn't.

00:36:59 So I'm very much looking forward to coming back in person.

00:37:01 but there's a bunch of great talks coming up.

00:37:04 - Exactly, so this year it's also really, although it's online, the online platform is very cool and there's still lots of great tools to watch.

00:37:14 In the show notes I put down a list of the tools that I'm excited to watch, but I also wanted to just put in a word for the things that I will be doing at PyCon US this year.

00:37:23 And the first thing I'm gonna be doing is I'm gonna be hosting the diversity and inclusion work group discussion along with four other really amazing women that are part of the diversity and inclusion work group.

00:37:36 I do wanna comment here because I thought like we got some comments about it, some feedback.

00:37:44 I posted a picture of like our group that's gonna be having this discussion or hosting this panel and it's all women.

00:37:50 And someone was just like, why is it all women?

00:37:52 How is this diversity?

00:37:53 So I do wanna throw it out there.

00:37:58 I just wanna throw it out there that we did try, like the work group itself has a lot of, it has a good balance of men and women in it.

00:38:06 But then when I asked people if they wanna come on the panel, it was only like women that volunteered.

00:38:11 So it's on my halt and I am aware of that.

00:38:14 That's just a general, or that's just general feedback there.

00:38:18 But I think the panel will be really exciting.

00:38:25 It's gonna be on Saturday on the main stage at 12 p.m. EST, I think.

00:38:31 If you're gonna be there, I really would encourage you to attend.

00:38:34 There's gonna be question and answer.

00:38:36 And I just think it's such an important thing.

00:38:38 I know that sometimes diversity can seem like a really tiring thing to talk about, especially like recently.

00:38:46 I feel like sometimes people use it as like this buzzword and it can, and people can be like, oh my gosh, and just turn off when they hear the word diversity.

00:38:55 But I really do think it's important.

00:38:57 And particularly now as Python is growing in popularity, I think a few years ago, it was okay for the nucleus of Python to be based in the United States or based in Europe, but it's growing so quickly.

00:39:13 Python for I don't know how many years now has been the most popular language in the world.

00:39:18 And I know even for me, I'm in Zimbabwe right now, and it's one of the most popular languages here where I live.

00:39:25 And so just providing the group, like our main purpose is to figure out how we can support the PSF to try and serve Pythonistas from around the world better and to connect the community better and have better representation and different things like that so very excited about that one.

00:39:44 - That's awesome and thanks for your work here.

00:39:47 I definitely agree that we're stronger together, right?

00:39:51 And one thing I would really like to see and I think we're getting there is when people look at Python, and programming in general, but generally the Python space, we have influence over that.

00:40:01 When people look at that world, I would like them to say, I can see myself being part of that.

00:40:06 I can see that I could belong there, right?

00:40:08 And if that's not the case, then how do we make that the case?

00:40:11 - Exactly, absolutely.

00:40:13 I think exactly that.

00:40:15 And I would love to see that happening in the next few years.

00:40:19 I would love to see, one of my things is that I'd love to see more women core developers and more like global core developers as well, and also people on the board and different things.

00:40:29 And those are all goals that we are working towards.

00:40:31 And obviously we don't know like the perfect way to achieve something or the perfect way to do things, but it's something that I think is really great and exciting to work on.

00:40:42 So please attend if you are listening to this.

00:40:45 And let me know if you like came from this podcast, it would be fantastic to see you there.

00:40:51 Maybe just comment.

00:40:53 - Fantastic.

00:40:53 - And then, oh, another thing that I am doing for Python this year as well is I will be, one, I will be in the, so there's like a lounge area.

00:41:05 Well, there's like a PSF booth, and if you would like to just, if you're gonna be there in the morning on Saturday or on Friday, I will be hanging out in the PSF booth.

00:41:15 And so yeah, if you just wanna talk about Python or the PSF or anything, I will be there.

00:41:20 And I will also be hosting the EMEA meeting.

00:41:24 So if you're in Europe, the Middle East, or Africa, there's a members meeting on Saturday.

00:41:30 I think it's at 10 a.m. Central African time.

00:41:34 I'm not sure what time that is in other places.

00:41:36 But I know it's at 10 a.m.

00:41:39 - It's on the schedule, right?

00:41:40 It's on the schedule.

00:41:41 - Yeah, we can use the date time thing, I don't know, you remember.

00:41:45 - Exactly.

00:41:46 Pull up the REPL, throw it into date time.

00:41:47 - Exactly, please do that.

00:41:49 (laughs)

00:41:50 So I will be hosting that, and that's gonna be in the morning.

00:41:54 And if you would like, even if you're not a member, you can watch it on the PSA YouTube channel.

00:42:00 It's gonna be streaming there, or you could join, there's a meetup link that I put in the show notes.

00:42:04 So people could join that way as well.

00:42:06 So yeah, Python is gonna be really exciting, and I'm really looking forward to it.

00:42:11 So just encouraging people to come along, for sure.

00:42:14 - Yeah, it should be fun.

00:42:15 And even though it is super sad that it's not in person, it's not in Pittsburgh this year.

00:42:21 I think in some ways it's more accessible to people around the world, right?

00:42:25 They don't have to travel there.

00:42:26 They can just log in and attend it.

00:42:29 And that's so much less expensive than I flew to the US and I paid $1,000 for a hotel.

00:42:35 So there's a little silver lining, you know, out there in the live stream.

00:42:39 Sam Morley really says, "I really wish I could go to PyCon in person." Adam Parkin there says, "Me too, maybe in 2020." I think so.

00:42:47 Finally, Sam is also thinks it's great that we're having this diversity conversation and paying attention to it.

00:42:53 - One of the things I've noticed in 2020 is all the regional, actually last year also though, but the 2020 and 2021, we've got all these PyCons going on all over the world.

00:43:07 I used to think of like PyCon US as the PyCon and everything else is regional.

00:43:13 Now I think of PyCon US as a regional conference also it's the regional one that's close to the people that are in the US.

00:43:21 It isn't necessarily better.

00:43:24 I love it. It's great.

00:43:26 Anybody that's hosting it, yes, it's better.

00:43:29 But no, I like all of them and I was excited to get to participate and watch videos from all over the world this year.

00:43:39 That was pretty neat. But yeah, I'm on board with, I want to get back to regional stuff.

00:43:46 I'd like to see people in person. I can't wait.

00:43:49 >> Yeah, I will say for sure, even if people are feeling adventurous, there is a regional conference, I didn't mention it before, that I am also part of the organizing team for, which is PyCon Africa.

00:44:02 If you would like to travel to another PyCon in a different part of the world, when we are able to travel and the world gets back to some form of free travel, Definitely recommend also hopping over to Python Africa.

00:44:19 I think, like you said, I think Python US is fantastic.

00:44:24 One of the unique things about that is that it's a conference that has been there for so long, so a lot of people are going to be there.

00:44:32 But there are 100 percent are a lot of great conferences like Python Africa, which you should attend if you can.

00:44:40 I think they're really just as exciting and there's so many cool things that you get to experience.

00:44:45 Like I think for me, it's like whenever I go to the US, like last year, I'd never been to Ohio before.

00:44:52 And like, I had never, like I would never, like in my, I would never have a reason that I would think to myself, let me go to America to go to Ohio.

00:45:02 But I feel like it was such a good experience for me and I really liked it and I was really surprised by that.

00:45:10 And so I think it's the same way, like pythons are a great way as well to like experience new places.

00:45:16 So yeah, definitely sticking in that.

00:45:18 Well, that's wraps up our six.

00:45:21 anybody got any extra information to share?

00:45:24 Nothing else for me other than the fact that if you do want to reach out to me, you can reach out to me on Twitter. I'm Marlene_Zaw there.

00:45:34 I'm also Marlene_Zaw on, on GitHub, I think.

00:45:38 and on my website.

00:45:40 My website is marleenmangami.com.

00:45:43 So if you would like to reach out to me here, feel free to.

00:45:47 I'm always happy to like chat about Python.

00:45:50 - Nice. - Cool.

00:45:51 - So I got a couple.

00:45:52 One made me really excited.

00:45:53 This tweet from GitHub, is your fork behind?

00:45:57 You can now sync your parent repo with just a single click.

00:46:01 So check this out.

00:46:02 If you go to your fork now, next to contribute for your PRs and stuff, there is now a fetch upstream button and all you have to do is click it and then automatically your fork will become in sync with whatever you forked it from.

00:46:16 You still have to go and go check it out, add an upstream origin and then pull from that and then merge that wherever you want it to go to.

00:46:24 Over here, you just click this button and boom, it's good to go.

00:46:28 So I think this will just lower the bar for people working something, they wanna get the current one and then make a change to see if they could contribute back.

00:46:35 here's one fewer steps in that process.

00:46:38 >> Any idea if it stays in sync or if you have to-

00:46:41 >> No, it's a one-time type of thing, I believe.

00:46:44 It says there's this many changes, we'll pull over and it basically just automatically does the process at that time.

00:46:49 >> Nice.

00:46:50 >> But still pretty nice.

00:46:51 Here, Flask 2.0 is out and that one was sent into us from Adam Parkin that, "Hey, heads up, this is now actually live." Very cool.

00:47:03 Actually, everything from palettes has been updated.

00:47:06 So yeah, I happen to have spoken, done a podcast recording with David Lord who runs palettes and Phil Jones who does core and contributes back to palettes as well about all the stuff coming in Flask 2.0, all the exciting stuff and their future plans as well.

00:47:22 So yeah, you can watch the live stream of that or wait a day or two until the episode is out and just listen at Talk Python as well.

00:47:29 But yeah, very, very cool.

00:47:30 Yeah. And then Adam also had a live stream again, says this super sweet always find it a headache to sync with upstream.

00:47:36 Yeah, about the GitHub thing.

00:47:37 That's that's cool.

00:47:38 Cool.

00:47:38 Close it out with a joke.

00:47:39 Well, I got a couple of things I wanted to mention.

00:47:42 Go for it.

00:47:42 Sorry.

00:47:43 I had Brett Cannon on last week on testing code and huge feedback from everybody that it was a great episode.

00:47:51 We talked about packaging.

00:47:52 I'll have Ryan Howard on this week talking about Playwright.

00:47:56 So that'll be fun.

00:47:57 And I wanted to mention a thank you to the 71 patrons that we have on Patreon.

00:48:03 So thank you for supporting the show.

00:48:05 Thanks.

00:48:06 Yeah, thank you, everyone.

00:48:07 How about a joke?

00:48:08 Joke, yes.

00:48:09 Sorry for almost skipping over your extras here.

00:48:13 No worries.

00:48:14 You ready? Yeah.

00:48:16 So this one we talked I talked about that crazy giant ship thing.

00:48:20 And we've got Marlene doing rapid.

00:48:22 So I thought maybe some kind of machine learning joke.

00:48:24 Here's a bunch of robots in school.

00:48:29 And they go like little Android looking thing.

00:48:32 Small ones because they're students, they're kids.

00:48:35 And they're in machine learning class.

00:48:36 And there's a big box of dirty data.

00:48:40 Like a bunch of bits that are like kind of gray and they just have dirt on them.

00:48:44 And the teacher says, "Robby, stop misbehaving or I will send you back to data cleaning." [Laughter]

00:48:51 >> Oh.

00:48:53 >> Yeah.

00:48:54 >> That's where they're spending half the day anyway.

00:48:56 >> Yeah, they actually spend most of their time there.

00:48:58 That's right.

00:48:59 I don't know who is drawing them.

00:49:00 Like one of the robots is looking the wrong way.

00:49:03 I was like, why is it drawn like that?

00:49:04 I don't understand.

00:49:05 - Hey, a more concrete, really quick closeout question I see in the live stream here is, Akmal, is there a difference between Kud-F and pandas in terms of utilization?

00:49:18 - Like in terms of how you actually use them?

00:49:23 Well, I don't think so.

00:49:26 For the most part, when you're using QDF, the way it's built is to mirror Pandas, so the APIs are really similar.

00:49:35 Ideally, the methods that you would use when you're using Pandas are exactly the same methods that you would use when you're using QDF.

00:49:43 The only difference is when you're creating a Pandas DataFrame, for example, you would use pd.DataFrame, for example.

00:49:51 But then with QDF, you would say qdf.DataFrame.

00:49:54 If you make it into a variable or something like that, then the methods that you're gonna pull are gonna be probably identical.

00:50:02 It's really easy to print.

00:50:03 - Yeah, that's awesome.

00:50:05 Yeah, and Dask has similar stuff as well, right?

00:50:07 You create a Dask data frame instead of a Pandas data frame, but the API looks quite similar.

00:50:11 They're not always 100% compatible, but most of the mainstream things, right?

00:50:16 - Definitely, so yeah, it's built definitely to make it as easy as possible to switch between the two, to you. So it's very similar to y'all.

00:50:24 Thanks a lot, everybody, for showing up.

00:50:26 Yeah, thanks. Thanks, Marlene. It's really great to have you here.

00:50:30 No problem. Thanks for having me.

00:50:32 Thank you for listening to Python Bytes. Follow the show on Twitter via @pythonbytes. That's Python Bytes as in B-Y-T-E-S. And get the full show notes at pythonbytes.fm. If you have a news item you want featured, just visit pythonbytes.fm and send it our way. We're always on the lookout for sharing something cool. On behalf of myself and Brian Aukin, This is Michael Kennedy.

00:50:54 Thank you for listening and sharing this podcast with your friends and colleagues.

