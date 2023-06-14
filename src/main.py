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
import logs
import gpioControle as gc

# env_file = f'{Path(__file__).resolve().parent}/.env'
ENV_FILE = f'/boot/.env'

def initGpio():

	try:
		GPIO.setwarnings(False)

		try:
			GPIO.cleanup()
		except:
			pass

		GPIO.setmode( GPIO.BCM )
		GPIO.setup( gc.RELAY_1, GPIO.OUT )
		GPIO.output( gc.RELAY_1, GPIO.LOW )
		GPIO.setup( gc.RELAY_2, GPIO.OUT )
		GPIO.output( gc.RELAY_2, GPIO.LOW )
	except:
		pass

	GPIO.setmode( GPIO.BCM )
	GPIO.setup( gc.RELAY_1, GPIO.OUT )
	GPIO.output( gc.RELAY_1, GPIO.LOW )
	GPIO.setup( gc.RELAY_2, GPIO.OUT )
	GPIO.output( gc.RELAY_2, GPIO.LOW )
    
def get_usb_port_count():
    port_count = str(usb.core.find()).count("bLength")
    with open(ENV_FILE, "a") as file:
        file.write("PORT_COUNT=" + str(port_count) + "\n")

def checkForConfig():
        
    if not os.path.exists(logs.LOG_FILE):
        os.mkdir(logs.LOG_FILE[0:-9])
		# Create the file
        with open(logs.LOG_FILE, 'w') as file:
            pass

    if not load_dotenv(dotenv_path=ENV_FILE):
        exit(1)
    # print("Trying to create .env file")
    # startFlask(ENV_FILE)
    get_usb_port_count()
    initGpio()
    # print(".env file created successfully")

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
    
    thread_list = []
    
    while 1337:
        connected_usb_devices = device.get_connected_usb_devices()
        print(connected_usb_devices)
        thread_list = reset_threads(thread_list, connected_usb_devices)
        device.wait_for_usb_connection_or_disconnection()
    