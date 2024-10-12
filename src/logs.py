import datetime
import os

def log(string, file_path='/var/log/gate/gate.log', expiration_days=90):
    # Check if the file exists
    if os.path.exists(file_path):
        # Get the file's modification time
        file_mod_time = os.path.getmtime(file_path)
        file_mod_date = datetime.datetime.fromtimestamp(file_mod_time)
        
        # Calculate the file's age
        current_date = datetime.datetime.now()
        file_age = (current_date - file_mod_date).days
        
        # If the file is older than the expiration period, delete or rotate the file
        if file_age >= expiration_days:
            os.remove(file_path)
            print(f"Log file {file_path} removed due to expiration.")
    
    # Append the log message to the file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] - {string}"
    with open(file_path, "a") as file:
        file.write(log_message + "\n")

