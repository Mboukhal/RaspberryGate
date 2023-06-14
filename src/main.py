#!/usr/bin/python
import extractData as exd
import device, os
# from rpConfig.config import startFlask
from pathlib import Path
from dotenv import load_dotenv
import logs
import gpioControle as gc

# env_file = f'{Path(__file__).resolve().parent}/.env'
ENV_FILE = f'/boot/.env'
    

def setUp():
        
    if not os.path.exists(logs.LOG_FILE):
        os.mkdir(logs.LOG_FILE[0:-9])
		# Create the file
        with open(logs.LOG_FILE, 'w') as file:
            pass

    if not load_dotenv(dotenv_path=ENV_FILE):
        exit(1)
    
    gc.initGpio()
    
if __name__ == '__main__':
    
    setUp()
    
    thread_list = []
    
    while 1337:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = device.reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
    