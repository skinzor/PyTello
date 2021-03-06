# PyTello

![FaceTracking.gif](/FaceTracking.gif)
Longer video can be found [here](https://youtu.be/6VKUbbYWZ3c)!
Using various image processing to control [DJI Tello](https://store.dji.com/shop/tello-series). The video is streamed from Tello to a laptop and processed off board. The laptop then send commands to the drone. The goal of this project is to learn high-level control for drones.

## Libraries and Packages
* OpenCV
* imutils
* Flask

## Programs
Below is list of programs available in this repository

### FaceDetection
The face detection algorithm is based on [OpenCV library](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html)

### DroneController
The DroneController is taken from [Damia Fuentes' Repo](https://github.com/damiafuentes) with a few modifications

### WebBasedGUI
Flask is used for the GUI

### main
