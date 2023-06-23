#!/bin/bash

installPath='/usr/bin/gateRp'

# Pull if there is any changes
sudo git config --global --add safe.directory $installPath
sudo git pull origin master --no-rebase
sudo python3 $installPath/src/main.py