#!/usr/bin/python

import device
from setup import setup


if __name__ == '__main__':
    
    setUp()
    
    thread_list = []
    
    while True:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = device.reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
