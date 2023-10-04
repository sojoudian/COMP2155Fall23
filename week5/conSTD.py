import paramiko
import time

sshClient = paramiko.SSHClient()

#to fix known issues with SSH we have to set the policy to auto add the keys
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshClient.connect(  hostname='192.168.25.129',username='albus',password='Dumbledore',port=22)

stdin,stdout,stderr = sshClient.exec_command("ls -l")
# time.sleep(2)
stdin.close()
print(stdout.read().decode())