#!/usr/bin/python

########################################################################
#
#  Created by Jarrey (jar_bob@163.com) for Speedpro Inc.
#  Copyright by Speedpro Inc. 2015
#
########################################################################

import picamera
import io
#import bar
import bar_zxing
import setting as s

class Capturer():
    def __init__(self):
        self.__parse_setting()
        self.camera = picamera.PiCamera()
        self.reader = bar.BarReader(self.bar_region)

    def __del__(self):
        self.camera.close()        
        
    def cap(self):
        stream = io.BytesIO()
        self.camera.resolution = self.resolution
        self.camera.capture(stream, format=self.capture_format)
        stream.seek(0)
        return self.__detect_bar(stream)
      
    def __parse_setting(self):    
        if hasattr(s, 'resolution') : self.resolution = s.resolution
        else : self.resolution = (1024, 768)        
        if hasattr(s, 'capture_format') : self.capture_format = s.capture_format 
        else: self.capture_format = "jpeg"
        if hasattr(s, 'bar_region') : self.bar_region = s.bar_region
        else : self.bar_region = (0, 0, self.resolution[0], self.resolution[1])
        if hasattr(s, 'left_marker_region') : self.left_marker_region = s.left_marker_region
        else : self.left_marker_region = (0, 0, self.resolution[0] / 2, self.resolution[1])  
        if hasattr(s, 'right_marker_region') : self.right_marker_region = s.right_marker_region
        else : self.right_marker_region = (self.resolution[0] / 2, 0, self.resolution[0] / 2, self.resolution[1])
          
    def __detect_bar(self, stream):
        return self.reader.getSymbol(stream)

    def __detect_mark(self, stream):
        return None
        

if __name__ == '__main__':
    while True:
        capturer = Capturer()
        print capturer.cap()
