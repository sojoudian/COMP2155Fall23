import telnetlib
from telnetlib import Telnet
import time
t = Telnet(host='192.168.122.20', port=23)
t.read_until("Username: ".encode())
t.write('u1\n'.encode())
t.read_until("Password: ".encode())
t.write('cisco\n'.encode())

t.write("terminal length 0\n".encode())

t.write('enable\n'.encode())
t.write('cisco\n'.encode())

t.write('show run\n'.encode())
time.sleep(2)
t.write('exit\n'.encode())
result=t.read_all().decode()
print(result)