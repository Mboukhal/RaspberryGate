import requests
import info

def isValid( idCard='00000000' ):
    
    response = requests.get( info.endpoint, headers=info.headers, data=idCard )
    # TODO: requist access
    if response.status_code == 200:
        return True
    return False