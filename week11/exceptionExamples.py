from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
cisco_device ={
    'device_type': 'cisco_ios',
    'host': '192.168.122.10', # change the IP to simulate the Timeout Exception
    'username': 'user',
    'password': '1234', # change the password to simulate the Authentication Exception
    'port': 22,
    'secret': 'secret',
}
try:
    netConnection=ConnectHandler(**cisco_device)
    netConnection.enable()
    print(netConnection.send_command('show clock'))
    netConnection.disconnect()
except NetmikoTimeoutException:
    print("Connection timed out.")
except NetmikoAuthenticationException:
    print("Authentication failed")