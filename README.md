# BotEyePi

**A "robot eye" detection for industry based on Python and Rasberry Pi platform**



## Environment
* Python 2.7
	* `sudo apt-get install python`

## Dependencies
* **python-picamera** A Raspberry Pi camera python moudle to drive camera from python.
	* (in Debian) `sudo apt-get install python-picamera`
* **pyhton-zbar**
	* (in Debian) `sudo apt-get install python-zbar`
* **pyhton-RPi.GPIO**
	* (in Debian) `sudo apt-get install python-RPi.GPIO`
* **python-imaging** Python Image Library (PIL)
	* (in Debian) `sudo apt-get install python-imaging`
* **python-serial** Python serial port library
	* (in Debian) `sudo apt-get install python-serial`
* **python-opencv** (Optional)
	* (in Debian) `sudo apt-get install libopencv-dev python-opencv` with opencv dev libraries.
	* For using opencv (without dev libraries) `sudo apt-get install python-opencv`


## Setup
* For serial port: 
	* Delete `console=ttyAMA0,115200 kgdboc=ttyAMA0,115200` from `/boot/cmdline.txt`
	* Comment line `T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100` in `/etc/inittab`
* Manually add two lines in `/etc/rc.local` to enable run program while system startup
	 `/usr/bin/python /speedpro/run.pyc &`
	 `/usr/bin/python /speedpro/power_monitor.pyc &`


## Complie Code and Deployment
* Execute `src/build.sh` script and copy all files from `src/bin` (use command `chmod +x build` to add execution permission for build script)

## Features (For Debugging)
* Detect bar-code image:
	* `python bar.py [image file path]`
* Detect the circle count from one image:
	* `python detector.py [image file path]`
* Real time to detect the bar-code:
	* `python capturer.py`
	* Before use `capturer.py`, please use `setup_camera.py` to set the Pi Camera and set the force and field.
