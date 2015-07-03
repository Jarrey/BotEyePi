# BotEyePi

**A "robot eye" detection for industry based on Python and Rasberry Pi platform**



## Environment
* Python 2.7

## Dependencies
* **python-picamera** A Raspberry Pi camera python moudle to drive camera from python.
	* (in Debian) `sudo apt-get install python-picamera`
* **pyhton-zbar**
	* (in Debian) `sudo apt-get install python-zbar`
* **python-imaging** Python Image Library (PIL)
	* (in Debian) `sudo apt-get install python-imaging`
* **python-opencv**
	* (in Debian) `sudo apt-get install libopencv-dev python-opencv` with opencv dev libraries.


## Features
* Detect bar-code image:
	* `python bar_reader.py [image file path]`
