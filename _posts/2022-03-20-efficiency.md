---
title: Efficiency, Fat Ideas, and False Negatives
date: 2022-03-20
tags:
layout: post
permalink: /efficiency
---
Before you even undertake the work to create a thing, there’s some assessment of whether it’s possible and how valuable it will be.[^1] (For some extremely nebulous definition of value — I’ll talk about that later). Some ideas take a large chunk of resources to assess(**“fat” ideas**).[^2] In other cases, a spreadsheet and well-founded assumptions can make a strong case that “it will be hard, but if we pull off all these things that don’t violate physics along this critical path, it will be incredible.” (**“Lean” ideas**).

SpaceX’s reusable rocket is a canonical lean idea: “If we can do X (which is very hard but has a clear critical path) then we will reduce/increase this key metric by an order of magnitude, which is a complete game changer.” Software’s low cost and fast iteration speeds make many bit-based ideas lean even without clear metrics or critical paths. “Basic Science”[^3] is a classic example of a “fat” idea: the curiosity-driven study of tree frog venom leads along a circuitous route to a miracle cure. However, fat ideas include more than just curiosity-based discovery. Most “systems research”[^4] ideas — of the sort that were the precursors of a good chunk of modern technology —are also fat ideas.[^5]

If all you care about is big returns per dollar (in either financial terms or “impact”) there is a clear strategy: work to quickly kill ideas and bias towards a thousand false negatives over one expensive false positive.

Imagine that lean ideas look good after 1 unit of work and will create 1000 units of value, while fat ideas look good after 100 units of work but produce 1100 units of value. Each idea creates the same *net* value but if you care about returns on investment you would rather spend 1 unit of work every time, ignoring every single one of the fat ideas and their potential results. In order to make it worth your while, the fat ideas would need to, on average, create 100000 units of value (an increase proportional to the cost of evaluating them).

Another framing is through the lens of scarce resources. If you have 100 units of work to deploy, your choice is whether to spend that 100 units of work on 100 lean ideas or 1 fat idea. If each project has the same expected value, you would have 100x expected value by focusing 100% on lean ideas. Lean ideas are better to work on in expected value and ROI terms.

The advantage of the lean strategy has nothing to do with whether you’re trying to capture the value you create or not — as long as you prioritize efficiency, it makes sense for both investments and philanthropic spending.

In reality, ideas don’t fall neatly into buckets that take one of two values of resources to evaluate. There’s some continuum from zero effort to a situation where you don’t know if it will be valuable and possible until you literally complete it. However, because we’re talking about a scalar evaluation effort, it’s reasonable to draw a line that is the maximum effort you’re willing to spend per idea. Everything to the left of the line is lean and everything to the right is fat. This bucketing system means that you lose out on the marginal idea immediately to the right of the line.

 The fact that it’s hard to distinguish between many fat and lean ideas compounds the argument for a “lean assessment only” strategy. As a result, many research organizations either implicitly or explicitly pursue the lean strategy — explicitly preferring many false negatives over an expensive false positive. Indeed, many organizations play up the efficiency of their process: "we kill ideas fast!" And given the assumptions and constraints they’re operating under, they’re not wrong.

Let’s examine those assumptions:
1. Lean and fat ideas create roughly the same amount of value on average.
2. The difference in cost between evaluating lean and fat ideas is several orders of magnitude.
3. There are plenty of lean ideas.
4. It’s impossible to know a-priori how much effort it will take to evaluate an idea.
5. The results of lean and fat ideas are interchangeable.
6. Efficiency should be prioritized.

### 1. Lean and fat ideas create, on average, roughly the same amount of value.
This assumption seems reasonable — I don’t know of a comprehensive study of innovations, the value they created, and whether it was easy for people to evaluate whether they were worth pursuing a priori but there are plenty of valuable examples of both types. SpaceX, Tesla, Transistors, airplanes, AI, artificial fertilizers, the structure of DNA, and atomic power (after a certain point) are all lean ideas — generally they’re characterized by either a gold rush or criticisms of impossibility to pull off. Lasers, cars, unix, the internet, germ theory, and solar panels are all fat ideas — generally they’re characterized by people calling them niche or useless and are preceded by a lot of “piddling around.”

While historically, lean and fat ideas do seem to create roughly the same amount of value on average if you force them into a framework of scalarized value, I’m going to push back against that framework in point #5.

### 2. The difference in cost between evaluating lean and fat ideas is several orders of magnitude.**

This assumption is also reasonable. Lean ideas are characterized by being able to put a lot of assumptions into a spreadsheet and possibly identifying one or two key experiments to validate some assumptions. Fat ideas often involve years of piddling around (and thus years of salaries and expensive equipment) before even having a clear idea of what the valuable output even could be.

### 3. There are plenty of lean ideas.

The number of fat ideas (even if they would only take slightly more effort to evaluate than the fat-lean cutoff) is irrelevant if all you care about is efficiency. The frequency of fat ideas is irrelevant unless the frequency of lean ideas is so low compared to the frequency of fat ideas that you hit a tipping point where pursuing a lean strategy forces you to spend more resources throwing away ideas quickly than you would spend evaluating fat ones. Thus, the lean strategy is rational if you believe there are plenty of lean ideas.

It’s (almost? actually?) impossible to evaluate this assumption. My personal hunch is that a component of the Low Hanging Fruit theory of stagnation is that so many institutions (rationally) pursue the lean strategy that lean ideas have become depleted. You could call lean ideas “low hanging fruit” themselves, but generally the “low hanging fruit” is understood to refer to the total effort to realize the idea, not to evaluate whether it’s worthwhile.

My other hunch is that while the distribution of evaluation costs is continuous, it is not flat. It likely has at least two peaks — one that’s lean-esque and one that’s fat-esque. If that’s the case, institutions pursuing the lean evaluation strategy can’t just incrementally increase their threshold for leanness as lean ideas are depleted.

The first three sets of assumptions all fit within a nice numerical framework. You can play with numbers [here](https://docs.google.com/spreadsheets/d/1j679FlpPgl4GT6Ohi9CR0yrZCLIuVrhT7rc36D_NpF0/edit?usp=sharing).

### 4.  It’s impossible to know a-priori how much effort it will take to evaluate an idea.
 The lean strategy implicitly assumes that it’s impossible to know how much effort it will take to evaluate an idea (meta evaluation!). If it were possible to know up front how much work it would take to at least know whether an idea was worth pursuing, you could know which ideas are marginal, taking two units of effort but not 100, and evaluate those ideas as well. The dream of program design as a discipline is to be able to cheaply determine how much work it will be to evaluate an idea (in some senses, an ARPA-like program is an idea evaluation).

### 5. The results of lean and fat ideas are interchangeable.
Collapsing value into scalar quantities assumes that the outputs of pursuing different ideas are the same in kind. That is, the *types* of innovations that will come out of pursuing only lean ideas look the same as if you pursued both lean and fat ideas. Or at least the types of innovations created by lean and fat ideas are equally desirable.

Here is where thinking in terms of monetary outcomes violently diverges from a more nebulous concept of “value.” If all you care about is cash in and cash out, the results of all ideas are interchangeable. However, I suspect that pursuing primarily lean ideas systemically biases towards certain types of innovations. As a result, whole classes of ideas are systematically *not* being explored. It will take a lot more work to enunciate what the systemic differences are between the outputs of lean and fat ideas, but my hunch is that a lot of software and point changes are lean ideas, while many general purpose technologies and systems research are fat ideas. Even ignoring which specific classes of innovations we’re missing out on by pursuing primarily lean ideas, I suspect that pursuing an “unbalanced” distribution of lean/fat ideas is unhealthy for long-term innovation because ideas feed on each other — fat ideas generate lean ideas and vice versa. The bias towards lean ideas may be a factor in vibes of stagnation.

### 6. Efficiency should be prioritized.
The final assumption underlying lean strategies is that efficiency (value created/effort in) is the most important thing. When you have a fiduciary duty to maximize shareholder value, *this is correct*. There are many important innovations that are just bad investments. Speaking to several high-ranking people who run corporate research labs, they constantly need to justify, not the absolute cost of the work they’re doing, but the ROI they expect.

You would expect the unbreakable coupling between profit and efficiency to suggest a clear opportunity for philanthropic money to step into the gap and enable the fat, inefficient assessments that can unlock entirely different classes of innovation. Disappointingly, I’ve found this to not be the case. Instead, the majority of philanthropic funding decisions I’ve run into are still implicitly or explicitly dominated by efficiency. Questions like “what is the most impactful way to use this dollar?” “How do we minimize risk of failure?” “How do you know it will work?” “What will the impact of this be?” Are all trying to maximize efficiency. Efficiency is not bad in a vacuum, but it is when it is killing fat ideas at a societal level (if the assumption that fat and lean ideas are interchangeable is wrong).

Where does this all leave us? If the outputs of lean and fat ideas do indeed generate different types of innovations, a relentless prioritization of return on investment (whether in dollars or impact) has created a world of systemically skewed innovations. Many incredible discoveries and inventions have been sacrificed on the altar of efficiency. The lean-only approach is completely rational for profit-seeking businesses. However, institutions with other mandates, like philanthropy and governments, have also been captured by the same mindset. It’s a heretical notion in the current zeitgeist (and there are many ways it can go wrong), but it would be powerful for institutions that can get away with it to prioritize things besides efficiency. Perhaps efficiency is overrated.

### Some Related Reading
- [Scott Alexander's Studies on Slack](https://slatestarcodex.com/2020/05/12/studies-on-slack/)
- [Jerry Neumann's One Process](http://reactionwheel.net/2020/04/one-process.html)

Thanks to Matt Clancy and Luke Constable for reading drafts of this piece and amazing ideas and Omar Rizwan for pointing me towards the piece on Systems Research.

[^1]: I’m implicitly talking about research ideas here, but I think this argument applies more broadly.
[^2]: The “fat” and “lean” framework comes from [GUTS: The Grand Unified Theory of Striving (or Slacking)](https://studio.ribbonfarm.com/p/guts-the-grand-unified-theory-of) which is a chronically underdiscussed framework.
[^3]: I think the pipeline model of innovation is deeply flawed, but for now this is the framework most people use.
[^4]: See [http://doc.cat-v.org/bell_labs/utah2000/utah2000.pdf](http://doc.cat-v.org/bell_labs/utah2000/utah2000.pdf)
[^5]: Digging into how to tell whether an idea is fat or lean and whether there are systemic differences between them is for another time.
