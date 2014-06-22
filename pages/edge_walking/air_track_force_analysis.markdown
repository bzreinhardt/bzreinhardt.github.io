---
layout: math_post 
title: Air Track Force Analysis
tags: [analysis,edge_experiments]
comments: true
---
The goal here is to investigate the correlations between spinning magnets' speed and direction and the resultant forces on an aluminum edge that the induction coupler straddles. 

A [Savitzky-Golay Filter][] [smooths and differentiates][numDif] the numerical position data from the [video analyis](air_track_image_analysis.html) after an interpolation increases the data sample rate.[^1]  The filter finds a second order least-squares polynomial fit to the function over the size of the window as it moves across the data. The filter then evaluates this fit and its derivatives at the point in the middle of the window. 

The Savitzky-Golay Filter produces smoother derivatives of the position than finite differences passed through a low-pass filter without losing information.[^2] 

<!-- Put in equations for the polynomials maybe --> 


<!-- Perhaps replace the filename with a liquid post name tag -->
 ![x_data](/pictures/air_track_force_analysis/all_data.jpg)

 This figure shows (from top to bottom)

 1.	The interpolated position data
 2. The filtered position data
 3. The velocity data from the derivative of the filtered position data
 4. The acceleration data from the derivative of the filtered position data 

{% include plot_img.html url = "https://plot.ly/~bzreinhardt/0" description = "Force on cart synched with motor commands" %}


Converting the cart's acceleration to the external forces on the cart[^3] and synching with the motor-command data shows the following results [(recall the setup)][data acq]:

* Faster Motor speeds yield to larger forces in either direction. 
* Outward spinning magnets produce repulsive (-X direction) forces. (Magnet 1 negative and Magnet 2 positive)
* Inward spinning magnets produce attractive (+X direction) forces. (Magnet 1 positive and Magnet 2 negative)
* The forces on the cart have a maximum magnitude of 8 mN when the motor is at 25% of maximum voltage. 

(Update 6/8/2014)
__Conversion between PWM and motor speed__ [^4] The motor has a no load speed of 16800. The effective voltage is 

$$ V_eff = V_0 \frac{\tau_0}{tau_c} $$ [^5] 

where \\(\frac{\tau_0}{tau_c}\\) is the % on-time shown in the graph and \\(V_0\\) is the input voltage (12 V.)

<a name = "specs"><a>
In this case the maxiumum force occurs at a 25% duty cycle, which corresponds to 4200 RPM and 0.25 amps. At 3 V and 0.25 amps, the motor will dissipate 0.75 Watts of electrical power. The motor needs additional power to start and turn direction, but the amount of electrical power disappated is important to consider for space applications. The disappated power will leave the battery and turn into heat.


__Future Things to Explore__

* Functional relationship between maximum motor speed and force - does the force increase linearly with motor speed or does the increase in force with increased motor speed drop off above a certain speed? It could be expected to drop off for two reasons: 
1)	Because [the skin effect][SE] reduces the volume of currents in the aluminum. 
2)	Because faster spinning magnets actually reduce the change in magnetic field seen by the target - think of how a quickly flickering light begins to blur and eventually looks like a single steady light. 

* Creating a bode plot of the system response in frequency space. 

The code for this analysis can be found [here][pos2Acc].



<!-- FOODNOTES AND REFERENCES -->

[Savitzky-Golay Filter]:http://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter_for_smoothing_and_differentiation
[numDif]:http://en.wikipedia.org/wiki/Numerical_differentiation
[data acq]: air_track_data_acquisition.html
[SE]: http://en.wikipedia.org/wiki/Skin_effect
[pos2Acc]: https://github.com/bzreinhardt/track-video-analysis/blob/master/Scripts/pos2accTest.m
***
 [^1]:  The interpolation increased the sampling rate by five times to a 3 millisecond timestep.
 [^2]:  The filter's window size \\(w = 201 \\) frames - 0.3 seconds is still fast compared to the dynamics.
 [^3]: \\(F = ma\\) with m = 294.5 g
 [^4]: Using a BaneBots RS540 Motor - 12V. It has a stall torque of 280 mN-m, so a force of 8 mN at a few centimeters is orders of magnitude below the stall torque. This means we can assume that it is effectively acting with at its no load RPM and current - 16800 RPM and one amp.
 [^5]: http://web.cecs.pdx.edu/~gerry/class/EAS199A/topics/pdf/PWM_output_Arduino.pdf