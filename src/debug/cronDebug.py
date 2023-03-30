#!/usr/bin/python
import subprocess

# Define the message to be printed
message = "Hi, world!"

subprocess.call(["wall", message])
