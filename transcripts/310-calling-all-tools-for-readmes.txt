00:00:00 Hello and welcome to Python Bytes, where we deliver Python news and headlines directly to your earbuds.

00:00:04 This is episode 310, recorded November 15th, 2022. I'm Michael Kennedy.

00:00:10 And I am Brian Okken.

00:00:12 And I'm Adam Hopkins.

00:00:13 Welcome, Adam. Great to have you here.

00:00:14 Awesome. Thank you. I'm excited to be here.

00:00:17 Yeah, people mostly know you, I would imagine, through Sanic, your web framework.

00:00:21 Tell people about yourself.

00:00:22 Yeah, that's correct. Well, first, I just noticed episode 310.

00:00:27 So, two more episodes and you guys pass the Python version.

00:00:30 So, congrats.

00:00:31 Thank you.

00:00:33 That's a milestone.

00:00:34 Six years. We just passed six years.

00:00:37 Yeah, that's exciting. I remember when you guys started it.

00:00:41 So, this is a great resource for the community.

00:00:43 Cool. Thanks.

00:00:44 So, just to introduce myself, I'm Adam Hopkins.

00:00:47 I am one of the developers of the Sanic project.

00:00:51 My day-to-day job, I'm a director of software engineering for Packet Fabric.

00:00:56 Where we, you know, day in, day out, I do web development.

00:01:01 So, that's my gig.

00:01:02 Fun stuff, it sounds like.

00:01:04 Yeah, absolutely.

00:01:05 Cool.

00:01:06 Yeah. Well, Brian, you want to kick us off with our first topic here?

00:01:10 Yeah, sure.

00:01:11 So, this is a little bit of an easy topic.

00:01:14 Tips for clean code in Python.

00:01:16 This is from Bob Bilderbos from PyBytes.

00:01:20 I was playing with this dark mode on and off.

00:01:23 It's kind of fun.

00:01:24 Anyway.

00:01:24 Dark mode is always appreciated in my book.

00:01:29 Yes.

00:01:29 Well, so, this resonated with me.

00:01:34 So, I'm going to blast through the tips really pretty quickly.

00:01:36 They're just good things to think about.

00:01:38 I think it's good occasionally to remind yourself of when you're organizing your code.

00:01:43 So, using smaller units.

00:01:44 I'm going to come back to this.

00:01:46 But essentially, it's thinking about if you've got huge functions that do a whole bunch of stuff, maybe breaking it up.

00:01:52 Like I said, I'm going to come back to that a little bit.

00:01:54 Magic numbers.

00:01:55 Always good constants are better than just numbers sitting in your file somewhere.

00:02:02 You know, I'm kind of on the fence on the void.

00:02:04 Avoid global scopes the third.

00:02:06 But there's nothing really global in Python.

00:02:08 It's module level.

00:02:09 But still, if you've got large files, global scope can still be confusing.

00:02:14 So, watch that.

00:02:15 Using linters and narrowing is a good thing.

00:02:20 Actually, I'm not going to run all through all the tips.

00:02:23 There's some good tips here.

00:02:24 So, go ahead and read the article.

00:02:27 But the thing I wanted to come back to is just this one, this first one, smaller units.

00:02:32 Because I just ran into this.

00:02:34 So, I'm working on refactoring the pytest-check plugin.

00:02:38 And currently, it's just all in one.

00:02:42 I mean, most of the code was in two files, like the basic plugin hookup.

00:02:47 And then all of the rest of the code.

00:02:49 And people have added a couple other people have added features.

00:02:53 And that's a good thing.

00:02:54 But I have had a hard time keeping my head around all the code in there.

00:03:00 And it was confusing myself.

00:03:02 So, I've been working on splitting it up.

00:03:05 So, I split up all the code into.

00:03:07 And I split it up into this notion of the single responsibility principle.

00:03:12 I thought about this plugin as the features.

00:03:15 And it's either large features that kind of take up their own.

00:03:19 They're enough to be their own module.

00:03:21 Or some related features that are kind of all together.

00:03:24 And I've split up the code into different modules about those sorts of pieces.

00:03:29 And the nice thing about that is I've also done that with the tests.

00:03:33 So, I've split the test up into focusing on a feature at a time.

00:03:36 So, the tests are in multiple tests.

00:03:38 So, it's a lot more files now.

00:03:39 But each little piece is just a few windows full of code.

00:03:45 So, it's pretty easy to get your head around.

00:03:47 Oh, for this feature, all of these things work together.

00:03:50 And it's really been great to work with now.

00:03:54 So, I haven't published the final yet.

00:03:57 But the smaller units thing, people do talk about large functions.

00:04:00 And that's something to watch out for.

00:04:02 But large files are a thing to keep in mind, too.

00:04:05 And sometimes breaking it up.

00:04:08 You can go too far, too.

00:04:09 If you've got like 100 different modules that all are like 10 lines long.

00:04:13 That's too far.

00:04:14 But, you know.

00:04:16 Yeah, I really like the idea of smaller units in both files.

00:04:19 And for like functions or classes or whatever.

00:04:22 And one of the ways that I think about it is if I'm looking at a chunk of code.

00:04:26 Maybe like an inner part of a loop or some other thing.

00:04:29 I'm like, oh, I should probably put a comment to describe what that does.

00:04:32 Alternatively, I could make it a small function and give it a name that tells you what it does.

00:04:37 Like if it's update last login for user.

00:04:41 That could be a comment or that you could highlight those five lines of code.

00:04:44 Extract method and give it that name.

00:04:45 Right.

00:04:46 Like it just.

00:04:47 There's sort of a natural.

00:04:48 If I'm looking at it and I don't understand it.

00:04:51 How can I.

00:04:52 How can I make it easier to understand?

00:04:54 Like that's a really productive way to do it, I think.

00:04:56 Yeah.

00:04:56 Especially if that bit of code really isn't the focus of the function.

00:05:00 It's just some other stuff that has to be done.

00:05:02 Moving it out of the function proper is good.

00:05:06 And then the function name.

00:05:07 Yeah.

00:05:08 Just name it something clever.

00:05:10 I think one of the things you also really kind of hit on there is breaking up the test files too.

00:05:14 Right.

00:05:15 And so I'm kind of curious to hear like, you know, typically, you know, for maybe for a smaller package.

00:05:20 I mean, do you try to keep sort of one test file for one module and keep a module?

00:05:25 Or, you know, sometimes I feel like when I've done that, even trying to iterate in all the different things that I might want to test in one file, it could still end up being, you know, a couple thousand lines long.

00:05:37 I'm focusing on features.

00:05:39 So I'm trying to keep the like, for instance, the one of the functionalities for pytest-check is stop on fail working correctly.

00:05:49 Because you possibly could have multiple failures in a single test.

00:05:54 So how does stop on fail work?

00:05:55 Well, there's a defined way we've defined it for the plugin.

00:05:59 And so I've got like one test file that tests the stop on fail functionality.

00:06:06 So I prefer breaking it up into user functionality instead of modules, internal modules.

00:06:13 But yeah.

00:06:13 Right on.

00:06:14 Oh, good tips, Bob.

00:06:16 And nice find, Brian.

00:06:17 One thing also, I noticed that it was in this article that I'm probably going to touch on in a little bit.

00:06:22 Sort of that idea of the global scope.

00:06:24 Because that's definitely something that I think can actually cause some problems down the road.

00:06:31 And I'll touch on that in a little bit.

00:06:33 Awesome.

00:06:34 Yeah, absolutely.

00:06:35 There's also a lot of tips in here that can be automated.

00:06:38 You should write code that matches this kind of stuff already.

00:06:42 But running the linters, running black.

00:06:45 Pre-commit.

00:06:46 Yeah, pre-commit.

00:06:48 One of them is using idiomatic code, which you could use Flint.

00:06:51 We talked about a bunch of things that like upgrade to Python 2 to 3.

00:06:56 What was that?

00:06:57 Py upgrade, I think.

00:06:58 Yeah.

00:06:58 Whatever you.

00:06:59 Yeah.

00:06:59 Those types of things.

00:07:00 A lot of this stuff could be brought in on the toolchain level too, which is kind of nice.

00:07:05 All right.

00:07:06 Let's talk about Mastodon.

00:07:09 So I don't know if you all have heard Twitter's kind of going nuts right now.

00:07:12 It seemed like a place that was just going to be around forever.

00:07:15 But apparently, maybe no.

00:07:17 And so, Brian, I think you maybe encouraged me to go over to Mastodon and check it out a little bit last time.

00:07:24 And this was just like a week ago, man.

00:07:26 You've like just went crazy.

00:07:27 I have gone crazy.

00:07:28 I'm telling you.

00:07:29 But I think there's a lot of cool stuff over here.

00:07:31 So I'm super psyched about it.

00:07:33 I just did a Talk Python episode, but I'll pull up a link to that in a moment.

00:07:38 But what I found, so you kind of encouraged me to go over there.

00:07:42 And I did.

00:07:43 And what I found was there's a whole bunch of the people that we know and have been interacting with over on Twitter.

00:07:48 Now they're all over on Mastodon.

00:07:50 And it's a super nice, active community.

00:07:52 I expected to kind of show up there and go like, well, I'll wait till people show up.

00:07:56 But they're there.

00:07:57 They're there.

00:07:57 They're already there.

00:07:58 They're already there.

00:07:59 And like, Adam, I saw that you're over there.

00:08:01 And Brian, obviously you are.

00:08:02 And I got the shows going over there.

00:08:04 And so people can follow Python Bytes on Mastodon.

00:08:07 They can follow Python.

00:08:09 I'll put a link to all of the various, all of our profiles, including Adam's over there in the show notes.

00:08:15 And we're all kind of learning at the same time.

00:08:17 So even the, you show up and they've already got hundreds of friends there.

00:08:21 But they're like, they're still learning also.

00:08:23 So, yeah.

00:08:24 Yeah.

00:08:25 Yeah, absolutely.

00:08:26 They are.

00:08:26 So, Marco.

00:08:28 Yeah, go ahead.

00:08:29 Go ahead.

00:08:29 Go ahead, Adam.

00:08:29 I was going to say, it does sort of kind of bring up an interesting question that I've sort of been, you know, feeling is, you know, are people starting to share in two different places now?

00:08:40 You know, trying to have conversations in multiple places.

00:08:42 And so there is a little bit of an awkward.

00:08:43 And maybe, you know, we'll kind of just, you know, trudge through it and see how it works.

00:08:48 But I definitely agree that it's, it feels very, it feels clean.

00:08:52 Like it just feels like very, you know, fresh.

00:08:56 Maybe it's just because it's a, you know, a new app to play with or one.

00:08:59 I don't know.

00:08:59 But there's, I agree.

00:09:01 It's, I'm very happy to see that, you know, people that I'm already, you know, subscribed to and trying to see what they have to say are already there.

00:09:08 And you're definitely interested to see how this develops because I think it's, you know, it can only be positive.

00:09:14 Yeah, I totally agree.

00:09:17 My philosophy is kind of for the moment to be Mastodon first, not to burn down my Twitter account or to leave my community over there.

00:09:24 But just like, all right, Twitter looks like it's trying to kill itself.

00:09:26 Let me try to put some energy over here.

00:09:28 And after Brian kind of got me moving, looking at Mastodon, it lines up way better with the ideology of open source and Python communities.

00:09:38 Having this federated different bunch of servers, people can control them.

00:09:42 They're open source.

00:09:43 There's not one central choke point for it or whatever.

00:09:46 But yeah, I think, I think it's, it's really interesting and I encourage people to check it out.

00:09:50 I was going to highlight that Marco out in the audience said, me two weeks ago, is Mastodon good enough to replace Twitter?

00:09:56 Me now.

00:09:57 Is Twitter good enough to replace it for Mastodon?

00:10:00 Yeah, I'm, I'm kind of the same way.

00:10:03 All right.

00:10:03 So I got a bunch of stuff I want to share real quick with you.

00:10:05 So I'll go through it quickly.

00:10:07 That is not a, got to go in the right order.

00:10:09 So I did a really cool episode with Gina Houska, Juan Luis, Simon Willison.

00:10:15 And oh, I got to update my show notes because she dropped in last minute.

00:10:19 Carol Willing as well.

00:10:20 So people can check that out.

00:10:22 These different places, you should really support them.

00:10:25 These little instances.

00:10:26 Like, for example, the one that Brian and I are on is Fosstodon, the free and open source software instance.

00:10:33 It went from 2000 to 40 something thousand users in a week.

00:10:37 And their hosting costs went from a hundred to a thousand dollars in the same period, which is a lot.

00:10:43 And it's just volunteer, right?

00:10:44 That's a lot to be paying.

00:10:45 But they have a Patreon, which is really nice.

00:10:47 You go to their Patreon and you can sponsor them.

00:10:49 You can also do that for Mastodon.

00:10:51 If you look at, they have a sort of a statement breakdown of like, here's how much we spend on hosting.

00:10:56 How much we spend on CDN and Bitward and all these different things and how it breaks down.

00:11:00 It turns out, Brian, 2.5 cents per user will fund Mastodon.

00:11:05 So I feel like, I feel like we should be doing this.

00:11:08 Like we can all spare 2.5 cents or maybe a dollar.

00:11:11 Not everybody.

00:11:12 And if you can't really, please don't.

00:11:14 But most people who are software developers can surely do that.

00:11:17 Put another way, out of those 40,000 people, if just 100 of them pay $10 a month, that will also fund Mastodon.

00:11:25 So it's very achievable that we could end up in a world that is not ad-ridden, tracker-ridden, surveillance capitalism that's trying to trick us or manipulate us into do things.

00:11:35 But these really nice open places that we can move around as our values match.

00:11:41 I think the other side of it, too, is we need to make sure that the people who are the content creators, people that have large followers and are putting out information that people want to read, make sure that they're supporting this as well.

00:11:55 Because where the content is, that's where the people will go.

00:11:58 Yeah.

00:11:58 So hopefully, hopefully we can get more people paying for it and supporting it.

00:12:02 Yeah.

00:12:03 I'm doing it myself and I definitely encourage people who can because it's fantastic.

00:12:07 All right.

00:12:08 What else did I want to cover about this?

00:12:10 It's open source.

00:12:11 It's Ruby, which is not the most amazing open source for Python people, but it is open source, which is very cool.

00:12:16 You can go get it.

00:12:17 There's a Python package called Toot.

00:12:20 There's also a CLI.

00:12:21 You cover it.

00:12:21 We covered this a little bit last time, Brian.

00:12:23 I said I'd go into it more, right?

00:12:24 I think.

00:12:25 Yeah.

00:12:25 So one of the things I did, come back to that.

00:12:29 One of the things I did on, one thing that's annoying is if you're logged in, it's really hard to pull up an individual tweet on your own instance without it being in the show here.

00:12:38 But one of the things I did Saturday morning, Brian, do you see the third button from the second row of my stream deck here?

00:12:44 Okay.

00:12:45 So I wrote and I integrated the Mastodon API into my stream deck.

00:12:50 So now whenever we start a show, I just push that button and off it goes.

00:12:54 Nice.

00:12:55 I think actually I might have pushed the one for Talk Python this time because they're the same screen, just slightly different.

00:13:00 But anyway, we can push that button and it'll kick it off and that'll just post a toot, I guess we would say.

00:13:07 I still can't get over that.

00:13:09 It's just funny.

00:13:10 It's a little much, isn't it?

00:13:12 All right.

00:13:13 And then finally, one thing that's really nice is if you have a Chrome-based browser like Vivaldi or one of those or Brave, you can right-click on the tab and say install.

00:13:25 Mine says install Fosstodon because I was on Fosstodon.

00:13:28 But if you were on, you know, Mastodon social or whatever it's called, it would say install that.

00:13:32 And then you get a progressive web app that is, I would say, probably the best app on the desktop for doing Mastodon.

00:13:39 Ooh, neat.

00:13:39 Got hotkeys, all sorts of fun stuff.

00:13:42 Lots of, you can do like the advanced view with_columns and all of these things.

00:13:45 So I encourage that out.

00:13:47 Yeah.

00:13:47 So I encourage people to check this out.

00:13:49 One more thing on toot.

00:13:50 We'll come back to close Vember in a little bit.

00:13:53 Maybe this is relevant here.

00:13:54 But this is a library, Python package that you can use to talk to Mastodon.

00:14:00 I have no idea how to use it.

00:14:01 It's completely opaque.

00:14:02 It's like star, star, star, star, star, kwr, callable.

00:14:07 Or so I mean, you just, there's, it doesn't have any structure.

00:14:10 It's all like run, done up at runtime.

00:14:13 You can't tell like what are the functions.

00:14:15 Even if you do it, like it doesn't have any functions or anything you can call.

00:14:18 So how it's used, I have no idea.

00:14:20 It's hard to use, but the one thing you can do is it has a CLI that will generate your

00:14:25 OAuth login tokens.

00:14:27 And then you just use that directly with requests or HTTPX or something.

00:14:30 So to, as far as I can tell, it's not particularly useful until some sort of example is written.

00:14:35 Even the tests don't seem to help very much.

00:14:37 But what it does do is it'll generate your access tokens that you can use in the rest of

00:14:41 your code, which is pretty cool.

00:14:42 Okay.

00:14:43 Yeah.

00:14:43 Nice.

00:14:44 All right.

00:14:44 Yeah.

00:14:45 Well, people definitely should check that out.

00:14:47 Adam, you're up next.

00:14:48 All right.

00:14:49 So I guess, you know, a little bit of a backstory to, you know, a couple episodes ago, you were

00:14:55 talking about an article that I posted on my blog about this new feature that we invited

00:15:01 and brought into Sanic about a month ago.

00:15:04 And I, well, I was on Twitter at the time, but I sent a tweet to you kind of with a little

00:15:09 bit of a correction.

00:15:10 And so I guess that's kind of why I'm here is I just wanted to kind of clear up a little

00:15:15 bit.

00:15:16 The feature that we added into Sanic is this worker manager.

00:15:20 And the idea covered in the blog article is sort of what an implementation of that might

00:15:26 look like.

00:15:27 So really kind of what the article was trying to cover was how to build a Celery-like clone.

00:15:35 Can we take a step back really quick and just have you give the elevator pitch for Sanic just

00:15:40 for people who maybe haven't used it?

00:15:42 Sure.

00:15:42 So Sanic is, it's an async framework, web framework for building web applications.

00:15:50 One of the things that it comes with is a built-in web server as well.

00:15:56 So it's both a web server and a framework.

00:16:00 So it does both parts.

00:16:01 So you don't need a micro-wiz gear or G-in-a-corn or something along those lines?

00:16:05 Correct.

00:16:06 You can use something like uvicorn if you wanted to.

00:16:08 So it can operate as an ASG I-app.

00:16:11 So that is a possibility.

00:16:13 But generally, I find that most people that use Sanic will use the integrated Sanic server

00:16:20 because it's sort of built for high performance.

00:16:26 It's optimized to work with the framework.

00:16:29 The framework itself is generally very unopinionated and sort of tries to get out of your way and

00:16:37 provide you with the tools that you need to build an application, but not dictate specific

00:16:41 patterns.

00:16:42 So that's the short and long pitch of it.

00:16:47 Last year, I put together a book on sort of different patterns and how you might build

00:16:52 production applications in it with Sanic and sort of what are some of the possibilities

00:17:00 that are sort of outside the scope of just these documents here.

00:17:03 So specifically, one of the things that we kind of had noticed and really drove us to what

00:17:10 ultimately became the worker manager feature is that, you know, Sanic comes out of the box with,

00:17:18 you know, auto reload, the ability to scale up multiple workers, all that kind of stuff that

00:17:23 you would sort of expect.

00:17:24 But you might in older versions, you might have a different experience when you're doing development

00:17:32 versus when you're in production mode.

00:17:34 And so we wanted to kind of get rid of that so that every single time that you boot up Sanic,

00:17:41 whether you're in, whether you're a local host or you're deploying it, you get the same experience.

00:17:48 You've got one process whose whole job is to sort of manage the whole show.

00:17:53 And then one or more of these worker processes that can be individual servers.

00:17:58 And the idea, once we have that, it really provides us the ability to take that abstraction

00:18:06 and turn it into something a little bit more and allow individuals to inject arbitrary processes

00:18:12 into it.

00:18:13 So the example in the article was this cellular-like worker manager.

00:18:17 But, you know, one of the other big use cases that we see a lot with Sanic are people that are

00:18:22 trying to build chatbots, you know, maybe something for Discord or something like that.

00:18:27 So this would really make it very simple for you to run both a web application and a chatbot

00:18:34 all from one process and have it all managed without having to scale multiple instances.

00:18:42 Nice.

00:18:42 Yeah.

00:18:43 Yeah.

00:18:43 So does it, when you run these worker processes, can it run in, does it run in a background thread?

00:18:48 Or one of the things when I first talked about this that was a little unclear to me is, you know,

00:18:53 once you have, when you go into production, you farm out to a bunch of worker processes

00:18:58 typically, right?

00:18:59 You know, you say like, we're going to run four worker processes and they're all going to,

00:19:02 you know, round robin handle these requests.

00:19:05 But how does that management correlate back to these worker processes?

00:19:10 Because if they all are kind of managing their own, then you're going to end up with, you know,

00:19:15 a whole bunch of them.

00:19:16 Correct.

00:19:17 So when you start up the application, and this actually is the whole reason, you know,

00:19:21 going back to Brian's thing from earlier about, you know, trying to keep things out of the global scope.

00:19:26 And why I encourage people to do that is, is under the hood, you know, we're using the multi-processing

00:19:34 from the standard library.

00:19:36 So, you know, it's, it's, it's very easy to make some mistakes.

00:19:42 And, and if you've got some code that is kind of sitting in the global scope, you might accidentally run it

00:19:47 on all these different worker processes that you don't necessarily want it to.

00:19:50 So trying to keep your abstractions nice and tight and keeping everything's instead of functions and callables

00:19:55 kind of avoids that.

00:19:56 So to answer sort of your, your, your question is when you start up a, a worker process, you know, it's,

00:20:02 there, there's two kinds, right?

00:20:04 There's the processes that are meant for, for static servers, and then for anything else that you might want.

00:20:10 The reloader is going to be one.

00:20:12 We also have in the extensions, we also provide out of the box, a, inspect utility.

00:20:20 So it basically would give you a CLI, command line utility that you can sort of check

00:20:27 the status of any operating workers.

00:20:30 So you can see, you know, how many things are running.

00:20:32 That's cool.

00:20:32 if you wanted to sort of see, you know, how many requests are on each of the workers,

00:20:36 you could kind of, you know, get that information.

00:20:38 That's so hard to tell in production.

00:20:40 You're like, it's kind of slow and this one seems stuck, but I don't know what the heck's going on.

00:20:44 Absolutely.

00:20:45 And this is really sort of the thing that this has opened up because what happens, and for anyone that's ever done anything that's using multiple processes in Python, one of the things that, that the package does provide you is these, different primitives where you can short share state between them.

00:21:07 and in older versions of, of, of Sanic, there was no way that you could do that.

00:21:13 but one of the things that we now have is you could have say, one queue object and every single one of your workers is able to push and pull information from that queue.

00:21:22 you know, you can have, you know, shared counters and, and, it really kind of gives you a lot more flexibility that just didn't exist before.

00:21:30 Cool.

00:21:31 Well, it looks fantastic.

00:21:32 And the other thing that you, put in here is cashews.

00:21:35 What, how, what's the, how's cashews related back to this?

00:21:38 It's not related back to this at all.

00:21:40 This is just something.

00:21:41 This is your second topic, right?

00:21:42 Yeah.

00:21:42 Yeah.

00:21:43 Okay.

00:21:43 Sorry.

00:21:43 I put it in the wrong order then.

00:21:44 We'll, we'll come back to that one then.

00:21:45 Sorry.

00:21:46 Okay.

00:21:47 Awesome.

00:21:47 All right.

00:21:48 Well, this is really cool and it's, it's something that a lot of web frameworks don't have is this ability to richly manage stuff that shouldn't be processed during a web request.

00:21:57 And a lot of times people end up running whole different servers, you know, Redis plus celery or something fairly complicated.

00:22:03 So this is really cool that it's kind of like tightly tied together there.

00:22:06 So one actually kind of use case, that, that just, just kind of give people a little bit of understanding of how you might actually use this in production.

00:22:14 so, so, I use celery very heavily, as well as Sanec.

00:22:20 one of the things that anyone that's used celery knows about, is there's this, function, this service called celery beat.

00:22:28 And basically the idea there is you're, you're sort of scheduling these crown like jobs that are going to run periodically over some defined schedule.

00:22:36 Well, when you put all these things into, you know, Kubernetes applications, you know, containers, your DevOps guys come knocking on your door and say, how do I know that this thing is still running?

00:22:47 Like, I want to be able to ping this and make sure that things haven't died.

00:22:50 and so that, like Kubernetes, that's sort of the, one of the things that it does for you, right?

00:22:54 Is it, is it kind of checks the health of your applications and kind of restarts things.

00:22:58 And it's very simple to do from a web application, not so easy to do from a service like celery beat.

00:23:03 so what we did is, we built celery beat into a Sanec worker process like this.

00:23:12 So basically what it does is it's kicking off these jobs every, I don't know, say every 10 seconds, some, some period.

00:23:18 And it's sending a ping, HTTP ping over to the, to the Sanec service that's running it.

00:23:26 And then we can keep the state there.

00:23:27 And then it's super simple for Kubernetes at that point to sort of see what's the health of this application.

00:23:32 And is it still running?

00:23:33 Yeah.

00:23:34 Very cool.

00:23:34 That's, that's a really interesting news.

00:23:36 Awesome.

00:23:36 All right, Brian, can we talk about our sponsor this week?

00:23:39 Yeah, let's.

00:23:40 Awesome.

00:23:41 All right.

00:23:41 Well, this week, once again, we have back Microsoft and such great supporters of the show.

00:23:48 And if you've not yet checked out Microsoft for startups, founders hub, you definitely should.

00:23:53 As we all know, starting a business is hard.

00:23:55 They provide a bunch of support, both in financial grants for compute and other cloud services,

00:24:03 as well as access to a mentorship network and other types of advice, basically, and connections.

00:24:10 So it's a free service.

00:24:13 All you have to do is apply.

00:24:14 You don't have to be third party validated.

00:24:16 You don't have to be VC backed.

00:24:18 You just apply.

00:24:19 And then once you're in, you're in.

00:24:20 And unlike the requirement to go live in San Francisco, Silicon Valley, New York City, one

00:24:27 of these places where there's a community of founders and mentors and experts, you get access

00:24:33 to a similar network from wherever you are.

00:24:36 So it's not about who you know, but or who you have access to because you can use their network.

00:24:40 So they give you access to hundreds of mentors across a range of disciplines like idea validation,

00:24:46 fundraising, management and coaching, sales and marketing, and a whole bunch of specific technical stress points.

00:24:52 And you'll be able to book a one on one meeting with these mentors, many of whom are former founders themselves.

00:24:57 And it'll really give you a leg up making connections and keeping your your company on the right track.

00:25:02 In addition to that, you get a bunch of Microsoft cloud credits, a bunch of GitHub credits.

00:25:07 They partnered with OpenAI, a global leader in AI research and development to provide exclusive benefits there as well.

00:25:14 To make your idea a reality with the critical support you'll get from Microsoft for startups, join.

00:25:18 To join, just visit pythonbytes.fm/founders hub 2022.

00:25:22 The link is in your show notes.

00:25:24 So as always, thanks to Microsoft for supporting the show.

00:25:28 Yes, thanks.

00:25:29 Hi, Brian.

00:25:30 What's next?

00:25:31 Well, I wanted to touch on FastAPI a little bit.

00:25:33 And specifically, there was a new release that caught my attention.

00:25:39 So the 0.87.0, we should bug them about being zero-verse still.

00:25:48 But so, yeah, come on.

00:25:51 It's definitely production ready by now.

00:25:53 So anyway, well, so what I wanted to talk about is some of the interesting bits here,

00:26:00 which I thought was really kind of cool of Sebastian and others to handle.

00:26:05 So one of the things is they upgraded to Starlet, and I think it's Starlette 0.2 or something.

00:26:12 Anyway, I'm not sure which version of Starlet.

00:26:14 But the Starlette version they changed to had a test client update and updated from requests to HTTPX.

00:26:24 And that's pretty interesting.

00:26:25 So FastAPI gets that also.

00:26:28 But what happens with that is the test client actually had some breaking changes with it.

00:26:34 And somebody named Cluedex just decided to create a tool called Bump Test Client.

00:26:43 And this is pretty cool because the idea is you've got some test code already that depends on test client.

00:26:51 And you can run this Bump Test Client on your test code, and it upgrades it to the new interface.

00:26:58 Cool as that.

00:26:59 That's just pretty cool.

00:27:00 That is cool.

00:27:00 Yeah.

00:27:01 Nice extra bit of upgrade help for people.

00:27:04 The other thing I wanted to point out is that there's a lot of documentation changes.

00:27:10 So one of the things he added was a help maintain FastAPI.

00:27:16 I say he, but I think there's a lot of people working on FastAPI now.

00:27:19 So I'm not sure who added it, but help maintain.

00:27:21 And I think this is really pretty great because let's see if I can find it.

00:27:27 Yeah.

00:27:27 It's focusing on like this section of help maintain it focuses on a couple of things that people don't think is very glamorous, but is hugely helpful for open source projects.

00:27:38 And that's helping with the issues because a lot of issues are really just questions or a user doesn't understand how to use it or they're using it in a weird way.

00:27:47 And it's just a knowledge gap thing.

00:27:49 So helping those people out.

00:27:51 Great help for the maintainers so they can focus on building new features.

00:27:54 Also kind of helps to point out maybe that there's documentation holes.

00:27:58 The other bit is a poll reviewing pull requests.

00:28:02 And both of the both of these topics have pop into bigger sections.

00:28:08 So like the helping with GitHub issues talk about how to do that.

00:28:12 So there's some documentation on how to help, like understand the question that somebody is asking and maybe maybe change the question if it's not clear.

00:28:19 Trying to reproduce other people's problems, suggesting solutions.

00:28:24 You know, if you think that it's been solved by somebody, if it's solved, but it's still open, ask if you can close it.

00:28:32 These sorts of this sort of help, especially with large projects, helps a ton.

00:28:37 And so I think it's cool that this has been focused on.

00:28:40 The other thing I wanted to point out, which I thought was cool, was we covered Ruff earlier on one of the other episodes.

00:28:48 And it's a Rust-based linter, but FastAPI is now using it.

00:28:54 Internally to lend to their FastAPI code.

00:28:57 So that's kind of fun.

00:28:58 Yeah, that's fun.

00:28:59 Now, one of the reasons why I was looking at this is coming back to the little project pytestCheck that I'm working on.

00:29:07 I'm refactoring it.

00:29:08 I also thought the readme is lame.

00:29:11 So I was looking at the FastAPI readme, which is pretty interesting.

00:29:17 And so I'm looking at different readmes to see if getting inspiration from others.

00:29:23 And the FastAPI readme is an interesting thing that I don't think I've seen in very many other open source projects.

00:29:29 There's the logo, of course, and then some links to documentation and source code, which actually I think are really handy to have right there at the top of the readme.

00:29:37 And then some features of key features, why you'd want to use it.

00:29:43 But it really feels like a sales page also somewhat.

00:29:45 But the sponsor list is interesting.

00:29:49 It directs right to some of the direct sponsors of the project.

00:29:52 And having sponsors that actually show up in the readme.

00:29:55 And look, Talk Python training is there, too.

00:29:58 So go, Michael.

00:30:00 But that's an interesting way to pay for large open source projects.

00:30:05 Kind of cool idea.

00:30:06 And then opinions like people that liked it and references.

00:30:11 This definitely feels like a single page.

00:30:13 Before it gets into the meat of the normal stuff that you kind of see in a readme, it's like a sales pitch page or a single page landing page.

00:30:21 And kind of maybe that's what a readme should maybe be to try to encourage people to use it.

00:30:26 I mean, we're not buying a product, but we do gain.

00:30:30 It is growing a project if more people use it.

00:30:33 So selling them on the project, it's kind of a cool idea.

00:30:36 Yeah.

00:30:36 I think that's great.

00:30:38 A couple of thoughts I have here.

00:30:40 Okay.

00:30:41 One, just on the sponsor thing.

00:30:43 That's one of the reasons it's really appealing to sponsor FastAPI is the visibility.

00:30:47 That you actually, it's not much.

00:30:50 It's not much to get a link back to your site, but it's a little bit.

00:30:53 And it's better than just the good feeling of, well, I paid to support this project and maybe buried in the contributors.md somewhere.

00:31:00 There's like my company name.

00:31:01 But no, it's like a little bit of give back.

00:31:04 And, you know, we get it.

00:31:05 We get some traffic from that.

00:31:06 And it's really nice.

00:31:07 And I think it's one of the things that other projects could do that have decent sponsorships is just to give a little visibility back like that.

00:31:16 Yeah.

00:31:17 I think it's working really well for Sebastian.

00:31:19 Because you can see I'm not the only one up there.

00:31:22 Am I coming in?

00:31:23 And then there's some of these listed here.

00:31:25 But then if you go to the documentation page, it has like even more sponsors.

00:31:29 Right.

00:31:30 Exactly.

00:31:30 Those are like gold sponsors that get the picture.

00:31:34 Then, too, I'd like to hear Adam's thoughts about sort of marketing your web project and presenting it in this way.

00:31:43 Because with Sanic, you're in a pretty parallel situation.

00:31:47 Yeah.

00:31:47 I mean, absolutely.

00:31:48 We do.

00:31:48 I agree 100%.

00:31:50 It's definitely a sales pitch.

00:31:53 And to your point about, you know, you're not necessarily buying anything, but you're buying into it.

00:31:57 Right.

00:31:58 You're buying into the project.

00:31:59 Because, you know, the idea is you're starting to build something.

00:32:04 And so you're going to be putting a lot of investment into that.

00:32:06 So, you know, I think it's sort of, you know, especially with some types of projects, it's a little bit more important than others.

00:32:15 If you need to specifically kind of buy into a specific philosophy and how you're going to be building something with it.

00:32:22 So, absolutely.

00:32:25 You know, we have do something a little bit similar, you know, trying to make sure that, you know, sponsors have a little bit, you know, have some visibility as well.

00:32:36 So, I think, but, and this is actually one of my pet peeves.

00:32:40 One of the, in my opinion, one of the most important things you touched on it is putting those links up at the very top.

00:32:47 You said that, you know, there's a link to the source code and the documentation.

00:32:51 And the source code, I feel like, is the one that's almost always missing.

00:32:55 You know, usually these readmes don't just show up in GitHub, right?

00:33:00 They show up on pypy.org.

00:33:02 You know, maybe they show up in, you know, the, you know, read the docs if it's getting, if it's, you know, that's where it's going to.

00:33:09 And it drives me nuts when I land on some sort of documentation website or something like that.

00:33:14 And I can't get back to the source code, you know, that, so, so I love to see that, that right up front.

00:33:21 You know, the catchy logo.

00:33:23 You go and say, like, edit the documentation in GitHub so that you can navigate back up the tree.

00:33:28 Like, that's probably my easiest way back, right?

00:33:30 That's what I do.

00:33:32 And exactly.

00:33:32 And you end up on some page, you know, 10, 10 levels deep inside of the project.

00:33:36 And that's not where you want to go.

00:33:38 Yeah, so Sanic looks like you got it right there.

00:33:40 You got source code.

00:33:41 Also, many of the, a lot of people don't know this, but a lot of, on PyPI, the homepage often links to the GitHub repo.

00:33:50 It doesn't have to.

00:33:51 People can link it to whatever they want to.

00:33:52 But this often links to the source code.

00:33:55 But, yeah, the source code right there on Sanic is pretty good.

00:33:59 Hey, you got sponsors too.

00:34:00 Neat.

00:34:01 Yeah.

00:34:01 I see the images and load in there, so maybe I need to look into that.

00:34:05 But.

00:34:06 Well, I think it loads on the GitHub thing.

00:34:10 Okay, that's good.

00:34:11 Yeah.

00:34:12 But while we're looking at readmes, I did want to also mention Will, because, you know, we have to.

00:34:19 Will McCugan.

00:34:20 It's Tuesday.

00:34:21 Yeah.

00:34:22 So, one of the cool things that he's got on both.

00:34:25 Is he unmasted on yet?

00:34:25 Yes.

00:34:27 I believe so, yes.

00:34:27 Yeah.

00:34:28 Okay.

00:34:28 So, on both rich and textual, there's a feature in the readmes of these dropdowns.

00:34:33 So, you can, like, open up a section that maybe, like this, the rich library talking about different ones.

00:34:41 It would be kind of overwhelming to have the whole thing listed here.

00:34:44 But having them collapsed is kind of a neat idea with little things.

00:34:47 So, and one of the great things about readmes is, I don't know how he does this, but I can go find out, because it's all in open source.

00:34:53 I can just look at the readme code and see how it's done.

00:34:57 I believe, yeah.

00:34:58 I believe it's a GitHub-specific thing.

00:35:00 So, I'd be curious, actually, to see how that might carry over to, like, PyPy.org or something like that.

00:35:06 Well, look.

00:35:06 Let's see if it works.

00:35:08 So, yeah, bear with us.

00:35:10 We're looking at to see if the dropdowns work on PyPI, and they seem to.

00:35:15 Oh.

00:35:15 Neat.

00:35:16 Amazing.

00:35:16 It's a TUI embedded in a Webby.

00:35:20 And I have seen this other places, too.

00:35:23 I think, I can't remember where, but there's a couple other open source projects that use these dropdowns that I've seen.

00:35:30 So, anyway.

00:35:31 That's probably enough on this topic.

00:35:33 No, it's not, Brian.

00:35:35 No, it's not.

00:35:36 No, it's not.

00:35:37 Okay.

00:35:37 Let me just, I just want to put out a call to people, because I tried this on the social medias, and it didn't really get me far, and maybe it's just going to go nowhere.

00:35:45 I want to do a Talk Python episode on awesome tools for managing your readme and your changelog and, like, release notes and stuff.

00:35:53 I think that would be fantastic.

00:35:54 I know there's things like Release Drafter and others, but none of them are big enough to be their own show.

00:35:59 So, I want to do, like, a set of, like, here's a bunch of cool tools that you can do.

00:36:03 So, if people are using some, please just tweet them to me, tweet them to me, email them to us, however you want to get them to me.

00:36:10 I don't, that's fine.

00:36:11 But it would be really helpful if I could find, you know, five, ten of these things, and then we could do a really cool show about, like, how to automate and do a bunch of these cool things.

00:36:18 Cool.

00:36:19 As well as just talking about what you got here.

00:36:20 I'll definitely send you a couple ideas.

00:36:22 Awesome.

00:36:23 I bet you got some.

00:36:23 Yeah.

00:36:24 Cool.

00:36:24 All right.

00:36:25 All right.

00:36:25 Now, let's talk about this thing that Brian Skin sent in.

00:36:30 Brian's been on the show before.

00:36:31 Thank you, Brian.

00:36:32 And he said, if you don't know, Closeember dev is coming up soon.

00:36:38 So, Closeember, like, December, closing on December, closing open source issues and other work on December, however you verbalize that, it's live.

00:36:49 And so, the idea here is let's support open source maintainers by helping them close issues and PRs through November.

00:36:57 I said December.

00:36:58 I guess it's November.

00:36:59 So, we're halfway through.

00:37:00 And it's a month-long initiative for maintainers and contributors and open source enthusiasts to go through and encourage healthier open source practices and raise awareness about maintainer burnout.

00:37:11 So, it's not about asking maintainers to do more, but it's like, how can we come in and do some of the tending of the garden and the cleanup of things?

00:37:20 You know, when I go to an open source project and I see, oh, there's PRs for the last three months and they're all open.

00:37:27 And like, I probably don't want to contribute to this because the chances are it's just going to be another thing sitting there for months and it's going to .gitignored and I don't care.

00:37:35 Right.

00:37:36 I mean, I want this change, but not enough that I'm going to do the work when there's a 90% chance that it's not going to get integrated.

00:37:41 Right.

00:37:42 I feel called out.

00:37:43 No, no, no.

00:37:44 So, the idea is like, well, let's go and kind of help people with these aspects of it.

00:37:51 Right.

00:37:51 So, there's, it talks about it being a two-way street and trying to do some of the healthy things to help people.

00:37:59 Right.

00:38:00 It also laments my challenge of like stale PR.

00:38:04 So, it has two aspects.

00:38:05 It has them for maintainers and for contributors.

00:38:07 So, for maintainers first, it says, keep in mind that the fundamental point of Closed Zember is maintainer health.

00:38:14 And so, take care of yourself, you know, go diet, exercise.

00:38:17 Also, has some really interesting things about decluttering your digital life.

00:38:21 I think that's actually really interesting.

00:38:23 I mean, we all just kind of have cruft build up.

00:38:27 Cruft, like on our physical desk, cruft on our computer desktop, cruft in like all the email and other things.

00:38:34 And really cleaning those things out.

00:38:36 It's really nice.

00:38:37 Like, I just formatted my Mac Mini after two years, about three days ago.

00:38:43 And it's like, I got a brand new computer.

00:38:44 I'm like, oh, I love to sit down at the sink.

00:38:46 There's no new computer here.

00:38:47 It's just the junk is gone.

00:38:48 And so, I think that's an interesting angle.

00:38:50 It talks about what you can do to help as a maintainer facilitate this.

00:38:56 So, you can get people help with triaging, with infrastructure, with technical writing.

00:39:00 For example, like that toot thing.

00:39:02 If there was a tutorial or any form of example or any line of code anywhere that said, here's how you use it, it would be way more used than if it's just, here's its name.

00:39:12 Good luck.

00:39:12 You know?

00:39:13 And so, having somebody do a little technical writing or put together a tutorial or even translation, all those would be really, really fantastic.

00:39:20 Right?

00:39:20 So, the idea is, if you're feeling up to it, you can identify some areas that would benefit from that.

00:39:26 You can edit your readme to have and create a close number issue to let people know that this is an option.

00:39:33 And you can actually go over here and see, right now, there's 729 repositories.

00:39:40 Like, some that come to mind that are, this is a search for all languages.

00:39:43 It just happens to be Pythons right at the top for all of them.

00:39:45 So, TQDM, NumPy, IPython, SciPy, Notebook, Spyder, Bolium.

00:39:52 Like, all of these are Python.

00:39:53 I don't really understand how that's happening, but maybe it's, maybe the algorithm.

00:39:57 Anyway, like, you could go to any of these that inspire you and pull this up.

00:40:00 All right.

00:40:00 So, that's on the maintainer side.

00:40:02 It's like, some things that you can do to help set it up, right?

00:40:04 Just like, label things and so on.

00:40:06 And then on the community side, it says, first, this is going to be on GitHub or GitLab.

00:40:11 You need to know Git.

00:40:12 So, take a moment and learn Git.

00:40:14 Because this is how you work on these things.

00:40:18 And able to just, like, run the tools, right?

00:40:22 Like, if I'm going to help you build a house, I should know how hammers work, right?

00:40:25 At least a little bit.

00:40:26 So, then it says you can start taking a look at GitHub issues that maybe you've opened and see whether or not they're outdated.

00:40:34 Or you could close stuff that you've sort of put out there in the burden.

00:40:37 And then go through that list like I talked about.

00:40:39 And, yeah.

00:40:41 Then, finally, there's, like, a celebration close boards.

00:40:44 So, down here, you can see there's, overall, there's, like, a scoreboard type thing.

00:40:48 It says, overall, there's, of the 16,531 issues, NPRs, 496 have been closed.

00:40:55 And then there's, like, a scoreboard of the closed issues by project.

00:40:59 So, like, Datalad is the number one.

00:41:02 And then AstroPi is just right behind it.

00:41:05 SciPi is up there.

00:41:06 And it tails off from there.

00:41:08 So, anyway, thanks, Brian Skin, for sending this in.

00:41:11 And, you know, people who want an angle to get into open source or want to contribute a little bit more, especially with some holiday time coming up, you know, here's something you could do that might mix up what you're doing.

00:41:21 Yeah, absolutely.

00:41:22 One of the things that I try to do as much as I can is try to advocate for people to get involved with sort of the small things, you know.

00:41:33 And so, I try to make, you know, if somebody's going to come on, you know, and create an issue, I say, well, great.

00:41:39 No, you can go, you can make this PR.

00:41:42 This is how you can go about and do it.

00:41:43 So, as a maintainer, I think, you know, these types of, you know, project, there was just one also in October.

00:41:51 There was a Hacktoberfest.

00:41:53 Yeah, Hacktoberfest, yeah.

00:41:55 So, I guess maybe something's coming in December.

00:41:56 Hacktoberfest, I think, is a little more about creating, like, creating your first PR or making your first contribution.

00:42:02 This is more about, like, I think, cleanup and closing out.

00:42:05 Yeah.

00:42:06 Yeah.

00:42:06 So, all the people from Hacktoberfest created a bunch of PRs and now they need closed.

00:42:11 Yes, I participated in both.

00:42:13 There you go.

00:42:16 One of the things that I wanted to point out is we did talk about the, how to help, how to help maintain FastAPI.

00:42:23 So, that would be all of, actually, all the tips that I read on how to help maintain FastAPI apply to every open source project.

00:42:30 So, if the open source project that you're interested in doesn't have really good how to help tips, the FastAPI stuff applies to almost everything.

00:42:39 Like, reproducing bugs, answering things.

00:42:42 And sometimes it's obvious from, like, a pull request or an issue that nobody's really excited about this thing and maybe it should just be closed.

00:42:51 So, that's helpful also is to just bring that up and say, hey, core maintainer people, this seems like it should be closed.

00:42:58 Should we go ahead and close that?

00:42:59 So, actually, on that point, I won't necessarily name names here, but there was a project that, not one that I maintain, but it's a project that, you know, was talking about retiring a specific feature, right?

00:43:17 And it was sort of, you know, no one's really using it.

00:43:19 It doesn't really seem like it has very much activity.

00:43:22 And they just put a little notice up there.

00:43:24 And just because people were engaging in conversation and because people were looking and were willing to, you know, write a couple of lines or even in GitHub, where you go and you just click, you know, a little thumbs up or whatever.

00:43:36 They saw all this interaction that people do care about this feature.

00:43:40 And, you know, it really does impact, you know, as a maintainer.

00:43:44 If you, you know, the more people that are engaged in discussion, the better it is to decide, you know, sort of how to steer the ship.

00:43:52 Yeah, absolutely.

00:43:53 Maybe it's just, hey, somebody suggested this.

00:43:56 I'm not sure.

00:43:57 What does the community think, right?

00:43:58 Having an opinion might be helpful, right?

00:44:01 Yeah.

00:44:01 Yep, absolutely.

00:44:02 All right.

00:44:03 You know what else is helpful?

00:44:03 Cashews.

00:44:04 Well, they're definitely delicious, but...

00:44:08 They are.

00:44:09 So, yeah, this popped up in my, you know, you go into GitHub, there's the Explore feed.

00:44:15 So, it just was in the top of my feed.

00:44:17 And it really caught my eye just because this is the type of thing that I find myself building and rebuilding on every single project that I do.

00:44:26 So, basically, you know, at its core, what Cashew uses, it calls itself an async cache framework for a simple API to build fast and reliable applications.

00:44:37 And when you look at sort of what they're providing you out of the box, it's a very feature-rich, but it's super simple to get up and running.

00:44:47 You know, I think you just really basically need one line to call a setup.

00:44:52 And after you do that, you're just adding decorators to stuff.

00:44:55 And, you know, I think this is really sort of, you know, provides some really good foresight on how to build a very nice, clean API that can be used in a lot of different situations.

00:45:07 So, you know, on their GitHub Remi, which I think is pretty well done, it gives you sort of how you might use this on a typical web application to cache, you know, cache some information on the request.

00:45:25 But you could really use it in a whole bunch of different features.

00:45:29 So, a couple of different things that I kind of wanted to, that really struck me as really interesting is, number one, they provide support for, you know, doing in-memory caching.

00:45:40 Also, Redis, which is very, very common.

00:45:42 And also, a write-to-disk, which I believe uses SQLite.

00:45:48 We talked about disk cache, which is, it looks like the foundational thing probably for the disk, the disk version of that caching.

00:45:57 And also, dill, instead of pickling, you dill things.

00:46:00 So, you can store more, wider variety of items into your cache, which is kind of cool.

00:46:06 I'm not familiar with dill, but it sounds like it's probably good.

00:46:09 Yeah, I don't know how much, you know, you combine dill and cache use on a normal basis, but I guess it could be done.

00:46:16 No, but so, one of the things that I think is really neat that they built into this is there's a cache on top of a cache.

00:46:24 And what I mean is, you know, let's say you're putting all this information, these really expensive operations into Redis or disk cache or something like that.

00:46:33 They also have what it looks like is maybe an application memory cache where you don't even necessarily need to go do those network calls every single time that you want to go fetch data.

00:46:45 And I feel like sort of, you know, there's sort of like that old saying that, you know, computer science, there's, you know, there's two hard things in computer science.

00:46:54 There's cache invalidation, naming, naming things and off by one errors, right?

00:47:00 So I feel like they sort of like are solving some of these problems and they've got a couple of really simple ways that you can, you can do cache invalidation.

00:47:10 You know, ways that you can, it just, it really strikes me as a very well thought out package.

00:47:18 But one of my favorite things that I noticed is one of the ways that you can invalidate a cache is by rate limiting.

00:47:25 Well, rate limiting is itself a huge area, especially for web applications.

00:47:32 And, you know, if you use a package like cache use, you know, you're getting two different, you know, two different requirements for one right here because, you know, it can, it can do the, you know, do double duty for you.

00:47:43 So I think this is, I haven't used this yet, but it looks super clean.

00:47:48 It looks like a very nice, very intuitive.

00:47:50 And I'm pretty excited to try to try to this one out for sure.

00:47:53 What an interesting kind of negative cache this rate limit thing is.

00:47:58 So the idea is if you call it, you can put it onto a function.

00:48:02 So if you call this function more than 10 times in a minute is the default of the example there.

00:48:08 Then you get, you basically get banned from calling it for a while.

00:48:12 So instead of saying, we're going to scale it by, by saving the answers to the questions you're asking to this function, we're going to save performance and CPU availability and whatnot by only allowing you to call too much.

00:48:25 And if you do it too much, like you're done, you're out.

00:48:28 Similar with circuit breakers for errors.

00:48:29 If there's too many errors, it's just going to stop for a while.

00:48:31 Yeah, exactly.

00:48:32 And, and there's also this, there's also, you know, I kind of glossed over it, but one of the things that they did for, for cache invalidation is there's sort of this, because it's using asyncioN under the hood, it looks like it's got this ability to sort of refresh your cache automatically.

00:48:52 So, so one of the things that you often have problems with caches is, you know, you might have stale data in there that you want, you know, how do you get rid of that stale data?

00:49:02 And so you can basically set up, it looks like, like, you know, in the background, it's, it's called early, early refresh or something like that.

00:49:11 And, you know, what it'll, you know, in the example that they give you, you know, if you've sort of, you know, called this, you know, within the given time period, it'll automatically go and sort of refresh it for you in the background, which I think is really cool.

00:49:25 Yeah. Okay. So this one says, I want the cache time to be 10 minutes, but if it gets called on minute seven to nine, in terms of the age of the cache result, go ahead and recompute it.

00:49:37 So that, you know, in the background, right, give them the answer that that's cash back, but then actually call it so that you, you know, if it takes 30 seconds to compute this thing or whatever, right.

00:49:47 It takes a long time, but every now and then there's going to be those gaps where it expired and you hit it again. Right. And so here's a way to kind of preempt that. So nobody sees the slow version.

00:49:57 There's a lot of interesting ideas here. Yeah. Way to go, Cassius. That's cool.

00:50:01 That's pretty cool.

00:50:02 Yeah. Yeah. Very cool. Awesome. Well, good find, Adam. Brian.

00:50:05 Yeah.

00:50:05 How about our extras?

00:50:06 Yeah. How about them? I don't have anything extra. Do you have something?

00:50:10 Let's go to Adam. Adam, anything else you want to give a shout out to while you're here?

00:50:14 Sure. I just noticed that definitely voting season is, is, is here. You know, there was just a big vote in, in the U S we, I live in Israel.

00:50:23 We just had an election season here, but now we've got Python elections coming up. So, so nominations for the Python steering council are open.

00:50:31 I think the way that it works is that you have to be a core member to, to do a nomination, but anybody that wants to, can go onto their discourse.

00:50:40 And, and, and, you know, if there's a candidate that you, that you support, you can, you know, you can reply to the comments, you can engage in the conversation.

00:50:46 And I think that's really cool and really, you know, a super way for people to sort of, you know, engage with the larger community.

00:50:54 Yeah. Very nice. And I actually have something related to that. Where is it? It's hiding.

00:51:00 So the, to pull out of my notes, maybe I didn't pull up, but the PSF survey. Oh yeah, here it is. It's just there.

00:51:07 David Lord put this out here. Speaking of web frameworks, we've covered them a lot. Let's bring Flask into it as well.

00:51:13 So over here on Mastodon, David says, take the PSF developer survey. It's closing in a few days. That was yesterday. So people should go and do that if they haven't.

00:51:23 Pretty sure I already did. I don't want to vote twice, but I also don't want to not vote. It's a dilemma. So anyway, it's really great that David put that out there.

00:51:31 So another thing is not quite voting, but it's, you know, tallying your opinion there. All right. I got a couple other things. Also quick, you know, shout out to your book while you're here.

00:51:42 Python web development was Sanic. People can check that out as well. So excellent. Let's see this one. No, that one is, that one's just a joke.

00:51:50 So I think actually, Brian, that's all I got for extras. So.

00:51:53 All right.

00:51:54 You ready for a joke?

00:51:55 I am.

00:51:56 All right. Over here. Again, I wish I could pull these up separately. I have to log out, but then I couldn't show you the other stuff.

00:52:01 And by the way, Samuel Colman just showed up on Mastodon as well. He wasn't there yet. So people go of

00:52:07 hydantic fame. So when all this stuff with Twitter came out, I thought this was a pretty hilarious, you

00:52:13 remember there was the switch of what did it mean for the blue mark, the blue check mark to be on an

00:52:19 account. It used to mean that you were verified and there's lots of rules about like showing your ID

00:52:22 and having a Wikipedia page. And there's like rules to get that check mark. And then Elon said, well,

00:52:28 we could just pay for that. And a bunch of people started impersonating people and doing

00:52:31 all sorts of funny shenanigans. Well, this, this is breaking here. And we've just noticed on Twitter

00:52:37 that the JavaScript verified account that it's the program. The, the Twitter name is real

00:52:44 programming language with 51 million followers. And there's a big message on it, Brian. What's the

00:52:50 message say?

00:52:51 It's, it's been canceled.

00:52:53 Suspended. Account suspended. Twitter suspends accounts that violate the Twitter rules.

00:52:58 JavaScript has been banned from Twitter for impersonating a real programming language.

00:53:02 I love it.

00:53:04 That's funny.

00:53:07 Yeah, it's pretty good. All right. Well, that's what I got for you this week in terms of jokes.

00:53:11 JavaScript has been suspended on Twitter.

00:53:14 You know, and I just speaking of Twitter, just if you want some humorous news, just Googling

00:53:19 Twitter on Google news is hilarious. just to me, I mean, it's also sad, but also funny.

00:53:25 Yeah, absolutely. Well, Adam, thanks for joining us this week and congrats on Sanic. It looks like

00:53:31 it's been going strong for a long time and it's got quite the community there.

00:53:35 I mean, yeah, we've been, we've been going strong since, 2016 or so.

00:53:39 Wow. That's awesome. All right, Brian. Thanks everyone. Thanks for being here.

