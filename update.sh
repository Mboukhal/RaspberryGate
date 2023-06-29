#!/bin/bash

while ! ping -c 1 google.com >/dev/null 2>&1; do
    :
done

# Pull if there is any changes
sudo git config --global --add safe.directory $installPath
sudo git pull origin master --no-rebase
