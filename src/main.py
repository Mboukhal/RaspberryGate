#!/usr/bin/python
import extractData as exd
import device, os
from rpConfig.config import startFlask
import info

def checkForConfig():
    if not ( info.endpoint and info.token ) :
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
