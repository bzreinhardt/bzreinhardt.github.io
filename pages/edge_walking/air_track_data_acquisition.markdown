---
layout: math_post 
title: Air Track Data Acquisition
tags: [analysis,edge_experiments]
comments: true
---
The goal of the experiment is to answer the question "what is the relationship between the speed/direction of the motors in an induction coupler and the force on the target?" Directly measuring the force or acceleration is hard,[^1] so a better option[^2] is to simultaneously video the movement of the cart and record the commands to the motors. 

<img src="https://docs.google.com/drawings/d/1fKgC4ga7c6hy0xF-isiNm6vD6HfRGn30neQAYKnst5A/pub?w=774&amp;h=358">

[The original video from an off-the-shelf camera.][vid]


 __Synching between motor data and video__ The motors always begin off and motor data acquisition begins before the video. This guarantees that the first frame of the video in which the magnets move synchs with the first data point in the motor data with non-zero command data.

 __Motor Control__ An Arduino issues PWM voltages to motor controllers based on the position of a potentiometer. The commands of the two motors are linked so that they always receive the same commands in opposite directions. The Arduino sends the PWM commands[^3] to each motor and the milliseconds since the program began via a serial connection. The full code is [here.][ArduinoCode]

<!-- references and links -->
[vid]:http://youtu.be/8lF_H1IqPiU
[ArduinoCode]:https://github.com/bzreinhardt/track-video-analysis/blob/master/Arduino%20Code/motor_control_2.ino
[setup_pic]: /pictures/air_track_data_acquisition/setup.jpg
***
 [^1]: Accelerometers have several problems: cheap, small accelerometers are imprecise. High quality accelerometers are expensive and often large. Both sorts need a way to communicate their information, which can happen one of three ways - through wires, through a wireless connection, or on-board stoarge. All three mess up the dynamics of the cart - wires interfere with movement  and the latter two options add mass that creates friction between the cart and the track. Other contactless position sensors have low precision (sonar sensors) or low bandwidth (laser sensors.)
 [^2]: Assuming off-line force calculation is acceptable. 
 [^3]: Ranging from 0-255