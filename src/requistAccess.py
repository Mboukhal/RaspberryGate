import requests
import logs
import os
import gpioControl as gc
import usb.core

def isValid( idCard, device ):

    '''check for port number
        and make request to check if 
        id granted or not and return
        the gate to open in (14) or out (15)'''

    # load env varibles
    endpoint = os.getenv("ENDPOINT")
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

    if not endpoint or not token or not idCard:
        logs.log("Fialed to load ENDPOINT or TOKEN variables.")
        return 0
    
    data = {
        "badge_id": idCard,
        "target_token": token
    }

    try:
        response = requests.post( endpoint, data=data, timeout=3 )
        if response.status_code == 200:
            gc.openGate(gate)
            logs.log(f"{str(idCard)} - Access granted - {str(gate)}")
            return 1
        else:
            return -1
    except Exception as e:
        logs.log("Exception: {str(e)}")
    logs.log("Failed to connect to the API server")
    return 0
