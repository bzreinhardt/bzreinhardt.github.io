---
layout: math_post 
title: 2D Inspection Outline and Abstract
tags: [papers, indexes]
comments: true
---
## Abstract
------------------------
Small satellites can enable a new mission profile: investigating larger satellites on orbit. Induction couplers are a new actuation technology that can augment on-orbit servicing. Current technologies for relative actuation between two spacecraft have glaring gaps - they require direct contact or propellant. Induction couplers using the forces between a magnetic field and its induced electric currents could control the relative position between a small chaser spacecraft and a larger target without physical contact. A system utilizing these eddy-current forces places relatively few requirements on the target and chaser compared to more exotic EM actuation systems. This paper presents a system overview of a contactless induction coupler, outlines those requirements through the analysis of an inspection mission on the International Space Station, and compares them to current experimental work.

## Contents
------------------------
1. Introduction
	* [Purpose - demonstrate the use case of an induction coupler for OOS](purpose.html)
	* [Alternative Tech Backgroundd](alt_tech_background.html)
	* [Physics Backgroundd](physics_background.html)
2. [Motivational Mission descriptionn](motivational_mission.html) 
	* EC actuated small satellite can replicate a spacewalk in ways that no other technology can
		* Robotics offers opportunities, 
		<!-- Emphasize positive. cit robonaut, be political. Offload astronauts from tasks.[spacewalks are expensive and dangerous] Possibly gravity reference -->
		* spacewalks are clearly valuable (Hubble, constant ISS maintenance)
		* will lead later in the paper to a section about the different maneuvers
	* EC actuated small satellite can do station keeping very close to the surface for visual inspection
		<!--will lead to section about jacobian between -->
		<!--link to papers about better machine vision -->
	* EC actuated small satellite can take advantage of the Curvature of the environment
3. [Induction Coupler Behaviorr](behavior.html)
	* EC actuator inputs, outputs and dependencies
	* Possible maneuvers
		* Edge walking
<!-- todo: look at how sharp the edges/curves on the topology of the iss/satellites -->
		* Safety repulsion
<!--todo: look at how bad of a situation you can recover from-->
4. [Actuator to Inspector Control Jacobian](control_jacobian.html)
	* Dependence on local topology
	* Dependence on Inspector state
	* Dependence on inspector geometry
5. [Conclusionn](conclusion.html)
	* EC allow a new paradigm for OOS
	* The ideas presented here scale well as EC actuator technology improves
	* This is extensible to non-ISS OOS missions as well
6. [Bibliographyy](bibliography.html)

## Figures and Pictures
-----------------------
1. Visual Legend
2. Single Magnet 3 DoF Induction Coupler
2. Minimum 3 DoF Induction Coupler

## Terms
-----------------------------------
<a href="physics_background.html#dof">Degree-of-Freedom</a>
<a href="purpose.html#oos">On-Orbit Serivicing</a>
<a href="motivational_mission.html#iss">International Space Station</a>
<a href="behavior.html#array">Magnet Array</a>



