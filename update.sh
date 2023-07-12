#!/bin/bash

# wait for internet 
while ! ping -c 1 google.com >/dev/null 2>&1; do
    :
done

git fetch
git reset --hard origin/master  # Replace 'master'
