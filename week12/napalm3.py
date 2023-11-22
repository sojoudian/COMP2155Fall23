import napalm
import json

def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))

try:
    driver = napalm.get_network_driver('ios')
    device = driver(hostname='192.168.122.20', username='u1', password='cisco', optional_args={"port": 22, "secret": "cisco"})
    device.open()

    pretty_print(device.get_facts())

    pretty_print(device.get_users())
    

    device.close()
except Exception as e:
    print(f"An error occurred: {e}")
