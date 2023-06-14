#!/usr/bin/python

import evdev
import requests
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
                gate = req.isValid( dataId, device.phys )
                if gate != -1:
                    gc.openGate(gate)
                print(dataId)
                dataId = ''
    except:
        pass
