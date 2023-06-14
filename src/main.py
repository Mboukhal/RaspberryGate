#!/usr/bin/python
import extractData as exd
import device, os
# from rpConfig.config import startFlask
from pathlib import Path
from dotenv import load_dotenv
import logs
import gpioControl as gc
import uuid


# env_file = f'{Path(__file__).resolve().parent}/.env'
ENV_FILE = f'/boot/.env'

def setUp():

    if not load_dotenv(dotenv_path=ENV_FILE):
        exit(1)
    
    endpoint = os.getenv("ENDPOINT")

    if not endpoint:
        exit(2)

    token_in = os.getenv("TOKEN_IN")
    token_out = os.getenv("TOKEN_OUT")
    
    if not token_in and not token_out:
        exit(3)

    gc.initGpio()

    if os.path.exists(logs.LOG_FILE):
        return
           
    os.mkdir(logs.LOG_FILE[0:-9])
    # Create the file
    with open(logs.LOG_FILE, 'w') as file:
        pass
    
    name = str(uuid.uuid4())

    with open("/etc/hosts", 'a') as file:
        file.write("127.0.1.1\t\t" + name)
    
    with open("/etc/hostname", 'w') as file:
        file.write(name)

if __name__ == '__main__':
    
    setUp()
    
    thread_list = []
    
    while True:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = device.reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
    