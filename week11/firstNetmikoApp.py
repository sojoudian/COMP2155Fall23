from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.30',
    'username': 'admin',
    'password': 'password',
    'port' : 22,
    'secret': 'secret',  # Enable password, if required
}

# Establishing the connection
net_connect = ConnectHandler(**cisco_device)

# Entering enable mode
net_connect.enable()

# Running a command
output = net_connect.send_command('show ip int brief')
print(output)

# Closing the connection
net_connect.disconnect()
