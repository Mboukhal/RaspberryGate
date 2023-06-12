#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import os

RELAY_1 = 14
RELAY_2 = 15

def openGate( gate ):
    
    GPIO.output( RELAY_1 + gate, GPIO.HIGH )
    sleep( 0.8 )
    GPIO.output( RELAY_1 + gate, GPIO.LOW )
    # print( "door opened" )
