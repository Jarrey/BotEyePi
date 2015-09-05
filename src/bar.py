#!/usr/bin/python
from sys import argv
import zbar
import Image
import io
import setting as s

#BarReader class
class BarReader:
    def __init__(self, region):
        self.bar_region = region
        # create a bar reader
        self.scanner = zbar.ImageScanner()
        # configure the reader
        self.scanner.parse_config('enable')

    def __del__(self):
        # clean up
        del(self.image)

    # private methods
    def __readImage(self, img):
        pil = Image.open(img).crop(self.bar_region).convert('L')
        if s.debug_mode : pil.save('debug.jpg')
        # obtain image data
        width, height = pil.size
        raw = pil.tostring()
        return zbar.Image(width, height, 'Y800', raw)

    def __scanImage(self, img):        
        # scan the image for barcodes
        self.scanner.scan(img)
        # extract results
        for symbol in img:
            # do something useful with results
            return BarResult(symbol.type, symbol.data)
        
    #end of private methods
        
    # public methods
    
    def getSymbol(self, imgStream):
        imgStream.seek(0)
        self.image = self.__readImage(imgStream)
        return self.__scanImage(self.image)
        
    def getSymbol(self, imgPath):
        self.image = self.__readImage(imgPath)
        return self.__scanImage(self.image)
        
    #end of public methods
        
# BarResult class
class BarResult:
    def __init__(self, decoded, data):
        self.decoded = decoded
        self.data = data
        
    def getDecoded(self):
        return self.decoded
    
    def getData(self):
        return self.data
    
    def __str__(self):
        return 'Decoded: %s\nData: %s' % (self.decoded, self.data)


############# test code #############  
if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)

    barreader = BarReader(None)
    print barreader.getSymbol(argv[1])
    del barreader
