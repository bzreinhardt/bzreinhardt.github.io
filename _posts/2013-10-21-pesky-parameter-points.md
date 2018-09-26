---
title: Pesky Parameter Points
date: 2013-10-21 22:44:49 -07:00
tags:
- computers
- documentation
- human filters
- models
layout: post
type: post
parent_id: '0'
password: ''
status: publish
meta:
  _edit_last: '44242401'
  _publicize_pending: '1'
author:
  login: bzreinhardt
  email: bzreinhardt@gmail.com
  display_name: Ben
  first_name: Ben
  last_name: Reinhardt
---

<p>I’ve been working on the <a href="http://www.spacecraftresearch.com/blog/?p=212" target="_blank">Quirk-E project</a>, in particular, tuning parameters so that it produces numerical results that resemble reality. [link to blog] I plan to share it <a href="https://github.com/bzreinhardt/quirk" target="_blank">on Github</a> soon, but until then, I wanted to bring up some important points about models. I may have made these points before, but I see so few people who actually think about them that I’m going to risk repeating myself.</p>
<p>The rise of cheap computing has allowed numerical models to explode into basically every domain. Some wonderful discoveries have come of this. It’s just important to remember both that they are only models and not reality and to keep in mind how much human discretion goes into modeling.</p>
<p>Every model is influenced by the discretion of the modeler, from something as simple as fitting a line to data points to running a <a href="http://en.wikipedia.org/wiki/Genetic_algorithm" target="_blank">genetic algorithm. </a>Even though the genetic algorithm nominally ‘figures it out for itself,’ the human still sets a number of parameters that heavily influence the outcome.  And it’s so tempting to tweak parameters without justification except that they give you the answer you want.</p>
<p>I’m trying to make sure I don’t fall into this trap by meticulously noting whenever I change a number and why I did it.  Even ignoring any malicious intent, it’s so easy to get into a flow state of ‘if I just tweak this one more number it will work!’ The proliferation of models and the inevitable tweaking temptation increases the need for something like <a href="http://benjaminreinhardt.wordpress.com/2013/06/30/research-big-brother/" target="_blank">automatic documentation.</a></p>
<p>What you should take away is that any time ‘a computer told us so’ a human directed it in how to do that.<a href="https://www.youtube.com/watch?v=m3dZl3yfGpc" target="_blank"> It’s often forgotten that scientific models are just that – models.</a> Nobody thinks that a model castle captures all of reality, we realize that instead, it’s a useful representation, whether for discovery or illustration. We should remember to treat scientific models the same way.</p>
<p>Computer models are like the <a href="http://en.wikipedia.org/wiki/Yin_and_yang" target="_blank">yin to human intuition yang</a>. Models bolster our intuition’s weaknesses and can teach us a lot of things. But it’s important to remember that like yin, a model can’t stand on it’s own and all models have a little dot of human choice in them.</p>
