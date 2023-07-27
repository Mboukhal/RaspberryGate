#!/usr/bin/python

import evdev
import requests
import gpioControl as gc
import requistAccess as req
from logs import log
import netifaces

from datetime import datetime as dt

def parssId(event):
    
    ev = evdev.categorize(event)
    if isinstance(ev, evdev.events.KeyEvent) and ev.keystate:
        return ev.keycode[-1]

LAST_ID = ['', dt.now()]

def checkId (idCard):
    
    if LAST_ID[0] != idCard:
        return True
    diff = (dt.now() - LAST_ID[1]).total_seconds()
    if diff < 8:
        return False
    return True

def collectId( device ):
    global LAST_ID
    
    '''collect id from usb RFID reader character by character 
        as keyboard keys click's'''
    dataId = ''
    try:
        # collect data from usb file
        for event in device.read_loop():
            data = parssId( event )
            if data and data.isnumeric():
                dataId += data
            elif data == 'R' and dataId:
                
                if checkId(dataId):
                    
                    # try to open gate
                    LAST_ID = [dataId, dt.now()]
                    gate = req.isValid( dataId, device.phys )
                    if gate == -1:
                        log(f"{dataId} - Access denied")
                    dataId = ''
                else:
                    dataId = ''
            elif len(dataId) > 19:
                dataId = ''
                    
    except Exception as e:
        log(f"Exception: {e}")

def get_interface_details():

    '''get interface info'''
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
