import requests
import info

def isValid( idCard='00000000' ):
	
    data = {
        "basge_id": idCard,
        "target_token": info.token
    }
    
    response = requests.get( info.endpoint, data=data )
    if response.status_code == 200:
        return True
    return False
