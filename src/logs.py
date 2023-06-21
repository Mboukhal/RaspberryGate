import datetime

def log(string, file_path='/var/log/gate/gate.log'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] - {string}"
    with open(file_path, "a") as file:
        file.write(log_message + "\n")
