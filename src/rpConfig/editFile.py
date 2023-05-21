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
    
    if 'wifi' in config:
        wifi_disabled()
    if config['hostname']:
        setHostname( config['hostname'] )
        import os
        os.system('reboot')

def replace_string_in_file(file_path, old_string, new_string):
    # Read the file contents
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Replace the string
    updated_contents = file_contents.replace(old_string, new_string)

    # Write the updated contents back to the file
    with open(file_path, 'w') as file:
        file.write(updated_contents)      
   
def setHostname( hostname ):
    
    hosts_path  = '/etc/hosts'
    hostname_path  = '/etc/hostname'
    string_to_remove = '127.0.1.1'

    replace_string_in_file( hosts_path, 'gate', hostname )
        
    with open( hostname_path, "w") as file:
        file.write( hostname + "\n" )
    print ("ok all done")


def wifi_disabled():
    subprocess.call('echo "dtoverlay=disable-wifi" >> /boot/config.txt;\
                    echo "dtoverlay=disable-bt" >> /boot/config.txt;\
                    sudo reboot',
                    shell=True)
