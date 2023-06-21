#!/usr/bin/python

import extractData as exd
from dotenv import load_dotenv
import logs
import gpioControl as gc
import uuid
import os


ENV_FILE = f'/boot/gate.env'
LOG_FILE = f'/boot/gate.log'
LOG_FILE_SYSTEM = f'/var/log/gate/gate.log'

def setUp():
    
    '''setup and load env file every start'''
    if not os.path.exists(LOG_FILE):
        interface_details = exd.get_interface_details()
        for interface in interface_details:
            if interface:
                logs.log(f"{interface['interface']} - {interface['mac_address']} - {interface['ip_address']}"
                        , file_path=LOG_FILE)
    # try load env
    if not load_dotenv(dotenv_path=ENV_FILE):
        logs.log("fail loading env file", file_path=LOG_FILE)
        exit(1)
    
    endpoint = os.getenv("ENDPOINT")

    # cheak for valide endpoint env 
    if not endpoint:
        logs.log("None valide Endpoit", file_path=LOG_FILE)
        exit(2)

    token_in = os.getenv("TOKEN_IN")
    token_out = os.getenv("TOKEN_OUT")
    # cheak for valide token env 
    if token_in == None and token_out == None:
        logs.log("None valide Token", file_path=LOG_FILE)
        exit(3)

    # initialize GPIO
    gc.initGpio()

    hostname = os.getenv("HOSTNAME")

    if hostname and not check_string_in_file('/etc/hostname', hostname):
        with open("/etc/hostname", 'w') as file:
            file.write(hostname)
        hostname = "127.0.1.1\t\t" + hostname + '\n'
        with open("/etc/hosts", 'a') as file:
            file.write(hostname)
        
        logs.log(f"{hostname} - is set as Hostname", file_path=LOG_FILE)
        

    if os.path.exists(LOG_FILE_SYSTEM):
        return
           
    os.mkdir(LOG_FILE_SYSTEM[0:-9])

    # Create the file
    with open(LOG_FILE_SYSTEM, 'w') as file:
        pass


def check_string_in_file(filename, search_string):
    with open(filename, 'r') as file:
        for line in file:
            if search_string in line:
                return True
    return False