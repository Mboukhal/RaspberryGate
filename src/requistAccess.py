import requests
import logs as log
import os
import usb.core

def isValid( idCard, device ):

    # load env varibles
    endpoint = os.getenv("ENDPOINT")
    token_in = os.getenv("TOKEN_IN")
    token_out = os.getenv("TOKEN_OUT")
    
    # set token to avalable token  
    if token_in:
        token = token_in
        gate = "in"
    elif token_out:
        gate = "out"
        token = token_out

    # cheak usb in half out or half in ports
    if token_out and token_in:
        portCount = (usb.core.find()).count("bLength")
        if portCount > 1:
            port = int(device[19])
            if port > (portCount / 2): 
                gate = "out"
                token = token_out

    # print(token)
    # print(endpoint)

    if not endpoint or not token:
        log().info("Fialed to load ENDPOINT or TOKEN variables.")
        return None
    
    data = {
        "badge_id": idCard,
        "target_token": token
    }

    try:
        response = requests.post( endpoint, data=data )
        if response.status_code == 200:
            return gate
        else:
            return "no"
    except:
        pass
    log().info("Failed to connect to the API server")
    return None
