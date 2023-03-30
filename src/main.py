#!/usr/bin/python

import extractData as exd

class   deviceId():
    def __init__(self):
        self.device = ''
        self.idCard = ''
    
    def getDevice( self ):
        self.device = exd.searchDevice()

    def listenForId( self ):
        print ("listening...")
        status = True
        while status:
            self.getDevice()
            status = exd.getNewId( self.device )
            if status:
                exd.waitForDevice()
    
    def run( self ):
        self.listenForId()

if __name__ == '__main__':
    device = deviceId()
    device.run()