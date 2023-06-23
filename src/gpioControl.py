#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import os


RELAY_1 = 14		# IN relay
RELAY_2 = 15		# OUT relay


def openGate( relay ):
    
    if os.getenv("RELAY_TYPE") == "GSRT":
        relayOn = GPIO.LOW
        relayOff = GPIO.HIGH
    elif os.getenv("RELAY_TYPE") == "PSRT":
        relayOn = GPIO.HIGH
        relayOff = GPIO.LOW
    
    GPIO.output( relay, relayOn )
    sleep( 0.8 )
    GPIO.output( relay, relayOff )

def initGpio():

    if os.getenv("RELAY_TYPE") == "GSRT":
        relayOff = GPIO.HIGH
    elif os.getenv("RELAY_TYPE") == "PSRT":
        relayOff = GPIO.LOW

    try:
        GPIO.setwarnings(False)

        try:
            GPIO.cleanup()
        except:
            pass

        GPIO.setmode( GPIO.BCM )
        GPIO.setup( RELAY_1, GPIO.OUT )
        GPIO.output( RELAY_1, relayOff )
        GPIO.setup( RELAY_2, GPIO.OUT )
        GPIO.output( RELAY_2, relayOff )
    except:
        pass