00:00:00 Hello and welcome to Python Bytes, where we deliver Python news and headlines directly to your earbuds.

00:00:04 This is episode 310, recorded November 15th, 2022.

00:00:09 I'm Michael Kennedy.

00:00:10 And I am Brian Okken.

00:00:12 And I'm Adam Hopkins.

00:00:13 Welcome, Adam. Great to have you here.

00:00:15 Awesome. Thank you. I'm excited to be here.

00:00:17 Yeah, people mostly know you, I would imagine, through Sanic, your web framework.

00:00:21 Tell people about yourself.

00:00:22 Yeah, that's correct.

00:00:24 Well, first, I just noticed episode 310.

00:00:27 So two more episodes and you guys pass the Python version.

00:00:30 So congratulations.

00:00:32 >> Thank you.

00:00:33 >> That's a milestone.

00:00:35 >> Six years. We just passed six years.

00:00:37 >> Yeah. It's exciting.

00:00:39 I remember when you guys started it.

00:00:41 So this is a great resource for the community.

00:00:43 >> Cool. Thanks.

00:00:44 >> So just to introduce myself, I'm Adam Hopkins.

00:00:48 I am one of the developers of the Sanic project.

00:00:51 My day-to-day job, I'm a Director of Software Engineering for Packet Fabric.

00:00:56 where we, you know, day in day out, I do web development.

00:01:01 So that's my gig.

00:01:03 - Right on, fun stuff, it sounds like.

00:01:05 - Yeah, absolutely.

00:01:06 - Cool.

00:01:07 - Yeah, well, Brian, you wanna kick us off with our first topic here?

00:01:10 - Yeah, sure.

00:01:11 So this is a little bit of an easy topic, tips for clean code in Python.

00:01:17 This is from Bob Bilderboss from PyBytes.

00:01:21 I was playing with this dark mode on and off.

00:01:23 It's kind of fun, anyway.

00:01:24 (laughing)

00:01:26 Dark mode is always appreciated in my book.

00:01:29 - Yes.

00:01:30 Well, so this resonated with me.

00:01:34 So I'm gonna blast through the tips really pretty quickly.

00:01:37 They're just good things to think about.

00:01:38 I think it's good occasionally to remind yourself of when you're organizing your code.

00:01:43 So using smaller units, I'm gonna come back to this, but essentially it's thinking about if you've got huge functions that do a whole bunch of stuff, maybe breaking it up.

00:01:52 Like I said, I'm gonna come back to that a little bit.

00:01:55 Magic numbers, always good constants are better than just numbers sitting in your file somewhere.

00:02:02 You know, I'm kind of on the fence on the void.

00:02:04 It's avoid global scopes the third, but there's nothing really global in Python.

00:02:08 It's module level, but still, if you've got large files, global scope can still be confusing.

00:02:14 So watch that.

00:02:15 Using linters and narrowing is a good thing.

00:02:20 I'm not, actually, I'm not gonna run all through all the tips.

00:02:23 some good tips here, so go ahead and read the article. But the thing I wanted to come back to is just this one, this first one, smaller units, because I just ran into this. So I'm working on refactoring the pytest check plugin, and currently it's just all in one. I mean, most of the code was in two files, like the basic plugin hookup, and then all of the rest of the code. And people have a couple of other people have added features, and that's a good thing, but I have had a hard time keeping my head around all the code in there and it was confusing myself.

00:03:03 I've been working on splitting it up.

00:03:05 I split up all the code and I split it up into this notion of the single responsibility principle.

00:03:12 I thought about this plugin as the features, and it's either large features that take up they're enough to be their own module or some related features that are altogether.

00:03:24 I've split up the code into different modules about those pieces.

00:03:29 The nice thing about that is I've also done that with the test.

00:03:33 I've split the test up into focusing on a feature at a time.

00:03:36 The tests are in multiple tests.

00:03:38 It's a lot more files now, but each little piece is just a few windows full of code.

00:03:45 It's pretty easy to get your head around, oh, for this feature, all of these things work together.

00:03:50 And it's really been great to work with now.

00:03:54 So I haven't published the final yet, but the smaller units thing, people do talk about large functions and that's something to watch out for.

00:04:02 But large files are a thing to keep in mind too.

00:04:05 And sometimes breaking it up.

00:04:08 You can go too far too, if you've got like a hundred different modules that are all are like 10 lines long, that's too far.

00:04:15 But you know, so.

00:04:16 - So I really like the idea of smaller units in both files and for like functions or classes or whatever.

00:04:23 And one of the ways that I think about it is if I'm looking at a chunk of code, maybe like an inner part of a loop or some other thing, I'm like, oh, I should probably put a comment to describe what that does.

00:04:32 Alternatively, I could make it a small function and give it a name that tells you what it does, right?

00:04:37 Like if it's, you know, update last login for user, that could be a comment or that you could highlight those five lines of code, extract method and give it that name.

00:04:46 Right, like it just, there's sort of a natural, if I'm looking at it and I don't understand it, how can I make it easier to understand?

00:04:54 Like that's a really productive way to do it, I think.

00:04:56 >> Yeah, especially if that bit of code really isn't the focus of the function, it's just some other stuff that has to be done.

00:05:02 Moving it out of the function proper is good.

00:05:06 Then the function name, yeah, just name it something clever.

00:05:09 >> I think one of the things you also really hit on there is breaking up the test files too, right?

00:05:15 And so I'm kind of curious to hear, like, you know, typically, you know, for maybe for a smaller package, I mean, do you try to keep sort of one test file for one module and keep a module or, you know, sometimes I feel like when I've done that, even trying to iterate and all the different things that I might want to test in one file, it could still end up being, you know, a couple thousand lines long.

00:05:37 - I'm focusing on features.

00:05:39 So trying to keep the, like for instance, the one of the functionalities for pytest check is stop on fail working, and work correctly because you possibly could have multiple failures in a single test.

00:05:54 So how does stop on fail work?

00:05:55 Well, there's a defined way we've defined it for the plugin.

00:05:59 And so I've got like one test file that tests the stop on fail functionality.

00:06:06 So I prefer breaking it up into user functionality instead of modules, internal modules.

00:06:13 - Right on.

00:06:15 Oh, good tips, Bob, and nice find, Brian.

00:06:17 - One thing also I noticed that was in this article that I'm probably gonna touch on in a little bit, sort of that idea of the global scope, 'cause that's definitely something that I think can actually cause some problems down the road, and I'll touch on that in a little bit.

00:06:33 - Awesome, yeah, absolutely.

00:06:35 There's also a lot of tips in here that can be automated.

00:06:38 You should write code that matches this kind of stuff already.

00:06:42 But running the linters, running black, yeah, pre-commit, one of them is using idiomatic code, which you could use flint.

00:06:52 We talked about a bunch of things that like upgrade to Python two to three, almost like pyupgrade, I think, whatever you, yeah.

00:06:59 Those types of things, like you could, a lot of this stuff could be brought in on the tool chain level too, which is kind of nice.

00:07:06 - Yeah.

00:07:07 - All right, let's talk about Mastodon.

00:07:09 So I don't know if you all have heard, Twitter's kind of going nuts right now.

00:07:13 It seemed like a place that was just gonna be around forever, but apparently maybe no.

00:07:18 And so Brian, I think you maybe encouraged me to go over to Mastodon and check it out a little bit last time.

00:07:24 - This was just like a week ago, man.

00:07:26 You've like just went crazy.

00:07:28 - I have gone crazy, I'm telling you.

00:07:29 But I think there's a lot of cool stuff over here.

00:07:31 So I'm super psyched about it.

00:07:34 I just did a Talk Python episode, but I'll pull up a link to that in a moment.

00:07:38 But what I found, so you encouraged me to go over there, and I did.

00:07:43 What I found was there's a whole bunch of the people that we know and have been interacting with over on Twitter.

00:07:48 Now, they're all over on Mastodon, and it's a super nice active community.

00:07:52 I expected to show up there and go like, "Well, I'll wait till people show up." >> They're here. They're there.

00:07:57 >> They're already there. They're already there.

00:07:59 Adam, I saw that you're over there, and Brian, obviously you are.

00:08:02 I got the shows going over there and so people can follow Python Bytes on Mastodon, they can follow Python.

00:08:09 I'll put a link to all of the various, all of our profiles, including Adam's over there in the show notes.

00:08:15 >>And we're all kind of learning at the same time.

00:08:17 So even the, you show up and they've already got hundreds of friends there, but they're like, they're still learning also.

00:08:24 So, yeah.

00:08:24 >>Yeah, yeah, absolutely.

00:08:26 They are.

00:08:27 So, Marco, go ahead, go ahead, go ahead, Adam.

00:08:30 I was gonna say, it does sort of kind of bring up an interesting question that I've sort of been, you know, feeling is, you know, are people starting to share in two different places now, you know, trying to have conversations multiple places. And so there is a little bit of an awkward and maybe, you know, we'll kind of just, you know, trudge through it and see how it works.

00:08:48 But I definitely agree that it's, it feels very, it feels clean. Like it just feels like very, you know, fresh. Maybe it's just because it's a, you know, a new app to play with or one, I don't know, but there's, I agree. It's, I'm very happy to see that, you know, people that I'm already, you know, subscribed to and trying to, trying to see what they have to say are already there. And, and you're definitely interested to see, see how this develops because I think it's, you know, it can only be positive. - Yeah, I totally agree. My philosophy is kind of, for the moment, to be mastered on first, not to burn down my Twitter account or to lead my community over there, but just like, all right, Twitter looks like it's trying to kill itself.

00:09:27 Let me try to put some energy over here.

00:09:28 And after Brian kind of got me moving, looking at Mastodon, it lines up way better with the ideology of open source and Python communities, having this federated different bunch of servers, people can control them, they're open source, there's not one central choke point for it or whatever.

00:09:47 But yeah, I think it's really interesting and I encourage people to check it out.

00:09:51 I was gonna highlight that Marco in the audience said, me two weeks ago, "Is Mastodon good enough to replace Twitter?" - Me now, is Twitter good enough of a replacement for Mastodon?

00:10:00 Yeah, I'm kind of the same way.

00:10:03 All right, so I got a bunch of stuff I wanna share real quick with you.

00:10:05 So I'll go through it quickly.

00:10:06 That is not it, gotta go in the right order.

00:10:09 So I did a really cool episode with Gina Houska, Juan Luis, Simon Willison, and oh, I gotta update my show notes 'cause she dropped in last minute, Carol Willing as well.

00:10:20 So people can check that out.

00:10:23 These different places, you should really support them.

00:10:25 these little instances, like for example, the one that Brian and I are on is Fosstodon, the free and open source software instance.

00:10:34 It went from 2,000 to 40 something thousand users in a week and their hosting cost went from 100 to $1,000 in the same period, which is a lot and it's just volunteer, right?

00:10:44 That's a lot to be paying, but they have a Patreon, which is really nice.

00:10:48 You go to their Patreon and you can sponsor them.

00:10:50 You can also do that for Mastodon.

00:10:52 If you look at, they have a sort of a statement breakdown of like, here's how much we spend on hosting, how much we spend on CDN and Bitwarden and all these different things and how it breaks down.

00:11:00 It turns out, Brian, 2.5 cents per user will fund Mastodon.

00:11:05 - That's awesome. - Wow.

00:11:06 - I feel like we should be doing this.

00:11:08 Like we can all spare 2.5 cents or maybe a dollar.

00:11:11 Not everybody, and if you can't really, please don't.

00:11:14 But most people who are software developers can surely do that.

00:11:18 Put another way, out of those 40,000 people, if just 100 of them pay $10 a month, that will also fund Mastodon.

00:11:25 So it's very achievable that we could end up in a world that is not ad-ridden, tracker-ridden, surveillance capitalism that's trying to trick us or manipulate us into doing things, but these really nice open places that we can move around as our values match, you know?

00:11:41 - Yeah.

00:11:42 - I think the other side of it too is, you know, we need to make sure that the people who are the content creators, people that have large followers and are putting out information that people wanna read, you know, make sure that they're supporting this as well because, you know, where the content is, that's where the people will go.

00:11:58 - Yeah.

00:11:59 - So hopefully we can get more people paying for it and supporting it.

00:12:02 - Yeah, I'm doing it myself and I definitely encourage people who can because it's fantastic.

00:12:08 All right, what else did I want to cover about this?

00:12:10 It's open source, it's Ruby, which is not the most amazing open source for Python people but it is open source, which is very cool and you can go get it.

00:12:17 There is a Python package called toot, there's also a CLI, you call it, We covered this a little bit last time, Brian.

00:12:23 I said I'd go into it more, right?

00:12:24 I think.

00:12:25 >> Yeah.

00:12:25 >> So one of the things I did, come back to that. One of the things I did on, one thing that's annoying if you're logged in, it's really hard to pull up an individual tweet on your own instance without it being in the show here.

00:12:39 But one of the things I did Saturday morning, Brian, do you see the third button from the second row of my Stream Deck here?

00:12:45 >> Okay.

00:12:45 >> So I wrote and I integrated the Mastodon API into my Stream Deck.

00:12:51 So now whenever we start a show, I just push that button and off it goes.

00:12:54 Nice.

00:12:55 I think actually I might have pushed the one for Talk Python this time because they're the same screen just slightly different.

00:13:00 But anyway, we push that button and it'll kick it off and that'll just post a toot, I guess we would say.

00:13:08 And then finally...

00:13:09 I still can't get over that.

00:13:10 It's just funny.

00:13:11 It's a little much, isn't it?

00:13:12 All right.

00:13:13 And then finally, finally, one thing that's really nice is if you have a Chrome-based browser like Vivaldi or one of those or Brave, you can right-click on the tab and say install.

00:13:25 Mine says install Fostadon because I was on Fostadon, but if you're on Mastodon social or whatever it's called, it would say install that, and then you get a progressive web app that is, I would say, probably the best app on the desktop for doing Mastodon.

00:13:39 >> Ooh, neat.

00:13:39 >> Got hotkeys, all sorts of fun stuff.

00:13:42 Lots of, you can do like the advanced view with columns and all of these things.

00:13:46 >> So I encourage people.

00:13:47 Yeah, so I encourage people to check this out.

00:13:49 One more thing on toot.

00:13:50 We'll come back to CloseVember in a little bit.

00:13:53 Maybe this is relevant here, but this is a library, Python package that you can use to talk to Mastodon.

00:14:00 I have no idea how to use it. It's completely opaque.

00:14:02 It's like star, star, star, star, star, KW args callable.

00:14:07 It doesn't have any structure.

00:14:10 It's all done up at runtime.

00:14:13 You can't tell what are the functions.

00:14:15 even if you dir it, like it doesn't have any functions or anything you can call.

00:14:18 So how it's used, I have no idea.

00:14:20 It's hard to use, but the one thing you can do is it has a CLI that will generate your OAuth login tokens and then you just use out directly with requests or HTTPS or something.

00:14:30 So as far as I can tell, it's not particularly useful until some sort of example is written.

00:14:35 Even the tests don't seem to help very much.

00:14:37 But what it does do is it'll generate your access tokens that you can use in the rest of your code, which is pretty cool.

00:14:42 >> Okay.

00:14:43 >> Yeah.

00:14:43 >> Nice.

00:14:44 - All right, yeah, well, people definitely should check that out.

00:14:48 Adam, you're up next.

00:14:49 - All right, so I guess, you know, little bit of a backstory to, you know, a couple episodes ago, you were talking about an article that I posted on my blog about this new feature that we invited and brought into Sanic about a month ago.

00:15:05 And I, well, I was on Twitter at the time, but I sent a tweet to you, kind of with a little bit of a correction.

00:15:11 And so I guess that's kind of why I'm here, I just wanted to kind of clear up a little bit.

00:15:16 The feature that we added into Sanic is this worker manager.

00:15:21 And the idea covered in the blog article is sort of what an implementation of that might look like.

00:15:27 So really, kind of what the article was trying to cover was how to build a Celery-like clone.

00:15:36 Can we take a step back really quick and just have you give the elevator pitch for Sanic, just for people who maybe haven't used it?

00:15:42 Sure. So Sanic is an async framework, web framework for building web applications.

00:15:51 One of the things that it comes with is a built-in web server as well.

00:15:56 So it's both a web server and a framework.

00:16:00 So it does both parts.

00:16:02 >> So you don't need a Microwave's gear, G-Core or something along those lines?

00:16:05 >> Correct. You can use something like UV-Core if you wanted to.

00:16:08 So it can operate as an ASGI app.

00:16:11 So that is a possibility.

00:16:14 But generally, I find that most people that use Sanic will use the integrated Sanic server because it's sort of built for high performance.

00:16:25 It's optimized to work with the framework.

00:16:29 The framework itself is generally very unopinionated and sort of tries to get out of your way and provide you with the tools that you need to build an application, but not dictate specific patterns.

00:16:42 So that's the short and long pitch of it.

00:16:47 Last year, I put together a book on different patterns and how you might build production applications in it with Sanic and what are some of the possibilities that are outside the scope of just these documents here.

00:17:04 So specifically, one of the things that we kind of had noticed and really drove us to what ultimately became the worker manager feature is that Santa comes out of the box with auto reload, the ability to scale up multiple workers, all that kind of stuff that you would sort of expect.

00:17:26 But you might, in older versions, you might have a different experience when you're doing development versus when you're in production mode.

00:17:34 And so we wanted to kind of get rid of that so that every single time that you boot up Sanic, whether you're in, whether you're local host or you're deploying it, you get the same experience.

00:17:48 You've got one process whose whole job is to sort of manage the whole show, and then one or more of these worker processes that can be individual servers.

00:17:58 And the idea, once we have that, it really provide us the ability to take that abstract abstraction and turn it into something a little bit more and allow individuals to inject arbitrary processes into it.

00:18:13 So the example in the article was this cellular like worker manager, but you know, one of the other big use cases that we see a lot with Sanhok are people that are trying to build chatbots, you know, maybe something for discord or something like that.

00:18:27 So this would really make it very simple for you to run both a web application and a chatbot all from one process and have it all managed without having to scale out multiple instances.

00:18:42 - Nice, yeah.

00:18:43 Yeah, so does it, when you run these worker processes, can it run in, does it run in a background thread?

00:18:48 Or one of the things when I first talked about this that was a little unclear to me is, once you have, when you go into production, you farm out to a bunch of worker processes, typically, right?

00:18:59 You say like, we're going to run four worker processes and they're all going to round robin, handle these requests.

00:19:05 But how does that management correlate back to these worker processes?

00:19:10 Because if they all are kind of managing their own, then you're going to end up with a whole bunch of them.

00:19:16 Correct. So when you start up the application, and this actually is the whole reason, going back to Brian's thing from earlier about trying to keep things out of the global scope, And why I encourage people to do that is under the hood, we're using the multiprocessing from the standard library.

00:19:36 So it's very easy to make some mistakes.

00:19:41 And if you've got some code that is kind of sitting in the global scope, you might accidentally run it in all these different work processes that you don't necessarily want it to.

00:19:50 So trying to keep your abstractions nice and tight and keeping everything's inside of functions and callables kind of avoids that.

00:19:57 So to answer sort of your question is, when you start up a worker process, you know, it's, there's two kinds, right?

00:20:04 There's the processes that are meant for personic servers, and then for anything else that you might want.

00:20:11 The reloader is going to be one.

00:20:12 We also have in the extensions, we also provide out of the box, a inspect utility.

00:20:21 So it basically would give you a CLI command line utility that you can sort of check the status of any operating workers.

00:20:30 So you can see how many things are running.

00:20:32 - Oh, that's cool.

00:20:33 - If you wanted to sort of see how many requests are on each of the workers, you could kind of get that information.

00:20:38 - That's so hard to tell in production.

00:20:40 You're like, it's kind of slow and this one seems stuck, but I don't know what the heck's going on.

00:20:44 - Absolutely.

00:20:45 And this is really sort of the thing that this has opened up because what happens, and for anyone that's ever done anything that's using multiple processes in Python, one of the things that the package does provide you is these different primitives where you can short share state between them.

00:21:07 And in older versions of Sanic, there was no way that you could do that.

00:21:13 But one of the things that we now have is you could have say one Q object and every single one of your workers is able to push and pull information from that queue.

00:21:22 You know, you can have, you know, shared counters and it really kind of gives you a lot more flexibility that just didn't exist before.

00:21:31 - Cool, well, it looks fantastic.

00:21:32 And the other thing that you put in here is cashews.

00:21:36 What's the, how's cashews relate back to this?

00:21:39 - It's not related back to this at all.

00:21:40 This is just something--

00:21:41 - Oh, this is your second topic, right?

00:21:42 - Yeah, yeah.

00:21:43 - Okay, sorry, I put it in the wrong order then.

00:21:44 We'll come back to that one then.

00:21:46 Sorry, okay.

00:21:47 - Awesome, all right, well, this is really cool.

00:21:49 And it's something that a lot of web frameworks don't have, is this ability to richly manage stuff that shouldn't be processed during a web request.

00:21:57 And a lot of times people end up running whole different servers, you know, Redis plus Celery or something fairly complicated.

00:22:03 So this is really cool that it's kind of like tightly tied together there.

00:22:06 - So one actually kind of use case that just kind of give people a little bit of understanding of how you might actually use this in production.

00:22:14 So I use Celery very heavily, as well as Sanic.

00:22:19 One of the things that anyone that's used Celery knows about is there's this function, this service called Celery B.

00:22:28 And basically the idea there is you're sort of scheduling these crown-like jobs that are gonna run periodically over some defined schedule.

00:22:36 Well, when you put all these things into Kubernetes applications, containers, your DevOps guys come knocking on your door and say, how do I know that this thing is still running?

00:22:47 Like, I want to be able to ping this and make sure that things haven't died.

00:22:50 And so that, like Kubernetes, that's sort of the, one of the things that it does for you, right?

00:22:54 Is it kind of checks the health of your applications and kind of restarts things.

00:22:58 And it's very simple to do from a web application, not so easy to do from a service like CeleryBeat.

00:23:04 So what we did is we built CeleryBeat into a Sanic worker process like this.

00:23:12 So basically what it does is it's kicking off these jobs every, I don't know, say every 10 seconds, some period, and it's sending a ping, HTTP ping over to the Sanic service that's running it, and then we can keep the state there, and then it's super simple for Kubernetes at that point to sort of see what's the health of this application, and is it still running.

00:23:34 - Yeah, very cool.

00:23:35 That's a really interesting use.

00:23:36 Awesome.

00:23:37 All right, Brian, can we talk about our sponsor this week?

00:23:39 - Yeah, let's.

00:23:40 - Awesome.

00:23:41 All right, well, this week, once again, we have back Microsoft, such great supporters of the show.

00:23:48 And if you've not yet checked out Microsoft for Startups Founders Hub, you definitely should.

00:23:53 As we all know, starting a business is hard.

00:23:55 They provide a bunch of support, both in financial grants for compute and other cloud services, as well as access to a mentorship network and other types of advice, basically, and connections.

00:24:10 So it's a free service.

00:24:13 All you have to do is apply.

00:24:14 You don't have to be third-party validated.

00:24:16 You don't have to be VC backed.

00:24:18 You just apply, and then once you're in, you're in.

00:24:20 And unlike the requirements that go live in San Francisco, Silicon Valley, New York City, one of these places where there's a community of founders and mentors and experts, you get access to a similar network from wherever you are.

00:24:36 So it's not about who you know, but, or who you have access to, 'cause you can use their network.

00:24:41 So they give you access to hundreds of mentors across a range of disciplines, like idea validation, fundraising, management and coaching, sales and marketing, and a whole bunch of specific technical stress points.

00:24:52 And you'll be able to book a one-on-one meeting with these mentors, many of whom are former founders themselves, and it'll really give you a leg up making connections and keeping your company on the right track.

00:25:03 In addition to that, you get a bunch of Microsoft Cloud credits, a bunch of GitHub credits.

00:25:07 They partnered with OpenAI, a global leader in AI research and development to provide exclusive benefits there as well.

00:25:14 To make your idea a reality with the critical support you'll get from Microsoft for Startups, join, is it join?

00:25:19 Just visit pythonbytes.fm/foundershub2022.

00:25:23 The link is in your show notes.

00:25:25 So as always, thanks to Microsoft for supporting the show.

00:25:29 - Yes, thanks.

00:25:30 - Hi Brian, what's next?

00:25:31 - Well, I wanted to touch on FastAPI a little bit And specifically, there was a new release that caught my attention.

00:25:40 So the 0.87.0, we should bug them about being zero-verse still.

00:25:49 But so, yeah, come on.

00:25:51 It's definitely production-ready by now.

00:25:55 So anyway, well, so what I wanted to talk about is some of the interesting bits here, which I thought was really kind of cool of Sebastian and others to handle.

00:26:05 So one of the things is they upgraded to Starlet, and I think it's Starlet 0.2 or something.

00:26:12 Anyway, I'm not sure which version of Starlet, but the Starlet version they changed to had a test client update and updated from requests to HTTPX.

00:26:24 And that's pretty interesting.

00:26:26 So FastAPI gets that also.

00:26:28 But what happens with that is the test client actually had some breaking changes with it.

00:26:34 And somebody named Cludex decided to create a tool called BumpTestClient.

00:26:43 And this is pretty cool because the idea is you've got some test code already that depends on test client, and you can run this BumpTestClient on your test code, and it upgrades it to the new interface.

00:26:58 Cool as that. That's just pretty cool.

00:27:00 >> That is cool. Yeah.

00:27:01 >> Nice extra bit of upgrade help for people.

00:27:04 The other thing I wanted to point out is that there's a lot of documentation changes.

00:27:11 One of the things he added was a help maintain FastAPI.

00:27:16 I say he, but I think there's a lot of people working on FastAPI now, so I'm not sure who added it, but help maintain.

00:27:22 I think this is really pretty great because, let's see if I can find it.

00:27:28 It's focusing on this section of help maintain it, focuses on a couple of things that people don't think is very glamorous, but it's hugely helpful for open-source projects, and that's helping with the issues.

00:27:40 Because a lot of issues are really just questions or a user doesn't understand how to use it or they're using it in a weird way, and it's just a knowledge gap thing.

00:27:49 Helping those people out, great help for the maintainers so they can focus on building new features.

00:27:54 Also helps to point out maybe that there's documentation holes.

00:27:58 The other bit is reviewing pull requests.

00:28:02 Both of these topics pop into bigger sections.

00:28:08 Like the helping with GitHub issues, talk about how to do that.

00:28:12 There's some documentation on how to help, like understand the question that somebody is asking and maybe change the question if it's not clear.

00:28:20 trying to reproduce other people's problems, suggesting solutions.

00:28:25 If you think that it's been solved by somebody, if it's solved but it's still open, ask if you can close it.

00:28:32 This sort of help, especially with large projects, helps a ton.

00:28:37 I think it's cool that this has been focused on.

00:28:40 The other thing I wanted to point out, which I thought was cool, was we covered Ruff earlier on one of the other episodes.

00:28:49 and it's a Rust-based linter, but FastAPI is now using it internally to lint the FastAPI code, so that's kind of fun.

00:28:58 - Yeah, that's fun.

00:28:59 - Now, one of the reasons why I was looking at this is coming back to the little project, pytestCheck, that I'm working on.

00:29:08 I'm refactoring it.

00:29:09 I also thought the readme is lame.

00:29:11 So I was looking at the FastAPI readme, which is pretty interesting.

00:29:18 I'm looking at different read-me's to see if getting inspiration from others.

00:29:24 The FastAPI read-me is an interesting thing that I don't think I've seen in very many other open-source projects.

00:29:29 There's a logo, of course, and then some links to documentation and source code, which actually I think are really handy to have right there at the top of the read-me.

00:29:38 Then some key features, why you might want to use it.

00:29:43 But it really feels like a sales page also somewhat.

00:29:46 But the sponsor list is interesting.

00:29:49 It directs right to some of the direct sponsors of the project.

00:29:52 And having sponsors that actually show up in the readme, and look, Talk Python Training is there too.

00:29:58 So go Michael.

00:30:00 But that's an interesting way to pay for large open source projects.

00:30:05 Kind of cool idea.

00:30:06 And then opinions, like people that liked it and references.

00:30:11 This still feels like a single page, before it gets into the meat of the normal stuff that you kind of see in a readme, it's like a sales pitch page or a single single page landing page.

00:30:21 And kind of maybe that's what a readme should maybe be to try to encourage people to use it.

00:30:26 I mean, we're not buying a product, but we we do gain.

00:30:29 It is growing a project if more people use it.

00:30:33 So selling them on the project.

00:30:35 It's kind of a cool idea.

00:30:36 Yeah, I think that's great.

00:30:38 A couple thoughts I have here.

00:30:41 Okay.

00:30:41 One, just on the sponsor thing, that's one of the reasons it's really appealing to sponsor FastAPI is the visibility.

00:30:48 That you actually, it's not much.

00:30:50 It's not much to get a link back to your site, but it's a little bit.

00:30:53 And it's better than just the good feeling of, well, I paid to support this project, and maybe buried in the contributors.md somewhere there's like my company name.

00:31:01 But no, it's like a little bit of give back, and we get some traffic from that, and it's really nice.

00:31:07 And I think it's one of the things that other projects could do that have decent sponsorships is just to give a little visibility back like that.

00:31:16 I think it's working really well for Sebastian, 'cause you can see I'm not the only one up there in my company.

00:31:23 - And then there's some of these listed here, but then if you go to the documentation page, it has like even more sponsors.

00:31:30 - Right, exactly, those are like gold sponsors that get the picture.

00:31:33 Then two, I'd like to hear Adam's thoughts about sort of marketing your web project and presenting it in this way, 'cause with Scenic, you're in a pretty parallel situation.

00:31:47 - Yeah, I mean, absolutely.

00:31:48 We do, I agree 100%.

00:31:50 It's definitely a sales pitch.

00:31:53 And to your point about, you're not necessarily buying anything, but you're buying into it, right?

00:31:58 You're buying into the project.

00:31:59 It's, you know, the idea is you're starting to build something, and so you're gonna be putting a lot of investment into that.

00:32:06 So, I think it's sort of, especially with some types of projects, it's a little bit more important than others, if you need to specifically kind of buy into a specific philosophy and how you're gonna be building something with it.

00:32:22 So, absolutely.

00:32:23 We have do something a little bit similar, trying to make sure that the sponsors have a little bit, have some visibility as well.

00:32:37 So I think, but, and this is actually one of my pet peeves.

00:32:40 One of the, in my opinion, one of the most important things you touched on it is putting those links up at the very top.

00:32:47 You said that, you know, it's got the, there's a link to the source code and the documentation.

00:32:51 And this, the source code, I feel like, is the one that's almost always missing.

00:32:55 You know, usually these readmes don't just show up in GitHub, right?

00:33:00 They show up on pypy.org.

00:33:02 Maybe they show up in, read the docs if it's getting, that's where it's going to.

00:33:09 And it drives me nuts when I land on some sort of documentation website or something like that, and I can't get back to the source code.

00:33:17 So I love to see that right up front, the catchy logo.

00:33:23 - You go and say, edit the documentation in GitHub so that you can navigate back up the tree.

00:33:29 That's probably my easiest way back, right?

00:33:31 That's not how it's gonna be. - That's what I do.

00:33:32 - Exactly, and you end up on some page, you know, 10 levels deep inside of the project, and that's not where you want to go.

00:33:38 - Yeah, so Sanic looks like you got it right there.

00:33:40 They got source code.

00:33:41 Also, many of the, a lot of people don't know this, but a lot of, on PyPI, the homepage often links to the GitHub repo.

00:33:50 It doesn't have to.

00:33:51 People can link it to whatever they want to, but this often links to the source code.

00:33:55 But yeah, the source code right there on Sanic, it's pretty good.

00:33:59 Hey, you got sponsors too, neat.

00:34:01 Yeah, I see the images and loading there.

00:34:04 So maybe I need to look into that, but.

00:34:06 (laughing)

00:34:07 - Well, I think it loads on the GitHub thing, but.

00:34:11 - Okay, that's good.

00:34:12 - Yeah, but while we're looking at readmes, I did wanna also mention Will, because we have to, Will McGugan.

00:34:21 - As it's Tuesday.

00:34:21 - Yeah, so one of the cool things that he's got on--

00:34:24 - Is he on Mastodon yet?

00:34:26 - Yes. - I believe so, yes.

00:34:27 - Yeah. - Okay.

00:34:28 - So on both rich and textual, there's a feature in their readmes of these drop downs.

00:34:33 So you can like open up a section that maybe like this, the rich library talking about different ones, it would be kind of overwhelming to have the whole thing listed here, but having them collapsed is kind of a neat idea with little things.

00:34:48 So, and one of the great things about readmes is, I don't know how he does this, but I can go find out 'cause it's all in open source.

00:34:54 I can just look at the readme code and see how it's done.

00:34:57 I believe, yeah, I believe it's a GitHub specific thing.

00:35:00 So I'd be curious actually to see how that might carry over to like pypi.org or something like that.

00:35:06 - Well, look, see if it works.

00:35:08 So yeah, bear with us.

00:35:10 We're looking at to see if the dropdowns work on PyPI and they seem to, so.

00:35:15 - Oh, neat.

00:35:16 - Amazing.

00:35:17 - It's a two-e embedded in a web-e.

00:35:20 - And I have seen this other places too.

00:35:23 I think, I can't remember where, but there's a couple of open source projects that use these dropdowns that I've seen.

00:35:30 So there.

00:35:32 That's probably enough on this topic.

00:35:34 - No, it's not, Brian.

00:35:35 No, it's not.

00:35:36 - No, it's not.

00:35:37 Okay. - Let me just, I just wanna put out a call to people because I tried this on the social medias and it didn't really get me far and maybe it's just gonna go nowhere.

00:35:45 I wanna do a Talk Python episode on awesome tools for managing your readme and your changelog and like release notes and stuff.

00:35:53 I think that'd be fantastic.

00:35:54 I know there's things like release drafter and others, but none of them are big enough to be their own show.

00:35:59 So I wanna do like a set of, like here's a bunch of cool tools that you can do.

00:36:03 So if people are using some, please just tweet them to me, toot them to me, email them to us, however you wanna get them to me, that's fine.

00:36:11 But it'd be really helpful if I could find, you know, five, 10 of these things, and then we could do a really cool show about like how to automate and do a bunch of these cool things.

00:36:19 - Cool. - As well as just talking about what you got here.

00:36:21 - I'll definitely send you a couple ideas.

00:36:22 - Awesome, I bet you got some, yeah, cool.

00:36:25 All right, now let's talk about this thing that Brian Skins sent in.

00:36:30 Brian's been on the show before, thank you Brian.

00:36:32 And he said, if you don't know, Closember dev is coming up soon.

00:36:38 So Closember, like December, closing on December, closing open source issues and other work on December, however you verbalize that, it's live.

00:36:49 And so the idea here is let's support open source maintainers by helping them close issues and PRs through November.

00:36:57 I said December, I guess it's November.

00:36:59 So we're halfway through.

00:37:00 And it's a month-long initiative for maintainers and contributors and open source enthusiasts to go through and encourage healthier open source practices and raise awareness about maintainer burnout.

00:37:12 So it's not about asking maintainers to do more, but it's like, how can we come in and do some of the tending of the garden and the cleanup of things?

00:37:20 You know, when I go to an open source project and I see, oh, there's PRS for the last three months and they're all open.

00:37:27 And like, I probably don't want to contribute to this because the chances are it's just going to be another thing sitting there for months and it's going to get ignored.

00:37:35 And I don't care.

00:37:35 Right.

00:37:36 I mean, I want this change, but not enough that I'm going to do the work when there's a 90% chance that it's not going to get integrated.

00:37:42 Right.

00:37:42 I feel called out.

00:37:46 So the idea is like, well, let's go and kind of help people with these aspects of it.

00:37:51 Right.

00:37:51 So there's, it, it talks about, it being a two way street and trying to do some of the, the healthy, healthy things, help people.

00:37:59 Right.

00:38:00 It also laments my challenge of like stale PR.

00:38:04 So it has two aspects.

00:38:05 It has for maintainers and for contributors.

00:38:07 So for maintainers first, it says, keep in mind that the fundamental point of Clozember is maintainer health.

00:38:14 And so take care of yourself, go diet, exercise.

00:38:17 Also has some really interesting things about decluttering your digital life.

00:38:22 I think that's actually really interesting.

00:38:24 I mean, we all just kind of have cruft build up.

00:38:27 Cruft on our physical desk, crufts on our computer desktop, cruft in all the email and other things, and really cleaning those things out.

00:38:36 It's really nice.

00:38:37 Like I just formatted my Mac Mini after two years, about three days ago, And it's like, I got a brand new computer.

00:38:44 I'm like, oh, I love to sit down at the sink.

00:38:46 There's no new computer here.

00:38:47 It's just the junk is gone.

00:38:48 And so I think that's an interesting angle.

00:38:50 It talks about what you can do to help as a maintainer facilitate this.

00:38:56 So you can get people help with triaging, with infrastructure, with technical writing.

00:39:00 For example, like that toot thing.

00:39:02 If there was a tutorial or any form of example or any line of code anywhere that said, here's how you use it, it would be way more used than if it's just, here's its name.

00:39:12 good luck, you know, and so having somebody do a little technical writing or put together a tutorial or even translation, all those would be really, really fantastic, right? So the idea is, if you're feeling up to it, you can identify some areas that would benefit from that.

00:39:26 You can edit your readme to have and create a closember issue to let people know that this is an option.

00:39:34 And you can actually go over here and see, right now there's 729 repositories, like some that come to mind that are, this is a search for all languages, it just happens to be Python's right at the top for all of them.

00:39:45 So TQDM, NumPy, iPython, SciPy, Notebook, Spyder, Volium, like all of these are Python.

00:39:53 I don't really understand how that's happening, but maybe it's maybe the algorithm.

00:39:57 Anyway, like you could go to any of these that inspire you and pull this up.

00:40:00 All right, so that's on the maintainer side.

00:40:02 It's like some things that you can do to help set it up, right, just like label things and so on.

00:40:06 And then on the community side, It says first, this is going to be on GitHub or GitLab.

00:40:11 You need to know Git, so take a moment and learn Git, because this is how you work on these things.

00:40:19 Able to just run the tools, if I'm going to help you build a house, I should know how hammers work, at least a little bit.

00:40:27 Then it says you can start taking a look at GitHub issues that maybe you've opened and see whether or not they're outdated, or you could close stuff that you've put out there in the burden.

00:40:37 and then go through that list like I talked about.

00:40:39 And yeah, then finally, there's like a celebration close boards.

00:40:44 So down here, you can see there's a overall, there's like a scoreboard type thing.

00:40:48 It says overall, there's of the 16,531 issues, NPRs 496 have been closed.

00:40:55 And then there's like a scoreboard of the closed issues by project.

00:40:59 So like Datalab is the number one and then Astropy is just right behind it.

00:41:05 SciPy is up there and it tails off from there.

00:41:08 So anyway, thanks Brian Skin for sending this in and people who want an angle to get into open source or want to contribute a little bit more, especially with some holiday time coming up, here's something you could do that might mix up what you're doing.

00:41:22 - Yeah, absolutely.

00:41:23 One of the things that I try to do as much as I can is try to advocate for people to get involved with sort of the small things.

00:41:33 And so I try to make, if somebody's gonna come on and write an issue, I say, well, great, you can make this PR, this is how you can go about and do it.

00:41:43 So as a maintainer, I think these types of, there was just one also in October, there was a Hacktoberfest.

00:41:54 - Yeah, Hacktoberfest, yeah.

00:41:55 - So I guess maybe something's coming in December.

00:41:57 - Hacktoberfest, I think is a little more about creating, like creating your first PR or making your first contribution.

00:42:03 this is more about like, I think, cleanup and closing out.

00:42:06 - Yeah.

00:42:07 - Yeah, so all the people from Hacktoberfest create a bunch of PRs and now they need closed.

00:42:12 - Yes, I participated in both.

00:42:13 There you go.

00:42:16 - One of the things that I wanted to point out is we did talk about the how to help maintain FastAPI.

00:42:23 So that would be all of, actually all the tips that I read on how to help maintain FastAPI apply to every open source project.

00:42:31 If the open-source project that you're interested doesn't have really good how to help tips, the FastAPI stuff applies to almost everything, like reproducing bugs, answering things.

00:42:42 Sometimes it's obvious from a pull request or an issue that nobody's really excited about this thing, and maybe it should just be closed.

00:42:51 That's helpful also is to just bring that up and say, "Hey, core maintainer people, this seems like it should be closed.

00:42:58 Should we go ahead and close that?" So actually on that point, I won't necessarily name names here, but there was a project that, not one that I'm involved, maintain, but it's a project that was talking about retiring a specific feature, right?

00:43:17 And it was sort of, you know, no one's really using it.

00:43:20 It doesn't really seem like it has very much activity.

00:43:22 And they just put a little notice up there.

00:43:24 And just by, because people were engaging in conversation and because people were looking and were willing to, you know, write a couple of lines or even in GitHub, where you go and you just click, you know, a little thumbs up or whatever, they saw all this interaction that people do care about this feature.

00:43:40 And, you know, it really does impact, you know, as a maintainer, if you, you know, the more people that are engaged in discussion, the better it is to decide, you know, sort of how to steer the ship.

00:43:52 - Yeah, absolutely.

00:43:53 Yeah, maybe it's just, hey, somebody suggested this.

00:43:56 I'm not sure what does the community think, right?

00:43:59 Having an opinion might be helpful, right?

00:44:01 - Yeah, yep, absolutely.

00:44:02 - All right, you know what else is helpful?

00:44:04 Cashews.

00:44:05 (laughing)

00:44:06 - Well, they're definitely delicious, but--

00:44:08 - They are.

00:44:09 - So this popped up in my, you know, you go into GitHub, there's the explore feed.

00:44:15 So it just was in the top of my feed.

00:44:17 And it really caught my eye just because this is the type of thing that I find myself building and rebuilding on every single project that I do.

00:44:26 So basically, at its core, what Cache uses, it calls itself an async Cache framework for a simple API to build fast and reliable applications.

00:44:37 And when you look at sort of what they're providing you out of the box, it's a very feature rich, but it's super simple to get it up and running.

00:44:48 I think you just really basically need one line to call a setup.

00:44:52 And after you do that, you're just adding decorators to stuff.

00:44:55 And I think this is really sort of, provides some really good foresight on how to build a very nice, clean API that can be used in a lot of different situations.

00:45:07 So on their GitHub readme, which I think is pretty well done, it gives you sort of how you might use this on a typical web application to cache some information on the request.

00:45:26 But you could really use it in a whole bunch of different features.

00:45:30 So a couple of different things that I kind of wanted to, that really struck me as really interesting.

00:45:34 Is number one, they provide support for doing in-memory caching.

00:45:40 Also Redis, which is very, very common.

00:45:43 And also a write to disk, which I believe uses SQLite.

00:45:48 - We talked about disk cache, which is, it looks like the foundational thing probably for the disk version of that caching.

00:45:57 And also, dill.

00:45:58 Instead of pickling, you dill things.

00:46:00 So you can store more, a wider variety of items into your cache, which is kinda cool.

00:46:07 I'm not familiar with dill, but it sounds like it's probably good.

00:46:10 - Yeah, I don't know how much, you know, you combine dill and cache use on a normal basis, but I guess it could be done.

00:46:17 No, but so one of the things that I think is really neat that they built into this is there's a cache on top of a cache.

00:46:24 And what I mean is, you know, let's say you're putting all this information, these really expensive operations into Redis or disk cache or something like that.

00:46:32 They also have what it looks like is maybe an in-application memory cache where you don't even necessarily need to go do those network calls every single time that you want to go fetch data.

00:46:46 And I feel like sort of, you know, there's sort of like that old saying that, in, you know, computer science, there's, you know, there's two hard things in computer science.

00:46:54 There's cache and validation, naming things, and off by one errors, right?

00:47:00 - Exactly.

00:47:01 - So I feel like they sort of, like, are solving some of these problems, and they've got a couple of really simple ways that you can do cache and validation, you know, ways that you can, It just, it really strikes me as a very well thought out package.

00:47:18 But one of my favorite things that I noticed is one of the ways that you can invalidate a cache is by rate limiting.

00:47:25 Well, rate limiting is itself a huge area, especially for web applications.

00:47:32 And if you use a package like caches, you're getting two different requirements for one right here, because it can do double duty for you.

00:47:43 So I think this is, I haven't used this yet, but it looks super clean.

00:47:48 It looks like a very nice, very intuitive, and I'm pretty excited to try this one out for sure.

00:47:53 - What an interesting kind of negative cache this rate limit thing is.

00:47:58 So the idea is, if you call it, you can put it onto a function.

00:48:02 So if you call this function more than 10 times in a minute, is the example there, then you basically get banned from calling it for a while.

00:48:12 So instead of saying, we're gonna scale up by saving the answers to the questions you're asking to this function, we're gonna save performance and CPU availability and whatnot by only allowing you to call too much.

00:48:25 And if you do it too much, you're done, you're out.

00:48:28 Similar with circuit breakers for errors.

00:48:29 If there's too many errors, it's just gonna stop for a while.

00:48:32 - Yeah, exactly.

00:48:33 And there's also this, I kind of glossed over it, But one of the things that they did for cache invalidation is there's sort of this, because it's using async Ion to the hood, it looks like it's got this ability to sort of refresh your cache automatically.

00:48:52 So one of the things that you often have problems with caches is, you might have stale data in there that you want, how do you get rid of that stale data?

00:49:02 And so you can basically set up, it looks like in the background, it's called early refresh or something like that.

00:49:10 And in the example that they give you, if you've sort of called this within the given time period, it'll automatically go and sort of refresh it for you in the background, which I think is really cool.

00:49:25 - Yeah, okay, so this one says, I want the cache time to be 10 minutes, but if it gets called on minute seven to nine in terms of the age of the cache result, go ahead and recompute it so that in the background, right?

00:49:40 Give them the answer that's cache back, but then actually call it so that you, 'cause if it takes 30 seconds to compute this thing or whatever, right?

00:49:47 It takes a long time, every now and then there's gonna be those gaps where it expired and you hit it again, right?

00:49:53 And so here's a way to kind of preempt that so nobody sees the slow version.

00:49:57 There's a lot of interesting ideas here.

00:49:59 Yeah, way to go Cacheus, that's cool.

00:50:01 - That's pretty cool. - Krukov, yeah.

00:50:03 Yeah, very cool.

00:50:03 Awesome, well, good find Adam.

00:50:05 Brian, how about our extras?

00:50:07 - Yeah, how about them?

00:50:08 I don't have anything extra.

00:50:09 Do you have something?

00:50:11 - Let's go to Adam.

00:50:12 Adam, anything else you wanna give a shout out to while you're here?

00:50:14 - Sure, I just noticed that definitely voting season is here.

00:50:19 There was just a big vote in the US.

00:50:22 I live in Israel, we just had election season here, but now we've got Python elections coming up.

00:50:27 So nominations for the Python Steering Council are open.

00:50:31 I think the way that it works is that you have to be a core member to do a nomination, but anybody that wants to can go on to their discourse.

00:50:40 And if there's a candidate that you support, you can reply to the comments, you can engage in the conversation.

00:50:47 And I think that's really cool and really, super way for people to sort of engage with the larger community.

00:50:55 - Yeah, very nice.

00:50:56 And I actually have something related to that.

00:50:59 Where is it?

00:50:59 It's hiding.

00:51:00 The, I have to pull out of my notes, maybe I didn't pull up, But the PSF survey, oh yeah, here it is.

00:51:06 It's just there.

00:51:07 David Lord put this out here.

00:51:09 Speaking of web frameworks, we've covered them a lot.

00:51:11 Let's bring Flask into it as well.

00:51:13 So over here on Mastodon, David says, "Take the PSF developer survey.

00:51:17 "It's closing in a few days." That was yesterday.

00:51:21 So people should go and do that if they haven't.

00:51:24 Pretty sure I already did.

00:51:25 I don't wanna vote twice, but I also don't wanna not vote.

00:51:27 It's a dilemma.

00:51:29 So anyway, it's really great that David put that out there.

00:51:31 So another thing is not quite voting, but it's, you know, tallying your opinion there.

00:51:37 All right, I got a couple other things.

00:51:38 Also quick, you know, just a shout out to your book, while you're here, "Python Web Development with Sanic." People can check that out as well.

00:51:45 So excellent.

00:51:47 Let's see, this one, no, that one is just a joke.

00:51:50 So I think actually, Brian, that's all I got for extras.

00:51:53 So you ready for a joke?

00:51:55 - I am.

00:51:56 - All right, over here.

00:51:57 Again, I wish I could pull these up separately.

00:51:59 I have to log out, but then I can show you the other stuff.

00:52:01 And by the way, Samuel Colvin just showed up on Mastodon as well.

00:52:05 He wasn't there yet, so people can go, of gigantic fame.

00:52:08 So when all this stuff with Twitter came out, I thought this was a pretty hilarious, you remember there was the switch of what did it mean for the blue mark, the blue check mark to be on an account.

00:52:19 It used to mean that you were verified and there was lots of rules about like showing your ID and having a Wikipedia page and there's like rules to get that check mark.

00:52:27 And then Elon said, well, we could just pay for that.

00:52:29 A bunch of people started impersonating people and doing all sorts of funny shenanigans.

00:52:34 Well, this is breaking here.

00:52:36 We've just noticed on Twitter that the JavaScript verified account that it's the program, the Twitter name is Real Programming Language with 51 million followers.

00:52:47 And there's a big message on it, Brian.

00:52:50 What's the message say?

00:52:51 - It's been canceled.

00:52:53 - Suspended, account suspended.

00:52:55 Twitter suspends accounts that violate the Twitter rules, JavaScript has been banned from Twitter for impersonating a real programming language.

00:53:02 (Adam laughs)

00:53:03 I love it.

00:53:04 - That's funny.

00:53:07 - Yeah, it's pretty good.

00:53:08 All right, well, that's what I got for you this week in terms of jokes.

00:53:12 JavaScript has been suspended on Twitter.

00:53:14 - You know, and I just, speaking of Twitter, just if you want some humorous news, just Googling Twitter on Google News is hilarious.

00:53:22 Just, I mean, it's also sad, but also funny.

00:53:26 - Yeah, absolutely.

00:53:27 Well, Adam, thanks for joining us this week and congrats on Sanic.

00:53:31 It looks like it's been going strong for a long time and it's got quite the community there.

00:53:34 - Thanks for having me.

00:53:35 Yeah, we've been going strong since 2016 or so.

00:53:40 - Wow, that's awesome.

00:53:41 All right, Brian, thanks everyone.

