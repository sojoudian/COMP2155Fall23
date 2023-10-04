import paramiko

sshClient = paramiko.SSHClient()

sshClient.connect(  hostname = '',username='',password='',port=22)