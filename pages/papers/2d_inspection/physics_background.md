---
title: Physics Background
layout: math_post
tags:
- papers
comments: true
linear: true
linear_name: 2d_inspection
next_page: motivational_mission.html
prev_page: alt_tech_background.html
---

### Physics of Induction Couplers

An induction coupler generates relative forces between itself and a target with eddy-current forces. These forces depend on a time-varying magnetic field that first induces a current in a conductive target and then produces a force on that current. 

In broad strokes, the generation of eddy-current forces is a straightforward manifestation of Maxwell's equations. 

1. Any material with non-infinite conductivity will experience a voltage gradient in response to a time-varying magnetic field. <!-- Maxwell equation -->
2. The voltage difference drives a current through the material. This current tries to "cancel out" the change in the magnetic field. <!-- Link -->
3. This induced current acts like a wire in a magnetic field, <!-- link --> and experiences a force.

These steps give intuition for the physical process, but they are a gross oversimplification. The currents in the conductor depend on the geometry of the material, material properties, the direction and magnitude of the changes in the magnets in the induction coupler, and the relative velocity between the target and the induction coupler. The actual forces depend not just on the current, but on the magnetic field's magnitude and direction. Compounding the difficulty is the unavoidable coupling between the magnetic field and the changes in the magnets. These interlocking dependencies make the forces very sensitive to the state of the system - induction actuators are a difficult nonlinear problem. 

Induction couplers can produce forces both tangential and perpendicular to the surface of a target . Therefore, a small spacecraft generating a time-varying magnetic field could produce forces in all three translational degrees of freedom. Extending that idea, two induction couplers separated by a moment arm could also produce torques to orient the spacecraft. 

There are two ways for an induction coupler to generate its changing magnetic fields and resultant forces. While both moving permanent magnets and variable electromagnets can generate those forces, each kind of magnet is especially good at producing different sorts of force. A single electromagnet with a sinusoidal driving current will always produce a repulsive force between itself and the target. Replicating that force with a permanent magnet would require either a closed-loop linear actuator or a complicated set of linkages. Similarly, a simple permanent magnet mounted on a motor shaft easily produces horizontal shear forces between itself and the target, a force that is hard to replicate with electromagnets. It isn't yet clear which combination of permanent and electromagnets optimally generates 6-degree-of-freedom <a name="dof"> </a>(DOF) forces. There may not be an optimal configuration. Instead, the composition of the magnets in an induction coupler may depend on the mission profile - different for an inspection vehicle operating near the surface of a large target than a free-flier maneuvering near a smaller target. This exploration will focus primarily on the former. 

#### References
______________




