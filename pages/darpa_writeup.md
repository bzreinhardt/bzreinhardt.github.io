---
title: D60 Writeup
permalink: "/d60_notes"
layout: page
---

_Update_: [DARPA released videos of some of the talks.](https://www.youtube.com/playlist?list=PL6wMum5UsYvbLCUdhDjA_j0cXhlBI0jnW)
The ones on [Mosaic Warfare](https://www.youtube.com/watch?v=33VAnIEjDgk&list=PL6wMum5UsYvbLCUdhDjA_j0cXhlBI0jnW&index=4&t=0s), [Electronics](https://www.youtube.com/watch?v=W_cB8VYunY8&list=PL6wMum5UsYvbLCUdhDjA_j0cXhlBI0jnW&index=5&t=0s), and [Bio](https://www.youtube.com/watch?v=CdRdkxb3G7w&list=PL6wMum5UsYvbLCUdhDjA_j0cXhlBI0jnW&index=8&t=0s) are worth watching.


These are my initial takeaways from the DARPA D60 Conference. Anything particularly interesting? Places I should go into more depth? <ben@benjaminreinhardt.com>


# Big Themes
### Mosaic Warfare
What is the implication of this? The focus on mosaic warfare elevates the importance of both systems that can act on their own, robust p2p communications, and computer systems that can process and make sense of a complex situation.

The term *"System of Systems"* comes up a lot. Translated, it's DARPA/Military speak for how a military based around Mosaic Warfare will be much more complex because there will be many more intra-component interactions.

One hypothesis that technology that has DARPA backing will be commercially viable in ~10 years. If you accept this hypothesis, I would bet on these things getting better:
- Smaller, better ways of doing chemistry and biology. The Mosaic Warfare concept requires a lot of "edge" operations. Imagine extending the idea of [edge computing](https://en.wikipedia.org/wiki/Edge_computing) to design and production in biology, chemistry, and manufacturing.
- Better connected devices. They currently suck, but they actually need to work both in terms of robust operation with non-ideal connections and they need to actually "talk" to each other intelligently - ie. share capabilities and create a useful system.
- Better security, especially for distributed systems - see the idea of edge operations above. Note that nobody was talking about blockchains, but they really need to care about distributed systems. Not for philosophical reasons but because for Mosaic Warfare to work, they need to trust computers collaborating.
### Third Wave AI
"Third Wave of AI" is a very DARPA-specific term but it's much more accurate than how most other fields talk about AI.
![](https://www.nextbigfuture.com/wp-content/uploads/2017/02/3wavesAI-1-730x430.jpg)
Currently (September 2018) the useful AI that everybody is excited about is mostly the second kind - the categorizing kind. This is incredibly useful but doesn't have the capabilities that people would ascribe to AI. As one program manager put it - "there are lots of pictures of cats on the internet. There aren't many pictures of common sense." What we *want* is for AI to have common sense.

# Organizational Learning
I was focusing not just on *what* DARPA was doing, but *how* it does it. I suspect there are many lessons for how to enable innovations in the practices that have emerged in DARPA over the decades.
### Continuity over time
How does DARPA maintain continuity between people and administrations? NASA has this terrible problem where they make 10 year plans that change at most every 8 years. I spoke to a previous division director and asked "how do you manage to get that continuity?" His response was that it depended on a few things:
- Relative autonomy for the director

  The director has the ability to kill or enable programs with only the oversight of a board-of-directors like organization.
- The ability to kill bad programs

  It's counterintuitive, but being able to kill programs quickly also enables longer-term bets for two reasons. 1) There's no danger that a program will continue simply out of momentum, so they don't have to hedge. 2) The organization to redirect resources more nimbly towards programs that are going well instead of needing to treat them all equally.
- Incentives tied to having successful programs, period, not successful programs tied to your name/initiatives.
- Clear criteria

  The [Heilmeier Catechism](https://www.darpa.mil/work-with-us/heilmeier-catechism) is one of those "Duh" but Brutal gauntlets that ideas must run before they're funded.


### Interdisciplinary Teams
DARPA is on of the few organizations I've seen that walks the walk when it comes to Interdisciplinary teams. One of the researchers unprompted said "They actually manage to make the Interdisciplinary thing work!"  
One actionable strategy was that they brought everybody together for two weeks and forced them to spend a lot of time talking about their particular concerns and ways of thinking.

One project was actually set up explicitly to test collaboration quality. The program revolves around fast design and prototyping which would need to be done in a distributed way so each discipline was explicitly separated geographically.

### Priority Alignment
At the end of the day, every piece of DARPA research has an explicit tie all the way up to well-defined high level goals. What makes these high level goals 'well-defined' as opposed to 'organize the world's knowledge' (Google) or 'make general AI' (OpenAI) is that they can actually be heirarchically broken down into smaller and *problems*. Darpa thus creates a problem-rich environment.


### Ecosystems and Timing
DARPA doesn't get attached to innovations throughout their whole lifecycle. Instead, it cultivates an ecosystem of other organizations including academia and private companies to shepherd innovations into existence.

This stands in contrast to VC funds who need to constantly see growth and progress. DARPA is happy to seed a line of research and then back off to let it putter along in Academia or a research lab like AFRL. The potential innovation doesn't progress quickly, but will occasionally hit an inflection point at which point DARPA will step back in and slam on the accelerator. These inflection points can look like an unexpected breakthrough or an external enabling innovation (like GPUs in the case of deep learning.) On the other side of the acceleration, DARPA hands off innovations to private companies if it looks like they will thrive by generating revenue.

For a much more thought-out report on this, [see here.](https://fas.org/sgp/crs/natsec/R45088.pdf)

# Cool technology
Obviously, DARPA is a technology organization at the end of the day. Here's a list of programs I found particularly interesting because of my biases (Human-computer hybrid systems, complex systems, space exploration, accelerating science and innovations.)

-  Automatically creating causal models (for biology at first) from research papers: [https://www.darpa.mil/program/big-mechanism](https://www.darpa.mil/program/big-mechanism)
- Creating better models for complex human systems:
[https://www.darpa.mil/program/causal-exploration](https://www.darpa.mil/program/causal-exploration)
- Better Human-Computer Collaboration:[https://www.darpa.mil/program/communicating-with-computers](https://www.darpa.mil/program/communicating-with-computers)
- Creating better models for complex physical systems using deep learning:
[https://www.darpa.mil/program/deep-purposeful-learning](https://www.darpa.mil/program/deep-purposeful-learning)
- Knowing what we don't know in complex physical systems:
[https://www.darpa.mil/program/equips](https://www.darpa.mil/program/equips)
- SPACE PLANE:
[https://www.darpa.mil/program/experimental-space-plane](https://www.darpa.mil/program/experimental-space-plane)
- Creating autonomous systems that you can ask "why did you do that?":
[https://www.darpa.mil/program/explainable-artificial-intelligence](https://www.darpa.mil/program/explainable-artificial-intelligence)
- Creating domain-independent principles for understanding complex systems:
[https://www.darpa.mil/program/fundamentals-of-complex-collectives](https://www.darpa.mil/program/fundamentals-of-complex-collectives)
- Ways to test social science models:
[https://www.darpa.mil/program/ground-truth](https://www.darpa.mil/program/ground-truth)
- More accurate models for transients in complex dynamical systems:
[https://www.darpa.mil/program/models-dynamics-and-learning](https://www.darpa.mil/program/models-dynamics-and-learning)
- Trying to make social science actually predictive science:
[https://www.darpa.mil/program/next-generation-social-science](https://www.darpa.mil/program/next-generation-social-science)
- Making speech tech actually useful:
[https://www.darpa.mil/program/robust-automatic-transcription-of-speech](https://www.darpa.mil/program/robust-automatic-transcription-of-speech)
- Better data analysis tools:
[https://www.darpa.mil/program/simplifying-complexity-in-scientific-discovery](https://www.darpa.mil/program/simplifying-complexity-in-scientific-discovery)
- Enabling design in domains with incomplete models:
[https://www.darpa.mil/program/synergistic-discovery-and-design](https://www.darpa.mil/program/synergistic-discovery-and-design)
- Repurposing dead/enemy satellites:
[https://www.darpa.mil/program/phoenix](https://www.darpa.mil/program/phoenix)
- Servicing satellites:
[https://www.darpa.mil/program/robotic-servicing-of-geosynchronous-satellites](https://www.darpa.mil/program/robotic-servicing-of-geosynchronous-satellites)


# Remaining Questions
- Is there a list of DARPA programs that were killed and why? Seems like it would be valuable for civilization.
-
