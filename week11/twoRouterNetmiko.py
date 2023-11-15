import threading
from netmiko import ConnectHandler

# Define your devices
device_list = [
    {
        'device_type': 'cisco_ios',
        'host':   '192.168.122.30',
        'username': 'admin',
        'password': 'password1',
        'port' : 22,
        'secret': 'secret1',
    },
    {
        'device_type': 'cisco_ios',
        'host':   '192.168.122.10',
        'username': 'admin',
        'password': 'password2',
        'port' : 22,
        'secret': 'secret2',
    },
    # Add more devices as needed
]

# Define a function to connect to each device and execute commands
def connect_and_run(device):
    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            output = net_connect.send_command('show ip int brief')
            print(f"Output from device {device['host']}:\n{output}\n")
    except Exception as e:
        print(f"An error occurred with device {device['host']}: {e}")

# Create and start a thread for each device
threads = []
for device in device_list:
    th = threading.Thread(target=connect_and_run, args=(device,))
    th.start()
    threads.append(th)

# Wait for all threads to complete
for th in threads:
    th.join()

print("All tasks are completed!")
