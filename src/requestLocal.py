# import requests
import logs
import os
import gpioControl as gc
import usb.core
import local.get_access as get_access

def isValid( idCard: str, device: str ):

    '''check for port number
        and make request to check if 
        id granted or not and return
        the gate to open in (14) or out (15)'''

    # load env varibles
    token_in = os.getenv("TOKEN_IN")
    token_out = os.getenv("TOKEN_OUT")
    
    # set token to avalable token  
    if token_in:
        token = token_in
        gate = 14
    elif token_out:
        gate = 15
        token = token_out

    # cheak usb in half out or half in ports
    if token_out and token_in:
        portCount = str(usb.core.find()).count("bLength")
        if portCount > 1:
            port = int(device[19])
            if port > (portCount / 2): 
                gate = 15
                token = token_out

    if not idCard:
        logs.log(f"Fialed to load ID'{idCard}'.")   
        return 0

    if not token:
        logs.log(f"Fialed to load TOKEN'{token}'.")
        return 0
    
    # TODO: send logs to server need structer
    try:
        response = get_access( idCard )
        if response.ok:
            gc.openGate(gate)
            logs.log(f"{str(idCard)} - Access granted - {str(gate)}")
            return 1
        else:
            logs.log(f"{str(idCard)} - Access denied - {str(gate)} - {response.message}")
            return -1
    except Exception as e:
        logs.log(f"Exception: {e}")
    logs.log("Failed to connect to the API server")
    return 0
