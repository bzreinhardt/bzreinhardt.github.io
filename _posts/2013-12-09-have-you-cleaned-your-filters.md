---
title: Have you cleaned your filters?
date: 2013-12-09 22:59:44 -08:00
tags:
- analogies
- brains
- engineering
- human filters
- kalman filters
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

<p>One tool in the control/dynamics engineer’s toolbox is the Kalman filter. It’s one of those big intellectual hammers that makes many problems look like nails.</p>
<p>Put simply, a Kalman filter combines noisy external measurements with an internal simulation of the system in question in order to estimate the system’s true state. Depending on how much you trust the measurements (the covariance of those measurements), the filter will weigh the internal model and the external measurements differently.</p>
<p>As with a lot of these big concepts, it’s a fun thought experiment to draw an analogy from the Kalman filter to the human brain. In many different domains, we are always running an internal model of the world, and comparing our own measurements to that model. We use a pseudo-Kalman filter when we’re walking – you hold a model of the ground in your head and for the most part assume that the ground at your next step is roughly the same as the ground on your last step. We also use a pseudo-Kalman filter when we’re learning or thinking – you compare new information to the model of the world in your head. Depending on certainty in your model and trust in the source of information, you give relative weight to both and compose the two together to estimate the true state of things.</p>
<p>This filtering can be powerful:</p>
<p>Say you see a bunch of dragons out of the corner of your eye. That’s your sensor data. Your internal model of the world says the word doesn’t have dragons (alas!) For most people, both the covariance of our peripheral vision and trust in our mental model are high enough to conclude that the ‘truth’ involves a flock of geese rather than a flight of dragons. (Fun fact: a group of dragons can also be referred to as a wing, flight or weyr.)</p>
<p>However, the filters can also fail: When your model is worse than you think (so you trust it too much) you can slip on a patch of ice by stepping like it’s firm ground or rejecting a new source of information simply because it doesn’t square with your internal picture of the world.</p>
<p>The trick, both in more advanced filters and in your brain, is to correctly update both your internal model and your sensor covariance based on new information. Like many worthwhile things, that’s simple to describe but surprisingly hard to implement.</p>
