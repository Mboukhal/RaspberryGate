#!/usr/bin/python

import evdev
import requests
import os
import gpioControl as gc
import requistAccess as req
from logs import log

# parss keys
def parssId( ev ):
    if isinstance(ev, evdev.events.KeyEvent) and ev.keystate:
        return ev.keycode[-1]

def	collectId( device ):
    dataId = ''
    try:
        # collect data from usb file
        for event in device.read_loop():
            ev = evdev.categorize(event)
            data = parssId( ev )
            if data and len(data) == 1 and data.isnumeric():
                dataId += data
            elif data:
                # try to open gate
                if req.isValid( dataId ):
                    gc.openGate()
                print(dataId)
                dataId = ''
    except KeyboardInterrupt:
        device.close()
        print("\rExiting program...")
        return False
    except requests.exceptions.MissingSchema:
        device.close()
        print( 'Need to set info in info.py' )
        log().info( 'Need to set info in info.py' )
        return False
    except Exception as e:
        print(str(e))
        print( "Reader Disconnected." )
        log().info( 'Reader Disconnected.' )
    return True
