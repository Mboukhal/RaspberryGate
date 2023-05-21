#!/usr/bin/python
import extractData as exd
import device, os
from rpConfig.config import startFlask
from pathlib import Path
from dotenv import load_dotenv

env_file = f'{Path(__file__).resolve().parent}/.env'


def checkForConfig():
    if not load_dotenv(dotenv_path=env_file):
        print("Trying to create .env file")
        startFlask(env_file)
    print(".env file created succssfully")

if __name__ == '__main__':
    # Load .env file

    checkForConfig()
    status = True
    while status:
        deviceEv = device.searchDevice()
        if deviceEv:
            status = exd.collectId( deviceEv )
        if status:
            device.waitForDevice()
