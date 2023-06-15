#!/usr/bin/python
import extractData as exd
import device, os
# from rpConfig.config import startFlask
from pathlib import Path
from dotenv import load_dotenv
import logs as log
import gpioControl as gc
import uuid


# env_file = f'{Path(__file__).resolve().parent}/.env'
ENV_FILE = f'/boot/.env'

def setUp():

    log_file = "/boot/gate.log"
    # try load env
    if not load_dotenv(dotenv_path=ENV_FILE):
        log(log_file).info("fail loading env file")
        exit(1)
    
    endpoint = os.getenv("ENDPOINT")

    # cheak for valide endpoint env 
    if not endpoint:
        log(log_file).info("None valide Endpoit")
        exit(2)

    token_in = os.getenv("TOKEN_IN")
    token_out = os.getenv("TOKEN_OUT")
    # cheak for valide token env 
    if token_in == None and token_out == None:
        log(log_file).info("None valide Token")
        exit(3)

    # initialize GPIO
    gc.initGpio()

    hostname = os.getenv("HOSTNAME")

    if hostname == None:
        hostname = str(uuid.uuid4())

    with open("/etc/hosts", 'a') as file:
        file.write("127.0.1.1\t\t" + hostname)
    
    with open("/etc/hostname", 'w') as file:
        file.write(hostname)

    log(log_file).info(f"{hostname} - is set as Hostname")

    interface_details = exd.get_interface_details()
    for interface in interface_details:
        log(log_file).info(f"{interface['interface']} - {interface['mac_address']} - {interface['ip_address']}")


    if os.path.exists(logs.LOG_FILE):
        return
           
    os.mkdir(logs.LOG_FILE[0:-9])

    # Create the file
    with open(logs.LOG_FILE, 'w') as file:
        pass

if __name__ == '__main__':
    
    setUp()
    
    thread_list = []
    
    while True:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = device.reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
    