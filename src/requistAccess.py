import requests
import info

def isValid( idCard='0000' ):
    global token
    
    response = requests.get( info.endpoint, headers=info.headers, data=idCard )
    # TODO: requist access
    if response.status_code == 200:
        return True
    return False