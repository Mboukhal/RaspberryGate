#!/usr/bin/python

import extractData as exd
import device
from rpConfig.config import startFlask

def checkForConfig():
    if not os.path.exists( "info.py" ):
        startFlask()  

if __name__ == '__main__':

    checkForConfig()
    status = True
    while status:
        deviceEv = device.searchDevice()
        if deviceEv:
            status = exd.collectId( deviceEv )
        if status:
            device.waitForDevice()
