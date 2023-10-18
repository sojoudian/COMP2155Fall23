import paramiko
import time

class Connector:
    def __init__(self, host, username, password, port=22):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__port = port

        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client.connect(self.__host,  self.__port, self.__username, self.__password)

        self.__shell = self.__client.invoke_shell()

    def __del__(self):        
            self.__client.close()

    def send_shell_command(self, command):
            self.__shell.send(command + "\n")
            time.sleep(2)
            response = self.__shell.recv(10000)
            output = response.decode("utf-8")
            return output

    def send_exec_command(self, command):
        stdin, stdout, stderr = self.__client.exec_command(command+"\n")
        time.sleep(2)
        output = stdout.read().decode("utf-8")
        return output
