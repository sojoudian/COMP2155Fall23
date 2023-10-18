from pClass import Connector

# Create an instance of the Connector class
p = Connector(
              host="192.168.25.133",
              username="maziar",
              password="maziar",
              port=22
)

# Send a command to the remote host
resultOne = p.send_shell_command("whoami")
print(resultOne)
print("*"*90)

resultTwo = p.send_exec_command("ls")
print(resultTwo)