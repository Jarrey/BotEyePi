#!/usr/bin/python

########################################################################
#
#  Created by Jarrey (jar_bob@163.com) for Speedpro Inc.
#  Copyright by Speedpro Inc. 2015
#
########################################################################

from sys import argv
import zxing
import Image
import io
import setting as s

#BarReader class
__tmp_img__ = './.tmp/__tmp__.jpg'
class BarReader:
    def __init__(self, region):
        self.bar_region = region
        # create a bar reader
        self.scanner = zxing.BarCodeReader(s.zxing_lib_loc + s.zxing_ver)		
        
    def __del__(self):
        # clean up, to delete the tmp file
        if os.path.isfile(__tmp_img__):  
        try:  
            os.remove(__tmp_img__)  
        except:  
            pass 

    # private methods
    def __readImage(self, img):
        pil = Image.open(img).crop(self.bar_region).convert('L')
        if s.debug_mode : pil.save('debug.jpg')
        pil.save(__tmp_img__)
        del pil
        return __tmp_img__

    def __scanImage(self, img):        
        # scan the image for barcodes
        symbol = self.scanner.decode(img)
        # extract results
        return BarResult('zxing detected', symbol.data)
        
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
