import os
from dotenv import load_dotenv

load_dotenv( dotenv_path='.env' )

if os.path.exists( ".env" ):
    endpoint = os.getenv('endpoint', '')
    token = os.getenv('token', '')
    try:
        relay = int( os.getenv('token', '14') )
    except:
        relay = 14
else:
    endpoint = ''
    token = ''
    relay = 14
