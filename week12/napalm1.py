import napalm

# Replace with your device details
driver = napalm.get_network_driver('ios') # 'ios' is for Cisco IOS, change this for other vendors
device = driver(hostname='192.168.1.1', username='u1', password='cisco'
                )


# Open a connection to the device
device.open()

# Close the connection
device.close()
