#!/bin/bash

NAME='gate'
installPath='/usr/bin/gateRp'


# check permissions
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 127
fi

SCRIPT=$(realpath "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

python -c "import evdev" &> /dev/null
if [ "$?" == "1" ]; then
  # install python libraries:
  echo "Install python libraries..."
  apt update
  apt upgrade -y
  apt install -y python3.9 python3-pip
  python -m pip install pyudev
  python -m pip install evdev
fi

# # set database check for news every 4h:

# if [ ! -f "/usr/bin/checkDbNews.py" ] then

#     # Install database checker:
#     echo "Install database checker..."
#     cp $SCRIPT_PATHd/atabaseHandeler/checkDbNews.py /usr/bin/
#     echo "0 */4 * * * /usr/bin/python /usr/bin/checkDbNews.py" > $SCRIPT_PATHd/atabaseHandeler//cronjob
#     crontab $SCRIPT_PATHd/atabaseHandeler/cronjob
#     rm $SCRIPT_PATHd/atabaseHandeler/cronjob &> /dev/null 
# fi


# install gate program
if [ ! -d "$installPath" ]; then

    # copy project directory:
    echo "Copying project directory..."
    mkdir -p $installPath
    cp -r $SCRIPT_PATH/src/* $installPath
    chmod +x $installPath/main.py
    mkdir -p /var/log/gate/
    touch /var/log/gate/gate.log
    # chmod +x $SCRIPT_PATH/src/debug/*

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
    exit 0
fi

INPUT=''
echo -n "To unistalling enter 'Y', (default: N): "
read  INPUT
[ "$INPUT" == "Y" -o "$INPUT" == "y" ] || exit 0

echo "Unistalling..."
rm -rf $installPath
rm -rf /etc/systemd/system/$NAME.service
systemctl disable $NAME.service
systemctl stop $NAME.service
# echo -n "To disable wireless communications enter: 'Y', (default: N): "
# read  INPUT
# if [ "$INPUT" == "Y" -o "$INPUT" == "y" ]; then 

  # # disable wifi and bleutooth
  # echo "dtoverlay=disable-wifi" >> /boot/config.txt
  # echo "dtoverlay=disable-bt" >> /boot/config.txt
  # sudo reboot
#fi

