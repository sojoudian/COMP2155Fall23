import threading
import time

# A function that simulates a time-consuming task
def print_numbers(task_name):
    for i in range(1, 6):
        print(f"{task_name} prints: {i}")
        time.sleep(1)  # Simulating a delay

# Creating threads for two tasks
thread1 = threading.Thread(target=print_numbers, args=("Task 1",))
thread2 = threading.Thread(target=print_numbers, args=("Task 2",))

# Starting the threads
thread1.start()
thread2.start()

# Joining threads to wait for them to complete
thread1.join()
thread2.join()

print("Both tasks completed!")
