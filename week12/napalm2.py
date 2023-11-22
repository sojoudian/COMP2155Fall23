import napalm

# Replace with your device details
driver = napalm.get_network_driver('ios') # 'ios' is for Cisco IOS, change this for other vendors
device = driver(hostname='192.168.1.1', username='u1', password='cisco', optional_args={"port":22, "secret": "cisco"})


# Open a connection to the device
device.open()

# Get device information
info = device.get_facts()
print("Device Information:")
print(info)

# Close the connection
device.close()
