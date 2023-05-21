#!/usr/bin/python

import extractData as exd
<<<<<<< HEAD
# import config
import device
import os
=======
import device, os
from rpConfig.config import startFlask
>>>>>>> 3dc469c9fd8452b5cab253ab8764b3dd5d15309b

<<<<<<< HEAD
def	config():
	return
	if not os.path.exists( "info.py" ):
		confi.config( "./src" )
		pass

=======
def checkForConfig():
    if not os.path.exists( "info.py" ):
        startFlask()  

>>>>>>> 3dc469c9fd8452b5cab253ab8764b3dd5d15309b
if __name__ == '__main__':
<<<<<<< HEAD



=======

    checkForConfig()
>>>>>>> 3dc469c9fd8452b5cab253ab8764b3dd5d15309b
    status = True
    while status:
        deviceEv = device.searchDevice()
        if deviceEv:
            status = exd.collectId( deviceEv )
        if status:
            device.waitForDevice()
