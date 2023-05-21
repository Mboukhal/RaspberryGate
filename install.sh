#!/bin/bash

NAME='gate'
installPath='/usr/bin/gateRp'

# check permissions
# if [ "$EUID" -ne 0 ]
#   then echo "Please run as root"
#   exit 127
# fi

# set hostname
echo "127.0.1.1		$NAME" >> /etc/hosts
echo "$NAME" > /etc/hostname

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

# install gate program
# if [ ! -d "$installPath" ]; then

# install python libraries:
echo "Install python libraries..."
apt update
apt install -y python3.9 python3-pip
python -m pip install pyudev
python -m pip install evdev
python -m pip install requests
python -m pip install flask
python -m pip install python-dotenv
python -m pip install watchdog

# copy project directory:
echo "Copying project directory..."
mkdir -p $installPath
cp -r $SCRIPT_PATH/src/* $installPath
chmod +x $installPath/main.py
mkdir -p /var/log/$NAME/
mv /var/log/$NAME/$NAME.log /var/log/$NAME/$NAME.log.$(date +"%F_%T").backup &> /dev/null
touch /var/log/$NAME/$NAME.log

# set gate in startup:
echo "Set gate in startup..."
echo "[Unit]" >> /etc/systemd/system/$NAME.service
echo "Description=$NAME" >> /etc/systemd/system/$NAME.service
echo "After=multi-user.target" >> /etc/systemd/system/$NAME.service
echo "" >> /etc/systemd/system/$NAME.service
echo "[Service]" >> /etc/systemd/system/$NAME.service
echo "Type=idle" >> /etc/systemd/system/$NAME.service
echo "User=root" >> /etc/systemd/system/$NAME.service
echo "Restart=always" >> /etc/systemd/system/$NAME.service
echo "RestartSec=2" >> /etc/systemd/system/$NAME.service
echo "ExecStart=/usr/bin/sudo /usr/bin/python $installPath/main.py" >> /etc/systemd/system/$NAME.service
echo "" >> /etc/systemd/system/$NAME.service
echo "[Install]" >> /etc/systemd/system/$NAME.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/$NAME.service

# Reload systemd:
echo "Reload systemd..."
systemctl daemon-reload

# Enable the service:
echo "Enable the service..."
systemctl enable $NAME.service
systemctl start $NAME.service
#   exit 0
# fi

# INPUT=''
# echo -n "To unistalling enter 'Y', (default: N): "
# read  INPUT
# [ "$INPUT" == "Y" -o "$INPUT" == "y" ] || exit 0

# echo "Unistalling..."
# rm -rf $installPath
# rm -rf /etc/systemd/system/$NAME.service
# systemctl disable $NAME.service
# systemctl stop $NAME.service


