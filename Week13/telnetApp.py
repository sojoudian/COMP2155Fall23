import telnetlib
from telnetlib import Telnet
t = Telnet(host='192.168.122.20', port=23)
t.read_until("Username: ".encode())
t.write('u1\n'.encode())
t.read_until("Password: ".encode())
t.write('cisco\n'.encode())

t.write('enable\n'.encode())
t.write('cisco\n'.encode())

t.write('show clock\n'.encode())
t.write('exit\n'.encode())
result=t.read_all().decode()
print(result)