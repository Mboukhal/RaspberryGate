# RaspberryGate

RaspberryGate is a gate control system designed specifically for use in the 1337 School. It is developed to replace the outdated gate badges system and seamlessly integrate with the infrastructure of the school. This repository contains the source code and installation script for RaspberryGate, which utilizes a Raspberry Pi along with an RFID USB reader, USB ports, and relays.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Logs](#logs)

## Installation

To install RaspberryGate, follow these steps:

1. Update and install git:
   ```
   sudo apt-get update; sudo apt-get install -y git
   ```

2. Clone the repository:
   ```
   git clone https://github.dev/Mboukhal/RaspberryGate
   ```

3. Run the installation script with root privileges:
   ```
   sudo bash RaspberryGate/install.sh
   ```

## Configuration

RaspberryGate utilizes relays connected to specific GPIO pins on the Raspberry Pi to control the gate opening. Pin 14 is used to open the gate for incoming access, while pin 15 is used to open the gate for outgoing access.

Make sure the relays are correctly connected to the respective GPIO pins on the Raspberry Pi before proceeding.

The configuration is done through the `/boot/gate.env` file. This file needs to contain the `ENDPOINT` and at least one of the `TOKEN_IN` or `TOKEN_OUT` entries.

Modify the `gate.env` file to set up the necessary parameters. Ensure that the file contains the following entries:

```shell
ENDPOINT="http://10.42.6.87"		
TOKEN_IN="token@in"
TOKEN_OUT="token@out"
HOSTNAME="Gate"
```

Adjust the values in the `gate.env` file according to your setup, including the endpoint and token values. The `HOSTNAME` can be customized to your desired gate name.

## Logs

RaspberryGate generates two types of logs:

- **Boot Logs**: These logs can be found in `/boot/gate.log`. They validate the environment file and provide information about connected interfaces, including MAC addresses and IP addresses.

- **Main Logs**: The main logs are located in `/var/log/gate/gate.log`. They include details about user ID validation, error logs, and other relevant information.

Feel free to explore the repository and make any necessary changes to adapt RaspberryGate to the specific requirements of the 1337 School.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
