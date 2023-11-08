import time

start=time.perf_counter()

def test():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done sleeping")

test()

finish=time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")