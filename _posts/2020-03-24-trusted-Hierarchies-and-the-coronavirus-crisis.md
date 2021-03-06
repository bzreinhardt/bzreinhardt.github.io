---
title: Trusted Hierarchies and the Coronavirus Crisis
date: 2020-03-24
categories:
- systems
permalink: /trusted-hierarchies
tags:
-
layout: post
---
**tl;dr:** Trusted hierarchies are important for solving problems under constrained time and resources. Governments have historically provided large-scale trusted hierarchy but the US government has completely botched that role in the coronavirus crisis. We need to ignore the false dichotomy of "government vs decentralized coordination" and create a new temporary trusted hierarchy to coordinate response to the crisis.
<div class="row">
<div class="column">
  <img style="border-radius:10%;width:100%;" src="https://storage.googleapis.com/bzreinhardt-images/hierarchy_based_collaboration.jpg" />
  <figcaption style="text-align:center;text-size:small;"> A hierarchy (hopefully trustworthy) </figcaption>
</div>

<div class="column">
  <img style="border-radius:10%;width:100%;" src="https://storage.googleapis.com/bzreinhardt-images/distributed_system.jpg" />
  <figcaption style="text-align:center;text-size:small;"> A decentralized system - it's very hard for yellow to coordinate with green </figcaption>
</div>

<div class="column">
  <img style="border-radius:10%;width:100%;" src="https://storage.googleapis.com/bzreinhardt-images/committee_based_centralization.jpg" />
  <figcaption style="text-align:center;text-size:small;"> Committees can also centralize coordination </figcaption>
</div>
</div>


##### If you have limited time and resources, trusted hierarchies are better for solving problems than decentralized systems

Trusted hierarchies make better use of time and resources because centralized coordination makes sure effort is not being repeated in stupid ways. Of course, centralized coordination sometimes stops effort from being repeated in smart ways, so centralization is not always good. Trusted Hierarchies can still have multiple attempts to solve the same problem - DARPA funds multiple groups to try different approaches, and companies often have multiple teams working in parallel. Mistakes can remain reasonably uncorrelated even if the two groups know about each others’ approaches. A well-functioning hierarchy prevents situations where two groups are doing literally the same work and makes sure that one group knows about something useful the other group has created.

During WWI many groups were trying to build technology to detect submarines.  None of these groups knew about each other. Vannevar Bush had a crazy and unsuccessful scheme to use magnets. Only after the war he realized that another group was attempting a much better method. However, that group’s method had a key flaw that Bush had solved in the process of building his own solution. If there was a trusted hierarchy, someone would have made the two groups aware of each other and the two solutions could have been combined.

##### Decentralized systems are great if you have lots of time and resources

Many uncorrelated mistakes come from many uncorrelated samples. Logically, uncorrelated samples of an idea space mean that some people’s approaches seem absurd. It would be quite correlated if everybody agreed that an approach was good, wouldn’t it? Even if everybody is working in good faith, it is hard for someone to work on something in a centralized system that the centralizers find absurd. The chances that people are working on the same thing under different constraints is the highest in decentralized systems. By analogy, the same way that [Monte Carlo sampling](https://en.wikipedia.org/wiki/Monte_Carlo_method) routinely beats human intuition for a sampling distribution, more uncorrelated samples lead to a better exploration of the idea space. This kind of sampling is expensive in time and resources.

##### Government as the source of trusted hierarchy

When you think of trusted hierarchies and centralized coordination, your mind probably leapt immediately to the government. However, government centralized coordination versus decentralized efforts is a false dichotomy. Government does not need to be the source of a trusted hierarchy. It’s true that governments are the only hierarchy that can be imposed by force. However, trusted hierarchies exist within companies, communities, and even open source projects have coordination and hierarchy. Is there a reason why these voluntary hierarchies can’t be scaled up (at least temporarily?)

The assumption that the government needs to be the source of trusted hierarchy may be a psychological hangover from the 20th century. During World War II the US government successfully provided a trusted hierarchy. The government’s R&D efforts were all in the Office of Scientific and Research and Development (OSRD) which was run by [Vannevar Bush](https://notes.benjaminreinhardt.com/Pieces_of_the_Action) who reported directly to FDR. Bush notes several times in his autobiography that FDR trusted him on R&D matters and in turn Bush trusted the people under him to give him accurate analyses that he could pass on to the president. A similar situation happened around the distribution of materials under the Controlled Materials Plan led by Georges Doriot. Arguably, this structure was effective for winning WWII. While many things stopped being part of the hierarchy - the government no longer dictates manufacturing plans - the psychological assumption that the government is the default trusted hierarchy remained. I believe this assumption led to the idea that a response is either centralized by the government or decentralized.

##### The US government has dropped the ball on coordinating a response to the virus and there is a large decentralized response

In the US, there is still no clear plan or way to focus effort around the coronavirus crisis. People and resources that can help are not being utilized by the government response. Instead, people have created a large decentralized effort to help with the coronavirus. A  centralized response could arguably do a better job addressing at least the well defined problems that the decentralized effort is tackling.

##### Well defined problems

* Get more PPE to medical personnel (and secondarily to other people) so they don’t get the virus or spread it.

* Enable more ventilators to save the lives of people with the virus. This problem has two parts: getting more ventilators into the hands of the hospitals and training more people to use them (or making ventilators that are easier to use.)

* Create millions of tests for the virus that are as fast and accurate as possible.

* Create a way to track who has the virus and who has come into contact with them once we have effective testing.

* Create an antiviral that can help people recover if they get the virus.

* Create a vaccine that prevents people from getting the virus.

* Distribute information about how to help with all of the above.

##### Fuzzier Problems (where decentralized responses might make more sense)

* Creating tools to make quarantine more tolerable.

* Creating tools to make the economy work even while people are quarantined (telerobotics, etc.)

* Creating better sterilization tools.

* Figuring out where the virus came from in the first place.

* Figuring out how the virus actually works.

* Helping people recover from the economic shock.

##### The decentralized coronavirus response has both a communication problem and a control problem
In an ideal situation, anybody who wants to contribute to the response would be able to quickly know the status of each high-level problem (the communication piece) and know how to best direct their efforts (the control piece.)

##### The Communication Problem
There are dozens or hundreds of efforts towards each problem on the list. There is no good way to figure out the global status of solutions or where to effectively direct your own effort to help. You have both a lot of people not working on something they should because ‘someone is working on that’ and a lot of duplication.

I am currently part of three discord groups, two slack channels and several WhatsApp groups all dedicated to coordinating people’s efforts. On top that, other coordination is happening on Facebook and Twitter. It takes a lot of bandwidth to pay attention to decentralized efforts.  

Distributed solutions to the communication problem cause more communication problems. There are multiple efforts to solve the communication problem with lists and databases, none of which you can trust to be complete. It’s almost as much work to synthesize these lists as it is to create your own.

##### The Control Problem
Even if the communication problem were solved and everybody could know the status of everything, there’s still the question of how to distribute resources. Which of the five contact-tracing apps should I give my time to? Which of the seventy mask-distribution teams should I give my masks to?

The control problem and communication problem are coupled. To answer these questions definitively you would need to do one of two things: control the number of projects/rank them by importance so there is a default or control who works on what.

Under normal circumstances it’s often fine to incompletely solve the communication problem and allow markets to work.  Controlling options comes with many downsides.  However, this is a clear market failure. Lost time here means lost human lives and livelihoods, so efficiency is more important than choice.[^1]

There are dozens and in some cases hundreds of separate efforts towards each item on the list and no good way to figure out the global status of each or where to effectively direct your own effort. You simultaneously have people not working on something they should because of the ‘someone is working on that’ problem and at the same time there’s a lot of effort duplication.

I am currently part of three Discord groups, two Slack channels and several WhatsApp groups all dedicated to helping with the crisis. On top of that, people are coordinating on Facebook and Twitter. There are at least seven different attempting to give an overview of everything that is going on. While they overlap, each includes things that the others do not. If you wanted a vaguely complete overview, you would need to pay attention to each of them. It takes a lot of bandwidth to pay attention to decentralized efforts.

##### The coronavirus is a situation where the normal arguments against centralized systems are flipped
 Often centralized systems are not the best because people are great at doing things in their own self interest not as good at doing things in the interest of others. Helping with the coronavirus crisis is a situation where people’s actions are primarily *on behalf of others* and not just people nearby.

If you buy that we need a centralized response to the coronavirus, that the US government has dropped the ball on coronavirus response, and that government does not need to be the source of a trusted hierarchy, what are the next steps?

1. The people and organizations who are currently part of the decentralized effort need to agree on a leader they trust. This could be done through some kind of democratized process where everybody votes or a representative process where people delegate to someone else (see #5.) Whatever it is it needs to be simple and fast. This may be the step that makes the whole process untenable.  
2. There should be a very clear expiration condition set on the hierarchy to both make it more palatable for people and prevent it from turning into a bureaucracy or dictatorship.
3. People and organizations need to cede limited autonomy to this leader. The leader needs to be able to tell them where to send money they want to contribute, what to produce on machinery they’re willing to devote to the cause, who to help with time they want to contribute.
4. Obviously it’s far too much for one person so that leader then needs to quickly and clearly delegate different pieces to subordinates and they in turn need to delegate further. People need to treat people with delegated authority as having just as much authority as the leader.
5. You can create a top-down hierarchy from the bottom-up.[^2]  First, everybody delegates one person to be their representative for each topic on the ‘clear problems’ list. You agree to do whatever that person says with respect to that subject (or whomever *that* person delegates to.) The trust trickles up to a few people who at the very least it produces a finite number of people to pay attention to.  In a best case scenario they can coordinate among themselves and then delegate actions which travel back down to everybody trying to figure out “how should I help?”   


[^1]: I realize this line of argument is the slippery slope towards dictatorship.
[^2]: This idea is not original and clearly has flaws but I think it's important to point out a clear action
