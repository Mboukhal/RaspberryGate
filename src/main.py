#!/usr/bin/python
import extractData as exd
import device, os
from rpConfig.config import startFlask
from pathlib import Path
from dotenv import load_dotenv
import usb.core
import threading
import ctypes
import RPi.GPIO as GPIO



env_file = f'{Path(__file__).resolve().parent}/.env'
RELAY_1 = 14
RELAY_2 = 15


def initGpio():

	try:
		GPIO.setwarnings(False)

		try:
			GPIO.cleanup()
		except:
			pass

		GPIO.setmode( GPIO.BCM )
		GPIO.setup( RELAY_1, GPIO.OUT )
		GPIO.output( RELAY_1, GPIO.LOW )
		GPIO.setup( RELAY_2, GPIO.OUT )
		GPIO.output( RELAY_2, GPIO.LOW )
	except:
		pass

	GPIO.setmode( GPIO.BCM )
	GPIO.setup( RELAY_1, GPIO.OUT )
	GPIO.output( RELAY_1, GPIO.LOW )
	GPIO.setup( RELAY_2, GPIO.OUT )
	GPIO.output( RELAY_2, GPIO.LOW )
    
def get_usb_port_count():
    port_count = str(usb.core.find()).count("bLength")
    with open(env_file, "a") as file:
        file.write("PORT-COUNT=" + str(port_count) + "\n")

def checkForConfig():
    if not load_dotenv(dotenv_path=env_file):
        log_filename = '/var/log/gate/gate.log'
        print("Trying to create .env file")
        startFlask(env_file)
        get_usb_port_count()
        print(".env file created successfully")
        if not os.path.exists(log_filename):
            os.mkdir(log_filename[0:-9])
            # Create the file
            with open(log_filename, 'w') as file:
                pass
        load_dotenv(dotenv_path=env_file)

def terminate_thread(thread):
    """Terminate a thread forcefully."""
    if not thread.is_alive():
        return

    thread_id = thread.ident
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
        print('Failed to terminate thread:', thread)
      
def reset_threads( old_threads_list, new_devices_list ):
    
    if old_threads_list:
        for thread in old_threads_list:
            terminate_thread(thread)
    
    new_threads_list = []
    
    for device in new_devices_list:
        thread = threading.Thread(target=exd.collectId, args=(device,))
        thread.start()
        new_threads_list.append(thread)
    
    return new_threads_list
    
if __name__ == '__main__':
    
    checkForConfig()
    initGpio()
    
    thread_list = []
    
    while 1337:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
    