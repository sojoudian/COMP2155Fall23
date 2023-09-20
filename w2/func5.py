SSH_PORT=" 22 "

def checkSSHPort():
    print("SSH is healthy on port"+ SSH_PORT + "Status OK..")
    print()
    print("+++++++++++++++++++++++++++")

checkSSHPort()    
print()
print("SSH port is"+ SSH_PORT)
print("+++++++++++++++++++++++++++")


def webPortHC():
    WEB_PORT= "HTTP "
    print("Web server is running on " + WEB_PORT + "protocol.")
    print()
    print("+++++++++++++++++++++++++++")


webPortHC()
print()
# print("Web port is"+ WEB_PORT)
print("+++++++++++++++++++++++++++")