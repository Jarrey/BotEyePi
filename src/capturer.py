#!/usr/bin/python
import zbar
import picamera
import io
import Image
import time
import bar

class Capturer():
    def __init__(self, setting):
        self.setting = setting
        self.camera = picamera.PiCamera()
        self.reader = bar.BarReader(self.setting)

    def cap(self):
      while True:
          stream = io.BytesIO()
          self.camera.capture(stream, format='jpeg')
          stream.seek(0)
          print self.reader.getSymbol(stream)


if __name__ == '__main__':
    capturer = Capturer(None)
    capturer.cap()
