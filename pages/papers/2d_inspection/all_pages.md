---
title: 2D Inspection Outline and Abstract
layout: math_post
tags:
- papers
- indexes
comments: true
---

## Abstract
------------------------
<!-- put picture in abstract -->
Small satellites can enable a new mission profile: investigating larger satellites on orbit. Induction couplers are a new actuation technology that can augment on-orbit servicing. Current technologies for relative actuation between two spacecraft have glaring gaps - they require direct contact or propellant. Induction couplers using the forces between a magnetic field and its induced electric currents could control the relative position between a small chaser spacecraft and a larger target without physical contact. A system utilizing these eddy-current forces places relatively few requirements on the target and chaser compared to more exotic EM actuation systems. This paper presents a system overview of a contactless induction coupler, outlines those requirements through the analysis of an inspection mission on the International Space Station, and compares them to current experimental work.

 <img src = "/pictures/2d_inspection/iss_inspector.jpg" width = "200" height = "200">

## Contents
------------------------
1. [Introduction](#purpose)
	* [Alternative Tech Backgroundd](#alt_tech)
		* There are other ways to generate contactless forces, but all of them have limitations that induction couplers do not.
	* [Physics Background](#physics_background)
		* A brief introduction to the physics behind induction couplers.
2. [Motivational Mission descriptionn](#mission) 
	* Small satellites using induction couplers can replicate a spacewalk in ways that no other technology can
		* Robotics offers opportunities, 
		<!-- Emphasize positive. cit robonaut, be political. Offload astronauts from tasks.[spacewalks are expensive and dangerous] Possibly gravity reference -->
		* Spacewalks are clearly valuable (Hubble, Space Station maintenance)
		* will lead later in the paper to a section about the different maneuvers
	* Small satellites using induction couplers can do station keeping very close to the surface for visual inspection
		<!--will lead to section about jacobian between -->
		<!--link to papers about better machine vision -->
	
3. [Induction Coupler Behavior](#behavior)
	* Description of Inputs, outputs and dependencies
	<!--  Possible maneuvers
		 Edge walking 
		 Safety repulsion-->
<!-- todo: look at how sharp the edges/curves on the topology of the iss/satellites -->
<!--todo: look at how bad of a situation you can recover from-->
4. [Actuator to Inspector Control Jacobian](#jacobian)
	* Dependence on local topology
	* Dependence on Inspector state
	* Dependence on inspector geometry
5. [Conclusion](#conclusion)
	* Induction Couplers enable a new paradigm for on-orbit servicing
	* The ideas presented here scale well as induction coupler technology improves
	
6. [Bibliographyy](#refereces)


## Figures and Pictures
-----------------------


## Terms
-----------------------------------
* [DoF](#dof)
* [OOS](#oos)
* [ISS](#iss)
* [Magnet Array](#array)

### <a name = 'purpose'>Introduction</a>

<!-- What is an induction coupler -->
An induction coupler uses magnetic eddy currents to create forces between itself and a conductive target. The coupler doesn't require direct contact with a target or cooperation from the target. The coupler can also operate on electricity alone, rather than requiring fuel or propellant. If you note that most satellites are skinned in aluminum, this makes induction couplers the closest thing we have to science fiction's tractor beam - a device that can produce contactless forces on an uncooperative target. 

Induction couplers could be particularly useful in space, for three major reasons. First, small forces can have large effects because they are not overwhelmed by gravity, friction, or drag. Second, objects designed for space tend to be fragile, so the ability to interact without potentially damaging direct contact is valuable. Third, propellant and fuel is at a premium in space so the ability to mutually maneuver without expendables can cut costs and extend the useable lifetime of a spacecraft.

A small spacecraft could use an induction coupler to control its own dynamics relative to a much larger target like the international spacestation, crawling along the targets surface without ever touching like the underwater robots that now inspect pipelines and shipwrecks. Increased interest in on-orbit servicing <a name="oos"> </a> (OOS) provides compelling motivation for developing induction couplers. A small inspection vehicle will be primarily concerned with planar motion perpendicular to the surface of the target. This paper will present how this planar motion can be achieved by a small spacecraft equipped with induction couplers. 

### <a name = 'alt_tech'>Alternative Technologies </a>
<!-- Other technologies -->
<!--### Contactless Actuatoion-->

There are other technologies that can produce contactless forces between a spacecraft and a target. Coulombic forces can mediate interactions between two charged spacecraft. <!--ref--> A number of different systems produce contactless forces with magnetic interactions between controlled dipoles on both the spacecraft and the target. !-- ref utah, ref RINGS, ref colorado --> All of these systems require a subsystem on both the chaser and the target (that is, the target must be cooperative.) However, none of the possible targets currently in orbit meet these criteria. Laser tweezers can produce contactless forces on an uncooperative target.  However, the target must be smaller than a micrometer - a size restriction that few spacecraft targets currently in orbit can meet. The restrictions of current technology leaves direct contact as the only option to create forces between two spacecraft.

<!-- Other inspection vehicles 
	SPHERES
	AerCAM'
	-->


	



### <a name = 'physics_background'>Physics of Induction Couplers </a>


An induction coupler generates relative forces between itself and a target with eddy-current forces. These forces depend on a time-varying magnetic field that first induces a current in a conductive target and then produces a force on that current. 

In broad strokes, the generation of eddy-current forces is a straightforward manifestation of Maxwell's equations. 

1. Any material with non-infinite conductivity will experience a voltage gradient in response to a time-varying magnetic field. <!-- Maxwell equation -->
2. The voltage difference drives a current through the material. This current tries to "cancel out" the change in the magnetic field. <!-- Link -->
3. This induced current acts like a wire in a magnetic field, <!-- link --> and experiences a force.

These steps give intuition for the physical process, but they are a gross oversimplification. The currents in the conductor depend on the geometry of the material, material properties, the direction and magnitude of the changes in the magnets in the induction coupler, and the relative velocity between the target and the induction coupler. The actual forces depend not just on the current, but on the magnetic field's magnitude and direction. Compounding the difficulty is the unavoidable coupling between the magnetic field and the changes in the magnets. These interlocking dependencies make the forces very sensitive to the state of the system - induction actuators are a difficult nonlinear problem. 

Induction couplers can produce forces both tangential and perpendicular to the surface of a target . Therefore, a small spacecraft generating a time-varying magnetic field could produce forces in all three translational degrees of freedom. Extending that idea, two induction couplers separated by a moment arm could also produce torques to orient the spacecraft. 

There are two ways for an induction coupler to generate its changing magnetic fields and resultant forces. While both moving permanent magnets and variable electromagnets can generate those forces, each kind of magnet is especially good at producing different sorts of force. A single electromagnet with a sinusoidal driving current will always produce a repulsive force between itself and the target. Replicating that force with a permanent magnet would require either a closed-loop linear actuator or a complicated set of linkages. Similarly, a simple permanent magnet mounted on a motor shaft easily produces horizontal shear forces between itself and the target, a force that is hard to replicate with electromagnets. It isn't yet clear which combination of permanent and electromagnets optimally generates 6-degree-of-freedom <a name="dof"> </a>(DOF) forces. There may not be an optimal configuration. Instead, the composition of the magnets in an induction coupler may depend on the mission profile - different for an inspection vehicle operating near the surface of a large target than a free-flier maneuvering near a smaller target. This exploration will focus primarily on the former. 



### <a name = 'mission'> Motivational Mission </a>

<img src = "/pictures/2d_inspection/iss_inspector.jpg" width = "200" height = "200"> 

A small inspection spacecraft can use induction couplers to crawl along the surface of a larger target spacecraft without physically grappling the target. The inspector can fulfill a number of functions including investigating problematic areas, scanning for damage, performing small tasks, or providing support for astronauts on space walks. This paper will focus on the International Space Sation <a name="iss"></a>(ISS), but a similar inspection spacecraft could enable unique OOS missions to inspect and repair other large satellites.

The inspection spacecraft would use induction couplers to pull itself along the aluminum surface of the ISS, maintaining a separation distance of a few centimeters. From this vantage point, it could act like a damage-inspection roomba, canvassing the surface and automatically detecting damage from micrometeorite strikes. It could also be controlled directly by an astronaut in the space station to look at a problem area and possibly use an attached robotic arm to perform small actions. During spacewalks, the spacecraft could act like an extra pair of hands, remaining near an astronaut and holding tools. Robotnaut <!-- citation --> and the Canada Arm have demonstrated the value of this role, but are limited by rails to specific locations. 

The ability to span the exterior of the ISS without being constrained by rails or fuel supply can free up one of the most valuable resources on the ISS - astronaut time. 

### <a name = 'behavior'> Induction Coupler Behavior </a>


Spinning-magnet induction couplers consist of  <a name = "array"> arrays </a> of one or more permanent magnets spinning on axes perpendicular to their dipole moment. The perpendicular orientation between the dipole moment and the spin axis maximizes the changes in the magnetic field as a motor spins the magnets. For consistency, these arrays are portrayed as a single dipole, but could consist of any number of magnets.[^1] <!-- TODO put in magnet picture -->
<figure>
<img src="https://docs.google.com/drawings/d/1XHJnncLGJkWnTkd02plwKgFV4Qtmm0zb3iikBr1uOlQ/pub?w=474&amp;h=263">
<figcaption> Diagram of Magnet Arrays with one dipole (left) and four dipoles (right)
</figcaption>
</figure>

The simplest induction-coupled system is a single array spinning on an axis perpendicular to a flat conductive surface. In this case, the coupler will produce a force perpendicular to <!-- the spin axis crossed with the surface --> \\( \mathbf{\omega} \times \textbf{r} \\).
<figure>
<img src="https://docs.google.com/drawings/d/1uwVR5Mcwh1GAjPA3Dt0PBwJQVE0dzptc1hgQqLCV9Uc/pub?w=474&amp;h=263">
<figcaption> A dipole spinning clockwise above a target that extends out of the page will generate a force to the left.
</figcaption>
</figure>
<!-- TODO put in video -->

Each array can only directly generate a force. The array can use this force to torque the spacecraft if it is located so there is a moment arm between the spacecraft's center of mass and the array. Experimental demonstration of an induction coupler have shown that these forces vary with the magnitude and sign of \\(\mathbf{\omega}\\). [Preliminary results](../edge_walking/air_track_force_analysis.html) show milliNewton shear forces perpendicular to a surface using small motors and permanent magnets. Two small motors[^4] driven by 12V at a 25% duty cycle while holding two neodymium permanent magnets have together generated 5 mN, or 2.5 mN apiece. Spinning at 4200 RPM, each motor drew 0.25 amps of current, dissipating 0.75 Watts of electrical power. This power consumption corresponds to a 3.33 mN/Watt force per power ratio. 

<img src="https://docs.google.com/drawings/d/1IPDk7SiyBEATDIrY5CKoQ60U-1c37dVs9MlSfIGoZ74/pub?w=474&amp;h=263"> 
__Picture of Experimental Setup: cart wth aluminum plate on left. The magnets on the right are rotating around axes pointed down.__

<!-- plot of force to demonstrate its magnitude -->
{% include plot_img.html url = "https://plot.ly/~bzreinhardt/0" description = "Force vs. motor speed for a small two-motor induction coupler" %}

 The angular velocity of the array can control the force because the induced voltage scales with \\(\left \| v \times B \right \| \\) where \\(v = \omega \times d\\)[^2] is the relative velocity between the target conductor and the magnetic field.[^3]

<a name = "dependencies"></a>
The force between the spinning array and the target also depends both on the system state, he design of the induction coupler, and the properties of the target. The forces decrease with \\(\frac{1}{d^4}\\). Larger magnets will increase the forces generated by the induction coupler for a given spin speed. Greater thickness and conductivity of the target both increase the induced current and scale the force. 


### <!-- references and links -->
***
[^1]: As the number of magnets increases on an array of a given size, the magnetic field will necessarily become smoother, becoming uniform as the number of magnets goes to infinity. This smoothing decreases the change in the magnetic field as the magnets spin. The number of magnets per array is one of the many considerations in the design of an induction coupler.
[^2]: Where \\(d\\) is the separation between the conductor and the array
[^3]: The direct scaling between force and \\(\omega\\) makes two assumptions: that \\(\frac{1}{\omega\\}) is much larger than the characteristic time of the inductor and that the relative velocity between the inspection spacecraft and the target is much smaller than the tangential velocity of the magnetic field seen by the target. 
[^4]: Motor - 

### <a name = 'jacobian'>Control Jacobian</a>

The rotational speed of each array controls the force between that array and the surface of the target. The sum of the forces from all the arrays and their resultant torques can be mapped through the linearized spacecraft dynamics to plan control inputs based on a desired maneuver. 

<a name="assumptions"></a>This analysis assumes that the inspection spacecraft maintains a small constant distance from the surface.[^5] With an operating range of a few centemeters, the surface for most of the ISS will look to the inspection spacecraft like an infinite plane. The analysis assumes that the proposed inspection vehicle conforms to the cubesat standard so the mass of the entire system will not exceed m = 4 kg.[^6]

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

$$ \hat{\textbf{\emph{r}} = \begin{bmatrix} \frac{\sqrt{2}}{2} & 0 & -\frac{\sqrt{2}}{2} \\
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

In this configuration on a 4 kg spacecraft, an induction coupler can generate a linear acceleration of \\(2* 10^{-3}\frac{m}{\text{s}^2} \\) and an angular acceleration of \\(9*10^{-3}\frac{\text{rad}}{s^2}\\).[^7] These values, while modest, will allow an inspection vehicle to overcome perturbance forces and move slowly over the surface of the ISS. Recall also that these values are based on a small prototype and an induction coupler with only three magnet arrays. Additional arrays and optimized hardware are two straightforward ways to increase the capabilities of an induction-coupled spacecraft. 
<!-- TODO what kind of analyses are really worthwhile ?-->




***
[^5]: This is not a trivial problem and deserves its own treatment.
[^6]: [Cube Sat Requirements](http://browncubesat.org/wp-content/uploads/2013/01/Cubesat-Reqs.pdf)
[^7]: \\(a = \frac{F}{m}\\) . Assuming a spherical spacecraft with r = 0.1 m. \\(I = \frac{2mr^2}{3}\\). \\(\alpha = \frac{\tau}{I}\\)---

### <a name = 'conclusion'>Conclusion</a>

There are many paths for future induction coupler research. The frequency response of the system and its sensitivity to system state and environment are important to future designs. This analysis assumed planar motion - remaining in that plane is a challenge in itself, and ideally the inspection vehicle would have full 6-degree-of-freedom maneuverability. 

This paper presents a starting point for induction coupler technology. It describes [the physics](physics) of spinning magnet arrays producing contactless forces and torques on any conductive target. [Preliminary experiments verified and measured these forces](behavior). [When coupled together, three or more arrays can produce 3 independent degrees of freedom in the plane above the target's surface.](jacobian)  

[This paper presents a completely new method for small-spacecraft mobility.](intro)Induction couplers can generate forces between an inspection spacecraft and any conductive target using only electric power and without physical contact. This capability is especially valuable for [on-orbit servicing of valuable targets like the ISS.](mission) 

### <a name = 'references'> References </a>
______________

### <a name = 'foot'> Footnotes </a>
--------------
[intro]:purpose.html
[physics]: physics_background.html
[mission]: motivational_mission.html
[jacobian]: control_jacobian.html
[behavior]: behavior.html