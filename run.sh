#!/bin/bash

installPath='/usr/bin/gateRp'

python3 $installPath/src/main.py &
python3 $installPath/src/local/database_update.py &
