#!/usr/bin/python

import extractData as exd

if __name__ == '__main__':
    status = True
    while status:
        device = exd.searchDevice()
        if device:
            status = exd.getNewId( device )
        if status:
            exd.waitForDevice()
