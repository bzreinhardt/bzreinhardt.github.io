---
layout: post
title:  "AI Breakfast"
date:   2018-2-14
tags: [AI, UX, process, lessons, tactics]
categories: [Informational Posts]
---
Some quick notes from a great discussion/breakfast put on by [Canvas Ventures](http://www.canvas.vc/) and [Bloomberg Beta](https://github.com/Bloomberg-Beta/Manual) focused on building AI products in the real world.

![One strategy for a development pipeline](/img/ai_breakfast/dev_pipeline_1.png)
One strategy for developing AI products is to start with a full product that is only usable by the PhDs who built. Then, you develop it further so that an engineer straight out of undergrad can use it. Finally, you refine it to the point where a random person at a Fortune 500 company can use it. 

Always assume that your end users have no idea what's going on under the hood.

![Another strategy for a development pipeline](/img/ai_breakfast/dev_pipeline_2.png)

Another strategy for developing AI products is to have hardcore developers - *not* PhDs develop a pipeline of rule-based buckets. This is fragile, but each peace can be tested individually. Then you bring in PhDs who generalize each bucket with NLP and other machine learning techniques. This method allows you to ensure that your key use cases are always addressed before worrying about the AI. 

![Layer Partnership](/img/ai_breakfast/frontier_layers.png)

A data scientist/research engineer + prototyping systems engineer is a formidable team. Together, they can stabalize "frontier layers. Meanwhile, the pure researchers are creating the frontier layers ~6-12 months ahead of the rest of the company.

![Beware Technical Debt](/img/ai_breakfast/beware_technical_debt.png)

ML pipelines can become so long that pieces farther down the pipeline are shaped around technical debt earlier in the pipeline. Beware!

![Communication Pipeline](/img/ai_breakfast/communication_pipeline.png)

PMs can be a critical bridge between customers and those building the AI product. Their (very hard) job is to transform fuzzy problems into concrete numbers.

![AI PMs Job](/img/ai_breakfast/pms_job.png)

How do you get metrics on fuzzy problems? Remember, people are terrible at coming up with number-based metrics, but are amazing at discriminating between two possibilies - Good/Bad, In/Out, A/B. If you can pose a problem in that way, you can get the metrics you need.

![Descriminator](/img/ai_breakfast/people_are_great_discriminators.png)

Certainty about undercertainty is a big and often ignored consideration. You would hope that when an AI system says it's 99% certain its answer is correct, you would also be 99% certain its answer is correct. This is rarely the case and instead you have systems that are usually correct at 50% certainty and incorrect most of the time at 99%. One possible step towards addressing this is [Yarin Gal's Baysean Model](https://arxiv.org/abs/1506.02142)



### References

