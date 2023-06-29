#!/bin/bash

installPath='/usr/bin/gateRp'

chmod +x update.sh
bash update.sh &

sudo python3 $installPath/src/main.py
