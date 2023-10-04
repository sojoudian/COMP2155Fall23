import paramiko
import time

sshClient = paramiko.SSHClient()

#to fix known issues with SSH we have to set the policy to auto add the keys
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshClient.connect(  hostname='192.168.25.129',username='albus',password='Dumbledore',port=22)

isSSHActive = sshClient.get_transport().is_active()
print(isSSHActive)
print("Successfully connected to the host")

shell = sshClient.invoke_shell()
shell.send("ls -l\n")
time.sleep(1)
respone = shell.recv(1000) #receive 5000 bytes
output = respone.decode('utf-8')
print(output)