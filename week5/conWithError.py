import paramiko

sshClient = paramiko.SSHClient()

sshClient.connect(  hostname='192.168.25.129',username='albus',password='Dumbledore',port=22)


