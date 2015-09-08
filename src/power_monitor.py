#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import gpio_utilities

power_pin = 43

# Can comment this line to enable the warning for GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setup light sensor pin status
GPIO.setup(power_pin, GPIO.IN)

try:
    while True:
        if gpio_utilities.getGPIOInput(power_pin1, 20) == GPIO.LOW:
            # print GPIO.input(power_pin)
            os.system("halt")
        time.sleep(1)
except KeyboardInterrupt:
    pass
