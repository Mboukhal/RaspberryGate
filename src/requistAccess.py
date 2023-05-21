import requests
import os

def isValid( idCard='00000000' ):
    endpoint = os.getenv("ENDPOINT")
    token = os.getenv("TOKEN")

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
        print("Failed to connect to the API server")
    return False
