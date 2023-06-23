#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import os


RELAY_1 = 14		# IN relay
RELAY_2 = 15		# OUT relay

RELAY_ON = GPIO.HIGH
RELAY_OFF = GPIO.LOW

def openGate( relay ):
    
    if os.getenv("RELAY_TYPE") == "GSRT":
        RELAY_ON = GPIO.LOW
        RELAY_OFF = GPIO.HIGH
    
    GPIO.output( relay, RELAY_ON )
    sleep( 0.8 )
    GPIO.output( relay, RELAY_OFF )

def initGpio():

    if os.getenv("RELAY_TYPE") == "GSRT":
        RELAY_OFF = GPIO.HIGH

    try:
        GPIO.setwarnings(False)

        try:
            GPIO.cleanup()
        except:
            pass

        GPIO.setmode( GPIO.BCM )
        GPIO.setup( RELAY_1, GPIO.OUT )
        GPIO.output( RELAY_1, RELAY_OFF )
        GPIO.setup( RELAY_2, GPIO.OUT )
        GPIO.output( RELAY_2, RELAY_OFF )
    except:
        pass