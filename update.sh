#!/bin/bash

installPath='/usr/bin/gateRp'

# wait for internet 
while ! ping -c 1 google.com >/dev/null 2>&1; do
    :
done

cd $installPath

git fetch
git reset --hard origin/master  # Replace 'master'

cd -
