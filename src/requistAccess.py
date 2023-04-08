import requests
import info

def isValid( idCard='00000000' ):
    # TORM:
    return True
	
    headers = { "Authorization": f"Bearer {info.token}" }
    response = requests.get( info.endpoint, headers=headers, data=idCard )
    if response.status_code == 200:
        return True
    return False