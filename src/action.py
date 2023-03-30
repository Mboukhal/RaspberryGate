#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess


relay = 21
# GPIO.cleanup()
# setup the GPIO
# GPIO.setmode( GPIO.BCM )
# GPIO.setup( relay, GPIO.OUT )


def debugStartUp( idCard ):
    message += idCard
    subprocess.call(["wall", message])


def setRelay( move ):
    # move = GPIO.HIGH || GPIO.LOW
    GPIO.output( relay, move )


def tryToOpen( idCard ):
    
    # message = "Hi, world!: "
    # TODO:
    #   check if id in database
    #   if exist - gate 
    #   else - make worning
    # idCard example: 0001257461
    # Define the message to be printed
    
    # debugStartUp( idCard )
    
    print( idCard )
