#!/usr/bin/python

import extractData as exd
import device

if __name__ == '__main__':
    status = True
    while status:
        deviceEv = device.searchDevice()
        if deviceEv:
            status = exd.collectId( deviceEv )
        if status:
            device.waitForDevice()
