# raspberryGate

This repository contains the source code and installation script for raspberryGate. It provides a gate control system using a Raspberry Pi.

## Installation

To install raspberryGate from scratch, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.dev/Mboukhal/raspberryGate
   ```

2. Run the installation script with root privileges:
   ```
   sudo bash raspberryGate/install.sh
   ```

## Configuration

Before running the application, make sure to add a `.env` file to the SD card with the following example content:

```
ENDPOINT="http://10.32.116.187"		*
TOKEN_IN="OK"
TOKEN_OUT="OK"
HOSTNAME="OK"
```

The `.env` file should at least contain the endpoint and one token. Adjust the values according to your setup.

## Logs

- Boot logs can be found in `/boot/gate.log`. These logs validate the environment file and display the interfaces' MAC addresses and IP addresses if connected.

- Main logs can be found in `/var/log/gate/gate.log`. These logs include information about user ID validation, error logs, and more.

Feel free to explore the repository and make any necessary changes to suit your requirements.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)