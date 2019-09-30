# [PYTHON] Photomosaic generator

## Introduction

Here is my python source code for Photomosaic generator. To the best of my knowledge, my code is the shortest one you could find out for this goal (< 30 lines of code). With my code, you could: 

* **Given input image, you could generate Photomosaic art stored under image formats (.png, .jpg, ...)**
* **Given input video, you could generate Photomosaic art stored under video formats (.avi, .mp4, ...)**


## Data preparation
In order to run my script, you first need to prepare a set of photos put in the same folder (my default folder is **image_pool**). These photos could be in any image format (jpg, png, ...) with any resolution. In this repository, I put all photos used to generate the demo for video2video case (Taylor Swift's photos taken from the internet). For image2image case, I used photos from VOC2012 dataset [link](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/).

## Video to video
By running the sript **video2video.py**, we will have following output:
<p align="center">
  <img src="demo/output.gif" width=800><br/>
  <i>Output video</i>
</p>


## Image to image
By running the sript **image2image.py**, we will have following output:
<p align="center">
  <img src="demo/output.jpg" width=800><br/>
  <i>Output image</i>
</p>


<p align="center">
  <img src="demo/input.jpg" width=800><br/>
  <i>Input image</i>
</p>

## Requirements

* **python 3.6**
* **cv2** 
* **numpy**
