#!/bin/bash

while ! ping -c 1 google.com >/dev/null 2>&1; do
    :
done


