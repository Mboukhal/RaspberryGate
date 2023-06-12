import requests
import os

def isValid( idCard, device ):
    endpoint = os.getenv("ENDPOINT")
    token = os.getenv("TOKEN")
    portCount = int(os.getenv("PORT-COUNT"))

    gate = 0

    if token == None:
        if portCount > 1:
            port = int(device[19])
            if port <= (portCount / 2): 
                gate = 0
                token = os.getenv("TOKEN-IN")
            else: 
                gate = 1
                token = os.getenv("TOKEN-OUT")

    if not endpoint or not token:
        print("Fialed to load ENDPOINT or TOKEN variables.")
        return False
    data = {
        "badge_id": idCard,
        "target_token": token
    }
    try:
        response = requests.post( endpoint, data=data )
        if response.status_code == 200:
            return True
    except:
        pass
        # print("Failed to connect to the API server")
    return False
