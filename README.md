# RaspberryGate

RaspberryGate is a gate control system designed to replace outdated gate badges and integrate seamlessly with your existing infrastructure. This repository contains the source code and installation script for RaspberryGate, which utilizes a Raspberry Pi along with an RFID USB reader and USB ports.

## Installation

To install RaspberryGate, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.dev/Mboukhal/raspberryGate
   ```

2. Run the installation script with root privileges:
   ```
   sudo bash raspberryGate/install.sh
   ```

## Configuration

RaspberryGate supports the use of an RFID USB reader and USB ports to assign tokens. The configuration is done through the `/boot/.env` file.

If two tokens are assigned, the available USB ports are divided evenly between the tokens. For example, if there are four USB ports, each assigned token will have access to two ports. If only one token is assigned, all USB ports will be dedicated to that token.

Modify the `/boot/.env` file to set up the necessary parameters. Ensure that the file contains the following entries:

```shell
ENDPOINT="http://10.42.6.87"		
TOKEN_IN="token@in"
TOKEN_OUT="token@out"
HOSTNAME="Gate"
```

Adjust the values in the `.env` file according to your setup and assign the appropriate tokens.

## Logs

RaspberryGate generates two types of logs:

- **Boot Logs**: These logs can be found in `/boot/gate.log`. They validate the environment file and provide information about connected interfaces, including MAC addresses and IP addresses.

- **Main Logs**: The main logs are located in `/var/log/gate/gate.log`. They include details about user ID validation, error logs, and other relevant information.

Feel free to explore the repository and make any necessary changes to adapt RaspberryGate to your specific requirements.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
