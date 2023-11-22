from netmiko import ConnectHandler

net_connect = ConnectHandler(host='192.168.122.10', username="u1", password="cisco", device_type="cisco_ios")