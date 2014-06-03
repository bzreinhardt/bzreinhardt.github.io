---
layout: post 
title: "Air Track Image Analysis"
tags: [analysis,edge_experiments]
date: 2014-5-26
comments: true
categories: [Thesis]
---

A sequence of image processing tricks turn the [raw video][vid] of the cart moving on an air track into an absolute position measurement.[^4] There are two major steps:

1. Locating the left side of the cart in pixel coordinates
2. Locating the positions of the 10cm markers in pixel coordinates
3. Finding the conversion between the pixel coordinate system and the cart coordinate system. 

<!-- IMAGE OF BOTH COORDINATE SYSTEMS -->
<img src="https://docs.google.com/drawings/d/1IPDk7SiyBEATDIrY5CKoQ60U-1c37dVs9MlSfIGoZ74/pub?w=960&amp;h=720">

__Locating the left side of the cart in pixel coordinates__ 
The algorithm makes the frame black and white, performs an [extended-maxima transform][em transform] (increasing the contrast) and removes all small objects.[^1] The cart is the largest dark object in the video so the left-most point of the largest object in the frame will be the left-most point of the cart.[^2]


__Locating the positions of the 10cm markers in pixel coordinates__ 
The algorithm clips the bottom third of the video frame to isolate the track. The algorithm converts the frame from an rgb to an [Lab color scheme][Lab] and creates a mask based on the distance between the a and b values of each pixel and the experimentally determined average a and b values of the red markers.[^3] The algorithm converts the frame to black and white, applies the mask, dilates the remaining pixels, eliminates small structures, and finds the centroids of the three largest structures remaining. These three centroids correspond to the middle of the three 10cm markers. 

{% include image.html url="/pictures/air_track_image_analysis/roi_with_mask.jpg" description="Masked air track with algorithmically generated 10cm marker locations" %}

__Finding the conversion between the pixel coordinate system and the cart coordinate system.__
With the locations of the 10cm markers, it is simple to convert the left side of the cart into absolute position on the track in each frame. The algorithm sets the origin of both coordinate systems as the position of the leftmost marker and finds a scaling factor between pixels and centimeters based on the length of the vectors to the second and third marker. Normalized vectors in each coordinate system generate a rotation matrix between the two. 

The combination of the scale factor, relative origin positions, and rotation matrix can convert the position of the cart in pixels into the track coordinates. Here, the X coordinates are the unconstrained values that are valuable to analyze.   

The code for this process can be found [here](https://github.com/bzreinhardt/track-video-analysis/tree/master).


__Upgrades__
In the future, this process can be made more precise with explicit markers. However, this process illustrates how to extract data from video from an experiment not explicitly designed for post-processing.


<!-- Links and references -->
[vid]:http://youtu.be/8lF_H1IqPiU
[Lab]:http://en.wikipedia.org/wiki/Lab_color_space
[em transform]:http://www.mathworks.com/help/images/ref/imextendedmax.html
***
 [^1]: In this case, smaller than 50 pixels. 
 [^2]:  The left-side-point on the cart doesn't need to have a consistent height because the entire left side of the cart is at the same x-coordinate in the cart coordinate system. 
 [^3]: The a and b values used were 143 and 132. The threshold value (above which the mask decided the pixel was 'not red') was 6.
 [^4]: Despite camera jitter and focus changes.