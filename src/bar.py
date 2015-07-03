#!/usr/bin/python
from sys import argv
import zbar
import Image

#BarReader class
class BarReader:
    def __init__(self, imagePath, setting):
        self.setting = setting
        # create a bar reader
        self.scanner = zbar.ImageScanner()
        # configure the reader
        self.scanner.parse_config('enable')
        pil = Image.open(imagePath).convert('L')
        # obtain image data
        width, height = pil.size
        raw = pil.tostring()
        self.image = zbar.Image(width, height, 'Y800', raw)
        
    def getSymbol(self):
        # scan the image for barcodes
        self.scanner.scan(self.image)
        # extract results
        for symbol in self.image:
            # do something useful with results
            return BarResult(symbol.type, symbol.data)
        
    def __del__(self):
        # clean up
        del(self.image)

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
    
if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)

    barreader = BarReader(argv[1], None)
    print  barreader.getSymbol()
    del barreader
