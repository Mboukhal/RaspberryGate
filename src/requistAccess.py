import requests
import os
import usb.core

def isValid( idCard, device ):
    endpoint = os.getenv("ENDPOINT")
    token = os.getenv("TOKEN_1")
    token_2 = os.getenv("TOKEN_2")
    gate = 0

    if token_2:
        portCount = (usb.core.find()).count("bLength")
        if portCount > 1:
            port = int(device[19])
            if port > (portCount / 2): 
                gate = 1
                token = token_2

    # print(token)
    # print(endpoint)

    if not endpoint or not token:
        print("Fialed to load ENDPOINT or TOKEN variables.")
        return -1
    data = {
        "badge_id": idCard,
        "target_token": token
    }
    try:
        response = requests.post( endpoint, data=data )
        if response.status_code == 200:
            return gate
    except:
        pass
        # print("Failed to connect to the API server")
    return -1
