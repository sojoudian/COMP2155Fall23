import paramiko
import time

sshClient = paramiko.SSHClient()

#to fix known issues with SSH we have to set the policy to auto add the keys
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshClient.connect(  hostname='192.168.122.100',username='u1',password='cisco',port=22)

isSSHActive = sshClient.get_transport().is_active()
print(isSSHActive)
print("Successfully connected to the host")

shell = sshClient.invoke_shell()
shell.send("enable\n")
time.sleep(1)
shell.send("cisco\n")
time.sleep(1)
shell.send("show version\n")
time.sleep(1)
respone = shell.recv(1000) #receive 5000 bytes
output = respone.decode('utf-8')
print(output)