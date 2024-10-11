#!/bin/bash

NAME='gate'
GITNAME='git-update'
INSTALL_PATH='/usr/bin/gateRp'

# check permissions
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 127
fi

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

if [ -d "$INSTALL_PATH" ]; then

    echo "Unistalling..."
    rm -rf $INSTALL_PATH

    rm -rf /etc/systemd/system/$NAME.service
    systemctl disable $NAME.service
    systemctl stop $NAME.service

    rm -rf /etc/systemd/system/$GITNAME.service
    systemctl disable $GITNAME.service
    systemctl stop $GITNAME.service
fi

echo "Install python libraries..."
apt update
apt install -y python3.9 python3-pip

python3 -m pip install evdev pyusb pyudev requests python-dotenv watchdog netifaces websockets



# python3 -m pip install evdev
# python3 -m pip install pyusb
# python3 -m pip install pyudev
# python3 -m pip install requests
# python3 -m pip install python-dotenv
# python3 -m pip install watchdog
# python3 -m pip install netifaces

# copy project directory:
echo "Copying project directory..."
mkdir -p $INSTALL_PATH
git config --global --add safe.directory $INSTALL_PATH
chmod +x ./src/main.py
chmod +x ./run.sh
chmod +x ./update.sh
cp -ra $SCRIPT_PATH/. $INSTALL_PATH
mkdir -p /var/log/$NAME/
mv /var/log/$NAME/$NAME.log /var/log/$NAME/$NAME.log.$(date +"%F_%T").backup &> /dev/null
touch /var/log/$NAME/$NAME.log

# set gate in startup service:
echo "Set gate in startup..."

GATE_SERVICE_FILE="/etc/systemd/system/$NAME.service"
cat << __EOF > $GATE_SERVICE_FILE
[Unit]
Description=$NAME
After=multi-user.target

[Service]
Type=idle
User=root
Restart=always
RestartSec=2
ExecStart=bash $INSTALL_PATH/run.sh

[Install]
WantedBy=multi-user.target
__EOF

echo "Set git update in startup..."

GIT_SERVICE_FILE="/etc/systemd/system/$GITNAME.service"
cat << __EOF > $GIT_SERVICE_FILE
[Unit]
Description=$GITNAME

[Service]
User=root
ExecStart=bash $INSTALL_PATH/update.sh

[Install]
WantedBy=default.target
__EOF

# Reload systemd:
echo "Reload systemd..."
systemctl daemon-reload

# Enable the service:
echo "Enable the service..."
systemctl enable $NAME.service
systemctl start $NAME.service

systemctl enable $GITNAME.service
systemctl start $GITNAME.service

