from pClass import Connector

def main():
    host = input("Enter host: ")
    port = int(input("Enter port for ssh (default is 22): ") or 22)
    username= input("Enter username: ")
    pasword= input("Enter password: ")

    connection = Connector(host, username, pasword, port)

    while True:
        choice = input("\nOptions:\n1. Execute command\n2. Send file\n3. Exit\nChoose: ")
        if choice == "1":
            cmd=input("Enter command: ")
            print(connection.send_exec_command(cmd))
        elif choice == "2":
            local_path = input("Enter the local path: ")
            remote_path = input("Enter remote file path: ")
            connection.send_file(local_path, remote_path)
        elif choice == "3":
            break

if __name__ == "__main__":
    main()