import sys
from pClass import Connector
import time
from datetime import datetime
import os

try:
    start_time = time.time()
    p = Connector(username="maziar", password="maziar", host="192.168.25.133", port=22)

    # Define the remote path of the sshd_config file
    REMOTE_PATH = '/etc/ssh/sshd_config'
    
    # Retrieve the sshd_config file's content
    result = p.send_shell_command(f"cat {REMOTE_PATH}")
    
    # Format the current date and time into a string suitable for a file name
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Define local file name by appending the current time to 'sshd_config'
    local_file_name = f"sshd_config_{current_time}.txt"

    # Write the contents of the sshd_config file to the local file
    with open(local_file_name, "w") as file:
        file.write(result)

    end_time = time.time()
    print(f"Script took {end_time - start_time} seconds")
except Exception as e:
    print(e, file=sys.stderr)
