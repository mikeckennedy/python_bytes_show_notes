00:00:00 Hello and welcome to Python Bytes, where we deliver news and headlines directly to your earbuds.

00:00:05 This is episode 233, recorded May 12, 2021, and I'm Brian Okken.

00:00:11 I'm Michael Kennedy.

00:00:12 And I'm Marlene Mangami.

00:00:13 Well, welcome, Marlene. For people who don't know you, can you introduce who you are?

00:00:18 So I am a Pythonista, of course, and I am based in Hawaii, Zimbabwe.

00:00:26 I am also really involved with the Python community.

00:00:30 So I'm currently the vice chair of the PSA Board of Directors.

00:00:34 The board, I think, for about coming up on four years now, which is really exciting.

00:00:41 And it's been really a very cool experience for me.

00:00:44 I'm also a software engineer.

00:00:47 I work right now with the Rapids team at NVIDIA and have just been doing software engineering with them.

00:00:53 I will talk a bit about that later.

00:00:55 But yeah, I'm trying to think what else.

00:00:59 I'm also a very avid reader and just like doing other things besides software.

00:01:04 So yeah, that's pretty much me.

00:01:07 Cool.

00:01:08 That's awesome.

00:01:08 You're doing a bunch of cool stuff.

00:01:10 So I think Rapids seems like a really neat project to work on as well.

00:01:13 And of course, the Python community side is great.

00:01:17 So super happy to have you here.

00:01:18 Brian, you know, having a good readme is really important to a project, wouldn't you say?

00:01:23 Yeah, definitely.

00:01:24 And I, for some reason, I don't know, readmes are not difficult to write, but I freeze up.

00:01:31 It's a blank page syndrome.

00:01:32 I think often I've gone through and just like copied from some other project.

00:01:37 What's in there?

00:01:38 Readme.

00:01:39 But I don't think that that's like the best way to go about it, really, because sometimes you forget stuff.

00:01:45 So this was a, we have a recommendation from Johnny Metz.

00:01:49 It's a tool called readme.so.

00:01:53 And this is like totally fun.

00:01:55 It's just this interactive thing where you get to add stuff.

00:02:00 So we've got the title.

00:02:01 You can, there's on the left-hand side, there's a bunch of sections where you can select what you want to go into the readme.

00:02:08 And then it shows a preview on the right, but you can also see the raw markdown.

00:02:15 And then in the middle, there's an editor.

00:02:17 So you can actually just edit the whole thing here.

00:02:19 But really, I don't know if I really would project title.

00:02:24 What I'd probably do is go through and, you know, pick out to look at what sort of things I'd want.

00:02:30 So I'd probably maybe some acknowledgements if I took the, if I got some help from somebody, maybe an API reference.

00:02:36 If it's got a, if it's a library, how to contribute.

00:02:40 Oh, badges.

00:02:42 Definitely want badges.

00:02:43 Oh, yeah.

00:02:44 And then, you know, maybe like how to run tests if you want to contribute.

00:02:48 If there's other cool projects using it, I'd want to use by all these sort of things.

00:02:54 And then you can, the editor only selects, it only shows you the ones, the one at a time, which is nice.

00:03:00 But then you've got this, this whole generated, really nice looking readme with tables and everything like built in.

00:03:09 And you can either just copy it or download it and just run with it.

00:03:12 I think this is really great.

00:03:14 I'll probably use this in the future.

00:03:16 I really love this.

00:03:17 And I'm surprised about the psychological benefit of just showing the little, the section with the one heading.

00:03:24 So for like example, acknowledgements, you just have hash, hash acknowledgements.

00:03:28 And then the few things, even though you're editing the whole readme, it seems so much more like, oh, I'm going to just work on that section.

00:03:34 It's really cool.

00:03:35 Marlene, what do you think?

00:03:36 It's really, really cool.

00:03:37 I like it.

00:03:38 I think I'm going to try it out.

00:03:40 I have put no if it at all in this.

00:03:45 So I think it's, it's something I need to put more if it into.

00:03:49 And this looks like a really good way to do that.

00:03:51 So, yeah.

00:03:52 I think that it would also be great to just like, if you have an existing readme and you want to add some new sections, you're not quite sure how it should look.

00:03:59 Using this as a jumping point of just to grab sections of a readme to add to an existing one too.

00:04:04 This would be great.

00:04:05 Yeah.

00:04:06 This is really, really cool.

00:04:08 How do you, how do you, can you start with a new one?

00:04:12 Like, can I, well, sorry, let me take it back.

00:04:13 Can I start with an existing one?

00:04:15 Can I somehow upload an existing one?

00:04:17 I don't see.

00:04:18 I don't think so.

00:04:19 Wait, I can go to raw.

00:04:21 Hold on.

00:04:22 Oh, you can probably just drop it into raw.

00:04:24 Maybe.

00:04:24 Yes, you can drop it into the raw.

00:04:26 That's it.

00:04:26 Okay, perfect.

00:04:27 You go to raw, which it doesn't hide the sections.

00:04:29 It's just pure markdown.

00:04:30 And then you just throw it in there.

00:04:31 Okay.

00:04:32 But you can't edit there.

00:04:34 No, no, but you can flip it back.

00:04:35 I think probably once you edit it there.

00:04:37 I don't think you can edit.

00:04:38 So you can only edit in the, like the editor part.

00:04:41 So.

00:04:42 Yeah.

00:04:42 It still looks really, really cool.

00:04:43 I've, I've heard of platform as a service.

00:04:46 I've heard of infrastructure as a service.

00:04:49 I've heard of database as a service, but I guess now we have read me as a service.

00:04:52 I don't know.

00:04:52 You just go to the website.

00:04:53 Exactly.

00:04:55 That's pretty cool.

00:04:56 Yeah.

00:04:57 I'm, I'm, I'm pretty excited about this.

00:04:59 Actually, I might, I might play around with this, for my next project.

00:05:02 I've got some stuff that may end up on PyPI soon and it'd be cool to do it.

00:05:07 All right.

00:05:07 So I've got the next item and it's a bit of, a skateboarding dog type of thing.

00:05:13 It's not something I think a lot of us will take advantage of, but it's something that is

00:05:16 pretty interesting as we kind of look at how Python is finding its way into the larger

00:05:22 computing space.

00:05:23 Yeah.

00:05:24 And Oh, Sam Morley out there and the live stream before we move on says, it'd be

00:05:28 really cool if you could point this at a GitHub repo and edit your repo directly.

00:05:32 the read me directly on your repo.

00:05:34 Yes, absolutely.

00:05:35 That's fantastic.

00:05:36 Yeah.

00:05:37 That's a really good idea.

00:05:38 Really good idea.

00:05:39 All right.

00:05:40 Back to my skateboarding dog.

00:05:41 So there's a company called Sarah brass, and this was sent over to, to us by Galen

00:05:48 Swint, who is a PhD researcher who does high performance computing.

00:05:53 And stuff.

00:05:53 So in that world, I think this, this may be a real thing.

00:05:57 You look through the article here that talks about this announcement and it's like, well,

00:06:01 there's like these 12 customers or 15 customers of this, this chip.

00:06:05 But for those of you watching, there's, or you check out the article, there's a woman holding

00:06:10 a chip.

00:06:11 And normally we think of computer chips as little tiny things.

00:06:13 This is a 12 inch by 12 inch computer chip, or you want to go metric 30 centimeters by 30

00:06:20 centimeters.

00:06:20 It is a big, big computer chip.

00:06:23 And the idea is we've had small little chips come along to do special types of processing.

00:06:29 We've had GPUs come along and do, be adapted, I guess, for things like machine learning, training

00:06:35 machine learning models.

00:06:36 This thing just takes that idea to an entire new level.

00:06:41 So for example, I'm always going on and on and raving about my Mac mini, my M1, where,

00:06:48 it's a cheap little computer relative to Apple stuff, I guess.

00:06:51 but it's, it's super fast, but it has four performance cores and four efficiency cores.

00:06:57 That's it.

00:06:57 your GPU, if you've got a really high end one might have 4,000 cores.

00:07:01 This insane little chip here has 850,000 AI cores on one chip.

00:07:08 Is that insane?

00:07:09 What do you, what do you do think?

00:07:10 I, I'm, I'm curious how they, I mean, this is, this is some major advances in, in wafer technology,

00:07:16 because how do you get that big of a chip with no defects in it?

00:07:19 Yeah.

00:07:20 And they have apparently 100%, efficiency.

00:07:23 Well, first of all, one of the ways you do it is you use the TSMC foundry, who seems to

00:07:28 be taking over all these small high efficiency, type of things.

00:07:32 And so they had a previous one that they've more than doubled the core count for.

00:07:36 And another way to kind of appreciate like how much is going on in this chip, I, you know,

00:07:41 go back to my, my M1, it has a zero, zero, one, six brilliant transistors.

00:07:47 This has 2.6 trillion.

00:07:49 Or is that another way?

00:07:50 2,600 billion, a billion transistors versus 1.6 billion.

00:07:55 Like it's a 2,000 times more on this chip.

00:07:58 So super, super cool.

00:08:00 And now you may be wondering, all right, all this is interesting and tips are neat.

00:08:03 What is the Python angle?

00:08:05 Like, why would I bother putting this on here?

00:08:08 Cause you know, we don't really talk about chips that much, except for when I go on and

00:08:11 on about my M1.

00:08:12 Here's the deal.

00:08:12 If you scroll down in this article a little bit, you'll see user program, this insane machine

00:08:17 transparently in machine learning frameworks, such as specifically TensorFlow and PyTorch.

00:08:23 Isn't that crazy?

00:08:25 That's really interesting.

00:08:27 Isn't it?

00:08:28 Yeah.

00:08:28 I said, I was just thinking about you as I'm going through this, cause you're working on the

00:08:31 Rapids project, which is, it's not the same thing obviously, but it's kind of in that space,

00:08:36 right?

00:08:36 Yeah, it is.

00:08:38 Have you heard of this before?

00:08:39 No, I haven't heard of it.

00:08:41 This is, yeah, this is really big and I have not heard of it.

00:08:45 Yeah.

00:08:46 I will get into reading a bit more about it after.

00:08:49 Yeah.

00:08:49 Yeah, for sure.

00:08:51 So there's a lot of interesting things.

00:08:52 And one of the, I can't remember where exactly they spoke about it, but they basically say,

00:08:57 what you do is you program and TensorFlow and PyTorch as normal.

00:09:00 And then they have this custom compiler that, that rewrites, that extracts this execution

00:09:07 graph to actually scale out to the 850,000 cores to the developers don't have to think about

00:09:14 how they program against something like this.

00:09:17 I don't want to spend too much time on this because there's something, my next item is

00:09:20 super amazing.

00:09:20 I want to take the time to dive into it.

00:09:22 But there's another thing that's really interesting.

00:09:25 Just as you look at it, like this thing takes an insane amount of power.

00:09:30 Like, oh, for this one chip, you're going to need a four kilowatt power supply with up to

00:09:36 a peak power of 23 kilowatts.

00:09:39 Oh, wow.

00:09:41 When you plug in an electric car at one of the high speed home chargers, that's seven

00:09:45 kilowatts, just to give you a sense.

00:09:47 This is like insane amounts for one chip, right?

00:09:51 You could think of it as a supercomputer.

00:09:52 Like it's one chip.

00:09:53 So anyway.

00:09:54 Our entire lab doesn't draw that much.

00:09:58 So the reason I said it's a skateboarding dog thing is I don't think most of us will be

00:10:03 able to ever even interact with one of these, much less buy one.

00:10:06 They're going to be shipping in the later part of this year.

00:10:09 And the price is something like $3 million plus.

00:10:13 So this is certainly super computer level.

00:10:15 But I do think it opens the door for really interesting stuff going on in the high performance

00:10:21 Python space.

00:10:22 So yeah.

00:10:23 Glad that Galen sent it over.

00:10:25 Well, I'm totally going to put $25 into Dogecoin so that I can afford this later this year.

00:10:29 Oh, speaking of which.

00:10:31 Exactly.

00:10:33 Well, what about, I think maybe you get this and you create an AI that can more intelligently

00:10:38 mine Dogecoin and then you take over the world.

00:10:40 Just an investment.

00:10:42 Yeah.

00:10:43 Just an investment.

00:10:43 All right.

00:10:45 So speaking of large scale, high performance computing, Marlene, take it away.

00:10:49 Sure.

00:10:50 I have the next item, which is Rapid.

00:10:53 And I wanted to speak about this because I'm working on it.

00:10:58 And it's what I've been working on for, I think.

00:11:00 Yeah.

00:11:01 Wow.

00:11:01 It's been about a year since I have been with NVIDIA.

00:11:07 working as a software engineer there and working specifically on the Rapids project.

00:11:12 And so Rapids, I think, is really interesting because the goal of Rapids, similarly, like the

00:11:19 last thing Michael just showed us, is to speed up data science.

00:11:23 But this is what GPUs.

00:11:25 So I think it's really, it's been really cool to work on the Rapids project.

00:11:32 And I think it's really interesting as well because it's open source.

00:11:37 It's also, there's a lot of Python involved.

00:11:40 So it's, well, it's not entirely, it's not mostly Python.

00:11:44 Actually, there's a lot of C++ and Cuda code in there as well.

00:11:49 But I am not, you know, personally, I'm not, I'm not, my aim is not to learn Cuda.

00:11:55 It's to try and avoid that as much as possible.

00:11:57 And also avoid as much C++ as possible.

00:12:01 So that's a bit more reasonable.

00:12:03 But one of the goals of the Rapids project is to allow people who are Pythonistas to work

00:12:11 primarily with GPUs and to get those speed ups without having to know any Cuda code or

00:12:19 to know any C++.

00:12:21 And so I have been working primarily on the Python side of things and have really been enjoying it.

00:12:29 I work specifically on, with the QDF data frame library.

00:12:34 And QDF is basically a, it mirrors, it's a, it's a GPU data frame library that mirrors pandas.

00:12:43 So if you have a data set and you'd like to do computations on your data set or do different

00:12:49 operations on your data set, if you can do that with pandas, you should be able, hopefully,

00:12:55 to do the same thing with QDF.

00:12:57 But the good thing is that it will be, it will, it will probably be faster.

00:13:03 I actually can't definitively say that it will be faster because I remember when I first joined

00:13:10 the project as well, I was, I really, I'm very enthusiastic and I really enjoy sort of sharing

00:13:17 when I'm learning something new.

00:13:19 And I remember I was like going around and speaking and saying that, you know, QDF is

00:13:25 so much better than pandas because it's just so much faster.

00:13:29 And then my manager was just like, you need to stop saying that because it's not true all

00:13:35 of the time.

00:13:36 it's true most like some of the time.

00:13:38 So for smaller data sets, it's probably better to stick with pandas because.

00:13:46 Yeah.

00:13:47 There's always this overhead, right?

00:13:48 Like as you scale things out and stuff, there's probably like, well, how do we convert this over

00:13:53 and get it onto the GPU?

00:13:55 And if, if that process takes half the time of what just doing the computation, you might

00:14:00 as well just do the computation, right?

00:14:01 Exactly.

00:14:02 Like if you're already, if you're mainly doing, right, I agree.

00:14:05 Like if you're working with smaller data sets and you are fine with that and that works for

00:14:11 you and your time is not like being wasted a lot, then I would say, please go ahead and

00:14:16 stick with pandas.

00:14:17 But if you have, if you are working on like larger data sets and the larger your data sets

00:14:24 get, the more the difference is going to be in terms of your speed up.

00:14:27 So with very large data sets, QDF is going to take a much shorter time to do computations

00:14:33 and things like that.

00:14:34 Yeah.

00:14:35 You've actually put a really interesting example in the show notes here, right?

00:14:38 Showing how many zeros is that?

00:14:40 A hundred million items or something like that?

00:14:44 Yeah.

00:14:44 It's a hundred million.

00:14:45 I just kind of like randomly chose a number to try and make it like, I didn't also want to

00:14:51 take a number that was too big because I didn't want to spend like a long time doing it.

00:14:58 And I know like for a lot of data scientists, like I think increasingly people are working

00:15:02 with larger and larger data sets, just depending which field you're in.

00:15:06 For the example, I put it on the show notes and it's on the screen right now.

00:15:10 But if you take a Pandas sort of data frame and try and calculate the mean and you take

00:15:16 the same QDF data set and try and calculate the mean, it will take, I think I'm trying to

00:15:22 look at the notes.

00:15:22 It's 105 milliseconds for Pandas and it's like 1.83 milliseconds for QDF, which is just,

00:15:32 That's awesome.

00:15:33 And that's like a smaller scale, I would say, data sets compared to some people.

00:15:39 Yeah, just a hundred million.

00:15:40 It's just a hundred million.

00:15:42 So it's not a lot.

00:15:44 I mean, it depends.

00:15:45 But yeah, I think it's definitely significant once you get to a certain threshold, which is

00:15:51 pretty cool.

00:15:51 Yeah.

00:15:52 Yeah.

00:15:52 Over on the rapid site, it's a rapid site AI.

00:15:55 It says it scales out on multiple GPUs.

00:15:58 So seamlessly scale from a GPU workstation to multi GPU servers and multi node clusters working

00:16:04 with Dask as well.

00:16:05 So Dask is also kind of about scaling Pandas and combining those.

00:16:09 That's pretty awesome.

00:16:10 So I actually saw that you have a Dask course out.

00:16:14 Like I recently thought, yes, definitely going to take that because I mean, yeah, check it

00:16:19 out.

00:16:19 That one's awesome.

00:16:21 Yeah.

00:16:22 Yeah.

00:16:22 We put that together with Matthew Rocklin and team over at Coiled.

00:16:27 Yeah.

00:16:27 And that's actually free.

00:16:28 So people can just drop in and take that course.

00:16:30 I think maybe I can put it in the show notes at the end.

00:16:32 I think it just just announced.

00:16:34 Let's see.

00:16:35 Very cool.

00:16:36 No, that was a lot.

00:16:37 That was last week.

00:16:37 But yeah, this is super cool.

00:16:38 And this one is certainly within normal person's reach.

00:16:43 You get a GPU and you're good to go.

00:16:45 Right?

00:16:45 Yeah.

00:16:46 I think.

00:16:46 Yeah.

00:16:47 I mean, I'm just using it on my laptop with the GPU.

00:16:50 You can also use it like online.

00:16:52 So there's also a CoLab notebook on the rapid side.

00:16:58 I think that you can click and then you can like kind of experiment if you just wanted to

00:17:02 do it online.

00:17:03 Or I think you can use any sort of online GPU that you have access to.

00:17:08 So it's very, I think it's trying to make it more accessible, which is great.

00:17:14 Yeah.

00:17:14 That's super cool.

00:17:15 Yeah.

00:17:16 Very neat.

00:17:16 Well, like I said, I think this is a cool project to be working on.

00:17:19 So thanks for sharing it with us.

00:17:20 No problem.

00:17:21 Ryan, is it time for the next one?

00:17:23 Is it time for the next one?

00:17:26 yes.

00:17:27 This was a recommended by a listener, Ira Horeca, I think.

00:17:32 So mentioned this in, it's kind of a rabbit hole.

00:17:35 I spent a whole bunch of time playing with all this stuff last night.

00:17:37 He recommended Date Finder.

00:17:39 So this is a Python utility and it kind of is amazing.

00:17:43 So it's a combination of a couple of things.

00:17:45 But so he pointed us to a comcode video, which, you know, I'm totally a fan of comcode stuff

00:17:53 because they kind of go through some of the Python libraries and some of the other, a lot

00:17:57 of other things, but just have kind of a quick demo of what it does.

00:18:01 And I really appreciate that.

00:18:03 It actually, the demo here is better than the read me in the, date finder, read me.

00:18:08 So, so maybe I guess a pull request is necessary, but anyway.

00:18:12 So what is, what date finder does is it takes, I'm going to scroll down a little bit.

00:18:17 So, date finder takes, it parses dates or finds them.

00:18:23 So it, you give it a string or a bunch of, list of strings or something, and it can find,

00:18:29 find where the dates are in there.

00:18:31 So if you've got, if you've got a sentence or a paragraph or, an entire page that has

00:18:36 a whole bunch of dates in it, it'll find all of them and then return you a list of,

00:18:42 of dates that it found.

00:18:43 It actually does a whole bunch of things, but that's the default or the one that

00:18:48 we're talking about find dates.

00:18:49 There's a bunch of other, Leslie, less documented, features of, date finder,

00:18:54 but this, this is the one that is demonstrated here and it's pretty cool.

00:18:58 So what it does, it finds those dates and then you can, and then it converts them to

00:19:02 date times.

00:19:03 So find dates will find them and convert them to date times.

00:19:06 And it does that by passing them off to the date util library.

00:19:09 So, this is just kind of a really cool demo that the list, the little video is

00:19:14 a good demo, of showing, showing how to, how to do this.

00:19:19 I also really kind of liked this way to play.

00:19:21 So the video shows this way to play with things of, of it just had a list of strings

00:19:26 and then, used a comprehension to convert that, to, to call a function on a whole bunch

00:19:32 of strings.

00:19:33 And I thought this was just kind of a clever way to just play with a function that translates

00:19:37 things.

00:19:38 This is a neat thing to do.

00:19:39 I would have probably so hard.

00:19:41 Yeah.

00:19:41 It's super hard, but, normally because it's so picky, right?

00:19:45 You've got to go to the date time parsing language, almost look up.

00:19:50 So if I put percent D, D, D, D, D, that might mean the year, but if it's capital D, it might

00:19:55 mean something different.

00:19:55 So you might say month, day, comma year, but like, there's an example here with month, day,

00:20:01 year without the comma is like March 12, 2010.

00:20:04 But if they forget the comma, it won't parse.

00:20:06 And like all those things are really annoying about working with reading, converting strings

00:20:10 to dates.

00:20:10 And this looks like it just, it doesn't care.

00:20:13 It's nice.

00:20:13 Yeah.

00:20:14 And then it also, it's kind of a clean, nice, clean air face to it as well.

00:20:18 the, and a limited documentation is just a focus tool, which is nice.

00:20:23 And it's interesting that this is just a focus tool that apparently a lot of people need

00:20:27 because according to GitHub, there's 662 projects using this.

00:20:31 So, it's used kind of all over the place.

00:20:34 The behind the scenes though, it's taking the, what the dates that it found to the strings

00:20:40 and passing those to date util.

00:20:41 So if you want to avoid the finding part, this actually is also a good library to look at for

00:20:47 the usage of how to use date util to easily convert, convert dates.

00:20:52 and date util is kind of an amazing tool as well.

00:20:56 and it gives you a, I told you this was a rabbit hole.

00:21:00 One of the cool things about it is you, it isn't just parse dates, but you can do relative

00:21:05 dates.

00:21:05 You can say like today plus three weeks or something, and it'll figure that out.

00:21:10 and then you can, or you can take two days, two dates and do, do date math with

00:21:16 it really well.

00:21:16 And also date util has an amazing time zone support, probably the best in Python.

00:21:21 So, this is pretty, pretty kind of cool.

00:21:24 also I think I was looking through the test code.

00:21:27 The test code for date util, has, is an, is kind of a neat mix of a unit test and pie

00:21:33 test.

00:21:34 Both of them are good examples of how to do both.

00:21:36 and I like some of the newer stuff is using pie test with parameterization, but it's

00:21:41 good.

00:21:42 Yeah.

00:21:42 I like this a lot.

00:21:43 Marlene, what do you think?

00:21:44 Yeah, I like it.

00:21:45 I think it, I'm not actually working with dates quite often.

00:21:48 So I'm, I'm trying to think of use cases for myself other than like maybe converting time

00:21:54 zones, which is like a nightmare.

00:21:56 so maybe, Oh, you can say that again.

00:22:00 Oh my gosh.

00:22:01 Maybe you said that, but it looks like it would be really useful for people that are, yeah.

00:22:07 Yeah.

00:22:07 Yeah.

00:22:10 I'm showing up some of the, some of the examples from date util of how to use it.

00:22:14 And it's based, I imagine this is one of the reasons why date finder is so used because,

00:22:20 this is non-trivial even to use date util.

00:22:23 So yeah, that's cool.

00:22:25 Cool.

00:22:26 Cool.

00:22:26 All right.

00:22:26 Well, I got the next one and this one doesn't exactly come to us from Anthony Shaw, but I was

00:22:31 talking to Anthony about something else and he's like, Oh, have you heard of this?

00:22:35 Have you heard of cinder?

00:22:37 And, cinder is pretty awesome.

00:22:39 So Anthony's doing interesting work around Python and performance at the CPython level,

00:22:45 especially now, I think he's given a talk on pigeon or piston, piston.

00:22:49 I believe it is.

00:22:50 I'm not a hundred percent sure.

00:22:51 I might be remembering which one's wrong at PyCon, which is, you know, we're going to talk

00:22:55 more about that in just a second as well.

00:22:57 But cinder is a really interesting fork of CPython from Instagram.

00:23:03 So it's under the Facebook incubator project.

00:23:06 And I think we've mentioned it before.

00:23:08 I definitely have talked about it before other presentations that Instagram has done really

00:23:12 interesting things like disable the garbage collector, just turn it off a hundred percent.

00:23:16 And they got less memory usage, not more memory usage by just allowing the cycles to leak, which

00:23:23 is insane.

00:23:23 But this is like, speaking of insane, this takes it to a whole nother level.

00:23:27 So this is that they've been doing all these low level things inside of CPython.

00:23:31 This is based on three, eight.

00:23:33 Hopefully some of these ideas can be brought forward and shared with everyone because there's

00:23:37 a lot going on.

00:23:38 So let me just cruise down here.

00:23:39 I'll just read the little intro part because it's jam packed.

00:23:44 And then I'll go into some of the details.

00:23:45 So this is the internal performance oriented production version of CPython 3.8.

00:23:50 And it contains a number of performance optimizations.

00:23:53 I feel like performance is some sort of theme of this episode.

00:23:56 It includes bytecode inline caching, eager evaluations of coroutines, a JIT, just in time compiler,

00:24:04 an experimental bytecode compiler that uses type annotations in some incredibly interesting

00:24:10 ways to enter, to emit type specialized bytecode that performs better.

00:24:14 So just to give you an example, one of the reasons that math in the pure Python layer is slower

00:24:22 than say C++ or C# is C++ and C# work with just the value.

00:24:27 So if you have the value seven, you might have two or four bytes that represent the value seven

00:24:32 in Python, you have a py object pointer, which is like 28 bytes pointing out to a thing on

00:24:38 the heap that represents the number seven.

00:24:40 And it's a whole lot more work to interact with that and set the reference count on that

00:24:45 and so on instead of just working with the value seven.

00:24:47 Right.

00:24:48 So one of the things they do is they actually have typed the, they use Python type annotations

00:24:54 to understand, oh, this is an integer.

00:24:56 This is a long and so on type of thing and actually convert those to the,

00:25:01 the machine oriented numbers.

00:25:03 Right.

00:25:03 So just the value four instead of a pointer.

00:25:05 And then it will use what's called boxing.

00:25:07 If something else that's outside of this world needs it, it'll up level that to like a py long

00:25:12 object pointer type thing and hand it off.

00:25:15 So there's, there's all sorts of stuff like that going on.

00:25:17 Interestingly, the first question is, is this supported?

00:25:20 No, not supported.

00:25:26 But there's some interesting things going on here.

00:25:28 And all of this has to be taken within, with an understanding that it's in a very specific

00:25:33 context and that may or may not be useful for you.

00:25:36 You know, Brian had pointed out some articles and ideas around that.

00:25:40 You're not Instagram.

00:25:41 You're not Facebook.

00:25:42 You're not Netflix.

00:25:44 And so on.

00:25:44 Most of the time people are building much smaller software with different constraints.

00:25:49 So they start out by saying, look, Instagram uses a multi-process web server architecture

00:25:54 where the parent process starts, performs initialization, and then forks 10 worker processes

00:26:00 to handle requests.

00:26:01 This is super common.

00:26:03 Like for example, Talk Python training literally does exactly this.

00:26:06 It, it uses micro-wisgi.

00:26:07 It starts up and it creates 10 worker processes to handle like people wanting to take courses.

00:26:11 So it's not uncommon in the web, but it's, it's not how all Python code runs.

00:26:15 And so the first optimization they did is they created what are called immortal instances.

00:26:21 The reason they were so focused on the garbage collector and all those sorts of things was

00:26:26 when you fork these processes, initially there's a bunch of memory that can be shared and that

00:26:32 helps with cache locality that helps with overall memory usage, all sorts of things.

00:26:37 But as soon as something has changed about one of those items, it has to copy a whole page

00:26:42 of memory.

00:26:42 And they realized that when an object's reference count is modified in one of the processes, it

00:26:49 has to copy a replicate and sort of fork off a bunch of the memory that used to be shared

00:26:55 across all those processes.

00:26:56 So they created what they call immortal instances that cannot be, that don't participate in reference

00:27:02 counting or garbage collection.

00:27:03 And that prohibits their reference count number to change so they can be shared.

00:27:07 So they can mark like a whole bunch of the startup stuff as like, just don't even look at this

00:27:12 or change it and don't do reference counting on it.

00:27:13 So in their world, they may, it got things faster, but it doesn't always, they said it's

00:27:17 something a little bit slower in straight line code, but in this sort of fork world, it's

00:27:22 better.

00:27:22 The next one is shadow byte code, which is an inline caching implementation.

00:27:28 And it goes through applies in certain optimization cases for generic Python op codes.

00:27:34 And it'll observe those for functions that take a lot of time and dynamically replace those

00:27:41 with specialized op codes that it thinks are going to be better.

00:27:44 Another thing it does that's pretty interesting is it will eagerly evaluate coroutine.

00:27:49 So if I say this is an async method, and then in that method, I call a weight, some function

00:27:54 call normal Python is going to create a coroutine.

00:27:58 It's going to schedule it on the asyncio event loop, and it's going to get to it.

00:28:01 And that's a lot of overhead.

00:28:02 But maybe that function says inside.

00:28:05 The first thing is if this case just return the cached answer, otherwise go to the database,

00:28:11 await the response and so on.

00:28:13 And what they realized is if it's going to go through that first case, it's not actually

00:28:17 awaiting something.

00:28:18 So they'll actually execute the awaited thing up until it actually needs to become async.

00:28:25 So it'll like look or effectively look inside the function and say, is the path we're going

00:28:29 on this time going to be async or not?

00:28:31 And if the answer is no, it will run it without async, which means it skips all that context switching

00:28:37 and all that stuff, which is pretty crazy.

00:28:38 It also has the cinder JIT, which is a method in time JIT compiler.

00:28:44 I think C#, Java, maybe even JavaScript V8.

00:28:48 So it's enabled for every function that is called.

00:28:52 Actually, it's not.

00:28:54 Sorry.

00:28:54 If it is, it'll make it slow.

00:28:55 So you can basically say which functions should be optimized.

00:28:59 But they say it supports almost everything that Python can do.

00:29:03 And it has a 1.5 to 4 times speed up of the Python benchmarks, which is pretty interesting.

00:29:09 They also have this thing called strict modules, which is actually a static analyzer capable of

00:29:15 validating top level code to see if a module has side effects and can treat it differently.

00:29:20 If it doesn't, you can have an immutable strict module type that is sort of a replacement for

00:29:27 Python's regular module that behaves and loads differently and so on.

00:29:32 And then the thing I talked about, the numbers more broadly is under this category of static

00:29:36 Python.

00:29:37 It's an experimental byte co-compiler that makes use of type annotations to emit better

00:29:43 things.

00:29:43 And check this out.

00:29:44 It can deliver performance similar to mypyC or Cython.

00:29:48 And this thing will go up to seven times faster than regular Python for the Richards benchmarks.

00:29:55 And I don't know if the 4x improvement before is like in addition to this.

00:29:59 So you get 28 or you just get seven.

00:30:01 I don't really know.

00:30:02 But there's a lot of things going on here and a lot of different ideas about how this

00:30:07 works.

00:30:07 So I'm just scratching the surface on the details, but I feel like I've gone on and on about it.

00:30:12 That's really interesting.

00:30:14 I saw, I think, is there a talk about it at Python?

00:30:17 At PyCon?

00:30:18 I think that's...

00:30:19 It is coming up.

00:30:20 Yes.

00:30:20 They're going to give a talk on this at PyCon.

00:30:22 Yeah.

00:30:22 It was one of the talks I was looking forward to listening to.

00:30:26 Yeah.

00:30:28 Just because I think it's super interesting to be able to kind of play around with that they

00:30:34 were able to kind of make their own version of Python.

00:30:37 And it might...

00:30:39 I don't know.

00:30:39 Like, I think that there's...

00:30:41 Like you mentioned, Anthony, and I also know Victor, I think, and someone else who are also

00:30:48 working on, like, sub-interpreters and different things to make Python faster.

00:30:52 So I'm really curious to see if, like, the core devs or people will also be, like, listening

00:30:58 to this talk and maybe take some ideas from it.

00:31:02 It would be really cool to kind of see.

00:31:05 And I mean, it's always good to get speed-ups, even if they...

00:31:09 I don't know.

00:31:09 I don't know if it will help, like, general, like, normal Python users, but I think it's

00:31:16 always good to look into.

00:31:17 Yeah.

00:31:19 Yeah.

00:31:19 Yeah.

00:31:19 I agree.

00:31:20 I think some things here are absolutely transferable to regular general-purpose CPython,

00:31:26 and some of them might not be.

00:31:27 For example, the immortal instances, that might be a thing that just...

00:31:32 They do that, and it makes sense for their large-scale farm of servers.

00:31:36 But the JIT that takes the type information and does math many, many times faster, that...

00:31:43 Everybody would want that.

00:31:44 Like, we all work with numbers at some level or another.

00:31:46 Right?

00:31:47 Well, one of the things I love about the...

00:31:50 I mean, this kind of applies to all of these sort of speed-up projects.

00:31:54 One of the things I love about Python is just the generalness of it.

00:31:57 You can throw it.

00:31:59 Data structures can hold anything.

00:32:00 So it's...

00:32:02 But there are times where you really are using a huge array of floats or a huge array of integers

00:32:09 or a huge array of, like, a fixed data size.

00:32:12 Those are times where you...

00:32:15 I don't need it to be generic.

00:32:17 I just need it...

00:32:18 I need it to be fast.

00:32:19 So having something...

00:32:21 That's the part where I think it would be interesting to pull into regular Python.

00:32:26 But don't we get that with, like, some of the data science stuff anyway?

00:32:30 Some of the number...

00:32:32 With, like, NumPy and stuff?

00:32:34 Yeah, you do.

00:32:35 But you can't do generic programming with it, right?

00:32:38 You do, like, sort of matrix math type of things.

00:32:41 And this one...

00:32:42 Like, the answer used to be, okay, well, this function is slow.

00:32:44 This serialization deserialization section might be slow.

00:32:48 So rewrite that in Cython, for example.

00:32:50 And what's really cool about this is you can write regular Python and just put type annotations on it.

00:32:57 And then it goes as fast as Cython.

00:32:59 And you don't even have to do, like, a separate compiler, I believe, in this world, right?

00:33:04 Because they have...

00:33:05 The JIT just knows that.

00:33:06 And then we'll...

00:33:07 Like, as you run it, it'll just compile and run it.

00:33:09 So, which is...

00:33:11 I think it just sort of makes some of those ideas closer and more automatic for most people.

00:33:16 I kind of think I foresee a future where we have sort of some types that affect runtime.

00:33:23 There's, like, this tension that I sense in the Python core people of whether or not types should be just an afterthought or whether they should be really part of the runtime.

00:33:35 And I think there are some cases where having them be part of the runtime might be a good thing.

00:33:42 Yeah, and this is interesting because what they do is they define these static modules.

00:33:48 And then in there, they can treat them differently.

00:33:51 I feel like I always see on Twitter some people kind of, like, ranting about how they don't like that direction that Python is going in.

00:33:59 Like, the idea of putting in, like, annotations and things like that.

00:34:03 I've seen some people that are not super big fans of that.

00:34:06 I'm not really sure why.

00:34:08 I generally would like to understand, like, I think most people...

00:34:12 Or not most people.

00:34:14 But I think some people would prefer Python to maybe remain as it is.

00:34:19 But I do think that there's, like, just having it be a bit lesser in a couple of cases would be helpful.

00:34:24 So, I don't know.

00:34:25 I don't know if it's in that direction.

00:34:28 I'm with you.

00:34:28 And one of the things they point out in this readme announcing the project is that you can still do gradual typing.

00:34:34 So, you can, in some places, have no types.

00:34:37 In some places, have some types.

00:34:39 And the thing can convert and just deal with that automatically.

00:34:42 And I think that's the reason that the types are really welcome in Python is because you can use them if you want, but you don't have to.

00:34:48 As opposed to places like TypeScript, which said, well, JavaScript doesn't have types, so we're going to add this very strict type system.

00:34:55 And if you don't fit it exactly, we're going to not compile and complain, and it's going to be really not good.

00:34:59 This feels like it continues that forgiving nature of Python to let you opt into it.

00:35:05 But if you do, it can go faster.

00:35:07 That's the direction I'd like to see.

00:35:09 I personally would like to see types be really a full-fledged feature of Python.

00:35:16 I agree.

00:35:17 I love that they're optional, but if they're there, let's see how much we can do and improve things with them, right?

00:35:23 A hundred percent.

00:35:24 Yeah.

00:35:25 All right.

00:35:26 Marlene, you got the last one.

00:35:27 I got it on screen for you.

00:35:28 Okay.

00:35:28 Yes.

00:35:29 The last one for today is PyCon US, which I'm very excited about.

00:35:34 It started today, which is really great.

00:35:39 Are both of you attending?

00:35:41 I don't know if you're attending.

00:35:42 Yes, absolutely.

00:35:45 Okay.

00:35:46 Brian, are you attending?

00:35:48 Yay.

00:35:48 Yeah.

00:35:50 I think it's such a great event in terms of the fact that I know it's PyCon US, but it is, at the moment, it's the largest Python.

00:35:58 Python gathering, or largest Python on Earth, I think, which is very cool because it means that you can meet people from all around the world.

00:36:08 I remember, I'm really sad that it's not in person because last year, not last year, but the year before that, that's where I actually met you, Michael, for the first time.

00:36:19 I think we were literally, I think we were at a table with you and Anthony Shaw and Łukasz Langa.

00:36:27 And I was just randomly there.

00:36:29 But it was such a cool discussion.

00:36:32 And I really love the idea of being able to be in a room with people that are contributing to Python.

00:36:40 That's my favorite part of PyCon.

00:36:43 Yeah.

00:36:44 It was so nice to meet you as well.

00:36:45 That is actually my favorite part of PyCon.

00:36:48 Yeah.

00:36:48 It's the just, you happen to end up at a table or out for a beer or coffee with this group of people.

00:36:54 And you're like, wow, I got these connections and this experience that just, I wouldn't.

00:36:59 So I'm very much looking forward to coming back in person.

00:37:01 But there's a bunch of great talks coming up.

00:37:04 Exactly.

00:37:04 So this year, although it's online, the online platform is very cool.

00:37:11 And there's still lots of great talks to watch.

00:37:13 In the show notes, I put down a list of the talks that I'm excited to watch.

00:37:17 But I also want to just put in a word for the things that I will be doing at PyCon US this year.

00:37:23 And the first thing I'm going to be doing is I'm going to be hosting the diversity and inclusion work group discussion,

00:37:29 along with four other really amazing women that are part of the diversity and inclusion work group.

00:37:36 I do want to comment here because I got like, we got some comments about it, some feedback.

00:37:43 I posted a picture of like a group that's going to be having this discussion or hosting this panel and it's all women.

00:37:49 And someone was just like, why is it all women?

00:37:52 How is this diversity?

00:37:53 So I do want to throw it out there.

00:37:57 I just want to throw it out there that we did try, like the work group itself has a lot of,

00:38:03 it has a good balance of men and women in it.

00:38:05 But then when I asked people if they want to come on the panel, it was only like women that volunteered.

00:38:11 So it's not my fault.

00:38:12 And I am aware of that.

00:38:14 That's just a general or that's just general feedback there.

00:38:18 But I think the panel will be really exciting.

00:38:24 It's going to be on Saturday on the main stage at 12 p.m.

00:38:28 EST, I think.

00:38:30 If you're going to be there, I really would encourage you to attend.

00:38:34 There's going to be questions and answers.

00:38:36 And I just think it's such an important thing.

00:38:38 I know that sometimes diversity can seem like a really tiring thing to talk about, especially like recently.

00:38:45 I feel like sometimes people use it as like this buzzword and it can, and people can be like, oh my gosh, and just turn off when they hear the word diversity.

00:38:54 But I really do think it's important.

00:38:56 And particularly now as Python is growing in popularity, I think a few years ago, it was okay for the nucleus of Python to be based in the United States or based in Europe.

00:39:10 But it's growing so quickly.

00:39:12 Python for I don't know how many years now has been the most popular language in the world.

00:39:18 And I know even for me, I'm in Zimbabwe right now, and it's one of the most popular languages here where I live.

00:39:25 And so just providing the group, like our main purpose is to figure out how we can support the PSF to try and serve Pythonistas from around the world better and to connect the community better and have better representation and different things like that.

00:39:42 So very excited about that one.

00:39:44 That's awesome.

00:39:46 And thanks for your work here.

00:39:47 I definitely agree that we're stronger together, right?

00:39:51 And one thing I would really like to see, and I think we're getting there, is when people look at Python and programming in general, but generally the Python space, we have influence over that.

00:40:00 When people look at that world, I would like them to say, I can see myself being part of that.

00:40:06 I can see that I could belong there, right?

00:40:08 And if that's not the case, then how do we make that the case?

00:40:11 Exactly.

00:40:12 Absolutely.

00:40:13 I think exactly that.

00:40:15 And I would love to see that happening in the next two years.

00:40:19 I would love to see, you know, one of my things is I'd love to see more like women core developers and more like global core developers as well.

00:40:27 And also people on the board and different things.

00:40:29 And those are all goals that we are working towards.

00:40:31 Obviously, we don't know, like, the perfect way to achieve something or the perfect way to do things.

00:40:37 But it's something that I think is really great and exciting to work on.

00:40:42 So please attend if you are listening to this.

00:40:46 And let me know if you, like, came from this podcast.

00:40:49 It would be fantastic to see you there.

00:40:51 Maybe just comment.

00:40:52 Yeah, fantastic.

00:40:53 And then, oh, another thing that I am doing for, like, on this year as well is I will be, one, I will be in the, so there's, like, a lounge area.

00:41:05 Well, there's, like, a PSF booth.

00:41:07 And if you would like to just, if you're going to be there in the morning on Saturday or on Friday, I will be hanging out in the PSF booth.

00:41:15 And so, yeah, if you just want to talk about Python or the PSF or anything, I will be there.

00:41:20 And I will also be hosting the EMEA meeting.

00:41:24 So if you're in Europe, the Middle East, or Africa, there's a members meeting on Saturday.

00:41:30 I think it's at 10 a.m. Central African time.

00:41:34 I'm not sure what time that is in other places.

00:41:36 But I know it's at 10 a.m.

00:41:38 It's on the schedule, right?

00:41:40 It's on the schedule.

00:41:40 Yeah.

00:41:40 We can use the daytime thing.

00:41:42 I don't know.

00:41:43 Exactly.

00:41:45 Pull up the ripple.

00:41:46 Throw it into daytime.

00:41:47 Exactly.

00:41:48 Please do that.

00:41:49 So I will be hosting that.

00:41:52 And that's going to be in the morning.

00:41:54 And if you would like, even if you're not a member, you can watch it on the PSF YouTube channel.

00:42:00 It's going to be streaming there.

00:42:01 Or you could join.

00:42:02 There's a meetup link that I put in the show notes.

00:42:04 So people could join that way as well.

00:42:06 So, yeah, Python is going to be really exciting.

00:42:09 And I'm really looking forward to it.

00:42:11 So just encouraging people to come along for sure.

00:42:14 Yeah, it should be fun.

00:42:15 And even though it is super sad that it's not in person, it's not in Pittsburgh this year.

00:42:21 I think in some ways it's more accessible to people around the world, right?

00:42:25 They don't have to travel there.

00:42:26 They can just log in and attend it.

00:42:29 And that's so much less expensive than I flew to the U.S.

00:42:32 And I paid $1,000 for a hotel.

00:42:34 So there's a little silver lining, you know, out there in the live stream.

00:42:38 Sam Morley really says, I really wish I could go to PyCon in person.

00:42:42 Adam Parkin there says, me too, maybe in 2020.

00:42:45 I think so.

00:42:46 Finally, Sam also thinks it's great that we're having this diversity conversation and paying attention to it.

00:42:53 One of the things I've noticed in 2020 is all the regional, actually last year also, though.

00:43:00 But the 2020 and 2021, we've got all these PyCons going on all over the world.

00:43:07 I used to think of like PyCon U.S. as the PyCon and everything else is regional.

00:43:13 Now I think of PyCon U.S. as a regional conference also.

00:43:17 It's the regional one that's close to the people that are in the U.S.

00:43:21 It isn't necessarily better.

00:43:23 It's, I love it.

00:43:26 It's great.

00:43:26 Anybody from that's hosting it, yes, it's better.

00:43:29 But no, I like all of them.

00:43:34 And I was excited to get to participate and watch videos from all over the world this year.

00:43:39 That was pretty neat.

00:43:41 But yeah, I'm on board with, I want to get back to regional stuff.

00:43:45 I'd like to see people in person.

00:43:47 I can't wait.

00:43:48 Yeah, I will say for sure, like, even if people are feeling adventurous, there is a regional conference.

00:43:56 I didn't mention it before that I am also part of the organizing team for, which is PyCon Africa.

00:44:01 So if you would like to travel to another PyCon in a different part of the world, when we are able to travel and the world gets back to,

00:44:11 some form of free travel, definitely recommend also hopping over to PyCon Africa.

00:44:19 I think, like you said, I think PyCon US is fantastic.

00:44:23 And one of the neat things about that is that it's a conference that has been there for so long.

00:44:29 So a lot of people are going to be there.

00:44:32 But there are 100% are a lot of great conferences like PyCon Africa, which you should attend if you can.

00:44:40 I think they're really just as exciting.

00:44:42 And there's so many cool things that you get to experience.

00:44:45 Like, I think for me, it's like whenever I go to the US, like last year, I'd never been to Ohio before.

00:44:51 And like, I had like, I would never like in my, I would never have a reason that I would think to myself, let me go to America to go to Ohio.

00:45:03 But I feel like it was such a good experience for me.

00:45:07 And I really liked it.

00:45:08 And I was really surprised by that.

00:45:10 And so I think it's the same way.

00:45:12 Like, PyCon is a great way as well to like experience new places.

00:45:16 So yeah, definitely sticking in that.

00:45:18 Well, that wraps up our six.

00:45:20 Anybody got any extra information to share?

00:45:24 Nothing else for me, other than the fact that if you do want to reach out to me, you can reach out to me on Twitter.

00:45:31 I'm Marlene underscore ZW there.

00:45:34 I'm also Marlene underscore ZW on GitHub, I think.

00:45:38 And on my website.

00:45:40 My website is MarleneMangami.com.

00:45:43 So if you would like to reach out to me here, feel free to.

00:45:46 I'm always happy to like chat about PyCon.

00:45:49 Nice.

00:45:50 Cool.

00:45:50 So I got a couple.

00:45:51 One made me really excited.

00:45:53 This tweet from GitHub.

00:45:55 Is your fork behind?

00:45:57 You can now sync your parent repo with just a single click.

00:46:01 So check this out.

00:46:02 If you go to your fork now, next to contribute for your PRs and stuff, there is now a fetch upstream button.

00:46:10 And all you have to do is click it and then automatically your fork will become in sync with whatever you forked it from.

00:46:16 You just have to go and go check it out.

00:46:19 Add an upstream origin and then pull from that and then merge that wherever you want it to go to.

00:46:24 Over here, you just click this button and boom.

00:46:27 It's good to go.

00:46:28 So I think this will just lower the bar for people forking something.

00:46:31 They want to get the current one and then make a change to see if they could contribute back.

00:46:35 Here's one fewer steps in that process.

00:46:37 Do you have any idea if it stays in sync or if you have to?

00:46:41 No, it's a one-time type of thing, I believe.

00:46:43 It says there's this many changes we'll pull over and it basically just automatically does the process at that time.

00:46:49 Nice.

00:46:49 But still pretty nice.

00:46:51 You know, Flask 2.0 is out.

00:46:53 And that one was sent in to us from Adam Parkin that, hey, heads up, this is now actually live.

00:47:01 So very, very cool.

00:47:03 Actually, everything from Palettes has been updated.

00:47:06 So, yeah.

00:47:07 I happen to have spoken, done a podcast recording with David Lord, who runs Palettes, and Phil Jones, who does Core and contributes back to Palettes as well, about all the stuff coming in Flask 2.0, all the exciting stuff and their future plans as well.

00:47:21 So, yeah.

00:47:23 You can watch the live stream of that or wait a day or two until the episode is out and just listen at Talk Python as well.

00:47:29 But, yeah, very, very cool.

00:47:30 Yeah.

00:47:30 And then Adam also at the live stream again says, this is super sweet.

00:47:33 Always find it a headache to sync with upstream.

00:47:35 Yeah, about the GitHub thing.

00:47:37 That's cool.

00:47:37 Cool.

00:47:38 Close it out with a joke.

00:47:39 Well, I got a couple of things I wanted to mention.

00:47:41 Go for it.

00:47:42 Sorry.

00:47:43 I had Brett Cannon on last week on testing code and huge feedback from everybody that it was a great episode.

00:47:51 We talked about packaging.

00:47:52 I'll have Ryan Howard on this week talking about Playwright.

00:47:56 So that'll be fun.

00:47:57 And I wanted to mention a thank you to the 71 patrons that we have on Patreon.

00:48:03 So thank you for supporting the show.

00:48:05 Thanks.

00:48:05 Yeah.

00:48:06 Thank you, everyone.

00:48:07 How about a joke?

00:48:08 Yes.

00:48:09 Sorry for almost skipping over your extras.

00:48:11 Here.

00:48:13 No worries.

00:48:14 You ready?

00:48:15 Yeah.

00:48:15 So this one, I talked about that crazy giant ship thing.

00:48:20 And we've got Marlene doing rapid.

00:48:22 So I thought maybe some kind of machine learning joke.

00:48:24 Here's a bunch of robots in school.

00:48:29 And they go like little Android looking things.

00:48:32 Small ones because they're students.

00:48:34 They're kids.

00:48:34 And they're in machine learning class.

00:48:37 And there's a big box of dirty data.

00:48:38 Like a bunch of bits that are like kind of gray.

00:48:42 And I don't know.

00:48:42 They just have dirt on them.

00:48:43 And the teacher says, Robbie, stop misbehaving.

00:48:47 Or I will send you back to data cleaning.

00:48:49 Yeah.

00:48:53 That's where they're spending half the day anyway.

00:48:56 Yeah.

00:48:56 They actually spend most of their time there.

00:48:58 That's right.

00:48:59 I don't know who is drawing them.

00:49:00 Like one of the robots is looking the wrong way.

00:49:03 I was like, why is it drawn like that?

00:49:04 I don't understand.

00:49:05 Hey, a more concrete, really quick closeout question I see in the live stream here is

00:49:12 Akmos.

00:49:13 Is there a difference between QDF and pandas in terms of utilization?

00:49:18 Like in terms of how you actually use them?

00:49:22 Well, I don't think so.

00:49:26 For the most part, if when you're using QDF, the way it's built is to mirror pandas.

00:49:32 So the APIs are really similar.

00:49:35 So ideally, the methods that you would use when you're using pandas are exactly the same

00:49:40 methods that you would use when you're using QDF.

00:49:43 The only difference is like when you're creating a pandas data frame, for example,

00:49:47 you would use PD dot data frame, for example.

00:49:50 But then with QDF, you would say QDF dot data frame.

00:49:54 If you make it like into a variable or something like that, then the methods that you're going

00:49:59 to pull are going to be totally identical.

00:50:01 It's really easy to try.

00:50:03 Yeah, that's it.

00:50:04 Yeah, that's awesome.

00:50:05 Yeah.

00:50:05 And Dask has similar stuff as well, right?

00:50:07 You create a Dask data frame instead of a pandas data frame, but the API looks quite similar.

00:50:11 They're not always 100% compatible, but most of the mainstream things, right?

00:50:16 Definitely.

00:50:17 So yeah, it's built definitely to make it as easy as possible to switch between the two.

00:50:23 So it's very similar.

00:50:24 Yeah.

00:50:24 Thanks a lot, everybody, for showing up.

00:50:26 Yeah.

00:50:27 Thanks.

00:50:27 Thanks, Maya.

00:50:28 Thank you, Marlene.

00:50:29 It's really great to have you here.

00:50:30 No problem.

00:50:31 Thanks for having me.

00:50:33 Thank you for listening to Python Bytes.

00:50:34 Follow the show on Twitter via at Python Bytes.

00:50:37 That's Python Bytes as in B-Y-T-E-S.

00:50:40 And get the full show notes at pythonbytes.fm.

00:50:43 If you have a news item you want featured, just visit pythonbytes.fm and send it our way.

00:50:47 We're always on the lookout for sharing something cool.

00:50:50 On behalf of myself and Brian Okken, this is Michael Kennedy.

00:50:53 Thank you for listening and sharing this podcast with your friends and colleagues.

