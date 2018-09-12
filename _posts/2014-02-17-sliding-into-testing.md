---
title: Sliding into testing
date: 2014-02-17 23:27:46 -08:00
categories:
- Dissertation
- Grad School
tags:
- experiments
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

<p>Testing on the ground removes all the characteristics of space that make eddy-currents and other exotic actuators useful there. Specifically, friction (with air or a surface) often overwhelms the small forces of spacecraft actuators that aren’t rocket powered. So, low friction test beds are necessary to experimentally verify things meant to move in space.</p>
<p>Several versions of low-friction test beds are available for spacecraft research, each with their own advantages and disadvantages. The two most common types are air-bearing test beds and rotational test beds. They have a number of advantages. However, unnecessary degrees of freedom, cost, complication and lack of extensibility motivated the construction of a <a href="http://www.spacecraftresearch.com/blog/?p=119" target="_blank">1-DOF air-track test bed.</a></p>
<p>Air-bearing test beds have simulated microgravity dynamics, both translational and rotational, for over 45 years. Traditional planar air bearing systems are ideal for testing 2-DOF dynamics, but have a number of drawbacks that make them unattractive for testing 1-DOF systems like early-stage eddy-current actuators. The second degree of freedom introduces extraneous variables when testing 1-DOF systems. Sensing the state of the 2-DOF system in real-time requires video processing software that is either custom built or expensive. Closed loop control requires on-board computing, adding to the complication of the system. Planar air bearings require extremely flat surfaces and rapidly consume compressed gas canisters.</p>
<p>[caption id="" align="alignnone" width="500"]<a href="http://www.surrey.ac.uk/ssc/images/111561_frictionless_motion_testbed_large.jpg"><img alt="" src="{{ site.baseurl }}/assets/111561_frictionless_motion_testbed_large.jpg" width="500" height="254" /></a> 2-D air-bearing test bed. Picture courtesy of The University of Surrey[/caption]</p>
<p>Rotational test-beds can also simulate 1-DOF microgravity dynamics. These test-beds consist of a target on the end of a long arm attached to a low-friction rotational axis. The throw over which they can approximate linear translation is limited by the length of the arm. The bearings holding the rotational axis experience more off-axis torque as the arm length increases so the friction will increase with the throw of the system.</p>
<p>[caption id="" align="alignnone" width="448"]<a href="http://www.umich.edu/~adcl/pic/Triax1.JPG"><img class=" " alt="" src="{{ site.baseurl }}/assets/Triax1.JPG" width="448" height="336" /></a> A rotational test bed. Picture courtesy of the University of Michigan.[/caption]</p>
