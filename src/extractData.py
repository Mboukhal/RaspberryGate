#!/usr/bin/python

import evdev
import gpioControl as gc
import requistAccess as req
import pyudev
from logs import log

# get keys
def     parssId( ev ):
    try:
        if isinstance(ev, evdev.events.KeyEvent) and ev.keystate:
            return ev.keycode[-1]
    except:
            pass

# wait for reader to connect
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
                        log().info( '%s Reader started:', device.name )
                        print ( device.name )
                        return device
                    elif device and "usb" in device.phys:
                        log().info( '%s not supported hardware:', device.name )
                device.close()
    except:
            pass

def	getNewId( device ):
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
                dataId = ''
    except KeyboardInterrupt:
        device.close()
        print("\rExiting program...")
        return False
    except Exception as e:
        log().info( 'Reader Error: %s', str(e) )
    return True
