import requests
import info

def isValid( idCard='00000000' ):
    # TORM:
    return True

    response = requests.get( info.endpoint, headers=info.headers, data=idCard )
    if response.status_code == 200:
        return True
    return False