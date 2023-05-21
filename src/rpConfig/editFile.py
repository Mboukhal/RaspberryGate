import subprocess



def setConfig( config ):
    fileName = '.env'

    with open(fileName, "w+") as file:
        file.write( "endpoint=" + config['endpoint'] + "\n" )
        file.write( "token=" + config['token'] + "\n" )
        
        if config['relay']:
            relay = int( config['relay'] )
            if 0 < relay < 28:
                file.write( "relay=" + config['relay'] + "\n" )
    
    # if 'wifi' in config.form:
    #     wifi_disabled()
    # if config['hostname']:
    #     setHostname( config['hostname'] )
        # import os
        # os.system('reboot')

def setHostname( hostname ):
    
    hosts_path  = '/etc/hosts'
    hostname_path  = '/etc/hostname'
    string_to_remove = '127.0.1.1'

    with open(hostname_path, "r") as file:
        hostname = file.read()

    with open(hosts_path, "r") as file:
        lines = file.readlines()

    with open(hosts_path, "w") as file:
        for line in lines:
            if string_to_remove not in line:
                file.write(line)
        file.write( "127.0.1.1 =\t" + hostname + "\n" )
    with open( 'hostname_path', "w") as file:
        file.write( hostname + "\n" )


def wifi_disabled():
    subprocess.call('echo "dtoverlay=disable-wifi" >> /boot/config.txt;\
                    echo "dtoverlay=disable-bt" >> /boot/config.txt;\
                    sudo reboot',
                    shell=True)
