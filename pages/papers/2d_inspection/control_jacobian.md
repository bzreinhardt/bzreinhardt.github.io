---
layout: math_post 
title: Control Jacobian
tags: [papers]
comments: true
linear: true
linear_name: 2d_inspection
next_page: conclusion.html
prev_page: behavior.html
---

The rotational speed of each array controls the force between that array and the surface of the target. The sum of the forces from all the arrays and their resultant torques can be mapped through the linearized spacecraft dynamics to plan control inputs based on a desired maneuver. 

<a name="assumptions"></a>This analysis assumes that the inspection spacecraft maintains a small constant distance from the surface.[^1] With an operating range of a few centemeters, the surface for most of the ISS will look to the inspection spacecraft like an infinite plane. The analysis assumes that the proposed inspection vehicle conforms to the cubesat standard so the mass of the entire system will not exceed m = 4 kg.[^2]

<a name = "magnum"></a> An induction coupler with only one or two spinning arrays can achieve planar motion, but it would not be holonomic - its ability to move in a desired direction would depend on its orientation. Three spinning arrays are needed to achieve three independent degrees of freedom. In implementation, more should be used for redundancy and greater control authority. As long as the arrays have sufficient separation, their forces will sum. These advantages will be a tradeoff with the additional power, weight, and number of moving parts introduced by the additional arrays.

In the induction coupler each array is located at some radius, \\(\textbf{r}\\), from the spacecraft's center of mass. Each array has a spin axis (\\(\hat{\textbf{a}}\\)) oriented parallel to the target surface at an angle \\(\phi\\) from the x-axis in spacecraft coordinates. 

<figure>
<img src="https://docs.google.com/drawings/d/1KdWXSclkymvUB7jrDnPewwD0Q3GvkfkN_5vG76apnZ8/pub?w=474&amp;h=263">
<figcaption> Diagram of a single array.
</figcaption>
</figure>

For N arrays, the transformation between the angular speeds of the arrays and the net force and torque on the spacecraft is:

$$ \begin{bmatrix} F_x\\F_y\\\tau \end{bmatrix} = \begin{bmatrix} \cos{(\phi_1 -\pi/2)} & \cos{(\phi_2 -\pi/2)} & ... & \cos{(\phi_N -\pi/2)} \\
\sin{(\phi_1 -\pi/2)} & \sin{(\phi_2 -\pi/2)} & ... & \sin{(\phi_N -\pi/2)} 
\\\textbf{r}_1\cdot \hat{\textbf{a}}_1 & \textbf{r}_2 \cdot \hat{\textbf{a}}_2 & ... & \textbf{r}_N \cdot \hat{\textbf{a}}_N \end{bmatrix}
\begin{bmatrix} \omega_1\\\omega_2\\...\\\omega_N \end{bmatrix}$$

The speed-force Jacobian imposes constraints on the design of the induction coupler. 

* \\(\textbf{r}_i \cdot \hat{\textbf{a}}_i\\) must be nonzero for at least one array, dictating that all of the spin axes cannot be perpendicular their moment arms, nor can all \\(r_i\\) be zero - some of the arrays cannot be at the spacecraft's center of mass.
* All of the axis angles cannot be in a line. This would cause all \\(\phi_i\\) to be integer multiples of \\(\pi \\) apart, and the Jacobian would not be full rank.

For a sense of the maneuverability, take the specific case of an inspection vehicle equipped with an induction coupler consisting of three magnet arrays with \\(\left \| r \right \| =0.1 \text{cm}\\)

$$\mathbf{\phi} = \begin{bmatrix} \frac{3\pi}{4}&\frac{pi}{2}&\frac{pi}{4}\end{bmatrix} $$ 

and 

$$ \hat{\textbf{r}} = \begin{bmatrix} \frac{\sqrt{2}}{2} & 0 & -\frac{\sqrt{2}}{2} \\
\frac{\sqrt{2}}{2} & 1 & \frac{\sqrt{2}}{2}\end{bmatrix} $$ 

<figure>
<img src="https://docs.google.com/drawings/d/1NNcgmmLkylAJuXrgxlEbyjmNYzpxVGD_Ov-WgdYSUHI/pub?w=474&amp;h=263">
<figcaption> Example induction coupler architecture with three magnet arrays.
</figcaption>
</figure>

The Jacobian will be:

$$ \begin{bmatrix} F_x\\F_y\\\tau \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2} & 1 & \frac{\sqrt{2}}{2} \\
\frac{\sqrt{2}}{2} & 0  & -\frac{\sqrt{2}}{2}
\\0  &  1 & 0 \end{bmatrix}
\begin{bmatrix} \omega_1\\\omega_2\\\omega_3 \end{bmatrix}$$

This Jacobian ignores the constants scaling \\(F_x\\), \\(F_y\\), \\(\tau\\) [based on the system state and physical constants of the target.](behavior.html#dependencies) 

In this configuration on a 4 kg spacecraft, an induction coupler can generate a linear acceleration of \\(2* 10^{-3}\frac{m}{\text{s}^2} \\) and an angular acceleration of \\(9*10^{-3}\frac{\text{rad}}{s^2}\\).[^3] These values, while modest, will allow an inspection vehicle to overcome perturbance forces and move slowly over the surface of the ISS. Recall also that these values are based on a small prototype and an induction coupler with only three magnet arrays. Additional arrays and optimized hardware are two straightforward ways to increase the capabilities of an induction-coupled spacecraft. 
<!-- TODO what kind of analyses are really worthwhile ?-->




***
[^1]: This is not a trivial problem and deserves its own treatment.
[^2]: [Cube Sat Requirements](http://browncubesat.org/wp-content/uploads/2013/01/Cubesat-Reqs.pdf)
[^3]: \\(a = \frac{F}{m}\\) . Assuming a spherical spacecraft with r = 0.1 m. \\(I = \frac{2mr^2}{3}\\). \\(\alpha = \frac{\tau}{I}\\)