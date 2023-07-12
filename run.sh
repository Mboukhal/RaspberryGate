#!/bin/bash

installPath='/usr/bin/gateRp'

bash $installPath/update.sh &

python3 $installPath/src/main.py
