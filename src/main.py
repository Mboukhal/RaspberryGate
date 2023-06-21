#!/usr/bin/python

import device
from logs import log
import setup
import extractData as exd


if __name__ == '__main__':
    
    # check all setup 
    setup.setUp()
    
    thread_list = []
    
    # make thread's for every usb reader and wait
    # for update usb if one removed or added
    # to update thread's list

    while True:
        connected_usb_devices = device.get_connected_usb_devices()
        if connected_usb_devices:
            log(f"new decies connected - {connected_usb_devices}")
        thread_list = device.reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
