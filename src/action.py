#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess
from time import sleep


def openGate():
    relay = 21
    
    # setup the GPIO
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( relay, GPIO.OUT )
    GPIO.output( relay, GPIO.HIGH )
    sleep( 2 )
    GPIO.output( relay, GPIO.LOW )
    GPIO.cleanup()

def debugStartUp( idCard ):
    message = "Hi, world!: " + idCard
    subprocess.call(["wall", message])


def setRelay( move ):
    # move = GPIO.HIGH || GPIO.LOW


def tryToOpen( idCard ):
    
    # TODO:
    #   check if id in database
    #   if exist - gate 
    #   else - make worning
    # idCard example: 0001257461
    # Define the message to be printed
    
    if inValide( idCard ):
        openGate()
    
    debugStartUp( idCard )
    
    print( idCard )
