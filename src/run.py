#!/usr/bin/python
import capturer as c
import serial
import thread
import RPi.GPIO as GPIO
import setting as s
import os
import logger as l
import time
import gpio_utilities

ids = []

try:
    ser = serial.Serial(s.ser_dev_name, s.ser_bps)
    capturer = c.Capturer()
except Exception as error:
    l.logger.info(error)
    os.system('reboot')

def setup():
    # Can comment this line to enable the warning for GPIO
    GPIO.setwarnings(s.gpio_warining)
    GPIO.setmode(GPIO.BCM)

    # Setup light sensor pin status
    GPIO.setup(s.switchInPin, GPIO.IN)
    GPIO.setup(s.outputPin, GPIO.OUT)
    GPIO.setup(s.lightPin, GPIO.OUT)

def capture():
    try:
        while True: 
            time.sleep(0.1)           
            # Monitor GPIO to get the control signal
            signal = gpio_utilities.getGPIOInput(s.switchInPin, 5) 
            if signal == s.signal_control:
                
                # Turn on light and capture image
                GPIO.output(s.lightPin, GPIO.HIGH)
                result = capturer.cap()
                
                if result != None :
                    ids.insert(0, result.getData())                
                    GPIO.output(s.outputPin, GPIO.HIGH)
                GPIO.output(s.lightPin, GPIO.LOW)
                
                if s.debug_mode : print "IDs: ", ids
                
                while gpio_utilities.getGPIOInput(s.switchInPin, 5) == s.signal_control: pass
                GPIO.output(s.outputPin, GPIO.LOW)
    except Exception as error:
        l.logger.info(error)
        if s.debug_mode : print error
        pass
                
def control():
    n = False
    while True:    
        time.sleep(0.1)
        try:         
            if ser.read() == s.ser_start_char : n = True        
            cmd = ''
            while (n):
                i = ser.read()
                if i == s.ser_end_char : n = False
                else : 
                    cmd = cmd + i
            
            if s.debug_mode : print "Get command: ", cmd  
            if cmd == s.ser_get_jigid:   
                id = ids.pop()
                if s.debug_mode : print "Send back ID: ", id                            
                ser.write(s.ser_start_char + id + s.ser_end_char)            
        except Exception as error:
            l.logger.info(error)
            if s.debug_mode : print error
            pass 
        

try:    
    setup()
    thread.start_new_thread(capture, ())
    thread.start_new_thread(control, ())
    
    while True: 
        time.sleep(0.5)
        pass
except KeyboardInterrupt:
    del(c)
    GPIO.output(s.lightPin, GPIO.LOW)
    GPIO.cleanup()
    pass
