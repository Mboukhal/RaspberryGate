#!/usr/bin/python

import evdev

listDevices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in listDevices:
    print ( device )