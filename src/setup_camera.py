#!/usr/bin/python
import picamera
import time

c = picamera.PiCamera()
while True:
    c.start_preview()
    time.sleep(5)
