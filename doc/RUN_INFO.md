# [src/run.py](../src/run.py) Information #

This script is designed for Speedpro Inc. supports automatically capture/scan and detect the bar-code in components. It contains three parts:

* **Setup GPIO in board**

	To initialize GPIO in board and setup the pins for functions. 

* **Capture bar-code image from component**

	That method will use camera module on the board and capture an image from component. It uses [src/capturer.py](../src/capturer.py), and to use bar (or bar_zxing) to detect the bar-code.

* **Send result via I/O**

	This method is used to send result to next device via serial I/O. So it wraps the result in a format. With a serial perfix and subfix (defined in `setting.py`). 

This module uses **multi-threads** to run bar-code capture and data sending. 