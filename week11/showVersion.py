from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '192.168.122.30',
    'username': 'admin',
    'password': 'password',
    'port' : 22,
    'secret': 'secret',
}

# Using a with statement to automatically close the connection
with ConnectHandler(**cisco_device) as net_connect:
    net_connect.enable()
    output = net_connect.send_command('show version')
    print(output)
