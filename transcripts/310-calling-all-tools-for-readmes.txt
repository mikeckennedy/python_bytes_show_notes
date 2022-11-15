0:00 Michael Kennedy  00:00

0:00 Hello, and welcome to python bytes where we deliver Python news and headlines directly to your earbuds. This is Episode 310, recorded November 15 2022. I'm Michael Kennedy.

0:00 Unknown Speaker  00:10

0:00 And I am Brian Aachen.

0:00 Unknown Speaker  00:12

0:00 And I'm Adam Hopkins.

0:00 Michael Kennedy  00:13

0:00 Welcome, Adam. Great to have you here.

0:00 Unknown Speaker  00:15

0:00 Awesome. Thank you. I'm really excited to be here.

0:00 Michael Kennedy  00:17

0:00 Yeah. People mostly know you, I would imagine through Sanic, your web framework and tell people?

0:00 Unknown Speaker  00:22

0:00 Yeah, that's correct. Well, first, I just, I just noticed episode 310. So two more episodes, and you guys pass the Python version. So Congratulation. Thank you. So that's a milestone.

0:00 Michael Kennedy  00:35

0:00 Six years, we just passed six years.

0:00 Unknown Speaker  00:38

0:00 Yeah, that's exciting. I remember when you guys started it. So this is this is a great resource for the community. Cool. So just introduce myself. I'm Adam Hopkins, I am one of the developers of the Sanic. Project. My day to day job. I'm director of software engineering for packet fabric, where we, you know, day in day out, I do web development. So that's, that's my gig

0:00 Michael Kennedy  01:02

0:00 on bone stuff. It sounds like Yeah, absolutely. Cool. Yeah. Well, Brian, you want to kick us off with our first topic here?

0:00 Brian Okken  01:10

0:00 Yeah, sure. So this is a bit of an easy topic, tips for clean code in Python. I was this is from Bob Beltre boss from pi bytes. I was playing with his dark mode on and off, it's kind of fun. Anyway.

0:00 Unknown Speaker  01:26

0:00 Dark Mode is always appreciated

0:00 Brian Okken  01:28

0:00 my book, yes. Well, so I, I, this resonated with me. So I'm gonna blast through the tips really, pretty quickly. They're just good things to think about, I think it's good occasionally to remind yourself of when you're organizing your code. So using smaller units, I'm going to come back to this but essentially, it's thinking about if you've got huge functions that do a whole bunch of stuff, maybe breaking it up. Like I said, I'm gonna come back to that a little bit. magic numbers are always good constants are better than just numbers sitting in your, in your, in your file somewhere. You know, I'm kind of on the fence on the Void is avoid global scopes. The third, but there's nothing really global in Python, it's module level. But still, if you've got large files, global scope can still be confusing. So watch that. Using winters and narrowing your is good thing. I'm not actually I'm not going to run out through through the, through all the tips, there's some good tips here. So go ahead and read the article. But the thing I wanted to come back to is just this one, this first one smaller, smaller units, because I just ran into this. So I'm, I'm working on refactoring the PI test check plugin. And currently it was, it's just all in one, I mean, most of the code was in two files, like the basic plugin hookup, and then all of the rest of the code. And people have added a couple other people have added features. And that's a good thing. But I have had my I had a hard time keeping my head around all the code in there. And it was confusing myself. So I, I've been working on splitting it up. So I split up all the code into it. And I split it up into this, this, this notion of the single responsibility principle, I thought about the, the this plugin as the features. And it's either large features that kind of take up their home there enough to be their own module, or some related features that are kind of all together. And I've split up the code into different modules about those sorts of pieces. And the the nice thing about that is I've also done the stuff that with the tests, I've split the test up into focusing on a feature at a time. So the tests are in multiple tests. So it's a lot more files now. But each little piece is just a few windows for full of code. So it's pretty easy to keep get your head around, oh, for this feature, all of these things work together. And it's really been great to, to work with now. So I haven't published the the final yet. But the smaller units thing, people do talk about large functions, and that's something to watch out for. But large files are a thing to keep in mind too. And sometimes, sometimes breaking it up can go too far too, if you got like, like 100 different modules that are all are like 10 lines long. That's, that's too far. But you know, so I really

0:00 Michael Kennedy  04:16

0:00 liked the idea of smaller units in both files, and for like functions for classes or whatever. And one of the ways that I think about it is if I'm looking at a chunk of code, maybe like an inner part of a looper or some other thing, and like, oh, I should probably put a comment to describe what that does. Alternatively, I can make it a small function and give it a name that tells you what it does, right? Like, if it's, you know, update, last login for user, that could be a comment or that you could highlight those five lines of code Extract Method and give it that name, right. Like it just there's sort of a natural if I'm looking at it, and I don't understand it, how can I how can I make it easier to understand like that's, that's a really productive way to do it, I think.

0:00 Brian Okken  04:56

0:00 Yep. Especially if that bit of code really isn't the focus of the folks Soon, it's just some other stuff that has to be done. Moving it out of the function proper is, is good. And then the function name. Yeah, just name it something clever.

0:00 Unknown Speaker  05:09

0:00 I think one of the things you you also really kind of hit on there is, is breaking up the test files too. Right? And so I'm kind of curious to hear, like, you know, typically, for maybe for a smaller package, I mean, do you try to keep sort of one test file for one module and keep a module? Or, you know, sometimes I feel like when I've done that, even even trying to iterate and all the different things that I might want to test in one file, it could still end up being, you know, a couple 1000 lines long,

0:00 Brian Okken  05:37

0:00 I'm, I'm focusing on features. So trying to keep the like, for instance, the one of the functionalities for PI test check is is stop on fail working at work correctly, because you possibly could have multiple failures in in a single test. So how to stop on fail work? Well, there's a is there's a defined way, we've defined it for the plugin. And so I've got like one test file that tests the stop on fail functionality. So I prefer breaking it up into user functionality instead of modules, internal modules, but

0:00 Michael Kennedy  06:14

0:00 Right. Oh, good tips, Bob. And nice find Brian, one.

0:00 Unknown Speaker  06:17

0:00 One thing also, I noticed that was in this article that I'm probably going to touch on in a little bit is sort of that idea of the global scope, because because that's definitely something that that I think, can actually cause caused some problems down the road. I'll touch on them a little bit.

0:00 Michael Kennedy  06:33

0:00 Awesome. Yeah, absolutely. There's also a lot of tips in here that can be automated. You should write code that matches this kind of stuff already. But in running the linters running Black is using Yeah, pre commit. One of them is using idiomatic code, which you could use Flint, we talked about a bunch of things that like upgrade to python two to three pi upgrade, I think, yeah, those types of things like you could a lot of this stuff could be brought in on the on the toolchain level too, which is kind of nice. Yeah. All right. Let's talk about mastodon. So I don't know if y'all have heard Twitter's kind of going nuts right now. It seemed like a place that was just gonna be around forever. But apparently, maybe no. And so Brian, I think you maybe encouraged me to go over to Mastodon and check it out a little bit last time. And

0:00 Brian Okken  07:24

0:00 so it was just like a week ago, man, like just went crazy.

0:00 Michael Kennedy  07:27

0:00 I have gone crazy, I'm telling you. But I think there's a lot of cool stuff over here. So I'm super psyched about it. I just did a talk Python episode. But I'll put the link that in a moment. But what I found, so you kind of encouraged me to go over there. And I did. And what I found was there's a whole bunch of the people that we know and have been interacting with over on Twitter. Now. They're all over on Mastodon, and it's a super nice, active community. I expected to kind of show up there and go like, well, I'll wait till people show up. But they're there. They're already there. They're already there. And like, Adam, I saw that you're over there. And Brian, obviously you are. And I got the shows going over there. And so people can follow Python bytes on Mastodon, they can follow Python all I'll put a link to all the various all of our profiles, including Adams over there in the show notes.

0:00 Brian Okken  08:15

0:00 And we're all kind of learning at the same time. So even the you show up and they've already got hundreds of friends there. But they're like, they're still learning also. So

0:00 Michael Kennedy  08:24

0:00 yeah, yeah. Yeah, absolutely. They are. So Mark, go out. Go ahead. Go ahead. Go ahead.

0:00 Unknown Speaker  08:30

0:00 I'm just gonna say it does, it does sort of, kind of bring up an interesting question that I've sort of been, you know, feeling is, you know, are people starting to share in two different places now, you're trying to have conversations multiple ways. And so there is a little bit of an awkward in it, maybe, you know, what kind of just, you know, trudge through it and see how it works. But I definitely agree that it's, it's, it feels very, feels clean, like, it just feels like very, you know, fresh, maybe it's just because it's a, you know, a new app to play with, or one I don't know, but there's, I agree, it's, I'm very happy to see that, you know, people that I'm already, you know, subscribed to, and trying to try to see what they have to say are already there. And it's definitely interesting to see. See how this develops? Because I think it's, it can only be positive.

0:00 Michael Kennedy  09:15

0:00 Yeah, I totally agree. My philosophy is kind of for the moment to be massive on first not to burn down my Twitter account or to leave my community over there. But just like, Twitter looks like it's trying to kill itself. Let me try to put some energy over here. And after Brian kind of got me moving and looking at masked on it, it lines up way better with the ideology of open source and Python communities having this federated different bunch of servers, people can control them. They're open source, there's not one central choke point for it or whatever. But yeah, I think I think it's really interesting and I encourage people to check it out. I was gonna highlight that Marco on the audience said, me two weeks ago is Macedon good enough to replace Twitter? Me now? Is Twitter good enough to have a replacement for Master Um, yeah, I'm, I'm kind of the same way. So I got a bunch of stuff I want to share real quick with you. So I'll go through it quickly. That is not gonna go into my order. So I did a really cool episode with Gina Houska, while Luis Simon Willison and I gotta update my show notes because she dropped in last minute and Carol willing as well. So people can check that out the these different places, you should really support them these little instances. Like, for example, the one that Brian and I are on is FastAPI, fostered on the free and open source software instance, it went from 2000 to 40, something 1000 users in a week, and their hosting cost went from 100 to $1,000. And the same period, which is a lot and it's just volunteer, right, that's a lot to be paying, but they have a Patreon, which is really nice. You go to their Patreon, you can sponsor them, you can also do that for Macedon, if you look at they have a sort of a statement breakdown of like, here's how much we spend on hosting and how much we spend on CDN and bid war and and all these different things and how it breaks down. It turns out brain 2.5 cents per user will fund Macedon. So wow, I feel like I feel like we should be doing this. Like we can all spare 2.5 cents or maybe $1. Not everybody. And if you can't really please don't. But most people who are software developers can surely do that. Put it another way out of those 40,000 people, if just 100 of them pay $10 a month that will also fund Macedon. So it's very achievable, that we could end up in a world that is not ad written tracker written surveillance capitalism is trying to trick us or manipulate us and to do things, but these really nice open places that we can move around as our values match, you know? Yeah,

0:00 Unknown Speaker  11:42

0:00 I think the other side of it too, is, you know, we need to make sure that the people who are the content creators, people that are that have, you know, large followers in our in our putting out information that people want to read, you know, make sure that they're there that they're supporting this as well, because you know, where the content is. That's where the people will go. Yeah. So hopefully, hopefully, we can get more people, people paying for it and supporting it. Yeah, I'm

0:00 Michael Kennedy  12:02

0:00 doing it myself. And I definitely encourage people who can, because it's, it's fantastic. Alright, what else did I want to cover about this? It's open source. It's Ruby, which is not the most amazing open source for Python people. But it is open source, which is very cool. You can go get it. There's a Python package called tuite. There's also a CLI you call it you cover it we covered a little bit last time prior. And I said I'd go into it more, I think yeah. So one of the things I did come back to that one of the things I did on one thing, that's annoying, if you log in, it's really hard to pull up an individual tweet on your own instance without like it being in the show here. But one of the things I did Saturday morning, Brian, do you see the third button from the second row? My stream deck here? Okay, so I wrote an A, I integrated the Macedon API into my stream deck. So now whenever we start a show, I just push that button, and off it goes. Nice. I think actually, I might have pushed the one for talk Python this time, because they're their same screen, just slightly different. But anyway, we push that button and it'll kick it off. And that'll just post a toot. I guess we would say,

0:00 Unknown Speaker  13:08

0:00 okay, get over that. It's funny.

0:00 Michael Kennedy  13:12

0:00 All right. And then finally, finally, one thing that's really nice is if you have a chrome based browser, like Vivaldi are one of those are brave, you can right click on the tab and state say install mine says install fostered on because I was on Fosston on but if you were on, you know, Macedon social or whatever it's called it would say install that. And then you get a progressive web app. That is, I would say probably the best app on the desktop for doing Macedon UI got hot. He's all sorts of fun stuff. Lots of you can do like the advanced view with columns and all of these things. So I encourage Ya, so I encourage people to check this out. One more thing on tuite. We'll come back to close vember in a little bit. Maybe this is relevant here. But this is a library Python package that you can use to talk to Macedon. I have no idea how to use it. It's completely opaque. It's like star star, star, star star, kW args callable or you just there's it doesn't have any structure. It's all the run done up at runtime, you can't tell like what are the functions, even if you do it, like it doesn't have any functions or anything you can call. So how is used I have no idea. It's it's it's hard to use. But the one thing you can do is it has a CLI that will generate your OAuth login tokens. And then you just use that directly with requests or ACP X or something. So too, as far as I can tell, it's not particularly useful until some sort of example is written. Even the tests don't seem to help very much. But what it does do is it'll generate your access tokens that they can use in the rest of your code, which is pretty cool. Okay, yeah. Nice. All right. Yeah. Well, people definitely should check that out. Adam, you're up next.

0:00 Unknown Speaker  14:49

0:00 All right. So I guess, you know, a little bit of a backstory to you know, a couple episodes. You you were talking about an article that I that I posted on my blog about this new feature. They've been invaded and bred into Sanic. About a month ago. And I, well, I was on Twitter at the time, but I sent a tweet to you kind of with a little bit of a correction. And so I guess that's kind of why I'm here is I just wanted to kind of clear up a little bit. The the feature that that we added into Sanik is this worker manager. And the idea covered in the blog article is sort of what an implementation of that might look like. So so really, kind of what what the what the article was trying to cover was how to build a salary like clone,

0:00 Michael Kennedy  15:36

0:00 and take a step back really quick and just have the elevator pitch for Sanic, just for people that maybe haven't used it.

0:00 Unknown Speaker  15:42

0:00 Sure. So Sanic is, it's an async. framework, web framework for building web applications. One of the things that it comes with is a built in web server as well. So it's both a web server and, and a framework. So it does both port parts,

0:00 Michael Kennedy  16:02

0:00 your native micro whiskey or G unicorn or something along those lines,

0:00 Unknown Speaker  16:05

0:00 correct, you can use something like unicorn if you wanted to. So it can operate as an ASG AI app. So that is a possibility. But generally, I find that most people that you send, it will will use the integrated Sanic server because it's sort of built, you know, for high performance, it's it's, you know, optimized to work with the with the framework, the framework itself is generally very unopinionated and sort of tries to get out of your way and provide you with the tools they need to build an application but not dictate specific patterns. So that's, that's the sort of the short and long, long pitch of it. Last year, I put a put together book on on sort of different patterns and how you might build production applications in it with Sanic. And sort of what a, you know, what are some of the possibilities that are sort of outside the scope of just these documents here. So specifically, one of the things that we kind of had noticed, and really drove us to, to what ultimately became the worker manager, that feature is that, you know, Santa comes out of the box with, you know, auto reload, the ability to scale up multiple workers, all that kind of stuff that you would sort of expect. But you might in older, older versions, you might have a different experience, when you're doing development versus when you're in production mode. And so we wanted to kind of get rid of that. So that every single time that you, you, you boot up Sanic, whether you're in whether we're your local localhost, or you're deploying it, you get the same experience, you've got one process whose whole job is to sort of manage the whole show. And then one or more of these worker processes that can be can be individual servers. And the idea, once we have that, it really provide provide us the ability to take that abstract abstraction and turn it into something a little bit more and, and allow individuals to inject arbitrary processes into it. So the example in the article was this set here, like, worker manager, but you know, one of the other big use cases that we see a lot with FANUC are people that are trying to build chat bots, you know, maybe something for discord or something like that. So this would really make it very simple for you to to run both a web application and a chat bot, all from one process and have it all managed, without having to scale multiple, multiple instances.

0:00 Michael Kennedy  18:42

0:00 Yeah, yeah. So does it when you run these worker processes, can it run? And Did it run in a background thread, or one of the things when I first talked about this that was a little unclear to me is, you know, once you have when you go into production, you farm out to a bunch of worker processes, typically, right? You say like, we're gonna run four worker processes, and they're all going to, you know, round robin handle these requests. But yes, how does that how does that management correlate back to these worker processes, because if they all are kind of managing their own, then you're going to end up with, you know, a whole bunch of them.

0:00 Unknown Speaker  19:16

0:00 Correct. So, so when you start up the application, and this actually, is the whole reason, going back to Brian's thing from earlier about, trying to keep things out of the global scope, and why I encourage people to do that is, is under the hood, you know, we're using the multi processing from the standard library. So it's, it's, it's very easy to make some mistakes. And and if you've got some code that is kind of sitting in the global scope, you might accidentally run it and all these different work processes that you don't necessarily want it to. So trying to keep your abstractions nice and tight and keeping everything's instead of functions and call bowls. Kind of avoids that. So to answer sort of your your question is when you start out per worker process, you know, it's there's two kinds, right? There's the processes that are meant for for Sanic servers, and then for anything else that you might want. Third reloader is going to be one we also have in the extensions, we also provide out of the box a inspect utility. So it basically would give you a CLI command line utility that you can sort of check the status of any operating worker. So you can see you know, how many things are running, that's cool. If you want it to sort of see you know, how many requests are on each of the workers, you can kind of get that information.

0:00 Michael Kennedy  20:38

0:00 That's, that's hard to tell and production, and you're like, it's kind of slow. And this one seems stuck. But I don't know, what the heck's going on.

0:00 Unknown Speaker  20:44

0:00 Absolutely. And this is really sort of the thing that this has opened up, because what happens, and for anyone that's ever done, anything that's using multiple processes in Python, one of the things that that the package does provide you is these different primitives where you can short share state between them. And in older versions of, of Sanic, there was no way that you can do that. But one of the things that we now have is you could have say, one queue object, and every single one of your workers is able to push and pull information from that queue. You know, you can have, you know, shared counters, and it really kind of gives you a lot more flexibility that just didn't exist before. Cool.

0:00 Michael Kennedy  21:31

0:00 Well, looks fantastic. And the other thing that you put in here is cashews. What What's the house cashews related back to this,

0:00 Unknown Speaker  21:38

0:00 it's not related back to this at all. This is just like a topic, right? Yeah.

0:00 Michael Kennedy  21:43

0:00 Okay, sorry, I put in the wrong order, then we'll we'll come back to that with it. Sorry. Okay. Awesome. All right. Well, this is really cool. And it's something that a lot of web frameworks don't have is this ability to richly manage stuff that shouldn't be processed during a web request. And a lot of times people end up running whole different servers, you know, Redis, plus celery, or something fairly complicated. So this is really cool that it's kind of like tightly tied together there.

0:00 Unknown Speaker  22:06

0:00 So when actually kind of use case, that that just just kind of give people a little bit of understanding of how you might actually use this in production. So So I use celery very heavily, as well as Sanic. One of the things that anyone that's used celery knows about is there's this function, this service called celery beet. And basically the idea there is you're sort of scheduling these cron, like jobs that are going to run periodically over some defined schedule. Well, when you put all these things into, you know, Kubernetes applications, you know, containers, your DevOps guys come knocking on the door and say, How do I know that this thing is still running? Like, I want to be able to ping this and make sure that things haven't died. And so that, like Kubernetes, that's sort of the one of the things that it does for you, right is it kind of checks the health of your applications and kind of restarts things. And it's very simple to do from a web application, not so easy to do from a service like celery beet. So what we did is, we built celery B into A Sanic worker process like this. So basically, what it does is it's kicking off these jobs every, say, every 10 seconds some period, and it's sending a ping, HTTP ping over to the to the Sanic service that's running it. And then we can keep the state there. And then it's super simple for Kubernetes at that point to sort of see what's the health of this application? And is it still running?

0:00 Michael Kennedy  23:33

0:00 Yeah, very cool. That's that's a really interesting use. Awesome. All right, Brian, we're talking about our sponsor this week. Yeah, let's Awesome. Well, this week, once again, we have back Microsoft, such great supporters of the show. And if you've not yet checked out Microsoft, for startups, founders hub, you definitely should, as we all know, starting a business is hard. They provide a bunch of support, both in financial grants for compute and other cloud services, as well as access to a mentorship network and other types of advice, basically, and connections. So it's a free service, all you have to do is apply. You don't have to be third party validated. You don't have to be VC backed, you just apply it and once you're in, you're in. And unlike the requirements, I go live in San Francisco, Silicon Valley in New York City, one of these places where there's a community of founders and mentors and experts, you get access to a similar network from wherever you are. So it's not about who you know, but or who you have access to, because you can use their network so they give you access to hundreds of mentors across a range of disciplines like idea validation, fundraising, management and coaching, sales and marketing and a whole bunch of specific technical stress points. And you'll be able to book a one on one meeting with these mentors, many of whom are former founders themselves, and it'll really give you a leg up making connections. and keeping your your company on the right track. In addition to that, you get a bunch of Microsoft Cloud Credits a bunch of GitHub credits, they partnered with open AI, a global leader in AI research and development to provide exclusive benefits there as well. To make your idea a reality with the critical support you'll get from Microsoft for startups join a join, just visit Python bisetta FM slash founders hub 2022. The link is in your show notes. So as always, thanks to Microsoft for supporting the show. Yes, thanks. Hi, Brian. What's next?

0:00 Brian Okken  25:31

0:00 Well, I wanted to touch on fast API a little bit. And specifically, there was some there was a new release that caught my attention. So zero, point 87.0. It's kind of cool. We should bug them about being zero versatil. But I said, Yeah, come on. It's it's definitely production ready by now. So anyway, well, so what I wanted to talk about is some of the some of the interesting bits here, which I thought was really kind of cool of Sebastian and others to handle. So one of the things is they upgraded to starlet and I think it's starlet 0.2 or something. Anyway, I'm not sure which version of starlight but the the starlet version, they changed to have a test client update and updated from a from from requests to HTTP X. And that's pretty interesting. So fast API gets that also. But what happens with that is the the test client actually had some breaking changes with it. And somebody's name, codecs said, or just to set decided to create a tool called Bump, bump test client. And this is pretty cool. Because the idea is you've got some test code already. That depends on test client. And you can, you can run this bump test client on your test code, and it upgrades it to the new interface. cool is that that's just pretty That is cool. Yeah, nice extra bit of upgrade help for people. The other thing I wanted to point out is, is that there's a lot of documentation changes. So there's one of the things he added was a help maintain fast API, I say he but I think there's a lot of people working on fast API now. So I'm not sure who added it, but helped maintain. And, and I think this is really pretty great. Because see if I can find it. Yeah. It's focusing on like this section of how helped maintain it focuses on a couple of things that people don't think is very glamorous, but is hugely helpful for open source projects. And that's helping with the issues. Because a lot of a lot of issues are really just questions or a user doesn't understand how to use it, or they're using it in a weird way. And it's just a knowledge gap thing. So helping those people out great help for the maintainer. So they can focus on building new features, also kind of helps to point out maybe that there's documentation holes. The other bit is a poll reviewing pull requests. And both of the both of these topics have helped pop into bigger sections. So like the helping with GitHub issues, talk about how to do that. So there's some documentation on how to help like, understand the question that somebody is asking, and maybe maybe change the question, if it's not clear, trying to reproduce other people's problems, suggesting solutions, you know, if you think that it's been solved by somebody if it's solved, but it's still open, ask if you can close it, these sorts of this sort of help, especially with large projects helps a ton. And so I think it's cool to that this has been focused on. The other thing I wanted to point out, which I thought was cool was we covered rough earlier on one of the other episodes, and it's a rust based linter. But fast API is now using it internally to link to their fast API code. So that's kind of fun. Yes. The now one of the reasons why I was looking at this is coming back to the little project pi test check that I'm working on. I'm refactoring it. I also thought the readme is lame. So I was looking at the the the fast API readme, which is pretty interesting. The one of the so I'm looking at different READMEs to see if that getting inspiration from others. And the fast API readme is an interesting thing that I don't think I've seen in very many other open source projects. There's the there's a logo, of course, and then some links to documentation and source code, which actually I think are really handy to have right there at the top of the readme. And then some features of why key features why you'd want might want to use it, but it really feels like a sales page also somewhat, but the the, the sponsor list is interesting. It directs right to some of the direct sponsors of the project and having sponsors that actually show up in the readme and look Tech Talk Python trainings there too. So go Michael But the the, that's an interesting way to, you know, pay for large open source projects, kind of cool idea. And then, you know, opinions like, you know, people that liked it and references, this still free feels like a single page before it gets into the meat of the normal stuff that you kind of see in a readme. It's like a sales pitch page or a single single page, landing page. And kind of maybe that's what a readme should maybe be to try to encourage people to use it. I mean, we're not buying a product, but we we do gain. It is growing a project if more people use it, so selling them on the project. It's kind of a cool,

0:00 Michael Kennedy  30:36

0:00 I do. Yeah. I think that's great. A couple of thoughts I have here. Okay, one just on the sponsor thing. That's one of the reasons it's really appealing to sponsor fast API is the visibility that you actually it's not much, it's not much that get a link back to your site, but it's a little bit in it's better than just a good feeling of well, I paid to support this project and maybe buried in the contributors.md. Somewhere, there's like my company name, but no, it's like a little bit of give back. And you know, we get it, we get some traffic from that. And it's, it's really nice. And I think it's one of the things that other projects could do that have decent sponsorships is just to give a little visibility back like that. I think it's working really well for Sebastian, because you can see, I'm not the only one up there and my company.

0:00 Brian Okken  31:23

0:00 And then there's some of these listed here. But then if you go to the documentation page, it has like even even more sponsors.

0:00 Michael Kennedy  31:30

0:00 Right, exactly. Those are gold sponsors. That could picture then, too, I'd like to hear Adams thoughts about sort of marketing your, your web project and presenting it in this way. Because Masonic, you're in a pretty parallel situation.

0:00 Unknown Speaker  31:47

0:00 Yeah, I mean, absolutely do. I agree, 100%, it's definitely a sales pitch. And to your point about, you know, you're not necessarily buying anything, but you're you're buying into it, right, you're you're buying into the project is, you know, you're you're the it is you're starting to build something, and so you're going to be putting a lot of investment into that. So, you know, I think it's sort of, you know, especially with with some some types of projects, it's a little bit more important than others, if you need to specifically kind of buy into a specific philosophy and how to, you're going to be building something with it. So So absolutely. You know, we have, do something a little bit similar, you know, trying to try and make sure that, you know, sponsors have a little bit, you know, have some visibility, as well. So I think, but, and this is actually one of my pet peeve is one of the in my opinion, one of the most important things you touched on is putting those links up at the very top, you said that, you know, there's got to, there's a link to the source code, and the documentation and this the source code, I feel like, is the one that's almost always missing, you know, usually, these READMEs don't just show up on GitHub, right, they show up on pi pi.org. You know, maybe they show up in, you know, the, you know, read the docs, if it's getting, if it's, you know, that's where it's going to, and it drives me nuts when I land on some sort of documentation website or something like that. And I can't get back to the source code, you know, the that so so I love to see that that right up front, you know, that

0:00 Michael Kennedy  33:23

0:00 you go and say, like, edit the documentation in GitHub so that you can navigate back up the tree? Like, that's probably my easiest way back. Right. That's what

0:00 Unknown Speaker  33:31

0:00 I do in exactly the end up on some page, you know, 1010 levels deep inside of the project. And that's not where you want to go.

0:00 Brian Okken  33:38

0:00 Yeah, so Sanic looks like you got it right there. The source code. Also, many of the a lot of people don't know this, but a lot of a lot of on pi pi, the homepage, often links to the GitHub repo, it doesn't have to people can link it to whatever they want to but this this often links to the source code. But yeah, the source code right there on Sanic. It's pretty good. Hey, you got some sponsors to me.

0:00 Unknown Speaker  34:01

0:00 Yeah, I'll see you the SEC, the images and load in there. So maybe I need to look into that, but

0:00 Brian Okken  34:06

0:00 Well, I think it loads on on the GitHub thing, but okay, that's good. But what, while we're looking at READMEs? The I did want to also mention, will because you know, we have to? Well, Tuesday, yeah. So one of the cool things that he's gotten

0:00 Unknown Speaker  34:24

0:00 Macedon yet.

0:00 Michael Kennedy  34:26

0:00 Yeah, yes, yeah. Okay, so

0:00 Brian Okken  34:28

0:00 on both rich and textual, there's a feature in there READMEs of these dropdowns. So you can, you can like, open up a section that maybe like like this, the rich library talking about different ones, it would be kind of overwhelming to have the whole thing listed here. But having them collapsed is kind of a neat idea with little things. So and one of the great things about READMEs is I don't know how he does this, but I can go find out because it's all in open source. I can just look at the readme code and and see how it's done.

0:00 Unknown Speaker  34:57

0:00 I believe Yeah, I believe it's a it's a GitHub specific thing. So I'd be curious actually to see how that might carry over to like pipeline that org or something like that.

0:00 Brian Okken  35:06

0:00 Well look, see works. So yeah, bear with us we're looking at to see if the dropdowns work on pi pi. And they seem to so Oh, neat. Amazing.

0:00 Michael Kennedy  35:17

0:00 It's a, it's a tui embedded in a Webby.

0:00 Brian Okken  35:21

0:00 And I have seen this other places, too. I think. I can't remember where but there's a couple of open source projects that use these dropdowns. And I've seen so that's probably enough on this topic.

0:00 Michael Kennedy  35:34

0:00 No, it's not Brian. No, it's not. No, it's not okay. Let me just, I just want to put out a call to people because I tried this on the social medias. And it didn't really get me far. And maybe it's just gonna go nowhere. I want to do a talk Python episode on awesome tools for managing your readme and your change log. And like, release notes and stuff, I think that'd be fantastic. I know, there's things like release drafter, and others, but none of them are big enough to be their own show. So I want to do like a set of like, here's a bunch of cool tools that you can do. So people are using some, please just tweet them to me, shoot them to me, email them to us, however you want to give them to me, that's fine. But it'd be really helpful if I could find you know, 510 of these things. And then we could do a really cool show about like, how to automate and do a bunch of these cool things. Cool. Well, I

0:00 Unknown Speaker  36:19

0:00 was just talking about we got here. Oh, definitely send you a couple ideas. Awesome.

0:00 Michael Kennedy  36:23

0:00 I bet you got some. Yeah. Cool. All right. Now, let's talk about this thing that brain skins and in Brian's been on the show before, thank you, Brian, and said, If you don't know, close, close, Ember Dev is coming coming up soon. So close, Zim close Ember, like December closing on December, closing open source issues and other work on December however you verbalize that. It's live. And so the idea here is, let's open let's support open source maintainers by helping them close issues and PRs through November, I said, December, I guess it's November, we're halfway through. And it's a month long initiative for maintainers, and contributors and open source enthusiast to go through and encourage healthier open source practices and a raise awareness about maintainer burnout. So it's not about asking maintainers to do more, but it's like, how can we come in and do some of the tending of the garden and the cleanup of things, you know, when I go to an open source project, and I see, oh, there's PRs for the last three months, and they're all open. And like, I probably don't want to contribute to this. Because the chances are, it's just going to be another thing sitting there for months, and it's gonna get ignored. And I don't care, right? I mean, I want this change, but not enough that I'm going to do the work when there's a 90% chance that it's not going to get integrated, right, I feel called out. So the idea is like, well, let's go and kind of help people with these aspects of it. Right. So there's, it talks about it being a two way street and trying to do some of the healthy, healthy things help people right, it also laments my challenge of like stale PR. So it has two aspects it has for maintainers. And for contributors. So for maintainers first, it says Keep in mind that the fundamental point of clothes, Ember is maintain our health. And so take care yourself, you know, go diet, exercise, also has some really interesting things about decluttering your digital life. I think that's actually really interesting. I mean, we all just kind of have cruft build up cruft like on our physical desk cruft in our computer desktop roughed in like all the email and other things, and really cleaning those things out. It's really nice. Like, I just formatted my Mac Mini, after two years, about three days ago. And it's like, I got a brand new computer, I'm like, Oh, I'd love to sit down with this thing. There's no new computer here. It's just the junk is gone. And so I think that's an interesting angle. It talks about what you can do to help, as a maintainer, facilitate this. So you can get people help with triaging with infrastructure with technical writing, for example, like that to thing, if there was a tutorial or any form of example, or any line of code anywhere that said, here's how you use it, it would be way more used than if it's just, here's its name, good luck, you know. And so having somebody do a little technical writing or put together a tutorial, or even translation, all those would be really, really fantastic, right? So the idea is, if you're feeling up to it, you can identify some areas that would benefit from that. You can edit your readme to have and create a close Ember issue to let people know that this is an option. And you can actually go over here and see on the right now there's 729 repositories, like some that come to mind that are this is a search for all languages. It just happens to be pythons right at the top for all of them. So TQ DM NumPy, IPython, Sai pi notebook spider folium. Like all these are Python, I don't really understand how that's happening. But maybe it's maybe the algorithm anyway, like you could go to any of these that inspire you at Pull this up, right? So that's on the maintainer side, it's like some things that you can do to help set it up, right, just like label things, and so on. And then on the community side, it says, First, this is going to be on GitHub or GitLab, you need to know Git. So take a moment look on Git, because this is how you work on these things, and are able to just like run the tools, right? Like, if I'm going to help you build a house, I should know how hammers work, right, at least a little bit. So then it says, you can start taking a look at GitHub issues that maybe you've opened and see whether or not they're outdated, or you could close stuff that you've sort of put out there in the burden, and then go through that list, like I talked about. And then finally, there's like a celebration, closed boards. So down here, you can see there's a overall there's like a scoreboard type thing, it says overall, there's the 16,531 issues and prs 496 had been closed. And then there's like, scoreboard of the closed issues by project. So like data, lad is the number one and then Astro pi is just right behind it, Sai pi is up there and tails off from there. So anyway, thanks, Brian skin for sending this in. And people who want to get an angle to get into open source or want to contribute a little bit more, especially with some holiday time coming up. You know, here's something you could do that might mix up what you're doing.

0:00 Unknown Speaker  41:21

0:00 Yeah, absolutely. One of the one of the things that I try to do as much as I can, is try to advocate for people to get involved with sort of the small things, you know, and so I try to be, you know, if somebody's going to come on, you know, and grade an issue and say, well, great, no, you can go you can make this PR this is how you can go about and do it. So, so, as as a maintainer. I think, you know, these types of projects project, there was just one also on October, there was a hack Tober fest. Yeah, so I guess. So I guess maybe someone's coming in December. But

0:00 Michael Kennedy  41:57

0:00 October fest, I think is a little more about creating, like creating your first PR or making your first contribution. This is more about like, I think cleanup and closing out. Yeah, yeah.

0:00 Brian Okken  42:06

0:00 So all the people from Oktoberfest created a bunch of PRs closed?

0:00 Michael Kennedy  42:11

0:00 Yes, I participated. There you go.

0:00 Brian Okken  42:17

0:00 One of the things that I wanted to point out is we did talk about the how to help how to help maintain fast API. So that would be all actually all the tips that I read on how to help maintain Fassi API, apply to every open source project. So if if the open source project that you're interested in, doesn't have really good, how to how to help, tips, the fast API stuff applies to almost everything, like reproducing bugs, answering things, in sometimes, sometimes it's obvious from like a pull request or an issue that nobody's really excited about this thing. And maybe it should just be closed. So that's helpful also, is to just bring that up and say, Hey, core maintainer, people, this seems like it should be closed, should we go ahead and close that?

0:00 Unknown Speaker  43:00

0:00 So actually, on that, that point, I'm won't necessarily name names here. But there was a project that not one that not one that I'm involved, maintained, but it's a project that, you know, was talking about retiring, specific feature, right, and it was sort of, you know, no one's really using it, the, it doesn't really seem like it has very much activity, and they put, they just put a little notice up there and just buy because people were engaging in conversation. And because people were looking and we're willing to, you know, read a couple lines, or even in GitHub, or you go and you just click a little thumbs up or whatever, they saw all this interaction that people do care about this feature. And, you know, it really does impact, you know, as a maintainer. If you you know, the more people that are engaged in a discussion, the better it is to decide, you know, sort of how to steer the ship. Yeah,

0:00 Michael Kennedy  43:52

0:00 absolutely. Got it. Maybe it's just hate somebody suggested this. I'm not sure. What is the community thing, right. Having having an opinion might be helpful, right? Yeah. Yep, absolutely. All right, what else is helpful? cashews?

0:00 Unknown Speaker  44:06

0:00 Well, they're definitely delicious. But

0:00 Michael Kennedy  44:08

0:00 they are so so this. Yeah, this popped

0:00 Unknown Speaker  44:11

0:00 up in my you go on to get up, there's the Explore feed, so it's just was in the top of my feed, and it really caught my eye just because this is the type of thing that I find myself building and rebuilding on every single project that I do. So basically, you know, at its core, what cashews is it calls itself an async cash framework for simple API to build fast and reliable applications and and when you look at sort of what they're providing you out of the box, it's a very feature rich but it's super simple to get to get up and running. You know, I think he just really basically in a one line to to call setup and as after you do that, you just adding decorators to stuff in, you know, I think this is really sort of, you know, provides I had some really good foresight on how to build a very nice clean API that can be used in a lot of different situations. So, you know, on their, their, their, their GitHub readme, which I think is pretty well done. It gives you sort of how you might use this on typical web application to cache caching information on, on, on the request. But you could really use it in a whole bunch of different different features. So a couple different things that I kind of wanted to really struck struck me is really interesting is number one, they provide support for doing in memory caching, also Redis, which is very, very common, and also a write to disk, which I believe uses SQL Lite.

0:00 Michael Kennedy  45:48

0:00 We talked about disk cache, which is it looks like the foundational thing probably for the disk, the disk version of that caching and also dill. Instead of pickling, you do things. So you can you can store more wider variety of items into your cache, which is kind of cool. Nothing to do. But it sounds like it's probably good.

0:00 Unknown Speaker  46:10

0:00 Yeah, I don't know how much you combine Dell and cashews on a normal basis. But the I guess it could be done. No, but so so one of the things that I think is really neat that they built into this is there's a cache on top of a cache. And what I mean is, you know, let's say you you're putting all this information, these really expensive operations into Redis, or disk cache or something like that. They also have what it looks like, is maybe an application memory cache, where you don't even necessarily need to go do those network calls every single time that you want to go. Fetch Data, and it feels like sort of, you know, there's sort of like that old, saying that in computer science, there's, there's two hard things in computer science, there's cache invalidation, naming, naming things, and off by one errors, right. So so I feel like they sort of, like, are solving some of these problems, and they've got a couple of really simple ways that you can, you can do cache invalidation, you know, ways that you can, it just, it really strikes me as a very well thought out. Package, but one of my favorite things that I noticed is one of the ways that you can invalidate a cache is by rate limiting, well, rate limiting is itself a huge area, especially for web applications. And, you know, if you use package like cashews, you know, you're getting two different two different requirements for one right here, because it can, it can do the, you know, do double duty for you. So I think this is, I haven't used this yet. But it looks super clean, it looks like a very nice, very intuitive, and I'm pretty excited to try to try this one out for sure

0:00 Michael Kennedy  47:53

0:00 what an interesting kind of negative cash, this rate limit thing is. So the idea is, if you call it, you can put it into a function. And so if you call this function more than 10 times in a minute as the default example there, then you get, you basically get banned from calling it for a while. So instead of saying, we're going to scale it by by saving the answers to the questions, you're asking for this function, we're gonna save performance and CPU availability and whatnot, by only allowing us a call too much. And if you do it too much like you're done, you're out. Similarly with circuit breakers for errors. If there's too many errors. It's just going to stop for a while.

0:00 Unknown Speaker  48:31

0:00 Yeah, exactly. And and there's also this. There's also, you know, I kind of glossed over it. But one of the things that the different percussion validation is, there's sort of this, because it's using async. Io under the hood, it looks like it's got this ability to sort of refresh your cache automatically. So one of the things that you often have problems with caches is, you know, you might have you stale data in there that you want, you know, how do you get rid of that stale data. And so you can basically set up it looks like, like in the background, it's, it's called Early, early refresh, or something like that. And, you know, what it'll, you know, in the example that they give you, you know, if you've sort of call this, you know, within the given time period, it'll automatically go and sort of refresh it for you in the background, which I think is really cool.

0:00 Michael Kennedy  49:25

0:00 Yeah. Okay, so this one says, I want the cache time to be 10 minutes. But if it gets called on minute, seven to nine, in terms of the age of the cache result, go ahead and recompute it, so that in the background, right, give them an answer that that's cash back, but then actually call it so that you, you know, if it takes 30 seconds to compute this thing, or whatever, right, it takes a long time. Every now and then there's gonna be those gaps where it expired and you hit it again, right? So here's a way to kind of preempt that so nobody sees the slow version. There's a lot of interesting ideas here. Yeah. We go cashless. That's cool. That's pretty cool golf. Yeah. Very cool. Awesome. Well, good find Adam. Brian. Yeah. How about are extras?

0:00 Brian Okken  50:07

0:00 Yeah. How about him? I don't have anything extra. Do you have something?

0:00 Michael Kennedy  50:11

0:00 Let's go to Adam. Adam, anything else you want to give a shout out to while you're here? Sure. I

0:00 Unknown Speaker  50:14

0:00 just noticed that. Definitely voting season is here. You know, there was just a big vote in in the US we I live in Israel, we just had an election season here. But now we've got Python elections coming up. So So nominations for the Python steering Council are open, I think the way that it works is that you have to be a core member to to do a nomination. But anybody that wants to you can go on to their discourse, and you know, if there's a candidate that you that you support, you can, you know, you can reply to the comments, you can engage in the conversation. And I think that's really cool. And really, you know, a super way for people to sort of, you know, engage with the larger community.

0:00 Michael Kennedy  50:55

0:00 Yeah, very nice. And I actually have something related to that. Where is it? It's hiding the, to pull it on my notes. Maybe I didn't pull up. But the PSF survey? Yeah, here it is. It's just there. David, Lord put this out here. Speaking of web frameworks, we've covered them a lot. Let's bring flask into it as well. So over here on Mastodon, David says, take the PSLF developer survey, it's closing in a few days. That was yesterday. So people should go and do that, if they haven't pretty sure already did. I don't want to vote twice. But I also don't want to not vote to deliver. So anyway, that's really great that David put that out there. So another thing is not quite voting, but it's, you know, tolerate telling your opinion there. Alright, I got a couple of things. Also, quick shout out to your book. While you're here. Python web development was Sanic. People can check that out as well. So excellent. Let's see this one. No, that was that was just a joke. So I think actually, Brian, that's all I got for extras. So all right, you ready for a joke? I am I over here. Again. I wish I could pull these up separate. I have to log out but then I couldn't show you the other stuff. And by the way, Samuel Coleman just showed up on Mastodon as well, he wasn't there yet. So on people go Pydantic fame. So when all this stuff with Twitter came out, I thought this was a pretty hilarious, you don't remember, there was the switch of what did it mean for the blue mark the blue checkmark to be on an account, it used to mean that you were verified. And there's lots of rules about like showing your ID and having a Wikipedia page. And there's like rules to get that checkmark. And then Elon said, Well, we could just pay for that. And a bunch of people will start impersonating people and doing all sorts of funny shenanigans. Well, this, this is breaking here. And we've just noticed on Twitter that the JavaScript verified account that it's the program the the Twitter name is real programming language with 51 million followers. And there's a big message on it, right? What's the message say? Its kids been canceled, suspended accounts, suspended Twitter suspended accounts that violate the Twitter rules, JavaScript has been banned from Twitter for impersonating a real programming language. That's fine. Yeah. It's pretty good. Bye. Well, that's what I got for you this week. In terms of jokes. JavaScript has been suspended on Twitter.

0:00 Brian Okken  53:14

0:00 You know, and I just speaking of Twitter, just a few months, some humorous news. just Googling Twitter on Google News is hilarious. Just me. I mean, it's also sad, but also funny.

0:00 Michael Kennedy  53:25

0:00 Yeah. Absolutely. Well, Adam, thanks for joining us this week. And congrats on Sanic. It looks like it's been going strong for a long time. And it's got quite the community there.

0:00 Unknown Speaker  53:34

0:00 Yeah. Thanks for having me. Yeah, we've been we've been going strong since 2016 or so.

0:00 Michael Kennedy  53:39

0:00 Wow. That's awesome. All right, right. Thanks, everyone. Thanks for being here.

0:00 Transcribed by https://otter.ai

