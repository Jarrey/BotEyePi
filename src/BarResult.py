#!/usr/bin/python

class BarResult:
    def __init__(self, decoded, data):
        self.decoded = decoded
        self.data = data
        
    def getDecoded(self):
        return self.decoded
    
    def getData(self):
        return self.data
    
    def __str__(self):
        return 'Decoded: %s,\t Data: %s' % (self.decoded, self.data)
