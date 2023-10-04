import paramiko
import time
#the one with error
sshClient = paramiko.SSHClient()

sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(hostname='192.168.25.131', username='comp2155', password='COMP2155', port=22)
isSSHActivated = sshClient.get_transport().is_active()
print("Successful connected to the Linux server", isSSHActivated)

shell = sshClient.invoke_shell()
shell.send('ls -la\n')
# shell.send('apt install nmap -y\n')
time.sleep(8)
response = shell.recv(16384) #receive 16384 bytes
output = response.decode('utf-8')
print(output)





