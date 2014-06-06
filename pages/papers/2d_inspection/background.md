---
layout: math_post 
title: Background
tags: [papers]
comments: true
---

### Physics of Induction Couplers

An induction coupler generates relative forces between itself and a target with eddy-current forces. These forces depend on a time-varying magnetic field that first induces a current in a conductive target and then produces a force on that current. 

In broad strokes, the generation of eddy-current forces is a straightforward manifestation of Maxwell's equations.
<!-- reference to old paper -->  

1) Any material with non-infinite conductivity will experience a voltage gradient in response to a time-varying magnetic field.
<!-- Maxwell equation -->
2) The voltage difference drives a current through the material. This current tries to "cancel out" the change in the magnetic field. <!-- Link -->
3) This induced current acts like a wire in a magnetic field, <!-- link --> and experiences a force.

These steps give intuition for the physical process, but they are a gross oversimplification. The currents in the conductor depend on the geometry of the material, material properties, the direction and magnitude of the changes in the magnets in the induction coupler, and the relative velocity between the target and the induction coupler. 


Eddy-current forces can act tangential to the targets’ surface as well as attractive and repulsive. Therefore, a small spacecraft generating a time-varying magnetic field could produce forces in all three translational degrees of freedom. Extending that idea, two sources of these forces separated by a moment arm could also produce torques to orient the spacecraft. 

Both moving permanent magnets and electromagnets with time-varying fields can generate eddy-current forces. A single electromagnet with a sinusoidal driving current will always produce a repulsive force between itself and the target, while replicating that signal with a permanent magnet would require either a closed-loop linear actuator or a complicated set of linkages. Similarly, the simple system comprising a permanent magnet mounted on a motor shaft produces horizontal shear forces between itself and the target. The advantages of different eddy-current generation methods suggests that a multi-degree-of-freedom actuator should utilize both electromagnets - for axial forces - and permanent magnets - for shear forces. 

### Previous Work

