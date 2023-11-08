import os
import paramiko
from datetime import datetime

# Configuration for the remote server
REMOTE_HOST = '192.168.122.1'  # Replace with your remote server IP
REMOTE_PORT = 22  # Replace with your remote server SSH port if different
USERNAME = 'student'  # Replace with your SSH username
PASSWORD = 'student'  # Replace with your SSH password
REMOTE_PATH = '/home/student/'  # Replace with the directory on the remote server

# Configuration for the local file
LOCAL_FILE_PATH = 'file.txt'  # Replace with your local file path

# Establish an SSH client and connect to the server
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(REMOTE_HOST, port=REMOTE_PORT, username=USERNAME, password=PASSWORD)
    sftp = ssh_client.open_sftp()

    # Get the current date in the format YYYYMMDD
    current_date = datetime.now().strftime('%Y%m%d')

    # Extract the file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(LOCAL_FILE_PATH))
    # Append the current date to the file name
    new_file_name = f"{file_name}_{current_date}{file_extension}"

    # Combine with the remote path
    remote_file_path = os.path.join(REMOTE_PATH, new_file_name)

    # Copy the file from the local machine to the remote server
    sftp.put(LOCAL_FILE_PATH, remote_file_path)
    print(f"File copied to {remote_file_path} successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if ssh_client:
        sftp.close()
        ssh_client.close()
