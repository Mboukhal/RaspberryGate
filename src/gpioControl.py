#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

relay = 18

try:
    GPIO.cleanup()
except:
    pass

GPIO.setmode( GPIO.BCM )
GPIO.setup( relay, GPIO.OUT )

def openGate():
    global relay

    GPIO.output( relay, GPIO.HIGH )
    sleep( 1 )
    GPIO.output( relay, GPIO.LOW )
