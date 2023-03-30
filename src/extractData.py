#!/usr/bin/python

import evdev
import action
import os
import pyudev

inputDir = "/dev/input/"

def     parssId( ev ):
    try:
        if isinstance(ev, evdev.events.KeyEvent) and ev.keystate:
            return ev.keycode[-1]
    except:
            pass


def waitForDevice():
    print ( "Wait for device..." )
    # Create a context object
    context = pyudev.Context()

    # Create a monitor object for USB devices
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    # Start the monitor
    monitor.start()

    # Wait for a new USB device to be connected
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            return device


def searchDevice(  ):
    
    listDevices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    try:
        for device in listDevices:
                device.grab()
                # check if device is HID device (data as keyword)
                if evdev.ecodes.EV_KEY in device.capabilities(verbose=False):
                    # check if the device is has RFID signe in device name and if is usb
                    if device and "usb" in device.phys and "RFID" or "rfid" in device.name:
                        print ( device.name )
                        return device
                device.close()
    except:
            pass


def	getNewId( device ):
    dataId = ''
    try:
        for event in device.read_loop():
            ev = evdev.categorize(event)
            x = parssId( ev )
            if x and len(x) == 1 and x.isnumeric():
                dataId += x
            elif x:
                action.tryToOpen( dataId )
                dataId = ''
    except KeyboardInterrupt:
        device.close()
        print("\rExiting program...")
        return False
    except TypeError:
            # TODO: set alert
            print ( "\rData error..." )
    except:
        # TODO: set alert
        # DONE: wait for new device
        print("\rNo reader...")
    return True
