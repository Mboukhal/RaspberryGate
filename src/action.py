#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess
from time import sleep
from logs import valideCard
from os import environ

gate = environ.get("GATE")
gateName = environ.get("GATE_NAME")

relay = 21

try:
    GPIO.cleanup()
except:
	pass

GPIO.setmode( GPIO.BCM )
GPIO.setup( relay, GPIO.OUT )

def openGate():
    global relay

    GPIO.output( relay, GPIO.HIGH )
    sleep( 2 )
    GPIO.output( relay, GPIO.LOW )

def debugStartUp( idCard ):
    message = "Hi, world!: " + idCard
    subprocess.call(["wall", message])


def tryToOpen( idCard ):
    global gateName, gate

    # TODO:
    #   check if id in database
    #   if exist - gate 
    #   else - make worning
    # idCard example: 0001257461
    # Define the message to be printed
    
    if inValide( idCard ):
        openGate()
        valideCard().info( '%s, %s in gate: %s.', idCard, gate, gateName )
    else:
		# TODO: cliam warning to check 
        valideCard().warning( '%s, not in database.', idCard )
    
    debugStartUp( idCard )
    
    print( idCard )
