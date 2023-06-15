#!/usr/bin/python

import evdev
import requests
import gpioControl as gc
import requistAccess as req
from logs import log
import netifaces


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
                if gate == "no":
                    log().info(f"{dataId} - Access denied")
                elif gate:
                    log().info(f"{dataId} - Access granted - {gate}")
                    gc.openGate(gate)
                print(dataId)
                dataId = ''
    except:
        pass

def get_interface_details():

    interfaces = netifaces.interfaces()

    interface_details = []
    for interface in interfaces:

        if interface != "lo":
            details = {"interface": interface}
            # Get IP address
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                ip_address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                details["ip_address"] = ip_address
            else:
                details["ip_address"] = None

            # Get MAC address
            if netifaces.AF_LINK in netifaces.ifaddresses(interface):
                mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
                details["mac_address"] = mac_address
            else:
                details["mac_address"] = None

            interface_details.append(details)

    return interface_details
