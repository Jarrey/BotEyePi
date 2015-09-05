#!/usr/bin/python
import picamera
import time
import RPi.GPIO as GPIO
import setting as s

# Can comment this line to enable the warning for GPIO
GPIO.setwarnings(s.gpio_warining)
GPIO.setmode(GPIO.BCM)
GPIO.setup(s.lightPin, GPIO.OUT)
GPIO.output(s.lightPin, GPIO.HIGH)
c = picamera.PiCamera()
c.resolution = s.resolution

try:
    while True:
        c.start_preview()
        time.sleep(5)
except KeyboardInterrupt:
    pass