from datetime import datetime
import threading
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_version(a_device):
    """Execute show version command using Netmiko."""
    try:
        remote_conn = ConnectHandler(**a_device)
        print("#" * 80)
        print(remote_conn.send_command_expect("show version"))
        print("#" * 80)
    except Exception as e:
        print(f"An error occurred with device {a_device['host']}: {e}")
    finally:
        remote_conn.disconnect()

def main():
    """
    Use threads and Netmiko to connect to each of the devices. Execute 'show version' on each device. Record the amount of time required to do this.
    """
    start_time = datetime.now()
    threads = []

    for a_device in devices:
        my_thread = threading.Thread(target=show_version, args=(a_device,))
        my_thread.start()
        threads.append(my_thread)

    for thread in threads:
        thread.join()

    elapsed_time = datetime.now() - start_time
    print("\nElapsed time: " + str(elapsed_time))

if __name__ == "__main__":
    main()
