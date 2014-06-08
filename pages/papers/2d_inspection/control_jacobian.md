---
layout: math_post 
title: Control Jacobian
tags: [papers]
comments: true
linear: true
linear_name: 2d_inspection
next_page: conclusion.html
prev_page: behaviors.html
---

The rotational speed of each array controls the force between that array and the surface of the target. The sum of the forces from all the arrays and their resultant torques can be mapped through the linearized spacecraft dynamics to plan control inputs based on a desired maneuver. 

<a name="assumptions"></a>This analysis assumes that the inspection spacecraft maintains a small constant distance from the surface.[^1] With an operating range of a few centemeters, the surface for most of the ISS will look to the inspection spacecraft like an infinite plane. 

<a name = "magnum"></a> An induction coupler with only one or two spinning arrays can achieve planar motion, but it would not be holonomic - its ability to move in a desired direction would depend on its orientation. Three spinning arrays are needed to achieve three independentent degrees of freedom. In implementation, more should be used for redundancy and greater control authority. As long as the arrays have sufficient separation, their forces will sum. These advantages will be a tradeoff with the additional power, weight, and number of moving parts introduced by the additional arrays.

In the induction coupler each array is located at some radius, \\(\textbf{r}\\), from the spacecraft's center of mass. Each array has a spin axis oriented parallel to the target surface at an angle \\(\phi\\)in spacecraft coordinates. For N arrays, the transformation between the angular speeds of the arrays and the net force and torque on the spacecraft is:

$$ \begin{bmatrix} F_x\\F_y\\\tau \end{bmatrix} = \begin{bmatrix} \cos{(\phi_1 -\pi/2)} & \cos{(\phi_2 -\pi/2)} & ... & \cos{(\phi_N -\pi/2)} \\
\sin{(\phi_1 -\pi/2)} & \sin{(\phi_2 -\pi/2)} & ... & \sin{(\phi_N -\pi/2)} 
\\r_1 & r_2 & ... & r_N \end{bmatrix}
\begin{bmatrix} \omega_1\\\omega_2\\...\\\omega_3 \end{bmatrix}$$  

***
[^1]: This is not a trivial problem and deserves its own treatment.