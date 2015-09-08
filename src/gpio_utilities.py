#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# pin: GPIO pin number
# delay: delay times in 0.01 second, default value is 0 (no delay)
def getGPIOInput(pin, delay = 0):
    try:
        i = -1
        value = 0 
        while i < delay:
            value = GPIO.input(pin)
            time.sleep(0.01)
            i = i + 1
        return value
    except:
        raise
            

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)
    while True:
        # print "original: ", GPIO.input(14)
        print "new: ", getGPIOInput(14, 10)
