import logging
from netmiko import Netmiko  
import time

logging.basicConfig(filename='v1.log', level=logging.DEBUG)  
logger = logging.getLogger("netmiko")

net_connect = Netmiko(host='192.168.25.135', username='u1', password='', device_type='', verbose=True)

print(net_connect.find_prompt())
print(net_connect.send_command("show clock\n"))
print("*"*100)
net_connect.write_channel("show version\n")
time.sleep(1)
output = net_connect.read_channel()

