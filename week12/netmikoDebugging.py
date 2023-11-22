import logging
from netmiko import Netmiko  
import time

net_connect = Netmiko(host='192.168.25.135', username='maziar', password='maziar', device_type='linux')

print(net_connect.find_prompt()) 
logging.basicConfig(filename='app.log', level=logging.DEBUG)  
logger = logging.getLogger("netmiko")

net_connect.write_channel("journalctl\n")
time.sleep(1)
output = net_connect.read_channel()
